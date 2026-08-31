"""Complete ternary-cube Tor characters from frozen source and exact duality."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "a895f47628b0bc7c7ee5e0392df2f79c24166f92"
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = (
    ("MATHEMATICS.md", "bbd847461b4955a93b4533fa687cdd8724e2347c"),
    ("replay.py", "795566f6ec91bf68dd7ee2f77450e73afd131032"),
    ("verification.json", "310ffc95cb6eaf19281de52dd18d2f2884bc0f49"),
)
OWNED = (
    "TERNARY_CUBE_TOR_CHARACTERS.md",
    "TOR_CHARACTER_REPLAY.md",
    "tor_character_replay.py",
)
TEST = ROOT / "tests/test_segre_hadamard_tor_characters.py"
FIXTURE = HERE / "tor_characters.verification.json"
CLASSES = ("identity", "transposition", "three_cycle")
IRREPS = {"trivial": (1, 1, 1), "sign": (1, -1, 1), "standard": (2, 0, -1)}
LOWER = {
    (0, 0): (((0, 0, 0), "trivial"),),
    (0, 1): (((2, 1, 0), "standard"), ((1, 1, 1), "sign")),
    (0, 2): (((2, 2, 2), "trivial"), ((3, 3, 0), "sign")),
    (1, 2): (((4, 1, 1), "standard"),),
    (1, 3): (
        ((5, 2, 2), "trivial"),
        ((5, 2, 2), "standard"),
        ((5, 3, 1), "sign"),
        ((4, 3, 2), "sign"),
    ),
}


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, label="integer"):
    need(type(value) is int and low <= value <= high, f"{label} outside declared cap")
    return value


def canonical_bytes(path):
    return path.read_bytes().replace(b"\r\n", b"\n")


def blob_id(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def authenticate_source():
    for name, expected in PINS:
        revision = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"], cwd=ROOT, text=True
        ).strip()
        need(revision == expected, "frozen source Git object mismatch")
        need(
            blob_id(canonical_bytes(HERE / name)) == expected,
            "working source bytes mismatch",
        )
    return json.loads((HERE / "verification.json").read_text(encoding="utf-8"))


def partition(value):
    need(isinstance(value, (tuple, list)) and len(value) == 3, "GL3 partition required")
    for part in value:
        integer(part, 0, 7, "partition part")
    need(value[0] >= value[1] >= value[2], "partition order")
    return tuple(value)


@lru_cache(maxsize=64)
def _schur_weights(lam):
    result = Counter()
    for mu1 in range(lam[1], lam[0] + 1):
        for mu2 in range(lam[2], lam[1] + 1):
            for nu in range(mu2, mu1 + 1):
                result[(nu, mu1 + mu2 - nu, sum(lam) - mu1 - mu2)] += 1
    return tuple(sorted(result.items()))


def schur_weights(lam):
    return dict(_schur_weights(partition(lam)))


def dual_partition(lam):
    a, b, c = partition(lam)
    return (7 - c, 7 - b, 7 - a)


def full_table():
    result = dict(LOWER)
    for (i, j), terms in LOWER.items():
        target = (3 - i, 7 - j)
        need(target not in result, "duality table unexpectedly overlaps")
        result[target] = tuple((dual_partition(lam), irrep) for lam, irrep in terms)
    return result


def weights_of_terms(terms):
    result = {}
    for lam, irrep in terms:
        need(irrep in IRREPS, "unknown factor-permutation representation")
        for weight, multiplicity in schur_weights(lam).items():
            row = result.setdefault(weight, [0, 0, 0])
            for index, trace in enumerate(IRREPS[irrep]):
                row[index] += multiplicity * trace
    return result


def compositions(total):
    integer(total, 0, 30, "weight degree")
    return [
        (a, b, total - a - b) for a in range(total + 1) for b in range(total - a + 1)
    ]


def check_primitive_panels(source):
    panels = [
        row
        for row in source["result"]["literal_koszul_sources"]
        if (row["dimension"], row["factor_count"]) == (3, 3)
    ]
    need(
        sorted(row["grade"] for row in panels) == [1, 2, 3],
        "complete primitive cube coverage required",
    )
    checked = []
    for panel in panels:
        j = panel["grade"]
        need(
            panel["source_d_squared_zero"] is True,
            "source chain not authenticated as a complex",
        )
        rows = panel["homology_weight_rows"]
        need(
            [tuple(row["weight"]) for row in rows] == compositions(3 * j),
            "source weight coverage/order differs",
        )
        for i in range(j + 1):
            expected = weights_of_terms(LOWER.get((i, j), ()))
            totals = [0, 0, 0]
            for row in rows:
                actual = row["homology"][i]
                need(set(actual) == set(CLASSES), "factor-class coverage differs")
                vector = [actual[key] for key in CLASSES]
                need(
                    all(type(value) is int for value in vector),
                    "exact source class trace required",
                )
                need(
                    vector == expected.get(tuple(row["weight"]), [0, 0, 0]),
                    "source weight/class disagrees with Schur table",
                )
                totals = [a + b for a, b in zip(totals, vector, strict=True)]
            need(
                totals
                == [panel["homology_factor_class_traces"][i][key] for key in CLASSES],
                "source total trace mismatch",
            )
            checked.append(
                {"homological_degree": i, "internal_degree": j, "class_traces": totals}
            )
    return checked


def table_record(table):
    rows = []
    for (i, j), terms in sorted(table.items()):
        character = weights_of_terms(terms)
        totals = [sum(row[k] for row in character.values()) for k in range(3)]
        need(all(sum(lam) == 3 * j for lam, _ in terms), "wrong GL central degree")
        rows.append(
            {
                "homological_degree": i,
                "internal_degree": j,
                "Schur_times_factor_irrep": [
                    {"partition": list(lam), "S3_irrep": irrep} for lam, irrep in terms
                ],
                "class_traces": totals,
                "complete_weight_character": [
                    {"weight": list(weight), "class_traces": vector}
                    for weight, vector in sorted(character.items())
                ],
            }
        )
    return rows


def check_duality(table):
    for (i, j), terms in table.items():
        source = weights_of_terms(terms)
        dual = weights_of_terms(table[(3 - i, 7 - j)])
        reflected = {
            tuple(7 - a for a in weight): vector for weight, vector in source.items()
        }
        need(dual == reflected, "canonical GL/S3 Tor duality mismatch")
    return {
        "determinant_twist": 7,
        "factor_permutation_sign_twist": False,
        "all_weights_checked": True,
    }


def multiply(a, b, cut):
    answer = [0] * (cut + 1)
    for i, x in enumerate(a[: cut + 1]):
        for j, y in enumerate(b[: cut + 1 - i]):
            answer[i + j] += x * y
    return answer


def monomial(values, weight):
    result = 1
    for a, n in zip(values, weight, strict=True):
        result *= a**n
    return result


def complete(values, grade):
    return sum(monomial(values, weight) for weight in compositions(grade))


def euler_control(values):
    need(
        isinstance(values, (list, tuple)) and len(values) == 3,
        "three diagonal values required",
    )
    need(
        all(type(a) is int and a != 0 for a in values),
        "nonzero integer diagonal values required",
    )
    need(all(abs(a) <= 7 for a in values), "diagonal size cap")
    cut = 10
    denominator = [1] + [0] * cut
    for weight in compositions(3):
        denominator = multiply(denominator, [1, -monomial(values, weight)], cut)
    table = full_table()
    rows = []
    for k, name in enumerate(CLASSES):
        euler = [0] * (cut + 1)
        for (i, j), terms in table.items():
            euler[j] += (-1) ** i * sum(
                monomial(values, weight) * traces[k]
                for weight, traces in weights_of_terms(terms).items()
            )
        series = []
        for n in range(cut + 1):
            h = complete(values, n)
            if name == "identity":
                series.append(h**3)
            elif name == "transposition":
                series.append(h * complete(tuple(a**2 for a in values), n))
            else:
                series.append(complete(tuple(a**3 for a in values), n))
        need(
            euler == multiply(denominator, series, cut),
            "actual tensor-cycle Euler identity failed",
        )
        rows.append(
            {
                "factor_class": name,
                "numerator": euler[:8],
                "tail_through_degree10_zero": not any(euler[8:]),
            }
        )
    return {"diagonal": list(values), "classes": rows}


def normalization_sector(table):
    actual = {
        (i, j): tuple(lam for lam, irrep in terms if irrep == "trivial")
        for (i, j), terms in table.items()
    }
    actual = {key: value for key, value in actual.items() if value}
    expected = {
        (0, 0): ((0, 0, 0),),
        (0, 2): ((2, 2, 2),),
        (1, 3): ((5, 2, 2),),
        (2, 4): ((5, 5, 2),),
        (3, 5): ((5, 5, 5),),
        (3, 7): ((7, 7, 7),),
    }
    need(actual == expected, "classical normalization-sector comparison differs")
    return [
        {"i": i, "j": j, "partitions": [list(lam) for lam in terms]}
        for (i, j), terms in sorted(actual.items())
    ]


def build_payload():
    source = authenticate_source()
    table = full_table()
    primitive = check_primitive_panels(source)
    record = table_record(table)
    ranks = [
        sum(row["class_traces"][0] for row in record if row["homological_degree"] == i)
        for i in range(4)
    ]
    need(ranks == [29, 85, 85, 29], "total free ranks changed")
    return {
        "schema": "segre-hadamard-ternary-cube-Tor-characters/v1",
        "source": {"freeze": FREEZE, "pins": [list(row) for row in PINS]},
        "owned_sha256_lf": {
            name: hashlib.sha256(canonical_bytes(HERE / name)).hexdigest()
            for name in OWNED
        },
        "test_sha256_lf": hashlib.sha256(canonical_bytes(TEST)).hexdigest(),
        "primitive_weight_character_comparison": primitive,
        "complete_Tor_table": record,
        "total_free_ranks": ranks,
        "duality": check_duality(table),
        "classical_normalization_comparison": normalization_sector(table),
        "actual_tensor_cycle_Euler_controls": [
            euler_control(values)
            for values in ((2, 3, 5), (1, 1, 1), (1, -1, 2), (2, 2, 3))
        ],
        "all_Tor_characters_determined": True,
        "minimal_differential_matrices_constructed": False,
        "new_large_chain_elimination_performed": False,
        "arithmetic_S3_source_identified": False,
    }


def serialized(payload):
    return json.dumps(payload, sort_keys=True, indent=2) + "\n"


def check_payload(candidate):
    need(
        serialized(candidate) == serialized(build_payload()),
        "payload differs from complete source character replay",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = serialized(build_payload())
    if args.write:
        FIXTURE.write_text(data, encoding="utf-8", newline="\n")
    else:
        need(FIXTURE.exists(), "missing Tor-character fixture")
        need(
            FIXTURE.read_text(encoding="utf-8") == data, "Tor-character fixture differs"
        )
    print(
        json.dumps(
            {
                "status": "PASS",
                "nonzero_Tor_bidegrees": 10,
                "free_ranks": [29, 85, 85, 29],
            }
        )
    )


if __name__ == "__main__":
    main()
