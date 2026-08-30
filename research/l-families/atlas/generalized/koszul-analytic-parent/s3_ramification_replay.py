"""Exact source-character and ramification replay for the finite S3 family.

No field sweep, infinite arithmetic Euler product, or expanded Lie state.
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import json
import math
import subprocess
from fractions import Fraction
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/"
PINS = (
    (
        "4c04db224fedde5d589f05f7183e004a67441a9c",
        "koszul-analytic-parent/replay.py",
        "08090ed1e35c1d20ce2f65c710007406b7419771",
        "9bebf69c2f022897af9bd22dba2022b88799ff91ff8288da9e45743000aa9e63",
    ),
    (
        "4c04db224fedde5d589f05f7183e004a67441a9c",
        "koszul-analytic-parent/MATHEMATICS.md",
        "02d8cda2a0c50876d378eb1eeb29df85b3b096b3",
        "db2ca0196edab3f3c7ef52af3f6c30e61023f3a0080c1285d7fdb6c8844a915c",
    ),
    (
        "23ad35cc8010f72cf1df54f09eccb4dcba108879",
        "global-s3-prym/GLOBAL_S3_PRYM_SOURCE.md",
        "522aedf9ba87921112c23d7fe68d9983f90d396e",
        "966ce26a41caf4a99d36d807a290726ccdc812e6353d202a53b830c9119efa04",
    ),
)
OWNED = (
    "S3_RAMIFICATION_AND_GRADED_FAMILY.md",
    "S3_RAMIFICATION_REPLAY.md",
    "s3_ramification_replay.py",
    "tests/test_s3_ramification.py",
)
FIXTURE = HERE / "s3_ramification.verification.json"
CLASSES = ("e", "s", "c")
GROUP = tuple(itertools.permutations(range(3)))


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate_frozen() -> None:
    for freeze, name, blob, expected in PINS:
        resolved = subprocess.check_output(
            ["git", "rev-parse", freeze + ":" + PREFIX + name], cwd=ROOT, text=True
        ).strip()
        need(resolved == blob, "S3 source dependency blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(digest(frozen) == expected, "S3 source dependency hash mismatch")
        need(
            digest((HERE.parent / name).read_bytes()) == expected,
            "working S3 source dependency changed",
        )


authenticate_frozen()
SPEC = importlib.util.spec_from_file_location("frozen_s3_koszul", HERE / "replay.py")
need(SPEC is not None and SPEC.loader is not None, "cannot load authenticated parent")
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def permutation(value: object) -> tuple[int, ...]:
    need(isinstance(value, tuple) and len(value) == 3, "permutation triple required")
    for entry in value:
        R.integer(entry, 0, 2)
    need(set(value) == {0, 1, 2}, "not a permutation")
    return value


def parity(value: tuple[int, ...]) -> int:
    return (-1) ** sum(
        value[i] > value[j] for i in range(len(value)) for j in range(i + 1, len(value))
    )


def class_of(value: object) -> str:
    value = permutation(value)
    if value == (0, 1, 2):
        return "e"
    return "s" if parity(value) == -1 else "c"


def power_class(kind: str, exponent: int) -> str:
    need(kind in CLASSES, "unknown S3 class")
    R.integer(exponent, 0, 64)
    return "e" if kind == "e" or exponent % (2 if kind == "s" else 3) == 0 else kind


def source_matrices(value: object) -> tuple[tuple[tuple[int, ...], ...], ...]:
    value = permutation(value)
    full = tuple(tuple(int(i == value[j]) for j in range(3)) for i in range(3))
    # Basis e0-e2,e1-e2 of the augmentation kernel. Coordinates are its first two entries.
    standard = tuple(tuple(full[i][j] - full[i][2] for j in range(2)) for i in range(2))
    return standard, full


def multiply(left: list[int], right: list[int], degree: int) -> list[int]:
    R.integer(degree, 0, 24)
    need(len(left) <= 25 and len(right) <= 25, "bounded polynomials required")
    need(
        all(isinstance(x, int) and not isinstance(x, bool) for x in left + right),
        "integer polynomial required",
    )
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += a * b
    return out


def determinant_polynomial(matrix: tuple[tuple[int, ...], ...]) -> list[int]:
    size = len(matrix)
    R.integer(size, 1, 3)
    need(all(len(row) == size for row in matrix), "square source matrix required")
    need(
        all(
            isinstance(x, int) and not isinstance(x, bool)
            for row in matrix
            for x in row
        ),
        "integer source matrix required",
    )
    out = [0] * (size + 1)
    for perm in itertools.permutations(range(size)):
        term = [parity(perm)]
        for row, col in enumerate(perm):
            term = multiply(term, [int(row == col), -matrix[row][col]], size)
        out = [a + b for a, b in zip(out, term, strict=True)]
    return out


def inverse_series(sequence: list[int], degree: int) -> list[int]:
    R.integer(degree, 0, 24)
    need(
        1 <= len(sequence) <= 25 and sequence[0] == 1,
        "normalized bounded integer series required",
    )
    need(
        all(isinstance(x, int) and not isinstance(x, bool) for x in sequence),
        "integer series required",
    )
    out = [1] + [0] * degree
    for n in range(1, degree + 1):
        out[n] = -sum(
            sequence[j] * out[n - j] for j in range(1, min(n + 1, len(sequence)))
        )
    return out


@cache
def source_sequences(degree: int) -> dict[str, tuple[int, ...]]:
    R.integer(degree, 0, 24)
    found = {}
    for perm in GROUP:
        a, b = source_matrices(perm)
        ha = inverse_series(determinant_polynomial(a), degree)
        hb = inverse_series(determinant_polynomial(b), degree)
        row = tuple(x * y for x, y in zip(ha, hb, strict=True))
        kind = class_of(perm)
        if kind in found:
            need(found[kind] == row, "source character is not a class function")
        found[kind] = row
    expected = {
        "e": tuple((n + 1) * math.comb(n + 2, 2) for n in range(degree + 1)),
        "s": tuple(n // 2 + 1 if n % 2 == 0 else 0 for n in range(degree + 1)),
        "c": tuple(int(n % 3 == 0) for n in range(degree + 1)),
    }
    need(
        found == expected,
        "matrix-defined symmetric characters disagree with closed forms",
    )
    return found


def irreducibles(
    characters: tuple[int, int, int], positive: bool = True
) -> tuple[int, int, int]:
    need(
        isinstance(characters, tuple) and len(characters) == 3,
        "three source characters required",
    )
    need(
        all(isinstance(x, int) and not isinstance(x, bool) for x in characters),
        "integral characters required",
    )
    need(isinstance(positive, bool), "explicit positivity flag required")
    d, t, c = characters
    values = (
        Fraction(d + 3 * t + 2 * c, 6),
        Fraction(d - 3 * t + 2 * c, 6),
        Fraction(d - c, 3),
    )
    need(
        all(x.denominator == 1 for x in values), "not an integral S3 virtual character"
    )
    result = tuple(int(x) for x in values)
    need(not positive or min(result) >= 0, "not a genuine S3 character")
    return result


def fusion(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[int, int, int]:
    for vector in (left, right):
        need(
            isinstance(vector, tuple) and len(vector) == 3, "S3 fusion vector required"
        )
        need(
            all(isinstance(x, int) and not isinstance(x, bool) for x in vector),
            "integral fusion vector required",
        )
    a, b, c = left
    x, y, z = right
    return a * x + b * y + c * z, b * x + a * y + c * z, c * x + c * y + (a + b + c) * z


def source_rows(degree: int) -> list[dict[str, object]]:
    seq = source_sequences(degree)
    out = []
    for n in range(degree + 1):
        d, t, r = (seq[k][n] for k in CLASSES)
        a, b, c = irreducibles((d, t, r))
        finite_codim = d - (d + t) // 2
        infinite_codim = d - (d + 2 * r) // 3
        conductor = 4 * finite_codim + infinite_codim
        h1 = conductor - 2 * d + 2 * a
        need(h1 == d - t == 2 * (b + c), "global conductor/cohomology ledger failed")
        need(
            a + c == (d + t) // 2 and a + b == (d + 2 * r) // 3,
            "inertia multiplicities disagree",
        )
        out.append(
            {
                "grade": n,
                "characters_e_s_c": [d, t, r],
                "multiplicities_1_sign_std": [a, b, c],
                "finite_branch_invariant_dimension": a + c,
                "infinite_invariant_dimension": a + b,
                "infinite_nonsplit_frobenius_trace": a - b,
                "tame_conductor_degree": conductor,
                "h0_h1_h2_dimensions": [a, h1, a],
                "global_L_exponents_ZP1_PD_PE": [a, b, c],
            }
        )
    return out


def fusion_control(degree: int) -> dict[str, object]:
    sequences = source_sequences(degree)
    inverse = {
        kind: inverse_series(list(row), degree) for kind, row in sequences.items()
    }
    native = [
        irreducibles(tuple(sequences[k][n] for k in CLASSES)) for n in range(degree + 1)
    ]
    signed_dual = [
        irreducibles(tuple(inverse[k][n] for k in CLASSES), False)
        for n in range(degree + 1)
    ]
    for n, vector in enumerate(signed_dual):
        need(
            min((-1) ** n * x for x in vector) >= 0,
            "quadratic dual is not a genuine source representation",
        )
        value = tuple(
            sum(fusion(native[j], signed_dual[n - j])[k] for j in range(n + 1))
            for k in range(3)
        )
        need(
            value == ((1, 0, 0) if n == 0 else (0, 0, 0)),
            "full fusion Koszul inverse failed",
        )
    for n in range(1, min(degree, 3) + 1):
        need(
            (-1) ** n * inverse["e"][n] == R.source_grade(n)[0],
            "source quotient dimension disagrees with dual complex",
        )
    return {
        "through_grade": degree,
        "signed_dual_irreducible_multiplicities": [list(v) for v in signed_dual],
        "full_fusion_inverse": True,
    }


def native_low_lie() -> list[list[int]]:
    out = []
    for n in (1, 2, 3):
        weights = R.source_grade(n)[2]
        transposition = sum((-1) ** (w[1] + w[4]) for w in weights)
        # Exact Q(omega) evaluation; omega^2=-1-omega, no approximate roots.
        constant = omega = 0
        for w in weights:
            exponent = (w[0] + 2 * w[1] + w[3] + 2 * w[4]) % 3
            constant += (1, 0, -1)[exponent]
            omega += (0, 1, -1)[exponent]
        need(omega == 0, "rational S3 character retained an omega coefficient")
        row = [len(weights), transposition, constant]
        need(
            row == ([6, 0, 0], [3, 1, 0], [2, 0, -1])[n - 1],
            "native quotient Lie character disagrees",
        )
        out.append(row)
    return out


def invariant_character(characters: tuple[int, int, int], inertia: int) -> int:
    R.integer(inertia, 2, 3)
    d, s, c = characters
    value = Fraction(d + s, 2) if inertia == 2 else Fraction(d + 2 * c, 3)
    need(value.denominator == 1, "nonintegral inertia invariant multiplicity")
    return int(value)


def ramification_control(inertia: int) -> dict[str, object]:
    R.integer(inertia, 2, 3)
    seq = source_sequences(2)
    actual = [
        invariant_character(tuple(seq[k][n] for k in CLASSES), inertia)
        for n in range(3)
    ]
    m1, m2, _ = native_low_lie()
    lie = [invariant_character(tuple(row), inertia) for row in (m1, m2)]
    fake_degree2 = math.comb(lie[0] + 1, 2) - lie[1]
    naive_input = [1, 2, 3] if inertia == 2 else [1, 0, 0]
    need(actual[1] != naive_input[1], "naive invariant-input counterfeit survived")
    need(
        actual[1] == lie[0] and actual[2] != fake_degree2,
        "invariant-Lie counterfeit was not separated in degree two",
    )
    quadratic_dual2 = tuple(inverse_series(list(seq[k]), 2)[2] for k in CLASSES)
    b2inv = invariant_character(quadratic_dual2, inertia)
    middle_tensor = invariant_character(tuple(x * x for x in m1), inertia)
    full_euler = actual[2] - middle_tensor + b2inv
    dropped_euler = actual[2] - lie[0] ** 2 + b2inv
    need(full_euler == 0 and dropped_euler != 0, "tensor-sector obstruction was lost")
    gap = actual[2] - math.comb(actual[1] + 1, 2)
    need(gap > 0, "failure of degree-one generation was lost")
    return {
        "inertia_order": inertia,
        "actual_invariant_R_dimensions_0_1_2": actual,
        "naive_input_invariant_dimensions_0_1_2": naive_input,
        "invariant_Lie_dimensions_1_2": lie,
        "invariant_Lie_fake_degree2": fake_degree2,
        "minimum_new_degree2_generators": gap,
        "full_invariant_Koszul_degree2_terms": [actual[2], middle_tensor, b2inv],
        "full_invariant_Koszul_degree2_Euler": full_euler,
        "dropped_tensor_sector_Euler": dropped_euler,
    }


def field_size(q: int) -> int:
    R.integer(q, 5, 4096)
    divisor = next((d for d in range(2, math.isqrt(q) + 1) if q % d == 0), q)
    need(divisor > 3, "source field characteristic must exceed three")
    remaining = q
    while remaining % divisor == 0:
        remaining //= divisor
    need(remaining == 1, "field size must be a prime power")
    return q


def infinity_trace(q: int, degree: int) -> list[int]:
    q = field_size(q)
    rows = source_rows(degree)
    return [
        row["infinite_invariant_dimension"]
        if q % 3 == 1
        else row["infinite_nonsplit_frobenius_trace"]
        for row in rows
    ]


def local_factors(
    grade: int, place: str, q: int = 5
) -> tuple[tuple[tuple[int, ...], int], ...]:
    R.integer(grade, 0, 6)
    need(
        place in ("e", "s", "c", "finite_branch", "infinity"),
        "unknown arithmetic place type",
    )
    q = field_size(q)
    row = source_rows(grade)[grade]
    a, b, c = row["multiplicities_1_sign_std"]
    d = row["characters_e_s_c"][0]
    if place == "e":
        return (((1, -1), d),)
    if place == "s":
        return (((1, -1), a + c), ((1, 1), b + c))
    if place == "c":
        return (((1, -1), a + b), ((1, 1, 1), c))
    if place == "finite_branch":
        return (((1, -1), a + c),)
    return (((1, -1), a), ((1, -1 if q % 3 == 1 else 1), b))


def local_denominator(grade: int, place: str, q: int = 5, degree: int = 6) -> list[int]:
    R.integer(degree, 1, 6)
    out = [1] + [0] * degree
    for polynomial, exponent in local_factors(grade, place, q):
        for _ in range(exponent):
            out = multiply(out, list(polynomial), degree)
    return out


def determinant_trace_check(grade: int, place: str, q: int) -> dict[str, object]:
    denominator = local_denominator(grade, place, q)
    row = source_rows(grade)[grade]
    a, b, c = row["multiplicities_1_sign_std"]
    source = source_sequences(grade)
    traces = []
    for power in range(1, 7):
        if place in CLASSES:
            traces.append(source[power_class(place, power)][grade])
        elif place == "finite_branch":
            traces.append(a + c)
        else:
            traces.append(a + b * ((1 if q % 3 == 1 else -1) ** power))
    # Newton identity for det(1-zF), independent of its irreducible factorization.
    for n in range(1, 7):
        need(
            n * denominator[n]
            == -sum(traces[j - 1] * denominator[n - j] for j in range(1, n + 1)),
            "arithmetic determinant failed Frobenius-power trace check",
        )
    return {
        "grade": grade,
        "place_type": place,
        "field_size": q,
        "denominator_through_degree6": denominator,
        "frobenius_power_traces_1_to_6": traces,
    }


def build_payload() -> dict[str, object]:
    authenticate_frozen()
    R.authenticate()
    return {
        "schema": "koszul-s3-ramification-finite-family-v1",
        "provenance": {
            "pins": [list(pin) for pin in PINS],
            "owned_sha256_lf": {
                name: digest((HERE / name).read_bytes()) for name in OWNED
            },
        },
        "primitive_source": {
            "group": "S3 on three letters",
            "input_V": "augmentation kernel in permutation_3",
            "input_W": "permutation_3",
            "algebra": "direct sum Sym^n V tensor Sym^n W",
            "grade_cap": 24,
            "local_determinant_grade_cap": 6,
            "source_Lie_tensor_degree_cap": 3,
        },
        "source_matrices": [
            {
                "permutation": list(perm),
                "class": class_of(perm),
                "standard_and_permutation_matrices": [
                    [list(row) for row in matrix] for matrix in source_matrices(perm)
                ],
            }
            for perm in GROUP
        ],
        "source_sequences": {
            kind: list(seq) for kind, seq in source_sequences(24).items()
        },
        "native_Lie_characters_M1_M2_M3": native_low_lie(),
        "finite_grade_global_ledgers": source_rows(24),
        "full_fusion_complex": fusion_control(24),
        "ramification_counterfeits": [ramification_control(i) for i in (2, 3)],
        "infinity_Frobenius_controls": [
            {"field_size": q, "graded_stalk_traces": infinity_trace(q, 12)}
            for q in (5, 7, 25, 49, 125)
        ],
        "all_local_factor_types": [
            determinant_trace_check(n, place, q)
            for n in (0, 1, 2, 4, 6)
            for q in (5, 7)
            for place in (*CLASSES, "finite_branch", "infinity")
        ],
        "not_machine_proved": [
            "exactness of the canonical Koszul complex in all grades",
            "all-grade sheaf and trace-formula theorem",
            "Weil weights and duality",
            "global analytic completion of an infinite-grade family",
        ],
        "no_infinite_arithmetic_Euler_product": True,
    }


def check_payload(candidate: object) -> None:
    need(
        json.dumps(candidate, sort_keys=True)
        == json.dumps(build_payload(), sort_keys=True),
        "S3 ramification fixture differs from authenticated complete replay",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    if args.write:
        FIXTURE.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        need(
            json.dumps(json.loads(FIXTURE.read_text(encoding="utf-8")), sort_keys=True)
            == json.dumps(payload, sort_keys=True),
            "S3 ramification fixture differs from complete replay",
        )
    print("PASS S3 source ramification and finite-grade global family exact replay")


if __name__ == "__main__":
    main()
