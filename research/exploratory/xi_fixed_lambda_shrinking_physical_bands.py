"""Fixed lambda_(64), inherited HA certificates, fresh physical low-pass arithmetic.
No boundary census or local-root replay is performed here. Physical operator
interpretation is conditional on the component-innerness premise.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from itertools import pairwise
from pathlib import Path

import xi_companion_box_count_compression as bc
from flint import acb, acb_series, arb, ctx

oa = bc.oa
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_fixed_lambda_shrinking_physical_bands"
BASE = "64165b8c805d182dbc43f2e5855e64a86cf1aaf9"
LB_SHA = "a7479e85fdc2a464cdc753021435cfef7a1f3910"
DESIGN = "f7cc9bea51c6ab0b969acdc6e279ed09f608acac"
D = "research/exploratory/"
NOTE = HERE / (STEM.upper() + ".md")
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BINDINGS = [
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "path": "research/exploratory/XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md",
        "git_blob": "3e9a15404532e72255acb3e55751987eb29a4043",
        "sha256_lf": "592c8313e5e46c68af6e5b3b9aa46c2724e84f51394cac3bd6934d0139eb26b7",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.py",
        "git_blob": "b472d18a3404ceebbde76e02bd6346678f4bdcfa",
        "sha256_lf": "1ad06f941f1c24f4732ef4db772c915f8bdf080abbdf2b8754816ea70fff01f0",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.json",
        "git_blob": "e5f1bc4e97be9b92f715e24b3670d64171071334",
        "sha256_lf": "eb6464cc2eed61f8aecf2eff6e2f36a5ee5f850252237f0f95bd9b0e4e51b206",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "path": "research/exploratory/xi_fixed_lambda_heldout_alignment.sources.json",
        "git_blob": "0dac7784b5c2a912d44c479e069e045b9f1b85e1",
        "sha256_lf": "3bb7fdccc56b8e7ac2e3c6fb1c0a62874645893683e8d626f4cdca8becdf9ad6",
    },
    {
        "commit": "64165b8c805d182dbc43f2e5855e64a86cf1aaf9",
        "path": "tests/test_xi_fixed_lambda_heldout_alignment.py",
        "git_blob": "c244417d71e8f31d59d3bbafb29543643bbb8c06",
        "sha256_lf": "8ece2393f6039ae3ea42b137cd079ef727a0db932de440f9a641020c9a0b0392",
    },
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "research/exploratory/XI_LAPLACE_LOW_PASS_LOWER_BOUND.md",
        "git_blob": "90e6bd89ca9a23c401d6d947c04a9d548f6b3030",
        "sha256_lf": "c56d29037b85c45398bcb34dc7fb8450ba0e4b0f32fa7293edcaf5d1d2ea4b64",
    },
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "research/exploratory/xi_laplace_low_pass_lower_bound.py",
        "git_blob": "6c04e959ac106ebbc1e33621cb50cb121da2b27b",
        "sha256_lf": "cc5fa52704fb26742ded7c2605ee561f676166c7be1974090bbe8161d2b3a009",
    },
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "research/exploratory/xi_laplace_low_pass_lower_bound.json",
        "git_blob": "7c5a3813dec44105c729fe907011f23512ed79a0",
        "sha256_lf": "1f6b37f040eff6fc9d67f98a9b9af4ff2dd0e96ac84d3019a7d15f82ee529252",
    },
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "research/exploratory/xi_laplace_low_pass_lower_bound.sources.json",
        "git_blob": "ca17786f2fea78b1ca30a114a21637233f8d9af3",
        "sha256_lf": "96be4f20f167972f491c784090f4d9adcdcc8eb2afcdff13125a1e9648c26782",
    },
    {
        "commit": "a7479e85fdc2a464cdc753021435cfef7a1f3910",
        "path": "tests/test_xi_laplace_low_pass_lower_bound.py",
        "git_blob": "e7ea79ce7ab8aebb5cf3edd77cbb13c0bd4eb034",
        "sha256_lf": "6e03d1a7e1285d30602bb2057144dacff820567bdbbca8d72548415c4fd46b35",
    },
    {
        "commit": "f7cc9bea51c6ab0b969acdc6e279ed09f608acac",
        "path": "research/exploratory/XI_FIXED_LAMBDA_SHRINKING_PHYSICAL_BANDS.md",
        "git_blob": "54363a5f28a7e202dad2898dab64d5430a0fdc5f",
        "sha256_lf": "19e4f2c6ce491c430b458cab92eb4c467730f24c1759a63c1f71e893a2beffac",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
        "git_blob": "27e4db71377788b6e03b14005035d59c9e930611",
        "sha256_lf": "7f6efdcd6375d14db36ade51c073d3c04dc73f5e2c9c5cd27aa94d8107497460",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.py",
        "git_blob": "62f94b71810a49646830694cab25bb14c1eab470",
        "sha256_lf": "69e51a36a9180df97ae6b994104308a46b9ab84331027e1d8ed288c6490d5300",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.json",
        "git_blob": "d3ef5908f68a7b3025428bf55e8e1fa81970e273",
        "sha256_lf": "504071292138882ad5192fc62f765edc5615c3140542c7f597651679ba682cdb",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "research/exploratory/xi_fixed_lambda_joint_box_compression.sources.json",
        "git_blob": "62eb2fa59113bc87158659e538fb1fea5b7f7ca4",
        "sha256_lf": "b775a9c8bc054312644116b362960b1c1e950d23a8dfc82d556d86f67a30c819",
    },
    {
        "commit": "0e3fc9b482f0f115a49a6209ccbfeffae640014a",
        "path": "tests/test_xi_fixed_lambda_joint_box_compression.py",
        "git_blob": "6cdac911a7e62d12273d7eafd2fdef199b282d33",
        "sha256_lf": "deb2696c5c160e0da970c31f35e5ed472baabc4fb1d3db831b4e48371935ae80",
    },
    {
        "commit": "24544028cd033ea66a6b64bec254da5ea43230c9",
        "path": "research/exploratory/XI_FIXED_LAMBDA_HELDOUT_ALIGNMENT.md",
        "git_blob": "db03a1b0c1f5abc0e27be92c4232968f68f816b8",
        "sha256_lf": "714bf76812826957269bb26d10c3a919909ad7af97b0ec9becfb8a4e5f0c79bd",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/XI_COMPANION_BOX_COUNT_COMPRESSION.md",
        "git_blob": "2860d9c9bb90f4423f17f0d272229e78a30ae62b",
        "sha256_lf": "22d11bf3dccb72fa25633deeee063164611dbaa977c5e66fca84f4350ae79c65",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/xi_companion_box_count_compression.py",
        "git_blob": "698211f63f2268f421faa1ed76d4dd8749a4b311",
        "sha256_lf": "cea67ec0b5335ecef7a6df8d453859a249b73d1b716b8c87565709d27ec95e58",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/xi_companion_box_count_compression.json",
        "git_blob": "346a452e1c3136f19139debe1620577ef41e6b43",
        "sha256_lf": "9148321153c7319518dc9475adee61f2ba5b646663f1cb35b762f31f280834e4",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "research/exploratory/xi_companion_box_count_compression.sources.json",
        "git_blob": "fcbfb819e09f97f9f4e9af60141ffe198238bf1c",
        "sha256_lf": "b916af0286ddd686e700b56032a2f10f9b0bc08212bed6ca60bb99270b85299f",
    },
    {
        "commit": "7fbcd592042a5cc98c17d0db2fac62f8171267f2",
        "path": "tests/test_xi_companion_box_count_compression.py",
        "git_blob": "ea093cc50fb8b9de415ce4e71bc370ffe456d8ed",
        "sha256_lf": "e9b40aaa100f1f8ae74ad2d90978b8e7621303ac750a847cbfc8ec045a2e05b5",
    },
    {
        "commit": "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "path": "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "git_blob": "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "sha256_lf": "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    },
    {
        "commit": "e669d257711d8d4a6a0ab7aeb21254fd220f7dc3",
        "path": "research/exploratory/XI_FIXED_LAMBDA_JOINT_BOX_COMPRESSION.md",
        "git_blob": "a11b631e88343ad0782e2d7db511282eb473a30c",
        "sha256_lf": "d8e1f3cc061fc0671b45ef26e09c83b0e165545e3c56e049cf301221377ebc95",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "path": "research/exploratory/XI_COMPANION_OFF_AXIS_BALL_CERTIFICATES.md",
        "git_blob": "625cc29f67510bd58ed667f6f5fec242b84e4a11",
        "sha256_lf": "020597b67044d996e12e2f76655550557cc33cd52cf717553e2fc6be9d48e396",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.py",
        "git_blob": "b0cecac35dcdb3a583ae891609d7d89b378b537b",
        "sha256_lf": "319e9abf775199e1747b0642dd99f24e52d9700bf71c04385d02cf5be9aac15f",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.json",
        "git_blob": "e7cdd61fcc046d142ccc95b5796d3106a79139c4",
        "sha256_lf": "268e67f84bdae5d41a4acb95df96fff18e00c3d0ae3430a9be8c89f633ff7c5b",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "path": "research/exploratory/xi_companion_off_axis_ball_certificates.sources.json",
        "git_blob": "06434dc776028d155b8107f8cb5ea8687a3ce9dc",
        "sha256_lf": "eec3231292d8d5b030c68ffaed9520dd5697657dcd17f15c91e4f34ee8f9be4c",
    },
    {
        "commit": "134a55016b4f3ea970dc8e5f03505d4e97afff07",
        "path": "tests/test_xi_companion_off_axis_ball_certificates.py",
        "git_blob": "f1f323d579968949cf07c662dd245172380759ba",
        "sha256_lf": "3cfd3a3c2177ccbb242aeb5a9fa7e83b27859f9485a532489304019499b8dcd7",
    },
    {
        "commit": "7aed2ec0b99b9d7f2fb94a774922a83d5b84a870",
        "path": "research/exploratory/COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md",
        "git_blob": "cd74bd06267eb4d60bc977353d11f6a0fb72ba6a",
        "sha256_lf": "b9ab266898129389b94a9ed494b140422fc823552c6b69bf22ed36a9dbb2e7f7",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "git_blob": "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "sha256_lf": "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106610-riemann-siegel-gauge-factorization.md",
        "git_blob": "16ab64a193e59608c9e2c9fd9762addc58809c3f",
        "sha256_lf": "11c87fd9b50c309249b76f39fd87c3d20953779355a39a0338ef281d3cb57c87",
    },
    {
        "commit": "d38961c15fc76d671cef4fddfc92d3c866af4fd5",
        "path": "research/exploratory/XI_COMPANION_IMAGINARY_AXIS_SAMPLING.md",
        "git_blob": "9688e30825fcc3d2b13570539bf03299407eae87",
        "sha256_lf": "a9d6b51b3b2f1ccb388fb8d74e115023c622115b169d3214f071ef9005034081",
    },
    {
        "commit": "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d",
        "path": "research/exploratory/XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md",
        "git_blob": "e592a4c031876f56f07d28b7e18a8a7cf6e826f4",
        "sha256_lf": "5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d",
    },
    {
        "commit": "d76a1a8eb8ec40b19a351af95439b9a6514bee87",
        "path": "research/exploratory/XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md",
        "git_blob": "797f7b581580ad5a441c7702015c64a53eca6f4d",
        "sha256_lf": "55aa96745c3f269ac464ea7c0b8227e14e7d8ceb33f8bec2fc13f9642b33d44d",
    },
]
WIDTHS = (Q(1, 256), Q(1, 1024), Q(1, 4096))
HEIGHTS = tuple(2**j for j in range(6, 17))
PREFIXES = (14, 22, 31, 40)
CEILINGS = (Q(1171, 500), Q(599, 250), Q(1207, 500), Q(121, 50))
CAPS = {
    "source_bytes": 24000000,
    "report_bytes": 8000000,
    "json_nodes": 600000,
    "json_depth": 24,
    "container_length": 100000,
    "string_length": 4096,
    "integer_bits": 4096,
    "source_bindings": 40,
    "nodes": 40,
    "grid_cells": 1320,
    "precision_bits": 256,
    "series_cap": 2,
    "work_units": 10000,
}
WORK = 0
CONTRACT = {
    "primitive": "actual unrescaled Xi; ONE lambda_(64) fixed by exact digamma formula, not numeric64",
    "source_inheritance": "HA40 root/raw/fullGram and LB axis certificates inherited from authenticated frozen sources; no new root/census replay",
    "fresh_arithmetic": "11 axis values,1320 node/width/height bounds,12 prefix-band summaries,39 gap tests,40 cell-membership tests",
    "inner_premise": "Theta0 and Theta5 inner with Gamma common divisor, U and B reduced factors; UNPAID",
    "physical_operator": "Pi_[0,D] P_(UH2) P_E in boundary-dx Hardy norm; same lower bounds for E replaced by K_B",
    "raw_comparison": "scalar at b and ih only; NEVER band Loewner",
    "metric": "only inherited normalized Gram ceilings2.342,2.396,2.414,2.420 in HS denominator; Carleson cost is not Gram norm",
    "arithmetic_class": "MIXED",
    "arithmetic_components": [
        "DIRECTED_BALL_ENCLOSURES",
        "EXACT_RATIONAL",
        "CERTIFIED_INTEGER_COVERAGE",
    ],
    "rounding": "pinned FLINT outward balls; exact rational acceptance; strict final downward decimal floors12/16",
    "analytic_quantifiers_machine_certified": False,
    "cofinal_capture": False,
    "actual_innerness_proved": False,
    "RH": False,
    "all_failed_or_zero_grid_cells_retained": True,
    "caps": CAPS,
}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def charge(n=1):
    global WORK
    oa.integer(n, 0, CAPS["work_units"])
    WORK += n
    need(WORK <= CAPS["work_units"], "work cap")


def lf(raw):
    need(
        type(raw) is bytes and len(raw) <= CAPS["source_bytes"], "source byte cap/type"
    )
    out = raw.replace(b"\r\n", b"\n")
    text = out.decode("utf-8")
    need(
        all(ord(c) in (9, 10) or ord(c) >= 32 for c in text)
        and not any(127 <= ord(c) <= 159 for c in text),
        "source text control",
    )
    return out


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


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
        if type(v) is str:
            need(len(v) <= CAPS["string_length"], "JSON string cap")
        elif type(v) is int:
            need(v.bit_length() <= CAPS["integer_bits"], "JSON integer cap")
        else:
            need(
                type(v) in (list, dict) and len(v) <= CAPS["container_length"],
                "JSON container",
            )
            if type(v) is dict:
                need(all(type(k) is str and len(k) <= 1024 for k in v), "JSON keys")
                children = v.values()
            else:
                children = v
            for child in children:
                walk(child, depth + 1)

    walk(value, 0)


def canonical(value):
    typed(value)
    raw = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode()
    need(len(raw) <= CAPS["source_bytes"], "canonical byte cap")
    return raw


def decode(raw):
    need(type(raw) is bytes and len(raw) <= CAPS["source_bytes"], "JSON byte cap")

    def reject(_):
        raise ValueError("noninteger JSON number")

    out = json.loads(
        raw,
        object_pairs_hook=oa.pairs_unique,
        parse_float=reject,
        parse_constant=reject,
    )
    typed(out)
    return out


def file_bytes(path):
    need(path.stat().st_size <= CAPS["source_bytes"], "file byte cap")
    return path.read_bytes()


def read_source(row):
    raw = subprocess.check_output(
        ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
    )
    need(len(raw) <= CAPS["source_bytes"], "Git source byte cap")
    return raw


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "design": DESIGN,
        "direct_source_count": 11,
        "recursive_source_count": 35,
        "frozen_sources": BINDINGS,
        "runtime": oa.RUNTIME,
        "contract": CONTRACT,
        "documentation": bc.manifest()["documentation"],
    }


def authenticated_sources():
    need(
        canonical(decode(file_bytes(MANIFEST))) == canonical(manifest()),
        "fixed manifest",
    )
    need(len(BINDINGS) == 35 <= CAPS["source_bindings"], "source closure count")
    # This also authenticates the44 actual native runtime files.
    bc.authenticate()
    raw_map = {}
    hashes = {}
    for row in BINDINGS:
        raw = read_source(row)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and digest(lf(raw)) == row["sha256_lf"],
            "frozen Git/LF source identity",
        )
        key = (row["commit"], row["path"])
        need(key not in raw_map, "duplicate source identity")
        raw_map[key] = raw
        hashes[key] = row
    for row in BINDINGS:
        if row["path"].endswith(".sources.json"):
            data = decode(raw_map[row["commit"], row["path"]])
            for child in data.get("frozen_sources", data.get("sources", [])):
                key = (child["commit"], child["path"])
                need(
                    key in hashes
                    and all(
                        hashes[key][field] == child[field]
                        for field in ("commit", "path", "git_blob", "sha256_lf")
                    ),
                    "recursive source closure",
                )
    # Only the unchanged BC/OA helpers execute locally.
    for row in BINDINGS:
        if row["commit"] in (bc.BASE, "7fbcd592042a5cc98c17d0db2fac62f8171267f2") and (
            "xi_companion_off_axis_ball_certificates" in row["path"].lower()
            or "xi_companion_box_count_compression" in row["path"].lower()
        ):
            need(
                digest(lf(file_bytes(ROOT / row["path"]))) == row["sha256_lf"],
                "executed parent local identity",
            )
    return raw_map


def inherited_report(raw_map, commit, stem):
    path = D + stem + ".json"
    data = decode(raw_map[commit, path])
    need(type(data) is dict and "payload_sha256" in data, "inherited report schema")
    unsigned = {k: v for k, v in data.items() if k != "payload_sha256"}
    need(
        data["payload_sha256"] == digest(canonical(unsigned)), "inherited payload seal"
    )
    need(
        type(data["artifacts"]) is dict and len(data["artifacts"]) == 4,
        "inherited artifacts",
    )
    for artifact, sha in data["artifacts"].items():
        need(
            (commit, artifact) in raw_map
            and digest(lf(raw_map[commit, artifact])) == sha,
            "inherited artifact seal",
        )
    need(data["runtime"] == oa.RUNTIME, "inherited runtime")
    return data


def real_bounds(v):
    need(type(v) is list and len(v) == 2, "real enclosure shape")
    lo, hi = map(oa.unpair, v)
    need(lo <= hi, "real enclosure orientation")
    return lo, hi


def real_ball(v):
    lo, hi = real_bounds(v)
    return arb(oa.qarb((lo + hi) / 2), oa.qarb((hi - lo) / 2))


def complex_ball(v):
    need(type(v) is dict and set(v) == {"real", "imag"}, "complex enclosure schema")
    return acb(real_ball(v["real"]), real_ball(v["imag"]))


def prepared_nodes(ha):
    need(
        ha["parameter_anchor"] == 64 and type(ha["parameter_anchor"]) is int,
        "ONE exact anchor64",
    )
    rows = ha["roots"]
    need(type(rows) is list and len(rows) == 40, "complete40nodes")
    prepared = []
    for index, row in enumerate(rows):
        need(
            type(row["parameter_anchor"]) is int and row["parameter_anchor"] == 64,
            "each node same fixed calibration",
        )
        x, y = map(oa.unpair, row["center"])
        r = oa.unpair(row["radius"])
        need(
            r == Q(1, 2**120) and 20 < x - r < x + r < 1100 and 0 < y - r < y + r < 1,
            "inherited containing root rectangle",
        )
        rr = row["rouche"]
        need(
            oa.unpair(rr["left"]) * 2**50 < oa.unpair(rr["right"]),
            "inherited Rouche slack",
        )
        need(
            set(row["nonzero"]) == {"C5", "R0", "C0", "f6", "W", "R5prime"}
            and all(oa.unpair(v) > 0 for v in row["nonzero"].values()),
            "inherited survival",
        )
        bx = [oa.pair(x - r), oa.pair(x + r)]
        by = [oa.pair(y - r), oa.pair(y + r)]
        b = acb(real_ball(bx), real_ball(by))
        raw = complex_ball(row["raw_theta"])
        need(raw.abs_lower() > 0, "inherited raw survival enclosure")
        need(real_bounds(row["raw_modulus"])[0] > 0, "inherited raw modulus lower")
        prepared.append(
            (
                {
                    "index": index,
                    "box_center": row["box_center"],
                    "parameter_anchor": 64,
                    "center": row["center"],
                    "radius": row["radius"],
                    "x_interval": bx,
                    "y_interval": by,
                    "raw_theta": row["raw_theta"],
                    "raw_modulus": row["raw_modulus"],
                    "complete_parent_root_sha256": digest(canonical(row)),
                },
                b,
                raw,
            )
        )
    return prepared


def inherited_prefixes(ha):
    gram = ha["finite_data"]["normalized_gram"]
    need(
        type(gram) is list
        and len(gram) == 40
        and all(type(r) is list and len(r) == 40 for r in gram),
        "complete inherited40x40 Gram",
    )
    prefixes = ha["finite_data"]["prefixes"]
    need(len(prefixes) == 4, "four frozen prefixes")
    result = []
    for row, n, ceiling in zip(prefixes, PREFIXES, CEILINGS):
        indices = row["root_indices"]
        need(
            indices == list(range(n)) and all(type(i) is int for i in indices),
            "literal nested prefix indices",
        )
        need(
            oa.unpair(row["finite_bessel_strict_upper"]) == ceiling,
            "fixed Gram ceiling",
        )
        need(
            len(row["normalized_gram_row_sums"]) == n
            and all(
                real_bounds(v)[1] < ceiling for v in row["normalized_gram_row_sums"]
            ),
            "source Gram upper predicate",
        )
        result.append(
            {
                "nodes": n,
                "indices": indices,
                "Gram_ceiling": oa.pair(ceiling),
                "complete_parent_prefix_sha256": digest(canonical(row)),
            }
        )
    return result


def fixed_lambda():
    need(ctx.prec == 256, "fixed precision")
    return oa.frozen_lambda(64)


def axis_value(height, lam, direct=False):
    oa.integer(height, 64, 65536)
    need(height in HEIGHTS and type(lam) is arb and 0 < lam < 100, "axis domain")
    need(type(direct) is bool and ctx.prec == 256, "axis route/precision")
    charge()
    previous = ctx.cap
    ctx.cap = 2
    try:
        sigma = oa.qarb(Q(1, 2) + height)
        series = acb_series([acb(sigma), 1])
        zeta = series.zeta()
        need(zeta[0].real > 0 and zeta[0].imag.contains(0), "axis positive zeta")
        ell = (
            1 / sigma
            + 1 / (sigma - 1)
            - arb.pi().log() / 2
            + acb(sigma / 2).digamma().real / 2
            + (zeta[1] / zeta[0]).real
        )
        need(ell > 0 and 1 + lam * ell > 0, "axis nonzero denominator")
        value = (1 - lam * ell) / (1 + lam * ell)
        if direct:
            full = (
                series
                * (series - 1)
                / 2
                * (-series * arb.pi().log() / 2).exp()
                * (series / 2).gamma()
                * zeta
            )
            alternative = (full[0] - lam * full[1]) / (full[0] + lam * full[1])
            need(
                alternative.is_finite()
                and alternative.imag.contains(0)
                and alternative.real.overlaps(value),
                "direct reflected Xi axis route",
            )
        return value, ell
    finally:
        ctx.cap = previous


def lower_bound(node, raw, height, width, axis_modulus):
    need(
        type(node) is acb
        and node.is_finite()
        and 0 < node.imag < 1
        and 20 < node.real < 1100,
        "positive full node rectangle",
    )
    need(type(raw) is acb and raw.is_finite() and abs(raw) < 2, "raw ball")
    oa.integer(height, 64, 65536)
    width = oa.rational(width)
    need(
        height in HEIGHTS
        and width in WIDTHS
        and type(axis_modulus) is arb
        and 0 <= axis_modulus <= 1
        and ctx.prec == 256,
        "fixed grid/domain",
    )
    charge()
    h, w = arb(height), oa.qarb(width)
    laplace = (
        2
        * (h * node.imag).sqrt()
        * axis_modulus
        / ((h + node.imag) ** 2 + node.real**2).sqrt()
    )
    tail = (-h * w).exp()
    widened = False
    if tail < oa.qarb(Q(1, 2**512)):
        tail = arb(oa.qarb(Q(1, 2**513)), oa.qarb(Q(1, 2**513)))
        widened = True
    bracket = laplace - tail
    denominator = (1 - (-2 * h * w).exp()).sqrt()
    need(denominator > 0 and bracket.is_finite(), "finite band denominator")
    raw_abs = abs(raw)
    floor = (
        oa.endpoint((raw_abs * bracket / denominator).lower()) if bracket > 0 else Q(0)
    )
    need(floor >= 0, "nonnegative node floor")
    return {
        "h": height,
        "D": oa.pair(width),
        "laplace": oa.rbounds(laplace),
        "tail": oa.rbounds(tail),
        "tail_widened": widened,
        "bracket": oa.rbounds(bracket),
        "denominator": oa.rbounds(denominator),
        "raw_modulus_used": oa.rbounds(raw_abs),
        "norm_lower": oa.pair(floor),
        "positive": floor > 0,
    }


def strict_floor(value, digits):
    value = oa.rational(value)
    oa.integer(digits, 1, 16)
    need(value >= 0, "nonnegative reported bound")
    scaled = value * 10**digits
    n = scaled.numerator // scaled.denominator
    if n and scaled == n:
        n -= 1
    out = Q(n, 10**digits)
    need(out == 0 or 0 < out < value, "strict lower reporting")
    return out


def geometry(rows):
    need(type(rows) is list and len(rows) == 40, "geometry40")
    order = sorted(range(40), key=lambda j: real_bounds(rows[j]["x_interval"])[0])
    gaps = []
    for a, b in pairwise(order):
        x1, x2 = real_bounds(rows[a]["x_interval"]), real_bounds(rows[b]["x_interval"])
        y1, y2 = real_bounds(rows[a]["y_interval"]), real_bounds(rows[b]["y_interval"])
        gap = x2[0] - x1[1]
        need(gap > 0, "disjoint inherited real rectangles")
        rhs = y1[1] + y2[1]
        gaps.append(
            {
                "left": a,
                "right": b,
                "gap_lower": oa.pair(gap),
                "height_sum_upper": oa.pair(rhs),
                "certified": gap >= rhs,
            }
        )
    memberships = []
    cells = {}
    for j, row in enumerate(rows):
        lo, hi = real_bounds(row["x_interval"])
        cell = lo.numerator // lo.denominator
        certain = hi < cell + 1
        memberships.append({"index": j, "lower_cell": cell, "resolved": certain})
        if certain:
            cells.setdefault(cell, []).append(j)
    cell_rows = []
    for cell, indices in sorted(cells.items()):
        selected = sorted(indices, key=lambda j: real_bounds(rows[j]["x_interval"])[0])
        passed = all(
            real_bounds(rows[b]["x_interval"])[0]
            - real_bounds(rows[a]["x_interval"])[1]
            >= real_bounds(rows[a]["y_interval"])[1]
            + real_bounds(rows[b]["y_interval"])[1]
            for a, b in pairwise(selected)
        )
        cell_rows.append(
            {
                "cell": cell,
                "indices": selected,
                "occupancy": len(selected),
                "gap_certificate": passed,
                "Carleson_cost_upper": 1 if passed else len(selected),
            }
        )
    all_gaps = all(row["certified"] for row in gaps)
    return {
        "ordered_indices": order,
        "adjacent_gaps": gaps,
        "all39gaps_certified": all_gaps,
        "global_Carleson_box_upper": 1 if all_gaps else 40,
        "global_bound_route": "separated-height span"
        if all_gaps
        else "occupancy fallback",
        "memberships": memberships,
        "all40memberships_resolved": all(r["resolved"] for r in memberships),
        "occupied_unit_cells": cell_rows,
        "Carleson_upper_is_NOT_Gram_ceiling": True,
    }


def build_report():
    global WORK
    WORK = 0
    source = authenticated_sources()
    ha = inherited_report(source, BASE, "xi_fixed_lambda_heldout_alignment")
    lb = inherited_report(source, LB_SHA, "xi_laplace_low_pass_lower_bound")
    old = [op for op in lb["operators"] if op["anchor"] == 64]
    need(len(old) == 1, "unique inherited lambda_(64) calibration")
    old = old[0]
    prefixes = inherited_prefixes(ha)
    with oa.precision(256):
        lam = fixed_lambda()
        need(real_ball(old["lambda"]).overlaps(lam), "fixed lambda matches LBanchor64")
        prepared = prepared_nodes(ha)
        axes = []
        axis_balls = {}
        need([a["h"] for a in old["calibrations"]] == list(HEIGHTS), "inherited11axis")
        for h, historical in zip(HEIGHTS, old["calibrations"]):
            theta, ell = axis_value(h, lam, direct=h in (64, 256, 1024))
            need(
                theta.overlaps(real_ball(historical["theta_axis"]))
                and ell.overlaps(real_ball(historical["log_derivative"])),
                "parent axis agreement",
            )
            axes.append(
                {
                    "h": h,
                    "theta_axis": oa.rbounds(theta),
                    "log_derivative": oa.rbounds(ell),
                    "direct_route_checked": h in (64, 256, 1024),
                    "matches_parent_theta_exactly": oa.rbounds(theta)
                    == historical["theta_axis"],
                    "matches_parent_ell_exactly": oa.rbounds(ell)
                    == historical["log_derivative"],
                }
            )
            axis_balls[h] = abs(theta)
        bands = []
        for width in WIDTHS:
            grid = []
            best = []
            for row, node, raw in prepared:
                entries = [
                    lower_bound(node, raw, h, width, axis_balls[h]) for h in HEIGHTS
                ]
                grid.append({"node_index": row["index"], "witnesses": entries})
                best.append(max(oa.unpair(v["norm_lower"]) for v in entries))
            summaries = []
            for prefix in prefixes:
                indices = prefix["indices"]
                c = oa.unpair(prefix["Gram_ceiling"])
                trace = sum(best[j] ** 2 for j in indices) / c
                norm = max(best[j] for j in indices)
                summaries.append(
                    {
                        "prefix_nodes": prefix["nodes"],
                        "Gram_ceiling": prefix["Gram_ceiling"],
                        "squared_HS_lower": oa.pair(trace),
                        "norm_lower": oa.pair(norm),
                        "strict_squared_HS_floor": oa.pair(strict_floor(trace, 16)),
                        "strict_norm_floor": oa.pair(strict_floor(norm, 12)),
                    }
                )
            bands.append(
                {
                    "D": oa.pair(width),
                    "all1320_grid_part": grid,
                    "best_node_lower": [oa.pair(v) for v in best],
                    "all40_nodes_positive": all(v > 0 for v in best),
                    "prefixes": summaries,
                    "positive_cells": sum(
                        v["positive"] for row in grid for v in row["witnesses"]
                    ),
                    "zero_cells": sum(
                        not v["positive"] for row in grid for v in row["witnesses"]
                    ),
                }
            )
        rows = [r for r, _, _ in prepared]
        geo = geometry(rows)
        need(
            sum(
                len(row["witnesses"])
                for band in bands
                for row in band["all1320_grid_part"]
            )
            == 1320,
            "full1320grid",
        )
        result = {
            "schema": STEM + "-v1",
            "contract": CONTRACT,
            "runtime": oa.RUNTIME,
            "design": DESIGN,
            "sources": BINDINGS,
            "parameter_anchor": 64,
            "lambda_(64)": oa.rbounds(lam),
            "inherited_nodes": rows,
            "inherited_prefixes": prefixes,
            "parent_payloads": {"HA": ha["payload_sha256"], "LB": lb["payload_sha256"]},
            "axis_calibrations": axes,
            "bands": bands,
            "geometry": geo,
            "coverage": {
                "nodes": 40,
                "widths": 3,
                "heights": 11,
                "grid": 1320,
                "axis": 11,
                "prefixes": [14, 22, 31, 40],
                "prefix_band_cells": 12,
                "gaps": 39,
                "memberships": 40,
            },
            "work_units": WORK,
            "artifacts": {
                p.relative_to(ROOT).as_posix(): digest(lf(file_bytes(p)))
                for p in (NOTE, Path(__file__), MANIFEST, TEST)
            },
        }
    result["payload_sha256"] = digest(canonical(result))
    need(len(canonical(result)) <= CAPS["report_bytes"], "report byte cap")
    return result


def check_report(report):
    typed(report)
    need(type(report) is dict and "payload_sha256" in report, "report object")
    unsigned = {k: v for k, v in report.items() if k != "payload_sha256"}
    need(report["payload_sha256"] == digest(canonical(unsigned)), "payload seal")
    need(canonical(report) == canonical(build_report()), "complete fresh band replay")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--emit", action="store_true")
    modes.add_argument("--emit-sources", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.emit_sources:
        print(json.dumps(manifest(), sort_keys=True, indent=2))
    elif args.emit:
        print(json.dumps(build_report(), sort_keys=True, indent=2))
    else:
        raw = file_bytes(FIXTURE)
        check_report(decode(raw))
        print(
            "PASS ONElambda_(64),40nodes,1320physical-band cells,12prefix bounds; inner premise unpaid"
        )
        print("fixture_sha256_lf=" + digest(lf(raw)))


if __name__ == "__main__":
    main()
