#!/usr/bin/env python3
"""Bounded exact controls for a source-specific positive-Laplace boundary."""

import argparse
import ast
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = "43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678"
NOTE = HERE / "CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md"
FIXTURE = HERE / "cusp_flag_positive_spectrum_boundary.json"
MANIFEST = HERE / "cusp_flag_positive_spectrum_boundary.sources.json"
TEST = ROOT / "tests/test_cusp_flag_positive_spectrum_boundary.py"
MAX_D, MAX_MATRIX, MAX_ATOMS, MAX_ORDER = 24, 4, 8, 32
INPUT_BITS, INTERNAL_BITS, MAX_WORK = 32, 4096, 200000
RESIDUAL = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}
EXCEPTIONS = {(10, 4): 169884, (20, 8): 142884}
BINDINGS = [
    {
        "commit": "43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "git_blob": "e3d6fd8aff9e5d65a5d9b692623a4978a3ef4170",
        "sha256_lf": "859c9e545ce5c0268054d878aa9642bd82bf9f6eb378a48aaa2731b0c0aae56f",
    },
    {
        "commit": "43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "git_blob": "326efd383cf0972c4f67a4d003d649cd9f7b895f",
        "sha256_lf": "70812297758842c27af5840f0c31e3e738093d9aad930330588b4f8ed1450b57",
    },
    {
        "commit": "43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "43ecb4ac3f2487ee944b6bb6bef72e1ad92f2678",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "git_blob": "e1e3b1574e98bcb5776f48f549e250e6fe8b22a6",
        "sha256_lf": "3f6e343d9953223dba7b9922bdde9ce619c5307a520db7a5795797eee562de82",
    },
    {
        "commit": "8e9f05211954e0a7aae5e63c9367f1d520d3671d",
        "path": "research/l-families/atlas/generalized/RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT_AUDIT.md",
        "git_blob": "383cf031153ef080fd1e8631b9d1788a0d0dc3b6",
        "sha256_lf": "f48587c5300d3c27835a49be36b700e4f574546da9521e8b8c5348d8a85d247f",
    },
]
EXTERNAL = (
    (
        "https://arxiv.org/html/2607.09868v1#S2",
        "Salazar Proposition2.3: classical signed-Laplace determinacy and negative-atom boundary; not a unique imported proof dependency",
    ),
    (
        "https://www.motapa.de/bernstein_functions/",
        "Schilling-Song-Vondracek author book page: classical Bernstein-Widder context; not a remotely authenticated theorem",
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


def rat(value, *, internal=False):
    require(type(internal) is bool, "internal flag type")
    require(type(value) in (int, Q), "exact rational required")
    result = Q(value)
    bits = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= bits,
        "rational bit cap",
    )
    return result


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, count):
        count = integer(count, 0, MAX_WORK)
        require(self.used + count <= self.limit, "work cap before expansion")
        self.used += count


def budget(work):
    require(type(work) is Budget, "Budget required")
    return work


def family_control(d, r, c_N, active_b, work=None):
    d = integer(d, 2, MAX_D)
    require(type(r) is int and r in RESIDUAL, "residual class")
    c_N, active_b = coefficient(c_N), coefficient(active_b)
    require(c_N * (1 if r in (0, 4, 8) else -1) > 0, "source c_N sign")
    a, b = RESIDUAL[r]
    top = 240 * a - 504 * b - 24 * d
    exceptional = (d, r) in EXCEPTIONS
    pivot = d - 1 if exceptional else d
    require(active_b == (EXCEPTIONS[d, r] if exceptional else top), "source pivot")
    require(active_b != 0 and (top == 0) is exceptional, "retained exception")
    work = Budget() if work is None else budget(work)
    work.spend(32)
    N, k = d + 1, 12 * d + r
    rho = Q(N * N, pivot)
    p = rho.numerator // rho.denominator
    require(p < rho < p + 1, "fractional atom")
    if exceptional:
        candidates = (
            Q(N * (N + 1), d - 1),
            Q((N + 1) ** 2, d),
            Q(N * N, d - 2),
            rho * Q(N, d),
        )
        require(p == d + 3, "exception bracket")
    else:
        candidates = (Q(N * (N + 1), d), Q(N**3, d**2))
        if d >= 3:
            candidates += (Q(N * N, d - 1),)
        require(p == d + 2, "ordinary bracket")
    require(all(v > p + 1 for v in candidates), "nonfirst correction gap")
    lead_f = coefficient(c_N**2)
    lead_l = coefficient(
        (lead_f if N <= 4 else 0) + (2 ** (2 * k - 2) if N >= 4 else 0)
    )
    negative = coefficient(-((c_N * active_b) ** 2))
    return {
        "weight": k,
        "dimension": d,
        "residual": r,
        "N": N,
        "c_N": c_N,
        "top_b_N": top,
        "active_pivot": pivot,
        "active_b_N": active_b,
        "negative_frequency": rho,
        "negative_coefficient_w_F_and_L": negative,
        "adjacent_integer_bracket": [p, p + 1],
        "nonfirst_correction_lower_bounds": candidates,
        "F_first_positive_frequency": N,
        "F_first_positive_coefficient": lead_f,
        "L_first_positive_frequency": min(4, N),
        "L_first_positive_coefficient": lead_l,
        "effective_cusp_derivative_onset_computed": False,
    }


