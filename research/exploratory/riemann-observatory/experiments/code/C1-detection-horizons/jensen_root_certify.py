#!/usr/bin/env python3
"""C1: certify (Arb root isolation, python-flint fmpz_poly.complex_roots) whether the classical Jensen polynomial
J^{d,0} of Farmer's X_j has non-real zeros. J(z) = R(z^2); J real-rooted iff all roots of R are real and >= 0.
R is replaced by the integer polynomial round(10^S * C(d,2n) alpha_{2n}) (S digits of scaling); the statement is
certified for that rounded polynomial (NUMERICAL-RIGOROUS for it; rounding perturbation is ~10^-S relative)."""
import sys, time, json
import mpmath as mp, flint
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from jensen_exact_check import taylor_X
import common
S = 450
res = []
for j, ds in {20: [475, 478, 600, 749, 750], 10: [119, 120]}.items():
    alpha, ab = taylor_X(j, max(ds) + 2, dps=500)
    mp.mp.dps = 500
    for d in ds:
        t1 = time.time()
        co = [int(mp.nint(mp.binomial(d, 2 * n) * alpha[n] * mp.mpf(10)**S)) for n in range(d // 2 + 1)]
        P = flint.fmpz_poly(co)
        roots = P.complex_roots()
        nonreal = [(r, m) for r, m in roots if not (abs(r.imag) < 1e-300 or r.imag.contains(0)) ]
        neg_real = [(r, m) for r, m in roots if r.imag.contains(0) and r.real < 0]
        # roots are certified isolated balls; a root ball whose imaginary part excludes 0 is a certified non-real root
        cert_nonreal = [r for r, m in roots if not r.imag.contains(0)]
        row = {"j": j, "d": d, "deg_R": d // 2, "n_root_balls": len(roots), "certified_nonreal_roots_of_R": len(cert_nonreal),
               "certified_negative_real_roots_of_R": len(neg_real),
               "J_real_rooted": (len(cert_nonreal) == 0 and len(neg_real) == 0 and sum(m for r, m in roots) == d // 2),
               "example_nonreal": [str(r) for r in cert_nonreal[:2]], "sec": round(time.time() - t1, 1)}
        res.append(row); print(row, flush=True)
p = common.save_json("jensen_root_certify.json", {"env": common.env(), "scale_digits": S, "rows": res})
print("saved", p, common.sha256(p))
