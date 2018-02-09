from pyccl import ccllib as lib
from pyccl import constants as const
from pyccl.pyutils import _cosmology_obj, check
import numpy as np


def pk2xi(k, pk):
    """
    Convert 3D power spectrum to 3D correlation function

    Args:
        k (array_like): Array of wavenumbers (arbitrary units)
        pk (array_like): power spectrum at k

    Returns:
        r (array_like): array of distances (inverse units of k)
        xi (array_like): correlation function

    """

    assert (k.shape==pk.shape)
    status = 0
    r,xi,status=lib.pk2xi_(k,pk,len(k), len(pk),status)
    check(status)
    return r,xi

def xi2pk(r, xi):
    """
    Convert 3D power spectrum to 3D correlation function

    Args:
        k (array_like): Array of wavenumbers (arbitrary units)
        pk (array_like): power spectrum at k

    Returns:
        r (array_like): array of distances (inverse units of k)
        xi (array_like): correlation function

    """

    assert (r.shape==xi.shape)
    status = 0
    k,pk,status=lib.xi2pk_(r,xi,len(r), len(xi),status)
    check(status)
    return k,pk