def matrix(value):
    require(type(value) in (list, tuple), "matrix container")
    n = integer(len(value), 1, MAX_MATRIX)
    require(
        all(type(row) in (list, tuple) and len(row) == n for row in value),
        "square matrix shape",
    )
    return tuple(tuple(rat(x, internal=True) for x in row) for row in value)


def vector(value, n, *, internal=False):
    n = integer(n, 1, MAX_MATRIX)
    require(type(value) in (list, tuple) and len(value) == n, "vector shape")
    return tuple(rat(x, internal=internal) for x in value)


def positive_solve(value, rhs, work):
    value = matrix(value)
    n, work = len(value), budget(work)
    rhs = vector(rhs, n, internal=True)
    require(
        all(value[i][j] == value[j][i] for i in range(n) for j in range(n)), "symmetric"
    )
    work.spend(n**3 + n**2)
    a, b = [list(row) for row in value], list(rhs)
    for j in range(n):
        require(a[j][j] > 0, "positive elimination pivot")
        for i in range(j + 1, n):
            scale = rat(a[i][j] / a[j][j], internal=True)
            for col in range(j, n):
                a[i][col] = rat(a[i][col] - scale * a[j][col], internal=True)
            b[i] = rat(b[i] - scale * b[j], internal=True)
    result = [Q(0)] * n
    for i in range(n - 1, -1, -1):
        result[i] = rat(
            (b[i] - sum(a[i][j] * result[j] for j in range(i + 1, n))) / a[i][i],
            internal=True,
        )
    return tuple(result)


def quadratic(a, value):
    value = matrix(value)
    a = vector(a, len(value), internal=True)
    return rat(
        sum(a[i] * value[i][j] * a[j] for i in range(len(a)) for j in range(len(a))),
        internal=True,
    )


def envelope_control(atoms, work=None):
    """Atoms supply exact already-tilted weights at one real basepoint."""
    require(type(atoms) in (tuple, list), "atom container")
    integer(len(atoms), 1, MAX_ATOMS)
    require(
        all(type(atom) in (tuple, list) and len(atom) == 3 for atom in atoms),
        "atom triple",
    )
    require(type(atoms[0][2]) in (list, tuple), "atom vector container")
    n = integer(len(atoms[0][2]), 2, MAX_MATRIX)
    clean = []
    for rate, weight, row in atoms:
        rate, weight = integer(rate, 0, MAX_ORDER), rat(weight)
        require(weight > 0, "positive atom weight")
        clean.append((rate, weight, vector(row, n)))
    work = Budget() if work is None else budget(work)
    work.spend(3 * len(clean) * n * n + 4 * n * n)
    moments = []
    for h in range(3):
        moments.append(
            tuple(
                tuple(
                    rat(
                        sum(
                            weight * (-rate) ** h * row[i] * row[j]
                            for rate, weight, row in clean
                        ),
                        internal=True,
                    )
                    for j in range(n)
                )
                for i in range(n)
            )
        )
    D, D1, D2 = moments
    positive_solve(D, (1,) + (0,) * (n - 1), work)
    H = tuple(tuple(D[i][j] for j in range(1, n)) for i in range(1, n))
    y = positive_solve(H, tuple(-D[i][0] for i in range(1, n)), work)
    a = (Q(1),) + y
    g = tuple(
        rat(sum(D1[i][j] * a[j] for j in range(n)), internal=True) for i in range(1, n)
    )
    inverse_g = positive_solve(H, g, work)
    loss = rat(2 * sum(x * z for x, z in zip(g, inverse_g)), internal=True)
    F, F1, parent_F2 = (quadratic(a, D), quadratic(a, D1), quadratic(a, D2))
    require(F > 0 and F1 <= 0 and parent_F2 >= 0 and loss >= 0, "Gram envelope signs")
    require(
        all(sum(D[i][j] * a[j] for j in range(n)) == 0 for i in range(1, n)),
        "stationarity",
    )
    return {
        "dimension": n,
        "atoms_rate_tilted_weight_vector": clean,
        "D_Dprime_Dsecond": moments,
        "minimizer_coordinates": a,
        "F": F,
        "Fprime": F1,
        "frozen_vector_second_derivative": parent_F2,
        "curvature_loss": loss,
        "Fsecond": rat(parent_F2 - loss, internal=True),
        "source_kind": "FINITE_RATIONAL_GRAM_CALIBRATION_NOT_CUSP_FORMS",
    }


