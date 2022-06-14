.. prose documentation master file, created by
   sphinx-quickstart on Mon Apr 27 15:15:45 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


.. role:: underline
    :class: underline

   
.. image:: prose_illustration.png
   :width: 350
   :align: center
   
.. raw:: html

   <p align="center">
   A python framework to build FITS images pipelines.
   <br>
   <p align="center">
      <a href="https://github.com/lgrcia/prose">
         <img src="https://img.shields.io/badge/github-lgrcia/prose-blue.svg?style=flat" alt="github"/>
      </a>
      <a href="">
         <img src="https://img.shields.io/badge/license-MIT-lightgray.svg?style=flat" alt="license"/>
      </a>
      <a href="https://arxiv.org/abs/2111.02814">
         <img src="https://img.shields.io/badge/paper-yellow.svg?style=flat" alt="paper"/>
      </a>
      <a href="https://lgrcia.github.io/prose-docs">
         <img src="https://img.shields.io/badge/documentation-black.svg?style=flat" alt="documentation"/>
      </a>
   </p>
   </p>


|prose| is a Python tool to build pipelines dedicated to astronomical images processing (all based on pip packages 📦). Beyond providing all the blocks to do so, it features default pipelines to perform common tasks such as automated calibration, reduction and photometry.


.. toctree::
   :caption: References
   :maxdepth: 1

   installation.md
   notebooks/quickstart.ipynb
   core
   blocks
   api
   

.. toctree::
   :caption: Tutorials
   :maxdepth: 1

   notebooks/tutorials/fits_manager.ipynb
   notebooks/tutorials/photometry.ipynb
   notebooks/tutorials/reports.ipynb
   notebooks/tutorials/custom_block.ipynb
   notebooks/tutorials/modeling.ipynb
   .. notebooks/neb.ipynb
   notebooks/tutorials/archival.ipynb

.. toctree::
   :caption: Case studies 🔭
   :maxdepth: 1

   notebooks/case_studies/diagnostic_video.ipynb
   .. notebooks/case_studies/gaia_photometry.ipynb
   
.. toctree::
   :caption: Notes
   :maxdepth: 1

   notebooks/phot.ipynb
   notebooks/extra.ipynb


.. image:: lookatit.png
   :width: 150
   :align: center