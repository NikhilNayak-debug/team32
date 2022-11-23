# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Fab-AD'
copyright = '2022, Saket Joshi <saket_joshi@g.harvard.edu> , Nishtha Sardana <>, Nikhil Nayak <>, Sree Harsha Tanneru <>, Kareema Batool <>'
author = 'Saket Joshi <saket_joshi@g.harvard.edu> , Nishtha Sardana <>, Nikhil Nayak <>, Sree Harsha Tanneru <>, Kareema Batool <>'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./src/fab_ad'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.coverage', 'numpydoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
