"""Independent exact arithmetic audit of a licensed Xu--Sang parameter choice.

This file does not prove the imported analytic statements. It reconstructs
every scalar admissibility inequality and the global endpoint certificate
of arXiv:2610.15291v2, Sections 6.2, 7, and Appendix D.

Only Python's standard library is used. Checks remain enabled under -O.
"""
from fractions import Fraction as F
import argparse
import hashlib
import json
from pathlib import Path


def check(condition, message):
    if not condition:
        raise ArithmeticError(message)


class Poly:
    """Bivariate rational polynomial; keys are powers of delta and y."""

    def __init__(self, terms=0):
        if isinstance(terms, Poly):
            self.t = dict(terms.t)
        elif isinstance(terms, dict):
            self.t = {k: F(v) for k, v in terms.items() if v}
        else:
            self.t = {(0, 0): F(terms)} if terms else {}

    def __add__(self, other):
        out = dict(self.t)
        for k, v in Poly(other).t.items():
            out[k] = out.get(k, F(0)) + v
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({k: -v for k, v in self.t.items()})

    def __sub__(self, other):
        return self + -Poly(other)

    def __rsub__(self, other):
        return Poly(other) + -self

    def __mul__(self, other):
        out = {}
        for (i, j), a in self.t.items():
            for (k, l), b in Poly(other).t.items():
                idx = (i + k, j + l)
                out[idx] = out.get(idx, F(0)) + a * b
        return Poly(out)

    __rmul__ = __mul__

    def coeff_delta(self, d):
        return Poly({(0, j): a for (i, j), a in self.t.items() if i == d})

    def y_coefficients(self):
        check(all(i == 0 for i, _ in self.t), "not univariate in y")
        n = max((j for _, j in self.t), default=0)
        return [self.t.get((0, j), F(0)) for j in range(n + 1)]


def rat(x):
    return f"{x.numerator}/{x.denominator}"


def certify(b, boundary, g):
    kappa = F(29991, 40000)
    ell = 4 * (F(11, 12) - boundary)
    zeta = F(1, 10**10)
    gstar = g / 2
    c = 1 / (3 * kappa)
    h = (1 + b + 3 * ell) / 2
    lx = (1 - b - ell) / 2
    ly = (1 + b - ell) / 2
    C0 = -F(1, 4) + b / 6 + 5 * ell / 4
    Asm = F(1, 2) + (ell / 2) * (F(1, 2) + 2 * ell / h) - h / 2
    z0 = F(17, 50)
    dmin = F(1, 100)
    margins = {
        "b_positive": b,
        "ell_above_one_sixth": ell - F(1, 6),
        "ell_below_one_fifth": F(1, 5) - ell,
        "kappa_above_lower_inclusive": kappa - F(29991, 40000),
        "kappa_below_upper_inclusive": F(3, 4) - kappa,
        "boundary_above_87_over_100": boundary - F(87, 100),
        "lx_above_ell": lx - ell,
        "ly_minus_ell_above_11b_over_6": ly - ell - 11 * b / 6,
        "prime_supply_lower": 6 * kappa * ell - F(3, 4),
        "prime_supply_upper": 1 / (6 * kappa) - ell / h,
        "prime_supply_extended": ell / (h + zeta) - F(21, 100),
        "ly_above_h_half": ly - h / 2,
        "ly_below_half": F(1, 2) - ly,
        "gstar_positive": gstar,
        "gstar_below_1e_minus_3": F(1, 1000) - gstar,
        "twice_zeta_positive": 2 * zeta,
        "twice_zeta_below_1e_minus_3": F(1, 1000) - 2 * zeta,
        "g_minus_twice_zeta_above_gstar": g - 2 * zeta - gstar,
        "small_delta_C0": -F(1, 250) - C0,
        "small_delta_other_endpoint": -F(1, 250) - C0 - Asm / 8,
        "floor": -F(1, 100) - C0 - (F(1, 2) + 3 * ell / 2) / 50,
        "small_rows": -F(1, 20) - h * (z0 - F(1, 6)) + ly / 2 - 2 * dmin,
        "license_from_Xu_stage_0_inclusive": (1 + kappa) / 2 - F(69991, 80000),
        "strict_gain_over_Xu_stage_1": F(8748867, 10**7) - boundary,
    }
    inclusive = {"kappa_above_lower_inclusive", "kappa_below_upper_inclusive", "license_from_Xu_stage_0_inclusive"}
    for name, margin in margins.items():
        check(margin >= 0 if name in inclusive else margin > 0, name)

    delta = Poly({(1, 0): 1})
    y = Poly({(0, 1): 1})
    x = F(1, 2) - y
    alpha = F(5, 6)
    D = 3 - (1 + 2 * c) * x
    P = (2 - 2 * c * x) * (1 - x)
    J = (alpha - delta) * D + delta * P
    T = ell + c * (h / 4 - ly / 2)
    # E = C0+delta/2+delta*x*T-3*h*delta/4
    #     +3*h*(alpha-delta)*delta*P/(8*J).
    # Therefore Q=-8*J*(E+g), with no numerical division.
    Q = -8 * J * (C0 + g + delta * F(1, 2) + delta * x * T - delta * (3 * h / 4)) - 3 * h * (alpha - delta) * delta * P
    check(all(i <= 2 for i, _ in Q.t), "Q is not quadratic in delta")
    A = Q.coeff_delta(2)
    B = Q.coeff_delta(1)
    C = Q.coeff_delta(0)
    discriminant_complement = 4 * A * C - B * B
    ac = A.y_coefficients()
    bc = B.y_coefficients()
    cc = C.y_coefficients()
    dc = discriminant_complement.y_coefficients()
    check(ac[0] > 0 and all(a >= 0 for a in ac), "A has a negative coefficient")
    check(dc[0] > 0 and all(a >= 0 for a in dc), "4AC-B^2 has a negative coefficient")
    # D>=5/2-c>0 and P>=(2-c)/2>0 on 0<=x<=1/2.
    check(F(5, 2) - c > 0 and (2 - c) / 2 > 0, "J positivity")
    # Complete the square: 4*A*Q = (2*A*delta+B)^2+(4*A*C-B^2).
    identity = 4 * A * Q - ((2 * A * delta + B) * (2 * A * delta + B) + discriminant_complement)
    check(not identity.t, "complete-square identity")
    return {
        "status": "PASS",
        "scope": "exact rational parameter admissibility; imported analytic theorems remain assumptions",
        "parameters": {n: rat(v) for n, v in dict(b=b, ell=ell, kappa=kappa, boundary=boundary, g=g, zeta=zeta, gstar=gstar, lx=lx, ly=ly, h=h, C0=C0).items()},
        "margins": {n: rat(v) for n, v in margins.items()},
        "endpoint_identity": "Q=-8*J*(E+g)=A(y)*delta^2+B(y)*delta+C(y), y=1/2-x",
        "A_y_ascending": list(map(rat, ac)),
        "B_y_ascending": list(map(rat, bc)),
        "C_y_ascending": list(map(rat, cc)),
        "four_AC_minus_B2_y_ascending": list(map(rat, dc)),
        "endpoint_domain": "all real delta and y>=0 for Q; 0<=delta<=5/6, 0<=x<=1/2 for J>0 and E<-g",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--b", default="86457/1000000")
    ap.add_argument("--boundary", default="87488666/100000000")
    ap.add_argument("--g", default="1/100000000")
    ap.add_argument("--output")
    args = ap.parse_args()
    result = certify(F(args.b), F(args.boundary), F(args.g))
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        Path(args.output).write_text(out)
    print(out, end="")


if __name__ == "__main__":
    main()
