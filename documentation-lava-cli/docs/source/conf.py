# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Linaro LAVA CLI'
copyright = '2026 Linaro'
author = 'Philip Colmer'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Show TODO entries in the rendered output so that documentation gaps
# (e.g. missing example command output) are visible until they are filled in.
todo_include_todos = True

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
