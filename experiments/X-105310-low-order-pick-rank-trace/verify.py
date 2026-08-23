#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105310_LOW_ORDER_PICK_RANK_TRACE"
ROOT = Path(__file__).resolve().parents[2]

CONTENT_FILES = (
    "claims/lemmas/L-105310-critical-residue-pick-kernel.md",
    "claims/lemmas/L-105311-multiplicity-inertia-budget.md",
    "claims/lemmas/L-105312-qjet-gamma-model.md",
    "claims/refutations/R-105310-scalar-boundary-is-not-density-certificate.md",
    "claims/theorems/T-105310-low-order-pick-rank-trace-frontier.md",
    "claims/methodology/M-105310-hostile-review-contract.md",
    "experiments/X-105310-low-order-pick-rank-trace/verify.py",
    "experiments/X-105310-low-order-pick-rank-trace/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@dataclass(frozen=True)
class G:
    """Gaussian rational a+b*i."""

    a: F = F(0)
    b: F = F(0)

    @staticmethod
    def coerce(value: object) -> "G":
        if isinstance(value, G):
            return value
        return G(F(value), F(0))

    def __add__(self, other: object) -> "G":
        z = G.coerce(other)
        return G(self.a + z.a, self.b + z.b)

    __radd__ = __add__

    def __neg__(self) -> "G":
        return G(-self.a, -self.b)

    def __sub__(self, other: object) -> "G":
        return self + (-G.coerce(other))

    def __rsub__(self, other: object) -> "G":
        return G.coerce(other) - self

    def __mul__(self, other: object) -> "G":
        z = G.coerce(other)
        return G(self.a * z.a - self.b * z.b, self.a * z.b + self.b * z.a)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "G":
        z = G.coerce(other)
        denominator = z.a * z.a + z.b * z.b
        if denominator == 0:
            raise ZeroDivisionError("Gaussian rational division by zero")
        return G(
            (self.a * z.a + self.b * z.b) / denominator,
            (self.b * z.a - self.a * z.b) / denominator,
        )

    def conj(self) -> "G":
        return G(self.a, -self.b)

    def norm_sq(self) -> F:
        return self.a * self.a + self.b * self.b

    def text(self) -> str:
        return f"({self.a})+({self.b})i"


def derivative(coefficients: list[F]) -> list[F]:
    return [F(index) * coefficients[index] for index in range(1, len(coefficients))]


def evaluate(coefficients: list[F], point: G) -> G:
    value = G()
    for coefficient in reversed(coefficients):
        value = value * point + coefficient
    return value


def matrix_entry_direct(
    p: list[F], p1: list[F], z: G, w: G, degree: int
) -> G:
    qz = evaluate(p, z) / evaluate(p1, z)
    qw_bar = (evaluate(p, w) / evaluate(p1, w)).conj()
    return (qz - qw_bar) / (z - w.conj()) - F(1, degree)


def matrix_entry_atoms(
    roots: list[G], residues: list[G], z: G, w: G
) -> G:
    value = G()
    for root, residue in zip(roots, residues, strict=True):
        value -= residue / ((z - root) * (w.conj() - root))
    return value


def pick_kernel_fixture() -> dict[str, object]:
    # p'(x)=5(x+2)(x-1)(x^2+1).  The additive constant is chosen so that
    # the two real critical residues have opposite signs.
    p = [F(10), F(-10), F(5, 2), F(-5, 3), F(5, 4), F(1)]
    p1 = derivative(p)
    p2 = derivative(p1)
    roots = [G(F(-2)), G(F(1)), G(F(0), F(1)), G(F(0), F(-1))]
    residues = []
    for root in roots:
        require(evaluate(p1, root) == G(), "declared derivative root is wrong")
        residues.append(evaluate(p, root) / evaluate(p2, root))

    require(residues[0].b == 0 and residues[0].a < 0, "first real residue orientation")
    require(residues[1].b == 0 and residues[1].a > 0, "second real residue orientation")
    require(residues[3] == residues[2].conj(), "nonreal residue conjugation")

    points = [G(F(0), F(2)), G(F(1), F(2)), G(F(-1), F(3))]
    checks = 0
    matrix: list[list[G]] = []
    for z in points:
        row = []
        for w in points:
            direct = matrix_entry_direct(p, p1, z, w, 5)
            atoms = matrix_entry_atoms(roots, residues, z, w)
            require(direct == atoms, "Pick kernel atom decomposition failed")
            row.append(direct)
            checks += 1
        matrix.append(row)

    for i in range(len(points)):
        for j in range(len(points)):
            require(matrix[i][j] == matrix[j][i].conj(), "compressed matrix not Hermitian")

    rho = residues[2]
    # The coefficient matrix [[0,-rho],[-bar(rho),0]] has determinant -|rho|^2.
    pair_determinant = -rho.norm_sq()
    require(pair_determinant < 0, "nonreal pair must have opposite eigenvalue signs")

    return {
        "degree": 5,
        "checks": checks,
        "real_residues": [residues[0].text(), residues[1].text()],
        "nonreal_residue": residues[2].text(),
        "nonreal_pair_determinant": str(pair_determinant),
    }


def confluent_budget_checks() -> dict[str, object]:
    real_checks = 0
    pair_checks = 0
    for multiplicity in range(2, 101):
        charge = (multiplicity + 1) // 2
        excess = multiplicity - 1
        require(F(charge) <= F(3, 4) * excess + F(1, 2), "real block budget")
        real_checks += 1
    for multiplicity in range(1, 101):
        charge = multiplicity
        excess = 2 * (multiplicity - 1)
        require(F(charge) <= F(3, 4) * excess + F(1), "nonreal pair budget")
        pair_checks += 1

    b = F(5429, 6250)
    d = F(11679, 12500)
    require(d == (1 + b) / 2, "xi-prime constants lost exact relation")
    excess_bound = 1 - d
    total_defect = 1 - b
    nuisance = F(3, 4) * excess_bound + F(1, 2) * (total_defect - excess_bound)
    require(nuisance == F(821, 10000), "nuisance constant mutation")

    # Enumerate aggregate integer ledgers at moderate size and check the linear maximum.
    aggregate_checks = 0
    for total in range(1, 301):
        # Use exact ceiling versions of the imported asymptotic lower bounds.
        simple_min = (5429 * total + 6249) // 6250
        distinct_min = (11679 * total + 12499) // 12500
        for simple in range(simple_min, total + 1):
            for distinct in range(max(simple, distinct_min), total + 1):
                excess = total - distinct
                unprotected = distinct - simple
                charge_upper = F(3, 4) * excess + F(1, 2) * unprotected
                # Finite ceiling effects are allowed one unit; asymptotically the exact density is 821/10000.
                require(
                    charge_upper <= F(821, 10000) * total + 1,
                    "aggregate nuisance ceiling failed",
                )
                aggregate_checks += 1

    return {
        "real_block_checks": real_checks,
        "nonreal_pair_checks": pair_checks,
        "aggregate_checks": aggregate_checks,
        "simple_constant": str(b),
        "distinct_constant": str(d),
        "nuisance_density": str(nuisance),
    }


def rank_trace_checks() -> dict[str, object]:
    fixtures = [
        [F(3), F(2), F(-4), F(0)],
        [F(1, 3), F(1, 7), F(1, 11), F(-9)],
        [F(-1), F(-2), F(-3)],
        [F(5), F(0), F(0), F(-1), F(-1)],
    ]
    rows = []
    for eigenvalues in fixtures:
        positive = [value for value in eigenvalues if value > 0]
        trace_positive = max(sum(eigenvalues, F(0)), F(0))
        hs_sq = sum((value * value for value in eigenvalues), F(0))
        positive_index = len(positive)
        require(trace_positive * trace_positive <= positive_index * hs_sq, "rank-trace inequality")
        rows.append(
            {
                "eigenvalues": [str(value) for value in eigenvalues],
                "positive_index": positive_index,
                "trace_positive": str(trace_positive),
                "hs_squared": str(hs_sq),
            }
        )
    return {"fixtures": rows}


def model_and_record_checks() -> dict[str, object]:
    q = F(1, 50)
    theta_upper = 1 + 2 * q / (1 - q)
    require(theta_upper == F(51, 49), "Toeplitz theta upper bound")
    eta_gamma = 1 / theta_upper
    require(eta_gamma == F(49, 51), "gamma effective rank")

    eta_robust = eta_gamma * F(99, 101) ** 2
    require(eta_robust == F(160083, 173417), "robust effective rank mutation")
    require(eta_robust > F(919, 1000), "one-percent reserve no longer clears target")

    b = F(5429, 6250)
    nuisance = F(821, 10000)
    target_eta = F(919, 1000)
    record_target = 2 * target_eta - 1 - 2 * nuisance
    require(record_target == F(3369, 5000), "record target mutation")

    published_upper = F(672501, 1_000_000)
    require(record_target > published_upper, "target no longer exceeds published MT upper decimal")

    robust_output = 2 * eta_robust - 1 - 2 * nuisance
    require(robust_output == F(591369643, 867085000), "robust output mutation")
    require(robust_output > F(682, 1000), "robust output lost 0.682 threshold")

    # A one-dimensional compression cannot certify positive density by inertia.
    for total in (2, 10, 100, 10_000):
        require(F(1, total) <= F(1, 2), "rank-one firewall")

    return {
        "toeplitz_q": str(q),
        "gamma_effective_rank_lower": str(eta_gamma),
        "robust_effective_rank_lower": str(eta_robust),
        "record_eta_target": str(target_eta),
        "multiplicity_counted_line_target": str(record_target),
        "published_mt_decimal_upper_import": str(published_upper),
        "robust_line_target": str(robust_output),
    }


def content_hashes() -> dict[str, str]:
    values: dict[str, str] = {}
    for relative in CONTENT_FILES:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        values[relative] = hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
    return values


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "verdict": VERDICT,
        "pick_kernel": pick_kernel_fixture(),
        "confluent_budget": confluent_budget_checks(),
        "rank_trace": rank_trace_checks(),
        "model_and_record": model_and_record_checks(),
        "content_sha256": content_hashes(),
        "imported_anthropic_theorems_machine_reproved": False,
        "cauchy_power_model_limit_machine_proved": False,
        "lprt105310_proved": False,
        "simple_parent_upgrade_proved": False,
        "new_zero_proportion_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    print(VERDICT)
    print(payload["proof_object_sha256"])
    print("NEW_ZERO_PROPORTION_UNPROVED")
    print("RH_UNPROVED")


if __name__ == "__main__":
    main()
