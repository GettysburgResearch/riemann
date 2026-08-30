"""Exact source-bound certificate for a negative weight-24 derivative."""

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "cusp_flag_effective_negative_derivative"
BASE = "282ce03941444d0e02daba5fde260ccb54a3f909"
NOTE = HERE / "CUSP_FLAG_EFFECTIVE_NEGATIVE_DERIVATIVE.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
MAX_Q, MAX_CUTOFF, MAX_ORDER = 64, 12, 8192
MAX_TERMS, MAX_DEPTH, MAX_SUPPORT = 64, 2, 64
INPUT_BITS, INTERNAL_BITS = 32, 8192
MAX_BYTES, MAX_WORK = 1048576, 1000000
LOG_BITS, MASS_BITS, W0 = 40, 160, 96
STAR, ATOM = Q(9, 2), -88203653222400
BINDINGS = [
    {
        "id": "positive_spectrum",
        "commit": "282ce03941444d0e02daba5fde260ccb54a3f909",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md",
        "kind": "scientific_source",
        "git_blob": "d241501272a32771717494dd4c59aa17a6888e98",
        "sha256_lf": "62925bbe9ebe327ed491f99e886eea5599253295c69f05878d278dd453abe0d7",
    },
    {
        "id": "weight24",
        "commit": "b62dfc6348661992bca659c99de226a1b6b22e14",
        "path": "research/l-families/atlas/generalized/RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md",
        "kind": "scientific_source",
        "git_blob": "4a3f9f0b6644bffdc94214e6fb2b60dfafdd93ca",
        "sha256_lf": "1828196e08782ce692f28e3fdec2feae55c6d24e9b3eb5c35ff1c315434aee75",
    },
    {
        "id": "weight24_coefficients",
        "commit": "b62dfc6348661992bca659c99de226a1b6b22e14",
        "path": "research/l-families/atlas/generalized/rankin_selberg_quotient_global_parent.json",
        "kind": "coefficient_fixture",
        "git_blob": "f44fe4d65225601e04d86c58e6d6d296c51126c7",
        "sha256_lf": "ff9c5e7cc43db1d9c63f317cd842e4337066ec30c30a2f8be6f45958648ce856",
    },
    {
        "id": "weight24_review",
        "commit": "8e9f05211954e0a7aae5e63c9367f1d520d3671d",
        "path": "research/l-families/atlas/generalized/RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT_AUDIT.md",
        "kind": "review_context",
        "git_blob": "383cf031153ef080fd1e8631b9d1788a0d0dc3b6",
        "sha256_lf": "f48587c5300d3c27835a49be36b700e4f574546da9521e8b8c5348d8a85d247f",
    },
]
EXTERNAL_URL = "https://people.mpim-bonn.mpg.de/zagier/files-restricted/doi/10.1007/978-3-540-74119-0/fulltext.pdf"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    require(type(value) is int and low <= value <= high, "strict integer/domain cap")
    return value


def rational(value, *, internal=False):
    require(type(internal) is bool, "strict internal flag")
    require(type(value) in (int, Q), "strict rational")
    value = Q(value)
    limit = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= limit,
        "rational bit cap",
    )
    return value


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, count):
        count = integer(count, 0, MAX_WORK)
        require(self.used + count <= self.limit, "work cap before expansion")
        self.used += count


def budget(value):
    require(type(value) is Budget, "Budget required")
    return value


def polynomial(value, order):
    order = integer(order, 1, MAX_Q)
    require(type(value) is tuple and len(value) == order + 1, "polynomial shape")
    require(
        all(type(x) is int and abs(x).bit_length() <= 512 for x in value),
        "integer coefficient cap",
    )
    return value


