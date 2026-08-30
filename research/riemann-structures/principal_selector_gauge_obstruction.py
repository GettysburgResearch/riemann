#!/usr/bin/env python3
"""Exact clean-record principal-weight test for a native prime-square gauge entry."""

from __future__ import annotations

import argparse
import json
import subprocess
import types
from fractions import Fraction
from hashlib import sha1, sha256
from math import factorial, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "PRINCIPAL_SELECTOR_GAUGE_OBSTRUCTION.md"
FIXTURE = HERE / "principal_selector_gauge_obstruction.json"
TEST = ROOT / "tests" / "test_principal_selector_gauge_obstruction.py"
EA = "5ef9a0800e7d0f03bfef1ad4ba467f8843a90058"
ALGEBRA_PATH = "research/riemann-structures/euler_activation_source_adapter.py"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCES = {
    (EA, ALGEBRA_PATH): "f8248cd97c4fc72ad4034d9baf83cec91396f27e",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md",
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        FAMILY,
        "claims/lemmas/L-106090-least-discrepancy-prime-triangularizes-the-coprime-boolean-core.md",
    ): "dadf3a4a65d2575983d692dafc0c94142c9a038d",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        FAMILY,
        "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
    ): "955c3ed0363ca330439eedbae1bf0041a4c96468",
    (
        FAMILY,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}
MAX_BYTES = 262144
P_OWNERS, Q_OWNERS = (11, 13), (17, 19)
WINDOWS = {
    "A": (Fraction(1), Fraction(101, 100)),
    "B": (Fraction(51, 50), Fraction(103, 100)),
    "C": (Fraction(6, 5), Fraction(121, 100)),
    "D": (Fraction(61, 50), Fraction(123, 100)),
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "frozen primitive identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen primitive Git blob")
    return raw


def load_boolean_algebra(raw):
    key = (EA, ALGEBRA_PATH)
    digest = sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "executable source blob")
    module = types.ModuleType("frozen_boolean_selector_algebra")
    module.__file__ = str(ROOT / ALGEBRA_PATH)
    # Execute only the fixed, rehashed Git primitive, never a working-tree file.
    exec(compile(raw, f"{EA}:{ALGEBRA_PATH}", "exec"), module.__dict__)  # noqa: S102
    return module


def prime(n: int) -> bool:
    require(type(n) is int and 2 <= n <= 1000000, "trial-prime cap/type")
    return all(n % divisor for divisor in range(2, isqrt(n) + 1))


def c_weight(q: int) -> Fraction:
    require(prime(q) and q > 2, "odd phase prime")
    return Fraction(q + 1, q - 1)


