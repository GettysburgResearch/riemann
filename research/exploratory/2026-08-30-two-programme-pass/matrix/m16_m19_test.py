"""Fourth held-out round for the torsion entry law m = 2 ord(alpha^2) + 1
(O-108512). PROVENANCE NOTE: this file records the round's predictions
as written BEFORE any computation ran. The sympy route below was killed
for cost mid-m=16 and the round was executed instead by
matrix/torsion_field_probe.py (exact number-field arithmetic, stdlib),
which confirmed every prediction; this file is kept as the prediction
record. Predictions, written BEFORE the run:
  m = 16, 17, 18: NO new torsion among the tested points;
  m = 19: BOTH ord(alpha^2) = 9 cubics enter JOINTLY —
    a^3 - 3a + 1   (2cos 2pi/9,  ord alpha = 9)
    a^3 - 3a - 1   (2cos pi/9,   ord alpha = 18)
    — and the ord(alpha^2) = 10 quartic a^4 - 5a^2 + 5 (2cos pi/10,
    ord alpha = 20; predicted entry m = 21) stays absent, as does the
    ord-11 quintic (2cos 2pi/11; predicted entry m = 23).

Method (exact throughout): the defect numerator from the proved
T-108500 formula; M_m by TRIANGULAR top-down peeling on the Laurent
basis (the system is triangular in degree — no general solve); then
each divisibility test computed in the small quotient ring
Q[a]/(C(a)) at b = 1 (C irreducible over Q, so disc == 0 in the
quotient iff C | disc): reduce M_m's z-coefficients mod (C, b-1),
take the discriminant of the reduced z-polynomial in that ring, and
test zero. Full-ring residual certifies the peeling.
Writes matrix/m16_m19_spectrum.json incrementally.
rh_established = false.
"""
import sys, json, time
sys.path.insert(0, '.')
sys.path.insert(0, 'matrix')
import sympy as sp
from c1_defect_atlas import defect_numerator, check_selfdual, a, b, z

TESTS = {
    "ord9_2cos2pi9": sp.Poly(a**3 - 3*a + 1, a),
    "ord18_2cospi9": sp.Poly(a**3 - 3*a - 1, a),
    "ord20_2cospi10": sp.Poly(a**4 - 5*a**2 + 5, a),
    "ord11_2cos2pi11": sp.Poly(a**5 + a**4 - 4*a**3 - 3*a**2 + 3*a + 1, a),
}


def spectrum_triangular(N, m):
    """M_m by top-down peeling: w_j = T^nu (b^m T + 1/T)^j has degree
    nu + j with leading coefficient b^{m j}; subtract from the top."""
    eps = 1 if m % 2 == 0 else 0
    nu = (m - 1 - eps) // 2
    resid = list(N)
    if eps:
        # exact division by (1 + b^{m/2} T)
        c = b ** (m // 2)
        quo = [sp.Integer(0)] * (len(resid) - 1)
        for i in range(len(resid) - 2, -1, -1):
            quo[i] = sp.expand(sp.cancel(resid[i + 1] / c))
            resid[i + 1] = sp.Integer(0)
            resid[i] = sp.expand(resid[i] - quo[i])
        assert sp.simplify(resid[0]) == 0, "even division failed"
        resid = quo
    # resid has degree 2 nu; peel
    mus = [sp.Integer(0)] * (nu + 1)
    work = resid[:]
    for j in range(nu, -1, -1):
        top = work[nu + j] if nu + j < len(work) else sp.Integer(0)
        mu = sp.expand(sp.cancel(top / b ** (m * j)))
        mus[j] = mu
        # w_j coefficients: T^{nu + 2i - j} gets C(j,i) b^{m i}
        for i in range(j + 1):
            k = nu + 2 * i - j
            work[k] = sp.expand(work[k]
                                - mu * sp.binomial(j, i) * b ** (m * i))
    assert all(sp.simplify(v) == 0 for v in work), "residual nonzero"
    return sum(mus[j] * z ** j for j in range(nu + 1)), nu


def disc_zero_mod(Mpoly, nu, C):
    """Is disc_z(M) == 0 in Q[a]/(C) at b = 1? Reduce coefficients,
    then discriminant of the reduced z-polynomial in the quotient."""
    coeffs = [sp.rem(sp.Poly(sp.expand(
        sp.Poly(Mpoly, z).coeff_monomial(z ** j)).subs(b, 1), a), C)
        for j in range(nu + 1)]
    Mred = sum(coeffs[j].as_expr() * z ** j for j in range(nu + 1))
    d = sp.discriminant(sp.Poly(Mred, z), z)
    r = sp.rem(sp.Poly(sp.expand(d), a), C)
    return r.is_zero


def main():
    out = {}
    for m in (16, 17, 18, 19):
        t0 = time.time()
        N = defect_numerator(m)
        assert check_selfdual(N, m)
        M, nu = spectrum_triangular(N, m)
        res = {name: bool(disc_zero_mod(M, nu, C))
               for name, C in TESTS.items()}
        print(f"m={m} ({time.time()-t0:.0f}s) {res}", flush=True)
        out[str(m)] = res
        json.dump(out, open('matrix/m16_m19_spectrum.json', 'w'),
                  indent=1)
    print("prediction: m=16..18 all False; m=19 ord9 True ord18 True "
          "ord20 False ord11 False")


if __name__ == "__main__":
    main()
