#!/usr/bin/env python3
"""Exact bounded q/frequency controls; not an analytic period or zero prover."""

import argparse
import ast
import hashlib
import json
import math
import subprocess
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE = HERE / "RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md"
FIXTURE = HERE / "rankin_selberg_quotient_global_parent.json"
MANIFEST = HERE / "rankin_selberg_quotient_global_parent.sources.json"
TEST = ROOT / "tests/test_rankin_selberg_quotient_global_parent.py"
BASE = "246434f343029cc821aa236081c4d12080f571f2"
MAX_Q, MAX_CUTOFF, MAX_TERMS = 24, 12, 256
INPUT_BITS, INTERNAL_BITS, MAX_WORK = 32, 4096, 200000
CONTEXT = (
    "research/l-families/atlas/generalized/CONTINUATION_RESULTS.md",
    "3047f87a0a6e01c4ff6c6455e056a0aecb7e6cad",
    "516e70e412b82c6c8535d7a1637db14571965a89331a72f29c8981155dbdd5b1",
)
EXTERNAL = (
    (
        "https://arxiv.org/pdf/math/0605783",
        "Miller-Schmid (1.7)-(1.14): period and unfolding; completed pole-at-zero omission is corrected using Zagier",
    ),
    (
        "https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf",
        "Zagier section1(a)-(c), equations3-17: completed E* poles0,1, residues-/+1/2, reflection and moderate growth",
    ),
    (
        "https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf",
        "Zagier Elliptic Modular Forms sections2.1,2.2,2.4,4.1: E4/Delta, ring/dimension and Hecke algebra",
    ),
    (
        "https://doi.org/10.1137/0120053",
        "Anderson 1971 Shorted Operators: classical Schur/positive-form boundary",
    ),
    (
        "https://doi.org/10.1137/0128007",
        "Anderson-Trapp 1975 Shorted Operators II: classical positive operator boundary",
    ),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lower, upper):
    require(type(value) is int and lower <= value <= upper, "integer cap/type")
    return value


def exact(value, *, internal=False):
    require(type(internal) is bool, "internal flag type")
    require(type(value) in (int, F), "exact int/Fraction required")
    value = F(value)
    limit = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= limit,
        "rational bit cap",
    )
    return value


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, count=1):
        count = integer(count, 0, MAX_WORK)
        require(self.used + count <= self.limit, "work cap before operation")
        self.used += count


def budget(value):
    require(type(value) is Budget, "Budget required")
    return value


def polynomial(values):
    require(type(values) in (list, tuple), "polynomial list required")
    integer(len(values), 1, MAX_Q + 1)
    for value in values:
        require(type(value) is int, "integer polynomial coefficients")
        exact(value, internal=True)
    return tuple(values)


def qmul(left, right, order, work):
    order = integer(order, 1, MAX_Q)
    left, right, work = polynomial(left), polynomial(right), budget(work)
    require(len(left) <= order + 1 and len(right) <= order + 1, "q shape")
    work.spend(sum(min(len(right), order + 1 - i) for i in range(len(left))))
    out = [0] * (order + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right[: order + 1 - i]):
            out[i + j] += a * b
            exact(out[i + j], internal=True)
    return tuple(out)


