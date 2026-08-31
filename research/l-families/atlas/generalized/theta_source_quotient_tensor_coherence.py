"""Exact preregistered source quotient/tensor/averaging controls.
No analytic integral, theta value, asymptotic limit or infinite closure proof
is machine-certified. The full written theorem has independent obligations.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
STEM = "theta_source_quotient_tensor_coherence"
BASE = "fdd349dcf6ba1b104e27866ae66b4c89752d5f05"
DESIGN = "e2c659ef1c1af926de63b69bf6c9ead6a95feaf5"
ARTIFACTS = [
    DIR + STEM.upper() + ".md",
    DIR + STEM + ".py",
    DIR + STEM + ".sources.json",
    "tests/test_" + STEM + ".py",
]
BINDINGS = [
    {
        "commit": "fdd349dcf6ba1b104e27866ae66b4c89752d5f05",
        "path": "research/l-families/atlas/generalized/CUSP_MATRIX_PERIOD_POSITIVITY.md",
        "git_blob": "c901150a44e981ed2ef548d8b123d4e6e99f2c27",
        "sha256_lf": "fabb13f35e0f6a45ddbc3b5f54f0376e9c0aec5d75b44ae9b4ae10cf17136c0c",
    },
    {
        "commit": "fdd349dcf6ba1b104e27866ae66b4c89752d5f05",
        "path": "research/l-families/atlas/generalized/cusp_matrix_period_positivity.py",
        "git_blob": "5044fd2901aaafad015ee056388966bb2d8e2674",
        "sha256_lf": "719f7b8fa6d52efb88ec0d7162a15a5c146b51256eacdfef514b6ca12b788eed",
    },
    {
        "commit": "fdd349dcf6ba1b104e27866ae66b4c89752d5f05",
        "path": "research/l-families/atlas/generalized/cusp_matrix_period_positivity.json",
        "git_blob": "e601072cd96a3ac8ec7eca6e73c2a08f29c44c7b",
        "sha256_lf": "021b0bd08e96fa4a58dfac352f4833ef86587ea273e6d656bcda8c19bf789689",
    },
    {
        "commit": "fdd349dcf6ba1b104e27866ae66b4c89752d5f05",
        "path": "research/l-families/atlas/generalized/cusp_matrix_period_positivity.sources.json",
        "git_blob": "8841b26a3256556df178e90d78c657c775d3c01d",
        "sha256_lf": "82a568b0d338cf45a1168206fdecbc9132bbb57c28684b22777c3768e4f3b17b",
    },
    {
        "commit": "fdd349dcf6ba1b104e27866ae66b4c89752d5f05",
        "path": "tests/test_cusp_matrix_period_positivity.py",
        "git_blob": "b8a0878c6561816ec1617e1e3842cc781a70751b",
        "sha256_lf": "0c681025da1e6957e412abd853052454ef5c8f03c56b3c9c64cb8379bf3764a5",
    },
    {
        "commit": "bd53c016dbd006ac5e40d4fff412162a68e99525",
        "path": "research/l-families/atlas/generalized/THETA_SOURCE_QUOTIENT_TENSOR_COHERENCE.md",
        "git_blob": "fddbcc89852d2e9280d2208b67603855f6f8667c",
        "sha256_lf": "4271b58d5ed8ea805441ae38fd720baa6c698866e94a5023c7813a6eb7cd1442",
    },
    {
        "commit": "e2c659ef1c1af926de63b69bf6c9ead6a95feaf5",
        "path": "research/l-families/atlas/generalized/THETA_SOURCE_QUOTIENT_TENSOR_COHERENCE.md",
        "git_blob": "2fc590b7fac8681d5afde0c576693193c56306e7",
        "sha256_lf": "a45c015fc8a07f76ca9c23411ea3854397b3afdf01205a0c33c6594926d3c5f0",
    },
]
CAPS = {
    "matrix_dimension": 4,
    "integer_bits": 4096,
    "work_units": 2000000,
    "json_bytes": 3000000,
    "json_nodes": 200000,
    "json_depth": 32,
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
    need(type(a) in (list, tuple) and 1 <= len(a) <= 4, "matrix row cap/type")
    need(all(type(row) in (list, tuple) for row in a), "matrix row type")
    n = len(a[0])
    need(1 <= n <= 4 and all(len(row) == n for row in a), "matrix column/rectangle")
    return tuple(tuple(z(x) for x in row) for row in a)


def eye(n):
    integer(n, 1, 4)
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


def tensor(a, b):
    a, b = matrix(a), matrix(b)
    need(len(a) * len(b) <= 4 and len(a[0]) * len(b[0]) <= 4, "tensor dimension cap")
    return matrix(
        [
            [mul(a[i][j], b[k][h]) for j in range(len(a[0])) for h in range(len(b[0]))]
            for i in range(len(a))
            for k in range(len(b))
        ]
    )


def direct_sum(a, b):
    a, b = matrix(a), matrix(b)
    need(
        len(a) + len(b) <= 4 and len(a[0]) + len(b[0]) <= 4, "direct-sum dimension cap"
    )
    return matrix(
        [list(r) + [ZERO] * len(b[0]) for r in a]
        + [[ZERO] * len(a[0]) + list(r) for r in b]
    )


def quotient(h, p):
    h, p = matrix(h), matrix(p)
    need(
        len(h) == len(h[0]) and len(p[0]) == len(h) and len(p) <= len(h),
        "quotient dimensions",
    )
    psd_minors(h, strict=True)
    return inverse(product(product(p, inverse(h)), star(p)))


def lift(h, p):
    h, p = matrix(h), matrix(p)
    return product(product(inverse(h), star(p)), quotient(h, p))


def energy_control(h, p):
    h, p = matrix(h), matrix(p)
    q, j = quotient(h, p), lift(h, p)
    need(product(p, j) == eye(len(p)), "right inverse")
    need(congruence(h, j) == q, "minimum energy")
    defect = minus(h, congruence(q, p))
    need(product(defect, j) == scale(j, 0), "minimum-energy residual orthogonality")
    return {
        "quotient": encoded_matrix(q),
        "lift": encoded_matrix(j),
        "quotient_minors": psd_minors(q, strict=True),
        "contraction_minors": psd_minors(defect),
    }


def specifications():
    return [
        {
            "id": "source1",
            "G": matrix([[2, (1, 1)], [(1, -1), 3]]),
            "R": matrix([[2, (0, 1)], [(0, -1), 1]]),
            "alpha": 1,
            "pi": matrix([[1, (0, 1)]]),
            "C": matrix([[1, (0, 1)], [0, 1]]),
            "B": matrix([[(1, 1)]]),
        },
        {
            "id": "source2",
            "G": matrix([[1, 0], [0, 2]]),
            "R": matrix([[3, 1], [1, 1]]),
            "alpha": 2,
            "pi": matrix([[1, (1, -1)]]),
            "C": matrix([[1, (1, 1)], [(0, 1), 2]]),
            "B": matrix([[(2, -1)]]),
        },
    ]


def source_value(spec, t):
    need(
        type(spec) is dict and set(spec) == {"id", "G", "R", "alpha", "pi", "C", "B"},
        "source specification schema",
    )
    integer(spec["alpha"], 1, 2)
    t = rational(t)
    need(Q(1, 100) <= t <= 100, "positive source parameter cap")
    if t < 1:
        return scale(source_value(spec, 1 / t), t ** (-spec["alpha"]))
    return plus(spec["G"], spec["R"]) if t <= 2 else spec["G"]


def base_control(spec, t):
    h, g, p = source_value(spec, t), spec["G"], spec["pi"]
    hq, gq = quotient(h, p), quotient(g, p)
    excess = scale(minus(hq, gq), Q(1, 2))
    reciprocal = scale(minus(quotient(source_value(spec, 1 / t), p), gq), Q(1, 2))
    need(
        reciprocal
        == plus(
            scale(excess, t ** spec["alpha"]), scale(gq, (t ** spec["alpha"] - 1) / 2)
        ),
        "affine reciprocity",
    )
    cp, bp = spec["C"], spec["B"]
    pp = product(product(inverse(bp), p), cp)
    hp, gp = congruence(h, cp), congruence(g, cp)
    need(quotient(hp, pp) == congruence(hq, bp), "source quotient covariance")
    need(quotient(gp, pp) == congruence(gq, bp), "vacuum quotient covariance")
    need(
        lift(hp, pp) == product(product(inverse(cp), lift(h, p)), bp),
        "minimum lift covariance",
    )
    return {
        "id": spec["id"],
        "t": str(t),
        "alpha": spec["alpha"],
        "G": encoded_matrix(g),
        "R": encoded_matrix(spec["R"]),
        "H": encoded_matrix(h),
        "pi": encoded_matrix(p),
        "C": encoded_matrix(cp),
        "B": encoded_matrix(bp),
        "transformed_pi": encoded_matrix(pp),
        "vacuum": energy_control(g, p),
        "source": energy_control(h, p),
        "excess": encoded_matrix(excess),
        "excess_minors": psd_minors(excess),
        "reciprocal_excess": encoded_matrix(reciprocal),
        "reciprocal_strict_minors": psd_minors(reciprocal, strict=True),
        "transformed_excess": encoded_matrix(
            scale(minus(quotient(hp, pp), quotient(gp, pp)), Q(1, 2))
        ),
    }


def tensor_control(a, b, t):
    h1, h2 = source_value(a, t), source_value(b, t)
    g, p = tensor(a["G"], b["G"]), tensor(a["pi"], b["pi"])
    h = tensor(h1, h2)
    for m1, m2 in ((h1, h2), (a["G"], b["G"])):
        hm = tensor(m1, m2)
        need(
            quotient(hm, p) == tensor(quotient(m1, a["pi"]), quotient(m2, b["pi"])),
            "tensor quotient",
        )
        need(lift(hm, p) == tensor(lift(m1, a["pi"]), lift(m2, b["pi"])), "tensor lift")
    hr = tensor(source_value(a, 1 / t), source_value(b, 1 / t))
    need(hr == scale(h, t**3), "tensor source weight")
    hq, gq = quotient(h, p), quotient(g, p)
    cq = scale(minus(hq, gq), Q(1, 2))
    c1 = scale(minus(quotient(h1, a["pi"]), quotient(a["G"], a["pi"])), Q(1, 2))
    c2 = scale(minus(quotient(h2, b["pi"]), quotient(b["G"], b["pi"])), Q(1, 2))
    expected = plus(
        plus(
            tensor(c1, quotient(b["G"], b["pi"])), tensor(quotient(a["G"], a["pi"]), c2)
        ),
        scale(tensor(c1, c2), 2),
    )
    need(cq == expected, "tensor excess contains both vacua and cross term")
    return {
        "t": str(t),
        "weight": 3,
        "G": encoded_matrix(g),
        "H": encoded_matrix(h),
        "pi": encoded_matrix(p),
        "source": energy_control(h, p),
        "vacuum": energy_control(g, p),
        "excess": encoded_matrix(cq),
        "reciprocal_quotient": encoded_matrix(quotient(hr, p)),
        "source_excess_minors": psd_minors(minus(h, g)),
    }


def sum_control(a, b, t):
    g = direct_sum(a["G"], b["G"])
    h = direct_sum(source_value(a, t), source_value(b, t))
    p = direct_sum(a["pi"], b["pi"])
    need(
        quotient(h, p)
        == direct_sum(
            quotient(source_value(a, t), a["pi"]), quotient(source_value(b, t), b["pi"])
        ),
        "sum quotient",
    )
    need(
        quotient(g, p)
        == direct_sum(quotient(a["G"], a["pi"]), quotient(b["G"], b["pi"])),
        "sum vacuum",
    )
    need(quotient(scale(h, t), p) == scale(quotient(h, p), t), "common weight1 sum")
    return {
        "t": str(t),
        "weight": 1,
        "second_source_reweighted_to_one": True,
        "source": energy_control(h, p),
        "vacuum": energy_control(g, p),
        "excess_minors": psd_minors(minus(quotient(h, p), quotient(g, p))),
    }


def chain_maps():
    return [
        matrix([[1, 0, 0, (0, 1)], [0, 1, 0, 1], [0, 0, 1, 0]]),
        matrix([[1, (0, 1), 0], [0, 1, 1]]),
        matrix([[1, (1, 1)]]),
    ]


def chain_control(a, b, t):
    h, g = tensor(source_value(a, t), source_value(b, t)), tensor(a["G"], b["G"])
    records = []
    for name, m in (("source", h), ("vacuum", g)):
        current = m
        composite = eye(4)
        total_lift = eye(4)
        stages = []
        for p in chain_maps():
            total_lift = product(total_lift, lift(current, p))
            current = quotient(current, p)
            composite = product(p, composite)
            need(current == quotient(m, composite), "nested quotient associativity")
            need(total_lift == lift(m, composite), "nested minimum lift composition")
            stages.append(
                {
                    "dimension": len(p),
                    "map": encoded_matrix(p),
                    "composite_map": encoded_matrix(composite),
                    "quotient": encoded_matrix(current),
                    "lift": encoded_matrix(total_lift),
                }
            )
        records.append({"kind": name, "stages": stages})
    return {"t": str(t), "chains": records}


def block(a, b, c, d):
    a, b, c, d = map(matrix, (a, b, c, d))
    need(
        len(a) == len(b)
        and len(c) == len(d)
        and len(a[0]) == len(c[0])
        and len(b[0]) == len(d[0]),
        "block dimensions",
    )
    return matrix(
        [list(x) + list(y) for x, y in zip(a, b)]
        + [list(x) + list(y) for x, y in zip(c, d)]
    )


def weighted_sum(matrices, weights):
    need(
        type(matrices) in (list, tuple) and 1 <= len(matrices) <= 3,
        "averaging sample cap",
    )
    need(
        type(weights) in (list, tuple) and len(weights) == len(matrices),
        "averaging weights",
    )
    ws = [rational(w) for w in weights]
    need(all(w > 0 for w in ws), "positive averaging weights")
    result = scale(matrices[0], 0)
    for m, w in zip(matrices, ws):
        result = plus(result, scale(m, w))
    return result


def averaging_data(common):
    need(type(common) is bool, "common-lift flag")
    ds = [
        matrix([[2, 1], [1, 2]]),
        matrix([[3, (0, 1)], [(0, -1), 2]]),
        matrix([[1, 0], [0, 4]]),
    ]
    ls = [
        matrix([[0, 0], [0, 0]]),
        matrix([[Q(1, 2), (0, Q(1, 2))], [0, 0]]),
        matrix([[0, 0], [Q(1, 2), Q(1, 2)]]),
    ]
    if common:
        ls = [ls[1]] * 3
    hs = [
        block(plus(eye(2), congruence(d, l)), product(star(l), d), product(d, l), d)
        for d, l in zip(ds, ls)
    ]
    return ds, ls, hs, [Q(1, 6), Q(2, 6), Q(3, 6)]


def averaging_control(common):
    ds, ls, hs, weights = averaging_data(common)
    for h in hs:
        psd_minors(h, strict=True)
        need(schur(h, 2) == eye(2), "unit pointwise Schur source")
    mean = weighted_sum(hs, weights)
    defect = minus(schur(mean, 2), weighted_sum([schur(h, 2) for h in hs], weights))
    dl = weighted_sum([product(d, l) for d, l in zip(ds, ls)], weights)
    lbar = product(inverse(weighted_sum(ds, weights)), dl)
    variance = weighted_sum(
        [congruence(d, minus(l, lbar)) for d, l in zip(ds, ls)], weights
    )
    need(defect == variance, "averaging lift variance")
    if common:
        need(defect == scale(eye(2), 0), "equal lift zero defect")
    return {
        "common_lift": common,
        "locations": ["1", "3/2", "2"],
        "weights": [str(w) for w in weights],
        "D": [encoded_matrix(d) for d in ds],
        "L": [encoded_matrix(l) for l in ls],
        "H": [encoded_matrix(h) for h in hs],
        "mean_H": encoded_matrix(mean),
        "mean_lift": encoded_matrix(lbar),
        "defect": encoded_matrix(defect),
        "variance": encoded_matrix(variance),
        "determinant": str(determinant(defect)[0]),
        "principal_minors": psd_minors(defect, strict=not common),
    }


def polynomial_product(a, b):
    need(
        type(a) is list and type(b) is list and 1 <= len(a) <= 8 and 1 <= len(b) <= 8,
        "polynomial cap",
    )
    need(
        all(type(v) is int and v.bit_length() <= 4096 for v in a + b),
        "polynomial exact integer",
    )
    result = [0] * (len(a) + len(b) - 1)
    need(len(result) <= 8, "polynomial product cap")
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            charge()
            result[j + k] += x * y
            need(
                result[j + k].bit_length() <= CAPS["integer_bits"],
                "polynomial output bit cap",
            )
    return result


def observation_control():
    # Common denominator 2*s^2*(s-1)*(s-2)*(s-3).
    p = polynomial_product([0, 3], polynomial_product([-1, 1], [-2, 1]))
    p[0] += 3
    p[1] -= 1
    need(p == [3, 5, -9, 3], "Mellin/tensor nonidentity polynomial")
    rows = []
    for s in (4, 5, 6):
        values = [Q(a, 2 * s * (s - a)) for a in (1, 2, 3)]
        difference = values[2] - values[0] * values[1]
        need(
            difference
            == sum(Q(v) * s**j for j, v in enumerate(p))
            / (2 * s * s * (s - 1) * (s - 2) * (s - 3)),
            "observation difference exact",
        )
        rows.append(
            {
                "s": s,
                "L1": str(values[0]),
                "L2": str(values[1]),
                "L3": str(values[2]),
                "L1_times_L2": str(values[0] * values[1]),
                "difference": str(difference),
            }
        )
    return {
        "source_tensor_weights": [1, 2, 3],
        "numerator_ascending": p,
        "denominator": "2*s^2*(s-1)*(s-2)*(s-3)",
        "evaluations": rows,
    }


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "authoring_base": BASE,
        "final_control_design": DESIGN,
        "frozen_sources": BINDINGS,
        "remote_bytes_authenticated": False,
        "references": [
            {
                "url": "https://doi.org/10.1137/0120053",
                "passage": "Anderson, Shorted operators (1971), classical finite maximal shorted form",
            },
            {
                "url": "https://doi.org/10.1137/0128007",
                "passage": "Anderson-Trapp, Shorted Operators II (1975), classical maximality; proof here is native finite algebra",
            },
            {
                "url": "https://doi.org/10.1016/0024-3795(79)90040-5",
                "passage": "Ando, Generalized Schur complements (1979), classical quotient context; not an imported unread theorem",
            },
        ],
        "contract": {
            "arithmetic_class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
            "caps": CAPS,
            "analytic_claims_machine_certified": False,
            "native_theta_evaluations": False,
            "tensor_closed_source_class": "locally bounded measurable",
            "weaker_quotient_class": "locally integrable measurable",
            "local_L1_tensor_closure": False,
            "matrices_are_preregistered_synthetic_sources": True,
            "full_quantifiers_require_written_proof": True,
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
    specs = specifications()
    parameters = (Q(3, 2), Q(2), Q(3))
    for sp in specs:
        psd_minors(sp["G"], strict=True)
        psd_minors(sp["R"], strict=True)
    bases = [base_control(sp, t) for sp in specs for t in parameters]
    tensors = [tensor_control(*specs, t) for t in parameters]
    sums = [sum_control(*specs, t) for t in parameters]
    chains = [chain_control(*specs, t) for t in parameters]
    averages = [averaging_control(common) for common in (False, True)]
    observations = observation_control()
    need(
        (len(bases), len(tensors), len(sums), len(chains), len(averages))
        == (6, 3, 3, 3, 2),
        "complete preregistered coverage",
    )
    out = {
        "schema": STEM + "-v1",
        "contract": manifest()["contract"],
        "sources": BINDINGS,
        "base_cells": bases,
        "tensor_cells": tensors,
        "same_weight_sums": sums,
        "nested_chains": chains,
        "averaging": averages,
        "observation": observations,
        "unequal_weight_sum": {
            "t": "2",
            "reciprocal": "1/2",
            "block_scalings": [2, 4],
            "common_scalar": False,
        },
        "regularity_failure": {
            "local_exponent": "2/3",
            "tensor_exponent": "4/3",
            "local_L1_tensor_closed": False,
        },
        "coverage": {
            "base": 6,
            "tensor": 3,
            "direct_sum": 3,
            "chains": 3,
            "stages_per_chain": 3,
            "source_and_vacuum_chains": True,
            "averaging": 2,
            "observation_points": 3,
            "observation_polynomials": 1,
            "unequal_weight_countercontrols": 1,
            "parameters": ["3/2", "2", "3"],
            "matrix_dimension_max": 4,
        },
        "not_claimed": [
            "analytic theorem machine certification",
            "actual theta evaluation",
            "tensor Mellin equals product of Mellins",
            "period-side Schur interchange",
            "preferred flag",
            "Euler product",
            "new automorphic representation",
            "RH",
        ],
        "work_units": WORK,
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
        "full source-authenticated primitive replay",
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
            "PASS 6 base,3 tensor,3 sums,3 nested chains,2 averaging,3 observation controls"
        )
        print("fixture_sha256_lf=" + digest(lf(raw)))


if __name__ == "__main__":
    main()