def qmul(left, right, order, work):
    left, right = polynomial(left, order), polynomial(right, order)
    budget(work).spend((order + 1) * (order + 2) // 2)
    result = tuple(
        sum(left[j] * right[n - j] for j in range(n + 1)) for n in range(order + 1)
    )
    return polynomial(result, order)


def q_source(order=MAX_Q, work=None):
    order = integer(order, 12, MAX_Q)
    work = Budget() if work is None else budget(work)
    work.spend(2 * order * order)
    e4 = (1,) + tuple(
        240 * sum(d**3 for d in range(1, n + 1) if n % d == 0)
        for n in range(1, order + 1)
    )
    e6 = (1,) + tuple(
        -504 * sum(d**5 for d in range(1, n + 1) if n % d == 0)
        for n in range(1, order + 1)
    )
    cube = qmul(qmul(e4, e4, order, work), e4, order, work)
    square = qmul(e6, e6, order, work)
    require(
        all((a - b) % 1728 == 0 for a, b in zip(cube, square)), "Delta divisibility"
    )
    delta = tuple((a - b) // 1728 for a, b in zip(cube, square))
    b = qmul(delta, delta, order, work)
    a = qmul(delta, cube, order, work)
    g = tuple(x - 696 * y for x, y in zip(a, b))
    require(
        (g[1], g[2], g[3], b[1], b[2], b[3]) == (1, 0, 195660, 0, 1, -48),
        "fixed native source",
    )
    for n in range(1, order + 1):
        require(
            abs(b[n]) <= 2**84 * n**23 and abs(g[n]) <= 2**95 * n**23,
            "finite coefficient majorants",
        )
    return {"delta": delta, "E4": e4, "E6": e6, "a": a, "b": b, "g": g}


def frequency_prefix(g, b, cutoff=Q(12), work=None):
    cutoff = rational(cutoff)
    require(STAR <= cutoff <= MAX_CUTOFF, "frequency cutoff")
    require(type(g) is tuple and type(b) is tuple and len(g) == len(b), "source shape")
    order = integer(len(g) - 1, 12, MAX_Q)
    g, b = polynomial(g, order), polynomial(b, order)
    work = Budget() if work is None else budget(work)
    endpoint_cap = int(2 * cutoff / 3)
    internal_cap = int(4 * cutoff / 9)
    depth = 0
    while STAR * Q(3, 2) ** (depth + 1) <= cutoff:
        depth += 1
    require(depth <= MAX_DEPTH, "geometric depth cap")
    require(max(int(cutoff), endpoint_cap, internal_cap) <= order, "q-tail coverage")
    candidates = (endpoint_cap - 2) ** 2 * sum(
        (internal_cap - 2) ** h for h in range(depth + 1)
    )
    work.spend(candidates * (depth + 3))
    bare = {Q(n): g[n] ** 2 for n in range(1, int(cutoff) + 1)}
    counts = []
    for h in range(depth + 1):
        count = 0
        for n in range(3, endpoint_cap + 1):
            for m in range(3, endpoint_cap + 1):
                for middle in itertools.product(range(3, internal_cap + 1), repeat=h):
                    rho = Q(n * m, 2)
                    coefficient = (-1) ** (h + 1) * g[n] * b[n] * g[m] * b[m]
                    for ell in middle:
                        rho *= Q(ell, 2)
                        coefficient *= b[ell] ** 2
                    if rho <= cutoff:
                        count += 1
                        bare[rho] = bare.get(rho, 0) + coefficient
        counts.append(count)
    bare = {rho: value for rho, value in bare.items() if value}
    uncompleted = {}
    work.spend(len(bare) * math.isqrt(int(cutoff)))
    for d in range(1, math.isqrt(int(cutoff)) + 1):
        for rho, value in bare.items():
            if d * d * rho <= cutoff:
                target = d * d * rho
                uncompleted[target] = uncompleted.get(target, 0) + d**46 * value
    uncompleted = {rho: value for rho, value in uncompleted.items() if value}
    require(len(bare) <= MAX_SUPPORT and len(uncompleted) <= MAX_SUPPORT, "support cap")
    require(bare[STAR] == uncompleted[STAR] == ATOM, "actual negative atom")
    return {
        "F": bare,
        "L": uncompleted,
        "cutoff": cutoff,
        "ordered_word_counts": counts,
        "endpoint_cap": endpoint_cap,
        "internal_cap": internal_cap,
        "max_depth": depth,
        "next_depth_minimum": STAR * Q(3, 2) ** (depth + 1),
        "candidate_words_before_frequency_filter": candidates,
    }


def floor_q(value):
    value = rational(value, internal=True)
    return value.numerator // value.denominator


def ceil_q(value):
    value = rational(value, internal=True)
    return -((-value.numerator) // value.denominator)


def dyadic_upper(value, bits):
    bits = integer(bits, 1, MASS_BITS)
    value = rational(value, internal=True)
    require(value >= 0, "nonnegative majorant")
    return Q(ceil_q(value * 2**bits), 2**bits)


def log_interval(value, terms=MAX_TERMS, bits=LOG_BITS, work=None):
    value = rational(value)
    require(1 <= value <= MAX_CUTOFF, "log argument domain")
    terms = integer(terms, 1, MAX_TERMS)
    bits = integer(bits, 1, LOG_BITS)
    work = Budget() if work is None else budget(work)
    work.spend(6 * terms + 10)
    u = (value - 1) / (value + 1)
    partial, power = Q(0), u
    for j in range(terms):
        partial = rational(partial + 2 * power / (2 * j + 1), internal=True)
        power = rational(power * u * u, internal=True)
    remainder = rational(2 * power / ((2 * terms + 1) * (1 - u * u)), internal=True)
    scale = 2**bits
    return (
        Q(floor_q(partial * scale), scale),
        Q(ceil_q((partial + remainder) * scale), scale),
    )


def kernel_gap(rho, order=MAX_ORDER, work=None):
    rho = rational(rho)
    order = integer(order, 1, MAX_ORDER)
    require(1 < rho <= MAX_CUTOFF and rho != STAR, "nonconstant nontarget frequency")
    work = Budget() if work is None else budget(work)
    lo, hi = log_interval(rho, work=work)
    star_lo, star_hi = log_interval(STAR, work=work)
    require(star_lo > 0, "positive target logarithm")
    lower, upper = lo / star_hi, hi / star_lo
    require(upper < 1 or lower > 1, "unresolved logarithmic separation")
    delta = 1 - upper if upper < 1 else lower - 1
    loss = rational(delta * delta / (2 * max(1, upper)), internal=True)
    exponent = floor_q(order * loss / Q(7, 10))
    integer(exponent, 0, 4 * MAX_ORDER)
    return {
        "frequency": rho,
        "log_interval": (lo, hi),
        "ratio_interval": (lower, upper),
        "log_kernel_loss_lower": loss,
        "power_two_exponent": exponent,
    }


def mass_certificate(g, b, work=None):
    g, b = polynomial(g, MAX_Q), polynomial(b, MAX_Q)
    work = Budget() if work is None else budget(work)
    work.spend(6 * MAX_Q + 32)
    require(2160 <= 2**12 and 75600 <= 2**17, "Eisenstein majorant constants")
    require(2**36 + 2**34 <= 1728 * 2**26, "Delta majorant constant")
    require(2**62 + 696 * 2**52 <= 2**63 and 24 <= 2**32, "g and binomial constants")
    exponents = {"B_nonconstant": 190, "C_absolute": 179, "U_absolute": 264}
    coarse = {
        "B_nonconstant": Q(1, 2**100),
        "C_absolute": Q(1, 2**110),
        "U_absolute": Q(1, 2**30),
    }
    rows = {}
    for name, exponent in exponents.items():
        total = Q(0)
        for n in range(2, MAX_Q + 1):
            numerator = {
                "B_nonconstant": g[n] ** 2,
                "C_absolute": abs(g[n] * b[n]),
                "U_absolute": b[n] ** 2 * 2**W0 if n >= 3 else 0,
            }[name]
            total += dyadic_upper(Q(numerator, n**W0), MASS_BITS)
        tail = Q(2**exponent, 49 * 64**49)
        total += dyadic_upper(tail, MASS_BITS)
        require(total < coarse[name], "certified infinite mass majorant")
        rows[name] = {
            "prefix_dyadic_upper": total - dyadic_upper(tail, MASS_BITS),
            "tail_rational_upper": tail,
            "total_dyadic_upper": total,
            "strict_coarse_upper": coarse[name],
        }
    f_mass = (
        1
        + coarse["B_nonconstant"]
        + 2**W0 * coarse["C_absolute"] ** 2 / (1 - coarse["U_absolute"])
    )
    zeta_mass = 1 + Q(1, 145)
    require(
        coarse["U_absolute"] < 1 and f_mass < 2 and f_mass * zeta_mass < 4,
        "absolute F/L mass",
    )
    return {
        "abscissa": W0,
        "q_prefix": MAX_Q,
        "rows": rows,
        "F_absolute_mass_upper": 2,
        "zeta_146_upper": zeta_mass,
        "L_absolute_mass_upper": 4,
    }


def derivative_certificate(prefix, mass, order=MAX_ORDER, work=None):
    order = integer(order, 1, MAX_ORDER)
    require(type(prefix) is dict and set(prefix) == {"F", "L"}, "two fixed source maps")
    require(type(mass) is dict, "mass certificate container")
    for name, bound in (("F", 2), ("L", 4)):
        require(
            type(prefix[name]) is dict and len(prefix[name]) <= MAX_SUPPORT,
            "source map cap before expansion",
        )
        for rho, coefficient in prefix[name].items():
            require(type(rho) is Q and 1 <= rho <= MAX_CUTOFF, "source frequency type")
            rational(rho)
            require(
                type(coefficient) is int and abs(coefficient).bit_length() <= 512,
                "source coefficient type/bit cap",
            )
        value = mass.get(name + "_absolute_mass_upper")
        require(type(value) is int and value == bound, "fixed certified mass bound")
        require(prefix[name].get(STAR) == ATOM, "source target identity")
    work = Budget() if work is None else budget(work)
    require(log_interval(Q(2), work=work)[1] < Q(7, 10), "log 2 upper certificate")
    gaps = {
        rho: kernel_gap(rho, order, work)
        for rho in set(prefix["F"]) | set(prefix["L"])
        if rho not in (1, STAR)
    }
    results = {}
    tail_gap = kernel_gap(Q(12), order, work)
    for name in ("F", "L"):
        require(
            type(prefix[name]) is dict and prefix[name].get(STAR) == ATOM,
            "source target identity",
        )
        require(len(prefix[name]) <= MAX_SUPPORT, "source map cap")
        terms = []
        for rho, coefficient in sorted(prefix[name].items()):
            require(
                type(rho) is Q and 1 <= rho <= 12 and type(coefficient) is int,
                "source frequency/coefficient types",
            )
            if rho in (1, STAR):
                continue
            exponent = gaps[rho]["power_two_exponent"]
            bound = rational(
                abs(coefficient) * (STAR / rho) ** W0 / 2**exponent, internal=True
            )
            terms.append(
                {
                    "frequency": rho,
                    "coefficient": coefficient,
                    "power_two_exponent": exponent,
                    "normalized_error_integer_upper": ceil_q(bound),
                }
            )
        tail = rational(
            mass[name + "_absolute_mass_upper"]
            * STAR**W0
            / 2 ** tail_gap["power_two_exponent"],
            internal=True,
        )
        tail_integer = ceil_q(tail)
        error = (
            sum(row["normalized_error_integer_upper"] for row in terms) + tail_integer
        )
        require(error < -ATOM // 2, "negative derivative not certified at this order")
        results[name] = {
            "prefix_terms": terms,
            "omitted_frequency_strictly_greater_than": 12,
            "tail_integer_upper": tail_integer,
            "normalized_error_integer_upper": error,
            "normalized_derivative_upper": ATOM + error,
            "negative": True,
        }
    return {
        "order": order,
        "w0": W0,
        "w_exact": "96+8192/log(9/2)"
        if order == MAX_ORDER
        else str(W0) + "+" + str(order) + "/log(9/2)",
        "star_log_interval": log_interval(STAR, work=work),
        "normalizer": "(log(9/2))^m*(9/2)^(-w_m)",
        "log_two_upper": Q(7, 10),
        "gaps": [gaps[rho] for rho in sorted(gaps)],
        "tail_gap": tail_gap,
        "functions": results,
    }


def json_types(value, depth=0):
    require(depth <= 16, "JSON depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "JSON type")
    if type(value) is dict:
        require(
            len(value) <= 256 and all(type(k) is str and len(k) <= 2048 for k in value),
            "JSON key/object cap",
        )
        for child in value.values():
            json_types(child, depth + 1)
    elif type(value) is list:
        require(len(value) <= 2048, "JSON list cap")
        for child in value:
            json_types(child, depth + 1)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= INTERNAL_BITS, "JSON integer cap")


def encode(value):
    if type(value) is Q:
        return str(value)
    if type(value) is tuple:
        return [encode(x) for x in value]
    if type(value) is list:
        return [encode(x) for x in value]
    if type(value) is dict:
        return {str(key): encode(child) for key, child in value.items()}
    return value


def render(value):
    json_types(value)
    return json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n"


def parse_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def pairs(values):
        out = {}
        for key, value in values:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def nonfinite(value):
        raise ValueError("nonfinite JSON: " + value)

    try:
        value = json.loads(
            raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=nonfinite
        )
        json_types(value)
        return value
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def lf_sha(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "artifact byte cap")
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def expected_manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": BINDINGS,
        "primitive_contract": {
            "source": "g=Delta*E4^3-696*Delta^2, b=Delta^2, standard q=exp(2*pi*i*z)",
            "variable": "w=s+23; derivatives are d/dw before evaluation",
            "F": "B(w)-2^w*C(w)^2/(1+U(w))",
            "L": "zeta(2w-46)*F(w)",
            "negative_atom": "-88203653222400 at 9/2",
            "method": "complete rho<=12 prefix plus every omitted word, exact rational log bounds",
        },
        "external_context": {
            "url": EXTERNAL_URL,
            "role": "Zagier sections2.2/2.4, Proposition5 and equation23: Eisenstein coefficients and Delta identity",
            "remote_bytes_authenticated": False,
        },
    }


def authenticate(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        render(manifest) == render(expected_manifest()),
        "complete typed manifest identity",
    )
    parent = None
    for row in BINDINGS:
        ref = row["commit"] + ":" + row["path"]
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", ref], cwd=ROOT, timeout=10
            )
        )
        require(0 <= size <= MAX_BYTES, "source byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=10)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and lf_sha(raw) == row["sha256_lf"],
            "frozen Git blob/LF source identity",
        )
        if row["kind"] == "coefficient_fixture":
            parent = parse_json(raw)
    require(
        parent is not None
        and parent["schema"] == "rankin-selberg-quotient-global-parent-v1",
        "parent coefficient schema",
    )
    return parent


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload, "unsealed payload"
    )
    raw = render(payload).encode()
    require(len(raw) <= MAX_BYTES, "report byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(raw).hexdigest()}


def build_report():
    parent = authenticate()
    work = Budget()
    source = q_source(work=work)
    require(
        parent["source_q_rows"]
        == [[n, source["a"][n], source["b"][n], source["g"][n]] for n in range(1, 25)],
        "all frozen q rows",
    )
    prefix = frequency_prefix(source["g"], source["b"], work=work)
    row = parent["frequency_controls"][-1]
    require(row["cutoff"] == "12", "parent exact cutoff")
    require(
        {str(k): str(v) for k, v in prefix["F"].items()} == row["bare_F"],
        "full parent F prefix",
    )
    require(
        {str(k): str(v) for k, v in prefix["L"].items()} == row["L_Q_zeta_times_F"],
        "full parent L prefix",
    )
    mass = mass_certificate(source["g"], source["b"], work=work)
    cert = derivative_certificate(
        {name: prefix[name] for name in ("F", "L")}, mass, work=work
    )
    artifacts = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "current artifact cap")
        artifacts[path.relative_to(ROOT).as_posix()] = lf_sha(path.read_bytes())
    payload = encode(
        {
            "schema": STEM + "-v1",
            "status": "PROPOSED_EXACT_CERTIFICATE_REQUIRING_INDEPENDENT_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integer/Fraction arithmetic; analytic logarithms enclosed by rational series then outward dyadic rounding; no floats",
            "source_bindings": BINDINGS,
            "artifact_sha256_lf": artifacts,
            "caps": {
                "q_order": MAX_Q,
                "cutoff": MAX_CUTOFF,
                "order": MAX_ORDER,
                "log_terms": MAX_TERMS,
                "log_bits": LOG_BITS,
                "mass_bits": MASS_BITS,
                "input_bits": INPUT_BITS,
                "internal_bits": INTERNAL_BITS,
                "bytes": MAX_BYTES,
                "work_units": MAX_WORK,
            },
            "coverage": {
                "q_rows": MAX_Q,
                "F_atoms": len(prefix["F"]),
                "L_atoms": len(prefix["L"]),
                "work_units": work.used,
            },
            "q_rows": [
                [n, source["delta"][n], source["g"][n], source["b"][n]]
                for n in range(1, MAX_Q + 1)
            ],
            "frequency_prefix": prefix,
            "absolute_mass": mass,
            "derivative_certificate": cert,
            "scope": {
                "actual_weight24_F_and_L": True,
                "all_omitted_words_bounded": True,
                "exact_derivative_value_sampled": False,
                "negative_second_derivative_claimed": False,
                "completed_Q_claim": False,
                "uniform_in_weight": False,
                "minimal_derivative_order_claimed": False,
                "RH_GRH_or_novelty_claim": False,
                "analytic_proof_machine_verified": False,
            },
        }
    )
    return seal(payload)


def validate_report(value, expected=None):
    require(type(value) is dict and "payload_sha256" in value, "sealed report required")
    payload = {key: child for key, child in value.items() if key != "payload_sha256"}
    require(render(value) == render(seal(payload)), "payload seal")
    expected = build_report() if expected is None else expected
    require(
        render(value) == render(expected), "complete typed certificate reconstruction"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--emit-report", action="store_true")
    modes.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(render(expected_manifest()), end="")
    elif args.emit_report:
        print(render(build_report()), end="")
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS: actual weight24 F and L have certified negative order8192 derivative"
        )


if __name__ == "__main__":
    main()
