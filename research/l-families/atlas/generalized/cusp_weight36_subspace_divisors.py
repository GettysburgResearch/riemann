"""Exact bounded SD controls; no numerical period, prime phase, or zero evaluation."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized"
STEM = "cusp_weight36_subspace_divisors"
BASE = "ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf"
HC = "14fa39a02267c043ac27cd68ef7157ef77afe83b"
HCSTEM = "cusp_flag_hecke_source_concentration"
REVIEW = "0f29fd2d687c57402a14723dde2bc2b7e74fa317"
CAPS = {
    "q_order": 18,
    "dirichlet_order": 36,
    "matrix_dimension": 3,
    "polynomial_degree": 3,
    "polynomial_terms": 256,
    "subspace_count": 27,
    "target_attempts": 729,
    "integer_bits": 4096,
    "work": 8000000,
    "json_bytes": 3000000,
    "json_nodes": 150000,
    "json_depth": 24,
    "container_length": 1024,
    "string_length": 4096,
}
PINS = (
    (HC, f"{DIR}/CUSP_FLAG_HECKE_SOURCE_CONCENTRATION.md"),
    (HC, f"{DIR}/{HCSTEM}.py"),
    (HC, f"{DIR}/{HCSTEM}.json"),
    (HC, f"tests/test_{HCSTEM}.py"),
    (BASE, f"{DIR}/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md"),
    (
        "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        f"{DIR}/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
    ),
    (REVIEW, f"{DIR}/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY_AUDIT_EC5BDD9B.md"),
)
ARTIFACTS = (
    f"{DIR}/CUSP_WEIGHT36_SUBSPACE_DIVISORS.md",
    f"{DIR}/{STEM}.py",
    f"{DIR}/{STEM}.sources.json",
    f"tests/test_{STEM}.py",
)
PRIMARY = (
    (
        "BT",
        "https://msp.org/ant/2014/8-9/ant-v8-n9-p01-s.pdf",
        "Theorem1.2 hypotheses; Proposition3.1; pp2040-2041",
    ),
    (
        "BT-correction",
        "https://msp.org/ant/2014/8-9/ant-v8-n9-x01-Correction-ZerosOfLFunctions.pdf",
        "both pages",
    ),
    (
        "GJ",
        "https://www.numdam.org/article/ASENS_1978_4_11_4_471_0.pdf",
        "p472; Theorem9.3 p534",
    ),
    (
        "R",
        "https://www.maths.tcd.ie/EMIS/journals/Annals/152_1/ramak.pdf",
        "Proposition2.3.1 and TheoremM pp53-54",
    ),
    ("Nullstellensatz", "https://stacks.math.columbia.edu/tag/00FV", "Theorem10.34.1"),
)
EXPECTED_P = [-1467625047588864, -59208339456, -139656, 1]
EXPECTED_DISC = 606037485049196709344808901017600
EXPECTED_OPPOSITE = -1113023000511109845739295110772461437714432000000
ROOT_INTERVALS = ((-165110, -165109), (-26809, -26808), (331573, 331574))


class Rejected(ValueError):
    """Malformed, over-budget, or unauthenticated data."""


def need(ok: bool, why: str) -> None:
    if not ok:
        raise Rejected(why)


def integer(n: object, low: int | None = None, high: int | None = None) -> int:
    need(type(n) is int, "integer type")
    need(abs(n).bit_length() <= CAPS["integer_bits"], "integer bits")
    need(low is None or n >= low, "integer lower")
    need(high is None or n <= high, "integer upper")
    return n


def rational(x: object) -> F:
    need(type(x) is F, "rational type")
    integer(x.numerator)
    integer(x.denominator, 1)
    return x


def wire(x: F) -> list[int]:
    rational(x)
    return [x.numerator, x.denominator]


class Budget:
    def __init__(self, limit: int = CAPS["work"]):
        self.limit = integer(limit, 1, CAPS["work"])
        self.used = 0

    def charge(self, n: int = 1) -> None:
        integer(n, 0, CAPS["work"])
        need(self.used + n <= self.limit, "work cap")
        self.used += n


def lf(raw: bytes) -> bytes:
    return raw.replace(b"\r\n", b"\n")


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value: object) -> bytes:
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    ).encode("ascii")


def typed(value: object, depth: int = 0, nodes: list[int] | None = None) -> None:
    if nodes is None:
        nodes = [0]
    nodes[0] += 1
    need(
        nodes[0] <= CAPS["json_nodes"] and depth <= CAPS["json_depth"], "JSON tree cap"
    )
    if type(value) is int:
        integer(value)
    elif type(value) is str:
        need(len(value) <= CAPS["string_length"], "string cap")
    elif type(value) is list:
        need(len(value) <= CAPS["container_length"], "list cap")
        for v in value:
            typed(v, depth + 1, nodes)
    elif type(value) is dict:
        need(len(value) <= CAPS["container_length"], "dict cap")
        for key, v in value.items():
            need(type(key) is str, "key type")
            typed(key, depth + 1, nodes)
            typed(v, depth + 1, nodes)
    else:
        raise Rejected("bool/float/null/foreign type")


def pairs(items: list[tuple[str, object]]) -> dict:
    out = {}
    for key, value in items:
        need(key not in out, "duplicate JSON key")
        out[key] = value
    return out


def decode(raw: bytes) -> object:
    need(type(raw) is bytes and len(raw) <= CAPS["json_bytes"], "JSON byte cap")
    try:
        out = json.loads(
            raw,
            object_pairs_hook=pairs,
            parse_constant=lambda _: (_ for _ in ()).throw(Rejected("nonfinite JSON")),
        )
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise Rejected("invalid JSON") from exc
    typed(out)
    return out


def file_bytes(path: Path) -> bytes:
    need(path.stat().st_size <= CAPS["json_bytes"], "file byte cap")
    raw = path.read_bytes()
    need(len(raw) <= CAPS["json_bytes"], "read byte cap")
    return raw


def git_bytes(commit: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "--no-replace-objects", "show", commit + ":" + path],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    need(result.returncode == 0, "frozen source unavailable")
    need(len(result.stdout) <= CAPS["json_bytes"], "source byte cap")
    return result.stdout


def manifest() -> dict:
    rows = []
    for commit, path in PINS:
        raw = git_bytes(commit, path)
        rows.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": hashlib.sha1(
                    b"blob " + str(len(raw)).encode() + b"\0" + raw
                ).hexdigest(),
                "sha256_lf": digest(lf(raw)),
            }
        )
    return {
        "schema": "weight36-subspace-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": rows,
        "primary_references": [
            {"id": a, "url": b, "passage": c} for a, b, c in PRIMARY
        ],
        "remote_bytes": "not_authenticated_by_offline_git_checker",
    }


def authenticate() -> None:
    need(
        decode(file_bytes(ROOT / DIR / f"{STEM}.sources.json")) == manifest(),
        "source drift",
    )


def parity(permutation: tuple[int, ...]) -> int:
    return (-1) ** sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )


def determinant(matrix: list[list[F]], budget: Budget) -> F:
    need(type(matrix) is list, "matrix type")
    n = integer(len(matrix), 1, 6)
    need(all(type(row) is list and len(row) == n for row in matrix), "square matrix")
    for row in matrix:
        for value in row:
            rational(value)
    # At most six by six: exact elimination, not factorial enumeration.
    a = [row.copy() for row in matrix]
    out = F(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return F(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            out = -out
        value = a[j][j]
        out = rational(out * value)
        for i in range(j + 1, n):
            multiplier = rational(a[i][j] / value)
            for k in range(j, n):
                budget.charge()
                a[i][k] = rational(a[i][k] - multiplier * a[j][k])
    return out


def trim(poly: list[F]) -> list[F]:
    need(type(poly) is list and 1 <= len(poly) <= 7, "univariate degree cap")
    for x in poly:
        rational(x)
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def remainder(a: list[F], b: list[F], budget: Budget) -> list[F]:
    a, b = trim(a.copy()), trim(b.copy())
    need(b != [0], "zero polynomial divisor")
    while a != [0] and len(a) >= len(b):
        shift, scalar = len(a) - len(b), a[-1] / b[-1]
        for i, value in enumerate(b):
            budget.charge()
            a[i + shift] = rational(a[i + shift] - scalar * value)
        trim(a)
    return a


def peval(poly: list[F], x: F) -> F:
    rational(x)
    value = F(0)
    for coefficient in reversed(trim(poly.copy())):
        value = rational(value * x + coefficient)
    return value


def sturm(poly: list[F], budget: Budget) -> list[list[F]]:
    poly = trim(poly.copy())
    need(len(poly) >= 2, "nonconstant polynomial")
    sequence = [poly, [rational(i * poly[i]) for i in range(1, len(poly))]]
    while sequence[-1] != [0]:
        r = remainder(sequence[-2], sequence[-1], budget)
        if r == [0]:
            break
        sequence.append([-v for v in r])
    return sequence


def variations(sequence: list[list[F]], x: F) -> int:
    values = [peval(poly, x) for poly in sequence]
    signs = [1 if value > 0 else -1 for value in values if value]
    return sum(a != b for a, b in itertools.pairwise(signs))


def resultant(a: list[F], b: list[F], budget: Budget) -> F:
    a, b = trim(a.copy()), trim(b.copy())
    m, n = len(a) - 1, len(b) - 1
    need(1 <= m <= 3 and 1 <= n <= 3, "resultant degrees")
    rows = []
    for shift in range(n):
        rows.append([F(0)] * shift + list(reversed(a)) + [F(0)] * (n - 1 - shift))
    for shift in range(m):
        rows.append([F(0)] * shift + list(reversed(b)) + [F(0)] * (m - 1 - shift))
    return determinant(rows, budget)


def native_source(budget: Budget) -> dict:
    path = f"{DIR}/{HCSTEM}.py"
    raw = git_bytes(HC, path)
    ns = {"__file__": str(ROOT / path), "__name__": "frozen_hc_dependency"}
    exec(compile(raw, ns["__file__"], "exec"), ns)  # noqa: S102 - fixed frozen Git producer, not user code
    inherited = ns["Budget"]()
    basis = ns["echelon"](3, 0, 18, 0, inherited)
    need(
        basis == ns["echelon"](3, 0, 18, 1, inherited),
        "two actual Miller constructions",
    )
    t2, t3 = (ns["hecke"](basis, 36, prime, inherited) for prime in (2, 3))
    need(
        ns["matmul"](t2, t3, inherited) == ns["matmul"](t3, t2, inherited),
        "Hecke commutation",
    )
    for prime, matrix in ((2, t2), (3, t3)):
        for n in range(1, CAPS["q_order"] // prime + 1):
            for j in range(3):
                budget.charge(4)
                actual = basis[j][prime * n] + (
                    prime**35 * basis[j][n // prime] if n % prime == 0 else 0
                )
                need(
                    actual == sum(matrix[i][j] * basis[i][n] for i in range(3)),
                    "complete held-out Hecke action within q18",
                )
    frozen = decode(git_bytes(HC, f"{DIR}/{HCSTEM}.json"))
    row = next(row for row in frozen["q_rows"] if row["k"] == 36)
    need(
        row["T2"] == t2 and row["T3"] == t3 and row["basis"] == [b[:16] for b in basis],
        "frozen native prefix binding",
    )
    square = ns["matmul"](t2, t2, inherited)
    need(
        all(
            72 * t3[i][j]
            == (34416831456 if i == j else 0) + 194184 * t2[i][j] - square[i][j]
            for i in range(3)
            for j in range(3)
        ),
        "eigenform q3 polynomial",
    )
    budget.charge(inherited.used)
    # Newton identities are independent of the source's matrix calibration.
    tr1 = sum(t2[i][i] for i in range(3))
    tr2 = sum(square[i][i] for i in range(3))
    elementary2 = F(tr1 * tr1 - tr2, 2)
    det = determinant([[F(x) for x in row] for row in t2], budget)
    poly = [-det, elementary2, F(-tr1), F(1)]
    need(poly == EXPECTED_P, "preregistered characteristic polynomial")
    derivative = [poly[1], 2 * poly[2], F(3)]
    disc = -resultant(poly, derivative, budget)
    opposite = resultant(poly, [(-1) ** i * x for i, x in enumerate(poly)], budget)
    need(
        disc == EXPECTED_DISC
        and disc > 0
        and opposite == EXPECTED_OPPOSITE
        and opposite != 0
        and det != 0,
        "preregistered root predicates",
    )
    s1, s2, s3 = -poly[2], poly[1], -poly[0]
    pair_sum_product = s1 * s2 - s3
    need(opposite == -8 * s3 * pair_sum_product**2, "opposite-root resultant identity")
    square_poly = [-(s3**2), s2**2 - 2 * s1 * s3, -(s1**2 - 2 * s2), F(1)]
    pair_poly = [-(s3**2), s1 * s3, -s2, F(1)]
    sqdisc = -resultant(square_poly, [square_poly[1], 2 * square_poly[2], F(3)], budget)
    productdisc = -resultant(pair_poly, [pair_poly[1], 2 * pair_poly[2], F(3)], budget)
    need(
        sqdisc == disc * pair_sum_product**2 and productdisc == disc * s3**2,
        "all seven prime2 distinctions",
    )
    sequence = sturm(poly, budget)
    intervals = []
    for a, b in ROOT_INTERVALS:
        left, right = variations(sequence, F(a)), variations(sequence, F(b))
        need(
            left - right == 1 and peval(poly, F(a)) * peval(poly, F(b)) < 0,
            "exact root interval",
        )
        intervals.append({"interval": [a, b], "variations": [left, right]})
    return {
        "basis": basis,
        "T2": t2,
        "T3": t3,
        "held_out_action_through": {"2": 9, "3": 6},
        "P": list(map(wire, poly)),
        "discriminant": wire(disc),
        "opposite_resultant": wire(opposite),
        "square_polynomial": list(map(wire, square_poly)),
        "pair_product_polynomial": list(map(wire, pair_poly)),
        "square_discriminant": wire(sqdisc),
        "pair_product_discriminant": wire(productdisc),
        "sturm_sequence": [list(map(wire, p)) for p in sequence],
        "root_intervals": intervals,
    }


def ordered_divisors3(n: int) -> int:
    integer(n, 1, 6)
    return sum(
        1 for a in range(1, n + 1) for b in range(1, n // a + 1) if n % (a * b) == 0
    )


def native_determinant(source: dict, budget: Budget) -> list[dict]:
    basis = source["basis"]
    change_squared = F(EXPECTED_DISC, 72**2)
    rows = []
    for n in range(1, CAPS["dirichlet_order"] + 1):
        value = F(0)
        for m in range(1, math.isqrt(n) + 1):
            if n % (m * m):
                continue
            product = n // (m * m)
            for a in range(1, product + 1):
                for b in range(a + 1, product // a + 1):
                    budget.charge()
                    if product % (a * b):
                        continue
                    c = product // (a * b)
                    if b < c:
                        need(c <= CAPS["q_order"], "complete Fourier tuple coverage")
                        matrix = [[F(f[h]) for h in (a, b, c)] for f in basis]
                        minor = determinant(matrix, budget)
                        value = rational(
                            value
                            + change_squared
                            * ordered_divisors3(m)
                            * minor**2
                            / product**35
                        )
        rows.append({"n": n, "coefficient": wire(value)})
    need(
        all(rows[n - 1]["coefficient"] == [0, 1] for n in (1, 2, 3, 4, 5, 7)),
        "preregistered vanishing coefficients",
    )
    need(
        rows[5]["coefficient"] == wire(F(EXPECTED_DISC, 72**2 * 6**35)),
        "preregistered coefficient6",
    )
    need(
        rows[7]["coefficient"] == wire(F(EXPECTED_DISC, 8**35)), "held-out coefficient8"
    )
    return rows


def zpair(z: object) -> tuple[F, F]:
    need(type(z) is tuple and len(z) == 2, "Gaussian pair type")
    return rational(z[0]), rational(z[1])


def za(z: tuple, w: tuple) -> tuple[F, F]:
    a, b = zpair(z)
    c, d = zpair(w)
    return rational(a + c), rational(b + d)


def zm(z: tuple, w: tuple) -> tuple[F, F]:
    a, b = zpair(z)
    c, d = zpair(w)
    return rational(a * c - b * d), rational(a * d + b * c)


def zc(z: tuple) -> tuple[F, F]:
    a, b = zpair(z)
    return a, -b


def zn(z: tuple) -> tuple[F, F]:
    a, b = zpair(z)
    return -a, -b


def zd(z: tuple, w: tuple) -> tuple[F, F]:
    c, d = zpair(w)
    denominator = rational(c * c + d * d)
    need(denominator != 0, "zero Gaussian denominator")
    return zm(z, (rational(c / denominator), rational(-d / denominator)))


def zw(z: tuple) -> list[list[int]]:
    return list(map(wire, zpair(z)))


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
IMAG = (F(0), F(1))
EXP0 = (0, 0, 0, 0, 0, 0)


def polynomial(p: object) -> dict:
    need(type(p) is dict and len(p) <= CAPS["polynomial_terms"], "polynomial term cap")
    for exponent, coefficient in p.items():
        need(type(exponent) is tuple and len(exponent) == 6, "six-variable exponent")
        for power in exponent:
            integer(power, 0, CAPS["polynomial_degree"])
        need(sum(exponent) <= CAPS["polynomial_degree"], "total degree cap")
        need(zpair(coefficient) != ZERO, "canonical nonzero coefficient")
    return p


def pc(z: tuple) -> dict:
    zpair(z)
    return {} if z == ZERO else {EXP0: z}


def variable(index: int) -> dict:
    integer(index, 0, 5)
    return {tuple(int(i == index) for i in range(6)): ONE}


def pa(p: dict, q: dict, budget: Budget) -> dict:
    polynomial(p)
    polynomial(q)
    out = p.copy()
    for exponent, coefficient in q.items():
        budget.charge()
        out[exponent] = za(out.get(exponent, ZERO), coefficient)
        if out[exponent] == ZERO:
            del out[exponent]
    return polynomial(out)


def pm(p: dict, q: dict, budget: Budget) -> dict:
    polynomial(p)
    polynomial(q)
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            budget.charge()
            exponent = tuple(i + j for i, j in zip(e, f))
            need(sum(exponent) <= CAPS["polynomial_degree"], "product degree cap")
            out[exponent] = za(out.get(exponent, ZERO), zm(a, b))
            if out[exponent] == ZERO:
                del out[exponent]
    return polynomial(out)


def poly_det(matrix: list[list[dict]], budget: Budget) -> dict:
    need(type(matrix) is list, "polynomial matrix type")
    n = integer(len(matrix), 1, CAPS["matrix_dimension"])
    need(
        all(type(row) is list and len(row) == n for row in matrix),
        "square polynomial matrix",
    )
    for row in matrix:
        for p in row:
            polynomial(p)
    out = {}
    for permutation in itertools.permutations(range(n)):
        term = pc((F(parity(permutation)), F(0)))
        for i, j in enumerate(permutation):
            term = pm(term, matrix[i][j], budget)
        out = pa(out, term, budget)
    return out


def evaluate(p: dict, values: tuple, budget: Budget) -> tuple:
    polynomial(p)
    need(type(values) is tuple and len(values) == 6, "six entry values")
    for z in values:
        zpair(z)
    out = ZERO
    for exponent, coefficient in p.items():
        term = coefficient
        for i, power in enumerate(exponent):
            for _ in range(power):
                budget.charge()
                term = zm(term, values[i])
        out = za(out, term)
    return out


def pw(p: dict) -> list[dict]:
    polynomial(p)
    return [{"exponents": list(e), "coefficient": zw(c)} for e, c in sorted(p.items())]


def matrix_polynomials() -> list[list[dict]]:
    x, y, z, a, b, c = (variable(i) for i in range(6))
    return [[x, a, b], [a, y, c], [b, c, z]]


def vector_matrix(v: object) -> list:
    need(type(v) is list and len(v) == 3, "three-row coefficient matrix")
    need(type(v[0]) is list, "coefficient row type")
    j = integer(len(v[0]), 1, 2)
    need(
        all(type(row) is list and len(row) == j for row in v),
        "coefficient matrix shape",
    )
    for row in v:
        for value in row:
            zpair(value)
    return v


def restricted(v: list, budget: Budget) -> dict:
    vector_matrix(v)
    j = len(v[0])
    m = matrix_polynomials()
    out = [[{} for _ in range(j)] for _ in range(j)]
    for a in range(j):
        for b in range(j):
            for i in range(3):
                for l in range(3):
                    coefficient = zm(zc(v[i][a]), v[l][b])
                    out[a][b] = pa(
                        out[a][b], pm(pc(coefficient), m[i][l], budget), budget
                    )
    return poly_det(out, budget)


def pluecker(v: list) -> list[tuple[tuple[int, ...], tuple[F, F]]]:
    vector_matrix(v)
    j = len(v[0])
    out = []
    for indices in itertools.combinations(range(3), j):
        if j == 1:
            value = v[indices[0]][0]
        else:
            a, b = indices
            value = za(zm(v[a][0], v[b][1]), zn(zm(v[a][1], v[b][0])))
        out.append((indices, value))
    return out


def subspaces() -> list[tuple[str, list]]:
    pool = (ZERO, ONE, IMAG)
    out = [
        (f"line_chart_{i}_{j}", [[ONE], [a], [b]])
        for i, a in enumerate(pool)
        for j, b in enumerate(pool)
    ]
    out.extend(
        [
            ("line_e2", [[ZERO], [ONE], [ZERO]]),
            ("line_e3", [[ZERO], [ZERO], [ONE]]),
            ("line_heldout1", [[ONE], [(F(-1), F(0))], [(F(0), F(2))]]),
            ("line_heldout2", [[ONE], [(F(2), F(-1))], [(F(-1), F(-1))]]),
        ]
    )
    out.extend(
        (f"plane_chart_{i}_{j}", [[ONE, ZERO], [ZERO, ONE], [a, b]])
        for i, a in enumerate(pool)
        for j, b in enumerate(pool)
    )
    out.extend(
        [
            ("plane_e1e3", [[ONE, ZERO], [ZERO, ZERO], [ZERO, ONE]]),
            ("plane_e2e3", [[ZERO, ZERO], [ONE, ZERO], [ZERO, ONE]]),
            (
                "plane_heldout1",
                [[ONE, ZERO], [ZERO, ONE], [(F(1), F(-1)), (F(-2), F(1))]],
            ),
            (
                "plane_heldout2",
                [[ONE, ZERO], [ZERO, ONE], [(F(2), F(-1)), (F(-1), F(2))]],
            ),
            (
                "canonical_first_coefficient_plane",
                [[ONE, ONE], [(F(-1), F(0)), ZERO], [ZERO, (F(-1), F(0))]],
            ),
        ]
    )
    need(len(out) == CAPS["subspace_count"], "complete declared subspace grid")
    return out


def protected_target(vanish: dict, protect: dict, budget: Budget) -> dict:
    pool = (ONE, (F(2), F(0)), (F(3), F(0)))
    attempts = 0
    for solved in range(3):
        need(all(e[solved] <= 1 for e in vanish), "diagonal multilinearity")
        others = [i for i in range(6) if i != solved]
        for values in itertools.product(pool, repeat=5):
            attempts += 1
            need(attempts <= CAPS["target_attempts"], "target search cap")
            budget.charge()
            point = [ZERO] * 6
            for i, z in zip(others, values):
                point[i] = z
            constant = evaluate(vanish, tuple(point), budget)
            point[solved] = ONE
            linear = za(evaluate(vanish, tuple(point), budget), zn(constant))
            if linear == ZERO:
                continue
            point[solved] = zd(zn(constant), linear)
            if point[solved] == ZERO:
                continue
            point = tuple(point)
            zero, guarded = (
                evaluate(vanish, point, budget),
                evaluate(protect, point, budget),
            )
            need(zero == ZERO, "exact solved target")
            if guarded == ZERO:
                continue
            radius = F(2)
            for a, b in point:
                radius = max(radius, 1 + abs(a) + abs(b), 1 + 1 / max(abs(a), abs(b)))
            for a, b in point:
                need(1 / radius**2 <= a * a + b * b <= radius**2, "annulus witness")
            return {
                "matrix_entries": list(map(zw, point)),
                "Z": [1, 1],
                "vanishing_value": zw(zero),
                "protected_value": zw(guarded),
                "annulus_radius": wire(radius),
                "solved_diagonal": solved,
                "attempts": attempts,
            }
    raise Rejected(
        "fixed finite target pool exhausted; no analytic conclusion from this search"
    )


def subspace_controls(budget: Budget) -> tuple[dict, list]:
    delta = poly_det(matrix_polynomials(), budget)
    need(len(delta) == 5, "complete symmetric determinant terms")
    explicit = (ONE, ONE, ONE, ONE, ONE, (F(2), F(0)))
    need(
        evaluate(delta, explicit, budget) == (F(-1), F(0)),
        "Hecke-plane protected full determinant",
    )
    rows = []
    for label, v in subspaces():
        p = restricted(v, budget)
        need(
            all(c[1] == 0 for c in p.values()), "real polynomial coefficients retained"
        )
        j = len(v[0])
        pl = pluecker(v)
        expected = {}
        for indices, z in pl:
            size = zm(zc(z), z)
            exponent = tuple(int(i in indices) for i in range(6))
            if size != ZERO:
                expected[exponent] = size
        actual_diagonal = {e: c for e, c in p.items() if not any(e[3:])}
        need(
            actual_diagonal == expected and expected,
            "positive Pluecker diagonal identity",
        )
        gram = evaluate(p, (ONE, ONE, ONE, ZERO, ZERO, ZERO), budget)
        need(gram[0] > 0 and gram[1] == 0, "full coefficient rank")
        coordinate_line = j == 1 and len(expected) == 1
        need(
            (len(p) == 1) == coordinate_line,
            "monomial classification on declared controls",
        )
        pole = [] if coordinate_line else [protected_target(p, delta, budget)]
        zero = protected_target(delta, p, budget)
        if label == "plane_chart_0_0":
            need(
                evaluate(p, explicit, budget) == ZERO,
                "explicit actual Hecke-plane target",
            )
        rows.append(
            {
                "label": label,
                "dimension": j,
                "coefficient_matrix": [[zw(z) for z in row] for row in v],
                "gram_determinant": zw(gram),
                "P_W": pw(p),
                "diagonal_character": pw(expected),
                "class": "pole_free_Hecke_line" if coordinate_line else "genuine_poles",
                "zero": zero,
                "pole": pole,
            }
        )
    need(
        sum(row["class"] == "pole_free_Hecke_line" for row in rows) == 3,
        "exact protected line coverage",
    )
    return delta, rows


def payload() -> dict:
    budget = Budget()
    source = native_source(budget)
    coefficients = native_determinant(source, budget)
    delta, rows = subspace_controls(budget)
    out = {
        "schema": "weight36-subspace-divisors-v1",
        "authoring_base": BASE,
        "arithmetic_class": "MIXED",
        "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        "rounding": "none",
        "analytic_claims_machine_certified": "no",
        "weight": 36,
        "caps": CAPS.copy(),
        "native_source": source,
        "full_determinant_coefficients": coefficients,
        "symmetric_determinant": pw(delta),
        "subspaces": rows,
        "controls": {
            "primitive_degrees": [1, 3, 3, 3, 4, 4, 4],
            "source_majorants": {"line": [3, 4], "plane": [6, 8], "full": [6, 12]},
            "q3_denominator": 72,
            "scaled_coefficient8_to6": 5184,
            "prime_cutoff": [3, 2],
            "no_uniform_cap_override": "HC_q18_preserved",
        },
        "work_used": budget.used,
        "scope": "fixed_weight36_all_proper_complex_subspaces_analytic_theorem",
        "not_claimed": [
            "all_weights",
            "exhaustive_Grassmannian_grid",
            "effective_BT_width",
            "numerical_divisor_location",
            "simplicity",
            "unsigned_asymptotic",
            "RH",
            "new_automorphic_family",
        ],
    }
    typed(out)
    return out


def fixture() -> dict:
    authenticate()
    out = payload()
    out["artifact_sha256_lf"] = {
        path: digest(lf(file_bytes(ROOT / path))) for path in ARTIFACTS
    }
    out["payload_sha256"] = digest(encoded(out))
    need(len(encoded(out)) <= CAPS["json_bytes"], "output byte cap")
    return out


def validate(value: object) -> None:
    typed(value)
    need(type(value) is dict and value == fixture(), "strict primitive reconstruction")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit-fixture", action="store_true")
    group.add_argument("--emit-sources", action="store_true")
    args = parser.parse_args()
    try:
        if args.emit_sources:
            sys.stdout.buffer.write(encoded(manifest()))
        elif args.emit_fixture:
            sys.stdout.buffer.write(encoded(fixture()))
        else:
            raw = file_bytes(ROOT / DIR / f"{STEM}.json")
            validate(decode(raw))
            print(
                "PASS: native weight36, seven inputs, 36 determinant coefficients, 27 fixed subspaces"
            )
            print("fixture_sha256_lf=" + digest(lf(raw)))
        return 0
    except (Rejected, OSError, subprocess.SubprocessError) as exc:
        print("REJECTED: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
