import ccllib as lib
import constants as const
from pyutils import _cosmology_obj, check
import numpy as np

correlation_methods = {
    'fftlog_projected':   const.CCL_CORR_FFTLOG_PROJECTED,
    'fftlog':   const.CCL_CORR_FFTLOG_PROJECTED, #default option for fftlog
    'fftlog_3d':   const.CCL_CORR_FFTLOG_3D,
    'bessel':   const.CCL_CORR_BESSEL,
    'legendre': const.CCL_CORR_LGNDRE,
}

correlation_types = {
    'gg': const.CCL_CORR_GG,
    'gl': const.CCL_CORR_GL,
    'l+': const.CCL_CORR_LP,
    'l-': const.CCL_CORR_LM,
}

correlation_space = {
    'ang': const.CCL_CORR_ANG,
    'angular': const.CCL_CORR_ANG,
    'l': const.CCL_CORR_ANG,
    'ell': const.CCL_CORR_ANG,
    'phys': const.CCL_CORR_PHYS,
    'physical': const.CCL_CORR_PHYS,
    'k': const.CCL_CORR_PHYS
}

def correlation(cosmo, ell, C_ell, theta, corr_type='gg',corr_space='ang', method='fftlog'):
    """
    Compute the angular correlation function.

    Args:
        cosmo (:obj:`Cosmology`): A Cosmology object.
        ell (array_like): Multipoles corresponding to the input angular power spectrum
        C_ell (array_like): Input angular power spectrum.
        theta (float or array_like): Angular separation(s) at which to calculate the angular correlation function (in degrees).
        corr_type (string): Type of correlation function. Choices: 'GG' (galaxy-galaxy), 'GL' (galaxy-shear), 'L+' (shear-shear, xi+), 'L-' (shear-shear, xi-).
        method (string, optional): Method to compute the correlation function. Choices: 'Bessel' (direct integration over Bessel function), 'FFTLog' (fast integration with FFTLog), 'Legendre' (brute-force sum over Legendre polynomials).
    Returns:
        Value(s) of the correlation function at the input angular separation(s).
    """

    cosmo = _cosmology_obj(cosmo)
    status = 0
    # Convert to lower case
    corr_type = corr_type.lower()
    method = method.lower()
    corr_space=corr_space.lower()

    if corr_type not in correlation_types.keys():
        raise KeyError("'%s' is not a valid correlation type." % corr_type)

    if method.lower() not in correlation_methods.keys():
        raise KeyError("'%s' is not a valid correlation method." % method)

    if corr_space not in correlation_space.keys():
        raise KeyError("'%s' is not a valid correlation space." % corr_space)

    # Convert scalar input into an array
    scalar = False
    if isinstance(theta, float):
        scalar = True
        theta = np.array([theta,])

    # Call correlation function
    wth, status = lib.correlation_vec(cosmo, ell, C_ell, theta,
                                      correlation_types[corr_type],
                                      correlation_space[corr_space],
                                      correlation_methods[method],
                                      len(theta),status)
    check(status)
    if scalar: return wth[0]
    return wth
