"""Bounded exact controls for actual canonical denominator-induced cusp poles."""

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
STEM = "cusp_flag_native_denominator_poles"
NOTE = HERE / "CUSP_FLAG_NATIVE_DENOMINATOR_POLES.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "1653565cc80cde6fa882ae9e150626187d3071d0"
MAX_Q, MAX_K, MAX_WORK, SOURCE_WORK = 8, 1048576, 2000000, 300000
BITS, INPUT_BITS, MAX_BYTES, MAX_JSON_NODES = 4096, 128, 2000000, 20000
BINDINGS = [
    {
        "commit": "1653565cc80cde6fa882ae9e150626187d3071d0",
        "kind": "native_complex_coercivity_normal_family",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_LOCAL_SIMPLE_ENDPOINT_ZERO.md",
        "git_blob": "0fa98ad20e040ea9b2e81c9906042ed56782bfaf",
        "sha256_lf": "a8a3e87b075f0d4c4f8834001c5b40b1b027bff23c5c32df88821116a0bcc13f",
    },
    {
        "commit": "1653565cc80cde6fa882ae9e150626187d3071d0",
        "kind": "native_complex_coercivity_normal_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_local_simple_endpoint_zero.py",
        "git_blob": "7ebf67ccbd2aba1059771c4a57d07f53de6ebe9b",
        "sha256_lf": "ddceb433c84a3d15b6e0298a415303aa75488990951ddb1b9bedb539176a3ef2",
    },
    {
        "commit": "1653565cc80cde6fa882ae9e150626187d3071d0",
        "kind": "native_complex_coercivity_normal_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_local_simple_endpoint_zero.json",
        "git_blob": "9c5df6fafa484118cb16b6e46e4fb36b5e92c610",
        "sha256_lf": "ab534135547ed8c82642b3d681988936a1e16b701d57f1736fa8c7294c27b1d7",
    },
    {
        "commit": "1653565cc80cde6fa882ae9e150626187d3071d0",
        "kind": "native_complex_coercivity_normal_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_local_simple_endpoint_zero.sources.json",
        "git_blob": "496034972646f6c0ac1cb73bbf5ccf51afdcee54",
        "sha256_lf": "b2abe7c462b1f87c5da3e8e46106dffe4defcc8ed080543a2f4bb534959b483a",
    },
    {
        "commit": "1653565cc80cde6fa882ae9e150626187d3071d0",
        "kind": "native_complex_coercivity_normal_family",
        "path": "tests/test_cusp_flag_local_simple_endpoint_zero.py",
        "git_blob": "be3719164ace6d90634efab5f07716b3421ba725",
        "sha256_lf": "17b15156c68918a52cba9198204cdb2fdbd475c5673a55499c516bece7457345",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_six_class_modular_source",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_ALL_WEIGHT_ENDPOINT_SEPARATION.md",
        "git_blob": "3e6a8d13959a69bf7f261747f65ea5e52f3d82ff",
        "sha256_lf": "920a7fcf1e63de46e902846b747bed2b7da5defbd34e9fec9b98a61866cb1d2d",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_six_class_modular_source",
        "path": "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.py",
        "git_blob": "1f1ec4ba008f86de0c4ad553748aabe98cd38bef",
        "sha256_lf": "04c2f8ac0b93be7d7621bcab8284fab63de5987e18f86e4e204107483fac782b",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_six_class_modular_source",
        "path": "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.json",
        "git_blob": "4174d3423c2b901f09fc320a51afbda32c5ad1f9",
        "sha256_lf": "0cfd9a8742b4f9ef9eb503e6a818a87ecb27774989403f9a3f07aff49aefcf23",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_six_class_modular_source",
        "path": "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.sources.json",
        "git_blob": "1c07e50b1a25bdeed5c98a536ce561c383c174c1",
        "sha256_lf": "6acf346bf72e6323dea4fd4b4f3e4ae137e85f7e2299409fc24226d688b06349",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "kind": "native_six_class_modular_source",
        "path": "tests/test_cusp_flag_all_weight_endpoint_separation.py",
        "git_blob": "4b7222beb363d83e2468c72aae757a835e5c2bfc",
        "sha256_lf": "326b7cd43f7e77c264513e245c2fab6efeab95734bd2f713c9a7edc9efac66fe",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_all_vector_moment_and_Eisenstein",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md",
        "git_blob": "c95b70b98052c9b608ab15cd7adae39edab55363",
        "sha256_lf": "55ed2486b59066ec825efcf2beabb47da9b685f7891c1824f794733001b73941",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_all_vector_moment_and_Eisenstein",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.py",
        "git_blob": "7e7bed2c227e58a7c27e69a8ae3bf70e9805393d",
        "sha256_lf": "21f898a0944c13cf25a973c290f27b4703363f7d626922ad391c56ec625e1ce5",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_all_vector_moment_and_Eisenstein",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.json",
        "git_blob": "fd2ec70a97d1aff5b2a878dae30ef02cb4982e94",
        "sha256_lf": "45bff65cecca10a128efa142e29b6281ce81d3490e9ebceec3bcf961ecbc8b2b",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_all_vector_moment_and_Eisenstein",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.sources.json",
        "git_blob": "0e6a9c3aabb80def9638192f6af7a40b39f027ff",
        "sha256_lf": "9049ba583f6f1e489726576bbc3e787e31b6291db3bb3bd68be6943cef7938fb",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_all_vector_moment_and_Eisenstein",
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


def bounded_integer(value):
    require(
        type(value) is int and abs(value).bit_length() <= BITS, "integer output bit cap"
    )
    return value


def source_module(sources, name):
    require(
        type(name) is str and name == "allweight", "fixed authenticated source enum"
    )
    path = "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.py"
    raw = sources[path]
    binding = next(row for row in BINDINGS if row["path"] == path)
    require(lf_sha(raw) == binding["sha256_lf"], "source identity before execution")
    module = types.ModuleType("_authenticated_native_poles_" + name)
    module.__file__ = str(ROOT / path)
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def native_pair(allweight, work, weight, order=MAX_Q):
    weight = integer(weight, 36, MAX_K)
    order = integer(order, 4, MAX_Q)
    require(
        type(work) is allweight.Budget and work.limit <= SOURCE_WORK,
        "capped source Budget",
    )
    k, d, r, a, b = allweight.parameters(weight)
    require(d >= 3, "actual W3 chart dimension")
    first = allweight.native_prefix(k, 1, order, work)
    second = allweight.native_prefix(k, 2, order, work)
    tau = bounded_integer(-24 + 240 * first["E4_power"] - 504 * b)
    require(tau == 60 * k - 744 - 864 * b, "actual shear coefficient identity")
    h = [
        bounded_integer(x - tau * y)
        for x, y in zip(first["q_prefix"], second["q_prefix"], strict=True)
    ]
    require(h[:3] == [0, 1, 0], "native ell1 and q2 cancellation")
    p = first["E4_power"]
    g1_q3 = bounded_integer(252 + 28800 * p * p - 32400 * p - 4536 * b - 120960 * p * b)
    require(first["q_prefix"][3] == g1_q3, "independent modular q3 formula")
    require(second["q_prefix"][3] == tau - 744, "native second-witness q3")
    require(h[3] == g1_q3 - tau * (tau - 744), "entire-tail starting coefficient")
    return {
        "weight": k,
        "dimension": d,
        "r": r,
        "a": a,
        "b": b,
        "g1": first,
        "g2": second,
        "tau": tau,
        "h_prefix": h,
        "h_q3": h[3],
        "W2_unchanged": True,
        "arbitrary_flag": False,
        "analytic_pole_onset_asserted_here": False,
    }


def native_controls(sources, allweight, source_work):
    old = parse_json(
        sources[
            "research/l-families/atlas/generalized/cusp_flag_all_weight_endpoint_separation.json"
        ]
    )
    reference = old["native_CF_small_prefixes"] + old["native_first_effective_prefixes"]
    weights = sorted(
        {r["weight"] for r in reference if r["dimension"] == 3 or r["weight"] >= 65536}
    )
    require(len(weights) == 12, "fixed twelve native pair controls")
    rows = [native_pair(allweight, source_work, k) for k in weights]
    for row in rows:
        for key in ("g1", "g2"):
            expected = next(
                r
                for r in reference
                if r["weight"] == row["weight"]
                and r["delta_power"] == row[key]["delta_power"]
            )
            require(
                canonical(row[key]) == canonical(expected),
                "complete frozen native prefix agreement",
            )
    return rows


def cauchy_envelope(k):
    k = integer(k, 48, MAX_K)
    radius = Q(1, 1000 * k)
    exponent = rational(Q(120, 1000) + (48 / (1 - radius) + 1008) / (1000 * k))
    require(exponent < Q(1, 4), "whole complex-q disc exponent")
    require(Q(1, 1) / (1 - Q(1, 4)) < 2, "product bound less than2")
    first_tail = 4 * 1000**2 + 4 * 100 * 1000
    second_tail = 4 * 1000
    require(
        first_tail == 4400000 and second_tail == 4000, "Cauchy shear tail constants"
    )
    return {
        "weight": k,
        "q_disc_radius": str(radius),
        "product_exponent_upper": str(exponent),
        "g1_shear_tail_k2_rho3": first_tail,
        "g2_tail_k_rho3": second_tail,
        "requires_rho_le_half_radius": True,
        "full_analytic_tail_not_prefix": True,
    }


def low_cutoff_control(k):
    k = integer(k, 4, MAX_K)
    eta, theta = Q(1, 10000), Q(1, 10)
    ratio = Q(k, k - 2)
    base = rational(24 * 4 * 3 * eta * ratio)
    require(
        ratio <= 2 and base <= 48 * 4 * 3 * eta < theta,
        "uniform factorial exponential base",
    )
    coefficient = rational(1056000 * 4 * eta * 2 * theta**-2)
    require(
        coefficient == 84480 and coefficient < 100000, "low mass constant absorption"
    )
    return {
        "integer_k_control": k,
        "eta": str(eta),
        "k_over_kminus2": str(ratio),
        "base_upper": str(base),
        "uniform_base": str(48 * 4 * 3 * eta),
        "theta": str(theta),
        "prefactor_k2": str(coefficient),
        "proved_mass_C_k4": 100000,
        "analytic_low_region_requires_k_ge10000": True,
        "pole_onset_computed": False,
    }


def bessel_control(nu, x):
    nu, x = input_rational(nu), input_rational(x)
    require(0 <= nu <= Q(1, 2) and x >= 1, "real Bessel control chamber")
    power, mean = nu - Q(1, 2), nu + Q(1, 2)
    loss = rational((Q(1, 4) - nu * nu) / (2 * x))
    tangent = rational(1 + power * mean / (2 * x))
    coarse = rational(1 - Q(1, 8) / x)
    require(
        tangent == 1 - loss and coarse <= tangent <= 1,
        "Gamma-integral tangent identity",
    )
    require(power * (power - 1) >= 0, "convex nonpositive power")
    return {
        "nu": str(nu),
        "x": str(x),
        "power": str(power),
        "Gamma_mean": str(mean),
        "tangent_lower": str(tangent),
        "coarse_lower": str(coarse),
        "upper": "1",
        "Bessel_value_sampled": False,
    }


def disc_point(x, y):
    x, y = input_rational(x), input_rational(y)
    require(abs(x) <= 64 and abs(y) <= 64, "point coordinate cap")
    norm = x * x + y * y
    require(norm > 0, "pole c0 excluded")
    gap = rational(x / (2 * norm) - Q(1, 72))
    distance = (x - 18) ** 2 + y * y
    require(gap == (324 - distance) / (72 * norm), "deeper W3 chamber identity")
    return {
        "c": [str(x), str(y)],
        "gap": str(gap),
        "inside": distance < 324,
        "boundary": distance == 324,
    }


def radius_control(delta, radius):
    delta, radius = input_rational(delta), input_rational(radius)
    require(0 < delta < radius < 12, "fixed0<delta<R<12")
    margin = rational((324 - (6 + radius) ** 2) / (72 * (24 + radius) ** 2))
    circle = rational(delta / (48 * (24 + delta)))
    require(margin > 0 and circle > 0, "fixed positive reserves")
    return {
        "delta": str(delta),
        "R": str(radius),
        "m_R": str(margin),
        "kappa_R": str(margin / 2),
        "Rouche_lower": str(circle),
        "effective_weight_threshold": False,
    }


def decay_ledger():
    rows = [
        ("P_cross_tail", 5, Q(3)),
        ("R_first_tail", 2, Q(3)),
        ("R_second_tail", 1, Q(5, 2)),
        ("R_double_tail", 3, Q(7, 2)),
        ("W3_cross_correction", 6, Q(3)),
        ("W3_self_correction", 5, Q(3)),
    ]
    out = []
    for name, polynomial_degree, n in rows:
        base = rational(2 / n)
        require(0 < base < 1, "strict exponential error scale")
        out.append(
            {
                "term": name,
                "polynomial_degree": polynomial_degree,
                "A_N": str(n),
                "ratio_base_to_A2": str(base),
            }
        )
    require(4 + 3 - 1 == 6 and 0 + 3 - 1 == 2, "dual norms times inverse powers")
    return {
        "ordinary_terms": out,
        "mixed_correction_polynomial_degree": 2,
        "mixed_squared_ratio_base": "2/3",
        "mixed_ratio": "(2/3)^((k-1)/2)",
        "Gamma_moment1_ratio": "(k-1)/(4*pi*N)",
        "analytic_decay_machine_certified": False,
    }


def normalization_ledger():
    source_cosine, x_integral = 4, Q(1, 2)
    half_order = Q(1, 2)
    require(
        source_cosine * x_integral * half_order == 1, "native n1 cross normalization"
    )
    c0 = 24
    derivative = Q(1, 2 * c0 * c0)
    residue = 1 / derivative
    require(
        derivative == Q(1, 1152) and residue == 1152,
        "second-scale derivative and residue",
    )
    return {
        "source_cosine_coefficient": source_cosine,
        "x_integral": str(x_integral),
        "half_order_K_sqrt_y_coefficient": str(half_order),
        "B0_over_A2_leading": "1",
        "q1_q2_decay_exponent_pi": 6,
        "Bessel_decay_exponent_pi": 2,
        "combined_exponent_pi": 8,
        "second_zero_c": c0,
        "F2_derivative_at24": str(derivative),
        "s_residue_coefficient": str(residue),
        "s_residue_A2_power": 1,
        "s_residue_k_power": -2,
        "dc_ds_sign": -1,
        "reflected_residue_sign": -1,
    }


def conditional_schur(a, b, slope):
    a, b, slope = input_rational(a), input_rational(b), input_rational(slope)
    require(slope != 0, "simple scalar zero slope")
    numerator = rational(-b * b)
    residue = rational(-b * b / slope)
    return {
        "nonnative_algebra_only": True,
        "a_at_zero": str(a),
        "b_at_zero": str(b),
        "d_prime": str(slope),
        "numerator_at_dzero": str(numerator),
        "c_residue": str(residue),
        "uncancelled_iff_b_nonzero": b != 0,
        "native_coupling_not_proved_by_this_control": True,
    }


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
        "schema": "cusp-flag-native-denominator-poles-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "primitive_contract": {
            "native_flags": "W2=ker[q], W3=ker[q] intersect ker[q2], full actual coefficient spaces",
            "native_shear": "h=g1-[q2]g1*g2; ell1 unchanged; all six classes",
            "cross_lower_bound": "whole-domain B_eff/A2=1+O(1/k), native n1 Fourier cosine coefficient4",
            "inverse_payment": "all-W3 dual bounds in Petersson norm, no dimension or free coefficient assumption",
            "complex_zero": "fixed disc24 radiusR<12; eventual holomorphy, normal families, Rouche",
            "residue": "Cauchy derivative convergence plus actual B_eff; 1152*A2/k2, positive at right pole",
            "excluded": "no effective onset, global pole census, RH, zero-free local disc or new family",
            "source_execution": "only authenticated AW bounded prefix functions",
        },
        "primary_analytic_references": [
            "https://dlmf.nist.gov/10.32.E8",
            "https://dlmf.nist.gov/10.39.E2",
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
    allweight = source_module(sources, "allweight")
    work, source_work = Budget(), allweight.Budget(SOURCE_WORK)
    pairs = native_controls(sources, allweight, source_work)
    work.spend(4096 + len(pairs) * 64)
    return seal(
        {
            "schema": "cusp-flag-native-denominator-poles-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; analytic values not sampled",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "native_shear_pairs": pairs,
            "whole_q_disc_envelopes": [cauchy_envelope(k) for k in (48, 65536, MAX_K)],
            "low_cutoff_controls": [
                low_cutoff_control(k) for k in (4, 48, 10000, 65536, MAX_K)
            ],
            "Bessel_tangent_controls": [
                bessel_control(nu, x)
                for nu in (Q(0), Q(1, 4), Q(1, 2))
                for x in (1, 10)
            ],
            "deeper_chamber_points": [
                disc_point(x, y)
                for x, y in ((24, 0), (24, 5), (18, 18), (36, 0), (37, 0), (1, 1))
            ],
            "fixed_disc_controls": [
                radius_control(d, r)
                for d, r in ((1, 2), (3, 6), (9, 11), (Q(23, 2), Q(47, 4)))
            ],
            "error_scale_ledger": decay_ledger(),
            "native_normalization_ledger": normalization_ledger(),
            "conditional_schur_controls": [
                conditional_schur(3, 2, 5),
                conditional_schur(3, 0, 5),
            ],
            "coverage": {
                "native_pairs": len(pairs),
                "classes": 6,
                "charged_work": work.used,
                "charged_source_work": source_work.used,
            },
            "caps": {
                "q_order": MAX_Q,
                "weight": MAX_K,
                "bits": BITS,
                "input_bits": INPUT_BITS,
                "work": MAX_WORK,
                "source_work": SOURCE_WORK,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_JSON_NODES,
            },
            "scope": {
                "actual_canonical_Q_additional_poles": True,
                "all_six_even_weight_classes_eventually": True,
                "fixed_delta_lt12": True,
                "local_simple_real_reflected_poles": True,
                "entire_tail_nonzero_effective_cross": True,
                "full_W3_metric_payment": True,
                "native_cosine_factor4_retained": True,
                "residue_1152_positive_right": True,
                "conditional_Schur_control_is_native_evidence": False,
                "denominator_zero_alone_implies_pole": False,
                "effective_pole_onset": False,
                "65536_pole_onset_inherited": False,
                "no_numerator_zeros_in_pole_disc": False,
                "global_pole_census": False,
                "RH_or_new_automorphic_family": False,
                "varying_delta": False,
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
        print(
            "PASS_NATIVE_CUSP_DENOMINATOR_POLES; independent analytic review required"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
