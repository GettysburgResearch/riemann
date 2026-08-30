"""Bounded exact algebra for the native signed cusp-flag counting law."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
import types
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "cusp_flag_signed_riemann_von_mangoldt"
NOTE = HERE / "CUSP_FLAG_SIGNED_RIEMANN_VON_MANGOLDT.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "a27781310ded92125ef16d97d78db4d97cec4c1b"
MAX_D, MAX_COLUMNS, MAX_SUBSETS = 20, 21, 4096
MAX_WORK, FAMILY_WORK, BITS, MAX_BYTES = 5000000, 2000000, 4096, 2000000
RESIDUALS = (0, 4, 6, 8, 10, 14)
PANELS = tuple((d, r) for d in (2, 3, 4) for r in RESIDUALS) + ((10, 4), (20, 8))
BINDINGS = [
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "git_blob": "7e6ae5bb1fd9c53930cee1198eb185806a2ea118",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "sha256_lf": "34120d58416c902db94fbeaf69ceb004694888908341b630a1b750f2f1e8316a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "git_blob": "7ca422e505e6ccd817aadee3362f1ace2fa83fd4",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "sha256_lf": "fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "git_blob": "c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a",
        "kind": "reviewed_family_release",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "sha256_lf": "84603f0412d8a7f1d2c2384c7055f55b4956db3df68b42dde7074d18cbe8265b",
    },
    {
        "commit": "a27781310ded92125ef16d97d78db4d97cec4c1b",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA.md",
        "kind": "frozen_native_growth_parent",
        "git_blob": "1ec20ba529d34b833799d72515921fda7252da81",
        "sha256_lf": "c7123450f6201fc62af7b2c42a315a20c5e107d0348533b7348223fbbd24d373",
    },
    {
        "commit": "a27781310ded92125ef16d97d78db4d97cec4c1b",
        "path": "research/l-families/atlas/generalized/cusp_flag_divisor_explicit_formula.py",
        "kind": "frozen_native_growth_parent",
        "git_blob": "81f8f778488e83fe7ae7d0a2c9296031558449cb",
        "sha256_lf": "45ebd934c6d8e3547bde285ea30b3a6b2574cd2f634300dd76044662829f83d9",
    },
    {
        "commit": "a27781310ded92125ef16d97d78db4d97cec4c1b",
        "path": "research/l-families/atlas/generalized/cusp_flag_divisor_explicit_formula.json",
        "kind": "frozen_native_growth_parent",
        "git_blob": "2eef1c6196789b852db99391b931d668da383b8e",
        "sha256_lf": "bdf15afc43f5d246b494f0c9ebd3b0947a5ba6209c0ccfa0418513abc1db3922",
    },
    {
        "commit": "a27781310ded92125ef16d97d78db4d97cec4c1b",
        "path": "research/l-families/atlas/generalized/cusp_flag_divisor_explicit_formula.sources.json",
        "kind": "frozen_native_growth_parent",
        "git_blob": "0649c2b51271f92499903fc209e575422c482d61",
        "sha256_lf": "bc8beef55e1301354f3ab7ae6c4954b196bb92a9bef7cdf745d64e5b49ac8aa4",
    },
    {
        "commit": "a27781310ded92125ef16d97d78db4d97cec4c1b",
        "path": "tests/test_cusp_flag_divisor_explicit_formula.py",
        "kind": "frozen_native_growth_parent",
        "git_blob": "cd121b856db740cf16bb78b7ff0cde1e4ad5a39a",
        "sha256_lf": "cd1d67310afba80e1efa40735532bb4a8036b05ad592fb39a5249cb6abe67a6d",
    },
]
EXTERNAL = [
    {
        "url": "https://arxiv.org/pdf/1208.5846v2",
        "role": "section2 equation2.4 real-part crossings; section3 Lemma1 Jensen",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/",
        "role": "section4 Theorem41 classical argument-principle counting framework",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://terrytao.wordpress.com/2009/02/28/tricks-wiki-give-yourself-an-epsilon-of-room/",
        "role": "Exercise1 classical maximum-principle strip damping",
        "remote_bytes_authenticated": False,
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def rational(value):
    require(type(value) in (int, Q), "strict rational type")
    value = Q(value)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= BITS,
        "rational bit cap",
    )
    return value


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, amount):
        amount = integer(amount, 0, MAX_WORK)
        require(self.used + amount <= self.limit, "charged work cap before expansion")
        self.used += amount


def checked_work(work):
    require(type(work) is Budget, "Budget required")
    return work


def matrix(value):
    require(type(value) in (list, tuple) and 1 <= len(value) <= MAX_D, "matrix row cap")
    require(type(value[0]) in (list, tuple), "matrix row type")
    columns = len(value[0])
    require(1 <= columns <= MAX_COLUMNS, "matrix column cap")
    result = []
    for row in value:
        require(type(row) in (list, tuple) and len(row) == columns, "ragged matrix")
        result.append([rational(x) for x in row])
    return result


def determinant(value, work=None):
    value = matrix(value)
    n = len(value)
    require(len(value[0]) == n, "square matrix required")
    work = Budget() if work is None else checked_work(work)
    work.spend(n**3)
    answer = Q(1)
    for column in range(n):
        pivot = next((j for j in range(column, n) if value[j][column]), None)
        if pivot is None:
            return Q(0)
        if pivot != column:
            value[pivot], value[column] = value[column], value[pivot]
            answer = -answer
        lead = value[column][column]
        answer = rational(answer * lead)
        for row in range(column + 1, n):
            ratio = rational(value[row][column] / lead)
            for j in range(column + 1, n):
                value[row][j] = rational(value[row][j] - ratio * value[column][j])
            value[row][column] = Q(0)
    return answer


def column_nodes(nodes, width):
    require(type(nodes) in (list, tuple) and len(nodes) == width, "node shape")
    nodes = tuple(integer(n, 1, MAX_COLUMNS) for n in nodes)
    require(list(nodes) == sorted(set(nodes)), "strictly increasing distinct nodes")
    return nodes


def cb_coefficients(value, nodes, work=None):
    value = matrix(value)
    rank, width = len(value), len(value[0])
    require(rank <= width, "rank/column shape")
    nodes = column_nodes(nodes, width)
    count = math.comb(width, rank)
    require(count <= MAX_SUBSETS, "subset cap before enumeration")
    work = Budget() if work is None else checked_work(work)
    work.spend(count * rank)
    output = {}
    for chosen in itertools.combinations(range(width), rank):
        minor = [[row[j] for j in chosen] for row in value]
        coefficient = rational(determinant(minor, work) ** 2)
        if coefficient:
            frequency = math.prod(nodes[j] for j in chosen)
            output[frequency] = rational(output.get(frequency, Q(0)) + coefficient)
    return output


def gram_determinant(value, nodes, exponent=2, work=None):
    value = matrix(value)
    rank, width = len(value), len(value[0])
    nodes = column_nodes(nodes, width)
    exponent = integer(exponent, 1, 4)
    work = Budget() if work is None else checked_work(work)
    work.spend(rank * rank * width)
    gram = [
        [
            rational(
                sum(
                    (
                        value[i][j] * value[h][j] / Q(nodes[j]) ** exponent
                        for j in range(width)
                    ),
                    Q(0),
                )
            )
            for h in range(rank)
        ]
        for i in range(rank)
    ]
    return determinant(gram, work)


def phase_ledger(d, residual):
    d = integer(d, 2, MAX_D)
    require(type(residual) is int and residual in RESIDUALS, "residual class")
    weight = 12 * d + residual
    product = math.factorial(d)
    rows = []
    for rank in (d, d - 1):
        # Formal coefficients are not evaluations of logarithms or pi.
        rows.append(
            {
                "rank": rank,
                "gamma_arguments": [
                    {"s_coefficient": 1, "shift": 0, "multiplicity": rank},
                    {"s_coefficient": 1, "shift": weight - 1, "multiplicity": rank},
                ],
                "phase_T_log_T": 2 * rank,
                "phase_T": -2 * rank,
                "phase_T_log_2": -2 * rank,
                "phase_T_log_pi": -2 * rank,
                "phase_T_log_P": -1,
                "P": product,
                "positive_count_pi_multiplier": 2 * rank,
                "real_endpoint_poles_each": rank,
            }
        )
    difference = {
        key: rows[0][key] - rows[1][key]
        for key in (
            "phase_T_log_T",
            "phase_T",
            "phase_T_log_2",
            "phase_T_log_pi",
            "phase_T_log_P",
            "positive_count_pi_multiplier",
            "real_endpoint_poles_each",
        )
    }
    require(
        difference["phase_T_log_T"] == 2 and difference["phase_T_log_P"] == 0,
        "native phase cancellation",
    )
    return {
        "weight": weight,
        "P": product,
        "determinants": rows,
        "quotient_difference": difference,
        "symbolic_contract": "pi*N_Q^+(T) = 2*T*log(T/(2*pi*e)) + O_k(log(T+2))",
        "logs_pi_gamma_or_phase_evaluated": False,
    }


def strip_ledger(rank, right):
    rank = integer(rank, 1, MAX_D)
    right = rational(right)
    require(2 < right <= 16, "finite right-line algebra domain")
    left = 1 - right
    exponent = rank * (2 - 4 * left)
    require(exponent == rank * (4 * right - 2), "FE gamma exponent")
    return {
        "rank": rank,
        "right": str(right),
        "left": str(left),
        "F_left_power": str(exponent),
        "H_left_power": str(exponent + rank),
        "inner_Jensen_radius": str(2 * right),
        "outer_Jensen_radius": str(4 * right),
        "window_inside_gap": str((2 * right) ** 2 - ((2 * right - 1) ** 2 + 1)),
        "actual_right_zero_free_abscissa_certified": False,
    }


def signed_divisor_control(full, minor, height):
    """Non-native finite divisor algebra only; locations are exact (Re, Im) pairs."""
    height = rational(height)
    require(0 <= height <= 32, "height cap")
    converted = []
    for source in (full, minor):
        require(type(source) is dict and len(source) <= 32, "finite divisor cap")
        result = {}
        for node, multiplicity in source.items():
            require(type(node) is tuple and len(node) == 2, "divisor node shape")
            node = tuple(rational(x) for x in node)
            require(max(abs(x) for x in node) <= 32, "divisor location cap")
            result[node] = integer(multiplicity, 1, 32)
        converted.append(result)
    a, b = converted
    native = lambda data: sum(m for (_, y), m in data.items() if 0 < y <= height)
    net = {node: a.get(node, 0) - b.get(node, 0) for node in a.keys() | b.keys()}
    net = {node: m for node, m in net.items() if m}
    signed = sum(m for (_, y), m in net.items() if 0 < y <= height)
    require(signed == native(a) - native(b), "signed cancellation identity")
    return {
        "height": str(height),
        "full_count": native(a),
        "minor_count": native(b),
        "net_signed_count": signed,
        "net_absolute_count": sum(
            abs(m) for (_, y), m in net.items() if 0 < y <= height
        ),
        "actual_cusp_flag_divisor_sample": False,
    }


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    raw.decode("utf-8")
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lf_sha(raw):
    return hashlib.sha256(normalized(raw)).hexdigest()


def json_types(value, depth=0):
    require(depth <= 24, "JSON depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "JSON type")
    if type(value) is dict:
        require(len(value) <= 1024, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key")
            json_types(child, depth + 1)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            json_types(child, depth + 1)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= BITS, "JSON integer cap")


def canonical(value):
    json_types(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def parse_json(raw):
    normalized(raw)

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def nonfinite(value):
        raise ValueError("nonfinite JSON " + value)

    try:
        result = json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
        json_types(result)
        return result
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def expected_manifest():
    return {
        "schema": "cusp-flag-signed-count-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": [dict(row) for row in EXTERNAL],
        "primitive_contract": {
            "object": "Q=det(I_k)/det(I_W), fixed full Miller first-coefficient flag",
            "native_pivots": "full1..d; minor2..d; common product d! and coefficient1",
            "growth": "EF5-EF11 actual theta growth plus native CF2 reflection",
            "count": "net signed ord Q, 0<Im rho<=T, all real parts",
            "constructor": "execute only authenticated frozen family producer bytes",
            "finite_Gram": "weights n^(-2); algebra only, not a continued period evaluation",
            "phase": "two Gamma factors and log(4*pi^2); log(d!) cancels",
        },
    }


def authenticated_sources(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    outputs = {}
    for row in BINDINGS:
        ref = row["commit"] + ":" + row["path"]
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", ref], cwd=ROOT, timeout=15
            )
        )
        require(0 <= size <= MAX_BYTES, "primitive byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and lf_sha(raw) == row["sha256_lf"],
            "primitive identity",
        )
        outputs[row["path"]] = raw
    return outputs


def frozen_family(sources):
    path = "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py"
    raw = sources[path]
    binding = next(row for row in BINDINGS if row["path"] == path)
    require(
        lf_sha(raw) == binding["sha256_lf"], "constructor identity before execution"
    )
    module = types.ModuleType("_authenticated_frozen_cusp_family")
    module.__file__ = str(ROOT / path)
    # Only a fixed, authenticated Git object reaches this constructor.
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def native_panel(family, frozen_row, d, residual, work, family_work):
    d = integer(d, 2, MAX_D)
    require(type(residual) is int and residual in RESIDUALS, "native residual")
    rows = family.miller_basis(d, residual, d + 2, "e4", family_work)
    other = family.miller_basis(d, residual, d + 2, "e6", family_work)
    require(rows == other, "two frozen Miller constructions")
    digest = hashlib.sha256(canonical([list(row) for row in rows]).encode()).hexdigest()
    require(
        type(frozen_row) is dict
        and frozen_row["dimension"] == d
        and type(frozen_row["dimension"]) is int
        and frozen_row["residual"] == residual
        and type(frozen_row["residual"]) is int
        and digest == frozen_row["complete_basis_sha256_canonical_json"],
        "complete frozen basis digest",
    )
    require(
        all(rows[i][j + 1] == int(i == j) for i in range(d) for j in range(d)),
        "native echelon identity",
    )
    product = math.factorial(d)
    controls = []
    for start in (0, 1):
        # In W the omitted n=1 column is explicitly zero, not an unexplained label collapse.
        if start:
            require(all(row[1] == 0 for row in rows[1:]), "W n1 zero column")
        nodes = tuple(range(1 + start, d + 2))
        value = [[row[n] for n in nodes] for row in rows[start:]]
        coefficients = cb_coefficients(value, nodes, work)
        require(
            min(coefficients) == product and coefficients[product] == 1,
            "native least product and coefficient",
        )
        weighted = rational(
            sum(
                (
                    coefficient / Q(frequency) ** 2
                    for frequency, coefficient in coefficients.items()
                ),
                Q(0),
            )
        )
        gram = gram_determinant(value, nodes, work=work)
        require(weighted == gram > 0, "finite Gram/Cauchy-Binet identity")
        controls.append(
            {
                "rank": d - start,
                "retained_nodes": list(nodes),
                "leading_product": product,
                "leading_coefficient": 1,
                "coefficient_map": {
                    str(key): str(coefficients[key]) for key in sorted(coefficients)
                },
                "finite_Gram_weight_exponent": 2,
                "finite_Gram_determinant": str(gram),
                "Cauchy_Binet_weighted_sum": str(weighted),
                "W_n1_zero_column_checked": bool(start),
                "infinite_period_evaluated": False,
                "all_infinite_tail_coefficients_computed": False,
            }
        )
    return {
        "dimension": d,
        "residual": residual,
        "weight": 12 * d + residual,
        "source_q_order": d + 2,
        "complete_basis_sha256_canonical_json": digest,
        "determinants": controls,
        "phase": phase_ledger(d, residual),
    }


def artifact_hashes():
    result = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        result[path.relative_to(ROOT).as_posix()] = lf_sha(path.read_bytes())
    return result


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload, "unsealed payload"
    )
    raw = canonical(payload).encode()
    require(len(raw) <= MAX_BYTES, "payload byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(raw).hexdigest()}


def build_report():
    sources = authenticated_sources()
    family = frozen_family(sources)
    data = parse_json(
        sources[
            "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json"
        ]
    )
    require(
        data["schema"] == "cusp-flag-quotient-global-family-v1"
        and type(data["family"]) is list
        and len(data["family"]) == 138,
        "parent complete family schema",
    )
    lookup = {(row["dimension"], row["residual"]): row for row in data["family"]}
    require(len(lookup) == 138, "parent pair uniqueness")
    work, family_work = Budget(), family.Budget(FAMILY_WORK)
    panels = [
        native_panel(family, lookup[(d, r)], d, r, work, family_work) for d, r in PANELS
    ]
    divisor = [
        signed_divisor_control(
            {(Q(1, 2), Q(3)): 4, (Q(1, 3), Q(2)): 1},
            {(Q(1, 2), Q(3)): 3, (Q(2, 3), Q(2)): 2},
            t,
        )
        for t in (Q(2), Q(5, 2), Q(3))
    ]
    return seal(
        {
            "schema": "cusp-flag-signed-riemann-von-mangoldt-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; logs and pi symbolic",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "native_panels": panels,
            "strip_geometry_controls": [
                strip_ledger(rank, right)
                for rank, right in ((1, 3), (2, Q(7, 2)), (20, 8))
            ],
            "non_native_divisor_algebra": divisor,
            "coverage": {
                "native_sources": 20,
                "native_determinants": 40,
                "complete_Miller_constructions": 40,
                "frozen_family_report_rerun": False,
                "frozen_Miller_constructor_called": True,
                "charged_work": work.used,
                "charged_frozen_family_work": family_work.used,
            },
            "caps": {
                "dimension": MAX_D,
                "columns": MAX_COLUMNS,
                "subsets": MAX_SUBSETS,
                "work": MAX_WORK,
                "frozen_family_work": FAMILY_WORK,
                "bits": BITS,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "fixed_weight_native_signed_law_by_written_proof": True,
                "polynomial_strip_growth_not_inferred_from_order_alone": True,
                "all_real_parts_included": True,
                "height_cutoff": "0<Im rho<=T; exceptional heights included by limits",
                "net_multiplicities_after_common_cancellation": True,
                "real_endpoint_poles_in_positive_count": False,
                "Q_count_assumed_monotone": False,
                "unsigned_Q_count_given_same_asymptotic": False,
                "critical_line_density_or_RH": False,
                "uncancelled_or_finitely_many_poles_asserted": False,
                "uniform_in_weight_or_effective_error_constant": False,
                "actual_period_phase_or_zero_samples": 0,
                "numerical_analytic_proof_certificate": False,
                "new_abstract_theory_or_novelty_claim": False,
            },
        }
    )


def validate_report(report):
    require(
        type(report) is dict and "payload_sha256" in report, "sealed report required"
    )
    payload = {key: value for key, value in report.items() if key != "payload_sha256"}
    require(canonical(report) == canonical(seal(payload)), "payload digest")
    require(
        canonical(report) == canonical(build_report()), "complete typed reconstruction"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit-report", action="store_true")
    mode.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        result = expected_manifest()
    elif args.emit_report:
        result = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS_CUSP_FLAG_SIGNED_COUNT; analytic counting proof is not machine-certified"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
