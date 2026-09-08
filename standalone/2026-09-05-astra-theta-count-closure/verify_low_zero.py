#!/usr/bin/env python3
"""Directed-interval Xi(14)/Xi(15) signs; NOT a complete zero census.
Analytic eta-series tail is enclosed by the exact rational 2**(-80).
Requires mpmath==1.3.0. The interval gamma implementation is an explicit
software trust dependency; this is not a Lean/kernel-checked proof.
"""
from fractions import Fraction
from math import comb
import json
import mpmath
from mpmath import iv


def enclosure(t: int):
    if t not in (14, 15):
        raise ValueError("The analytic tail contract is only for t=14,15")
    iv.dps = 80
    n_terms = 128
    s = iv.mpc(iv.mpf(1)/2, t)
    eta = iv.mpc(0)
    for n in range(1, n_terms + 1):
        c = sum((Fraction(comb(k, n-1), 2**(k+1))
                 for k in range(n-1, n_terms)), Fraction(0))
        w = iv.mpf(c.numerator) / c.denominator
        eta += (-1)**(n-1) * w * iv.exp(-s * iv.log(n))
    eps = iv.mpf(1) / 2**80
    error = iv.mpc(iv.mpf([-eps, eps]), iv.mpf([-eps, eps]))
    zeta = (eta + error)/(1-iv.exp((1-s)*iv.log(2)))
    xi = s*(s-1)*iv.exp(-s/2*iv.log(iv.pi))*iv.gamma(s/2)*zeta/2
    if not (xi.imag.a <= 0 <= xi.imag.b):
        raise ArithmeticError("Xi conjugation check failed")
    if t == 14:
        if not (xi.real.a > 0):
            raise ArithmeticError("Xi(14) sign not certified")
    elif not (xi.real.b < 0):
        raise ArithmeticError("Xi(15) sign not certified")
    return {"t": t, "xi_real_interval": str(xi.real),
            "xi_imag_interval": str(xi.imag),
            "sign": 1 if t == 14 else -1}


def main():
    if mpmath.__version__ != "1.3.0":
        raise RuntimeError("Replay requires mpmath==1.3.0")
    # Elementary tail receipt: sqrt(cosh(15*pi)) < exp(24) < 3**24 < 2**39.
    if not (Fraction(15*22, 2*7) < 24 and 3**24 < 2**39):
        raise ArithmeticError("Exact tail-budget check failed")
    result = {"status": "PASS_DIRECTED_LOW_ZERO_SIGN_CHANGE",
              "arithmetic": "DIRECTED_INTERVAL_WITH_EXACT_ANALYTIC_TAIL",
              "mpmath": mpmath.__version__, "decimal_precision": 80,
              "eta_terms": 128, "eta_error_radius": "1/1208925819614629174706176",
              "conclusion": "At least one critical-line zero has 14 < gamma < 15",
              "complete_zero_census": False, "rh_proved": False,
              "enclosures": [enclosure(14), enclosure(15)]}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