def state(left: tuple[int, ...], right: tuple[int, ...]) -> dict[str, object]:
    require(
        type(left) is tuple
        and type(right) is tuple
        and 1 <= len(left) <= 6
        and 1 <= len(right) <= 6,
        "bounded core labels",
    )
    require(
        len(set(left)) == len(left) and len(set(right)) == len(right),
        "squarefree cores",
    )
    require(all(prime(p) for p in left + right), "literal core primes")
    require(67 not in left + right, "duplicated physical label excluded")
    require(
        not set(left + right).intersection(P_OWNERS + Q_OWNERS),
        "clean owner/core incidence",
    )
    common = set(left).intersection(right)
    c_labels, d_labels = sorted(set(left) - common), sorted(set(right) - common)
    require(c_labels and d_labels, "two nontrivial reduced cores")
    ell, rho = c_labels[0], d_labels[0]
    require(ell != rho, "distinct canonical phases")
    g, c, d = prod(common), prod(c_labels), prod(d_labels)
    p, q = prod(P_OWNERS), prod(Q_OWNERS)
    a, b = prod(left), prod(right)
    n, physical_m = p * a * a, q * b * b
    require(a == g * c and b == g * d, "canonical common-core extraction")
    require(
        n % ell == 0
        and physical_m % ell != 0
        and physical_m % rho == 0
        and n % rho != 0,
        "nonzero phase incidence",
    )
    sigma = pow(q, (ell - 1) // 2, ell)
    tau = pow(p, (rho - 1) // 2, rho)
    require(sigma in (1, ell - 1) and tau in (1, rho - 1), "retained quadratic classes")
    weight = g * g * ell * rho * c_weight(ell) * c_weight(rho)
    return {
        "left_labels": list(left),
        "right_labels": list(right),
        "g": g,
        "c": c,
        "d": d,
        "ell": ell,
        "rho": rho,
        "N": n,
        "M": physical_m,
        "weight": str(weight),
        "physical_ratio": str(Fraction(n, physical_m)),
        "quadratic_classes": [1 if sigma == 1 else -1, 1 if tau == 1 else -1],
        "native_denominator_without_sqrt_PQ": g * g * c * d,
    }


def insertion(left, right, p: int, tau: Fraction) -> dict[str, object]:
    require(type(tau) is Fraction and 0 <= tau <= 1, "exact homotopy parameter")
    require(
        type(p) is int and p in right and p not in left,
        "opposite residual-prime insertion",
    )
    before = state(left, right)
    require(p not in set(left).intersection(right), "new common prime")
    after = state(tuple(sorted(left + (p,))), right)
    require(
        after["g"] == p * before["g"]
        and after["c"] == before["c"]
        and after["d"] * p == before["d"],
        "literal selector transport",
    )
    coefficient = -tau * (1 - tau) / (4 * p)
    exact = coefficient**2 * Fraction(after["weight"]) / Fraction(before["weight"])
    expected = (
        tau**2
        * (1 - tau) ** 2
        / 16
        * Fraction(after["rho"], before["rho"])
        * c_weight(after["rho"])
        / c_weight(before["rho"])
    )
    require(exact == expected, "principal selector weight cocycle")
    require(
        after["N"] == p * p * before["N"] and after["M"] == before["M"],
        "physical square shift",
    )
    require(
        after["native_denominator_without_sqrt_PQ"]
        == p * before["native_denominator_without_sqrt_PQ"],
        "source gamma normalization",
    )
    return {
        "before": before,
        "after": after,
        "gauge_physical_coefficient": str(coefficient),
        "weighted_matrix_entry_squared": str(exact),
    }


def sixth_root(n: int) -> int:
    require(type(n) is int and 1 <= n and n.bit_length() <= 256, "horizon bit cap")
    lo, hi = 0, 1 << ((n.bit_length() + 5) // 6)
    while lo + 1 < hi:
        middle = (lo + hi) // 2
        if middle**6 <= n:
            lo = middle
        else:
            hi = middle
    return hi if hi**6 <= n else lo


def symbolic_windows() -> dict[str, str]:
    a, b, c, d = (WINDOWS[key] for key in ("A", "B", "C", "D"))
    ratio_low = Fraction(3575, 2907) * (a[0] * b[0] / (c[1] * d[1])) ** 2
    ratio_high = Fraction(3575, 2907) * (a[1] * b[1] / (c[0] * d[0])) ** 2
    require(
        Fraction(1, 2) < ratio_low < ratio_high < Fraction(2, 3),
        "native ratio-eight input",
    )
    require(
        Fraction(9, 2) < 9 * ratio_low < 9 * ratio_high < 6, "native ratio-eight output"
    )
    n_prime_max = 9 * 143 * 25 * (a[1] * b[1]) ** 2
    m_max = 323 * 9 * (c[1] * d[1]) ** 2
    require(max(n_prime_max, m_max) < 40000, "common global horizon")
    return {
        "input_ratio_lower": str(ratio_low),
        "input_ratio_upper": str(ratio_high),
        "output_N_over_T4_upper": str(n_prime_max),
        "M_over_T4_upper": str(m_max),
    }


def build() -> dict[str, object]:
    raw = {key: source_bytes(key) for key in SOURCES}
    algebra = load_boolean_algebra(raw[(EA, ALGEBRA_PATH)])
    windows = symbolic_windows()
    t_scale = 1000
    primes = {"A": 1009, "B": 1021, "C": 1201, "D": 1223}
    for key, value in primes.items():
        require(prime(value), "exact fixed-fixture trial primality")
        require(
            WINDOWS[key][0] * t_scale < value < WINDOWS[key][1] * t_scale,
            "strict fixed prime window",
        )
    left, right = (5, primes["A"], primes["B"]), (3, primes["C"], primes["D"])
    record = insertion(left, right, 3, Fraction(1, 2))
    before, after = record["before"], record["after"]
    horizon = 40000 * t_scale**4
    cutoff = sixth_root(horizon)
    require(15 < cutoff < min(primes.values()), "live Boolean large/small split")
    require(
        max(before["N"], before["M"], after["N"], after["M"]) < horizon,
        "bounded horizon",
    )
    for item in (before, after):
        require(
            Fraction(1, 8) < Fraction(item["physical_ratio"]) < 8,
            "individual native shell ratio",
        )
    rows = {
        "before_left": algebra.boolean_rows(left, cutoff),
        "right": algebra.boolean_rows(right, cutoff),
        "after_left": algebra.boolean_rows(tuple(after["left_labels"]), cutoff),
    }
    require(
        [rows[key]["balanced"] for key in ("before_left", "right", "after_left")]
        == [-2, -2, 2],
        "live complete Boolean rows",
    )
    require(
        all(len(value["nonzero_balanced_histories"]) == 2 for value in rows.values()),
        "complete two-history support",
    )
    c = primes["C"]
    require(
        Fraction(before["weight"]) == 45
        and Fraction(after["weight"]) == Fraction(135, 2) * c * c_weight(c),
        "exact principal weights",
    )
    require(
        Fraction(record["weighted_matrix_entry_squared"]) == c * c_weight(c) / 1536,
        "power-loss native gauge entry",
    )
    beta_ratio = Fraction(factorial(10) * factorial(14), factorial(25)) / Fraction(
        factorial(8) * factorial(12), factorial(21)
    )
    require(beta_ratio == Fraction(273, 5060), "literal Euler path beta ratio")
    literal_ratio = c * c_weight(c) * beta_ratio / 96
    require(
        literal_ratio == Fraction(91, 161920) * c * c_weight(c),
        "literal-path weighted loss",
    )
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        data = path.read_bytes()
        require(len(data) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.principal_selector_gauge.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": blob}
            for key, blob in SOURCES.items()
        ],
        "source_hashes": hashes,
        "symbolic_window_bounds": windows,
        "fixed_primes": primes,
        "T": t_scale,
        "global_horizon": horizon,
        "Boolean_cutoff": cutoff,
        "native_transition": record,
        "complete_Boolean_rows": rows,
        "integrated_constant_path_squared_ratio": str(c * c_weight(c) / 2880),
        "literal_Euler_path_squared_ratio": str(literal_ratio),
        "single_unchanged_width_eight_shell_asserted": False,
        "retained_gauge_provenance_not_fresh_owner_reallocation": True,
        "complete_principal_vector_counterexample_asserted": False,
        "cofinal_operator_power_loss_proved_symbolically": True,
        "new_prime_search": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "exact canonical replay")
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
