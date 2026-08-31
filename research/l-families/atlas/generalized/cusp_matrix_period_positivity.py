"""Exact finite controls for the native matrix-period/theta-flag proof.

No period integral, theta value, Gamma phase, continuation, or infinite
positivity theorem is machine certified. Only the declared finite algebra is.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
STEM = "cusp_matrix_period_positivity"
BASE = "ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf"
DESIGN = "8cf1538b336acd2b60faba2d7129edba3676932c"
ARTIFACTS = [
    DIR + "CUSP_MATRIX_PERIOD_POSITIVITY.md",
    DIR + STEM + ".py",
    DIR + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
]
BINDINGS = [
    {
        "commit": "b62dfc6348661992bca659c99de226a1b6b22e14",
        "path": "research/l-families/atlas/generalized/RANKIN_SELBERG_QUOTIENT_GLOBAL_PARENT.md",
        "git_blob": "4a3f9f0b6644bffdc94214e6fb2b60dfafdd93ca",
        "sha256_lf": "1828196e08782ce692f28e3fdec2feae55c6d24e9b3eb5c35ff1c315434aee75",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "ec5bdd9b02ea68bddfcf34ac40a85d283faf64cf",
        "path": "research/l-families/atlas/generalized/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY.md",
        "git_blob": "ba8dd0d08aface85ef346106b158636177a88979",
        "sha256_lf": "d8737b8551ddd71249b799a1a2ebd61cb2c0ad01bc15ca7954cb36fe73d2f26f",
    },
    {
        "commit": "0f29fd2d687c57402a14723dde2bc2b7e74fa317",
        "path": "research/l-families/atlas/generalized/CUSP_WEIGHT24_FIXED_DIVISOR_INFINITY_AUDIT_EC5BDD9B.md",
        "git_blob": "91c1896791ef94b6f1f753fa48bc48eb7e91df7b",
        "sha256_lf": "0e86da5a218b066a7d46aa5336d35817ce0c7ad4c8da89a12797e23eed309655",
    },
    {
        "commit": "2bd3de4ec14077868a38def1ba8883c9b8feefb9",
        "path": "research/l-families/atlas/generalized/CUSP_MATRIX_PERIOD_POSITIVITY.md",
        "git_blob": "0071be9480527d0a53c03d57a66ebc795cff4a00",
        "sha256_lf": "dbe1a0fdf5c4bd7d249c8891a088d0b088f08f9d5a2ab1c01afc0dfe83951e9b",
    },
    {
        "commit": "aa93b79f38792aeffd55e44f0a6800ee255c2274",
        "path": "research/l-families/atlas/generalized/CUSP_MATRIX_PERIOD_POSITIVITY.md",
        "git_blob": "75b2efa3b065757866aa7ff554e58188e52cebd1",
        "sha256_lf": "6d18b0599f1e6678a8e99869b5165dfb75a61acce65b7b839c93f5b49719e557",
    },
    {
        "commit": "8cf1538b336acd2b60faba2d7129edba3676932c",
        "path": "research/l-families/atlas/generalized/CUSP_MATRIX_PERIOD_POSITIVITY.md",
        "git_blob": "5096f10f12da22a0c58dda1384d224a6bfd8b7ef",
        "sha256_lf": "7b6b8e0db2d358332b00f2195d7c25149d47f8d9e20d77b09451e680e0f1ccfa",
    },
]
CAPS = {
    "q_order": 4,
    "derivative_order": 16,
    "matrix_dimension": 6,
    "feature_rows": 5,
    "integer_bits": 4096,
    "polynomial_length": 20,
    "work_units": 2000000,
    "json_bytes": 3000000,
    "json_nodes": 200000,
    "json_depth": 24,
    "container_length": 5000,
    "string_length": 4096,
}
WORK = 0


def need(ok, message):
    if not ok:
        raise ValueError(message)


def charge(n=1):
    global WORK
    need(type(n) is int and n >= 0, "work charge type")
    WORK += n
    need(WORK <= CAPS["work_units"], "work cap")


def integer(n, low, high):
    need(type(n) is int and low <= n <= high, "integer type/range cap")
    return n


def rational(x):
    need(type(x) in (int, Q), "exact rational, not bool/float/string")
    q = Q(x)
    need(
        max(q.numerator.bit_length(), q.denominator.bit_length())
        <= CAPS["integer_bits"],
        "rational bit cap",
    )
    return q


def z(x):
    if type(x) in (int, Q):
        return rational(x), Q(0)
    need(type(x) in (list, tuple) and len(x) == 2, "Gaussian pair shape")
    return rational(x[0]), rational(x[1])


def add(a, b):
    charge()
    a, b = z(a), z(b)
    return z((a[0] + b[0], a[1] + b[1]))


def neg(a):
    a = z(a)
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    charge()
    a, b = z(a), z(b)
    return z((a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]))


def conj(a):
    a = z(a)
    return a[0], -a[1]


def div(a, b):
    a, b = z(a), z(b)
    d = b[0] * b[0] + b[1] * b[1]
    need(d > 0, "nonzero Gaussian denominator")
    c = mul(a, conj(b))
    return z((c[0] / d, c[1] / d))


ZERO = z(0)
ONE = z(1)


def matrix(a):
    need(type(a) in (list, tuple) and 1 <= len(a) <= 6, "matrix row cap/type")
    need(all(type(row) in (list, tuple) for row in a), "matrix row type")
    n = len(a[0])
    need(1 <= n <= 6 and all(len(row) == n for row in a), "matrix column/rectangle")
    return tuple(tuple(z(x) for x in row) for row in a)


def eye(n):
    integer(n, 1, 6)
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def star(a):
    a = matrix(a)
    return matrix([[conj(a[i][j]) for i in range(len(a))] for j in range(len(a[0]))])


def plus(a, b):
    a, b = matrix(a), matrix(b)
    need((len(a), len(a[0])) == (len(b), len(b[0])), "matrix sum dimensions")
    return matrix([[add(x, y) for x, y in zip(ra, rb)] for ra, rb in zip(a, b)])


def scale(a, c):
    a = matrix(a)
    return matrix([[mul(x, c) for x in row] for row in a])


def minus(a, b):
    return plus(a, scale(b, -1))


def product(a, b):
    a, b = matrix(a), matrix(b)
    need(len(a[0]) == len(b), "matrix product dimensions")
    out = []
    for row in a:
        r = []
        for j in range(len(b[0])):
            s = ZERO
            for k, x in enumerate(row):
                s = add(s, mul(x, b[k][j]))
            r.append(s)
        out.append(r)
    return matrix(out)


def congruence(a, c):
    return product(product(star(c), a), c)


def inverse(a):
    a = matrix(a)
    n = len(a)
    need(len(a[0]) == n, "square inverse")
    work = [list(row) + list(erow) for row, erow in zip(a, eye(n))]
    for k in range(n):
        pivot = next((j for j in range(k, n) if work[j][k] != ZERO), None)
        need(pivot is not None, "singular inverse")
        work[k], work[pivot] = work[pivot], work[k]
        p = work[k][k]
        work[k] = [div(x, p) for x in work[k]]
        for j in range(n):
            if j != k:
                c = work[j][k]
                work[j] = [sub(x, mul(c, y)) for x, y in zip(work[j], work[k])]
    return matrix([row[n:] for row in work])


def determinant(a):
    a = matrix(a)
    n = len(a)
    need(len(a[0]) == n, "square determinant")
    work = [list(row) for row in a]
    result = ONE
    for k in range(n):
        pivot = next((j for j in range(k, n) if work[j][k] != ZERO), None)
        if pivot is None:
            return ZERO
        if pivot != k:
            work[k], work[pivot] = work[pivot], work[k]
            result = neg(result)
        p = work[k][k]
        result = mul(result, p)
        for j in range(k + 1, n):
            c = div(work[j][k], p)
            for h in range(k + 1, n):
                work[j][h] = sub(work[j][h], mul(c, work[k][h]))
    return result


def principal(a, indices):
    a = matrix(a)
    need(
        type(indices) in (tuple, list)
        and indices
        and len(set(indices)) == len(indices),
        "principal index type",
    )
    for j in indices:
        integer(j, 0, len(a) - 1)
    return matrix([[a[i][j] for j in indices] for i in indices])


def psd_minors(a, strict=False):
    need(type(strict) is bool, "strict positivity flag type")
    a = matrix(a)
    need(a == star(a), "Hermitian principal-minor input")
    out = []
    for m in range(1, len(a) + 1):
        for indices in itertools.combinations(range(len(a)), m):
            d = determinant(principal(a, indices))
            need(
                d[1] == 0 and (d[0] > 0 if strict else d[0] >= 0),
                "positive principal minor",
            )
            out.append({"indices": list(indices), "determinant": str(d[0])})
    return out


def schur(a, r):
    a = matrix(a)
    need(len(a) == len(a[0]), "square quotient")
    integer(r, 1, len(a))
    a11 = matrix([row[:r] for row in a[:r]])
    if r == len(a):
        return a11
    a12 = matrix([row[r:] for row in a[:r]])
    a21 = matrix([row[:r] for row in a[r:]])
    a22 = matrix([row[r:] for row in a[r:]])
    return minus(a11, product(product(a12, inverse(a22)), a21))


def encoded_matrix(a):
    return [[[str(re), str(im)] for re, im in row] for row in matrix(a)]


def polynomial(p):
    need(type(p) in (list, tuple) and 1 <= len(p) <= 20, "polynomial length/type")
    need(
        all(type(x) is int and x.bit_length() <= 4096 for x in p),
        "polynomial coefficient",
    )
    return list(p)


def convolution(a, b, limit):
    integer(limit, 0, 4)
    a, b = polynomial(a), polynomial(b)
    out = [0] * (limit + 1)
    for i, x in enumerate(a[: limit + 1]):
        for j, y in enumerate(b[: limit + 1 - i]):
            charge()
            out[i + j] += x * y
    return out


def native_rows():
    order = 4
    p = [1] + [0] * 3
    for n in range(1, 4):
        factor = [0] * 4
        for j in range(4 // n + 1):
            if n * j < 4:
                factor[n * j] = (-1) ** j * math.comb(24, j)
        p = convolution(p, factor, 3)
    delta = [0] + p
    e4 = [1] + [
        240 * sum(d**3 for d in range(1, n + 1) if n % d == 0) for n in range(1, 5)
    ]
    e4cub = convolution(convolution(e4, e4, order), e4, order)
    f0 = convolution(delta, e4cub, order)
    b = convolution(delta, delta, order)
    shear = f0[2]
    g = [a - shear * v for a, v in zip(f0, b)]
    rows = [(g[n], b[n]) for n in range(1, 5)]
    need(
        rows == [(1, 0), (0, 1), (195660, -48), (12080128, 1080)],
        "native q4 prediction",
    )
    return delta, e4, f0, b, g, rows


def formal_log_determinant(rows):
    # Two formal independent indeterminates L2,L3; L4=2L2, L1=0.
    need(type(rows) in (list, tuple) and len(rows) == 4, "formal log row count")
    need(
        all(type(row) in (list, tuple) and len(row) == 2 for row in rows),
        "formal log row shape",
    )
    need(
        all(type(x) is int and x.bit_length() <= 4096 for row in rows for x in row),
        "formal log integer coefficients",
    )
    logs = ({}, {(1, 0): 1}, {(0, 1): 1}, {(1, 0): 2})
    entries = []
    for row, log in zip(rows, logs):
        entries.append(
            [
                {(0, 0): row[0]},
                {(0, 0): row[1]},
                {e: c * row[0] for e, c in log.items()},
                {e: c * row[1] for e, c in log.items()},
            ]
        )
    out = {}
    for perm in itertools.permutations(range(4)):
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        acc = {(0, 0): sign}
        for i, j in enumerate(perm):
            nxt = {}
            for e, a in acc.items():
                for f, b in entries[i][j].items():
                    h = e[0] + f[0], e[1] + f[1]
                    need(sum(h) <= 2, "formal log degree")
                    nxt[h] = nxt.get(h, 0) + a * b
            acc = nxt
        for e, a in acc.items():
            out[e] = out.get(e, 0) + a
    out = {e: a for e, a in out.items() if a}
    need(all(a.bit_length() <= 4096 for a in out.values()), "formal log output bit cap")
    need(out == {(2, 0): -1159692288, (1, 1): 1371005088}, "formal stacked determinant")
    return [[*e, c] for e, c in sorted(out.items())]


def derivative_numerator(order):
    integer(order, 0, 16)
    p = [1, 1, 1]
    for denominator_power in range(1, order + 1):
        dp = [(j + 1) * p[j + 1] for j in range(len(p) - 1)]
        out = [0] * (len(p) + 1)
        for j, c in enumerate(dp):
            out[j + 1] += c
            out[j + 2] += c
        for j, c in enumerate(p):
            out[j + 1] -= denominator_power * c
        while len(out) > 1 and out[-1] == 0:
            out.pop()
        p = polynomial(out)
    return p


def derivative(order, q):
    integer(order, 0, 16)
    q = rational(q)
    need(0 < q < 1, "declared positive rational q range")
    p = derivative_numerator(order)
    value = Q(0)
    for c in reversed(p):
        value = value * q + c
    return rational(value / (1 + q) ** (order + 1))


def fscalar(q):
    q = rational(q)
    need(q > 0, "positive synthetic q")
    return rational(1 + q * q / (1 + q))


def systems(rows):
    return [
        {
            "id": 1,
            "rows": [[1, 0], [1, 1], [0, 1]],
            "frequencies": [0, 1, 2],
            "weights": [1, Q(1, 2), Q(1, 4)],
            "basis": [[1, (0, 1)], [0, 1]],
        },
        {
            "id": 2,
            "rows": rows,
            "frequencies": [1, 2, 3, 4],
            "weights": [Q(1, n**25) for n in range(1, 5)],
            "basis": [[1, (1, 1)], [(0, 1), 2]],
        },
        {
            "id": 3,
            "rows": [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [1, -1, 2]],
            "frequencies": [0, Q(1, 2), 1, Q(3, 2), 2],
            "weights": [Q(1, 3**j) for j in range(5)],
            "basis": [[1, (0, 1), 0], [0, 1, 1], [1, 0, 1]],
        },
    ]


def gram(rows, weights):
    rows = matrix(rows)
    need(
        len(rows) <= 5 and type(weights) in (list, tuple) and len(weights) == len(rows),
        "feature row/weight cap",
    )
    weights = [rational(w) for w in weights]
    need(all(w > 0 for w in weights), "positive feature weights")
    n = len(rows[0])
    out = scale(eye(n), 0)
    for row, w in zip(rows, weights):
        out = plus(out, scale(product(star([row]), [row]), w))
    return out


def moments(rows, frequencies, weights):
    rows = matrix(rows)
    need(
        type(frequencies) in (list, tuple) and len(frequencies) == len(rows),
        "frequency shape",
    )
    nu = [rational(v) for v in frequencies]
    need(all(v >= 0 for v in nu), "nonnegative declared proxy frequencies")
    return [
        gram(
            rows,
            [rational(w) * v**j if j else rational(w) for v, w in zip(nu, weights)],
        )
        if j == 0 or all(v > 0 for v in nu)
        else _moment_allow_zero(rows, nu, weights, j)
        for j in range(3)
    ]


def _moment_allow_zero(rows, nu, weights, j):
    out = scale(eye(len(rows[0])), 0)
    for row, v, w in zip(rows, nu, weights):
        out = plus(out, scale(product(star([row]), [row]), rational(w) * v**j))
    return out


def block_moment(a, b, c):
    return matrix(
        [list(x) + list(y) for x, y in zip(a, b)]
        + [list(x) + list(y) for x, y in zip(b, c)]
    )


def feature_control(spec):
    rows = matrix(spec["rows"])
    basis = matrix(spec["basis"])
    need(determinant(basis) != ZERO, "invertible declared complex basis")
    m0, m1, m2 = moments(rows, spec["frequencies"], spec["weights"])
    variance = minus(m2, product(product(m1, inverse(m0)), m1))
    regression = product(inverse(m0), m1)
    residual = []
    for row, nu in zip(rows, spec["frequencies"]):
        residual.append(minus(scale([row], nu), product([row], regression))[0])
    need(gram(residual, spec["weights"]) == variance, "residual Gram variance identity")
    transformed = product(rows, basis)
    n0, n1, n2 = moments(transformed, spec["frequencies"], spec["weights"])
    need(
        [n0, n1, n2] == [congruence(m, basis) for m in (m0, m1, m2)],
        "complex moment congruence",
    )
    varnew = minus(n2, product(product(n1, inverse(n0)), n1))
    need(varnew == congruence(variance, basis), "variance congruence")
    return {
        "id": spec["id"],
        "rows": encoded_matrix(rows),
        "frequencies": [str(x) for x in spec["frequencies"]],
        "weights": [str(x) for x in spec["weights"]],
        "basis": encoded_matrix(basis),
        "moments": [encoded_matrix(m) for m in (m0, m1, m2)],
        "variance": encoded_matrix(variance),
        "residual_gram": encoded_matrix(gram(residual, spec["weights"])),
        "moment0_positive_minors": psd_minors(m0, True),
        "block_positive_semidefinite_minors": psd_minors(block_moment(m0, m1, m2)),
        "variance_positive_semidefinite_minors": psd_minors(variance),
        "transformed_moments": [encoded_matrix(m) for m in (n0, n1, n2)],
        "transformed_variance": encoded_matrix(varnew),
    }, m0


def soft_control(identifier, m0, r, t):
    t = rational(t)
    need(t > 1, "reciprocal pair t>1")
    d = len(m0)
    integer(r, 1, d - 1)
    g = eye(d)
    h = plus(g, m0)
    hrec = scale(h, t)
    rrec = minus(hrec, g)
    need(rrec == plus(scale(m0, t), scale(g, t - 1)), "reciprocal R construction")
    q = minus(schur(h, r), schur(g, r))
    qrec = minus(schur(hrec, r), schur(g, r))
    need(
        q == plus(scale(qrec, 1 / t), scale(eye(r), 1 / t - 1)),
        "quotient vacuum reciprocity",
    )
    adapted = [list(row) for row in g]
    adapted[0][0] = z((1, 1))
    adapted[d - 1][d - 1] = z(2)
    adapted[d - 1][0] = z((Q(1, 2), 1))
    if r >= 2:
        adapted[0][1] = z((0, 1))
    adapted = matrix(adapted)
    need(determinant(adapted) != ZERO, "adapted basis invertible")
    need(
        all(adapted[i][j] == ZERO for i in range(r) for j in range(r, d)),
        "flag-preserving block",
    )
    gnew, hnew = congruence(g, adapted), congruence(h, adapted)
    qnew = minus(schur(hnew, r), schur(gnew, r))
    aq = matrix([row[:r] for row in adapted[:r]])
    need(qnew == congruence(q, aq), "transform BOTH vacuum and density")
    return {
        "system": identifier,
        "quotient_dimension": r,
        "flag_dimension": d - r,
        "t": str(t),
        "R_t": encoded_matrix(m0),
        "R_reciprocal": encoded_matrix(rrec),
        "quotient_vacuum_difference": encoded_matrix(q),
        "reciprocal_difference": encoded_matrix(qrec),
        "positive_minors": psd_minors(q, True),
        "reciprocal_positive_minors": psd_minors(qrec, True),
        "adapted_basis": encoded_matrix(adapted),
        "transformed_vacuum": encoded_matrix(gnew),
        "transformed_difference": encoded_matrix(qnew),
        "congruence_positive_minors": psd_minors(qnew, True),
    }


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("ascii")


def lf(raw):
    return raw.replace(b"\r\n", b"\n")


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def typed(value):
    visits = 0

    def walk(v, depth):
        nonlocal visits
        visits += 1
        need(
            visits <= CAPS["json_nodes"] and depth <= CAPS["json_depth"],
            "JSON depth/node cap",
        )
        if type(v) is dict:
            need(len(v) <= CAPS["container_length"], "JSON object length")
            need(
                all(type(k) is str and len(k) <= CAPS["string_length"] for k in v),
                "JSON key cap/type",
            )
            for item in v.values():
                walk(item, depth + 1)
        elif type(v) is list:
            need(len(v) <= CAPS["container_length"], "JSON list length")
            for item in v:
                walk(item, depth + 1)
        elif type(v) is str:
            need(
                len(v) <= CAPS["string_length"] and v.isascii(), "JSON string cap/ASCII"
            )
        elif type(v) is int:
            need(v.bit_length() <= CAPS["integer_bits"], "JSON integer bit cap")
        else:
            need(type(v) is bool, "JSON primitive type")

    walk(value, 0)


def decode(raw):
    need(type(raw) is bytes and len(raw) <= CAPS["json_bytes"], "JSON byte cap/type")

    def pairs(items):
        out = {}
        for k, v in items:
            need(k not in out, "duplicate JSON key")
            out[k] = v
        return out

    def reject(_):
        raise ValueError("noninteger JSON numeric primitive")

    value = json.loads(
        raw, object_pairs_hook=pairs, parse_float=reject, parse_constant=reject
    )
    typed(value)
    return value


def file_bytes(path):
    need(path.stat().st_size <= CAPS["json_bytes"], "artifact byte cap")
    return path.read_bytes()


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "final_control_design": DESIGN,
        "frozen_sources": BINDINGS,
        "references": [
            {
                "url": "https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf",
                "passage": "equations2,4,6,7 printed pp275-277; theta and completed Eisenstein normalization",
            },
            {
                "url": "https://dlmf.nist.gov/5.11",
                "passage": "Gamma and digamma asymptotics",
            },
            {
                "url": "https://doi.org/10.1137/0128007",
                "passage": "classical quotient/shorted-form context; finite proof supplied",
            },
        ],
        "remote_bytes_authenticated": False,
        "contract": {
            "arithmetic_class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
            "caps": CAPS,
            "analytic_claims_machine_certified": False,
            "no_period_theta_gamma_zeta_zero_evaluation": True,
        },
    }


def authenticate():
    need(
        canonical(decode(file_bytes(ROOT / (DIR + STEM + ".sources.json"))))
        == canonical(manifest()),
        "fixed source manifest",
    )
    for row in BINDINGS:
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
        )
        need(len(raw) <= CAPS["json_bytes"], "frozen source byte cap")
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        need(
            blob == row["git_blob"] and digest(lf(raw)) == row["sha256_lf"],
            "frozen source authentication",
        )


def payload():
    global WORK
    WORK = 0
    delta, e4, f0, b, g, rows = native_rows()
    logs = formal_log_determinant(rows)
    derivative_rows = [
        {"order": r, "q": str(q), "value": str(derivative(r, q))}
        for r in range(1, 17)
        for q in (Q(1, 3), Q(1, 2), Q(2, 3))
    ]
    need(
        derivative(7, Q(1, 3)) == Q(-3311, 12288), "seventh derivative negative witness"
    )
    nodes = (Q(1, 3), Q(1, 2), Q(2, 3))
    kernel = matrix([[fscalar(x * y) for y in nodes] for x in nodes])
    kdet = determinant(kernel)
    need(kdet == z(Q(-81, 8808800)), "post-scout kernel determinant")
    leading = [Q(1)] + [
        determinant(principal(kernel, list(range(j))))[0] for j in range(1, 4)
    ]
    pivots = [leading[j] / leading[j - 1] for j in range(1, 4)]
    need(
        pivots == [Q(91, 90), Q(1189, 89180), Q(-5103, 7481188)],
        "post-scout exact LDL pivots",
    )
    features = []
    soft = []
    for spec in systems(rows):
        record, m0 = feature_control(spec)
        features.append(record)
        for r in range(1, len(m0)):
            for t in (Q(3, 2), Q(2), Q(5)):
                soft.append(soft_control(spec["id"], m0, r, t))
    need(
        (len(derivative_rows), len(features), len(soft)) == (48, 3, 12),
        "complete declared coverage",
    )
    out = {
        "schema": STEM + "-v1",
        "contract": manifest()["contract"],
        "sources": BINDINGS,
        "native": {
            "delta": delta,
            "E4": e4,
            "f0": f0,
            "b": b,
            "g": g,
            "q_rows": [list(row) for row in rows],
            "formal_log_determinant_L2_L3": logs,
            "positive_cone_decomposition": {
                "L2_times_L3": 211312800,
                "L2_times_L3_minus_L2": 1159692288,
            },
        },
        "derivative_panel": derivative_rows,
        "post_scout_kernel": {
            "q_nodes": [str(x) for x in nodes],
            "matrix": encoded_matrix(kernel),
            "determinant": str(kdet[0]),
            "LDL_pivots": [str(p) for p in pivots],
            "preregistered_before_first_scout": False,
        },
        "features": features,
        "soft_reciprocal_pairs": soft,
        "coverage": {
            "native_q_order": 4,
            "derivatives": 48,
            "feature_systems": 3,
            "soft_pairs": 12,
            "flags": "standard trailing coordinate flags at all nontrivial dimensions",
            "reciprocal_pair_contract": "G=I,R(t)=M0,R(1/t)=tM0+(t-1)I; algebraic pairs, not one theta function",
            "basis_congruence": "transform BOTH G and H; compare quotient-vacuum differences",
            "feature_frequencies": "declared rational proxies; system2 frequencies1,2,3,4 are NOT log n",
        },
        "work_units": WORK,
        "not_claimed": [
            "analytic proof machine certification",
            "numerical modular periods",
            "actual theta evaluations",
            "RH or GRH",
            "Euler product",
            "purity",
            "preferred flag",
            "period Schur equals source quotient",
        ],
    }
    typed(out)
    return out


def fixture():
    authenticate()
    out = payload()
    out["artifact_sha256_lf"] = {p: digest(lf(file_bytes(ROOT / p))) for p in ARTIFACTS}
    out["payload_sha256"] = digest(canonical(out))
    need(len(canonical(out)) <= CAPS["json_bytes"], "fixture byte cap")
    return out


def check(value):
    typed(value)
    need(type(value) is dict, "fixture object")
    need(
        canonical(value) == canonical(fixture()),
        "full fresh source-authenticated primitive reconstruction",
    )
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
        print(json.dumps(fixture(), sort_keys=True, indent=2))
    else:
        raw = file_bytes(ROOT / (DIR + STEM + ".json"))
        check(decode(raw))
        print(
            "PASS exact native q4,48 derivatives,3 feature systems,12 source quotient pairs"
        )
        print("fixture_sha256_lf=" + digest(lf(raw)))


if __name__ == "__main__":
    main()
