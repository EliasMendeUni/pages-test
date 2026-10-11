# pagestest

A tiny stand-in for TOSTADA, used to try out the documentation workflow
(Sphinx on GitHub Pages) before applying it to the real project.

<!-- install-start -->
## Installation

Create an environment and install the package in editable mode:

```bash
conda create -n pages-test python=3.12 -y
conda activate pages-test
pip install -e ".[dev]"
```

Add the documentation tools with `pip install -e ".[docs]"`.
<!-- install-end -->

## Tests

```bash
pytest
```