def qsource(order=MAX_Q, work=None):
    order = integer(order, 6, MAX_Q)
    work = Budget() if work is None else budget(work)
    delta = (0, 1) + (0,) * (order - 1)
    for n in range(1, order + 1):
        factor = [0] * (order + 1)
        for j in range(min(24, order // n) + 1):
            factor[n * j] = (-1) ** j * math.comb(24, j)
        delta = qmul(delta, factor, order, work)
    # Independent logarithmic-derivative recurrence for Delta/q.
    recurrence = [1]
    for n in range(1, order):
        work.spend(n)
        numerator = -24 * sum(
            sum(d for d in range(1, k + 1) if k % d == 0) * recurrence[n - k]
            for k in range(1, n + 1)
        )
        require(numerator % n == 0, "Delta recurrence nonintegral")
        recurrence.append(numerator // n)
    require(delta == (0,) + tuple(recurrence), "independent Delta mismatch")
    e4 = (1,) + tuple(
        240 * sum(d**3 for d in range(1, n + 1) if n % d == 0)
        for n in range(1, order + 1)
    )
    a = qmul(delta, qmul(qmul(e4, e4, order, work), e4, order, work), order, work)
    b = qmul(delta, delta, order, work)
    c = tuple(x - 696 * y for x, y in zip(a, b))
    expected = {
        1: (1, 0),
        2: (696, 1),
        3: (162252, -48),
        4: (12831808, 1080),
        6: (-882400608, 143820),
    }
    require(all((a[n], b[n]) == pair for n, pair in expected.items()), "q primitives")
    return a, b, c


def hecke_control(a, b, work):
    a, b, work = polynomial(a), polynomial(b), budget(work)
    require(len(a) == len(b) and len(a) >= 7, "Hecke source shape")
    matrix = ((a[2], b[2]), (a[4] + 2**23 - 696 * a[2], b[4] - 696 * b[2]))
    require(matrix == ((696, 1), (20736000, 384)), "T2 matrix")
    checked = 0
    for column, row in enumerate((a, b)):
        for n in range(1, (len(a) - 1) // 2 + 1):
            work.spend()
            actual = row[2 * n] + (2**23 * row[n // 2] if n % 2 == 0 else 0)
            require(actual == matrix[0][column] * a[n] + matrix[1][column] * b[n], "T2")
            checked += 1
    defect = (
        a[6] - a[2] * a[3],
        b[6] - a[2] * b[3] - b[2] * a[3],
        -b[2] * b[3],
    )
    require(defect == tuple(48 * x for x in (-20736000, 312, 1)), "Hecke polynomial")
    require(156**2 + 20736000 == 144 * 144169, "quadratic radical")
    return {"T2": matrix, "coefficient_checks": checked, "defect_coefficients": defect}


def series(values):
    require(type(values) is dict, "finite frequency dictionary required")
    integer(len(values), 0, MAX_TERMS)
    out = {}
    for frequency, coefficient in values.items():
        frequency, coefficient = (
            exact(frequency, internal=True),
            exact(coefficient, internal=True),
        )
        require(frequency >= 1, "frequency below one")
        if coefficient:
            out[frequency] = coefficient
    return out


def series_add(left, right):
    left, right = series(left), series(right)
    require(len(set(left) | set(right)) <= MAX_TERMS, "support cap before addition")
    out = dict(left)
    for key, value in right.items():
        out[key] = exact(out.get(key, F(0)) + value, internal=True)
    return {key: value for key, value in out.items() if value}


def series_mul(left, right, cutoff, work):
    cutoff = exact(cutoff)
    require(1 <= cutoff <= MAX_CUTOFF, "frequency cutoff")
    left, right, work = series(left), series(right), budget(work)
    work.spend(len(left) * len(right))
    out = {}
    for u, a in left.items():
        for v, b in right.items():
            frequency = exact(u * v, internal=True)
            if frequency <= cutoff:
                if frequency not in out:
                    require(len(out) < MAX_TERMS, "support cap before allocation")
                out[frequency] = exact(out.get(frequency, F(0)) + a * b, internal=True)
    return {key: value for key, value in out.items() if value}


def depth_bound(cutoff):
    cutoff = exact(cutoff)
    require(F(9, 2) <= cutoff <= MAX_CUTOFF, "public quotient cutoff")
    depth, first = 0, F(9, 2)
    while first * F(3, 2) <= cutoff:
        depth += 1
        first *= F(3, 2)
    return depth


def frequency_control(cutoff, source=None, work=None):
    cutoff = exact(cutoff)
    depth = depth_bound(cutoff)
    work = Budget() if work is None else budget(work)
    if source is None:
        source = qsource(MAX_Q, work)
    require(type(source) in (tuple, list) and len(source) == 3, "source triple")
    a, b, c = map(polynomial, source)
    require(len(a) == len(b) == len(c) == MAX_Q + 1, "complete q source through24")
    require(c == tuple(x - 696 * y for x, y in zip(a, b)), "source shear")
    require(
        (b[1], b[2], b[3], c[1], c[2], c[3]) == (0, 1, -48, 1, 0, 195660),
        "leading source",
    )
    # The declared q-prefix suffices: all correction indices >=3 and
    # nm/2<=cutoff imply n,m<=2*cutoff/3; every extra index l satisfies
    # (9/2)*(l/2)<=cutoff.  B's integer index is at most cutoff.
    u = {F(n, 2): b[n] ** 2 for n in range(3, MAX_Q + 1) if F(n, 2) <= cutoff}
    inverse, term = {F(1): F(1)}, {F(1): F(1)}
    for _ in range(depth):
        term = series_mul(term, {f: -v for f, v in u.items()}, cutoff, work)
        inverse = series_add(inverse, term)
    shifted_square = {}
    work.spend((MAX_Q - 2) ** 2)
    for n in range(3, MAX_Q + 1):
        for m in range(3, MAX_Q + 1):
            frequency = F(n * m, 2)
            if frequency <= cutoff:
                shifted_square[frequency] = (
                    shifted_square.get(frequency, 0) + c[n] * b[n] * c[m] * b[m]
                )
    correction = series_mul(shifted_square, inverse, cutoff, work)
    bare = series_add(
        {F(n): c[n] ** 2 for n in range(1, MAX_Q + 1) if n <= cutoff},
        {f: -v for f, v in correction.items()},
    )
    zeta = {
        F(d * d): d**46
        for d in range(1, math.isqrt(cutoff.numerator // cutoff.denominator) + 1)
    }
    uncompleted = series_mul(bare, zeta, cutoff, work)
    first_fractional = min(f for f in bare if f.denominator != 1)
    require(first_fractional == F(9, 2), "first noninteger frequency")
    expected = -88203653222400
    require(bare[F(9, 2)] == uncompleted[F(9, 2)] == expected, "fractional coefficient")
    require(bare.get(F(2), 0) == 0 and bare[F(3)] == 195660**2, "low integer terms")
    require(uncompleted[F(4)] == 12080128**2 + 2**46, "zeta square frequency")
    return {
        "cutoff": cutoff,
        "max_geometric_depth": depth,
        "next_depth_min_frequency": F(9, 2) * F(3, 2) ** (depth + 1),
        "bare_F": bare,
        "L_Q_zeta_times_F": uncompleted,
        "first_noninteger_frequency": first_fractional,
        "first_noninteger_coefficient_in_w_coordinates": expected,
        "full_q_tail_and_word_coverage_by_RQ10": True,
    }


def gram_control(weights, shear, scale, source, work):
    require(type(weights) in (list, tuple), "weight list")
    integer(len(weights), 2, 6)
    weights = tuple(exact(v) for v in weights)
    require(all(v > 0 for v in weights), "strict positive weights")
    shear, scale = exact(shear), exact(scale)
    require(scale != 0, "nonzero flag-line scale")
    require(type(source) in (list, tuple) and len(source) == 3, "source triple")
    a, b, _ = map(polynomial, source)
    require(min(len(a), len(b)) > len(weights), "Gram source length")
    work = budget(work)
    work.spend(3 * len(weights))
    g00 = sum(w * a[n] ** 2 for n, w in enumerate(weights, 1))
    g01 = sum(w * a[n] * b[n] for n, w in enumerate(weights, 1))
    g11 = sum(w * b[n] ** 2 for n, w in enumerate(weights, 1))
    det = g00 * g11 - g01**2
    require(g11 > 0 and det > 0, "finite coefficient Gram positivity")
    q = det / g11
    h00 = g00 + 2 * shear * g01 + shear**2 * g11
    h01 = scale * (g01 + shear * g11)
    h11 = scale**2 * g11
    require((h00 * h11 - h01**2) / h11 == q, "flag quotient invariance")
    minimizer = -g01 / g11
    require(g00 + 2 * minimizer * g01 + minimizer**2 * g11 == q, "quotient minimum")
    for value in (g00, g01, g11, det, q, h00, h01, h11):
        exact(value, internal=True)
    return {
        "weights": weights,
        "shear": shear,
        "line_scale": scale,
        "Gram": ((g00, g01), (g01, g11)),
        "quotient": q,
        "formal_endpoint_residues": (q / 2, -q / 2),
        "not_an_evaluated_Petersson_or_Eisenstein_Gram": True,
    }


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def lf_sha(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def bad_constant(value):
        raise ValueError("nonfinite JSON: " + value)

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=pairs,
        parse_constant=bad_constant,
    )


def expected_manifest():
    return {
        "schema": "rankin-selberg-quotient-sources-v1",
        "authoring_base": BASE,
        "context_sources": [
            {
                "role": "published_programme_checkpoint_not_analytic_dependency",
                "commit": BASE,
                "path": CONTEXT[0],
                "git_blob": CONTEXT[1],
                "sha256_lf": CONTEXT[2],
            }
        ],
        "primitive_definitions": {
            "q": "exp(2*pi*i*z)",
            "E4": "1+240*sum_(n>=1) sigma_3(n)*q^n",
            "Delta": "q*product_(m>=1)(1-q^m)^24",
            "f0": "Delta*E4^3",
            "f1": "Delta^2",
            "shift": "w=s+23",
            "completion": "A(s)=pi^(-s)*Gamma(s)*(4*pi)^(-s-23)*Gamma(s+23)",
            "scalar": "Q(s)=A(s)*zeta(2s)*(D00-D01*D10/D11)",
        },
        "external_contracts": [
            {"url": url, "contract": contract, "remote_bytes_authenticated": False}
            for url, contract in EXTERNAL
        ],
    }


def authenticate_sources(manifest=None):
    manifest = read_json(MANIFEST) if manifest is None else manifest
    require(
        canonical(manifest) == canonical(expected_manifest()),
        "complete manifest contract",
    )
    ref = BASE + ":" + CONTEXT[0]
    blob = (
        subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
        .decode()
        .strip()
    )
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
    require(blob == CONTEXT[1] and lf_sha(raw) == CONTEXT[2], "frozen context identity")
    return {
        "context_source_count": 1,
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "analytic_imports_formally_verified": False,
        "remote_bytes_authenticated": False,
    }


def serialize(value):
    if type(value) is F:
        return str(value)
    if type(value) in (list, tuple):
        return [serialize(v) for v in value]
    if type(value) is dict:
        return {str(k): serialize(v) for k, v in value.items()}
    return value


def build_report():
    auth = authenticate_sources()
    require(
        not any(
            isinstance(n, ast.Assert)
            for n in ast.walk(ast.parse(Path(__file__).read_text()))
        ),
        "-O invariant checks required",
    )
    work = Budget()
    source = qsource(MAX_Q, work)
    hecke = hecke_control(source[0], source[1], work)
    frequencies = [
        frequency_control(cutoff, source, work)
        for cutoff in (F(9, 2), F(6), F(10), F(12))
    ]
    grams = [
        gram_control(weights, shear, scale, source, work)
        for weights, shear, scale in (
            ((1, 1), 0, 1),
            ((F(1, 2), F(1, 3), F(1, 5)), F(2, 3), F(-3, 2)),
            ((1, 2, 3, 4, 5, 6), -696, 2),
        )
    ]
    directions = ((source[0][n], source[1][n]) for n in range(1, 4))
    directions = tuple(directions)
    minors = tuple(
        directions[i][0] * directions[j][1] - directions[j][0] * directions[i][1]
        for i, j in ((0, 1), (0, 2), (1, 2))
    )
    require(minors == (1, -48, -195660), "three independent projective directions")
    return serialize(
        {
            "schema": "rankin-selberg-quotient-global-parent-v1",
            "status": "PROPOSED_NATIVE_THEOREM_WITH_CLASSICAL_IMPORTS_REQUIRING_REVIEW",
            "arithmetic_class": "EXACT_RATIONAL",
            "source_authentication": auth,
            "artifact_sha256_lf": {
                p.relative_to(ROOT).as_posix(): lf_sha(p.read_bytes())
                for p in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "q_order": MAX_Q,
                "frequency_cutoff": MAX_CUTOFF,
                "series_terms": MAX_TERMS,
                "input_bits": INPUT_BITS,
                "internal_bits": INTERNAL_BITS,
                "max_work": MAX_WORK,
            },
            "coverage": {
                "q_coefficients_each": MAX_Q,
                "independent_Delta_recurrence": True,
                "frequency_cutoffs": len(frequencies),
                "finite_Gram_controls": len(grams),
                "work_units": work.used,
                "unbounded_search": False,
            },
            "source_q_rows": [
                (n, source[0][n], source[1][n], source[2][n])
                for n in range(1, MAX_Q + 1)
            ],
            "Hecke_calibration": hecke,
            "first_three_direction_minors": minors,
            "frequency_controls": frequencies,
            "finite_Gram_controls": grams,
            "scope": {
                "canonical_relative_to_cusp_flag": True,
                "classical_period_source": True,
                "completed_reflection_by_written_proof": True,
                "completed_endpoint_poles": [0, 1],
                "additional_denominator_zero_poles_allowed": True,
                "positivity_only_claimed_real_sigma_gt_one": True,
                "ordinary_absolutely_convergent_Dirichlet_series_excluded": True,
                "ordinary_prime_absolutely_expandable_Euler_product_excluded": True,
                "generalized_prime_systems_excluded": False,
                "all_possible_direct_sum_representations_excluded": False,
                "new_automorphic_representation": False,
                "analytic_proof_machine_verified": False,
                "numerical_period_or_zero_samples": 0,
                "RH_GRH_or_novelty_claim": False,
            },
        }
    )


def validate_report(report):
    require(
        canonical(report) == canonical(build_report()),
        "complete typed rebuild mismatch",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit-report", action="store_true")
    mode.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(json.dumps(expected_manifest(), sort_keys=True, indent=2))
    elif args.emit_report:
        print(json.dumps(build_report(), sort_keys=True, indent=2))
    else:
        validate_report(read_json(FIXTURE))
        print(
            "Rankin-Selberg quotient exact controls PASS; analytic imports/poles/RH boundaries retained"
        )


if __name__ == "__main__":
    main()
