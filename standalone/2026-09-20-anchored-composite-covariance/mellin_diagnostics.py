#!/usr/bin/env python3
"""Optional finite-band FLOATING diagnostics. Never an interval certificate."""
from __future__ import annotations
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import mpmath as mp
from verify_mellin_dense import cutoff, diagonal_polynomial, sf_completion


def evaluate(poly, ts):
    ns = np.asarray(sorted(poly), dtype=float)
    coeff = np.asarray([float(poly[int(n)]) for n in ns]) / np.sqrt(ns)
    logs = np.log(ns)
    result = np.empty(len(ts), dtype=complex)
    for start in range(0, len(ts), 2048):
        block = ts[start:start+2048]
        result[start:start+len(block)] = np.exp(-1j*block[:,None]*logs[None,:]) @ coeff
    return result


def simpson(vals, step):
    if (len(vals)-1) % 2:
        raise ValueError('Simpson requires an even number of cells')
    return float(step/3*(vals[0]+vals[-1]+4*np.sum(vals[1:-1:2])+2*np.sum(vals[2:-1:2])))


def main():
    ys = (15, 31, 63, 127)
    panels = []
    unit = 64
    max_t = 4*cutoff(max(sf_completion(max(ys))))
    ts = np.arange(max_t*unit+1, dtype=float)/unit
    zeta = np.asarray([mp.fp.zeta(complex(.5, float(t))) for t in ts])
    spots = []
    mp.mp.dps = 60
    for t in (0, .125, 3, 14.125, 30, 66, 148, 337, 1000):
        ordinary = mp.fp.zeta(complex(.5,t))
        high = complex(mp.zeta(mp.mpc('.5',str(t))))
        spots.append({'t': t, 'absolute_fp_vs_60digit_difference': abs(ordinary-high)})
    for y in ys:
        c = sf_completion(y)
        length = max(c)
        cut = cutoff(length)
        end = 4*cut
        grid = ts[:end*unit+1]
        cp = evaluate(c, grid)**2
        dp = evaluate(diagonal_polynomial(c), grid)
        op = cp-dp
        factor = abs(zeta[:len(grid)])**2 / (np.pi*(.25+grid**2))
        vals = {'P': factor*abs(cp)**2, 'D': factor*abs(dp)**2,
                'O': factor*abs(op)**2,
                'twice_covariance_D_O': factor*2*np.real(dp*np.conjugate(op))}
        bands = []
        for a,b in ((0,cut),(cut,end)):
            energies = {}
            diffs = {}
            for key,value in vals.items():
                fine = value[a*unit:b*unit+1]
                energies[key] = simpson(fine, 1/unit)
                diffs[key] = abs(energies[key]-simpson(fine[::2],2/unit))
            bands.append({'positive_t_interval': [a,b], 'both_signs_included': True,
                          'floating_energy': energies,
                          'absolute_mesh_difference': diffs,
                          'covariance_identity_residual': energies['P']-energies['D']-energies['O']-energies['twice_covariance_D_O']})
        panels.append({'Y': y, 'L': length, 'T_L': cut, 'finite_bands': bands})
    print(json.dumps({'status': 'DESCRIPTIVE_FLOATING_FINITE_BANDS_NOT_CERTIFICATES',
        'packet': 'DMC31', 'numpy_version': np.__version__, 'mpmath_version': mp.__version__,
        'method': 'Composite Simpson steps 1/64 and 1/32; real-source symmetry includes both signs of t.',
        'limits': 'No quadrature error enclosure. Nothing beyond 4*T_L evaluated. Not part of exact acceptance.',
        'zeta_spot_comparisons': spots, 'panels': panels}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
