project = "pagestest"
copyright = "2026, Elias Mende"
author = "Elias Mende"
release = "0.1.0"
html_title = "Testing GitHUb Pages"

root_doc = "index"

extensions = [
    "myst_nb",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "autoapi.extension",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = ["dollarmath", "colon_fence"]
nb_execution_mode = "off"

autoapi_dirs = ["../src"]
autoapi_root = "reference"
autoapi_add_toctree_entry = False
autoapi_keep_files = True
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
]

html_theme = "furo"
