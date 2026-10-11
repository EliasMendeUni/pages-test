import numpy as np


class PointSet:
    """
    A set of points in a periodic square 2D box.

    Parameters
    ----------
    positions : N x 2 ndarray
        Positions of the points.
    box : float
        Side length of the square box.
    """

    def __init__(self, positions, box):
        self.positions = np.asarray(positions, dtype=float)
        self.box = float(box)
        self.n = self.positions.shape[0]
        self.density = float(self.n / self.box**2)
        self.dmean = float(1.0 / np.sqrt(self.density))

    def structure_factor(self, k):
        r"""
        Structure factor of the point set.

        .. math::

            S(\mathbf{k}) = \frac{1}{N} \left| \sum_j e^{i \mathbf{k} \cdot \mathbf{r}_j} \right|^2

        Parameters
        ----------
        k : ndarray
            Wave vectors of shape (M, 2).

        Returns
        -------
        ndarray
            :math:`S(k)` for every wave vector, shape (M,).
        """
        k = np.atleast_2d(k)
        phase = self.positions @ k.T
        amplitude = np.exp(1j * phase).sum(axis=0)
        return np.abs(amplitude) ** 2 / self.n
