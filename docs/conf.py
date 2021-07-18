# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# from datetime import datetime
import os
import sys

import brainspace
brainspace.OFF_SCREEN = True  # off screen rendering for examples

# -- Project information -----------------------------------------------------

project = 'surfplot'
author = 'Dan Gale'
copyright = '2021, surfplot developers'

# The full version, including alpha/beta/rc tags
release = '0.0.1c'

# Import project to get version info
sys.path.insert(0, os.path.abspath(os.path.pardir))
import surfplot  # noqa
# The short X.Y version
version = surfplot.__version__
# The full version, including alpha/beta/rc tags
release = surfplot.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxarg.ext',
    'sphinx_gallery.gen_gallery',
    'matplotlib.sphinxext.plot_directive',
]

# Generate the API documentation when building
autosummary_generate = True
autodoc_default_options = {'members': True, 'inherited-members': True}
numpydoc_show_class_members = False
autoclass_content = "class"

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_param = True
napoleon_use_ivar = True
napoleon_use_rtype = False

napoleon_include_private_with_doc = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import sphinx_rtd_theme  # noqa
html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# CSS files to include
html_css_files = ['theme_overrides.css']

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'surfplotdoc'

# -- Extension configuration -------------------------------------------------
intersphinx_mapping = {
    'brainspace': ('https://brainspace.readthedocs.io/en/latest/', None),
    'brainnotation': ('https://netneurolab.github.io/brainnotation/', None)
}

from brainspace.plotting.sphinx_gallery_scrapper import _get_sg_image_scraper
from sphinx_gallery.sorting import FileNameSortKey
sphinx_gallery_conf = {
    'examples_dirs': '../tutorials', 
    'gallery_dirs': 'auto_examples',
    'thumbnail_size': (250, 250),
    # 'plot_gallery': 'False',
    'image_scrapers': ('matplotlib'),
    'within_subsection_order': FileNameSortKey,
    'download_all_examples': False,  
}

# sphinx_gallery_conf = {
#     'doc_module': 'surfplot',
#     'backreferences_dir': os.path.join('generated', 'modules'),
#     'reference_url': {
#         'surfplot': None
#     },
#     'thumbnail_size': (250, 250),
#     'ignore_pattern': r'/wip.*\.py',
# }

doctest_global_setup = """\
import numpy as np
np.random.seed(1234)\
"""