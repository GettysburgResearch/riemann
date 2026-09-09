#!/usr/bin/env python3
"""Optional NON_DIRECTED_HIGH_PRECISION checks of continuous-kernel asymptotics.
This script evaluates no large prime/Mobius sum and is not an acceptance dependency.
"""
from __future__ import annotations
import json
from pathlib import Path
import mpmath as mp

mp.mp.dps = 90


def tail_values(N, U):
    """Use a forward polynomial recurrence independent of the saddle approximation."""
    prev_l, cur_l = mp.mpf(0), mp.mpf(1)
    cur_p = mp.mpf(2)
    result = [cur_p]
    for n in range(1, N+1):
        next_l = ((2*n-1-2*U)*cur_l-(n-1)*prev_l)/n
        cur_p = -3*cur_p+2*(next_l-cur_l)
        result.append(cur_p)
        prev_l, cur_l = cur_l, next_l
    return [x*mp.exp(-U/2) for x in result]


def main():
    saddle = []
    for c in [mp.mpf(4), mp.mpf(8)]:
        p = c-1-mp.sqrt(c*(c-2))
        beta = (1-p)/(1+p)
        psi = -mp.log(p)-c*(1-3*p)/(2*(1+p))
        for N in [50, 200, 800]:
            vals = tail_values(N, c*N)
            leading = 2*mp.exp(N*psi)/((1-3*p)*mp.sqrt(2*mp.pi*beta*N))
            vector_leading = leading/mp.sqrt(1-p*p)
            saddle.append({
                'c': str(c), 'degree': N,
                'scalar_exact_over_leading': mp.nstr((-1)**N*vals[-1]/leading, 22),
                'vector_exact_over_leading': mp.nstr(mp.sqrt(mp.fsum(v*v for v in vals))/vector_leading, 22),
            })
    gaussian = []
    for N in [50, 200, 800]:
        for z in [-1, 0, 1]:
            U = mp.mpf(8)*N/3+z*mp.sqrt(mp.mpf(32)*N/9)
            ratio = (-1)**N*tail_values(N, U)[-1]/(2*mp.mpf(3)**N)
            normal = mp.erfc(mp.mpf(z)/mp.sqrt(2))/2
            gaussian.append({'degree': N, 'z': z,
                             'tail_fraction': mp.nstr(ratio, 22),
                             'normal_tail': mp.nstr(normal, 22)})
    data = {'arithmetic': 'NON_DIRECTED_HIGH_PRECISION', 'digits': mp.mp.dps,
            'proof_dependency': False, 'actual_arithmetic_sum': False,
            'saddle_checks': saddle, 'gaussian_checks': gaussian}
    print(json.dumps(data, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
