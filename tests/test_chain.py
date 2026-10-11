import numpy as np
import pytest

from pagestest import Pointprocess


@pytest.mark.parametrize("seed", range(5))
def test_rect_lattice_chain(seed):
    rng = np.random.default_rng(seed)
    n = int(rng.integers(5, 12))
    spacing = 2.0 ** int(rng.integers(-2, 2))
    msg = f"seed={seed}, n={n}, spacing={spacing}"

    points = Pointprocess(box=n * spacing, spacing=spacing).rect_lattice()

    assert points.n == n * n, msg
    assert points.dmean == pytest.approx(spacing), msg
    assert np.all(points.positions >= 0), msg
    assert np.all(points.positions < points.box), msg


def test_structure_factor_of_lattice_has_bragg_peaks():
    points = Pointprocess(box=4.0, spacing=1.0).rect_lattice()
    g = 2 * np.pi

    peaks = points.structure_factor(np.array([[0.0, 0.0], [g, 0.0], [g, g]]))
    assert peaks == pytest.approx(16.0)

    off_peak = points.structure_factor(np.array([[g / 2, 0.0]]))
    assert off_peak == pytest.approx(0.0, abs=1e-9)
