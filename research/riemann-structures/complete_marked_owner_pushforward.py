#!/usr/bin/env python3
"""Primitive complete-owner replay plus an independent exact class-count formula."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "COMPLETE_MARKED_OWNER_PUSHFORWARD.md"
LOCK = HERE / "complete_marked_owner_pushforward.sources.json"
FIXTURE = HERE / "complete_marked_owner_pushforward.json"
SCOUT = HERE / "marked_owner_pushforward_scout.py"
TEST = ROOT / "tests" / "test_complete_marked_owner_pushforward.py"
MAX_BYTES = 131_072
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCES = {
    (
        FAMILY,
        "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
    ): "346cc52420ec65457c2a5accc045d4a85635cc24",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        FAMILY,
        "claims/lemmas/L-106131-wick-normal-ordering-additive-kummer-decomposition.md",
    ): "37722c3f36ec7d1681f34d4329a3795e5028f7ae",
    (
        FAMILY,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        FAMILY,
        "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
    ): "388c7e166a0e6e534d7e908685f71a16de246575",
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md",
    ): "db018c64dde45ff4ad17541eb6ba00b4f6fa9d49",
    (
        "a30276a5be049749ebb2147f30f000dd5659298b",
        "research/l-families/atlas/function_field/FFPS_MARKED_PLACE_SIGNED_DESCENT_GATE0.md",
    ): "aad29a0401d0f26c3dceadaaaaf017af6da95ec1",
    (
        "b870366141fe8d5f43d5b81f6e50a67d2a888070",
        "research/l-families/atlas/function_field/FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md",
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
}
CLASSES = tuple(product((-1, 1), repeat=2))
CASES = ((5, 6), (5, 7), (5, 12), (6, 12))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate_sources() -> list[dict[str, object]]:
    raw = LOCK.read_bytes()
    require(len(raw) <= MAX_BYTES, "manifest byte cap")
    manifest = json.loads(raw)
    require(
        manifest.get("schema") == "riemann.complete_marked_owner.sources.v1",
        "source schema",
    )
    rows = manifest.get("sources")
    require(type(rows) is list and len(rows) == len(SOURCES), "source count")
    seen, result = set(), []
    for row in rows:
        require(type(row) is dict, "source row")
        key = (row.get("commit"), row.get("path"))
        require(key in SOURCES and key not in seen, "source identity/duplicate")
        require(row.get("git_blob") == SOURCES[key], "manifest blob mismatch")
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
        source = subprocess.run(
            ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
        ).stdout
        require(len(source) == size, "source byte count")
        blob = sha1(b"blob " + str(size).encode() + b"\0" + source).hexdigest()
        require(blob == SOURCES[key], "primitive source bytes")
        seen.add(key)
        result.append({**row, "bytes": size})
    require(seen == set(SOURCES), "complete source coverage")
    return result


def load_scout():
    require(SCOUT.stat().st_size <= MAX_BYTES, "local producer source cap")
    spec = importlib.util.spec_from_file_location("marked_owner_primitive", SCOUT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def class_formula(n: int, alpha: int, beta: int, omega: int) -> dict[str, int]:
    require(
        all(type(x) is int for x in (n, alpha, beta, omega)), "integer moment types"
    )
    require(4 <= n and n.bit_length() <= 512, "count bit cap")
    require(max(abs(alpha), abs(beta), abs(omega)) <= n, "sign moment range")
    a = n * (n - 1) * (n - 2) * (n - 3)
    b = (n - 2) * (n - 3) * (alpha * alpha - n)
    c = (n - 2) * (n - 3) * (beta * beta - n)
    t = (
        alpha**2 * beta**2
        - (n - 4) * (alpha**2 + beta**2)
        - 4 * omega * alpha * beta
        + n**2
        + 2 * omega**2
        - 6 * n
    )
    result = {}
    for sigma, tau in CLASSES:
        numerator = a + tau * b + sigma * c + sigma * tau * t
        require(
            numerator >= 0 and numerator % 16 == 0, "integral nonnegative source count"
        )
        result[str((sigma, tau))] = numerator // 16
    require(sum(result.values()) == a // 4, "total owner configurations")
    return result


def principal_integer(counts: dict[str, int]) -> int:
    require(
        type(counts) is dict and set(counts) == {str(key) for key in CLASSES},
        "class coverage",
    )
    require(
        all(
            type(n) is int and n >= 0 and n.bit_length() <= 2048
            for n in counts.values()
        ),
        "class count cap/type",
    )
    return sum(1296 * n * n - 36 * n for n in counts.values())


def norm_character(field, x):
    a, b = x % field.p, x // field.p
    norm = (a * a - field.nonsquare * b * b) % field.p
    require(norm != 0, "nonzero character argument")
    value = pow(norm, (field.p - 1) // 2, field.p)
    return 1 if value == 1 else -1


def independent_root_data(field, lam, rho):
    excluded = {0, 1, 2, 3, lam, rho}
    require(len(excluded) == 6, "clean independent marked data")
    bins = Counter({key: 0 for key in CLASSES})
    alpha = beta = omega = 0
    for root in range(field.q):
        if root in excluded:
            continue
        u = norm_character(field, field.sub(rho, root))
        v = norm_character(field, field.sub(lam, root))
        bins[(u, v)] += 1
        alpha += u
        beta += v
        omega += u * v
    return bins, (field.q - 6, alpha, beta, omega)


def category_count(bins) -> dict[str, int]:
    require(
        set(bins) == set(CLASSES)
        and all(type(x) is int and 0 <= x <= 49 for x in bins.values()),
        "bounded sign categories",
    )
    counts = Counter({key: 0 for key in CLASSES})
    for categories in product(CLASSES, repeat=4):
        multiplicities = Counter(categories)
        weight = 1
        for category, multiplicity in multiplicities.items():
            if bins[category] < multiplicity:
                weight = 0
                break
            weight *= prod(bins[category] - i for i in range(multiplicity))
        sigma = categories[2][1] * categories[3][1]
        tau = categories[0][0] * categories[1][0]
        counts[(sigma, tau)] += weight
    require(all(value % 4 == 0 for value in counts.values()), "free pair-swap quotient")
    return {str(key): counts[key] // 4 for key in CLASSES}


def history_record():
    histories = []
    for allocation in product(range(3), repeat=4):
        counts = [allocation.count(i) for i in range(3)]
        a_left = max(counts[0] - 1, 0)
        a_right = max(counts[1] - 1, 0)
        coefficient = a_left * a_right * (-1) ** counts[2]
        if coefficient:
            histories.append(
                {"allocation": list(allocation), "coefficient": coefficient}
            )
    require(
        len(histories) == 6 and all(row["coefficient"] == 1 for row in histories),
        "complete degree-four Boolean history",
    )
    q = 25
    one_history = Fraction(1, 15 * q**5)
    bilateral_history = one_history * one_history
    source_dual_history = q**5 * bilateral_history
    principal_weight = Fraction(q + 1, q - 1) ** 2 / q**2
    prefactor = principal_weight * source_dual_history**2
    require(
        prefactor == Fraction(q + 1, q - 1) ** 2 / (225**2 * q**12),
        "native principal prefactor",
    )
    return {
        "one_sided_histories": histories,
        "bilateral_histories": 36,
        "equal_pair_share": "1/15",
        "q25_one_history": str(one_history),
        "q25_bilateral_history": str(bilateral_history),
        "q25_principal_prefactor": str(prefactor),
        "wick_polynomial": "1296*K^2-36*K",
        "ordered_owner_counting_weight": "1/4",
        "integral_virtual_class": "81*T*T-36*T; trace(T)=16*K; trace(class)=16*J",
        "integral_parent_prefactor": str(prefactor / 16),
    }


def cofinal_record(m: int) -> dict[str, object]:
    require(
        type(m) is int and 1 <= m <= 27 and m % 2 == 1, "bounded odd extension control"
    )
    q, n = 25**m, 25**m - 6
    before, after = class_formula(n, -1, 1, 1), class_formula(n, 1, 3, 1)
    defect = principal_integer(after) - principal_integer(before)
    factorized = 324 * (n - 3) ** 2 * ((n - 2) ** 2 * (5 - n) - (n - 9))
    require(defect == factorized and defect < 0, "cofinal symbolic defect identity")
    return {
        "odd_extension_degree": m,
        "q": q,
        "available_roots": n,
        "before": before,
        "after": after,
        "integer_defect": defect,
        "enumerated_over_this_field": m == 1,
        "weighted_defect_without_common_observation_mass": str(
            Fraction(q + 1, q - 1) ** 2 * defect / (225**2 * q**12)
        ),
    }


def build() -> dict[str, object]:
    sources = authenticate_sources()
    hashes = {}
    for path in (Path(__file__), SCOUT, NOTE, LOCK, TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    module = load_scout()
    field = module.Field(5, 2)
    cases = []
    for lam, rho in CASES:
        transforms = {
            "original": (lam, rho),
            "left_partial": (field.power(lam, 5), rho),
            "total": (field.power(lam, 5), field.power(rho, 5)),
        }
        records = {}
        for name, (left, right) in transforms.items():
            native = module.fibre(field, left, right, 1, 2)
            bins, moments = independent_root_data(field, left, right)
            formula = class_formula(*moments)
            require(
                formula == category_count(bins) == native["quadratic_class_counts"],
                "three independent complete-owner counts",
            )
            require(
                principal_integer(formula) == native["integer_principal_literal_wick"],
                "literal principal polynomial",
            )
            records[name] = {
                **native,
                "sign_moments": list(moments),
                "root_sign_categories": {str(key): bins[key] for key in CLASSES},
            }
        require(
            records["original"]["quadratic_class_counts"]
            == records["total"]["quadratic_class_counts"],
            "total Frobenius class control",
        )
        require(
            records["original"]["exact_additive_characters"]
            == records["total"]["exact_additive_characters"],
            "total Frobenius additive control",
        )
        cases.append(records)
    first = cases[0]
    require(
        first["original"]["sign_moments"] == [19, -1, 1, 1]
        and first["left_partial"]["sign_moments"] == [19, 1, 3, 1],
        "primitive cofinal sign seed",
    )
    require(
        first["left_partial"]["integer_principal_literal_wick"]
        - first["original"]["integer_principal_literal_wick"]
        == -336420864,
        "exact nonzero source witness",
    )
    result = {
        "schema": "riemann.complete_marked_owner.v1",
        "sources": sources,
        "source_hashes": hashes,
        "arithmetic": "EXACT_FINITE_FIELD_INTEGER_RATIONAL_CYCLOTOMIC",
        "owner_coverage": "EVERY_UNORDERED_DISJOINT_OWNER_PAIR_AT_EACH_OF_TWELVE_FIXED_F25_FIBRES",
        "cases": cases,
        "history_normalization": history_record(),
        "cofinal_formula_controls": [cofinal_record(m) for m in (1, 3, 9)],
        "cofinal_theorem_proved_by_formula_not_enumeration": True,
        "full_carrier_binding_asserted": False,
        "RH_or_GRH_conclusion": False,
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
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(
            canonical(candidate) == canonical(result),
            "canonical primitive replay mismatch",
        )
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
