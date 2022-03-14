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

from sphinx.ext.autosummary import Autosummary
from sphinx.ext.autosummary import get_documenter
from docutils.parsers.rst import directives
from sphinx.util.inspect import safe_getattr
import re

class AutoAutoSummary(Autosummary):

    option_spec = {
        'methods': directives.unchanged,
        'attributes': directives.unchanged
    }

    required_arguments = 1

    @staticmethod
    def get_members(obj, typ, include_public=None):
        if not include_public:
            include_public = []
        items = []
        for name in dir(obj):
            try:
                documenter = get_documenter(safe_getattr(obj, name), obj)
            except AttributeError:
                continue
            if documenter.objtype == typ:
                items.append(name)
        public = [x for x in items if x in include_public or not x.startswith('_')]
        return public, items

    def run(self):
        clazz = str(self.arguments[0])
        try:
            (module_name, class_name) = clazz.rsplit('.', 1)
            m = __import__(module_name, globals(), locals(), [class_name])
            c = getattr(m, class_name)
            if 'methods' in self.options:
                _, methods = self.get_members(c, 'method', ['__init__'])

                self.content = ["~%s.%s" % (clazz, method) for method in methods if not method.startswith('_')]
            if 'attributes' in self.options:
                _, attribs = self.get_members(c, 'attribute')
                self.content = ["~%s.%s" % (clazz, attrib) for attrib in attribs if not attrib.startswith('_')]
        finally:
            return super(AutoAutoSummary, self).run()

def setup(app):
    app.add_directive('autoautosummary', AutoAutoSummary)