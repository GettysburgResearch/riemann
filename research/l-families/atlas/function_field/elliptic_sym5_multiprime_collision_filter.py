#!/usr/bin/env python3
"""Bounded multi-prime filter for the locked q=31 Sym^5 trace collision.

The packet realizes the locked local trace pair (-7,3) using every good
short Weierstrass model y^2=x^3+A*x+B with -4<=A,B<=4, then tests the
resulting cross-pairs at four declared auxiliary primes.  It proves only a
finite compatibility firewall; it does not search for or rule out a global
motive, isogeny, functorial transfer, or compatible-system identity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_PATH = HERE / "elliptic_sym5_collision_diophantine_pilot.json"
OUTPUT_PATH = HERE / "elliptic_sym5_multiprime_collision_filter.json"
NOTE_PATH = HERE / "ELLIPTIC_SYM5_MULTIPRIME_COLLISION_FILTER.md"
TEST_PATH = ROOT / "tests" / "test_elliptic_sym5_multiprime_collision_filter.py"

EXPECTED_SOURCE_SHA256_LF = (
    "66635391ee4d69382eaf6d11fd78a77c90cffc8919ccbede9d0f568915cdf167"
)
MODEL_BOUND = 4
LOCKED_PRIME = 31
AUXILIARY_PRIMES = (5, 7, 11, 17)
MAX_SOURCE_ATOMS = 4_096

Model = tuple[int, int]


def _lf_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _canonical_payload_sha256(value: dict[str, object]) -> str:
    payload = dict(value)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(
        payload,
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _is_odd_prime(value: int) -> bool:
    if isinstance(value, bool) or not isinstance(value, int):
        return False
    if value < 3 or value % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


@dataclass
class ResourceGuard:
    cap: int = MAX_SOURCE_ATOMS
    total: int = 0
    ledger: dict[str, int] = field(default_factory=dict)

    def charge(self, label: str, amount: int = 1) -> None:
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise ValueError("resource charge must be a nonnegative integer")
        if self.total + amount >= self.cap:
            raise RuntimeError(
                f"resource cap is exclusive: {self.total}+{amount}>={self.cap}"
            )
        self.total += amount
        self.ledger[label] = self.ledger.get(label, 0) + amount


def load_locked_collision() -> dict[str, int]:
    actual_file_hash = _lf_sha256(SOURCE_PATH)
    if actual_file_hash != EXPECTED_SOURCE_SHA256_LF:
        raise ArithmeticError(
            f"locked Sym5 source drifted: {actual_file_hash} "
            f"!= {EXPECTED_SOURCE_SHA256_LF}"
        )
    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    claimed_payload = source.get("payload_sha256")
    if claimed_payload != _canonical_payload_sha256(source):
        raise ArithmeticError("locked Sym5 source payload hash failed")
    census = source.get("finite_census")
    if not isinstance(census, dict) or not isinstance(census.get("rows"), list):
        raise TypeError("locked Sym5 census lost its rows")
    row = next(
        (item for item in census["rows"] if int(item.get("q", -1)) == LOCKED_PRIME),
        None,
    )
    if not isinstance(row, dict) or not isinstance(row.get("pairs"), list):
        raise TypeError("locked q=31 collision row is missing")
    pair = next(
        (
            item
            for item in row["pairs"]
            if item.get("collision_class") == "general"
            and int(item.get("x", 0)) == -7
            and int(item.get("y", 0)) == 3
        ),
        None,
    )
    if not isinstance(pair, dict):
        raise ArithmeticError("locked q=31 general collision (-7,3) vanished")
    result = {
        "q": int(row["q"]),
        "left_trace": int(pair["x"]),
        "right_trace": int(pair["y"]),
        "scalar_trace": int(pair["scalar_trace"]),
        "first_separating_coefficient_degree": int(
            pair["first_separating_coefficient_degree"]
        ),
    }
    if result != {
        "q": 31,
        "left_trace": -7,
        "right_trace": 3,
        "scalar_trace": 5544,
        "first_separating_coefficient_degree": 2,
    }:
        raise ArithmeticError(f"locked q=31 collision changed: {result}")
    return result


def discriminant_core(model: Model) -> int:
    a, b = model
    return 4 * a**3 + 27 * b**2


def has_good_reduction(model: Model, prime: int) -> bool:
    if not _is_odd_prime(prime):
        raise ValueError("good-reduction test requires an odd prime")
    return discriminant_core(model) % prime != 0


def legendre_symbol(value: int, prime: int) -> int:
    if not _is_odd_prime(prime):
        raise ValueError("Legendre symbol requires an odd prime")
    residue = value % prime
    if residue == 0:
        return 0
    symbol = pow(residue, (prime - 1) // 2, prime)
    if symbol == 1:
        return 1
    if symbol == prime - 1:
        return -1
    raise ArithmeticError("Euler criterion returned an invalid residue")


def elliptic_trace(model: Model, prime: int, guard: ResourceGuard) -> int:
    if not has_good_reduction(model, prime):
        raise ValueError("trace requested at bad reduction")
    a, b = model
    guard.charge("finite_field_point_atoms", prime)
    return -sum(
        legendre_symbol(x**3 + a * x + b, prime) for x in range(prime)
    )


def symmetric_power_trace(base_trace: int, q: int, degree: int) -> int:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("symmetric-power degree must be a nonnegative integer")
    if degree == 0:
        return 1
    previous, current = 1, int(base_trace)
    for _ in range(2, degree + 1):
        previous, current = current, int(base_trace) * current - int(q) * previous
    return current


def models_with_trace(
    target: int, prime: int, bound: int, guard: ResourceGuard
) -> tuple[Model, ...]:
    return models_for_traces((target,), prime, bound, guard)[int(target)]


def models_for_traces(
    targets: tuple[int, ...], prime: int, bound: int, guard: ResourceGuard
) -> dict[int, tuple[Model, ...]]:
    if not targets or len(set(targets)) != len(targets):
        raise ValueError("trace targets must be nonempty and distinct")
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 0:
        raise ValueError("model bound must be a nonnegative integer")
    target_set = {int(target) for target in targets}
    result: dict[int, list[Model]] = {target: [] for target in target_set}
    for a in range(-bound, bound + 1):
        for b in range(-bound, bound + 1):
            model = (a, b)
            guard.charge("integral_model_candidates")
            if not has_good_reduction(model, prime):
                continue
            trace = elliptic_trace(model, prime, guard)
            if trace in target_set:
                result[trace].append(model)
    return {target: tuple(result[target]) for target in target_set}


def _model_record(model: Model) -> dict[str, object]:
    return {
        "A": model[0],
        "B": model[1],
        "discriminant_core": discriminant_core(model),
        "equation": f"y^2=x^3{model[0]:+d}*x{model[1]:+d}",
    }


def build_fixture() -> dict[str, object]:
    locked = load_locked_collision()
    guard = ResourceGuard()
    model_buckets = models_for_traces(
        (locked["left_trace"], locked["right_trace"]),
        LOCKED_PRIME,
        MODEL_BOUND,
        guard,
    )
    left_models = model_buckets[locked["left_trace"]]
    right_models = model_buckets[locked["right_trace"]]
    expected_left = ((-4, 4), (-3, -3), (3, 1))
    expected_right = ((-1, -1), (2, -4), (3, -2), (4, -2))
    if left_models != expected_left or right_models != expected_right:
        raise ArithmeticError(
            f"bounded realization census drifted: {left_models}, {right_models}"
        )

    cache: dict[tuple[Model, int], int | None] = {}
    for model in (*left_models, *right_models):
        for prime in AUXILIARY_PRIMES:
            guard.charge("auxiliary_model_prime_checks")
            cache[model, prime] = (
                elliptic_trace(model, prime, guard)
                if has_good_reduction(model, prime)
                else None
            )

    pairs = []
    first_separator_counts: Counter[int] = Counter()
    for left in left_models:
        for right in right_models:
            prime_rows = []
            first_separator = None
            for prime in AUXILIARY_PRIMES:
                left_trace = cache[left, prime]
                right_trace = cache[right, prime]
                if left_trace is None or right_trace is None:
                    prime_rows.append(
                        {
                            "prime": prime,
                            "status": "BAD_REDUCTION_SKIPPED",
                            "left_good": left_trace is not None,
                            "right_good": right_trace is not None,
                        }
                    )
                    continue
                left_sym5 = symmetric_power_trace(left_trace, prime, 5)
                right_sym5 = symmetric_power_trace(right_trace, prime, 5)
                equal = left_sym5 == right_sym5
                if not equal and first_separator is None:
                    first_separator = prime
                prime_rows.append(
                    {
                        "prime": prime,
                        "status": "GOOD_REDUCTION",
                        "left_trace": left_trace,
                        "right_trace": right_trace,
                        "left_sym5_scalar": left_sym5,
                        "right_sym5_scalar": right_sym5,
                        "sym5_scalar_equal": equal,
                    }
                )
            if first_separator is None:
                raise ArithmeticError(
                    f"declared auxiliary panel failed to separate {left}, {right}"
                )
            first_separator_counts[first_separator] += 1
            pairs.append(
                {
                    "left_model": list(left),
                    "right_model": list(right),
                    "locked_q31_sym5_scalar_equal": True,
                    "first_auxiliary_separating_prime": first_separator,
                    "auxiliary_rows": prime_rows,
                }
            )

    if first_separator_counts != Counter({5: 4, 7: 6, 11: 1, 17: 1}):
        raise ArithmeticError(
            f"auxiliary separation profile drifted: {first_separator_counts}"
        )
    if guard.total >= guard.cap:
        raise ArithmeticError("resource guard failed closed")

    source = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    return {
        "schema": "riemann.function_field.elliptic_sym5_multiprime_filter.v1",
        "status": "EXACT_BOUNDED_MULTIPRIME_COMPATIBILITY_FIREWALL",
        "locked_local_collision": locked,
        "model_box": {
            "coefficient_range": [-MODEL_BOUND, MODEL_BOUND],
            "model_type": "short Weierstrass y^2=x^3+A*x+B over Z",
            "measure": "coefficient models, not Q-isomorphism classes",
            "left_trace_models": [_model_record(model) for model in left_models],
            "right_trace_models": [_model_record(model) for model in right_models],
            "cross_pair_count": len(pairs),
        },
        "auxiliary_filter": {
            "primes_in_order": list(AUXILIARY_PRIMES),
            "all_cross_pairs_separated": True,
            "first_separator_counts": {
                str(prime): count
                for prime, count in sorted(first_separator_counts.items())
            },
            "pairs": pairs,
        },
        "interpretation": {
            "proved": (
                "all 12 cross-pairs of bounded integral models realizing the locked "
                "q=31 scalar collision split at a good auxiliary prime in "
                "{5,7,11,17}"
            ),
            "not_proved": [
                "classification of all integral curve models",
                "classification of all multi-prime spectral twins",
                "absence of an isogeny, correspondence, or compatible system outside the box",
                "any global L-function, zero, RH, or GRH statement",
            ],
            "next_target": (
                "replace the coefficient box by an isomorphism-invariant bounded-height "
                "catalogue and require equality of complete local factors at held-out primes"
            ),
        },
        "source_locks": {
            "path": str(SOURCE_PATH.relative_to(ROOT)).replace("\\", "/"),
            "file_sha256_lf": EXPECTED_SOURCE_SHA256_LF,
            "payload_sha256": source["payload_sha256"],
        },
        "resource_contract": {
            "exclusive_source_atom_cap": guard.cap,
            "accounted_source_atoms": guard.total,
            "ledger": dict(sorted(guard.ledger.items())),
            "random_sampling": False,
            "finite_field_model_enumeration": True,
            "enumeration_scope": (
                "81 short-Weierstrass coefficient candidates at q=31, then "
                "the seven retained models at four declared auxiliary primes"
            ),
            "source_atom_definition": (
                "one model candidate/check or one finite-field x-coordinate "
                "Legendre evaluation"
            ),
            "largest_field": LOCKED_PRIME,
        },
        "provenance": {
            "producer_sha256_lf": _lf_sha256(Path(__file__)),
            "note_sha256_lf": _lf_sha256(NOTE_PATH),
            "test_sha256_lf": _lf_sha256(TEST_PATH),
        },
    }


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    arguments = parser.parse_args()
    rendered = _canonical(build_fixture())
    if arguments.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("Sym5 multiprime collision-filter fixture drifted")
        print("PASS_SYM5_MULTIPRIME_COLLISION_FILTER")
        return
    if arguments.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
