#!/usr/bin/env python3
"""Bounded exact cusp-flag controls; analytic all-weight claims have a written proof."""

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
NOTE = HERE / "CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md"
FIXTURE = HERE / "cusp_flag_quotient_global_family.json"
MANIFEST = HERE / "cusp_flag_quotient_global_family.sources.json"
TEST = ROOT / "tests/test_cusp_flag_quotient_global_family.py"
BASE = "8e9f05211954e0a7aae5e63c9367f1d520d3671d"
PARENT = "b62dfc6348661992bca659c99de226a1b6b22e14"
MAX_D, MAX_Q, MAX_CUTOFF = 24, 28, 28
INPUT_BITS, INTERNAL_BITS, MAX_WORK = 32, 4096, 20000000
MAX_STATES, MAX_TERMS = 4096, 1024
RESIDUAL = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}
EXCEPTIONS = {(10, 4): (-27000, 169884), (20, 8): (-54000, 142884)}
PREFIXES = ((2, 0, 12), (3, 0, 10), (3, 14, 8), (4, 0, 10), (10, 4, 14), (20, 8, 24))
SOURCE_DIR = "research/l-families/atlas/generalized/"
SOURCES = (
    (
        PARENT,
        SOURCE_DIR + "RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md",
        "4a3f9f0b6644bffdc94214e6fb2b60dfafdd93ca",
        "1828196e08782ce692f28e3fdec2feae55c6d24e9b3eb5c35ff1c315434aee75",
    ),
    (
        PARENT,
        SOURCE_DIR + "rankin_selberg_quotient_global_parent.py",
        "524c8ce891d79d751a324f70528e95e12bd5bc00",
        "214644425a7ee02aa145c14b8df45dc20d9dc5a8706f0e597657443728521098",
    ),
    (
        PARENT,
        SOURCE_DIR + "rankin_selberg_quotient_global_parent.json",
        "f44fe4d65225601e04d86c58e6d6d296c51126c7",
        "ff9c5e7cc43db1d9c63f317cd842e4337066ec30c30a2f8be6f45958648ce856",
    ),
    (
        PARENT,
        SOURCE_DIR + "rankin_selberg_quotient_global_parent.sources.json",
        "5fc1c031e34a879496165407f6c500d9abfeac5a",
        "f7675378cf26d6d026959ebe718cf90f99245a8ab98c2ac229e29fe90ada6415",
    ),
    (
        PARENT,
        "tests/test_rankin_selberg_quotient_global_parent.py",
        "479567d07bb4f553bcd9b00bcbe515ac53ad0b24",
        "db1df7d9c4dac3ab5a038e6d78a6647ec57c6611c477d9c8b40ead510bca16db",
    ),
    (
        BASE,
        SOURCE_DIR + "RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT_AUDIT.md",
        "383cf031153ef080fd1e8631b9d1788a0d0dc3b6",
        "f48587c5300d3c27835a49be36b700e4f574546da9521e8b8c5348d8a85d247f",
    ),
)
EXTERNAL = (
    (
        "https://www.math.ucla.edu/~wdduke/preprints/serre.pdf",
        "Duke-Jenkins equations2-8 and Corollary1: canonical integral basis and weight-two coefficient duality",
    ),
    (
        "https://wstein.org/books/modform/modform/level_one.html#the-miller-basis",
        "Stein Lemma2.20: Miller basis and triangular integral construction; original thesis not inspected",
    ),
    (
        "https://arxiv.org/pdf/math/0605783",
        "Miller-Schmid1.7-1.14: unfolding; completed reflected pole corrected using Zagier",
    ),
    (
        "https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf",
        "Zagier1(a)-(c): completed Eisenstein poles0,1, reflection, growth and period",
    ),
    (
        "https://doi.org/10.1137/0128007",
        "Anderson-Trapp1975: classical shorted-form boundary, not an imported proof dependency",
    ),
    (
        "https://www.numdam.org/item/AIF_2008__58_3_801_0/",
        "Boecherer-Chiera2008: adjacent Rankin-Selberg/Petersson work, no exact-quotient priority inference",
    ),
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lower, upper):
    require(type(value) is int and lower <= value <= upper, "integer type/cap")
    return value


