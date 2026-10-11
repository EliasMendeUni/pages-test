import numpy as np

from .PointSet import PointSet


class Pointprocess:
    """
    Definition of a point process in a periodic square box.

    Parameters
    ----------
    box : float
        Side length of the box.
    spacing : float
        Mean distance between neighbouring points.
    """

    def __init__(self, box, spacing):
        self.box = float(box)
        self.spacing = float(spacing)
        self.n_per_side = int(round(self.box / self.spacing))

    def rect_lattice(self, noise=0.0, seed=None):
        """
        Square lattice with optional uniform noise.

        Parameters
        ----------
        noise : float
            Maximum displacement in units of the spacing, drawn uniformly
            from [-noise/2, noise/2].
        seed : int, optional
            Random seed for reproducibility.

        Returns
        -------
        PointSet
        """
        rng = np.random.default_rng(seed)
        g = np.arange(self.n_per_side) * self.spacing
        x, y = np.meshgrid(g, g)
        positions = np.column_stack([x.ravel(), y.ravel()])
        half = noise * self.spacing / 2
        positions = positions + rng.uniform(-half, half, positions.shape)
        return PointSet(np.mod(positions, self.box), self.box)

    def poisson(self, seed=None):
        """
        Uncorrelated (Poisson) points with the same density as the lattice.

        Parameters
        ----------
        seed : int, optional
            Random seed for reproducibility.

        Returns
        -------
        PointSet
        """
        rng = np.random.default_rng(seed)
        n = self.n_per_side**2
        return PointSet(rng.uniform(0.0, self.box, (n, 2)), self.box)
