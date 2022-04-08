# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Photometry from gaia coordinates
#
# In this case study, we will build the lightcurves of some gaia stars present in the field, based on sky coordinates. Unlike previous tutorial, we will not use the pre-built `Claibration` and `AperturePhotometry` pipelines but do it from sratch.
#
# Here is the strategy for our pipeline:
# - Query reference gaia stars in the reference image
# - Align all images to this reference image
# - Perform aperture photometry based on the reference stars positions

# ## Getting our images

from prose import FitsManager

fm = FitsManager("/Users/lgrcia/data/20220405")
print(fm)

# ## Picking a reference image
#
# To align images we will select a reference image to work with. Generally one from the middle of your observation is good enough. 

# <div class="alert alert-info">
#
# While it is for applications in difference imaging, I noticed [this paper](https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.1836W/abstract) about reference selection
# </div>

# +
from prose import Image

files = fm.observation_files(0)
ref = Image(files['images'][100])
# -

# We will build a sequence to calibrate the image and detect the reference stars. This sequence can be reused later to calibrate the other images

# +
from prose import Sequence, blocks

calibration = Sequence([
    blocks.Calibration(files['darks'], files['flats'], files['bias']),
    blocks.Trim(),
    blocks.SegmentedPeaks(n_stars=15), # low number of stars usually enough for alignment
    blocks.detection.LimitStars()
])

calibration.run(ref)
ref.show()
# -

# <div class="alert alert-info">
# Since our telescope is set, trimming dimensions don't need to be specified. Which is why the `Trim` block has no kwargs
# </div>

# ## Detecting Gaia stars
#
# Since our strategy is to rely on reference gaia stars, let's find them in the reference image

# +
gaia = Sequence([
    blocks.catalogs.PlateSolve(),
    blocks.catalogs.GaiaCatalog(n_stars=50, mode="replace")
])

gaia.run(ref)
ref.show()
# -

# ## The reduction sequence
#
# We can now build the complete reduction sequence

# +
reduction = Sequence([
    *calibration,                                      # the simple calibration sequence previously built 
    blocks.Twirl(ref.stars_coords),                    # compute the transformation from reference stars
    blocks.Cutouts(),                                  # 
    blocks.MedianPSF(),                                # PSF building and analysis
    blocks.Moffat2D(),                                 #
    blocks.Set(stars_coords=ref.stars_coords),         # setting stars to the reference ones
    # and transform them to match reference
    blocks.AffineTransform(stars=True, data=False, inverse=True),
    blocks.BalletCentroid(),                           # stars centroiding
    blocks.PhotutilsAperturePhotometry(),              # photometry
    
    # Retrieving data from images in a conveniant way
    blocks.XArray(
        (("time"), "jd_utc"),
        (("time", "apertures", "star"), "fluxes"),
        (("time", "apertures", "star"), "errors"),
    ),
])

reduction.run(files['images'])
# -

# ## Getting the light curves

# In order to instantiate an `Observation` object, we need to retrieve the data from this sequence, mostly stored in the `XArray` block

# +
from prose import utils

xarr = reduction[-1].xarray # where the data lie
xarr = utils.image_in_xarray(ref, xarr, stars=True) # adding reference as a stack
xarr = xarr.transpose("apertures", "star", "time", ...) # ... just needed
# -

# We can now instantiate an `Observation` object and build light-curves as we want

# +
from prose import Observation

obs = Observation(xarr)
obs.show_stars()

# +
import matplotlib.pyplot as plt

obs.target = 1 # for example
obs.broeg2005()
obs.plot()

plt.ylim(0.98, 1.02)
