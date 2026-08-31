"""Exact Boolean controls for a bounded native-source acquisition audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "native_tuple_source_acquisition"
BASE = "1904d20cdb76ecd26e0e63472625da930075303e"
NOTE = HERE / "NATIVE_TUPLE_SOURCE_ACQUISITION.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
MAX_BYTES, MAX_NODES, MAX_DEPTH, MAX_SUPPORT = 2_000_000, 100_000, 20, 8
BINDINGS = [
    {
        "id": "DIAGNOSTIC",
        "commit": "1904d20cdb76ecd26e0e63472625da930075303e",
        "path": "research/exploratory/NATIVE_BOOLEAN_DECODER_DIAGNOSTIC.md",
        "git_blob": "7cebffd3b6b0db96128755e392f622029a74435a",
        "sha256_lf": "6694dc66c23f1f3cc833c0d71ddb3243d84c524fa13c78905ec5684ceb5eea4a",
        "role": "Exact U64 tuple, literal histories and missing complete native weights",
    },
    {
        "id": "BOOLEAN",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
        "git_blob": "346cc52420ec65457c2a5accc045d4a85635cc24",
        "sha256_lf": "8efc34b198fe4bc642f6292bb0cfc4b937922a25b0e3cee35bdc2e51a62e5b7d",
        "role": "Complete disjoint triple-history source",
    },
    {
        "id": "BETA",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md",
        "git_blob": "b988b14eb982504a799158eed4c76e7f033c96f0",
        "sha256_lf": "2c38355491c82c85886b9b528c4a79d492b74f32ed133d2f1335cd1e6b133a4f",
        "role": "Exact rational Beta measure and half-source",
    },
    {
        "id": "AMPLIFIER",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106093-mellin-polarization-places-the-anchor-inside-one-amplified-family-moment.md",
        "git_blob": "cb8665b8cdbe2bc7e6eb223d6bc009e8e4f5a5df",
        "sha256_lf": "11c781a133698ab823c60e2f44036ce04b19789d33baa8a3f78e0afdc185af74",
        "role": "Complete A_alpha and anchor-dependent incidence before squaring",
    },
    {
        "id": "PLANCHEREL",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
        "git_blob": "388c7e166a0e6e534d7e908685f71a16de246575",
        "sha256_lf": "1f2259fde8b6763c878354d09b13c7bd858b16dddd7b7784d43e53e52ad77fee",
        "role": "Finite source-owned omega_i retained in exact observation",
    },
    {
        "id": "TARGET",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
        "git_blob": "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
        "sha256_lf": "54592d5d8d67dd797f9aa2d134ab4825e8ccc52c3ed18edefaf226ea0852eb1d",
        "role": "Complete retained principal member and literal diagonal",
    },
    {
        "id": "SOURCE_FIRST",
        "commit": "b79aa2dcddd27a84d629e39fbbf39d31e5470aac",
        "path": "research/riemann-structures/SOURCE_FIRST_BOOLEAN_PRINCIPAL_ADAPTER.md",
        "git_blob": "c37145331aedf3c6a4ec0c70577a66da712a5edd",
        "sha256_lf": "9aecec7c149e90a2262b75ff137cb99b64e5a90dec258946537107e74699ae59",
        "role": "Squarefree quotient before completion; trivial induced gauge, spectator limitation",
    },
    {
        "id": "OBSERVATION_GAP",
        "commit": "b79aa2dcddd27a84d629e39fbbf39d31e5470aac",
        "path": "research/riemann-structures/NATIVE_DECODER_OBSERVATION_GAP.md",
        "git_blob": "1e069c3353406924d9ffee0751ffd5fa81dbbc7d",
        "sha256_lf": "2af45d0c47d49a442e46c95a857cb8f7ef1e6d506e2c54cc325dd6c050ec7e39",
        "role": "Prior norm/observation interface audit; no native decoder inferred",
    },
    {
        "id": "ACQUISITION",
        "commit": "b79aa2dcddd27a84d629e39fbbf39d31e5470aac",
        "path": "research/riemann-structures/NEXT_NATIVE_DECODER_GATE.md",
        "git_blob": "d36fc9cc8f22be90a03d56ab1d43f186192e419a",
        "sha256_lf": "439d16814b62d72cce09a47e9b482806032d69d206480af5f148842241ae01e3",
        "role": "Latest prescribed native acquisition route and stop condition",
    },
    {
        "id": "RANGE",
        "commit": "b79aa2dcddd27a84d629e39fbbf39d31e5470aac",
        "path": "research/riemann-structures/FIXED_CORE_OWNER_RANGE_CORRECTION.md",
        "git_blob": "8813e809f12e7c0d2736869d66658fb494e5064a",
        "sha256_lf": "d89e2f7ffae27b0b1fe4e266f62fc736f2de8c87bc0a609a20296c658d004716",
        "role": "Full cores Q<=2gc and P<=2gd; no uniform extra g^-2 energy saving",
    },
    {
        "id": "EULER",
        "commit": "b79aa2dcddd27a84d629e39fbbf39d31e5470aac",
        "path": "research/riemann-structures/EULER_ACTIVATION_SOURCE_ADAPTER.md",
        "git_blob": "8632b4442b9610535078ef55a97b46a77a342dfe",
        "sha256_lf": "1977a5e7cef25cd5fac017213f07bae7296c29b50affe8fafab1b690fd1e9e53",
        "role": "Raw mixed-monomial projection is not the source-first completed source",
    },
]
CONTRACT = {
    "native_reconstruction_complete": False,
    "native_zero_or_nonzero": "undetermined",
    "arithmetic": "exact integer coverage and exact rational",
    "source_order": "raw squarefree quotient before Boolean owner completion",
    "measure": "Beta theta and Euler tau are separate declared integrals",
    "character": "signed history permutation character; no native group action",
    "range": "Q<=2gc and P<=2gd; no uniform coherent g^-2 saving",
    "excluded": "full gamma decoder, principal bound, native cancellation, RH",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lower, upper):
    require(type(value) is int and lower <= value <= upper, "strict integer/cap")
    return value


def rational(value):
    require(type(value) in (int, Q), "strict rational type")
    result = Q(value)
    require(
        max(abs(result.numerator).bit_length(), result.denominator.bit_length()) <= 256,
        "rational bit cap",
    )
    return result


def pair(value):
    value = rational(value)
    return [value.numerator, value.denominator]


def lf(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte/source size cap")
    result = raw.replace(b"\r\n", b"\n")
    decoded = result.decode("utf-8")
    require(
        all(ord(c) in (9, 10) or ord(c) >= 32 for c in decoded)
        and not any(127 <= ord(c) <= 159 for c in decoded),
        "source control byte",
    )
    return result


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def validate_tree(value, depth=0, budget=None):
    budget = [0] if budget is None else budget
    budget[0] += 1
    require(depth <= MAX_DEPTH and budget[0] <= MAX_NODES, "JSON tree cap")
    if type(value) is str:
        require(len(value) <= MAX_BYTES, "JSON string cap")
        return
    if value is None or type(value) is bool:
        return
    if type(value) is int:
        require(value.bit_length() <= 256, "JSON integer bit cap")
        return
    require(type(value) in (list, dict), "JSON type")
    require(len(value) <= MAX_NODES, "JSON container cap")
    if type(value) is dict:
        require(
            all(type(k) is str and len(k) <= 1024 for k in value),
            "JSON string keys",
        )
        children = value.values()
    else:
        children = value
    for child in children:
        validate_tree(child, depth + 1, budget)


def canonical(value):
    validate_tree(value)
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    require(len(result) <= MAX_BYTES, "canonical size cap")
    return result.encode("ascii")


def pairs_unique(items):
    result = {}
    for key, value in items:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def load_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def reject(_):
        raise ValueError("noninteger JSON number")

    value = json.loads(
        raw,
        object_pairs_hook=pairs_unique,
        parse_float=reject,
        parse_constant=reject,
    )
    validate_tree(value)
    return value


def manifest():
    return {
        "schema": "native-tuple-source-acquisition-sources-v1",
        "authoring_base": BASE,
        "contract": CONTRACT,
        "frozen_sources": BINDINGS,
    }


def read_source(binding):
    return subprocess.check_output(
        ["git", "show", binding["commit"] + ":" + binding["path"]], cwd=ROOT
    )


def authenticate():
    require(
        canonical(load_json(MANIFEST.read_bytes())) == canonical(manifest()),
        "manifest mismatch",
    )
    for binding in BINDINGS:
        raw = read_source(binding)
        normalized = lf(raw)
        blob = hashlib.sha1(
            b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
        ).hexdigest()
        require(blob == binding["git_blob"], "frozen Git blob mismatch")
        require(digest(normalized) == binding["sha256_lf"], "frozen source hash")
    return BINDINGS


def prime(n):
    integer(n, 2, 1_000_000)
    return all(n % k for k in range(2, math.isqrt(n) + 1))


def support(values):
    require(type(values) in (tuple, list), "support sequence type")
    require(len(values) <= MAX_SUPPORT, "support cap")
    require(all(prime(p) for p in values), "support primality")
    require(len(set(values)) == len(values), "duplicate prime")
    return tuple(values)


def a_u(values, cutoff):
    values = support(values)
    integer(cutoff, 1, 1_000_000)
    total = 0
    for bits in product((0, 1), repeat=len(values)):
        divisor = math.prod(p for p, bit in zip(values, bits) if bit)
        if divisor <= cutoff:
            total += (-1) ** sum(bits)
    return int(not values) - total


def histories(values, cutoff):
    values = support(values)
    integer(cutoff, 1, 1_000_000)
    answer = []
    for assignment in product(range(3), repeat=len(values)):
        parts = [
            tuple(p for p, colour in zip(values, assignment) if colour == j)
            for j in range(3)
        ]
        coefficient = a_u(parts[0], cutoff) * a_u(parts[1], cutoff)
        coefficient *= (-1) ** len(parts[2])
        if coefficient:
            answer.append(
                {
                    "assignment": list(assignment),
                    "products": [math.prod(part) for part in parts],
                    "coefficient": coefficient,
                }
            )
    return answer


def half_source(values, cutoff):
    values = support(values)
    total = Q(0)
    for bits in product((0, 1), repeat=len(values)):
        chosen = tuple(p for p, bit in zip(values, bits) if bit)
        total += a_u(chosen, cutoff) * Q(-1, 2) ** (len(values) - len(chosen))
    return rational(total)


def balanced_half(values, cutoff):
    values = support(values)
    total = Q(0)
    for bits in product((0, 1), repeat=len(values)):
        left = tuple(p for p, bit in zip(values, bits) if bit)
        right = tuple(p for p, bit in zip(values, bits) if not bit)
        total += half_source(left, cutoff) * half_source(right, cutoff)
    return rational(total)


def integral(coefficients):
    require(type(coefficients) in (list, tuple), "polynomial sequence")
    require(len(coefficients) <= 24, "polynomial degree cap")
    return rational(
        sum((rational(c) / (i + 1) for i, c in enumerate(coefficients)), Q(0))
    )


def beta_owner(core_depth):
    j = integer(core_depth, 1, MAX_SUPPORT)
    mu = (-1) ** j
    owner = [Q(0)] + [Q(2 * mu * (-1) ** i * math.comb(j, i)) for i in range(j + 1)]
    core = [Q(0), Q(0)] + [
        Q(-j * mu * (-1) ** i * math.comb(j - 1, i)) for i in range(j)
    ]
    return integral(owner), integral(core)


def permutation(values):
    require(type(values) in (list, tuple), "permutation sequence")
    n = len(values)
    integer(n, 1, MAX_SUPPORT)
    require(all(type(x) is int for x in values), "permutation strict integers")
    require(sorted(values) == list(range(n)), "invalid permutation")
    return tuple(values)


def cycles(values):
    values = permutation(values)
    seen, lengths = set(), []
    for start in range(len(values)):
        if start in seen:
            continue
        current, count = start, 0
        while current not in seen:
            seen.add(current)
            current = values[current]
            count += 1
        lengths.append(count)
    return sorted(lengths, reverse=True)


def character_formula(values):
    lengths = cycles(values)
    odd = sum(n % 2 for n in lengths)
    even = len(lengths) - odd
    return 3**even - 2 * int(odd == 0) * 2**even + (-1) ** odd


def character_direct(values):
    values = permutation(values)
    positive = negative = 0
    for assignment in product(range(3), repeat=len(values)):
        if 0 not in assignment or 1 not in assignment:
            continue
        if any(assignment[i] != assignment[values[i]] for i in range(len(values))):
            continue
        if assignment.count(2) % 2:
            negative += 1
        else:
            positive += 1
    return positive, negative


def partitions(n, limit=None):
    integer(n, 0, MAX_SUPPORT)
    limit = n if limit is None else integer(limit, 1, MAX_SUPPORT)
    if n == 0:
        yield ()
        return
    for head in range(min(n, limit), 0, -1):
        for tail in partitions(n - head, head):
            yield (head,) + tail


def representative(lengths):
    require(type(lengths) in (tuple, list), "cycle list")
    require(bool(lengths), "empty cycle list")
    require(all(type(n) is int and n >= 1 for n in lengths), "strict cycle lengths")
    require(sum(lengths) <= MAX_SUPPORT, "cycle size cap")
    result, offset = [], 0
    for length in lengths:
        result.extend(list(range(offset + 1, offset + length)) + [offset])
        offset += length
    return permutation(result)


def tuple_record():
    cutoff, left, right = 64, (71, 73, 79), (401, 421)
    p, q, g = 6, 35, 1
    c, d, y = math.prod(left), math.prod(right), cutoff**6
    n, m = p * c * c, q * d * d
    lhs, rhs = histories(left, cutoff), histories(right, cutoff)
    lsum, rsum = (sum(row["coefficient"] for row in rows) for rows in (lhs, rhs))
    require(balanced_half(left, cutoff) == lsum, "left independent half-source")
    require(balanced_half(right, cutoff) == rsum, "right independent half-source")
    bilateral = [Q(a["coefficient"] * b["coefficient"], 60) for a in lhs for b in rhs]
    require(n <= 16 * y and m <= 16 * y, "horizon")
    require(Q(1, 8) < Q(n, m) < 8, "ratio eight")
    point = Q(31 * y, 16)
    require(y < point < 2 * y and 1 < n / point < 8 and 1 < m / point < 8, "support")
    require(q <= 2 * g * c and p <= 2 * g * d, "full core ranges")
    return {
        "U": cutoff,
        "Y": y,
        "tuple_P_Q_g_c_d": [p, q, g, c, d],
        "physical_N_M": [n, m],
        "interior_point": pair(point),
        "least_primes": [71, 401],
        "physical_residue": [(-q * d * d) % 71, (p * c * c) % 401],
        "left_histories": lhs,
        "right_histories": rhs,
        "left_half_source": pair(half_source(left, cutoff)),
        "right_half_source": pair(half_source(right, cutoff)),
        "balanced_coefficients": [lsum, rsum],
        "bilateral_coefficients": [pair(v) for v in bilateral],
        "bilateral_sum": pair(sum(bilateral, Q(0))),
        "literal_diagonal": pair(sum((v * v for v in bilateral), Q(0))),
        "physical_squared_prefactor": pair(Q(1, g**4 * c * c * d * d * p * q)),
    }


def parameter_records():
    answer = []
    for j, balanced in ((3, 0), (2, 2)):
        depth = j + 2
        share = Q(balanced, math.comb(depth, 2))
        beta_polynomial = [Q(0)] * j + [Q(2 * balanced), Q(-2 * balanced)]
        beta_value = integral(beta_polynomial)
        require(beta_value == share, "Beta share")
        raw_owner, raw_core = beta_owner(j)
        require(raw_owner == Q((-1) ** j, math.comb(depth, 2)), "Beta factorial route")
        require(raw_core == -raw_owner, "raw full derivative")
        answer.append(
            {
                "core_depth": j,
                "Beta_theta_density": [pair(v) for v in beta_polynomial],
                "Beta_integral": pair(beta_value),
                "source_first_tau_path": [pair(Q(0))] * depth + [pair(share)],
                "source_first_complete_derivative_integral": pair(share),
                "source_first_owner_integral": pair(Q(2, depth) * share),
                "source_first_core_integral": pair(Q(j, depth) * share),
                "raw_mixed_owner_integral": pair(raw_owner),
                "raw_mixed_core_integral": pair(raw_core),
            }
        )
    return answer


def character_records():
    answer = []
    for n in range(1, 8):
        for partition in partitions(n):
            sigma = representative(partition)
            plus, minus = character_direct(sigma)
            value = character_formula(sigma)
            require(plus - minus == value, "independent character reconstruction")
            answer.append(
                {
                    "degree": n,
                    "cycle_type": list(partition),
                    "permutation": list(sigma),
                    "fixed_positive": plus,
                    "fixed_negative": minus,
                    "virtual_character": value,
                }
            )
    return answer


def seal(report):
    require(type(report) is dict and "payload_sha256" not in report, "seal input")
    return {**report, "payload_sha256": digest(canonical(report))}


def build_report():
    authenticate()
    artifacts = {
        path.relative_to(ROOT).as_posix(): digest(lf(path.read_bytes()))
        for path in (NOTE, Path(__file__), MANIFEST, TEST)
    }
    return seal(
        {
            "schema": "native-tuple-source-acquisition-v1",
            "contract": CONTRACT,
            "frozen_sources": BINDINGS,
            "tuple": tuple_record(),
            "parameters": parameter_records(),
            "characters": character_records(),
            "artifacts": artifacts,
        }
    )


def check_report(report):
    validate_tree(report)
    require(type(report) is dict and "payload_sha256" in report, "report shape")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(report["payload_sha256"] == digest(canonical(unsigned)), "payload seal")
    require(canonical(report) == canonical(build_report()), "fresh reconstruction")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--check", action="store_true")
    actions.add_argument("--emit", action="store_true")
    actions.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        result = manifest()
    elif args.emit:
        result = build_report()
    else:
        check_report(load_json(FIXTURE.read_bytes()))
        print(
            "PASS native source acquisition controls; full native reconstruction OPEN"
        )
        return
    print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True))


if __name__ == "__main__":
    main()
