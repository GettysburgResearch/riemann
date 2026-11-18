#!/usr/bin/env python3
"""C2 zoo -- search for zeros of Z_{x^2+5y^2} in Re s > 1 (Davenport-Heilbronn 1936 prove infinitely many exist).

Screen (NON-RIGOROUS, numpy): |1 + R(s)| on sigma in {1.01, 1.03}, 0 <= t <= 1e7, step 0.05, where
  R(s) = ((1-2^-s)/(1+2^-s)) prod_{p = 3,7 mod 20, p < 400} ((1-p^-s)/(1+p^-s))^2   (truncated Euler product of
  L_genus/zeta_K; Z = zeta_K (1 + R) for sigma > 1).  Then Newton (Arb midpoints, full L-function formula) and
RIGOROUS Krawczyk certificate on the full Z (Arb, epstein_zeros.Zser).
The screening step was run once interactively (scratchpad ep_explore2.py, same formula); its best candidates
are hard-coded below so that this script only performs the (slow) Arb polishing/certification.
Usage: python3 epstein_sigma_gt1.py OUTDIR
"""
import sys, os, json, time, hashlib
import flint
from flint import acb
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import epstein_zeros as E
from zoo_common import newton_polish, certify_zero, series_eval, versions

SCREEN = [  # (sigma_screen, t, |1+R_trunc|) from the numpy screen
    (1.03, 3587891.14967258, 0.00729),
    (1.01, 4125904.8999034967, 0.00233),
    (1.01, 5000977.09999636, 0.00263),
]


def main():
    outdir = sys.argv[1]
    t0 = time.time()
    fdd = lambda z: series_eval(lambda s: E.Zser(s, 'x2+5y2'), z)
    out = []
    for sg, t, v in SCREEN:
        z, res = newton_polish(fdd, complex(sg, t), steps=30)
        rec = dict(screen=[sg, t, v], newton=[z.real, z.imag], residual=res)
        if res < 1e-20:
            c = certify_zero(fdd, z, radii=(1e-5, 1e-8), want_off_line=1.0)
            rec['certificate'] = c
            rec['re_gt_1_certified'] = bool(c.get('ok') and c.get('off_line') and float(c['re_mid']) > 1)
        out.append(rec)
        print(json.dumps(rec, default=str), round(time.time() - t0, 1), flush=True)
    rep = dict(model='Z_{x^2+5y^2}, zeros with Re s > 1', versions=versions(), prec_bits=flint.ctx.prec,
               results=out, runtime_s=round(time.time() - t0, 1))
    fn = os.path.join(outdir, 'epstein_sigma_gt1.json')
    json.dump(rep, open(fn, 'w'), indent=1, default=str)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
