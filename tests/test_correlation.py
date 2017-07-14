#if CCL not in python path
import sys
sys.path.insert(0, '../')
import numpy as np
import pylab as plt
import pyccl as ccl

cosmo = ccl.Cosmology(Omega_c=0.27, Omega_b=0.045, h=0.67, sigma8=0.83, n_s=0.96)

z = np.linspace(0., 3., 200)
i_lim = 26. # Limiting i-band magnitude
z0 = 0.0417*i_lim - 0.744

Ngal = 46. * 100.31 * (i_lim - 25.) # Normalisation, galaxies/arcmin^2
pz = 1./(2.*z0) * (z / z0)**2. * np.exp(-z/z0) # Redshift distribution, p(z)
dNdz = Ngal * pz # Number density distribution
b = 1.5*np.ones(200)

lens1 = ccl.ClTracerLensing(cosmo, False, z=z, n=dNdz)
clu1 = ccl.ClTracerNumberCounts(cosmo, False, False, n=(z,dNdz), bias=(z,b))

bias_ia = -0.01* np.ones(z.size) # Intrinsic alignment bias factor
f_red = 0.2 * np.ones(z.size) # Fraction of red galaxies
lens1_ia = ccl.ClTracerLensing(cosmo, True, z=z, n=dNdz, bias_ia=bias_ia, f_red=f_red)

ell = np.arange(2, 1000)
cls = ccl.angular_cl(cosmo, lens1, lens1, ell)
cls_ia = ccl.angular_cl(cosmo, lens1_ia, lens1_ia, ell)
cls_clu = ccl.angular_cl(cosmo, clu1, clu1, ell)

theta_deg = np.logspace(-1, np.log10(5.), 20) # Theta is in degrees

xi_plus = ccl.correlation(cosmo, ell, cls, theta_deg, corr_type='L+', method='FFTLog')
xi_plus_ia = ccl.correlation(cosmo, ell, cls_ia, theta_deg, corr_type='L+', method='FFTLog')
xi_minus = ccl.correlation(cosmo, ell, cls, theta_deg, corr_type='L-', method='FFTLog')

xi_clu = ccl.correlation(cosmo, ell, cls_clu, theta_deg, corr_type='GG', method='Legendre')

