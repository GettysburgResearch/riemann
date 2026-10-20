#!/usr/bin/env python3
"""Independent symbolic review of the displayed formulas (requires SymPy).

The acceptance checker beyond_hybrid_barrier.py uses only the standard library.
This separate implementation starts from the formulas in the written notes;
it verifies identities, not analytic estimates or interval sign coverage.
"""
import hashlib
import json
from pathlib import Path

import sympy as s


def main():
    k, b, d, R, th, ell, ell0, t, B0, gap = s.symbols(
        "k b d R theta ell ell0 t B0 gap"
    )
    rat = s.Rational
    checks = {}
    quartic = 16686*k**4 - 27405*k**3 + 9936*k**2 + 1290*k - 275
    u = 2200 - 26220*k - 49500*k**2 + 1086480*k**3 - 1263600*k**4
    v = 2220 - 25272*k - 30672*k**2 + 917568*k**3 - 1026432*k**4
    c, x, ellcrit = 1/(3*k), rat(1, 2), rat(5, 3) - 2*k
    den = 3 - (1 + 2*c)*x
    poly = (2 - 2*c*x)*(1 - x)
    jj = (rat(5, 6) - d)*den + d*poly
    count = 1 - d + (rat(5, 6) - d)*d*poly/(2*jj)
    h, ly = (1 + b + 3*ellcrit)/2, (1 + b - ellcrit)/2
    averaged = (-rat(1, 4) + b/6 + 5*ellcrit/4 + d/2
                + d*x*(ellcrit + c*(h/4 - ly/2)) - 3*h*(1 - count)/4)
    for bv in (0, 1):
        num, denominator = s.fraction(s.cancel(averaged.subs({b: bv, d: u/v})))
        checks[f"critical_averaged_zero_b{bv}"] = s.rem(num, quartic, k) == 0
        checks[f"critical_denominator_coprime_b{bv}"] = (
            s.degree(s.gcd(denominator, quartic), k) == 0
        )

    # Independent expansion of all four endpoints with free total length.
    total = 1 - ell + t
    ly, h = (total + b)/2, 1 - (total - b)/2 + ell
    a, g, target = (1 + d)/2, d/2, B0 - gap
    left = a-target-a*ly-ell/2+ell*g+h*(R+d/2-rat(1, 6))
    right = a-target+(a-1)*ly-ell/2+ell*g+h*(R-rat(1, 6))
    zero = a-target-ly/2-ell/2+ell*g+h*((3*R+1)/4-rat(1, 6))
    shifted = zero + th*(h/2-ly)
    aa = [-rat(1, 2)+3*R/2+3*d/2, -rat(1, 2)+3*R/2+d/4,
          -rat(1, 8)+9*R/8+d/2, -rat(1, 8)+9*R/8+d/2+5*th/4]
    cc = [-rat(1, 6)-(d+R)/2, -rat(1, 6)-R/2+d/4,
          -rat(7, 24)-3*R/8, -rat(7, 24)-3*R/8-3*th/4]
    paid = [-rat(1, 6)-d/2, -(1-d)/6, -(1+d)/6, -(1+d)/6-2*th/3]
    for name, endpoint, aj, cj, slope in zip(
            ("left", "right", "zero", "shifted"),
            (left, right, zero, shifted), aa, cc, paid):
        balanced = endpoint.subs({ell: ell0, t: 0, gap: 0})
        checks[f"free_affine_{name}"] = (
            s.expand(endpoint-balanced-aj*(ell-ell0)-cj*t-gap) == 0
        )
        checks[f"paid_negative_asymmetry_{name}"] = (
            s.expand(s.diff(balanced, b)-aj/3-slope) == 0
        )
    mm = s.symbols("M")
    lzero = rat(5, 6) + mm/12 - ell/6
    lk = rat(1, 3) + 7*mm/12 + ell/3
    lj = rat(23, 24) - mm/6 + 5*ell/24
    checks["unrestricted_direct_dual"] = (
        s.expand(rat(17, 30)*lzero+rat(1, 30)*lk+rat(2, 5)*lj-rat(13, 15)) == 0
    )

    # Principal local correction, with v=1/q, D=eta(p)q^-s.
    vv, dd, rr = s.symbols("v D resonance")
    local_h = (1-vv**2)*(1-(1-vv)*dd-vv*rr)/((1-dd)*(1-rr))
    residual = (1-vv**2)*(1+vv*(dd-rr)/(1-dd))
    checks["principal_factorization"] = s.cancel((1-rr)*local_h-residual) == 0

    pp, beta, z = s.symbols("p B z")
    beta_poly = 133488*beta**4-376596*beta**3+384534*beta**2-167541*beta+26231
    ppoly = 116*pp**4-5691*pp**3+55674*pp**2-157356*pp+133488
    checks["arithmetic_exponent_quartic"] = (
        s.expand(pp**4*beta_poly.subs(beta, 1-1/pp)-ppoly) == 0
    )
    checks["boundary_to_kappa_quartic"] = (
        s.expand(beta_poly.subs(beta, (1+k)/2)*2-quartic) == 0
    )
    weight = 960*(z-rat(1, 2))**2*(1-z)**2
    checks["annular_weight_mass"] = s.integrate(weight, (z, rat(1, 2), 1)) == 1
    for zz in (rat(1, 2), s.Integer(1)):
        checks[f"weight_value_{zz}"] = weight.subs(z, zz) == 0
        checks[f"weight_derivative_{zz}"] = s.diff(weight, z).subs(z, zz) == 0
    checks["annular_weight_peak"] = weight.subs(z, rat(3, 4)) == rat(15, 4)

    if not all(checks.values()):
        raise RuntimeError("Independent symbolic identity failed: " + str(checks))
    report = {
        "status": "PASS",
        "scope": "Exact identities only; no analytic proof or root-sign certification",
        "sympy_version": s.__version__,
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": checks,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
