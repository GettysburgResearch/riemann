"""Exact finite controls for the native cusp quotient's local simple zero."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import types
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "cusp_flag_local_simple_endpoint_zero"
NOTE = HERE / "CUSP_FLAG_LOCAL_SIMPLE_ENDPOINT_ZERO.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "98b4058ac29ba88cf993d7a3ce67579fab0c7844"
MAX_Q, MAX_WORK, SOURCE_WORK = 8, 2000000, 300000
BITS, INPUT_BITS, MAX_BYTES, MAX_JSON_NODES = 4096, 128, 2000000, 20000
BINDINGS = [
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_all_weight_real_endpoint",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_ALL_WEIGHT_ENDPOINT_SEPARATION.md",
        "git_blob": "3e6a8d13959a69bf7f261747f65ea5e52f3d82ff",
        "sha256_lf": "920a7fcf1e63de46e902846b747bed2b7da5defbd34e9fec9b98a61866cb1d2d",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_all_weight_real_endpoint",
        "path": "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.py",
        "git_blob": "1f1ec4ba008f86de0c4ad553748aabe98cd38bef",
        "sha256_lf": "04c2f8ac0b93be7d7621bcab8284fab63de5987e18f86e4e204107483fac782b",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_all_weight_real_endpoint",
        "path": "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.json",
        "git_blob": "4174d3423c2b901f09fc320a51afbda32c5ad1f9",
        "sha256_lf": "0cfd9a8742b4f9ef9eb503e6a818a87ecb27774989403f9a3f07aff49aefcf23",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_all_weight_real_endpoint",
        "path": "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.sources.json",
        "git_blob": "1c07e50b1a25bdeed5c98a536ce561c383c174c1",
        "sha256_lf": "6acf346bf72e6323dea4fd4b4f3e4ae137e85f7e2299409fc24226d688b06349",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_all_weight_real_endpoint",
        "path": "tests/test_cusp_flag_all_weight_endpoint_separation.py",
        "git_blob": "4b7222beb363d83e2468c72aae757a835e5c2bfc",
        "sha256_lf": "326b7cd43f7e77c264513e245c2fab6efeab95734bd2f713c9a7edc9efac66fe",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_endpoint_analytic_bounds",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md",
        "git_blob": "c95b70b98052c9b608ab15cd7adae39edab55363",
        "sha256_lf": "55ed2486b59066ec825efcf2beabb47da9b685f7891c1824f794733001b73941",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_endpoint_analytic_bounds",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.py",
        "git_blob": "7e7bed2c227e58a7c27e69a8ae3bf70e9805393d",
        "sha256_lf": "21f898a0944c13cf25a973c290f27b4703363f7d626922ad391c56ec625e1ce5",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_endpoint_analytic_bounds",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.json",
        "git_blob": "fd2ec70a97d1aff5b2a878dae30ef02cb4982e94",
        "sha256_lf": "45bff65cecca10a128efa142e29b6281ce81d3490e9ebceec3bcf961ecbc8b2b",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_endpoint_analytic_bounds",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.sources.json",
        "git_blob": "0e6a9c3aabb80def9638192f6af7a40b39f027ff",
        "sha256_lf": "9049ba583f6f1e489726576bbc3e787e31b6291db3bb3bd68be6943cef7938fb",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_endpoint_analytic_bounds",
        "path": "tests/test_cusp_flag_effective_endpoint_separation.py",
        "git_blob": "5b411d018ad3b6f88757a01e1b7e12e5f7a1d173",
        "sha256_lf": "a76a841fabad63f85f4c3156cf1aad2ddaf91468ec9b479325e768c69b5c1904",
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


def input_rational(value):
    value = rational(value)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= INPUT_BITS,
        "rational input bit cap",
    )
    return value


def gaussian(value):
    require(type(value) in (list, tuple) and len(value) == 2, "Gaussian rational shape")
    return rational(value[0]), rational(value[1])


def zadd(left, right):
    a, b = gaussian(left)
    c, d = gaussian(right)
    return gaussian((a + c, b + d))


def zneg(value):
    a, b = gaussian(value)
    return -a, -b


def zconj(value):
    a, b = gaussian(value)
    return a, -b


def zmul(left, right):
    a, b = gaussian(left)
    c, d = gaussian(right)
    return gaussian((a * c - b * d, a * d + b * c))


def zdiv(left, right):
    a, b = gaussian(left)
    c, d = gaussian(right)
    norm = rational(c * c + d * d)
    require(norm != 0, "Gaussian zero divisor")
    return gaussian(((a * c + b * d) / norm, (b * c - a * d) / norm))


def ztext(value):
    return [str(v) for v in gaussian(value)]


def matrix(value):
    require(type(value) in (tuple, list) and len(value) == 2, "matrix size2 cap")
    for row in value:
        require(type(row) in (tuple, list) and len(row) == 2, "matrix size2 cap")
    return [[gaussian(v) for v in row] for row in value]


def adjoint(value):
    value = matrix(value)
    return [[zconj(value[j][i]) for j in range(2)] for i in range(2)]


def matmul(left, right):
    left, right = matrix(left), matrix(right)
    return [
        [
            zadd(zmul(left[i][0], right[0][j]), zmul(left[i][1], right[1][j]))
            for j in range(2)
        ]
        for i in range(2)
    ]


def determinant(value):
    value = matrix(value)
    return zadd(zmul(value[0][0], value[1][1]), zneg(zmul(value[0][1], value[1][0])))


def mattext(value):
    return [[ztext(v) for v in row] for row in matrix(value)]


def point_control(x, y):
    x, y = input_rational(x), input_rational(y)
    require(abs(x) <= 32 and abs(y) <= 32, "point coordinate cap")
    norm = x * x + y * y
    require(norm != 0, "c=0 pole excluded")
    radius2 = (x - 12) ** 2 + y * y
    gap = rational(x / (2 * norm) - Q(1, 48))
    identity = rational((144 - radius2) / (48 * norm))
    require(gap == identity, "disc coercivity identity")
    side = "interior" if radius2 < 144 else "boundary" if radius2 == 144 else "exterior"
    require((gap > 0) == (side == "interior"), "strict interior equivalence")
    return {
        "c": [str(x), str(y)],
        "radius_squared": str(radius2),
        "coercivity_gap": str(gap),
        "side": side,
        "interior_coercivity_only": True,
    }


def radius_control(delta, radius):
    delta, radius = input_rational(delta), input_rational(radius)
    require(0 < delta < radius < 12, "fixed radii0<delta<R<12")
    margin = rational((12 - radius) / (48 * (12 + radius)))
    circle = rational(delta / (24 * (12 + delta)))
    require(margin > 0 and circle > 0, "positive fixed-radius reserves")
    return {
        "delta": str(delta),
        "R": str(radius),
        "m_R": str(margin),
        "kappa_R": str(margin / 2),
        "Rouche_lower": str(circle),
        "pole_distance": str(12 - radius),
        "effective_convergence_threshold": False,
        "varying_delta_allowed": False,
    }


def orientation_control():
    b, d = (1, 1), (-1, 1)
    actual = zneg(zdiv(zmul(b, b), d))
    false_adjoint = zneg(zdiv(zmul(b, zconj(b)), d))
    whole = [[(0, 0), b], [b, d]]
    require(actual == zdiv(determinant(whole), d), "literal Schur determinant")
    require(actual == (Q(-1), Q(1)), "true analytic Schur orientation")
    require(false_adjoint == (Q(1), Q(1)), "false Hermitian substitution exposed")
    reflected = adjoint(whole)
    require(
        zdiv(determinant(reflected), reflected[1][1]) == zconj(actual),
        "adjoint determinant conjugation",
    )
    return {
        "native_cusp_matrix": False,
        "D": ztext(d),
        "b": ztext(b),
        "actual_correction": ztext(actual),
        "false_adjoint_correction": ztext(false_adjoint),
        "complex_correction_nonnegative": False,
        "adjoint_determinant_conjugation": True,
    }


def nonnormal_control():
    d = [[(-2, 0), (0, 1)], [(0, 1), (-1, 0)]]
    star = adjoint(d)
    gram, opposite = matmul(star, d), matmul(d, star)
    reduced = [
        [zadd(gram[i][j], (-int(i == j), 0)) for j in range(2)] for i in range(2)
    ]
    inverse = [[(-Q(1, 3), 0), (0, -Q(1, 3))], [(0, -Q(1, 3)), (-Q(2, 3), 0)]]
    identity = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]
    require(matmul(d, inverse) == matrix(identity), "exact inverse identity")
    require(gram != opposite, "nonnormality control")
    require(
        reduced[0][0] == (Q(4), Q(0)) and determinant(reduced) == (Q(3), Q(0)),
        "positive principal minors, inverse norm at most1",
    )
    hermitian = [
        [tuple(v / 2 for v in zadd(d[i][j], star[i][j])) for j in range(2)]
        for i in range(2)
    ]
    require(
        hermitian == matrix([[(-2, 0), (0, 0)], [(0, 0), (-1, 0)]]),
        "negative Hermitian part not Hermitian matrix",
    )
    return {
        "native_cusp_matrix": False,
        "D": mattext(d),
        "Hermitian_part": mattext(hermitian),
        "DstarD_minus_Id": mattext(reduced),
        "principal_minors": [4, 3],
        "inverse": mattext(inverse),
        "normal": False,
        "inverse_norm_at_most1": True,
    }


def power_accounting():
    form, row, inverse, column, normalization = 1, 1, -1, 1, 1
    require(
        row + inverse + column == form == normalization, "dimension-free k accounting"
    )
    return {
        "form": form,
        "row": row,
        "inverse": inverse,
        "column": column,
        "Schur": row + inverse + column,
        "normalization": normalization,
        "normalized_power": row + inverse + column - normalization,
        "complex_Schur_smallness_required": False,
    }


def source_module(sources, name):
    require(
        type(name) is str and name in ("allweight", "endpoint"),
        "fixed source constructor enum",
    )
    stem = (
        "cusp_flag_all_weight_endpoint_separation"
        if name == "allweight"
        else "cusp_flag_effective_endpoint_separation"
    )
    path = "research/l-families/atlas/generalized/" + stem + ".py"
    raw = sources[path]
    binding = next(row for row in BINDINGS if row["path"] == path)
    require(lf_sha(raw) == binding["sha256_lf"], "source identity before execution")
    module = types.ModuleType("_authenticated_local_simple_" + name)
    module.__file__ = str(ROOT / path)
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def native_controls(sources, allweight, source_work):
    require(
        type(source_work) is allweight.Budget and source_work.limit <= SOURCE_WORK,
        "fixed capped authenticated source budget",
    )
    old = parse_json(
        sources[
            "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.json"
        ]
    )
    rows = []
    for reference in old["native_first_effective_prefixes"]:
        row = allweight.native_prefix(
            reference["weight"], reference["delta_power"], MAX_Q, source_work
        )
        require(
            canonical(row) == canonical(reference),
            "complete native AW prefix agreement",
        )
        rows.append(row)
    require(
        len(rows) == 12 and len({r["r"] for r in rows}) == 6,
        "six-class complete prefix coverage",
    )
    return rows


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    try:
        raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("invalid UTF-8") from exc
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lf_sha(raw):
    return hashlib.sha256(normalized(raw)).hexdigest()


def json_types(value, depth=0, counts=None):
    counts = [0, 0] if counts is None else counts
    counts[0] += 1
    require(counts[0] <= MAX_JSON_NODES, "total JSON node cap")
    require(depth <= 24, "JSON depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "JSON type")
    if type(value) is dict:
        require(len(value) <= 1024, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key")
            counts[1] += len(key.encode("utf-8"))
            require(counts[1] <= MAX_BYTES, "total JSON text byte cap")
            json_types(child, depth + 1, counts)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            json_types(child, depth + 1, counts)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
        counts[1] += len(value.encode("utf-8"))
        require(counts[1] <= MAX_BYTES, "total JSON text byte cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= BITS, "JSON integer cap")


def canonical(value):
    json_types(value)
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    require(len(result.encode()) <= MAX_BYTES, "canonical JSON byte cap")
    return result


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
        "schema": "cusp-flag-local-simple-endpoint-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "primitive_contract": {
            "object": "actual all-six-class canonical ell=[q] quotient and Petersson metric",
            "AW": "real compact asymptotic12/288; six actual classes; no inherited simplicity",
            "EP": "all-vector q-order moment bound; native half-lattice Fourier normalization",
            "new_complex": "Hermitian-part coercivity; separate row/column bounds; holomorphic local boundedness",
            "normal_family": "real interval convergence plus proved compact bounds; no complex rate",
            "Rouche": "each fixed0<delta<12 eventually exactly one zero counting multiplicity",
            "source_execution": "only fixed authenticated AW/EP finite functions with separate capped budget",
            "excluded": "no effective simplicity onset, global uniqueness, RH, or variable-delta result",
        },
        "primary_analytic_references": [
            "https://dlmf.nist.gov/10.32.E9",
            "https://dlmf.nist.gov/10.39.E2",
            "https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/",
        ],
        "remote_bytes_authenticated_offline": False,
    }


def authenticated_sources(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    output = {}
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
        output[row["path"]] = raw
    return output


def artifact_hashes():
    result = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        raw = path.read_bytes()
        require(
            all(v >= 32 or v in (9, 10, 13) for v in raw), "artifact control character"
        )
        result[path.relative_to(ROOT).as_posix()] = lf_sha(raw)
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
    allweight, endpoint = (
        source_module(sources, "allweight"),
        source_module(sources, "endpoint"),
    )
    work, source_work = Budget(), allweight.Budget(SOURCE_WORK)
    points = [
        (12, 0),
        (12, 1),
        (12, -1),
        (6, 3),
        (6, -3),
        (1, 0),
        (24, 0),
        (12, 12),
        (25, 0),
        (12, 13),
    ]
    radii = [(1, 2), (3, 6), (6, 9), (Q(23, 2), Q(47, 4))]
    work.spend(len(points) * 128 + len(radii) * 64 + 512)
    prefixes = native_controls(sources, allweight, source_work)
    return seal(
        {
            "schema": "cusp-flag-local-simple-endpoint-zero-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Gaussian Fraction pairs; no rounding; analytic values not sampled",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "disc_point_controls": [point_control(*point) for point in points],
            "fixed_radius_controls": [radius_control(*row) for row in radii],
            "analytic_Schur_orientation": orientation_control(),
            "nonnormal_inverse_control": nonnormal_control(),
            "power_accounting": power_accounting(),
            "native_six_class_prefixes": prefixes,
            "unchanged_real_location_ledger": endpoint.location_ledger(),
            "coverage": {
                "disc_points": len(points),
                "fixed_radii": len(radii),
                "native_prefixes": len(prefixes),
                "classes": 6,
                "charged_work": work.used,
                "charged_source_work": source_work.used,
            },
            "caps": {
                "q_order": MAX_Q,
                "matrix_size": 2,
                "point_absolute_coordinate": 32,
                "bits": BITS,
                "input_bits": INPUT_BITS,
                "work": MAX_WORK,
                "source_work": SOURCE_WORK,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_JSON_NODES,
            },
            "scope": {
                "eventual_each_fixed_disc_unique_simple": True,
                "all_six_actual_even_weight_classes": True,
                "denominator_complex_coercivity": True,
                "complex_matrix_Hermitian_assumed": False,
                "row_and_column_separately_bounded": True,
                "complex_Schur_correction_nonnegative": False,
                "actual_quotient_locally_bounded_holomorphic": True,
                "normal_family_no_complex_rate": True,
                "real_by_conjugation": True,
                "fine_REAL_location_inherited": True,
                "effective_simplicity_k0": False,
                "65536_simplicity_inherited": False,
                "global_uniqueness": False,
                "whole_open_chamber_uniform_uniqueness": False,
                "varying_delta": False,
                "RH_or_new_automorphic_family": False,
                "analytic_values_sampled": 0,
                "analytic_proof_machine_certified": False,
                "parents_modified": False,
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
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--emit-report", action="store_true")
    modes.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        result = expected_manifest()
    elif args.emit_report:
        result = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print("PASS_LOCAL_SIMPLE_CUSP_ENDPOINT; independent analytic review required")
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
