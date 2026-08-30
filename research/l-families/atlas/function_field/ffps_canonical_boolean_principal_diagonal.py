"""Exact finite controls for the scoped canonical Boolean principal diagonal."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE = HERE / "FFPS_CANONICAL_BOOLEAN_PRINCIPAL_DIAGONAL.md"
MANIFEST = HERE / "ffps_canonical_boolean_principal_diagonal.sources.json"
FIXTURE = HERE / "ffps_canonical_boolean_principal_diagonal.json"
TEST = ROOT / "tests/test_ffps_canonical_boolean_principal_diagonal.py"
SCHEMA = "ffps-canonical-boolean-principal-diagonal-v1"
SOURCE_SCHEMA = "ffps-canonical-boolean-principal-diagonal-sources-v1"
MAX_BYTES = 524288
MAX_SUPPORT = 6
MAX_PRIME = 1000
MAX_CUTOFF = 10**9
MAX_PRODUCT = 2**63
MAX_Y = 2**40
MAX_SUM = 128
MAX_ORDER = 81
MAX_ATOMS = 16
SOURCE_ROWS = [
    {
        "id": "boolean",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106080-squarefree-boolean-vaughan-keeps-the-balanced-core-literal.md",
        "kind": "scientific_source",
        "role": "Boolean Vaughan identity",
        "git_blob": "346cc52420ec65457c2a5accc045d4a85635cc24",
        "sha256_lf": "8efc34b198fe4bc642f6292bb0cfc4b937922a25b0e3cee35bdc2e51a62e5b7d",
    },
    {
        "id": "canonical",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md",
        "kind": "scientific_source",
        "role": "canonical equal-pair coefficient",
        "git_blob": "b988b14eb982504a799158eed4c76e7f033c96f0",
        "sha256_lf": "2c38355491c82c85886b9b528c4a79d492b74f32ed133d2f1335cd1e6b133a4f",
    },
    {
        "id": "fourier",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
        "kind": "scientific_source",
        "role": "Fourier convention and literal shell",
        "git_blob": "388c7e166a0e6e534d7e908685f71a16de246575",
        "sha256_lf": "1f2259fde8b6763c878354d09b13c7bd858b16dddd7b7784d43e53e52ad77fee",
    },
    {
        "id": "bilateral",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
        "kind": "scientific_source",
        "role": "physical tuple and retained masks",
        "git_blob": "a8d829dc10611adb7bfb4853902bdff0ab02a065",
        "sha256_lf": "2f1a1dfea2cdce53d84160261f746cdf19a67169b41a9bbd93acd9b8ccdd50d8",
    },
    {
        "id": "principal",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
        "kind": "scientific_source",
        "role": "original principal normalization",
        "git_blob": "955c3ed0363ca330439eedbae1bf0041a4c96468",
        "sha256_lf": "24f8661d8b3007e4a76202ca53cc3a19eecd966f1a9dc7608b40d879699e2f0c",
    },
    {
        "id": "anchors",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/lemmas/L-106093-mellin-polarization-places-the-anchor-inside-one-amplified-family-moment.md",
        "kind": "scientific_source",
        "role": "masked bilateral obstruction",
        "git_blob": "cb8665b8cdbe2bc7e6eb223d6bc009e8e4f5a5df",
        "sha256_lf": "11c781a133698ab823c60e2f44036ce04b19789d33baa8a3f78e0afdc185af74",
    },
    {
        "id": "target",
        "commit": "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "path": "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
        "kind": "scientific_source",
        "role": "literal native target remains distinct",
        "git_blob": "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
        "sha256_lf": "54592d5d8d67dd797f9aa2d134ab4825e8ccc52c3ed18edefaf226ea0852eb1d",
    },
    {
        "id": "kernel",
        "commit": "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "path": "claims/lemmas/L-102880-logarithmic-derivative-outer-detector-has-zero-square-lattice-moment.md",
        "kind": "scientific_source",
        "role": "actual piecewise native K",
        "git_blob": "d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6",
        "sha256_lf": "0358b6c377747512037e0e3e2ed88ffcc2974d6f6e9b815621a6ce450735b092",
    },
    {
        "id": "projection",
        "commit": "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "path": "claims/lemmas/L-102901-primewise-complementary-temperatures-form-an-infinite-dimensional-flat-gauge.md",
        "kind": "scientific_source",
        "role": "product identity is not mask intertwining",
        "git_blob": "65fa60eb0ac25ea9797eba3d057bc765cb10c1cd",
        "sha256_lf": "50249da3f2a0537aeed2dcad77cc1f1e4610cfe76fe323c5954a19e05b81fa31",
    },
    {
        "id": "selector",
        "commit": "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "path": "claims/lemmas/L-102963-owner-and-phase-gauges-decouple-on-the-boolean-source.md",
        "kind": "scientific_source",
        "role": "pair-dependent selector limitation",
        "git_blob": "6d5ed75b6938f76d98f2face50e3af62a9dc693c",
        "sha256_lf": "283b7fdfb5788091f5211a12cd74635e4c1a53bd7cfa99cd755a8150063a4df1",
    },
    {
        "id": "exclusion",
        "commit": "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "path": "claims/lemmas/L-102952-owner-excluded-boolean-vaughan-coefficients-are-universal.md",
        "kind": "scientific_source",
        "role": "owner-exclusion coefficient universality",
        "git_blob": "8e0de55d193d6f9dafd025235dac8ab48e687081",
        "sha256_lf": "5e73afb84c22dc043b6fd6c652233a75d0bbd87f91a5d5dc6e5a02d95635d351",
    },
    {
        "id": "context",
        "commit": "08187bdfae119f66c8c82baca2d1c1068e48ff40",
        "path": "research/l-families/atlas/function_field/FFPS_SIGNED_HISTORY_RECOMBINATION.md",
        "kind": "programme_context",
        "role": "history-only payment does not forget other labels",
        "git_blob": "c5f77f48bd19cc9af39698d4de53ae266bd42e17",
        "sha256_lf": "cd19af1dc2b75b07e6775651509a8cebf1b8db96d9cc9bf50c4e7412661a2798",
    },
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, name: str, low: int, high: int) -> int:
    require(type(value) is int, f"{name}: strict integer required")
    require(low <= value <= high, f"{name}: resource/domain cap")
    return value


def rational(value: object) -> Fraction:
    require(type(value) in (int, Fraction), "strict rational required")
    value = Fraction(value)
    require(
        value.numerator.bit_length() <= 64 and value.denominator.bit_length() <= 64,
        "rational bit cap",
    )
    return value


def prime(value: object) -> int:
    p = integer(value, "prime", 2, MAX_PRIME)
    require(all(p % d for d in range(2, math.isqrt(p) + 1)), "composite prime label")
    require(p != 67, "exceptional prime 67 excluded")
    return p


def support(values: object) -> tuple[int, ...]:
    require(type(values) is tuple, "support must be a tuple")
    require(len(values) <= MAX_SUPPORT, "support cap")
    result = tuple(prime(p) for p in values)
    require(tuple(sorted(set(result))) == result, "support must be sorted and distinct")
    require(math.prod(result) <= MAX_PRODUCT, "support product cap")
    return result


def mask_norm(mask: object) -> Fraction:
    require(type(mask) is tuple and len(mask) == 2, "mask must be a rational pair")
    real, imag = (rational(value) for value in mask)
    norm = real * real + imag * imag
    require(norm <= 1, "mask modulus exceeds one")
    return norm


def allocations(values: tuple[int, ...]):
    for tags in itertools.product(range(3), repeat=len(values)):
        yield tuple(
            tuple(p for p, tag in zip(values, tags) if tag == i) for i in range(3)
        )


def mu(values: tuple[int, ...]) -> int:
    return (-1) ** len(values)


def truncated_mu(values: tuple[int, ...], cutoff: int) -> int:
    return mu(values) if math.prod(values) <= cutoff else 0


def a_coefficient(values: object, cutoff: object) -> int:
    values = support(values)
    cutoff = integer(cutoff, "cutoff", 1, MAX_CUTOFF)
    subtotal = 0
    for bits in itertools.product(range(2), repeat=len(values)):
        selected = tuple(p for p, bit in zip(values, bits) if bit)
        subtotal += truncated_mu(selected, cutoff)
    return int(not values) - subtotal


def boolean_coefficients(values: object, cutoff: object) -> tuple[int, int, Fraction]:
    values = support(values)
    cutoff = integer(cutoff, "cutoff", 1, MAX_CUTOFF)
    cache = {}
    for bits in itertools.product(range(2), repeat=len(values)):
        selected = tuple(p for p, bit in zip(values, bits) if bit)
        cache[selected] = a_coefficient(selected, cutoff)
    original = sum(
        cache[left] * cache[right] * mu(rest)
        for left, right, rest in allocations(values)
    )
    expanded = mu(values) - 2 * truncated_mu(values, cutoff)
    expanded += sum(
        truncated_mu(left, cutoff) * truncated_mu(right, cutoff)
        for left, right, _ in allocations(values)
    )
    require(original == expanded, "Boolean Vaughan reconstructions differ")
    depth = len(values)
    beta = Fraction(2, (depth + 1) * (depth + 2))
    require(beta == Fraction(1, math.comb(depth + 2, 2)), "Beta/share mismatch")
    canonical = beta * expanded
    require(abs(canonical) <= 3**depth, "canonical coefficient majorant failed")
    if not values:
        require(original == 0, "unit core is not zero")
    return original, expanded, canonical


def principal_constant(ell: object, rho: object) -> Fraction:
    ell, rho = prime(ell), prime(rho)
    require(ell != rho, "least primes must differ")
    result = Fraction(ell + 1, ell - 1) * Fraction(rho + 1, rho - 1)
    require(result <= 6, "universal principal constant failed")
    return result


def atom_control(
    atom: object, cutoff: object, horizon: object, mask: object = (1, 0)
) -> dict:
    require(type(atom) is tuple and len(atom) == 5, "exact arithmetic tuple required")
    p_support, q_support, g_support, c_support, d_support = map(support, atom)
    require(len(p_support) == len(q_support) == 2, "two primes per owner")
    require(c_support and d_support, "both least-prime cores must be nonempty")
    flat = sum((p_support, q_support, g_support, c_support, d_support), ())
    require(len(set(flat)) == len(flat), "owner/core or core/core overlap")
    horizon = integer(horizon, "horizon", 1, MAX_Y)
    cutoff = integer(cutoff, "cutoff", 1, MAX_CUTOFF)
    norm_mask = mask_norm(mask)
    p, q, g, c, d = map(math.prod, atom)
    n, m = p * g**2 * c**2, q * g**2 * d**2
    require(n <= 16 * horizon and m <= 16 * horizon, "physical window exceeds 16Y")
    ell, rho = c_support[0], d_support[0]
    left = boolean_coefficients(tuple(sorted(g_support + c_support)), cutoff)[2]
    right = boolean_coefficients(tuple(sorted(g_support + d_support)), cutoff)[2]
    bare = left**2 * right**2 / (g**4 * c**2 * d**2 * p * q)
    c_product = principal_constant(ell, rho)
    original = g**2 * ell * rho * c_product * bare * norm_mask
    rescaled = Fraction(c_product, ell * rho) * (g * ell * rho) ** 2 * bare * norm_mask
    require(original == rescaled, "original/source-dual principal weights differ")
    majorant = Fraction(
        6 * 81 ** len(g_support) * 9 ** (len(c_support) + len(d_support)),
        g**2 * c * d * p * q,
    )
    require(original <= majorant, "pointwise principal majorant failed")
    return {
        "arithmetic_tuple": [p, q, g, c, d],
        "prime_supports": [list(s) for s in atom],
        "horizon": horizon,
        "cutoff": cutoff,
        "physical_products": [n, m],
        "least_primes": [ell, rho],
        "canonical_coefficients": [str(left), str(right)],
        "phase": f"exp(i*t*log({p * c * c}/{q * d * d}))",
        "mask_norm_squared": str(norm_mask),
        "original_principal_squared_amplitude": str(original),
        "source_dual_principal_squared_amplitude": str(rescaled),
        "pointwise_majorant": str(majorant),
        "native_masked_identification": False,
    }


def panel_control(atoms: object, cutoff: object, horizon: object) -> list[dict]:
    require(type(atoms) is tuple and 1 <= len(atoms) <= MAX_ATOMS, "atom count cap")
    rows = [atom_control(atom, cutoff, horizon) for atom in atoms]
    keys = [tuple(row["arithmetic_tuple"]) for row in rows]
    require(len(set(keys)) == len(keys), "repeated exact arithmetic tuple")
    return rows


# Quadratic field elements are exact pairs a+b*sqrt(2), with no floating evaluation.
def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qmul(x, y):
    return (x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qscale(x, c):
    return (c * x[0], c * x[1])


def kernel_norm() -> dict:
    pieces = (
        ((8, 0), (-4, 0), (1, 0), (0, 1), 1, 2),
        ((-8, -8), (0, 4), (0, 1), (2, 0), 2, 4),
        ((0, 8), (-2, 0), (2, 0), (0, 2), 4, 8),
    )
    constant, log_coefficient = (0, 0), (0, 0)
    rows = []
    for a, b, sqrt_lo, sqrt_hi, lo, hi in pieces:
        delta = qadd(sqrt_hi, qscale(sqrt_lo, -1))
        part = qadd(qscale(qmul(qmul(a, b), delta), 4), qscale(qmul(b, b), hi - lo))
        log_part = qmul(a, a)
        constant = qadd(constant, part)
        log_coefficient = qadd(log_coefficient, log_part)
        rows.append(
            {
                "y_interval": [lo, hi],
                "A": list(a),
                "B": list(b),
                "constant_Qsqrt2": list(part),
                "log2_Qsqrt2": list(log_part),
            }
        )
    require(constant == (-288, 0), "kernel constant differs")
    require(log_coefficient == (384, 128), "kernel log coefficient differs")
    return {
        "pieces": rows,
        "basis": ["1", "sqrt2", "log2", "sqrt2_log2"],
        "exact_coefficients": [-288, 0, 384, 128],
        "norm": "128*(3+sqrt(2))*log(2)-288",
        "measure": "abs(kappa_hat(t))^2*dt/(2*pi)",
        "numerical_Mellin_integration": False,
    }


def factor_exponents(value: object) -> tuple[int, ...]:
    n = integer(value, "divisor integer", 1, MAX_SUM)
    exponents = []
    p = 2
    while p * p <= n:
        exponent = 0
        while n % p == 0:
            exponent += 1
            n //= p
        if exponent:
            exponents.append(exponent)
        p += 1
    if n > 1:
        exponents.append(1)
    return tuple(exponents)


def divisor_count(value: object, order: object) -> int:
    order = integer(order, "divisor order", 1, MAX_ORDER)
    return math.prod(
        math.comb(e + order - 1, order - 1) for e in factor_exponents(value)
    )


def divisor_convolution(limit: object, order: object) -> list[int]:
    limit = integer(limit, "sum limit", 1, MAX_SUM)
    order = integer(order, "divisor order", 1, MAX_ORDER)
    values = [0] + [1] * limit
    for _ in range(order - 1):
        next_values = [0] * (limit + 1)
        for d in range(1, limit + 1):
            for multiple in range(d, limit + 1, d):
                next_values[multiple] += values[d]
        values = next_values
    return values


def harmonic(limit: object) -> Fraction:
    limit = integer(limit, "harmonic limit", 1, MAX_SUM)
    return sum((Fraction(1, n) for n in range(1, limit + 1)), Fraction())


def majorant_control(limit: object = 32) -> dict:
    limit = integer(limit, "sum limit", 1, MAX_SUM)
    nine = divisor_convolution(limit, 9)
    require(
        all(nine[n] == divisor_count(n, 9) for n in range(1, limit + 1)),
        "independent divisor convolution differs",
    )
    squarefree = sum(
        (
            Fraction(9 ** len(factor_exponents(n)), n)
            for n in range(1, limit + 1)
            if all(e == 1 for e in factor_exponents(n))
        ),
        Fraction(),
    )
    full = sum((Fraction(nine[n], n) for n in range(1, limit + 1)), Fraction())
    upper = harmonic(limit) ** 9
    require(squarefree <= full <= upper, "finite harmonic majorant failed")
    euler_left, euler_right = Fraction(1), Fraction(1)
    prime_rows = []
    for p in (2, 3, 5, 7, 11):
        left, right = 1 + Fraction(81, p**2), (1 - Fraction(1, p**2)) ** -81
        require(left <= right, "finite Euler majorant failed")
        euler_left *= left
        euler_right *= right
        prime_rows.append({"prime": p, "left": str(left), "right": str(right)})
    require(euler_left <= euler_right, "Euler product majorant failed")
    return {
        "finite_limit": limit,
        "squarefree_weighted_sum": str(squarefree),
        "divisor_weighted_sum": str(full),
        "harmonic_power_upper": str(upper),
        "finite_euler_rows": prime_rows,
        "g_exponent": 81,
        "harmonic_components": [9, 9, 2, 2],
        "harmonic_exponent": 22,
        "universal_principal_constant": str(principal_constant(2, 3)),
        "all_horizon_proof_location": "note CBPD11-CBPD12; not certified by finite enumeration",
    }


def boolean_control() -> dict:
    rows = []
    primes = (2, 3, 5, 7, 11)
    for depth in range(len(primes) + 1):
        values = primes[:depth]
        products = {
            math.prod(p for p, bit in zip(values, bits) if bit)
            for bits in itertools.product(range(2), repeat=depth)
        }
        thresholds = sorted(products | {p - 1 for p in products if p > 1})
        for cutoff in thresholds:
            original, expanded, canonical = boolean_coefficients(values, cutoff)
            rows.append(
                {
                    "support": list(values),
                    "cutoff": cutoff,
                    "original": original,
                    "expanded": expanded,
                    "canonical": str(canonical),
                    "majorant": 3**depth,
                }
            )
    return {"rows": rows, "case_count": len(rows), "all_cutoffs_proved_in_note": True}


def normalize_lf(raw: bytes) -> bytes:
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "source bytes/type cap")
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def digest(raw: bytes) -> str:
    return hashlib.sha256(normalize_lf(raw)).hexdigest()


def render(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n"


def reject_duplicates(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def reject_constant(value: str):
    raise ValueError(f"nonfinite JSON constant {value}")


def read_json_bytes(raw: bytes) -> object:
    normalize_lf(raw)
    return json.loads(
        raw.decode("utf-8"),
        object_pairs_hook=reject_duplicates,
        parse_constant=reject_constant,
    )


def exact_match(actual: object, expected: object) -> None:
    # JSON distinguishes true/1 and 1.0/1, unlike Python's ordinary equality.
    require(render(actual) == render(expected), "typed replay differs")


def validate_manifest(value: object) -> None:
    exact_match(value, {"schema": SOURCE_SCHEMA, "sources": SOURCE_ROWS})


def authenticate_raw(row: dict, blob: str, raw: bytes) -> None:
    require(row in SOURCE_ROWS, "unrecognized source identity")
    require(blob == row["git_blob"], "source blob identity differs")
    normalize_lf(raw)
    git_digest = hashlib.sha1(
        b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
    ).hexdigest()
    require(git_digest == blob, "raw Git blob digest differs")
    require(digest(raw) == row["sha256_lf"], "source LF digest differs")


def source_locks() -> dict:
    require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
    validate_manifest(read_json_bytes(MANIFEST.read_bytes()))
    for row in SOURCE_ROWS:
        ref = row["commit"] + ":" + row["path"]
        blob = subprocess.check_output(
            ["git", "rev-parse", ref], cwd=ROOT, timeout=10, text=True
        ).strip()
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", blob], cwd=ROOT, timeout=10, text=True
            ).strip()
        )
        require(0 <= size <= MAX_BYTES, "primitive source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=10)
        authenticate_raw(row, blob, raw)
    current = {}
    for path in (NOTE, Path(__file__).resolve(), TEST, MANIFEST):
        require(path.stat().st_size <= MAX_BYTES, "current artifact byte cap")
        current[path.relative_to(ROOT).as_posix()] = {
            "kind": "current_artifact",
            "sha256_lf": digest(path.read_bytes()),
        }
    return {"frozen_sources": SOURCE_ROWS, "current_artifacts": current}


def seal(payload: dict) -> dict:
    require(
        type(payload) is dict and "payload_sha256" not in payload,
        "unsealed dict required",
    )
    canonical = render(payload).encode("utf-8")
    require(len(canonical) <= MAX_BYTES, "report byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(canonical).hexdigest()}


def check_fixture(actual: object, expected: dict) -> None:
    require(type(actual) is dict, "fixture must be object")
    require("payload_sha256" in actual, "missing payload digest")
    payload = {key: value for key, value in actual.items() if key != "payload_sha256"}
    exact_match(actual, seal(payload))
    exact_match(actual, expected)


def build_report() -> dict:
    atoms = (
        ((5, 31), (3, 137), (37,), (43,), (47,)),
        ((2, 101), (7, 71), (37,), (43,), (47,)),
    )
    return seal(
        {
            "schema": SCHEMA,
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding_contract": "integer/Fraction and formal Q(sqrt2)+Q(sqrt2)*log2; no rounding",
            "sources": source_locks(),
            "boolean": boolean_control(),
            "canonical_arithmetic_panels": panel_control(atoms, 32, 2**30),
            "kernel_norm": kernel_norm(),
            "divisor_majorants": majorant_control(),
            "scope": {
                "ordinary_prime_67_free_chart_only": True,
                "one_atom_per_exact_arithmetic_tuple": True,
                "mask_modulus_at_most_one": True,
                "original_principal_weight_and_measure": True,
                "native_masked_bilateral_identity_proved": False,
                "full_principal_moment_difference_paid": False,
                "native_sign_or_RH_consequence": False,
                "finite_computation_proves_analytic_limits": False,
                "unpaid_term": "P_nat-P_B",
                "centered_identity": "P_nat^circ-P_B^circ=(P_nat-P_B)+(D_B-D_lit)",
                "diagonal_bound": "6*C_kappa*zeta(2)^81*H_floor(16Y)^22",
            },
            "resource_caps": {
                "bytes": MAX_BYTES,
                "support": MAX_SUPPORT,
                "prime": MAX_PRIME,
                "cutoff": MAX_CUTOFF,
                "product": MAX_PRODUCT,
                "horizon": MAX_Y,
                "finite_sum": MAX_SUM,
                "divisor_order": MAX_ORDER,
                "atom_count": MAX_ATOMS,
                "rational_bits": 64,
            },
        }
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = build_report()
    if args.check:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        check_fixture(read_json_bytes(FIXTURE.read_bytes()), expected)
        print("PASS_FFPS_CANONICAL_BOOLEAN_PRINCIPAL_DIAGONAL")
    else:
        print(render(expected), end="")


if __name__ == "__main__":
    main()
