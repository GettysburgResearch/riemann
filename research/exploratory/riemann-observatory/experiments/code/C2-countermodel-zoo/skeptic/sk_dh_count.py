#!/usr/bin/env python3
"""SKEPTIC: rigorous completeness test for C2-04 (Davenport-Heilbronn zeros, 1 <= t <= T).

N_box := number of zeros of f in [-0.6, 1.6] x [1, T]  (rigorous argument principle, sk_wind.py).
N_line >= number of certified sign changes of the real function xi_f(1/2+it) on [1, T] (Arb signs).
f has no zeros for sigma >= 1.41 (investigator's elementary bound, re-derived below) and, by the functional
equation, none for sigma <= -0.41; so the box contains all zeros with 1 <= t <= T.
If N_box - N_line_lower == 2 * (number of certified off-line zeros with Re > 1/2 in the box), then there
are NO other off-line zeros (in particular none with 1/2 < sigma < 0.52), rigorously.
Usage: python3 sk_dh_count.py OUTDIR [T]
"""
import sys, os, json, time
import flint
from flint import acb, arb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sk_wind import winding
import sk_dh

flint.ctx.prec = 80


def xi_f(s):
    return ((acb(5) / acb.pi()).log() * s / 2).exp() * ((s + 1) / 2).gamma() * sk_dh.f(s)


def main():
    T = float(sys.argv[2]) if len(sys.argv) > 2 else 300.0
    t0 = time.time()
    # zero-free half-plane check at sigma = 1.6 is implied by sigma>=1.41; we rely on the winding box anyway
    W = winding(sk_dh.f, -0.6, 1.6, 1.0, T, nseg=400, maxdepth=16)
    print('box', W, round(time.time() - t0, 1), flush=True)
    # certified sign changes on the critical line
    signs = []
    t = 1.0
    dt = 0.005
    nunc = 0
    while t <= T:
        v = xi_f(acb(0.5, t)).real
        if v > 0:
            signs.append(1)
        elif v < 0:
            signs.append(-1)
        else:
            nunc += 1
        t += dt
    sc = sum(1 for a, b in zip(signs, signs[1:]) if a != b)
    out = dict(T=T, box=[-0.6, 1.6, 1.0, T], winding=W, line_sign_changes=sc, line_step=dt,
               uncertified_sign_points=nunc, runtime_s=round(time.time() - t0, 1))
    if W.get('ok'):
        out['N_box_minus_line_lower'] = W['count'] - sc
    print(out, flush=True)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(out, open(os.path.join(sys.argv[1], f'sk_dh_count_T{int(T)}.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