def moving_toy(order, ratio=Q(3, 5), work=None):
    order = integer(order, 1, MAX_ORDER)
    ratio = rat(ratio)
    require(0 < ratio < 1, "toy ratio in (0,1)")
    work = Budget() if work is None else budget(work)
    work.spend(8 * order + 12)
    t = rat(ratio**order, internal=True)
    signed_derivative = rat(
        sum(a * rate**order * t**rate for rate, a in ((1, 2), (2, -1), (3, 1))),
        internal=True,
    )
    denominator = rat((2 * ratio**2) ** order, internal=True)
    normalized = rat(signed_derivative / denominator, internal=True)
    alternate = rat(
        2 * (1 / (2 * ratio)) ** order - 1 + (3 * ratio / 2) ** order,
        internal=True,
    )
    require(normalized == alternate, "exact toy extraction identity")
    return {
        "order": order,
        "sample_w": "order*log(1/ratio)",
        "ratio": ratio,
        "exp_minus_w": t,
        "signed_derivative": signed_derivative,
        "positive_normalizer": denominator,
        "normalized_derivative": normalized,
        "negative": signed_derivative < 0,
        "actual_cusp_sample": False,
    }


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def lf_sha(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def parse_json(raw):
    require(type(raw) is str, "JSON text required")

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def nonfinite(value):
        raise ValueError("nonfinite JSON: " + value)

    result = json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
    canonical(result)
    return result


def expected_manifest():
    return {
        "schema": "cusp-flag-positive-spectrum-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(entry) for entry in BINDINGS],
        "primitive_contract": {
            "source": "Full integral Miller basis and first-coefficient flag of CF1",
            "variable": "w=s+k-1; every derivative is d/dw",
            "F": "D11-D1W*DW^-1*DW1",
            "L": "zeta(2w-2k+2)*F(w)",
            "completion_unchanged": "Q(s)=A_k(s)*L(s+k-1), not assigned Laplace monotonicity",
            "source_import": "CF5-CF12 all-weight nonvanishing, absolute expansion and first fractional coefficient",
            "negative_atom_limit": "w_m=w0+m/log(rho_star); normalized mth derivative tends to its signed coefficient",
            "numerical_cusp_onset": "not computed; requires certified absolute tail mass",
        },
        "external_context": [
            {"url": url, "contract": contract, "remote_bytes_authenticated": False}
            for url, contract in EXTERNAL
        ],
    }


def authenticate_sources(manifest=None):
    manifest = (
        parse_json(MANIFEST.read_text(encoding="utf-8"))
        if manifest is None
        else manifest
    )
    require(
        canonical(manifest) == canonical(expected_manifest()),
        "complete typed source manifest",
    )
    family_raw = None
    for entry in BINDINGS:
        ref = entry["commit"] + ":" + entry["path"]
        blob = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        require(
            blob == entry["git_blob"] and lf_sha(raw) == entry["sha256_lf"],
            "frozen source identity",
        )
        if entry["path"].endswith("/cusp_flag_quotient_global_family.json"):
            family_raw = raw
    require(family_raw is not None, "authenticated family fixture missing")
    source = parse_json(family_raw.decode("utf-8"))
    require(source["schema"] == "cusp-flag-quotient-global-family-v1", "parent schema")
    require(
        type(source["family"]) is list and len(source["family"]) == 138,
        "source finite coverage",
    )
    return source, {
        "frozen_source_count": len(BINDINGS),
        "parent_fixture_sha256_lf": lf_sha(family_raw),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "remote_bytes_authenticated": False,
        "parent_q_producer_rerun": False,
    }


def artifact_digests():
    return {
        p.relative_to(ROOT).as_posix(): lf_sha(p.read_bytes())
        for p in (NOTE, Path(__file__), TEST, MANIFEST)
    }


def serialize(value):
    if type(value) is Q:
        return str(value)
    if type(value) in (tuple, list):
        return [serialize(v) for v in value]
    if type(value) is dict:
        return {str(k): serialize(v) for k, v in value.items()}
    return value


def build_report():
    source, auth = authenticate_sources()
    require(
        not any(
            isinstance(n, ast.Assert)
            for n in ast.walk(ast.parse(Path(__file__).read_text()))
        ),
        "acceptance must survive -O",
    )
    work = Budget()
    rows = []
    require(
        [(r["dimension"], r["residual"]) for r in source["family"]]
        == [(d, r) for d in range(2, MAX_D + 1) for r in RESIDUAL],
        "ordered complete parent rows",
    )
    for row in source["family"]:
        control = family_control(
            row["dimension"], row["residual"], row["c_N"], row["active_b_N"], work
        )
        require(
            control["negative_frequency"] == Q(row["first_fractional_frequency"])
            and control["negative_coefficient_w_F_and_L"]
            == row["first_fractional_coefficient_w"]
            and control["top_b_N"] == row["top_b_N"]
            and control["active_pivot"] == row["active_pivot"],
            "parent coefficient/pivot match",
        )
        rows.append(control)
    curvature = envelope_control(
        ((0, 1, (1, 0)), (1, 1, (0, 1)), (10, 1, (1, 3))), work
    )
    require(
        (
            curvature["F"],
            curvature["Fprime"],
            curvature["Fsecond"],
            curvature["curvature_loss"],
        )
        == (Q(11, 10), Q(-19, 100), Q(-46, 125), Q(729, 500)),
        "negative curvature calibration",
    )
    other = envelope_control(
        ((0, 1, (1, 0, 0)), (1, 1, (0, 1, 0)), (2, 2, (0, 0, 1)), (3, 1, (1, 2, 1))),
        work,
    )
    toys = [moving_toy(order, work=work) for order in (1, 2, 4, 8, 16, 32)]
    require(toys[3]["signed_derivative"] < 0, "exact eighth-order control")
    result = serialize(
        {
            "schema": "cusp-flag-positive-spectrum-boundary-v1",
            "status": "PROPOSED_SOURCE_STRUCTURAL_THEOREM_REQUIRING_INDEPENDENT_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact Python integers and Fraction; no rounding",
            "source_authentication": auth,
            "artifact_sha256_lf": artifact_digests(),
            "caps": {
                "dimension": MAX_D,
                "matrix_dimension": MAX_MATRIX,
                "atoms": MAX_ATOMS,
                "derivative_order": MAX_ORDER,
                "primitive_rational_bits": INPUT_BITS,
                "coefficient_and_internal_bits": INTERNAL_BITS,
                "work_units": MAX_WORK,
            },
            "coverage": {
                "family_rows": len(rows),
                "finite_gram_controls": 2,
                "signed_toy_controls": len(toys),
                "work_units": work.used,
                "unbounded_computation": False,
            },
            "family": rows,
            "finite_gram_controls": [curvature, other],
            "signed_toy_controls": toys,
            "scope": {
                "all_weight_claims_by_written_proof_and_parent": True,
                "F_and_L_strictly_gt_one_and_decreasing_w_gt_k": True,
                "fixed_order_eventual_signs": True,
                "one_tail_for_all_orders": False,
                "no_positive_Laplace_measure_in_fixed_variable_on_any_tail": True,
                "completed_Q_assigned_same_monotonicity": False,
                "actual_cusp_second_derivative_negativity": False,
                "certified_cusp_absolute_tail_mass": False,
                "effective_cusp_onset_computed": False,
                "uniform_in_weight_halfplane": False,
                "every_spectral_representation_excluded": False,
                "Weil_positivity_RH_GRH_or_novelty_claim": False,
                "analytic_proof_machine_verified": False,
            },
        }
    )
    result["payload_sha256_canonical_json"] = hashlib.sha256(
        canonical(result).encode()
    ).hexdigest()
    return result


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
        validate_report(parse_json(FIXTURE.read_text(encoding="utf-8")))
        print(
            "Positive-spectrum boundary exact controls PASS; actual cusp derivative onset remains uncomputed"
        )


if __name__ == "__main__":
    main()
