#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import random
import sympy as sp


def symbolic_checks() -> int:
    r, z = sp.symbols("r z", positive=True)
    checks = 0

    A = 1 - r**2
    B = 1 - r
    d = r * (1 - r)

    # Survival/hazard target and score kernels from the frozen binary-return branch.
    alpha_s = 2 * (r + 2) / (r + 3)
    alpha_h = 2 * (r + 1) / (r + 2)
    beta_h = (4 * r + 1) / (2 * r + 1)

    T_s = (1 - r) * (r + 3) * (alpha_s * z - 1)
    T_h = r * (r + 2) * (alpha_h * z - 1)
    S_s = 3 * A * (sp.Rational(5, 3) * z - 1)
    S_h = r * (2 * r + 1) * (beta_h * z - 1)

    assert sp.factor(T_s + T_h - (4 * z - 3)) == 0
    checks += 1
    assert sp.factor(S_s + S_h - (5 * z - 3) - d * (z - 1)) == 0
    checks += 1

    q_s = sp.factor(T_s / S_s)
    q_h = sp.factor(T_h / S_h)
    assert sp.factor(q_s - ((2*r + 4)*z - (r + 3)) / ((r + 1)*(5*z - 3))) == 0
    checks += 1
    assert sp.factor(q_h - ((2*r + 2)*z - (r + 2)) / ((4*r + 1)*z - (2*r + 1))) == 0
    checks += 1

    # Exact physical-corridor certificates, valid for 0<r<1 and z>=1.
    Ns = (2*r + 4)*z - (r + 3)
    Ds = (r + 1)*(5*z - 3)
    Nh = (2*r + 2)*z - (r + 2)
    Dh = (4*r + 1)*z - (2*r + 1)

    assert sp.factor(2*Ns - Ds - (3-r)*(z-1)) == 0       # q_s >= 1/2
    checks += 1
    assert sp.factor(Ds - Ns - ((3*r+1)*z - 2*r)) == 0    # q_s < 1
    checks += 1
    assert sp.factor(2*Nh - Dh - 3*(z-1)) == 0            # q_h >= 1/2
    checks += 1
    assert sp.factor(2*Dh - Nh - 3*r*(2*z-1)) == 0        # q_h < 2
    checks += 1

    # The one-child endpoint residual is positive for every affine positive kernel.
    a, b, rho = sp.symbols("a b rho", positive=True)
    K_parent = a*z - b
    K_child = a*rho*z - b
    assert sp.factor(K_parent - K_child - a*(1-rho)*z) == 0
    checks += 1

    # Binary matrix target/score identities.
    C = sp.Matrix([[A, sp.Rational(2, 3)*d],
                   [0, (4*B-A)/3]])
    H = sp.diag(r**2, r)
    t = sp.Matrix([[1, 2]])
    s = sp.Matrix([[2, 1]])
    assert sp.simplify(t*(C+H)-t) == sp.zeros(1, 2)
    checks += 1
    assert sp.simplify(s*(C+H)-s-sp.Matrix([[0, d]])) == sp.zeros(1, 2)
    checks += 1

    return checks


def fraction_branching_checks(seed: int = 91540) -> int:
    rng = random.Random(seed)
    checks = 0
    for _ in range(500):
        # Positive affine target/score kernels K(z)=a z-b on z>=1.
        # z>=9 makes the diagnostic child scale rho=1/9 active.
        z = Fraction(rng.randint(9, 40), 1)
        at = Fraction(rng.randint(1, 8), 1)
        bt = Fraction(rng.randint(0, at.numerator), at.denominator)
        ass = Fraction(rng.randint(1, 8), 1)
        bs = Fraction(rng.randint(0, ass.numerator), ass.denominator)
        T0 = at*z-bt
        S0 = ass*z-bs
        assert T0 >= 0 and S0 >= 0

        branches = []
        total_theta = Fraction(0)
        for _j in range(rng.randint(0, 5)):
            remaining = Fraction(1)-total_theta
            if remaining == 0:
                break
            theta = remaining * Fraction(rng.randint(0, 5), 5)
            rho = Fraction(1, 9)
            branches.append((theta, rho))
            total_theta += theta

        child_T = sum((theta*(at*rho*z-bt) for theta, rho in branches), Fraction(0))
        child_S = sum((theta*(ass*rho*z-bs) for theta, rho in branches), Fraction(0))
        residual_T = T0-child_T
        residual_S = S0-child_S

        # Rewrite as unused-parent part plus endpoint-monotonicity differences.
        rhs_T = (1-total_theta)*T0 + sum(
            (theta*at*(1-rho)*z for theta, rho in branches), Fraction(0)
        )
        rhs_S = (1-total_theta)*S0 + sum(
            (theta*ass*(1-rho)*z for theta, rho in branches), Fraction(0)
        )
        assert residual_T == rhs_T and residual_T >= 0
        checks += 1
        assert residual_S == rhs_S and residual_S >= 0
        checks += 1

        # Any adverse local score imbalance is bounded by residual target.
        debt = max(Fraction(0), residual_T-residual_S)
        assert debt <= residual_T
        checks += 1

        # Child target fractions are a subprobability vector.
        if T0 > 0:
            assert child_T/T0 <= 1
            checks += 1

    return checks


def main() -> None:
    checks = symbolic_checks() + fraction_branching_checks()
    result = {
        "classification": "PASS_PAIRED_KERNEL_TYPED_BRANCHING",
        "checks": checks,
        "scope": (
            "Exact symbolic verification of the survival/hazard target and score "
            "telescopes, the uniform physical-corridor inequalities, the binary "
            "matrix identities, and exact Fraction diagnostics for arbitrary "
            "subprobability endpoint branching. This replay does not certify the "
            "imported directed Hall/finite-row inequalities, the factor-54 "
            "composition, or RH."
        ),
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
