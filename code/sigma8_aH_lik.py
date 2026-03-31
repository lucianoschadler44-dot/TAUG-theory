import numpy as np
from scipy.interpolate import interp1d

# sigma8(alphaH) scan — EFTCAMB P(k) integral R=8 Mpc/h
# alphaH_eff = MP0 / 0.112
_aH = np.array([0.0, 0.0714, 0.0982, 0.1250, 0.1518, 0.1786,
                 0.2286, 0.4696, 0.5955, 0.7241, 0.9920])
_s8 = np.array([0.8121, 0.7837, 0.7733, 0.7630, 0.7529, 0.7430,
                 0.7242, 0.6448, 0.6082, 0.5733, 0.5090])
_s8f = interp1d(_aH, _s8, kind='linear', fill_value='extrapolate')

# DES Y3 + KiDS-1000 + HSC combinado
_s8_obs = 0.763
_s8_err = 0.020

def sigma8_aH_logp(alpha_H):
    s8 = float(_s8f(np.clip(alpha_H, 0.0, 1.0)))
    return -0.5 * ((s8 - _s8_obs) / _s8_err)**2
