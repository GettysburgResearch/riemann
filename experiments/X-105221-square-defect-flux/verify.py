#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction

def coherence_defect(residues, lam):
    R = len(residues)
    m1 = -sum(residues, Fraction(0))
    m2 = sum((r*r for r in residues), Fraction(0))
    direct = sum(((1 + lam*r)**2 for r in residues), Fraction(0))
    moment = Fraction(R) - 2*lam*m1 + lam*lam*m2
    assert direct == moment
    wrong = sum(1 for r in residues if r > 0)
    assert wrong <= direct
    return direct, m1, m2, wrong

def compute():
    residues = [Fraction(1,8), Fraction(-1,2), Fraction(1,8)]
    lam = Fraction(2)
    defect, m1, m2, wrong = coherence_defect(residues, lam)
    assert defect == Fraction(25,8)
    assert wrong == 2

    def U(x):
        return Fraction(5*x*x-4, 8)
    assert U(-1) == Fraction(1,8)
    assert U(0) == Fraction(-1,2)
    assert U(1) == Fraction(1,8)
    interpolated = [(1 + lam*U(x))**2 for x in (-1,0,1)]
    assert sum(interpolated, Fraction(0)) == defect

    RK, K = 1000, 3
    defects = [Fraction(4), Fraction(7,2), Fraction(2)]
    lower = Fraction(RK) - 2*sum(defects, Fraction(0)) - K
    assert lower == Fraction(978)

    p3 = 1 - (math.e**2 + 2) / 144
    threshold = (p3 - 0.9) / 2
    assert 0.01739 < threshold < 0.01741

    payload = {
        "schema": "riemann.x105221.square-defect-flux.v1",
        "classification": "PASS_T105221_DEBT_FREE_SQUARE_DEFECT_FLUX",
        "quartic_residues": [str(r) for r in residues],
        "quartic_lambda": str(lam),
        "quartic_defect": str(defect),
        "quartic_wrong_extrema": wrong,
        "interpolation_fixture": "U(z)=(5z^2-4)/8",
        "multilevel_fixture_lower_bound": str(lower),
        "k3_literature_target_approx": threshold,
        "entire_interpolation_boundary_bound_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output")
    args=ap.parse_args()
    payload=compute()
    text=json.dumps(payload, indent=2, sort_keys=True)+"\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(payload["classification"])
    print(payload["proof_object_sha256"])

if __name__ == "__main__":
    main()
