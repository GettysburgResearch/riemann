#!/usr/bin/env python3
"""C2 countermodel zoo -- zeros of partial sums zeta_N(s) = sum_{n<=N} n^{-s} in Re s > 1.

Background (IMPORTED): Turan showed that if zeta_N(s) != 0 for sigma > 1 for all large N then RH holds;
Montgomery (1983) showed zeta_N has zeros in sigma > 1 + (4/pi - 1 - eps) log log N / log N for N >= N0(eps);
Platt & Trudgian (LMS J. Comput. Math. 19 (2016) 37-41): no zeros in sigma > 1 for 1 <= N <= 18 and N = 20, 21, 28,
infinitely many for every other N.
This script: NON-RIGOROUS numpy screen of |zeta_19(1+it)| on 0 <= t <= T_MAX (step dt), Newton polishing of
the smallest local minima, and RIGOROUS Arb Krawczyk certificates; reports the certified zeros with Re s > 1.
Usage: python3 partial_sums.py OUTDIR [N] [T_MAX]
"""
import sys, os, json, time, hashlib
import numpy as np
import flint
from flint import acb, arb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_common import certify_zero, newton_polish, versions

flint.ctx.prec = 128


def make_fd(N):
    logs = [acb(n).log() for n in range(1, N + 1)]

    def fd(z):
        f, d = acb(0), acb(0)
        for L in logs:
            e = (-z * L).exp()
            f += e
            d -= L * e
        return f, d
    return fd


def main():
    outdir = sys.argv[1]
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 19
    T_MAX = float(sys.argv[3]) if len(sys.argv) > 3 else 2e6
    dt, thresh, chunk = 0.05, 0.03, 1e5
    t0 = time.time()
    n = np.arange(1, N + 1); ln = np.log(n); amp = n ** -1.0
    mins = []
    for T0 in np.arange(0, T_MAX, chunk):
        t = np.arange(T0, T0 + chunk, dt)
        F = np.zeros(t.size, complex)
        for a, l in zip(amp, ln):
            F += a * np.exp(-1j * t * l)
        v = np.abs(F)
        loc = np.nonzero((v[1:-1] < thresh) & (v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
        mins += [(float(v[i]), float(t[i])) for i in loc]
    fd = make_fd(N)
    found = []
    for v, t in sorted(mins):
        best = None
        for s0 in (1.0, 1.005, 0.995):
            z, res = newton_polish(fd, complex(s0, t))
            if res < 1e-20 and abs(z.imag - t) < 2:
                best = z
                break
        if best is None or any(abs(best - c['approx_c']) < 1e-8 for c in found):
            continue
        c = certify_zero(fd, best, want_off_line=1.0)   # test whether Re-enclosure excludes 1
        c['approx_c'] = best
        c['screen_min_abs_on_sigma_1'] = v
        found.append(c)
    for c in found:
        z = c.pop('approx_c'); c['approx'] = [z.real, z.imag]
        if c.get('ok'):
            c['re_gt_1_certified'] = bool(c.get('off_line') and float(c['re_mid']) > 1)
    rep = dict(model=f'partial sum zeta_{N}', versions=versions(), prec_bits=128,
               params=dict(N=N, T_MAX=T_MAX, dt=dt, screen_threshold=thresh, screen_sigma=1.0),
               zeros=found,
               n_certified_re_gt_1=sum(1 for c in found if c.get('re_gt_1_certified')),
               runtime_s=round(time.time() - t0, 1))
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, f'partial_sums_N{N}.json')
    json.dump(rep, open(fn, 'w'), indent=1, default=str)
    for c in found:
        print(c.get('ok'), c.get('re_mid', '')[:20], c.get('im_mid', '')[:22], c.get('re_gt_1_certified'))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn, rep['runtime_s'])


if __name__ == '__main__':
    main()
