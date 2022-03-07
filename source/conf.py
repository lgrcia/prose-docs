# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

import os
import sys

sys.path.insert(0, os.path.abspath("../prose"))


# -- Project information -----------------------------------------------------

project = 'prose'
copyright = '2022, Lionel Garcia'
author = 'Lionel Garcia'

extensions = [
    'sphinx.ext.autodoc', 
    'sphinx.ext.napoleon', 
    'sphinx.ext.autosummary',
    'sphinx_copybutton', 
    'nbsphinx',
    'jupyter_sphinx'
    ]

master_doc = 'index'
exclude_patterns = ['_build', '**.ipynb_checkpoints']
source_suffix = {'.rst': 'restructuredtext'}

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"

html_theme = "prosedoc"
html_theme_path = ["."]

#html_theme_options = {"display_version": True}
#html_static_path = ["_static"]
#html_css_files = ["css/style.css"]
#html_style = "css/style.css"
pygments_style = "friendly"

napoleon_numpy_docstring = True
napoleon_use_param = False


nbsphinx_execute = 'never'
autodoc_member_order = 'bysource'


rst_prolog = """
.. |prose| replace:: *prose*
.. _photutils: https://photutils.readthedocs.io/en/stable/
.. _scikit-image: https://scikit-image.org/

.. role:: blockread
.. |read| replace:: :blockread:`reads`

.. role:: blockwrite
.. |write| replace:: :blockwrite:`writes`

.. role:: blockmodify
.. |modify| replace:: :blockmodify:`modifies data`

"""

templates_path = ["prosedoc"]