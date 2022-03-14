#!/usr/bin/env python
# coding: utf-8

# In[1]:


from prose import Telescope

telescope_dict = dict(
    # Name(s)
    # -------
    name = "Unknown",
    names = [],

    # Keywords
    # --------
    keyword_telescope = "TELESCOP",
    keyword_object = "OBJECT",
    keyword_image_type = "IMAGETYP",
    keyword_light_images = "light",
    keyword_dark_images = "dark",
    keyword_flat_images = "flat",
    keyword_bias_images = "bias",
    keyword_observation_date = "DATE-OBS",
    keyword_exposure_time = "EXPTIME",
    keyword_filter = "FILTER",
    keyword_airmass = "AIRMASS",
    keyword_fwhm = "FWHM",
    keyword_seeing = "SEEING",
    keyword_ra = "RA",
    keyword_dec = "DEC",
    keyword_jd = "JD",
    keyword_bjd = "BJD",
    keyword_flip = "PIERSIDE",
    keyword_observation_time = None,

    # Units, formats and scales
    # -------------------------
    ra_unit = "deg",
    dec_unit = "deg",
    jd_scale = "utc",
    bjd_scale = "utc",
    mjd = 0,

    # Specs
    # -----
    trimming = (0, 0), # in piwel along y/x
    read_noise = 9, # in ADU
    gain = 1, # in e-/ADU
    altitude = 2000, # in meters
    diameter = 100, # in meters
    pixel_scale = None, # in arcseconds
    latlong = [None, None],
    saturation = 55000, # in ADU
    hdu = 0
)

telescope = Telescope(telescope_dict)

