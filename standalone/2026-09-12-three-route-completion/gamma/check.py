"""Bounded exact controls for the gamma signed-production proof.

This does NOT verify analytic theorems or replay inherited zero certificates.
No external packages, numerical quadrature, or ordinary floating arithmetic.
"""
from fractions import Fraction as Q
from math import factorial
import argparse
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rational(q):
    q = Q(q)
    return {"numerator": q.numerator, "denominator": q.denominator}


def convolution(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def reconstruct():
    checks = {}

    # Rational controls of the distinct source formulas in the proved
    # Gamma/compound-Poisson head identity; these panels are not its proof.
    for s in [Q(0), Q(1, 7), Q(3, 2), Q(11), Q(-1, 2)]:
        anchored = (1 + s / 4) ** -4 * ((1 + s / 4) / (1 + s)) ** 2
        native = (1 + s) ** -2 * (1 + s / 4) ** -2
        require(anchored == native, "head factor panel")
    checks["head_identity_panels"] = 5

    a = Q(13, 4)
    fisher = Q(256, 6) * (9 / a**2 - 48 / a**3 + 96 / a**4)
    require(fisher == Q(382976, 28561), "weighted gamma Fisher integral")
    require(1024 * fisher < 2**14, "whole-source Fisher ceiling")
    require(Q(256, 6) * Q(6, 7)**3 < 32, "tilted anchor density ceiling")
    require(3**17 < 2**27, "anchor lower endpoint")
    require(Q(3, 26) > Q(1, 10), "normalizer Markov reserve")
    require(Q(1, 50 * 10 * 2**14) > Q(1, 2**23), "whole normalizer bound")
    require(256 * Q(4, 3) * Q(4, 5) < 274, "fast velocity bound")
    require(274 + 192 == 466 and 466 + 2 * 192 == 850,
            "integrated parameter velocity")
    checks["weighted_fisher_anchor"] = rational(fisher)
    checks["weighted_fisher_whole_ceiling"] = 2**14
    checks["whole_path_velocity_constant"] = 850

    # Genuine finite positive scale-measure controls, not native high-r rules.
    # r=1 Radau: node=m2/m1, positive-node weight=m1^2/m2,
    # drift=m0-weight; verify all matched and first unmatched cumulants.
    measures = [
        [(Q(1, 2), Q(2)), (Q(1, 3), Q(3)), (Q(1, 7), Q(5))],
        [(Q(1, 9), Q(2, 9)), (Q(1, 16), Q(1, 8)), (Q(1, 25), Q(2, 25))],
        [(Q(1, 2), Q(1, 5)), (Q(2, 3), Q(2, 7)), (Q(3, 4), Q(3, 11))],
    ]
    radau_controls = []
    for atoms in measures:
        moments = [sum((weight * x**j for x, weight in atoms), Q(0))
                   for j in range(5)]
        m0, m1, m2, m3, m4 = moments
        node, weight = m2 / m1, m1 * m1 / m2
        drift, shape = m0 - weight, weight / node
        defect = m3 - m2 * m2 / m1
        require(drift > 0 and shape > 0 and defect > 0, "Radau positivity")
        require(drift + shape * node == m0, "Levy first-moment compensation")
        for k in range(2, 4):
            require(factorial(k - 1) * shape * node**k
                    == factorial(k - 1) * moments[k - 1], "matched cumulant")
        kappa4_delta = 6 * (shape * node**4 - m3)
        require(kappa4_delta == -6 * defect, "first lost cumulant sign")
        require(-(defect / 4) * factorial(4) == kappa4_delta,
                "native Mellin tangent normalization")
        # W mean from the positive exact remainder; r=1, M=4.
        weighted_x = (m4 - 2 * node * m3 + node**2 * m2) / defect
        mean_w = Q(4, 5) * (weighted_x + 2 * node)
        b = max(x for x, _ in atoms)
        require(0 < mean_w <= Q(12, 5) * b, "complete remainder-law mean")
        radau_controls.append({"node": rational(node), "drift": rational(drift),
                               "first_scale_defect": rational(defect),
                               "remainder_mean": rational(mean_w)})
    checks["finite_radau_controls"] = radau_controls

    # In variable w=i*z, p=1/4+w/2. Then -4p(p-1)=3/4+w-w^2.
    # Returning w=i*z yields z^2+3/4+i*z, the actual M=2 reflected sign.
    p = [Q(1, 4), Q(1, 2)]
    pm1 = [Q(-3, 4), Q(1, 2)]
    tangent_poly = [-4 * c for c in convolution(p, pm1)]
    require(tangent_poly == [Q(3, 4), Q(1), Q(-1)], "native M2 shift sign")
    checks["native_M2_polynomial_in_i_z"] = [rational(c) for c in tangent_poly]

    # Exact collision control: for t>0, the squared roots have modulus one;
    # their cosine is 1-t/2. No numerical root finder is used.
    collision_panels = []
    for t in [Q(-1, 4), Q(-1, 16), Q(0), Q(1, 16), Q(1, 4)]:
        mu2 = 4 - 2 * t
        inverse_square_moduli = Q(4) if t >= 0 else mu2
        delta = (inverse_square_moduli - mu2) / 8
        require(delta == max(t, Q(0)) / 4, "collision-aware defect")
        collision_panels.append({"parameter": rational(t), "defect": rational(delta)})
    checks["collision_controls"] = collision_panels

    # Imported GE4 disk. These rational consequences do not replay GE4.
    re = Q("31.0835163803300613860836804713778137956057544691")
    im = Q("0.2347791171837078741080118319340221394471947526")
    radius = Q(1, 10**12)
    require(im - radius > Q(23, 100), "GE4 disk imaginary lower bound")
    require(re + im + 2 * radius < 32, "GE4 disk modulus upper bound")
    lower = Q(529, 10000 * 32**4)
    require(lower > Q(1, 20_000_000), "native net defect production lower bound")
    checks["imported_GE4_disk_defect_lower_bound"] = rational(lower)

    # Optional use of the named published finite-height theorem. This checks
    # only our fourth-power-tail arithmetic, not Platt--Trudgian's computation.
    height = 3 * 10**12
    exp31_lower = sum((Q(31**k, factorial(k)) for k in range(65)), Q(0))
    require(exp31_lower > 4 * height, "log(4H)<31 via positive exponential series")
    upper = Q(13, 8 * height**4) + Q(47, 9 * height**3)
    require(upper < Q(2, 10**37), "optional complete xi defect upper bound")
    checks["optional_xi_defect_upper_bound"] = rational(upper)

    return {
        "schema": "gamma-anchored-jensen-bounded-controls-v1",
        "arithmetic": "exact integers and fractions; no floating primitives",
        "scope": "bounded algebra/inequalities only; no analytic proof or inherited integral replay",
        "rh_proved": False,
        "open_gate": "OPEN-GJV",
        "checks": checks,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", type=Path, help="write reconstructed bounded results")
    args = parser.parse_args()
    result = reconstruct()
    canonical = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.write_text(canonical, encoding="utf-8")
    else:
        existing = Path(__file__).with_name("results.json")
        require(existing.read_text(encoding="utf-8") == canonical,
                "results.json does not match complete bounded reconstruction")
    print("PASS gamma anchored Jensen bounded controls; OPEN-GJV remains open; RH unproved")


if __name__ == "__main__":
    main()