def coefficient(value):
    require(
        type(value) is int and value.bit_length() <= INTERNAL_BITS,
        "coefficient type/bit cap",
    )
    return value


def exact(value, *, internal=False):
    require(type(internal) is bool, "internal flag type")
    require(type(value) in (int, F), "exact rational required")
    result = F(value)
    cap = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= cap,
        "rational bit cap",
    )
    return result


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, count=1):
        count = integer(count, 0, MAX_WORK)
        require(self.used + count <= self.limit, "work cap before expansion")
        self.used += count


def budget(work):
    require(type(work) is Budget, "Budget required")
    return work


def parameters(d, r, order):
    d = integer(d, 2, MAX_D)
    require(type(r) is int and r in RESIDUAL, "residual class")
    order = integer(order, d + 2, MAX_Q)
    return d, r, order


def polynomial(values, order):
    order = integer(order, 1, MAX_Q)
    require(
        type(values) in (tuple, list) and len(values) == order + 1, "polynomial shape"
    )
    return tuple(coefficient(v) for v in values)


def qmul(left, right, order, work):
    order = integer(order, 1, MAX_Q)
    left, right, work = polynomial(left, order), polynomial(right, order), budget(work)
    work.spend((order + 1) * (order + 2) // 2)
    out = [0] * (order + 1)
    for i, a in enumerate(left):
        for j in range(order + 1 - i):
            out[i + j] = coefficient(out[i + j] + a * right[j])
    return tuple(out)


def qpower(row, exponent, order, work):
    exponent = integer(exponent, 0, 3 * MAX_D + 2)
    order = integer(order, 1, MAX_Q)
    row, work = polynomial(row, order), budget(work)
    out = (1,) + (0,) * order
    while exponent:
        if exponent % 2:
            out = qmul(out, row, order, work)
        exponent //= 2
        if exponent:
            row = qmul(row, row, order, work)
    return out


def primitives(order, work):
    order = integer(order, 4, MAX_Q)
    work = budget(work)
    work.spend(order * (order + 1))
    e4 = (1,) + tuple(
        240 * sum(a**3 for a in range(1, n + 1) if n % a == 0)
        for n in range(1, order + 1)
    )
    e6 = (1,) + tuple(
        -504 * sum(a**5 for a in range(1, n + 1) if n % a == 0)
        for n in range(1, order + 1)
    )
    left, right = qpower(e4, 3, order, work), qpower(e6, 2, order, work)
    require(all((a - b) % 1728 == 0 for a, b in zip(left, right)), "Delta division")
    delta = tuple((a - b) // 1728 for a, b in zip(left, right))
    product = (0, 1) + (0,) * (order - 1)
    for n in range(1, order + 1):
        work.spend(min(24, order // n) + 1)
        factor = [0] * (order + 1)
        for j in range(min(24, order // n) + 1):
            factor[n * j] = (-1) ** j * math.comb(24, j)
        product = qmul(product, factor, order, work)
    require(product == delta, "independent Delta product/identity")
    return delta, e4, e6


def miller_basis(d, r, order=None, method="e4", work=None):
    # Validate all public caps before producing the primitive arrays.
    integer(d, 2, MAX_D)
    order = d + 2 if order is None else order
    d, r, order = parameters(d, r, order)
    require(type(method) is str and method in ("e4", "e6"), "basis method")
    work = Budget() if work is None else budget(work)
    delta, e4, e6 = primitives(order, work)
    a, b = RESIDUAL[r]

    def powers(row, count):
        result = [(1,) + (0,) * order]
        for _ in range(count):
            result.append(qmul(result[-1], row, order, work))
        return result

    dp = powers(delta, d)
    ep4 = powers(e4, a + (3 * (d - 1) if method == "e4" else 0))
    ep6 = powers(e6, b + (2 * (d - 1) if method == "e6" else 0))
    rows = []
    for j in range(1, d + 1):
        x = a + (3 * (d - j) if method == "e4" else 0)
        y = b + (2 * (d - j) if method == "e6" else 0)
        row = qmul(dp[j], qmul(ep4[x], ep6[y], order, work), order, work)
        rows.append(row)
    for i in range(d):
        for j in range(i + 1, d):
            work.spend(order + 1)
            scale = rows[i][j + 1]
            rows[i] = tuple(
                coefficient(x - scale * y) for x, y in zip(rows[i], rows[j])
            )
    require(
        all(rows[i][j + 1] == int(i == j) for i in range(d) for j in range(d)),
        "echelon identity",
    )
    return tuple(rows)


def colored_partitions(d, work):
    d, work = integer(d, 2, MAX_D), budget(work)
    K = 24 * (d + 1)
    work.spend(d * d)
    sigma = [0] + [
        sum(a for a in range(1, n + 1) if n % a == 0) for n in range(1, d + 1)
    ]
    p = [1]
    for n in range(1, d + 1):
        work.spend(n)
        value = coefficient(K * sum(sigma[h] * p[n - h] for h in range(1, n + 1)))
        require(value % n == 0, "partition integrality")
        p.append(value // n)
    require(p[d] < 44 * p[d - 1] and p[d] < 3828 * p[d - 2], "partition ratio controls")
    return tuple(p)


def family_row(d, r, work):
    integer(d, 2, MAX_D)
    d, r, order = parameters(d, r, d + 2)
    work = budget(work)
    rows = miller_basis(d, r, order, "e4", work)
    other = miller_basis(d, r, order, "e6", work)
    require(rows == other, "independent complete Miller bases")
    p = colored_partitions(d, work)
    _, e4, e6 = primitives(order, work)
    a, b = RESIDUAL[14 - r]
    complement = qmul(
        qpower(e4, a, order, work), qpower(e6, b, order, work), order, work
    )
    work.spend(d + 1)
    dual = coefficient(-sum(complement[j] * p[d - j] for j in range(d + 1)))
    N, c = d + 1, rows[0][d + 1]
    require(c == dual and c * (1 if r in (0, 4, 8) else -1) > 0, "duality/sign")
    a, b = RESIDUAL[r]
    top = 240 * a - 504 * b - 24 * d
    require(rows[-1][N] == top, "top pivot formula")
    pivot = d
    if (d, r) in EXCEPTIONS:
        next_top, next_pivot = EXCEPTIONS[d, r]
        require(top == 0 and rows[-1][N + 1] == next_top, "retained zero/next top")
        require(rows[-2][N] == next_pivot == 196884 + next_top, "exception next pivot")
        require(F(N * N, d - 1) < F((N + 1) ** 2, d), "exception endpoint minimum")
        pivot = d - 1
    else:
        require(top != 0, "unexpected zero top pivot")
    frequency, factor = F(N * N, pivot), rows[pivot - 1][N]
    require(frequency.denominator > 1 and factor != 0, "noninteger nonzero witness")
    return {
        "weight": 12 * d + r,
        "dimension": d,
        "residual": r,
        "q_order": order,
        "complete_basis_sha256_canonical_json": hashlib.sha256(
            canonical(rows).encode()
        ).hexdigest(),
        "c_N": c,
        "dual_c_N": dual,
        "top_b_N": top,
        "top_b_Nplus1": rows[-1][N + 1],
        "active_pivot": pivot,
        "active_b_N": factor,
        "first_fractional_frequency": frequency,
        "first_fractional_coefficient_w": coefficient(-((c * factor) ** 2)),
        "partition_ratios": (F(p[d], p[d - 1]), F(p[d], p[d - 2])),
        "first_N_direction_support": [i + 1 for i in range(d) if rows[i][N]],
    }


def depth_bound(d, cutoff):
    d, cutoff = integer(d, 2, MAX_D), exact(cutoff)
    require(F((d + 1) ** 2, d) <= cutoff <= MAX_CUTOFF, "frequency cutoff")
    depth, lower = 0, F((d + 1) ** 2, d)
    while lower * F(d + 1, d) <= cutoff:
        depth += 1
        lower *= F(d + 1, d)
    return depth


def insert(out, key, value, cap):
    value = coefficient(value)
    if not value:
        return
    if key not in out:
        require(len(out) < cap, "support cap before allocation")
    result = coefficient(out.get(key, 0) + value)
    if result:
        out[key] = result
    else:
        out.pop(key, None)


def frequency_control(d, r, cutoff, work=None):
    integer(d, 2, MAX_D)
    require(type(r) is int and r in RESIDUAL, "residual class")
    cutoff = exact(cutoff)
    depth = depth_bound(d, cutoff)
    N = d + 1
    pivot = d - 1 if (d, r) in EXCEPTIONS else d
    require(cutoff >= F(N * N, pivot), "cutoff before actual first witness")
    work = Budget() if work is None else budget(work)
    order = max(d + 2, cutoff.numerator // cutoff.denominator)
    rows = miller_basis(d, r, order, work=work)
    c, tail = rows[0], range(N, order + 1)
    bare = {
        F(n): coefficient(c[n] ** 2)
        for n in range(1, order + 1)
        if n <= cutoff and c[n]
    }
    states = {}
    work.spend((d - 1) * len(tail))
    for j in range(2, d + 1):
        for n in tail:
            freq = F(n, j)
            if freq * N <= cutoff:
                insert(states, (j, freq), c[n] * rows[j - 1][n], MAX_STATES)
    state_counts, closing_pairs = [], 0
    for h in range(depth + 1):
        state_counts.append(len(states))
        work.spend(len(states) * len(tail))
        for (j, freq), value in states.items():
            for n in tail:
                final = exact(freq * n, internal=True)
                factor = c[n] * rows[j - 1][n]
                if final <= cutoff and factor:
                    insert(bare, final, (-1) ** (h + 1) * value * factor, MAX_TERMS)
                    closing_pairs += 1
        if h == depth:
            break
        work.spend(len(states) * (d - 1) * len(tail))
        next_states = {}
        for (j, freq), value in states.items():
            for new in range(2, d + 1):
                for n in tail:
                    next_freq = exact(freq * F(n, new), internal=True)
                    if next_freq * N <= cutoff:
                        insert(
                            next_states,
                            (new, next_freq),
                            value * rows[j - 1][n] * rows[new - 1][n],
                            MAX_STATES,
                        )
        states = next_states
    completed = {}
    squares = range(1, math.isqrt(cutoff.numerator // cutoff.denominator) + 1)
    work.spend(len(bare) * len(squares))
    for freq, value in bare.items():
        for a in squares:
            if freq * a * a <= cutoff:
                insert(
                    completed,
                    freq * a * a,
                    value * a ** (2 * (12 * d + r) - 2),
                    MAX_TERMS,
                )
    first = min(f for f in bare if f.denominator != 1)
    expected = coefficient(-((c[N] * rows[pivot - 1][N]) ** 2))
    require(first == F(N * N, pivot), "first fractional frequency")
    require(
        bare[first] == completed[first] == expected < 0,
        "first coefficient/zeta survival",
    )
    return {
        "dimension": d,
        "residual": r,
        "weight": 12 * d + r,
        "cutoff": cutoff,
        "source_q_order": order,
        "max_depth_CF9": depth,
        "next_depth_lower_bound": F(N * N, d) * F(N, d) ** (depth + 1),
        "grouped_state_counts_by_depth": state_counts,
        "closing_grouped_state_pairs": closing_pairs,
        "bare_F": dict(sorted(bare.items())),
        "zeta_times_F": dict(sorted(completed.items())),
        "first_fractional_frequency": first,
        "first_fractional_coefficient_w": expected,
        "complete_tail_and_word_coverage_by_CF9": True,
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

    def nonfinite(value):
        raise ValueError("nonfinite JSON: " + value)

    result = json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=pairs,
        parse_constant=nonfinite,
    )
    canonical(result)  # Also rejects a finite-looking exponent overflowing to inf.
    return result


def expected_manifest():
    return {
        "schema": "cusp-flag-quotient-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [
            {"commit": commit, "path": path, "git_blob": blob, "sha256_lf": digest}
            for commit, path, blob, digest in SOURCES
        ],
        "primitive_definitions": {
            "q": "exp(2*pi*i*z)",
            "E4": "1+240*sum sigma_3(n)q^n",
            "E6": "1-504*sum sigma_5(n)q^n",
            "Delta": "(E4^3-E6^2)/1728=q*product(1-q^n)^24",
            "weights": "k=12d+r,d>=2,r in {0,4,6,8,10,14}",
            "flag": "ell=[q], W=ker ell; integral Miller q-echelon basis",
            "shift": "w=s+k-1",
            "completion": "pi^(-s)Gamma(s)(4pi)^(-s-k+1)Gamma(s+k-1)",
            "quotient": "Q=det(I_k)/det(I_W)=A_k*zeta(2s)*(B-C^t D_W^(-1) C)",
        },
        "external_contracts": [
            {"url": url, "contract": contract, "remote_bytes_authenticated": False}
            for url, contract in EXTERNAL
        ],
    }


def authenticate_sources(manifest=None):
    manifest = read_json(MANIFEST) if manifest is None else manifest
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    for commit, path, blob, digest in SOURCES:
        ref = commit + ":" + path
        actual = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        require(actual == blob and lf_sha(raw) == digest, "frozen source identity")
    return {
        "frozen_source_count": len(SOURCES),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "remote_bytes_authenticated": False,
    }


def artifact_digests():
    return {
        p.relative_to(ROOT).as_posix(): lf_sha(p.read_bytes())
        for p in (NOTE, Path(__file__), TEST, MANIFEST)
    }


def serialize(value):
    if type(value) is F:
        return str(value)
    if type(value) in (tuple, list):
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
        "checks must survive -O",
    )
    work = Budget()
    family = [family_row(d, r, work) for d in range(2, MAX_D + 1) for r in RESIDUAL]
    frequencies = [frequency_control(d, r, cutoff, work) for d, r, cutoff in PREFIXES]
    require(
        [(v["dimension"], v["residual"]) for v in family if not v["top_b_N"]]
        == list(EXCEPTIONS),
        "exact finite exception census",
    )
    return serialize(
        {
            "schema": "cusp-flag-quotient-global-family-v1",
            "status": "PROPOSED_ALL_WEIGHT_THEOREM_WITH_CLASSICAL_INPUTS_REQUIRING_REVIEW",
            "arithmetic_class": "EXACT_INTEGER_AND_RATIONAL",
            "source_authentication": auth,
            "artifact_sha256_lf": artifact_digests(),
            "caps": {
                "max_dimension": MAX_D,
                "max_q_order": MAX_Q,
                "max_cutoff": MAX_CUTOFF,
                "input_bits": INPUT_BITS,
                "internal_bits": INTERNAL_BITS,
                "max_states": MAX_STATES,
                "max_terms": MAX_TERMS,
                "max_work": MAX_WORK,
            },
            "coverage": {
                "dimension_interval": [2, MAX_D],
                "residuals": list(RESIDUAL),
                "family_rows": len(family),
                "frequency_prefixes": len(frequencies),
                "complete_bases_compared": 2 * len(family),
                "work_units": work.used,
                "unbounded_computation": False,
            },
            "partition_majorant_sum": F(14400, 12167),
            "family": family,
            "frequency_controls": frequencies,
            "scope": {
                "all_even_weights_dim_ge_two_by_written_proof": True,
                "fixed_weight_analytic_inverse_only": True,
                "uniform_in_weight_halfplane": False,
                "canonical_relative_to_source_cusp_flag": True,
                "meromorphic_reflection_by_classical_inputs": True,
                "endpoint_poles": [0, 1],
                "additional_denominator_zero_poles_allowed": True,
                "positivity_only_real_sigma_gt_one": True,
                "full_constant_congruence_diagonalization_excluded": True,
                "all_nontrivial_block_decompositions_excluded": False,
                "ordinary_absolutely_expandable_prime_products_excluded": True,
                "generalized_prime_systems_excluded": False,
                "new_automorphic_representation": False,
                "analytic_proof_machine_verified": False,
                "numerical_period_or_zero_samples": 0,
                "RH_GRH_or_exhaustive_novelty_claim": False,
            },
        }
    )


def validate_report(report):
    require(
        canonical(report) == canonical(build_report()),
        "complete typed reconstruction mismatch",
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
            "Cusp-flag family exact controls PASS; fixed-weight analytic and pole boundaries retained"
        )


if __name__ == "__main__":
    main()
