#!/usr/bin/env python3
"""C2 zoo -- smallest degree d with J^{d,0} non-hyperbolic for the synthetic xi~ (injected quadruple).

g~(k) = k! * [z^{2k}] xi~(1/2+z) (Arb, prec PREC bits, series length K); J^{d,0}(X) = sum_j C(d,j) g~(j) X^j.
Hyperbolicity tested by FLINT/Arb rigorous root isolation of the integer polynomial obtained by rounding the
coefficients to 60 significant digits (rigorous for the rounded polynomial only; NUMERICAL-NONRIGOROUS
for the exact one).  Sanity check: the truncated Taylor series of xi~(1/2+z) at z = rho0 - 1/2 (a zero).
Usage: python3 jensen_degree_scan.py OUTDIR
"""
import sys, os, json, time, math, hashlib, fractions
import flint
from flint import acb, arb, fmpq, fmpq_poly, fmpz
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import synthetic_xi as S
from zoo_common import versions

CASES = [(0.6, 5.0), (0.9, 5.0), (0.9, 14.0), (0.75, 10.0), (0.6, 14.0)]
DLIST = list(range(40, 120, 4)) + list(range(120, 241, 10))


def main():
    outdir = sys.argv[1]
    K, PREC = 500, 5000
    t0 = time.time()
    c = S.xi_taylor(K, PREC)
    c = list(c) + [acb(0)] * (K - len(c))
    out = dict(versions=versions(), K=K, prec=PREC, dlist=DLIST, cases=[])
    for beta, gam0 in CASES:
        P = [acb(1)]
        for r in (acb(beta, gam0), acb(beta, -gam0), acb(1 - beta, -gam0), acb(1 - beta, gam0)):
            P = S.poly_mul(P, [(r - acb("0.5")) / r, acb(-1) / r], 5)
        cc = S.poly_mul(c, P, K)
        z0 = acb(beta - 0.5, gam0)
        val = sum((cc[j] * z0 ** j for j in range(K)), acb(0))
        g = [cc[2 * k].real * arb.fac_ui(k) for k in range(K // 2)]

        def q(x):
            F = fractions.Fraction(x.mid().str(60, radius=False))
            return fmpq(F.numerator, F.denominator)
        gq = [q(x) for x in g]
        relrad = [float(x.rad() / abs(x.mid())) if not x.mid().is_zero() else float('inf') for x in g]
        first = None
        rows = []
        for d in DLIST:
            if d >= len(gq) or max(relrad[:d + 1]) > 1e-60:
                rows.append((d, 'coefficients not accurate enough'))
                break
            Pd = fmpq_poly([fmpz(math.comb(d, j)) * gq[j] for j in range(d + 1)])
            rr = Pd.numer().complex_roots()
            nonreal = sum(m for r, m in rr if not r.imag.contains(0))
            rows.append((d, nonreal))
            if nonreal and first is None:
                first = d
                break
        rec = dict(beta=beta, gamma0=gam0, X0=str((z0 * z0)), taylor_value_at_zero=str(val),
                   first_d_nonhyperbolic_in_list=first, rows=rows, elapsed=round(time.time() - t0, 1))
        out['cases'].append(rec)
        print(json.dumps(rec), flush=True)
    out['runtime_s'] = round(time.time() - t0, 1)
    fn = os.path.join(outdir, 'jensen_degree_scan.json')
    json.dump(out, open(fn, 'w'), indent=1)
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
