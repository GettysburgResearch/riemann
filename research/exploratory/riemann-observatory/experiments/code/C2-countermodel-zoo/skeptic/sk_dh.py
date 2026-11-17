#!/usr/bin/env python3
"""SKEPTIC replay of C2-02/03/04 (Davenport-Heilbronn) using an independent code path.

* f is evaluated via the L-function form ((1-ik)/2)L(s,chi)+((1+ik)/2)L(s,chibar) (acb.dirichlet_l),
  NOT the Hurwitz form used by the investigator; chi values are checked explicitly.
* Off-line zeros are certified with the rigorous argument principle of sk_wind.py on a rectangle
  [sigma0, sigma1] x [t0, t1] with sigma0 > 1/2 (winding 1 => exactly one zero, multiplicity 1, Re > 1/2),
  NOT with the investigator's Krawczyk routine.
* mpmath (non-rigorous) check of the functional equation at random points.
Usage: python3 sk_dh.py OUTDIR
"""
import sys, os, json, time, random
import flint
from flint import acb, arb
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sk_wind import winding

flint.ctx.prec = 100
K = ((10 - 2 * arb(5).sqrt()).sqrt() - 2) / (arb(5).sqrt() - 1)
I = acb(0, 1)
chi = flint.dirichlet_char(5, 2)
chib = flint.dirichlet_char(5, 3)


def chival(c, n):
    e = c.chi_exponent(n)              # chi(n) = exp(2 pi i e / order)
    return acb(0, 1) ** ((4 // c.order()) * e) if e is not None else 0


def f(s):
    return (1 - I * K) / 2 * acb.dirichlet_l(s, chi) + (1 + I * K) / 2 * acb.dirichlet_l(s, chib)


def main():
    out = {}
    t0 = time.time()
    out['chi_values_n=1..4'] = [str(chival(chi, n)) for n in range(1, 5)]
    out['chibar_values_n=1..4'] = [str(chival(chib, n)) for n in range(1, 5)]
    out['kappa'] = K.str(25)
    # coefficient check a_n for n=1..5 from the L-form: ((1-ik)/2)chi(n)+((1+ik)/2)chibar(n)
    out['a_n_from_Lform'] = [str((1 - I * K) / 2 * chival(chi, n) + (1 + I * K) / 2 * chival(chib, n)) for n in range(1, 5)]
    # functional equation, mpmath non-rigorous, random points
    mp.mp.dps = 30
    kk = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    def fm(s):
        a = [0, 1, kk, -kk, -1]
        return mp.fsum(a[j] * mp.zeta(s, mp.mpf(j) / 5) for j in range(1, 5)) * 5 ** (-s)
    def xim(s):
        return (5 / mp.pi) ** (s / 2) * mp.gamma((s + 1) / 2) * fm(s)
    random.seed(1)
    fe = []
    for _ in range(4):
        s = mp.mpc(random.uniform(-2, 3), random.uniform(0, 120))
        fe.append(float(abs(xim(s) - xim(1 - s)) / abs(xim(s))))
    out['FE_relative_defect_mpmath_random_points'] = fe
    # rigorous argument-principle certificates
    zs = [(0.8085171824566374, 85.6993484853776), (0.6508300806097371, 114.16334273075698),
          (0.574356050450806, 166.47930591316816), (0.7242576946268098, 176.70246124285583),
          (0.8695305796406431, 240.4046723514407)]
    certs = []
    for (x, y) in zs:
        h = min(0.01, (x - 0.5) / 2)
        r = winding(f, x - h, x + h, y - h, y + h, nseg=16)
        r.update(center=[x, y], halfwidth=h, sigma_lower=x - h)
        certs.append(r)
        print(r, flush=True)
    out['winding_certificates'] = certs
    out['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(out, open(os.path.join(sys.argv[1], 'sk_dh.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'winding_certificates'}, indent=1))


if __name__ == '__main__':
    main()
