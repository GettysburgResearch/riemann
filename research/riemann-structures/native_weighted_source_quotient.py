#!/usr/bin/env python3
"""Bounded exact replay of native carrier and support-renewal interfaces."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import Counter
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import permutations, product
from math import factorial, isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "NATIVE_WEIGHTED_SOURCE_QUOTIENT.md"
LOCK = HERE / "native_weighted_source_quotient.sources.json"
FIXTURE = HERE / "native_weighted_source_quotient.json"
TEST = ROOT / "tests" / "test_native_weighted_source_quotient.py"
MAX_BYTES = 131_072
MAX_LABELS = 7
SOURCE_SHA = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
FAMILY_SHA = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCE_BLOBS = {
    (
        SOURCE_SHA,
        "claims/lemmas/L-102741-wick-gauge-and-exact-prime-carrier-quotient.md",
    ): "b526c4889f7027fee0fd1db69c41621cab8a0a23",
    (
        SOURCE_SHA,
        "claims/lemmas/L-102830-largest-two-owner-is-an-exact-subpower-gauge.md",
    ): "a96ecfee909abe684841171faa45e9c6682548f3",
    (
        SOURCE_SHA,
        "claims/lemmas/L-102831-largest-two-completion-produces-a-unique-semiprime-squareclass.md",
    ): "ca83a373043a18a6dc60b6eadb99646d6860199b",
    (
        SOURCE_SHA,
        "claims/lemmas/L-102860-balanced-cross-side-phase-after-common-factor-extraction.md",
    ): "39e336892eca5829d51ab312379226861a582de7",
    (
        SOURCE_SHA,
        "claims/lemmas/L-102862-owner-core-overlaps-are-a-polylogarithmic-common-factor-renewal.md",
    ): "28d16897b210c52869227688b6e2f2f6ae308b04",
    (
        SOURCE_SHA,
        "claims/lemmas/L-102904-endpoint-color-walsh-expansion-has-only-squared-activity-off-the-midpoint.md",
    ): "f0bdbf09e620027eafe9a198350f588edafdd269",
    (
        SOURCE_SHA,
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
    ): "6810bcece309b0c54ae6c8fc84b314990004549c",
    (
        FAMILY_SHA,
        "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
    ): "955c3ed0363ca330439eedbae1bf0041a4c96468",
    (
        FAMILY_SHA,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def authenticate_sources() -> list[dict[str, object]]:
    raw = LOCK.read_bytes()
    require(len(raw) <= MAX_BYTES, "manifest byte cap")
    manifest = json.loads(raw)
    require(
        manifest.get("schema") == "riemann.native_weighted_quotient.sources.v1",
        "source schema",
    )
    rows = manifest.get("sources")
    require(type(rows) is list and len(rows) == len(SOURCE_BLOBS), "source coverage")
    seen, result = set(), []
    for row in rows:
        require(type(row) is dict, "source row")
        key = (row.get("commit"), row.get("path"))
        require(key in SOURCE_BLOBS and key not in seen, "unknown or duplicate source")
        expected = SOURCE_BLOBS[key]
        require(row.get("git_blob") == expected, "manifest blob mismatch")
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
        require(0 < size <= MAX_BYTES, "primitive byte cap")
        source = subprocess.run(
            ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
        ).stdout
        require(len(source) == size, "source byte count")
        actual = sha1(b"blob " + str(size).encode() + b"\0" + source).hexdigest()
        require(actual == expected, "primitive source authentication")
        seen.add(key)
        result.append({**row, "bytes": size})
    require(seen == set(SOURCE_BLOBS), "complete source coverage")
    return result


def carrier_record(k: int) -> dict[str, object]:
    require(type(k) is int and 2 <= k <= MAX_LABELS, "carrier degree cap/type")
    coefficient = Fraction((-1) ** k, factorial(k))
    total, diagonal, count = Fraction(0), Fraction(0), 0
    for word in permutations(range(k)):
        require(len(set(word)) == k, "squarefree word")
        total += coefficient
        diagonal += coefficient * coefficient
        count += 1
    require(count == factorial(k), "word coverage")
    require(total == (-1) ** k, "native complete coefficient")
    require(diagonal == Fraction(1, factorial(k)), "word diagonal")
    occupation = total * total
    probability_diagonal = sum((occupation / count for _ in range(count)), Fraction(0))
    require(probability_diagonal == occupation, "probability measure repair")
    return {
        "degree": k,
        "ordered_words": count,
        "coefficient_per_word": str(coefficient),
        "complete_coefficient": str(total),
        "word_counting_diagonal": str(diagonal),
        "occupation_diagonal": str(occupation),
        "probability_diagonal": str(probability_diagonal),
        "diagonal_amplification": str(occupation / diagonal),
    }


def occupation_record(alpha: tuple[int, ...]) -> dict[str, object]:
    require(type(alpha) is tuple and 1 <= len(alpha) <= 4, "occupation tuple")
    require(
        all(type(a) is int and a >= 0 for a in alpha), "occupation nonnegative integers"
    )
    k = sum(alpha)
    require(1 <= k <= MAX_LABELS, "occupation degree cap")
    labels = tuple(
        i for i, multiplicity in enumerate(alpha) for _ in range(multiplicity)
    )
    words = set(permutations(labels))
    expected = factorial(k) // prod(factorial(a) for a in alpha)
    require(len(words) == expected, "multiset word coverage")
    word_coefficient = Fraction((-1) ** k, factorial(k))
    total = word_coefficient * len(words)
    native = Fraction((-1) ** k, prod(factorial(a) for a in alpha))
    require(total == native, "native occupation coefficient")
    return {
        "occupation": list(alpha),
        "words": len(words),
        "coefficient": str(native),
        "counting_diagonal": str(len(words) * word_coefficient**2),
        "occupation_diagonal": str(native**2),
    }


def support(value: tuple[int, ...]) -> tuple[int, ...]:
    require(type(value) is tuple and 1 <= len(value) <= MAX_LABELS, "support size/type")
    require(
        all(type(p) is int and 1 < p < 100 for p in value), "support label cap/type"
    )
    require(tuple(sorted(set(value))) == value, "ordered distinct support")
    require(
        all(all(p % d for d in range(2, isqrt(p) + 1)) for p in value), "prime support"
    )
    return value


def completed(value: tuple[int, ...]) -> int:
    value = support(value)
    require(len(value) >= 2, "two owners required")
    return prod(value[-2:]) * prod(value[:-2]) ** 2


def eligible(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    a, b = support(a), support(b)
    if min(len(a), len(b)) < 2 or set(a[-2:]) & set(b[-2:]):
        return ()
    result = tuple((0, p) for p in a[-2:] if p in b[:-2]) + tuple(
        (1, p) for p in b[-2:] if p in a[:-2]
    )
    require(len(result) <= 2, "Top2 branching")
    require(len({side for side, _ in result}) <= 1, "one-direction renewal")
    return result


def renewal_paths(
    a: tuple[int, ...], b: tuple[int, ...]
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], tuple[tuple[int, int], ...]], ...]:
    a, b = support(a), support(b)
    original_union = set(a) | set(b)
    require(len(original_union) <= MAX_LABELS, "renewal union cap")
    result = []

    def visit(left, right, path):
        require(set(left) | set(right) == original_union, "union support invariant")
        require(len({p for _, p in path}) == len(path), "no repeated extraction")
        options = eligible(left, right)
        if not options:
            result.append((left, right, path))
            return
        for side, prime in options:
            next_left = tuple(p for p in left if p != prime) if side == 0 else left
            next_right = tuple(p for p in right if p != prime) if side == 1 else right
            visit(next_left, next_right, (*path, (side, prime)))

    visit(a, b, ())
    require(len(result) <= 3 ** len(original_union), "ancestral path bound")
    return tuple(result)


def renewal_coverage() -> dict[str, object]:
    primes = (2, 3, 5, 7, 11, 13)
    outputs = Counter()
    ancestors = paths = 0
    for assignment in product((1, 2, 3), repeat=len(primes)):
        a = tuple(p for p, mask in zip(primes, assignment, strict=True) if mask & 1)
        b = tuple(p for p, mask in zip(primes, assignment, strict=True) if mask & 2)
        if min(len(a), len(b)) < 2 or set(a[-2:]) & set(b[-2:]):
            continue
        ancestors += 1
        for left, right, path in renewal_paths(a, b):
            outputs[(left, right)] += 1
            paths += 1
            require(len({side for side, _ in path}) <= 1, "path direction")
    for (a, b), count in outputs.items():
        bound = 3 ** len(set(b) - set(a)) + 3 ** len(set(a) - set(b)) - 1
        require(count <= bound, "terminal ancestry bound")
    return {
        "support": list(primes),
        "assignment_coverage": 3 ** len(primes),
        "hard_ancestors": ancestors,
        "terminal_outputs": len(outputs),
        "literal_paths": paths,
        "maximum_terminal_preimages": max(outputs.values()),
    }


def transport_record() -> dict[str, object]:
    a, b = (2, 3, 5, 7), (5, 7, 11, 13)
    n, m = completed(a), completed(b)
    require((n, m) == (1260, 175175), "native original products")
    prime = 7
    require((0, prime) in eligible(a, b), "legal first extraction")
    literal = (n // prime, m // prime)
    next_a = tuple(p for p in a if p != prime)
    recharted = (completed(next_a), completed(b))
    ratio = Fraction(n, m)
    require(Fraction(*literal) == ratio, "common extraction preserves ratio")
    defect = ratio / Fraction(*recharted)
    require(defect == 21, "recompletion ratio defect")
    terminal_pairs = {(left, right) for left, right, _ in renewal_paths(a, b)}
    other_terminals = {(left, right) for left, right, _ in renewal_paths(next_a, b)}
    common = ((2, 3), b)
    require(common in terminal_pairs & other_terminals, "shared clean terminal")
    require(not eligible(*common), "terminal overlap-free")
    terminal_ratio = Fraction(completed(common[0]), completed(common[1]))
    return {
        "original_supports": [list(a), list(b)],
        "original_owners": [list(a[-2:]), list(b[-2:])],
        "original_products": [n, m],
        "extracted_prime": prime,
        "literal_extracted_products": list(literal),
        "recompleted_owners": [list(next_a[-2:]), list(b[-2:])],
        "recompleted_products": list(recharted),
        "ratio_defect": str(defect),
        "terminal_products": [completed(common[0]), completed(common[1])],
        "ancestral_transport_ratios": [
            str(ratio / terminal_ratio),
            str(Fraction(*recharted) / terminal_ratio),
        ],
        "literal_extraction_intertwines": True,
        "bare_recompletion_intertwines": False,
    }


def build() -> dict[str, object]:
    sources = authenticate_sources()
    hashes = {}
    for path in (Path(__file__), NOTE, LOCK, TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.native_weighted_quotient.v1",
        "arithmetic": "EXACT_INTEGER_RATIONAL",
        "coverage": "DECLARED_SMALL_SOURCE_INTERFACES_NOT_COMPLETE_NATIVE_HORIZON",
        "sources": sources,
        "source_hashes": hashes,
        "carrier": [carrier_record(k) for k in range(2, 8)],
        "occupations": [
            occupation_record(a) for a in ((2, 1), (3, 2), (2, 2, 1), (1, 2, 1, 2))
        ],
        "renewal": renewal_coverage(),
        "transport": transport_record(),
        "full_principal_bound_proved": False,
        "T106140_word_atomization_asserted": False,
    }
    result["proof_object_sha256"] = sha256(canonical_json(result).encode()).hexdigest()
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
        require(
            canonical_json(json.loads(FIXTURE.read_text(encoding="utf-8")))
            == canonical_json(result),
            "canonical primitive replay mismatch",
        )
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
