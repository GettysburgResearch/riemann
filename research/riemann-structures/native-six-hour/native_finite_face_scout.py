#!/usr/bin/env python3
"""Original-kernel KKT discovery on preregistered literal prime clusters."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1
from itertools import combinations, pairwise
from math import comb, prod
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
KERNEL_COMMIT = "033bc967f8fd9b5e23e00386dfe81e92b25dc012"
KERNEL_PATH = "research/riemann-structures/native-six-hour/native_activation_kernel.py"
KERNEL_BLOB = "1846674ad08e9f070cc6884c3928d619552f8011"
ACQUISITION_COMMIT = "1d1088d36f0d873ffc94d786415616df95b00edc"
ACQUISITION_PATH = (
    "research/riemann-structures/native-six-hour/native_face_prime_acquisition.json"
)
ACQUISITION_BLOB = "4dcfad8765a0e9f52f56c1a77f3c28dc27ad760e"
PRIME_PATH = "research/riemann-structures/native-six-hour/native_face_prime_scout.py"
PRIME_BLOB = "ad1a0c502b151fdb6b3c2729f3df6764da19485f"
PREREG_PATH = (
    "research/riemann-structures/native-six-hour/NATIVE_FACE_PRIME_PREREGISTRATION.md"
)
PREREG_BLOB = "8d5a45f27c67ace7ea28c36336babd388abf7d28"
OLD = "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc"
GE_PATH = "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md"
GE_BLOB = "6810bcece309b0c54ae6c8fc84b314990004549c"
MAX_BYTES = 1048576
MAX_BITS = 256
MAX_INTERVAL_ARITHMETIC_BITS = 131072
SERIALIZED_INTERVAL_BITS = 512


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def frozen_bytes(commit, path, blob):
    require(len(commit) == len(blob) == 40, "completed source freeze required")
    ref = f"{commit}:{path}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "frozen byte cap")
    raw = subprocess.run(
        ["git", "show", ref], cwd=ROOT, capture_output=True, check=True
    ).stdout
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact frozen source authentication",
    )
    return raw


def load_module(commit, path, blob):
    raw = frozen_bytes(commit, path, blob)
    namespace = {
        "__name__": "authenticated_finite_face_source",
        "__file__": str(ROOT / path),
    }
    # Execute only exact source bytes authenticated to the declared frozen commit/blob.
    exec(compile(raw, str(ROOT / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def exact_ratio(value):
    require(type(value) in (int, F) and value > 0, "positive exact source ratio")
    value = F(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= MAX_BITS,
        "explicit 256-bit finite-source ratio cap",
    )
    return value


def normalize_logs(kernel, expression, primes):
    coefficients = {p: kernel.ZERO for p in (2,) + primes}
    for base, coefficient in expression[1].items():
        base = exact_ratio(base)
        numerator, denominator = base.numerator, base.denominator
        for p, previous_coefficient in coefficients.items():
            exponent = 0
            while numerator % p == 0:
                numerator //= p
                exponent += 1
            while denominator % p == 0:
                denominator //= p
                exponent -= 1
            coefficients[p] = kernel.qa(
                previous_coefficient, kernel.qs(coefficient, exponent)
            )
        require(
            numerator == denominator == 1,
            "logarithms supported on exact literal primes",
        )
    prime_sum = kernel.ZERO
    for p in primes:
        prime_sum = kernel.qa(prime_sum, coefficients[p])
    require(prime_sum == kernel.ZERO, "same-cardinality frequency is scale invariant")
    logs = {F(2): coefficients[2]}
    for p in primes[1:]:
        logs[F(p, primes[0])] = coefficients[p]
    return kernel.expr(expression[0], logs)


def original_gamma(kernel, ratio, primes):
    """Nine actual kernel intersections, with a new explicit input cap."""
    ratio = exact_ratio(ratio)
    ratio = ratio if ratio >= 1 else 1 / ratio
    shift = exact_ratio(ratio**2)
    require(shift <= 2, "preregistered small-shift panel domain")
    pieces = (
        (F(1), F(2), kernel.q(8), kernel.q(-4)),
        (F(2), F(4), kernel.q(-8, -8), kernel.q(0, 4)),
        (F(4), F(8), kernel.q(0, 8), kernel.q(-2)),
    )
    result = kernel.expr()
    for lo1, hi1, a, b in pieces:
        for lo2, hi2, c, d in pieces:
            lo, hi = max(lo1, shift * lo2), min(hi1, shift * hi2)
            if lo >= hi:
                continue
            logarithm = kernel.qm(a, c)
            root = kernel.qs(
                kernel.qa(kernel.qm(a, d), kernel.qs(kernel.qm(c, b), ratio)), 2 / ratio
            )
            linear = kernel.qs(kernel.qm(b, d), 1 / ratio)
            constant = kernel.qa(
                kernel.qm(
                    root,
                    kernel.qa(
                        kernel.sqrt_boundary(hi),
                        kernel.qs(kernel.sqrt_boundary(lo), -1),
                    ),
                ),
                kernel.qs(linear, hi - lo),
            )
            result = kernel.ea(result, kernel.expr(constant, {hi / lo: logarithm}))
    result = normalize_logs(kernel, result, primes)
    closed = kernel.expr(kernel.q(-288), {F(2): kernel.q(384, 128)})
    closed = kernel.ea(closed, kernel.expr(logs={ratio: kernel.q(-1152, -512)}))
    constant = kernel.qa(
        kernel.qs(kernel.q(288, 192), ratio - 1),
        kernel.qs(kernel.q(-576, -192), 1 / ratio - 1),
    )
    closed = normalize_logs(kernel, kernel.ea(closed, kernel.expr(constant)), primes)
    require(result == closed, "independent overlap and exact native cusp formula")
    return result


def expression_json(value):
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 4096
            for x in value[0]
        )
        and all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 4096
            for coefficient in value[1].values()
            for x in coefficient
        ),
        "bounded exact expression serialization",
    )
    return {
        "constant_Q_sqrt2": [str(x) for x in value[0]],
        "log_terms": [
            {"base": str(base), "Q_sqrt2_coefficient": [str(x) for x in coefficient]}
            for base, coefficient in sorted(value[1].items())
        ],
    }


def interval_json(value):
    """Outward dyadic serialization; all KKT decisions use the exact bounds."""
    require(
        type(value) is tuple
        and len(value) == 2
        and all(type(x) is F for x in value)
        and value[0] <= value[1],
        "ordered exact interval",
    )
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length())
            <= MAX_INTERVAL_ARITHMETIC_BITS
            for x in value
        ),
        "explicit interval arithmetic bit cap before serialization",
    )
    scale = 1 << SERIALIZED_INTERVAL_BITS
    lower = F((value[0].numerator * scale) // value[0].denominator, scale)
    upper = F(-((-value[1].numerator * scale) // value[1].denominator), scale)
    require(
        lower <= value[0] <= value[1] <= upper, "outward dyadic interval containment"
    )
    require(
        all(
            max(x.numerator.bit_length(), x.denominator.bit_length()) <= 2048
            for x in (lower, upper)
        ),
        "bounded dyadic output before integer conversion",
    )
    return {
        "lower": str(lower),
        "upper": str(upper),
        "approximate_midpoint": float((lower + upper) / 2),
        "outward_dyadic_precision_bits": SERIALIZED_INTERVAL_BITS,
        "exact_interval_used_for_all_decisions": True,
    }


def source_gram(kernel, primes):
    require(
        type(primes) is tuple and len(primes) in (4, 6),
        "fixed four- or six-prime panel",
    )
    require(
        all(type(p) is int and 2 < p < 120000000 for p in primes)
        and all(a < b for a, b in pairwise(primes)),
        "ordered bounded physical labels",
    )
    r = len(primes)
    for k in range(r):
        numerator = prod(primes[: k + 1])
        denominator = prod(primes[r - k :]) if k else 1
        require(
            numerator**2 > 8 * denominator**2,
            "all cardinality bands separated in the original kernel",
        )
    for k in range(1, r + 1):
        require(
            prod(primes[r - k :]) ** 2 <= 2 * prod(primes[:k]) ** 2,
            "every within-band shift lies in the exact formula domain",
        )
    matrix = [[kernel.expr() for _ in range(r)] for _ in range(r)]
    records, pair_count = [], 0
    K = prod(primes)

    @lru_cache(maxsize=512, typed=True)
    def gamma(ratio):
        return original_gamma(kernel, ratio, primes)

    for k in range(r + 1):
        supports = tuple(combinations(range(r), k))
        for support in supports:
            n = prod(primes[j] for j in support)
            records.append(
                {
                    "support": support,
                    "n": n,
                    "m": K // n,
                    "activation_incidence": [int(j in support) for j in range(r)],
                }
            )
        if not k:
            continue
        for S in supports:
            n = prod(primes[j] for j in S)
            for T in supports:
                m = prod(primes[j] for j in T)
                pair_count += 1
                correlation = gamma(F(n, m))
                for i in S:
                    for j in T:
                        matrix[i][j] = kernel.ea(matrix[i][j], correlation)
    require(
        len(records) == 2**r and pair_count == comb(2 * r, r) - 1,
        "complete source factor and same-band census",
    )
    require(
        all(matrix[i][j] == matrix[j][i] for i in range(r) for j in range(r)),
        "exact original source Gram symmetry",
    )
    return tuple(tuple(row) for row in matrix), records, pair_count


def subtraction(kernel, a, b):
    return kernel.ea(a, kernel.es(b, -1))


def panel(kernel, primes):
    matrix, records, pair_count = source_gram(kernel, primes)
    r, K = len(primes), prod(primes)
    left, right = r // 2 - 1, r // 2
    g00, g01, g11 = matrix[left][left], matrix[left][right], matrix[right][right]
    numerator_left = subtraction(kernel, g11, g01)
    numerator_right = subtraction(kernel, g00, g01)
    denominator = kernel.ea(numerator_left, numerator_right)
    d = kernel.ei(denominator)
    require(d[0] > 0, "positive original-kernel central-face curvature")
    n, m = kernel.ei(numerator_left), kernel.ei(numerator_right)
    q_left, q_right = kernel.im(n, kernel.inv(d)), kernel.im(m, kernel.inv(d))
    require(
        0 < q_left[0] <= q_left[1] < 1 and 0 < q_right[0] <= q_right[1] < 1,
        "source-realizable interior activation on the declared face",
    )
    scale = F(4, 4**r * K)
    slacks = []
    for i in range(r):
        if i in (left, right):
            slacks.append({"coordinate": i, "active": True, "exact_stationarity": True})
            continue
        difference0 = subtraction(kernel, matrix[i][left], g00)
        difference1 = subtraction(kernel, matrix[i][right], g01)
        cleared = kernel.ia(
            kernel.im(kernel.ei(difference0), n), kernel.im(kernel.ei(difference1), m)
        )
        slack = kernel.im(cleared, kernel.inv(d))
        slacks.append(
            {
                "coordinate": i,
                "active": False,
                "cleared_KKT_numerator_interval": interval_json(cleared),
                "bare_half_gradient_slack_interval": interval_json(slack),
                "physical_half_gradient_slack_interval": interval_json(
                    kernel.im(slack, kernel.point(scale))
                ),
                "strict_KKT_certified": slack[0] > 0,
                "opposite_sign_certified": slack[1] < 0,
            }
        )
    uniform = kernel.expr()
    for row in matrix:
        for value in row:
            uniform = kernel.ea(uniform, kernel.es(value, F(1, r * r)))
    decrement = kernel.im(kernel.im(n, n), kernel.inv(d))
    candidate = kernel.ia(kernel.ei(g11), kernel.neg(decrement))
    improvement = kernel.ia(kernel.ei(subtraction(kernel, uniform, g11)), decrement)
    success = all(row.get("strict_KKT_certified", True) for row in slacks)
    return {
        "primes": primes,
        "arity": r,
        "K": K,
        "all_source_records": records,
        "same_cardinality_ordered_pairs_excluding_empty": pair_count,
        "bare_original_kernel_Gram": [
            [expression_json(value) for value in row] for row in matrix
        ],
        "physical_Gram_multiplier": str(scale),
        "candidate_active_coordinates": (left, right),
        "exact_left_activation_numerator": expression_json(numerator_left),
        "exact_central_face_denominator": expression_json(denominator),
        "central_activations": [
            interval_json(q_left),
            interval_json(q_right),
        ],
        "all_coordinate_KKT": slacks,
        "unique_full_source_simplex_minimizer_certified": success,
        "restricted_candidate_physical_energy_interval": interval_json(
            kernel.im(candidate, kernel.point(scale))
        ),
        "uniform_minus_candidate_physical_energy_interval": interval_json(
            kernel.im(improvement, kernel.point(scale))
        ),
        "negative_face_result_would_be_retained": True,
        "kernel_replaced_by_its_quadratic_approximation": False,
        "literal_prime_product_aliases_assumed": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--discover", action="store_true", required=True)
    parser.parse_args()
    kernel = load_module(KERNEL_COMMIT, KERNEL_PATH, KERNEL_BLOB)
    kernel.authenticate()
    frozen_bytes(OLD, GE_PATH, GE_BLOB)
    acquisition = json.loads(
        frozen_bytes(ACQUISITION_COMMIT, ACQUISITION_PATH, ACQUISITION_BLOB)
    )
    prime_source = load_module(ACQUISITION_COMMIT, PRIME_PATH, PRIME_BLOB)
    frozen_bytes(ACQUISITION_COMMIT, PREREG_PATH, PREREG_BLOB)
    require(
        acquisition.get("schema")
        == "riemann.native_six_hour.face_prime_acquisition.v1",
        "frozen actual-prime acquisition",
    )
    for i, row in enumerate(acquisition["windows"]):
        require(
            canonical(prime_source.window(i)) == canonical(row),
            "literal first-prime window replay",
        )
    if not acquisition["all_windows_succeeded"]:
        print(
            json.dumps(
                {
                    "schema": "riemann.native_six_hour.finite_face_discovery.v1",
                    "acquisition_failed": True,
                    "windows": acquisition["windows"],
                    "models": [],
                },
                indent=2,
                sort_keys=True,
            )
        )
        return
    primes = tuple(row["first_prime"] for row in acquisition["windows"])
    result = {
        "schema": "riemann.native_six_hour.finite_face_discovery.v1",
        "acquisition_failed": False,
        "exact_input_ratio_bit_cap": MAX_BITS,
        "exact_interval_arithmetic_bit_cap": MAX_INTERVAL_ARITHMETIC_BITS,
        "outward_interval_serialization_precision_bits": SERIALIZED_INTERVAL_BITS,
        "sources": [
            {"commit": KERNEL_COMMIT, "path": KERNEL_PATH, "blob": KERNEL_BLOB},
            {
                "commit": ACQUISITION_COMMIT,
                "path": ACQUISITION_PATH,
                "blob": ACQUISITION_BLOB,
            },
            {"commit": ACQUISITION_COMMIT, "path": PRIME_PATH, "blob": PRIME_BLOB},
            {"commit": ACQUISITION_COMMIT, "path": PREREG_PATH, "blob": PREREG_BLOB},
            {"commit": OLD, "path": GE_PATH, "blob": GE_BLOB},
            {
                "commit": kernel.SOURCE_COMMIT,
                "path": kernel.SOURCE_PATH,
                "blob": kernel.SOURCE_BLOB,
            },
        ],
        "models": [panel(kernel, primes[:4]), panel(kernel, primes)],
        "prime_panels_changed_after_kernel_test": False,
        "full_post_renewal_gamma_identified": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
