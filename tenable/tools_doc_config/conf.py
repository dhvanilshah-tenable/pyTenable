# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

# import tenable  # noqa: E402

autodoc_mock_imports = [
    'lxml',
    'dateutil',
    'dateutil.parser',
    'semver',
    'docker',
    'defusedxml',
    'ipaddress',
    'arrow',
    'tenable.io'
]


def setup(app):
    app.connect('autodoc-skip-member', autodoc_skip_member)
    app.connect('autodoc-process-signature', pretty_signature)
    app.add_css_file('custom.css')


# -- Project information -----------------------------------------------------


project = u'pyTenable'
year = datetime.datetime.now().year
copyright = u'{}, Tenable, Inc.'.format(year)
author = u'Tenable, Inc.'

# The short X.Y version
# version = tenable.__version__
# The full version, including alpha/beta/rc tags
# release = version

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
]

autosummary_generate = True

# Skip documenting class/module variables/constants in HTML pages
def autodoc_skip_member(app, what, name, obj, skip, options):
    if what in ('class', 'module'):
        if ('class' in str(obj)) or ('module' in str(obj)) or ('function' in str(obj)):
            pass
        else:
            skip = True
    return skip

# Suppress variable expression (i.e. x='abc') in function/class/method declaration
def pretty_signature(app, what, name, obj, options, signature, return_annotation):
    if what not in ('function', 'method', 'class'):
        return

    if signature is None:
        return

    import inspect
    module_name = inspect.getmodule(obj)

    new_signature = signature
    # Get all-caps names with no leading underscore
    global_names = [name for name in dir(module_name) if name.isupper() if name[0] != '_']
    # Get only names of variables with distinct values
    names_to_replace = [name for name in global_names
                        if [module_name.__dict__[n] for n in global_names].count(module_name.__dict__[name]) == 1]
    # Substitute name for value in signature, including quotes in a string value
    for variable_name in names_to_replace:
        var_value = module_name.__dict__[variable_name]
        value_string = str(var_value) if type(var_value) is not str else "'{0}'".format(var_value)
        new_signature = new_signature.replace(value_string, variable_name)

    return new_signature, return_annotation

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'build', "_static", "logs"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "default"
pygments_dark_style = "monokai"

add_module_names = False
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'classic'
html_show_sphinx = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_logo = '_static/logo.png'
html_theme_options = {
    'sidebar_hide_name': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyTenabledoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pyTenable.tex', u'pyTenable Documentation',
     u'Steven McGrath', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pytenable', u'pyTenable Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyTenable', u'pyTenable Documentation',
     author, 'pyTenable', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'https://docs.python.org/': None,
    'requests': ('https://requests.readthedocs.io/en/master/', None),
    'restfly': ('https://restfly.readthedocs.io/en/latest/', None),
    'box': ('https://box.readthedocs.io/en/latest', None),
}

extlinks = {
    'devportal': ('https://developer.tenable.com/reference/%s', 'devportal'),
    'sc-api': ('https://docs.tenable.com/sccv/api/%s', 'sc-api'),
    'requests': ('https://requests.readthedocs.io/en/master/%s', 'requests'),
}
