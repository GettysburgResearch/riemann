"""Exact bounded ledgers for effective native cusp endpoint separation."""

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
STEM = "cusp_flag_effective_endpoint_separation"
NOTE = HERE / "CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "bcd3ad5ff0c42e7b205663b68a010e2dbde6d941"
K, MAX_K, MAX_Q, MAX_ORDER, MAX_WORK = 65536, 1048576, 8, 32, 2000000
BITS, MAX_BYTES, MAX_JSON_NODES = 4096, 2000000, 20000

BINDINGS = [
    {
        "commit": "bcd3ad5ff0c42e7b205663b68a010e2dbde6d941",
        "kind": "native_UQ_scientific_parent",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_UNCANCELLED_OFF_CENTRAL_REAL_ZEROS.md",
        "git_blob": "5c6472b64dc70930bba76dea115ea8e745233c8d",
        "sha256_lf": "bf219006f997d75c53e9cdda0c505f6402b8cfde57d3b444ee9d70591df72873",
    },
    {
        "commit": "bcd3ad5ff0c42e7b205663b68a010e2dbde6d941",
        "kind": "native_UQ_scientific_parent",
        "path": "research/l-families/atlas/generalized/cusp_flag_uncancelled_off_central_real_zeros.py",
        "git_blob": "816dbff2bd777bdec0322eb27d60e2064f32c544",
        "sha256_lf": "1c8ebbae726b78067e83285d29a14f8363704758e6cd06bdaa1822aa94f1f416",
    },
    {
        "commit": "bcd3ad5ff0c42e7b205663b68a010e2dbde6d941",
        "kind": "native_UQ_scientific_parent",
        "path": "research/l-families/atlas/generalized/cusp_flag_uncancelled_off_central_real_zeros.json",
        "git_blob": "0c569db7bf4336cc987e1187421747eefb1ecaee",
        "sha256_lf": "cc120e9d2af305db0e26fbb7a3635062b94eb3cf95d34c1f58d8168e41b1acce",
    },
    {
        "commit": "bcd3ad5ff0c42e7b205663b68a010e2dbde6d941",
        "kind": "native_UQ_scientific_parent",
        "path": "research/l-families/atlas/generalized/cusp_flag_uncancelled_off_central_real_zeros.sources.json",
        "git_blob": "42f86fe7bd6a40250ff5fd69f4047c6aea4e17ce",
        "sha256_lf": "c6bb8d62e913c358d6e8c236294e7bd010ce87076faf571752647cd657a3de44",
    },
    {
        "commit": "bcd3ad5ff0c42e7b205663b68a010e2dbde6d941",
        "kind": "native_UQ_scientific_parent",
        "path": "tests/test_cusp_flag_uncancelled_off_central_real_zeros.py",
        "git_blob": "e2697a6bdb4a71bdc4503ba7c35c1539acb3e8fb",
        "sha256_lf": "3aaa629162c869eb5717bb8473102b114867e9d2329e5d8f52546c818a9db665",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "native_CZ_release",
        "path": "research/l-families/atlas/generalized/CUSP_PERIOD_OFF_CENTRAL_REAL_ZEROS.md",
        "git_blob": "0fcafec61b564a1f2db4c15d24c881d99b8ebcd1",
        "sha256_lf": "cb792b56a687922573711027d9d6a43221d468c0d42311251d4b882c2d7f7906",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "native_CZ_release",
        "path": "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.py",
        "git_blob": "40e65f048cf602f937e326b1e1594c08da81c471",
        "sha256_lf": "cc573a19d3e64344bcb217dafb86094470b4af15304f0c647f090eb12d3fd66c",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "native_CZ_release",
        "path": "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.json",
        "git_blob": "ec6698279aed159326220061ccf36d6cd7ae15cd",
        "sha256_lf": "ea44f9b40af18e6657729b6bb2e2b2ffdf9d814c596f77d7b8542b4249406514",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "native_CZ_release",
        "path": "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.sources.json",
        "git_blob": "0d5ec23bab396ccf2d16cff89247805b935706e3",
        "sha256_lf": "35490b7422b93e2623cc492ab8fc3689f6aa969d9daec2d2caaf5c49e4887721",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "native_CZ_release",
        "path": "tests/test_cusp_period_off_central_real_zeros.py",
        "git_blob": "4f047bf05250ea6e70f93ae06ab26903b019b2ff",
        "sha256_lf": "f256d73577dc6babd3fa652f1f69738e72d26d23edc219ae8eb103d639c920ff",
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


def bigint(value):
    require(
        type(value) is int and abs(value).bit_length() <= BITS, "strict integer bit cap"
    )
    return value


def convolution(left, right, order, work):
    order = integer(order, 0, MAX_Q)
    for row in (left, right):
        require(
            type(row) in (list, tuple) and len(row) == order + 1, "polynomial shape cap"
        )
        for value in row:
            bigint(value)
    work = checked_work(work)
    work.spend((order + 1) ** 2)
    out = [0] * (order + 1)
    for i in range(order + 1):
        for j in range(order + 1 - i):
            out[i + j] = bigint(out[i + j] + left[i] * right[j])
    return out


def unit_power(row, exponent, order, work):
    order = integer(order, 0, MAX_Q)
    exponent = integer(exponent, 0, MAX_K)
    require(type(row) in (list, tuple) and len(row) == order + 1, "unit series shape")
    for value in row:
        bigint(value)
    require(row[0] == 1, "unit series constant")
    work = checked_work(work)
    work.spend(order + 1)
    tail = [0, *row[1:]]
    answer = [1] + [0] * order
    power = answer[:]
    for j in range(1, min(exponent, order) + 1):
        power = convolution(power, tail, order, work)
        work.spend(order + 1)
        coefficient = math.comb(exponent, j)
        answer = [
            bigint(a + coefficient * b) for a, b in zip(answer, power, strict=True)
        ]
    return answer


def native_prefix(k, j, order, work):
    k = integer(k, 24, MAX_K)
    require(k % 12 == 0, "actual weight12d")
    j = integer(j, 1, 2)
    order = integer(order, j + 1, MAX_Q)
    work = checked_work(work)
    work.spend((order + 1) ** 2)
    e4 = [1] + [
        240 * sum(divisor**3 for divisor in range(1, n + 1) if n % divisor == 0)
        for n in range(1, order + 1)
    ]
    delta = [1] + [0] * order
    for n in range(1, order + 1):
        work.spend(min(24 * j, order // n) + 1)
        factor = [0] * (order + 1)
        for a in range(min(24 * j, order // n) + 1):
            factor[a * n] = (-1) ** a * math.comb(24 * j, a)
        delta = convolution(delta, factor, order, work)
    exponent = k // 4 - 3 * j
    out = convolution(delta, unit_power(e4, exponent, order, work), order, work)
    prefix = [0] * j + out[: order + 1 - j]
    require(
        prefix[j] == 1 and all(v == 0 for v in prefix[:j]), "literal q leading order"
    )
    return {
        "weight": k,
        "dimension": k // 12,
        "delta_power": j,
        "E4_power": exponent,
        "q_order": order,
        "q_prefix": prefix,
        "is_in_W": j >= 2,
        "period_or_special_function_sample": False,
    }


def lambda_constants():
    require(Q(1, 4) ** -1 + Q(1, 2) < 5, "Gamma lower-u envelope")
    require(Q(1, 4) ** -2 + 1 == 17, "Gamma derivative envelope; Euler tail strict")
    require(Q(1, 2) * (17 + 2 * 5) < 14, "F derivative lower-u")
    require(Q(3, 4) ** -1 + Q(1, 2) < 2, "Gamma upper-u envelope")
    require(Q(3, 4) ** -2 + 1 < 3, "Gamma derivative upper-u envelope")
    require(Q(1, 2) * (3 + 2 * 2) < 4, "F derivative upper-u")
    require(4 * 3 + 2 * 6 == 24 and 14 + 5 == 19, "Lambda constants")
    return {
        "lower_u_interval": ["1/2", "1"],
        "lower_Gamma_argument_interval": ["1/4", "1/2"],
        "lower_Gamma_upper": 5,
        "lower_abs_Gamma_prime_upper": 17,
        "lower_abs_F_prime_upper": 14,
        "Euler_H_interval": ["0", "1"],
        "D_Laurent_error_upper": 19,
        "upper_u_interval": ["3/2", "2"],
        "upper_Gamma_argument_interval": ["3/4", "1"],
        "upper_Gamma_upper": 2,
        "upper_abs_Gamma_prime_upper": 3,
        "upper_abs_F_prime_upper": 4,
        "zeta_upper": 3,
        "abs_zeta_prime_upper": 6,
        "abs_Lambda_prime_upper": 24,
        "C_error_coefficient_times_epsilon": 48,
        "analytic_integrals_machine_evaluated": False,
    }


def onset_certificate(k):
    k = integer(k, K, MAX_K)
    work = {
        "weight_control": k,
        "is_admissible_weight12d": k % 12 == 0,
        "log_K_upper": 16,
        "uniform_96logk_over_k_upper": str(Q(96 * 16, K)),
        "comparison_power2_exponent_upper": 26 - 4 * k,
        "modular_error_u_upper": str(Q(289, k**5)),
        "epsilon_logk_upper": str(Q(18 * 16, K)),
        "M_over_A_lower": "499/500",
        "M_over_A_upper": "1003/1000",
        "moment_ratio_factor_lower": str(Q(998, 1003)),
        "Gamma_Jensen_product_lower": str(Q(99, 100) * Q(999, 1000) * Q(199, 200)),
        "first_moment_factor_lower": "49/50",
        "epsilon_moment_upper": "101/100",
        "C_relative_lower": "19/20",
        "all_W_upper": str(-Q(k, 144) + 60),
        "witness_lower": str(Q(773 * k, 72000) - Q(2019, 100)),
        "special_function_or_period_evaluated": False,
    }
    require(
        Q(work["uniform_96logk_over_k_upper"]) < Q(1, 32), "all-k logarithm envelope"
    )
    require(work["comparison_power2_exponent_upper"] <= -10, "low mass exponent budget")
    require(Q(1, 2**10) < Q(1, 1000), "low mass rational boundary")
    require(Q(work["modular_error_u_upper"]) < Q(1, 1000), "modular error boundary")
    require(Q(work["epsilon_logk_upper"]) < Q(1, 200), "Jensen exponential budget")
    require(Q(998, 1003) > Q(99, 100), "mass ratio factor")
    require(Q(work["Gamma_Jensen_product_lower"]) > Q(49, 50), "Gamma Jensen lower")
    require(Q(200, 199) < Q(101, 100), "concavity upper")
    require(Q(864, k) < Q(1, 40), "C error below pi/120 from pi>3")
    require(
        Q(work["all_W_upper"]) < 0 < Q(work["witness_lower"]),
        "effective opposite signs",
    )
    require(
        Q(19, 20) * Q(49, 50) / 24 - Q(101, 100) / 36 == Q(773, 72000),
        "native positive coefficient",
    )
    require(19 * Q(101, 100) + 1 == Q(2019, 100), "native bounded error")
    return work


def induction_certificate():
    require(3**16 < 2**26, "fixed power envelope")
    require(K == 2**16, "fixed effective threshold")
    require(2 * 4**2 - 5**2 > 0 and 4**2 == 2**4, "integer induction start")
    return {
        "ratio_gap_coefficients_ascending": [-1, -2, 1],
        "gap_at3": 2,
        "forward_difference_coefficients_ascending": [-1, 2],
        "difference_at3": 5,
        "k2_le_2k_base": 4,
        "logk_over_k_decreasing_for_k_ge_K_by_written_derivative": True,
        "low_mass_all_integer_proof_not_sampling": True,
        "witness_affine_slope": "773/72000",
        "denominator_affine_slope": "-1/144",
        "threshold_K": K,
        "first_admissible_weight": 12 * ((K + 11) // 12),
        "explicit_6144_onset_inherited": False,
    }


def scale_ledger(c):
    c = rational(c)
    require(0 < c < 24, "compact-c chamber")
    return {
        "c": str(c),
        "leading_k_coefficient": str(rational(Q(1, 24) - 1 / (2 * c))),
        "log_k_over_4pi_coefficient": str(rational(-c / 24 - Q(1, 2))),
        "B0_coefficient": "1",
        "constant_rational": "-1/24",
        "Lambda_prime2_over_pi_coefficient": str(rational(-c / 2)),
        "leading_c_derivative": str(rational(1 / (2 * c**2))),
        "special_functions_symbolic": True,
        "uniform_as_c_approaches0_or24": False,
    }


def location_ledger():
    row = scale_ledger(12)
    slope = Q(row["leading_c_derivative"])
    inverse = 1 / slope
    require(
        row["leading_k_coefficient"] == "0" and inverse == 288, "simple leading zero"
    )
    return {
        "first_scale": 12,
        "inverse_leading_slope": str(inverse),
        "log_k_over_4pi_shift": str(-Q(row["log_k_over_4pi_coefficient"]) / slope),
        "B0_shift": str(-inverse),
        "rational_shift": str(-Q(row["constant_rational"]) / slope),
        "Lambda_prime2_over_pi_shift": str(
            -Q(row["Lambda_prime2_over_pi_coefficient"]) / slope
        ),
        "epsilon_error": "O(log^2(k)/k^3)",
        "effective_asymptotic_error_or_onset": False,
        "uniqueness_or_simplicity": False,
    }


def decoupling_order(order):
    order = integer(order, 0, MAX_ORDER)
    cutoff = (order + 3) // 6 + 1
    power = 3 - 6 * cutoff
    require(power < -order, "fixed-A arbitrary algebraic order")
    return {
        "requested_fixed_order": order,
        "chosen_fixed_integer_A": cutoff,
        "cross_upper_power_from_pi_gt3": power,
        "A_depends_on_k": False,
        "complex_ratio_not_modulus_only": True,
        "dimension_factor": 0,
        "analytic_limit_machine_certified": False,
    }


def native_controls(sources, work):
    path = "research/l-families/atlas/generalized/cusp_flag_uncancelled_off_central_real_zeros.json"
    ancestor = parse_json(sources[path])
    overlap = []
    for oldrow in ancestor["native_modular_prefixes"]:
        row = native_prefix(12 * oldrow["dimension"], oldrow["delta_power"], 8, work)
        require(
            row["q_prefix"] == oldrow["q_prefix"], "frozen native q-prefix agreement"
        )
        overlap.append(row)
    threshold_rows = [
        native_prefix(k, j, 8, work)
        for k in (65544, 65556, 98304, 1048572)
        for j in (1, 2)
    ]
    return overlap, threshold_rows


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
        "schema": "cusp-flag-effective-endpoint-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": [
            {
                "url": "https://dlmf.nist.gov/25.11.E5",
                "role": "positive-real Euler fractional-part formula",
                "remote_bytes_authenticated": False,
            },
            {
                "url": "https://dlmf.nist.gov/5.9.E19",
                "role": "Gamma integral and derivative",
                "remote_bytes_authenticated": False,
            },
            {
                "url": "https://dlmf.nist.gov/5.11.E2",
                "role": "positive-real digamma over shrinking intervals",
                "remote_bytes_authenticated": False,
            },
        ],
        "primitive_contract": {
            "object": "actual canonical CF quotient and h_d=Delta E4^(3d-3)",
            "completion": "unchanged half-lattice E*, residue1/2, cosine4sqrt(y)",
            "effective_threshold": "all k=12d>=65536, first65544; sufficient not optimal",
            "uniform_space": "all W=ker[q], original Petersson norm, no dimension loss",
            "new_cross_input": "complex h/q-1 product telescoping and exact high-cusp q orthogonality",
            "asymptotic_scope": "c in fixed compact subset(0,24); no effective error onset",
            "location": "12/k+(288logk+O(1))/k^2; no uniqueness or simplicity",
            "execution": "no ancestor code executed; frozen prefix data compared exactly",
        },
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
    work = Budget()
    overlap, threshold_rows = native_controls(sources, work)
    return seal(
        {
            "schema": "cusp-flag-effective-endpoint-separation-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; special functions symbolic",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "Lambda_envelope_constants": lambda_constants(),
            "all_integer_induction": induction_certificate(),
            "effective_onset_controls": [
                onset_certificate(k) for k in (K, 65544, 65556, 98304, MAX_K)
            ],
            "uniform_scale_ledgers": [
                scale_ledger(c)
                for c in (Q(6), Q(23, 2), Q(12), Q(25, 2), Q(18), Q(47, 2))
            ],
            "location_ledger": location_ledger(),
            "arbitrary_fixed_order_ledgers": [
                decoupling_order(m) for m in range(MAX_ORDER + 1)
            ],
            "frozen_overlap_q_prefixes": overlap,
            "effective_weight_q_prefixes": threshold_rows,
            "coverage": {
                "overlap_q_prefixes": len(overlap),
                "effective_weight_q_prefixes": len(threshold_rows),
                "fixed_order_models": MAX_ORDER + 1,
                "charged_work": work.used,
            },
            "caps": {
                "control_weight": MAX_K,
                "q_order": MAX_Q,
                "fixed_order": MAX_ORDER,
                "work": MAX_WORK,
                "bits": BITS,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_JSON_NODES,
            },
            "scope": {
                "actual_uncancelled_pair_effective": True,
                "all_W_bound_not_basis_only": True,
                "threshold_K": K,
                "first_admissible_weight": 65544,
                "optimal_onset": False,
                "6144_inherited": False,
                "Schur_cross_uniform_all_W": True,
                "complex_modular_ratio_proved": True,
                "constant12_and_logshift288": True,
                "asymptotic_error_onset_effective": False,
                "uniqueness_or_simplicity": False,
                "endpoint_escaping_c_sequences_excluded": False,
                "actual_period_zero_Gamma_zeta_Bessel_samples": 0,
                "analytic_limits_integrals_machine_certified": False,
                "global_zero_census_or_RH": False,
                "new_automorphic_family_or_exhaustive_novelty": False,
                "parent_files_modified": False,
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
            "PASS_CUSP_EFFECTIVE_ENDPOINT; analytic proof requires independent review"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
