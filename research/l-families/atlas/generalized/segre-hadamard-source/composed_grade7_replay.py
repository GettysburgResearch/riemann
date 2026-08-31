"""Compose accepted lower-stage proofs with fresh exact grade-seven kernels."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
MAX_BYTES = 64 * 1024 * 1024
GRADE6 = "d3bda0446a379ce0bd8dfe4024f0184451adb1d5"
COORDINATES = "41b74441d26dc69c3c2134cc2b839ce522f9f183"
# Complete directly consumed chain: authenticate all entries before any parse/import.
GROUPS = (
    (
        COORDINATES,
        {
            "STREAMED_RESOLUTION640_PREREGISTRATION.md": "06344a37659c0e07c74273de5b083179317fa262",
            "STREAMED_RESOLUTION640_REPLAY.md": "d7faaaacc21ae542b67e1083de68632f75e271dd",
            "streamed_resolution640.py": "56f3f33bb2ef5d12943ae8191d135c464ae78141",
            "streamed640_coordinate.discovery.json": "1d3b340f50f975b3aa98af23f6d7016ec822632a",
            "@tests/test_segre_hadamard_streamed640.py": "3ae36d6f445f48633f3c2bdd954010ee843a3ba1",
        },
    ),
    (
        GRADE6,
        {
            "row_restricted_grade6.discovery.json": "b9131081876be381c43237ea42c5695767bd73ae"
        },
    ),
    (
        "423a25c35996ec5bf2c4dfaac6594d31f89f1081",
        {
            "GLOBAL_EXACTNESS_FROM_CERTIFIED_KERNELS.md": "79e3792aad018275ba90353e470f1fa234bd76d5",
            "TERNARY_CUBE_FULL_RESOLUTION.md": "daa8d3f42701dbc6ba5a22c18782e4568bec22cf",
        },
    ),
    (
        "a9c78452768df3f3be643afbbfe1661e4f14bd85",
        {
            "ROW_RESTRICTED_RESOLUTION_PREREGISTRATION.md": "7f3ab0fdc833b4b6004df7e8b1c59c4c4aa22dda",
            "ROW_RESTRICTED_RESOLUTION_REPLAY.md": "29163a7bb3c59cb2202c90671a06745874e1bffe",
            "row_restricted_resolution.py": "0a43b7ebce8e4a868952fa53a96ca42be76998b3",
            "@tests/test_segre_hadamard_row_restricted_resolution.py": "d30a8ebdd65214453def0d986929c8848856417b",
        },
    ),
    (
        "5cb770ce6ef7e20535de155d9b232698424d2e3c",
        {
            "RESOLUTION_SHAPE_PREREGISTRATION.md": "acba78d69b017771a6af608184e024ebf180ce71",
            "resolution_shape_preflight.py": "c38e375c626962eebc653700ab84d40ba75619c1",
            "resolution_shape.discovery.json": "53dd114fd6eedb179c6b0fe2e4730f2909d1bc4d",
        },
    ),
    (
        "742d68b6d3c37191589b0e6463bc122af6d90f76",
        {
            "RESOLUTION_STAGE5_CACHE_PREREGISTRATION.md": "b3f9807415543a780ea18db2f07b2293c9a0aa3a",
            "resolution_stage5_cache.py": "fb7420f12e667d73b8f51bc3ed3ff3150be372ba",
            "resolution_stage5.cache.json": "3f1689a7388de3b4cf3f33e3cc7057d51a94118b",
            "@tests/test_segre_hadamard_stage5_cache.py": "7506e6b226360f81a85e662e2f0c9ec2e67a50a3",
        },
    ),
    (
        "b1c48ff9f09ec521a7f33b2ecbf81f661e8145cd",
        {
            "full_resolution_replay.py": "421fd58e65c529b93b0d3bb781f135c3bd3b090a",
            "TERNARY_CUBE_FULL_RESOLUTION_PREREGISTRATION.md": "5e6f37cd49df1b0f18664638828953b6bb01f55c",
            "full_resolution_stage5.discovery.json": "4c9f58cc8383855504b333852d677756c271163c",
        },
    ),
    (
        "1a5a63f1148fb884e9ae7aae9e9324a40aee9f33",
        {
            "TERNARY_CUBE_RESOLUTION_PREREGISTRATION.md": "54b477ab74eccb925b471a0adeab0500bd61d8ae",
            "resolution_replay.py": "610f50d0e7ef2a47e361ba61a6b4caf53b0fb543",
            "resolution_degree4.discovery.json": "dd9898be35c4898101347e28af6c9206199bf5d8",
        },
    ),
    (
        "4c635b2ee8d7cf6caa41efde2d2e0c7baea1b787",
        {
            "TERNARY_CUBE_PRESENTATION.md": "ff8bcf95ef425ac976718d8037cedc6a5374ee4e",
            "presentation_replay.py": "cf6bf60d04301c71881fe312511ec3c43bd9402a",
            "presentation.verification.json": "06eec475eac92726ede0a6c342b81904eae7bf99",
        },
    ),
)
PREREG = HERE / "COMPOSED_GRADE7_PREREGISTRATION.md"
OWNED = (
    Path(__file__),
    PREREG,
    HERE / "COMPOSED_GRADE7_REPLAY.md",
    ROOT / "tests/test_segre_hadamard_composed_grade7.py",
)
DIRECTORY = HERE / "composed_grade7_weightblocks"
FIXTURE = HERE / "composed_grade7.verification.json"
PREFIX_FIXTURE = HERE / "composed_grade7_prefix.discovery.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal bounded integer")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    result, size = hashlib.sha256(), 0
    for chunk in json.JSONEncoder(
        sort_keys=True, separators=(",", ":"), allow_nan=False
    ).iterencode(value):
        raw = chunk.encode()
        size += len(raw)
        need(size <= MAX_BYTES, "proof-object byte cap")
        result.update(raw)
    return result.hexdigest()


def equal(left, right):
    need(canonical(left) == canonical(right), "complete typed composed replay differs")


def no_float(_value):
    raise ValueError("floating or nonfinite JSON")


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded acquisition bytes")
    return json.loads(
        raw, parse_float=no_float, parse_constant=no_float, object_pairs_hook=unique
    )


def body_check(payload):
    need(
        type(payload) is dict and type(payload.get("proof_object_sha256")) is str,
        "complete proof-object identity",
    )
    need(
        digest({k: v for k, v in payload.items() if k != "proof_object_sha256"})
        == payload["proof_object_sha256"],
        "complete proof-object body",
    )


def authenticate():
    raw, provenance = {}, []
    for freeze, pins in GROUPS:
        for name, expected in pins.items():
            path = name[1:] if name.startswith("@") else PREFIX + name
            need(len(expected) == 40, "literal exact blob identity")
            actual = subprocess.check_output(
                ["git", "rev-parse", f"{freeze}:{path}"], cwd=ROOT, text=True
            ).strip()
            need(actual == expected, "composed input source mismatch")
            size = int(
                subprocess.check_output(["git", "cat-file", "-s", actual], cwd=ROOT)
            )
            need(0 < size <= MAX_BYTES, "frozen source byte cap")
            data = subprocess.check_output(
                ["git", "cat-file", "blob", actual], cwd=ROOT
            )
            need(
                len(data) == size
                and hashlib.sha1(
                    b"blob " + str(size).encode() + b"\0" + data
                ).hexdigest()
                == actual,
                "actual Git source bytes",
            )
            current = ROOT / path
            need(current.stat().st_size <= MAX_BYTES, "working source byte cap")
            need(
                data.replace(b"\r\n", b"\n")
                == current.read_bytes().replace(b"\r\n", b"\n"),
                "frozen working source changed",
            )
            # The accepted cache is authenticated, not decoded or re-eliminated.
            if name != "resolution_stage5.cache.json":
                raw[name] = data
            provenance.append(
                {
                    "freeze": freeze,
                    "path": path,
                    "blob": actual,
                    "sha256_lf": hashlib.sha256(
                        data.replace(b"\r\n", b"\n")
                    ).hexdigest(),
                }
            )
    return raw, provenance


def compile_helper(raw, name):
    namespace = {
        "__name__": "composed_authenticated_" + name.replace(".", "_"),
        "__file__": str(HERE / name),
    }
    exec(compile(raw[name], str(HERE / name), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def check_inputs(raw):
    stage6 = read_json(raw["row_restricted_grade6.discovery.json"])
    coordinate = read_json(raw["streamed640_coordinate.discovery.json"])
    body_check(stage6)
    body_check(coordinate)
    need(
        stage6["schema"] == "actual-ternary-Chow-certified-original-row-resolution-v1",
        "accepted grade-six schema",
    )
    need(
        stage6["proof_object_sha256"]
        == "82804857869343db3371d42b7aa64bd5a71cecde7f02269a6df7ff05afb25d5c",
        "accepted grade-six exact proof",
    )
    need(
        coordinate["schema"] == "streamed640-exhaustive-coordinate-comparison-v1",
        "accepted coordinate schema",
    )
    need(
        coordinate["proof_object_sha256"]
        == "6811029c4411d48e1b9b33f5004576dddaf1757a61761c03cb40d88699850bc5",
        "accepted coordinate exact proof",
    )
    expected = {
        PREFIX + name: hashlib.sha256(raw[name].replace(b"\r\n", b"\n")).hexdigest()
        for name in (
            "STREAMED_RESOLUTION640_PREREGISTRATION.md",
            "STREAMED_RESOLUTION640_REPLAY.md",
            "streamed_resolution640.py",
        )
    }
    test = "tests/test_segre_hadamard_streamed640.py"
    expected[test] = hashlib.sha256(raw["@" + test].replace(b"\r\n", b"\n")).hexdigest()
    equal(coordinate["owned_sha256_lf"], expected)
    result = coordinate["result"]
    equal(
        {k: v for k, v in result.items() if k != "digests"},
        {
            "all_descriptors_addresses_weights_columns_compared": True,
            "domain_columns": 3775,
            "grade": 6,
            "kernel_or_rank_computed": False,
            "target_rows": 28600,
        },
    )
    maps = stage6["result"]
    integer(maps["stage"], 6, 6)
    need(
        maps["complete_resolution_constructed"] is False
        and maps["marked_basis_is_GL3_equivariant"] is False,
        "accepted lower maps only",
    )
    return stage6, coordinate


def checked_coefficient(value):
    need(
        type(value) is int and value != 0 and abs(value).bit_length() <= 4096,
        "literal nonzero bounded coefficient",
    )
    return value


def validate_map(helper, targets, columns, shifts):
    need(
        type(columns) is list and Counter(c["degree"] for c in columns) == shifts,
        "complete map degree counts",
    )
    total = 0
    for column in columns:
        degree = integer(column["degree"], 1, 7)
        weight = helper.exponent(column["weight"], 3)
        need(sum(weight) == 3 * degree, "map weight total")
        terms = column["terms"]
        need(type(terms) is list and terms, "actual nonzero polynomial column")
        seen = set()
        for term in terms:
            target = integer(term["generator"], 0, len(targets) - 1)
            exponent = helper.exponent(term["S_exponent"])
            checked_coefficient(term["coefficient"])
            need((target, exponent) not in seen, "duplicate polynomial coefficient")
            seen.add((target, exponent))
            need(
                0 < sum(exponent) == degree - targets[target]["degree"],
                "positive minimal grading",
            )
            need(
                helper.add(
                    helper.polynomial_weight(exponent), targets[target]["weight"]
                )
                == weight,
                "actual full weight homogeneity",
            )
            total += 1
    return {
        "columns": len(columns),
        "degree_counts": [[d, n] for d, n in sorted(shifts.items())],
        "nonzero_polynomial_terms": total,
    }


def compose(lower, upper):
    products, largest = 0, 0
    for column in upper:
        coefficients = {}
        for outer in column["terms"]:
            target = integer(outer["generator"], 0, len(lower) - 1)
            for inner in lower[target]["terms"]:
                exponent = tuple(
                    a + b
                    for a, b in zip(
                        outer["S_exponent"], inner["S_exponent"], strict=True
                    )
                )
                key = (inner["generator"], exponent)
                value = coefficients.get(key, 0) + checked_coefficient(
                    outer["coefficient"]
                ) * checked_coefficient(inner["coefficient"])
                largest = max(largest, abs(value).bit_length())
                need(largest <= 4096, "stored polynomial composition bit cap")
                if value:
                    coefficients[key] = value
                else:
                    coefficients.pop(key, None)
                products += 1
        need(not coefficients, "nonzero actual polynomial differential composition")
    return {
        "upper_columns": len(upper),
        "all_compositions_zero": True,
        "term_products": products,
        "maximum_stored_integer_bits": largest,
    }


def map_checks(helper, upstream, maps, presentation, degree4, final=False):
    f0, d1, d2, d3 = (
        maps[k] for k in ("F0_generators", "D1_columns", "D2_columns", "D3_columns")
    )
    equal(f0, presentation["result"]["generators"])
    equal(d1, presentation["result"]["D1_columns"])
    helper.validate_modules(f0, d1)
    need(
        hashlib.sha256(upstream.canonical(d2[:65]).encode()).hexdigest()
        == degree4["D2_degree_four_columns_sha256"],
        "actual acquired degree-four map digest",
    )
    d2_shape = validate_map(helper, d1, d2, {4: 65, 5: 20})
    d3_shape = validate_map(helper, d2, d3, {5: 11, 6: 17, **({7: 1} if final else {})})
    weights = {
        "D2_degree4": upstream.weight_check(d2[:65], d1, 3),
        "D2_degree5": upstream.weight_check(d2[65:], d1, 2),
    }
    for degree in (5, 6, *((7,) if final else ())):
        weights[f"D3_degree{degree}"] = upstream.weight_check(
            [c for c in d3 if c["degree"] == degree], f0, 7 - degree
        )
    for key, value in weights.items():
        equal(value, maps["complete_Tor_weight_checks"][key])
    return {
        "D2": d2_shape,
        "D3": d3_shape,
        "D1D2": compose(d1, d2),
        "D2D3": compose(d2, d3),
        "full_dual_weight_checks": weights,
    }


def algorithm_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in (Path(__file__), PREREG)
    }


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def source():
    raw, provenance = authenticate()
    stage6, coordinate = check_inputs(raw)
    modules = {
        name: compile_helper(raw, name)
        for name in (
            "streamed_resolution640.py",
            "resolution_stage5_cache.py",
            "full_resolution_replay.py",
            "resolution_replay.py",
        )
    }
    presentation = read_json(raw["presentation.verification.json"])
    degree4 = read_json(raw["resolution_degree4.discovery.json"])
    helper, upstream = (
        modules["resolution_replay.py"],
        modules["full_resolution_replay.py"],
    )
    maps = stage6["result"]
    checks = map_checks(helper, upstream, maps, presentation, degree4)
    lower_hashes = {
        key: digest(maps[key])
        for key in ("F0_generators", "D1_columns", "D2_columns", "D3_columns", "stages")
    }
    inherited = {
        "grade6_freeze": GRADE6,
        "grade6_proof_object_sha256": stage6["proof_object_sha256"],
        "coordinate_freeze": COORDINATES,
        "coordinate_proof_object_sha256": coordinate["proof_object_sha256"],
        "lower_map_hashes": lower_hashes,
        "lower_stage_rank_and_minimality_imported_as_proved_inputs": True,
        "lower_stage_elimination_replayed": False,
        "coordinate_acquisition_replayed": False,
    }
    context = SimpleNamespace(
        streamed=modules["streamed_resolution640.py"],
        verifier=modules["resolution_stage5_cache.py"],
        upstream=upstream,
        helper=helper,
        maps=maps,
        presentation=presentation,
        acquisition=degree4,
        inherited=inherited,
        prefix_checks=checks,
        coordinate=coordinate["result"],
        prior_stage_count=len(maps["stages"]),
        source_provenance={
            "bindings": provenance,
            "composed_algorithm": algorithm_bindings(),
            "proof_composition": inherited,
        },
        cache_provenance={
            "accepted_cache_freeze": "742d68b6d3c37191589b0e6463bc122af6d90f76",
            "fresh_cache_verification_performed": False,
        },
        stage6_provenance={
            "freeze": GRADE6,
            "proof_object_sha256": stage6["proof_object_sha256"],
            "exact_accepted_maps_consumed": True,
        },
    )
    return context


def prefix_result(context):
    return {
        "schema": "composed-grade7-prefix-only-v1",
        "source_provenance": context.source_provenance,
        "inherited_proofs": context.inherited,
        "fresh_polynomial_checks": context.prefix_checks,
        "grade7_constructed": False,
        "new_kernel_rank_claimed": False,
    }


def build(directory=DIRECTORY):
    context = source()
    maps = context.streamed.extend_stage7(context, directory)
    for key in ("F0_generators", "D1_columns", "D2_columns"):
        need(
            digest(maps[key]) == context.inherited["lower_map_hashes"][key],
            "accepted lower map changed",
        )
    need(
        digest(maps["D3_columns"][:28])
        == context.inherited["lower_map_hashes"]["D3_columns"],
        "accepted D3 prefix changed",
    )
    need(
        digest(maps["stages"][: context.prior_stage_count])
        == context.inherited["lower_map_hashes"]["stages"],
        "accepted lower witnesses changed",
    )
    final_checks = map_checks(
        context.helper,
        context.upstream,
        maps,
        context.presentation,
        context.acquisition,
        final=True,
    )
    payload = {
        "schema": "composed-certified-ternary-grade7-resolution-v1",
        "owned_sha256_lf": owned_bindings(),
        "source_provenance": context.source_provenance,
        "inherited_proofs": context.inherited,
        "prefix_polynomial_checks": context.prefix_checks,
        "final_polynomial_checks": final_checks,
        "accepted_coordinate_result": context.coordinate,
        "summary": context.upstream.summary(maps),
        "result": maps,
        "contract": {
            "grade7_fresh_full_original_row_certificates": True,
            "grade7_actual_old_quotient_constructed": True,
            "complete_minimal_resolution_by_pinned_global_proof": True,
            "lower_stage_elimination_replayed": False,
            "coordinate_acquisition_replayed": False,
            "old52_contract_completed": False,
            "old42_contract_completed": False,
            "old26_contract_completed": False,
            "old_producers_modified": False,
            "selected_row_and_column_cap": 640,
            "original_supported_row_cap": 4096,
            "guarded_stored_integer_bit_cap": 4096,
        },
    }
    payload["proof_object_sha256"] = digest(payload)
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--prefix-check", action="store_true")
    modes.add_argument("--scout", action="store_true")
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.prefix_check:
        payload = prefix_result(source())
        payload["owned_sha256_lf"] = owned_bindings()
        payload["proof_object_sha256"] = digest(payload)
        PREFIX_FIXTURE.write_text(canonical(payload) + "\n", encoding="utf-8")
        print(
            canonical(
                {
                    "status": "PREFIX_PASS",
                    "grade7_constructed": False,
                    "proof_object_sha256": payload["proof_object_sha256"],
                }
            )
        )
        return
    payload = build()
    if args.scout:
        print(canonical(payload))
        return
    if args.write:
        FIXTURE.write_text(canonical(payload) + "\n", encoding="utf-8")
    else:
        candidate = read_json(FIXTURE.read_bytes())
        body_check(candidate)
        equal(candidate, payload)
    print(
        canonical(
            {
                "status": "PASS",
                "summary": payload["summary"],
                "proof_object_sha256": payload["proof_object_sha256"],
                "old52_contract_completed": False,
                "old42_contract_completed": False,
            }
        )
    )


if __name__ == "__main__":
    main()
