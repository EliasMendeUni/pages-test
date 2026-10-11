"""
pagestest: a tiny stand-in for TOSTADA used to test the documentation workflow.
"""
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _pkg_version

try:
    __version__ = _pkg_version("pagestest")
except PackageNotFoundError:
    __version__ = "0.0.0+unknown"

# Module and class share a name on purpose, like in TOSTADA (PointDistribution).
from .PointSet import PointSet  # noqa: F401
from .pointprocess import Pointprocess  # noqa: F401
