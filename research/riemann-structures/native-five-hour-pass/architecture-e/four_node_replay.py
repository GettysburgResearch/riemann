"""Exact bounded support for the written all-node Architecture E theorem."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ARTIFACT = HERE / "four_node_verification.json"
TEST = ROOT / "tests/test_architecture_e_pass_four_node.py"
MAX_BITS = 4096
MAX_JSON_BYTES = 2_000_000
PANELS = (
    (256, 257, 300, 1024),
    (256, 256, 256, 256),
    (256, 256, 512, 512),
    (256, 65536, 16777216, 4294967296),
)
SHIFTS = (Q(-1, 2), Q(0), Q(1, 2), Q(1), Q(17), Q(4096))
PINS = (
    (
        "9421846721cd788ab01615c8b6d459d9de849df7",
        "research/integrated/xi_pick/ORDER_THREE_CANONICAL.md",
        "f16e936294172dc272e67edcdffc822ba6edf5e6",
    ),
    (
        "8f01064df805624c045877655893c324a220975d",
        "research/exploratory/XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md",
        "797f7b581580ad5a441c7702015c64a53eca6f4d",
    ),
    (
        "9497db89e34669e2167c632c918c491bf6ee73ab",
        "research/exploratory/prs-765-766-770-781-proof-review/GENERALIZED_SCHUR_ZERO_INDEX.md",
        "5e120b6bae9d65e5a90c63716f1c1382839bb3bf",
    ),
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def rational(value):
    need(type(value) in (int, Q), "literal integer/Fraction required")
    value = Q(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= MAX_BITS,
        "exact-number cap",
    )
    return value


def encode(value):
    if type(value) is Q:
        value = rational(value)
        return [value.numerator, value.denominator]
    if isinstance(value, tuple | list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    need(type(value) in (int, str, bool) or value is None, "JSON value type")
    if type(value) is int:
        rational(value)
    return value


def decode_fraction(value):
    need(type(value) is list and len(value) == 2, "fraction pair")
    a, b = value
    need(type(a) is int and type(b) is int and b > 0, "literal fraction integers")
    need(math.gcd(a, b) == 1, "canonical reduced fraction")
    return rational(Q(a, b))


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_load(raw):
    need(len(raw.encode("utf-8")) <= MAX_JSON_BYTES, "JSON byte cap")

    def unique(pairs):
        result = {}
        for key, value in pairs:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def refuse(_):
        raise ValueError("floating/nonfinite JSON token")

    result = json.loads(
        raw, object_pairs_hook=unique, parse_float=refuse, parse_constant=refuse
    )
    # This also checks integer bit caps and rejects unexpected Python objects.
    encode(result)
    return result


def mm(a, b):
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def ident(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def det(a):
    a = [row[:] for row in a]
    value = Q(1)
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            value = -value
        p = a[j][j]
        value *= p
        for i in range(j + 1, len(a)):
            scale = a[i][j] / p
            for k in range(j + 1, len(a)):
                a[i][k] -= scale * a[j][k]
    return rational(value)


def checked_nodes(nodes):
    need(1 <= len(nodes) <= 4, "node-count cap")
    nodes = tuple(rational(x) for x in nodes)
    need(all(x > 0 for x in nodes), "positive nodes")
    return nodes


def source_matrix(nodes):
    """B=D^-1 A D, D=diag(sqrt(x_i)); B_ij=2*x_j above diagonal."""
    nodes = checked_nodes(nodes)
    return [
        [Q(0) if i > j else x if i == j else 2 * x for j, x in enumerate(nodes)]
        for i in range(len(nodes))
    ]


def resolvent_product(nodes, shift):
    nodes, shift = checked_nodes(nodes), rational(shift)
    need(all(x + shift != 0 for x in nodes), "resolvent pole")
    n = len(nodes)
    out = [[Q(0) for _ in nodes] for _ in nodes]
    for i in range(n):
        out[i][i] = 1 / (nodes[i] + shift)
        for j in range(i + 1, n):
            out[i][j] = -2 * nodes[j] / ((nodes[i] + shift) * (nodes[j] + shift))
            for k in range(i + 1, j):
                out[i][j] *= (shift - nodes[k]) / (shift + nodes[k])
    return out


def resolvent_paths(nodes, shift):
    """Independent finite D^-1 sum(-ND^-1)^k, retaining original coordinates."""
    a = source_matrix(nodes)
    n = len(nodes)
    dinv = [[Q(int(i == j), nodes[i] + shift) for j in range(n)] for i in range(n)]
    upper = [[a[i][j] if j > i else Q(0) for j in range(n)] for i in range(n)]
    step = [[-x for x in row] for row in mm(upper, dinv)]
    term, result = dinv, [row[:] for row in dinv]
    for _ in range(1, n):
        term = mm(term, step)
        result = [[result[i][j] + term[i][j] for j in range(n)] for i in range(n)]
    return result


def poly_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_shift(a, center, count):
    return [
        sum(
            (a[k] * math.comb(k, j) * center ** (k - j) for k in range(j, len(a))), Q(0)
        )
        for j in range(count)
    ]


def inverse_laplace(numerator, poles):
    """Literal rational partial fractions -> coefficients of t^k exp(-x*t)."""
    out = {}
    for x in sorted(set(poles)):
        multiplicity = poles.count(x)
        denominator = [Q(1)]
        for y in poles:
            if y != x:
                denominator = poly_mul(denominator, [y, Q(1)])
        top = poly_shift(numerator, -x, multiplicity)
        bottom = poly_shift(denominator, -x, multiplicity)
        need(bottom[0] != 0, "partial-fraction divisor")
        quotient = []
        for j in range(multiplicity):
            quotient.append(
                (
                    top[j]
                    - sum((bottom[k] * quotient[j - k] for k in range(1, j + 1)), Q(0))
                )
                / bottom[0]
            )
        for power in range(1, multiplicity + 1):
            value = quotient[multiplicity - power] / math.factorial(power - 1)
            if value:
                out[x, power - 1] = value
    return out


def source_functions(nodes):
    nodes = checked_nodes(nodes)
    out = []
    for j, x in enumerate(nodes):
        numerator = [x]
        for y in nodes[:j]:
            numerator = poly_mul(numerator, [-y, Q(1)])
        out.append(inverse_laplace(numerator, nodes[: j + 1]))
    return out


def newton_functions(nodes):
    nodes = checked_nodes(nodes)
    return [inverse_laplace([Q((-1) ** j)], nodes[: j + 1]) for j in range(len(nodes))]


def derivative_minus(function):
    out = {}
    for (x, power), coefficient in function.items():
        out[x, power] = out.get((x, power), Q(0)) + x * coefficient
        if power:
            out[x, power - 1] = out.get((x, power - 1), Q(0)) - power * coefficient
    return {key: value for key, value in out.items() if value}


def combine(functions, coefficients):
    out = {}
    for function, c in zip(functions, coefficients, strict=True):
        for key, value in function.items():
            out[key] = out.get(key, Q(0)) + c * value
    return {key: value for key, value in out.items() if value}


def inner(a, b):
    return sum(
        (
            u * v * math.factorial(k + ell) / (x + y) ** (k + ell + 1)
            for (x, k), u in a.items()
            for (y, ell), v in b.items()
        ),
        Q(0),
    )


def function_record(function):
    return [[x, power, value] for (x, power), value in sorted(function.items())]


def panel_record(raw_nodes):
    nodes = checked_nodes(raw_nodes)
    need(min(nodes) >= 256, "declared source panel threshold")
    n = len(nodes)
    b = source_matrix(nodes)
    functions = source_functions(nodes)
    gram = [[inner(f, g) for g in functions] for f in functions]
    expected_gram = [
        [nodes[i] / 2 if i == j else Q(0) for j in range(n)] for i in range(n)
    ]
    need(gram == expected_gram, "literal exponential Gram")
    for j in range(n):
        need(
            derivative_minus(functions[j])
            == combine(functions, [b[i][j] for i in range(n)]),
            "literal derivative source map",
        )
    resolvents = []
    for shift in SHIFTS:
        value = resolvent_product(nodes, shift)
        shifted = [
            [b[i][j] + (shift if i == j else 0) for j in range(n)] for i in range(n)
        ]
        need(
            mm(value, shifted) == ident(n) and mm(shifted, value) == ident(n),
            "both inverse products",
        )
        need(value == resolvent_paths(nodes, shift), "independent resolvent paths")
        resolvents.append({"shift": shift, "matrix": value})
    newton = newton_functions(nodes)
    ng = [[inner(f, g) for g in newton] for f in newton]
    nd = det(ng)
    expected = Q(1)
    for x in nodes:
        for y in nodes:
            expected /= x + y
    need(nd == expected, "confluent Newton determinant")
    pivot = nd / det([row[:-1] for row in ng[:-1]]) if n > 1 else nd
    expected_pivot = 1 / (2 * nodes[-1])
    for x in nodes[:-1]:
        expected_pivot /= (x + nodes[-1]) ** 2
    need(pivot == expected_pivot, "last Newton residual")
    return {
        "nodes": nodes,
        "source_matrix_diagonal_similarity": b,
        "literal_source_functions": [function_record(f) for f in functions],
        "literal_source_gram": gram,
        "resolvents": resolvents,
        "newton_gram": ng,
        "newton_determinant": nd,
        "cauchy_last_newton_residual": pivot,
        "xi_residual_proved_lower_bound": pivot / 4,
    }


def exp_upper(x, degree):
    x = rational(x)
    need(
        type(degree) is int and 0 <= degree <= 32 and 0 <= x < degree + 2,
        "Taylor cap/domain",
    )
    total, term = Q(1), Q(1)
    for j in range(1, degree + 1):
        term *= x / j
        total += term
    tail = term * x / (degree + 1) / (1 - x / (degree + 2))
    return total, total + tail


def pi_integral_identity():
    numerator = poly_mul([Q(0)] * 4 + [Q(1)], [Q(1), Q(-4), Q(6), Q(-4), Q(1)])
    rest = numerator[:]
    quotient = [Q(0)] * 7
    for degree in range(8, 1, -1):
        coefficient = rest[degree]
        quotient[degree - 2] = coefficient
        rest[degree] -= coefficient
        rest[degree - 2] -= coefficient
    need(
        rest[:2] == [Q(-4), Q(0)] and not any(rest[2:]),
        "positive pi-integral remainder",
    )
    integral = sum((v / (j + 1) for j, v in enumerate(quotient)), Q(0))
    need(integral == Q(22, 7), "positive pi-integral polynomial part")
    return {
        "quotient": quotient,
        "remainder": rest[:2],
        "polynomial_integral": integral,
    }


def prime_power_labels(cap=32):
    need(type(cap) is int and 2 <= cap <= 32, "prime-source cap")
    primes = [
        p for p in range(2, cap + 1) if all(p % d for d in range(2, math.isqrt(p) + 1))
    ]
    labels = {}
    for p in primes:
        value = p
        while value <= cap:
            labels[value] = p
            value *= p
    # Independent factorization detects whether the support is a single prime.
    for n in range(2, cap + 1):
        rest, factors = n, []
        for p in primes:
            if rest % p == 0:
                factors.append(p)
                while rest % p == 0:
                    rest //= p
        expected = factors[0] if len(factors) == 1 else None
        need(labels.get(n) == expected, "literal von Mangoldt owner")
    return [[n, labels.get(n)] for n in range(2, cap + 1)]


def constant_record():
    r, c = Q(256), Q(1, 2)
    q = (r + c) / (r - c)
    j4 = 1 / (r - c) + 2 * r / (r - c) ** 2 * sum((q**j for j in range(3)), Q(0))
    need(j4 < Q(1, 32), "rational resolvent majorant")
    lower, upper = exp_upper(Q(7, 2), 16)
    need(upper < 34 and Q(3591, 88) > 34, "logarithmic lower bound")
    frame_square = 2 * sum(25**j for j in range(4))
    need(frame_square == 32552 and frame_square < 181**2, "weighted frame bound")
    prime = 181 * (Q(1, 2**127) + Q(1, 126 * 2**126))
    need(prime < Q(1, 2**118) < Q(1, 1024), "full prime-series tail")
    gamma = 27 / (r + c)
    margin = Q(1, 4) - Q(27, 256) - Q(1, 2048) - Q(1, 1024)
    need(margin == Q(293, 2048) and margin > Q(1, 8), "four-node coercivity margin")
    return {
        "minimum_node": r,
        "maximum_jet_dimension": 4,
        "half_shift": c,
        "resolvent_q": q,
        "resolvent_majorant": j4,
        "exp_7_over_2_partial": lower,
        "exp_7_over_2_upper": upper,
        "pi_positive_integral": pi_integral_identity(),
        "gamma_norm_majorant": gamma,
        "weighted_frame_square": frame_square,
        "weighted_frame_integer_upper": 181,
        "prime_series_majorant": prime,
        "real_operator_margin_lower": margin,
        "claimed_real_operator_margin": Q(1, 8),
        "claimed_kernel_relative_margin": Q(1, 4),
    }


def authenticated_sources():
    records = []
    for commit, path, blob in PINS:
        result = subprocess.run(
            ["git", "cat-file", "blob", f"{commit}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        data = result.stdout
        need(len(data) <= 512_000, "source byte cap")
        actual = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        need(actual == blob, f"source blob mismatch: {path}")
        records.append(
            {
                "commit": commit,
                "path": path,
                "blob": blob,
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    return records


def owned_sources():
    paths = [
        HERE / "FOUR_NODE_HIGH_AXIS.md",
        HERE / "FOUR_NODE_PREREGISTRATION.md",
        Path(__file__),
        TEST,
    ]
    return {
        p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in paths
    }


def build():
    sources = authenticated_sources()
    result = encode(
        {
            "schema": "architecture-e-four-node-v1",
            "arithmetic": "EXACT_RATIONAL_NO_FLOAT",
            "sources": sources,
            "owned_sources": owned_sources(),
            "constants": constant_record(),
            "panels": [panel_record(nodes) for nodes in PANELS],
            "von_mangoldt_formal_log_prime_labels": prime_power_labels(),
            "scope": {
                "finite_algebra_recomputed": True,
                "xi_values_sampled": False,
                "global_theorem_proved_by_sampling": False,
                "written_analytic_proof_required": True,
                "all_node_ratios_and_confluence": "written theorem, minimum node256 and total dimension<=4",
                "unrestricted_order_four_safe_axis": "OPEN",
                "rh": "OPEN",
            },
        }
    )
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    return result


def accept(candidate, fresh):
    need(
        canonical(candidate) == canonical(fresh), "fresh typed reconstruction mismatch"
    )


def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fresh = build()
    if args.write:
        ARTIFACT.write_text(
            json.dumps(fresh, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
    else:
        accept(strict_load(ARTIFACT.read_text(encoding="utf-8")), fresh)
    print(
        canonical(
            {
                "result": "PASS",
                "proof_sha256": fresh["proof_sha256"],
                "panels": len(PANELS),
                "sampled_xi_values": False,
            }
        )
    )


if __name__ == "__main__":
    main()
