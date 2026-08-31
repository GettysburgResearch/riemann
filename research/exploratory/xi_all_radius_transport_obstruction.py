"""Post-QT all-radius sufficient-criterion obstruction; critical roots inherited."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

import xi_fixed_lambda_heldout_alignment as ha
from flint import acb, arb, ctx

oa = ha.oa
ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
D = "research/exploratory/"
STEM = "xi_all_radius_transport_obstruction"
BASE = "530732c5fd7f50364381f8af50e97ce809b674c5"
DESIGN = "800b5e212f61a4df9a640788d294b0bbbf37862b"
NOTE = HERE / (STEM.upper() + ".md")
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BINDINGS = [
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "git_blob": "cb634e9ac1e5ddbdffad01286a0b37ca958ac92b",
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "sha256_lf": "b9e7cf4911688d81c44ec9d871104e063c7bf46f574d86b479c6d912559d7269",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "git_blob": "a5e48dea3a25e1ff7419b2f6e2cfeef3de230185",
        "path": "research/exploratory/xi_quadratic_critical_transport.py",
        "sha256_lf": "28033a330ade30e0079f6e24cd0f4b07e9de9ba70438f92c88fe5c0f7fe8c373",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "git_blob": "322281110f34af24575be29aed32acfd25657959",
        "path": "research/exploratory/xi_quadratic_critical_transport.json",
        "sha256_lf": "45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "git_blob": "58bd03b1d15ce4d2eb91addb4c209a0f43fab80c",
        "path": "research/exploratory/xi_quadratic_critical_transport.sources.json",
        "sha256_lf": "66aa6f3d483bc638eed43315592c3cc5f3f8ef2baa9d9518e2fa0de3e685d757",
    },
    {
        "commit": "530732c5fd7f50364381f8af50e97ce809b674c5",
        "git_blob": "cde20699d7b3894bf40db419b2d90a3d93459751",
        "path": "tests/test_xi_quadratic_critical_transport.py",
        "sha256_lf": "d5493e8c31d53d66fdb00f35dfa1198b173513e23b2bfd3bdcb2d39d80423749",
    },
    {
        "commit": "800b5e212f61a4df9a640788d294b0bbbf37862b",
        "git_blob": "e650833c358584df63f93ccb46bdaf848b992053",
        "path": "research/exploratory/XI_ALL_RADIUS_TRANSPORT_OBSTRUCTION.md",
        "sha256_lf": "d25179cdb529e8641ff0dc35bd36ea8e83cc7d38392f4b5fcf51bb2eb143735f",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "git_blob": "3e9a15404532e72255acb3e55751987eb29a4043",
        "path": "research/exploratory/XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md",
        "sha256_lf": "592c8313e5e46c68af6e5b3b9aa46c2724e84f51394cac3bd6934d0139eb26b7",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "git_blob": "b472d18a3404ceebbde76e02bd6346678f4bdcfa",
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.py",
        "sha256_lf": "1ad06f941f1c24f4732ef4db772c915f8bdf080abbdf2b8754816ea70fff01f0",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "git_blob": "e5f1bc4e97be9b92f715e24b3670d64171071334",
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.json",
        "sha256_lf": "eb6464cc2eed61f8aecf2eff6e2f36a5ee5f850252237f0f95bd9b0e4e51b206",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "git_blob": "0dac7784b5c2a912d44c479e069e045b9f1b85e1",
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.sources.json",
        "sha256_lf": "3bb7fdccc56b8e7ac2e3c6fb1c0a62874645893683e8d626f4cdca8becdf9ad6",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "git_blob": "c244417d71e8f31d59d3bbafb29543643bbb8c06",
        "path": "tests/test_xi_fixed_lambda_heldout_alignment.py",
        "sha256_lf": "8ece2393f6039ae3ea42b137cd079ef727a0db932de440f9a641020c9a0b0392",
    },
    {
        "commit": "9162b5ea6112c346e200c044f9f3f2324ed4fc59",
        "git_blob": "171f69088e6d4becd2043cbdf14a3581c364846e",
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "sha256_lf": "66c966140b2c4ec60cf9b4b47f00710dc8caf85b6a38a3cd2a07f0f26be56ccd",
    },
    {
        "commit": "24c52d25f9cf606f5db9c40e4919a78c196b9565",
        "git_blob": "d9bbf53508c079e2558526baaa6a77e86249e71d",
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "sha256_lf": "d6483e2ca82beb4d889842a635fdfd30688e51b06ad7327f222d3164864328ba",
    },
    {
        "commit": "edb7d1ccffdc83c8e2b95e533da078508d009990",
        "git_blob": "679022e3a03c263270aba6ebd61548080ebca71a",
        "path": "research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md",
        "sha256_lf": "768df469cd46943918fba844f392be6f8a762a5a9dd8898007d083b7ecf9ad4a",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "git_blob": "27e4db71377788b6e03b14005035d59c9e930611",
        "path": "research/exploratory/XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
        "sha256_lf": "7f6efdcd6375d14db36ade51c073d3c04dc73f5e2c9c5cd27aa94d8107497460",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "git_blob": "62f94b71810a49646830694cab25bb14c1eab470",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.py",
        "sha256_lf": "69e51a36a9180df97ae6b994104308a46b9ab84331027e1d8ed288c6490d5300",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "git_blob": "d3ef5908f68a7b3025428bf55e8e1fa81970e273",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.json",
        "sha256_lf": "504071292138882ad5192fc62f765edc5615c3140542c7f597651679ba682cdb",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "git_blob": "62eb2fa59113bc87158659e538fb1fea5b7f7ca4",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.sources.json",
        "sha256_lf": "b775a9c8bc054312644116b362960b1c1e950d23a8dfc82d556d86f67a30c819",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "git_blob": "6cdac911a7e62d12273d7eafd2fdef199b282d33",
        "path": "tests/test_xi_fixed_lambda_joint_box_compression.py",
        "sha256_lf": "deb2696c5c160e0da970c31f35e5ed472baabc4fb1d3db831b4e48371935ae80",
    },
    {
        "commit": "24544028cd033ea66a6b64bec254da5ea43230c9",
        "git_blob": "db03a1b0c1f5abc0e27be92c4232968f68f816b8",
        "path": "research/exploratory/XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md",
        "sha256_lf": "714bf76812826957269bb26d10c3a919909ad7af97b0ec9becfb8a4e5f0c79bd",
    },
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "git_blob": "90e6bd89ca9a23c401d6d947c04a9d548f6b3030",
        "path": "research/exploratory/XI_LAPLACE_LOW_PASS_LOWER_BOUND.md",
        "sha256_lf": "c56d29037b85c45398bcb34dc7fb8450ba0e4b0f32fa7293edcaf5d1d2ea4b64",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "git_blob": "2860d9c9bb90f4423f17f0d272229e78a30ae62b",
        "path": "research/exploratory/XI_COMPANION_BOX_COUNT_COMPRESSION.md",
        "sha256_lf": "22d11bf3dccb72fa25633deeee063164611dbaa977c5e66fca84f4350ae79c65",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "git_blob": "698211f63f2268f421faa1ed76d4dd8749a4b311",
        "path": "research/exploratory/xi_companion_box_count_compression.py",
        "sha256_lf": "cea67ec0b5335ecef7a6df8d453859a249b73d1b716b8c87565709d27ec95e58",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "git_blob": "346a452e1c3136f19139debe1620577ef41e6b43",
        "path": "research/exploratory/xi_companion_box_count_compression.json",
        "sha256_lf": "9148321153c7319518dc9475adee61f2ba5b646663f1cb35b762f31f280834e4",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "git_blob": "fcbfb819e09f97f9f4e9af60141ffe198238bf1c",
        "path": "research/exploratory/xi_companion_box_count_compression.sources.json",
        "sha256_lf": "b916af0286ddd686e700b56032a2f10f9b0bc08212bed6ca60bb99270b85299f",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "git_blob": "ea093cc50fb8b9de415ce4e71bc370ffe456d8ed",
        "path": "tests/test_xi_companion_box_count_compression.py",
        "sha256_lf": "e9b40aaa100f1f8ae74ad2d90978b8e7621303ac750a847cbfc8ec045a2e05b5",
    },
    {
        "commit": "e669d257711d8d4a6a0ab7aeb21254fd220f7dc3",
        "git_blob": "a11b631e88343ad0782e2d7db511282eb473a30c",
        "path": "research/exploratory/XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
        "sha256_lf": "d8e1f3cc061fc0671b45ef26e09c83b0e165545e3c56e049cf301221377ebc95",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "625cc29f67510bd58ed667f6f5fec242b84e4a11",
        "path": "research/exploratory/XI_COMPANION_OFF_AXIS_BALL_CERTIFICATES.md",
        "sha256_lf": "020597b67044d996e12e2f76655550557cc33cd52cf717553e2fc6be9d48e396",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "b0cecac35dcdb3a583ae891609d7d89b378b537b",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.py",
        "sha256_lf": "319e9abf775199e1747b0642dd99f24e52d9700bf71c04385d02cf5be9aac15f",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "e7cdd61fcc046d142ccc95b5796d3106a79139c4",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.json",
        "sha256_lf": "268e67f84bdae5d41a4acb95df96fff18e00c3d0ae3430a9be8c89f633ff7c5b",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "06434dc776028d155b8107f8cb5ea8687a3ce9dc",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.sources.json",
        "sha256_lf": "eec3231292d8d5b030c68ffaed9520dd5697657dcd17f15c91e4f34ee8f9be4c",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "git_blob": "f1f323d579968949cf07c662dd245172380759ba",
        "path": "tests/test_xi_companion_off_axis_ball_certificates.py",
        "sha256_lf": "3cfd3a3c2177ccbb242aeb5a9fa7e83b27859f9485a532489304019499b8dcd7",
    },
    {
        "commit": "7aed2ec0b99b9d7f2fb94a774922a83d5b84a870",
        "git_blob": "cd74bd06267eb4d60bc977353d11f6a0fb72ba6a",
        "path": "research/exploratory/COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md",
        "sha256_lf": "b9ab266898129389b94a9ed494b140422fc823552c6b69bf22ed36a9dbb2e7f7",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "git_blob": "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "path": "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "sha256_lf": "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "git_blob": "16ab64a193e59608c9e2c9fd9762addc58809c3f",
        "path": "claims/lemmas/L-106610-riemann-siegel-gauge-factorization.md",
        "sha256_lf": "11c87fd9b50c309249b76f39fd87c3d20953779355a39a0338ef281d3cb57c87",
    },
    {
        "commit": "d38961c15fc76d671cef4fddfc92d3c866af4fd5",
        "git_blob": "9688e30825fcc3d2b13570539bf03299407eae87",
        "path": "research/exploratory/XI_COMPANION_IMAGINARY_AXIS_SAMPLING.md",
        "sha256_lf": "a9d6b51b3b2f1ccb388fb8d74e115023c622115b169d3214f071ef9005034081",
    },
    {
        "commit": "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d",
        "git_blob": "e592a4c031876f56f07d28b7e18a8a7cf6e826f4",
        "path": "research/exploratory/XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md",
        "sha256_lf": "5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d",
    },
    {
        "commit": "d76a1a8eb8ec40b19a351af95439b9a6514bee87",
        "git_blob": "797f7b581580ad5a441c7702015c64a53eca6f4d",
        "path": "research/exploratory/XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md",
        "sha256_lf": "55aa96745c3f269ac464ea7c0b8227e14e7d8ceb33f8bec2fc13f9642b33d44d",
    },
]
CAPS = {
    "nodes": 26,
    "precision_bits": 1024,
    "series_coefficients": 9,
    "rational_endpoint_bits": 4096,
    "source_bytes": 24000000,
    "report_bytes": 2000000,
    "json_nodes": 600000,
    "json_depth": 24,
    "work_units": 10000,
}
CONTRACT = {
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "pinned FLINT outward; exact Fraction comparisons and integer-square-root brackets",
    "panel": "ALL26 frozen QT critical intervals; no new source or calibration",
    "inheritance": "QT real critical-point existence/uniqueness inherited, not reexecuted",
    "fresh": "nine actual Xi coefficients on each full interval at1024bits and one fixed lambda_(64)",
    "quantifier": "ALL admissible radii; analytic maximization proof, not a radius-grid census",
    "threshold_is_exact_supremum": False,
    "target_is_QT_separate_triangle_criterion_only": True,
    "joint_remainder_criterion_ruled_out": False,
    "proof_of_no_companion_root": False,
    "innerness_or_RH_assumed": False,
    "RH_proved": False,
    "cofinal_transport": False,
    "post_QT_result_design": True,
    "caps": CAPS,
}


def need(value, reason):
    if not value:
        raise ValueError(reason)


def lf(data):
    need(type(data) is bytes and len(data) <= CAPS["source_bytes"], "source bytes")
    normalized = data.replace(b"\r\n", b"\n")
    text = normalized.decode("utf-8")
    need(
        all(ord(c) in (9, 10) or ord(c) >= 32 for c in text)
        and not any(127 <= ord(c) <= 159 for c in text),
        "source text controls",
    )
    return normalized


def sha(data):
    return hashlib.sha256(data).hexdigest()


def typed(value):
    visits = 0

    def walk(v, depth):
        nonlocal visits
        visits += 1
        need(
            visits <= CAPS["json_nodes"] and depth <= CAPS["json_depth"],
            "JSON tree cap",
        )
        if v is None or type(v) is bool:
            return
        if type(v) is int:
            need(v.bit_length() <= 4096, "JSON integer cap")
        elif type(v) is str:
            need(len(v) <= 4096, "JSON string cap")
        else:
            need(type(v) in (list, dict) and len(v) <= 100000, "JSON container")
            if type(v) is dict:
                need(all(type(k) is str and len(k) <= 1024 for k in v), "JSON keys")
            for child in v.values() if type(v) is dict else v:
                walk(child, depth + 1)

    walk(value, 0)


def canonical(value):
    typed(value)
    result = json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode()
    need(len(result) <= CAPS["source_bytes"], "canonical source cap")
    return result


def decode(data):
    need(type(data) is bytes and len(data) <= CAPS["source_bytes"], "decode cap")

    def bad(_):
        raise ValueError("noninteger JSON")

    value = json.loads(
        data, object_pairs_hook=oa.pairs_unique, parse_float=bad, parse_constant=bad
    )
    typed(value)
    return value


def source(row):
    data = subprocess.check_output(
        ["git", "--no-replace-objects", "show", row["commit"] + ":" + row["path"]],
        cwd=ROOT,
    )
    need(len(data) <= CAPS["source_bytes"], "Git byte cap")
    return data


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "preregistration": DESIGN,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "contract": CONTRACT,
    }


def authenticate():
    need(
        canonical(decode(MANIFEST.read_bytes())) == canonical(manifest()),
        "fixed manifest",
    )
    ha.authenticate()
    saved = {}
    for row in BINDINGS:
        data = source(row)
        blob = hashlib.sha1(
            b"blob " + str(len(data)).encode() + b"\0" + data
        ).hexdigest()
        need(
            blob == row["git_blob"] and sha(lf(data)) == row["sha256_lf"],
            "frozen source identity",
        )
        key = row["commit"], row["path"]
        need(key not in saved, "unique source")
        saved[key] = data
        if row["path"].endswith(".py") and any(
            name in row["path"]
            for name in (
                "xi_fixed_lambda_heldout_alignment",
                "xi_companion_box_count_compression",
                "xi_companion_off_axis_ball_certificates",
            )
        ):
            need(
                sha(lf((ROOT / row["path"]).read_bytes())) == row["sha256_lf"],
                "executed helper identity",
            )
    index = {(r["commit"], r["path"]): r for r in BINDINGS}
    for key, data in saved.items():
        if key[1].endswith(".sources.json"):
            doc = decode(data)
            for row in doc.get("frozen_sources", doc.get("sources", [])):
                need(
                    all(
                        index[row["commit"], row["path"]][k] == row[k]
                        for k in ("commit", "path", "git_blob", "sha256_lf")
                    ),
                    "recursive source closure",
                )
    parent = decode(saved[BASE, D + "xi_quadratic_critical_transport.json"])
    unsigned = {k: v for k, v in parent.items() if k != "payload_sha256"}
    need(sha(canonical(unsigned)) == parent["payload_sha256"], "QT payload")
    need(len(parent["artifacts"]) == 4, "QT artifact count")
    for path, digest in parent["artifacts"].items():
        need(sha(lf(saved[BASE, path])) == digest, "QT artifact seal")
    need(parent["runtime"] == oa.RUNTIME, "QT runtime")
    return parent


def bounds(value):
    need(type(value) is list and len(value) == 2, "bounds shape")
    lo, hi = map(oa.unpair, value)
    need(lo <= hi, "bounds order")
    return lo, hi


def mul(a, b):
    products = [x * y for x in a for y in b]
    return min(products), max(products)


def div(a, b):
    need(b[1] < 0 or b[0] > 0, "interval division zero")
    return mul(a, (1 / b[1], 1 / b[0]))


def abs_interval(a):
    lo, hi = a
    return (Q(0) if lo <= 0 <= hi else min(abs(lo), abs(hi)), max(abs(lo), abs(hi)))


def sqrt_interval(a, bits=256):
    need(type(bits) is int and 16 <= bits <= 1024 and 0 <= a[0] <= a[1], "sqrt domain")
    scale = 1 << bits
    lower = math.isqrt((a[0].numerator << (2 * bits)) // a[0].denominator)
    upper = math.isqrt((a[1].numerator << (2 * bits)) // a[1].denominator)
    if Q(upper, scale) ** 2 < a[1]:
        upper += 1
    return Q(lower, scale), Q(upper, scale)


def exact_comparison(jets, lambda_bounds):
    a, c, v8 = (bounds(jets[key]) for key in ("f5", "f7", "f8"))
    L = bounds(lambda_bounds)
    need(L[0] > 0, "positive exact lambda")
    ratio = div((-a[1], -a[0]), mul(L, c))
    need(
        0 < ratio[0] <= ratio[1] and 2 * ratio[1] < L[0],
        "exact opposite-sign/discriminant",
    )
    ld = mul(L, L)
    lq = mul(L, ratio)
    d = sqrt_interval((ld[0] - 2 * lq[1], ld[1] - 2 * lq[0]))
    y = div((2 * lq[0], 2 * lq[1]), (L[0] + d[0], L[1] + d[1]))
    need(d[0] > 0 and y[0] > 0, "exact positive geometry")
    Bhi = 3 * d[1] ** 2 / (y[0] * (L[0] + d[0]) * (3 * L[0] + y[0]))
    mlo = abs_interval(v8)[0] / abs_interval(c)[1]
    coarse_hi = d[1] / (2 * L[0] * y[0])
    scale = 1 << 512
    lower = Q((mlo * scale).numerator // (mlo * scale).denominator, scale)

    def upper(q):
        v = q * scale
        return Q(-((-v.numerator) // v.denominator), scale)

    sharp, coarse = upper(Bhi), upper(coarse_hi)
    return {
        "sharp": lower >= sharp,
        "coarse": lower >= coarse,
        "m_lower": str(lower),
        "sharp_upper": str(sharp),
        "coarse_upper": str(coarse),
        "report_rounding_bits": 512,
    }


def sharp_threshold(lam, d, y):
    need(
        ctx.prec == 1024
        and all(type(v) is arb and v.is_finite() and v > 0 for v in (lam, d, y)),
        "threshold domain",
    )
    return 3 * d * d / (y * (lam + d) * (3 * lam + y))


def algebra_controls():
    count = 0
    for di in range(1, 13):
        for yi in range(1, 13):
            d, y = Q(di, 7), Q(yi, 11)
            L = d + y
            r = d * y / L
            need(0 < r < y and r < 2 * d, "maximizer admissible")
            f = r * (d - r / 2) / (y + r) ** 2
            need(f == d * d / (2 * y * (L + d)), "exact maximum identity")
            B = 3 * d * d / (y * (L + d) * (3 * L + y))
            need(
                d / (2 * L * y) - B
                == d * (5 * d + 4 * y) / (2 * L * (L + d) * (3 * L + y))
                > 0,
                "strict coarse improvement",
            )
            for j in range(1, 16):
                rr = Q(j, 16) * min(y, 2 * d)
                fp_numerator = (d - rr) * (y + rr) - 2 * (d * rr - rr * rr / 2)
                need(fp_numerator == d * y - L * rr, "derivative identity")
                threshold = rr * (d - rr / 2) / ((y + rr) ** 2 * ((y + rr) / 6 + L / 2))
                need(
                    0 < threshold < B,
                    "all test thresholds strictly below analytic ceiling",
                )
                count += 1
    need(Q(1, 100) < Q(2, 7) <= 1, "both sides of polynomial obstruction control")
    return {
        "rational_geometries": 144,
        "exact_radius_controls": count,
        "polynomial_threshold": "2/7",
        "low_cubic_third_derivative": "1/100",
        "high_cubic_third_derivative": "1",
        "finite_controls_are_not_all_radius_proof": True,
    }


def build_report():
    parent = authenticate()
    rows = parent["records"]
    need(
        len(rows) == 26 and [r["index"] for r in rows] == list(range(26)),
        "all26 source records",
    )
    outcomes = []
    with ha.precision(1024):
        lam = ha.fixed_lambda()
        L = oa.rbounds(lam)
        for row in rows:
            critical = row["critical"]
            need(
                critical["simple_real_critical"] is True,
                "inherited simple real critical",
            )
            center = oa.unpair(critical["center"])
            epsilon = oa.unpair(critical["radius"])
            need(
                epsilon == Q(1, 2**120)
                and 20 < center - epsilon < center + epsilon < 1100,
                "inherited full critical interval",
            )
            result = {
                "index": row["index"],
                "box_center": row["box_center"],
                "center": critical["center"],
                "radius": critical["radius"],
                "parent_critical_sha256": sha(canonical(critical)),
                "status": "UNRESOLVED",
            }
            outcomes.append(result)
            try:
                coeff = ha.xi_series(acb(arb(oa.qarb(center), oa.qarb(epsilon))), 9)
                need(all(v.imag.contains(0) for v in coeff), "real-interval jets")
                vals = {j: (coeff[j] * math.factorial(j)).real for j in (5, 6, 7, 8)}
                need(
                    vals[6].contains(0) and vals[5] * vals[7] < 0,
                    "critical consistency/opposite signs",
                )
                q = -vals[5] / (lam * vals[7])
                need(q > 0 and 2 * q < lam, "positive discriminant")
                d = (lam * lam - 2 * lam * q).sqrt()
                y = 2 * lam * q / (lam + d)
                B = sharp_threshold(lam, d, y)
                coarse = d / (2 * lam * y)
                m = abs(vals[8]) / abs(vals[7])
                mlo, Bhi, Chi = (
                    oa.endpoint(m.lower()),
                    oa.endpoint(B.upper()),
                    oa.endpoint(coarse.upper()),
                )
                impossible, old_impossible = mlo >= Bhi, mlo >= Chi
                jets = {"f" + str(j): oa.rbounds(v) for j, v in vals.items()}
                independent = exact_comparison(jets, L)
                need(
                    not impossible or independent["sharp"],
                    "independent sharp comparison",
                )
                need(
                    not old_impossible or independent["coarse"],
                    "independent coarse comparison",
                )
                result.update(
                    status="ALL_RADII_CRITERION_IMPOSSIBLE"
                    if impossible
                    else "UNRESOLVED",
                    jets=jets,
                    q=oa.rbounds(q),
                    d=oa.rbounds(d),
                    y=oa.rbounds(y),
                    normalized_third_derivative=oa.rbounds(m),
                    sharp_threshold=oa.rbounds(B),
                    coarse_threshold=oa.rbounds(coarse),
                    sharp_obstruction=impossible,
                    coarse_obstruction=old_impossible,
                    independent_fraction_comparison=independent,
                )
            except (ValueError, ZeroDivisionError, OverflowError) as error:
                result["reason"] = str(error)
        report = {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "frozen_sources": BINDINGS,
            "runtime": oa.RUNTIME,
            "design": DESIGN,
            "parent_payload_sha256": parent["payload_sha256"],
            "lambda_(64)": L,
            "records": outcomes,
            "coverage": {
                "nodes": 26,
                "fresh_coefficients_per_node": 9,
                "work_units": 234,
            },
            "summary": {
                "all_radii_impossible": sum(
                    r["status"] == "ALL_RADII_CRITERION_IMPOSSIBLE" for r in outcomes
                ),
                "unresolved": sum(r["status"] == "UNRESOLVED" for r in outcomes),
                "coarse_obstructions": sum(
                    r.get("coarse_obstruction", False) for r in outcomes
                ),
            },
            "exact_algebra": algebra_controls(),
            "artifacts": {
                p.relative_to(ROOT).as_posix(): sha(lf(p.read_bytes()))
                for p in (NOTE, Path(__file__), MANIFEST, TEST)
            },
        }
    report["payload_sha256"] = sha(canonical(report))
    need(len(canonical(report)) <= CAPS["report_bytes"], "own report cap")
    return report


def check_report(report):
    typed(report)
    need(type(report) is dict and "payload_sha256" in report, "report shape")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    need(sha(canonical(unsigned)) == report["payload_sha256"], "payload seal")
    need(
        canonical(report) == canonical(build_report()),
        "fresh complete all-radius replay",
    )
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--emit", action="store_true")
    mode.add_argument("--emit-sources", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.emit_sources:
        result = manifest()
    elif args.emit:
        result = build_report()
    else:
        check_report(decode(FIXTURE.read_bytes()))
        print("PASS all26 actual critical jets; all-radius criterion scope only")
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
