"""Non-author standard-library reconstruction of frozen MP finite arithmetic.

No scientific producer or test module is imported. This is not an evaluation
of a theta integral or a machine proof of the analytic theorems.
"""

import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DIR = "research/l-families/atlas/generalized/"
SCIENCE = "fdd349dcf6ba1b104e27866ae66b4c89752d5f05"
LOCKS = {
    DIR
    + "CUSP_MATRIX_PERIOD_POSITIVITY.md": "fabb13f35e0f6a45ddbc3b5f54f0376e9c0aec5d75b44ae9b4ae10cf17136c0c",
    DIR
    + "cusp_matrix_period_positivity.py": "719f7b8fa6d52efb88ec0d7162a15a5c146b51256eacdfef514b6ca12b788eed",
    DIR
    + "cusp_matrix_period_positivity.json": "021b0bd08e96fa4a58dfac352f4833ef86587ea273e6d656bcda8c19bf789689",
    DIR
    + "cusp_matrix_period_positivity.sources.json": "82a568b0d338cf45a1168206fdecbc9132bbb57c28684b22777c3768e4f3b17b",
    "tests/test_cusp_matrix_period_positivity.py": "0c681025da1e6957e412abd853052454ef5c8f03c56b3c9c64cb8379bf3764a5",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def digest(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def authenticate():
    for path, wanted in LOCKS.items():
        frozen = subprocess.check_output(
            ["git", "show", SCIENCE + ":" + path], cwd=ROOT
        )
        require(digest(frozen) == wanted, "frozen science lock")
        require(digest((ROOT / path).read_bytes()) == wanted, "resident science lock")
    value = json.loads(
        (ROOT / (DIR + "cusp_matrix_period_positivity.json")).read_bytes()
    )
    seal = value.pop("payload_sha256")
    require(hashlib.sha256(canonical(value)).hexdigest() == seal, "payload seal")
    value["payload_sha256"] = seal
    for path, wanted in value["artifact_sha256_lf"].items():
        require(wanted == LOCKS[path], "artifact lock")
    for row in value["sources"]:
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT
        )
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and digest(raw) == row["sha256_lf"], "source lock"
        )
    require(len(value["sources"]) == 7, "seven literal source bindings")
    return value


class C:
    """Exact Gaussian rational; deliberately no float or complex conversion."""

    def __init__(self, re=0, im=0):
        if isinstance(re, C):
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = Q(re), Q(im)

    def __add__(self, other):
        other = C(other)
        return C(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.re, -self.im)

    def __sub__(self, other):
        return self + -C(other)

    def __mul__(self, other):
        other = C(other)
        return C(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = C(other)
        norm = other.re**2 + other.im**2
        require(norm > 0, "nonzero exact divisor")
        product = self * other.conjugate()
        return C(product.re / norm, product.im / norm)

    def __eq__(self, other):
        other = C(other)
        return (self.re, self.im) == (other.re, other.im)

    def conjugate(self):
        return C(self.re, -self.im)


def matrix(rows):
    return [[C(x) for x in row] for row in rows]


def unpack(rows):
    return [[C(re, im) for re, im in row] for row in rows]


def star(a):
    return [[x.conjugate() for x in row] for row in zip(*a)]


def product(a, b):
    return [
        [sum((x * y for x, y in zip(row, column)), C()) for column in zip(*b)]
        for row in a
    ]


def scale(a, c):
    return [[x * c for x in row] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(row, col)] for row, col in zip(a, b)]


def subtract(a, b):
    return add(a, scale(b, -1))


def eye(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def minor(a, row, column):
    return [
        [x for j, x in enumerate(r) if j != column] for i, r in enumerate(a) if i != row
    ]


def det(a):
    if not a:
        return C(1)
    return sum(
        ((-1) ** j * x * det(minor(a, 0, j)) for j, x in enumerate(a[0]) if x != 0), C()
    )


def inverse(a):
    determinant = det(a)
    require(determinant != 0, "invertible exact matrix")
    return [
        [((-1) ** (i + j) * det(minor(a, j, i))) / determinant for j in range(len(a))]
        for i in range(len(a))
    ]


def quotient(a, r):
    # The quotient is the inverse of the restricted inverse metric.
    # This differs from the producer's direct block-elimination route.
    inv = inverse(a)
    return inverse([row[:r] for row in inv[:r]])


def congruence(a, change):
    return product(product(star(change), a), change)


def check_minors(a, records, strict=False):
    expected = [
        list(ind)
        for n in range(1, len(a) + 1)
        for ind in itertools.combinations(range(len(a)), n)
    ]
    require([row["indices"] for row in records] == expected, "complete minor coverage")
    for row in records:
        indices = row["indices"]
        value = det([[a[i][j] for j in indices] for i in indices])
        require(value == C(row["determinant"]), "exact principal determinant")
        require(
            value.im == 0 and (value.re > 0 if strict else value.re >= 0), "minor sign"
        )


def convolution(a, b, n):
    return [
        sum(
            (a[j] * b[k - j] for j in range(k + 1) if j < len(a) and k - j < len(b)),
            Q(0),
        )
        for k in range(n + 1)
    ]


def native(value):
    # Algebraic modular identity, independent of the producer's Euler product.
    e4 = [Q(1)] + [
        Q(240 * sum(d**3 for d in range(1, n + 1) if n % d == 0)) for n in range(1, 5)
    ]
    e6 = [Q(1)] + [
        Q(-504 * sum(d**5 for d in range(1, n + 1) if n % d == 0)) for n in range(1, 5)
    ]
    e43, e62 = convolution(convolution(e4, e4, 4), e4, 4), convolution(e6, e6, 4)
    delta = [(x - y) / 1728 for x, y in zip(e43, e62)]
    f0, b = convolution(delta, e43, 4), convolution(delta, delta, 4)
    g = [x - 696 * y for x, y in zip(f0, b)]
    for key, data in (("delta", delta), ("E4", e4), ("f0", f0), ("b", b), ("g", g)):
        require(data == value[key], "native modular coefficients")
    rows = [[g[n], b[n]] for n in range(1, 5)]
    require(rows == value["q_rows"], "native q rows")
    a, b3 = rows[2]
    c, d = rows[3]
    # Expansion along the first two unit-pivot rows of [a(n),log(n)a(n)].
    require(
        [a * d - 2 * b3 * c, 2 * b3 * c] == [1371005088, -1159692288],
        "formal log coefficients",
    )
    require(
        value["formal_log_determinant_L2_L3"]
        == [[1, 1, 1371005088], [2, 0, -1159692288]],
        "formal coefficient encoding",
    )
    return rows


def all_derivatives(records):
    # Taylor composition F(q exp(h)); r-th coefficient times r! equals (q d/dq)^r F.
    # Neither the producer's rational-numerator recurrence nor the test's
    # Stirling-number expansion is used.
    table = {}
    for q in (Q(1, 3), Q(1, 2), Q(2, 3)):
        x = [q / math.factorial(j) for j in range(17)]
        denom = list(x)
        denom[0] += 1
        reciprocal = [1 / denom[0]]
        for n in range(1, 17):
            reciprocal.append(
                -sum(denom[j] * reciprocal[n - j] for j in range(1, n + 1)) / denom[0]
            )
        result = convolution(convolution(x, x, 16), reciprocal, 16)
        for r in range(1, 17):
            table[(r, str(q))] = result[r] * math.factorial(r)
    require(
        [(r["order"], r["q"]) for r in records]
        == [(r, str(q)) for r in range(1, 17) for q in (Q(1, 3), Q(1, 2), Q(2, 3))],
        "48 derivative coverage",
    )
    for record in records:
        require(
            table[(record["order"], record["q"])] == Q(record["value"]),
            "Taylor derivative",
        )
    negatives = [(r["order"], r["q"]) for r in records if Q(r["value"]) < 0]
    require(
        len(negatives) == 12 and negatives[0] == (7, "1/3"), "retained negative cells"
    )
    return negatives


def gram(rows, weights, frequencies, order):
    return product(
        star(rows),
        [
            [x * w * nu**order for x in row]
            for row, w, nu in zip(rows, weights, frequencies)
        ],
    )


def feature_records(records, native_rows):
    definitions = [
        (
            [[1, 0], [1, 1], [0, 1]],
            [0, 1, 2],
            [1, Q(1, 2), Q(1, 4)],
            [[1, C(0, 1)], [0, 1]],
        ),
        (
            native_rows,
            [1, 2, 3, 4],
            [Q(1, n**25) for n in range(1, 5)],
            [[1, C(1, 1)], [C(0, 1), 2]],
        ),
        (
            [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1], [1, -1, 2]],
            [0, Q(1, 2), 1, Q(3, 2), 2],
            [Q(1, 3**j) for j in range(5)],
            [[1, C(0, 1), 0], [0, 1, 1], [1, 0, 1]],
        ),
    ]
    require([r["id"] for r in records] == [1, 2, 3], "feature coverage")
    originals = {}
    ranks = []
    for record, (rows, nu, weights, basis) in zip(records, definitions):
        rows, basis = matrix(rows), matrix(basis)
        require(
            rows == unpack(record["rows"]) and basis == unpack(record["basis"]),
            "declared features",
        )
        require(
            nu == list(map(Q, record["frequencies"]))
            and weights == list(map(Q, record["weights"])),
            "declared proxy frequencies and weights",
        )
        moments = [gram(rows, weights, nu, j) for j in range(3)]
        require(moments == [unpack(m) for m in record["moments"]], "fresh moment sums")
        m0, m1, m2 = moments
        variance = subtract(m2, product(product(m1, inverse(m0)), m1))
        require(
            variance == unpack(record["variance"]) == unpack(record["residual_gram"]),
            "variance residual",
        )
        regression = product(inverse(m0), m1)
        residual = subtract(
            [[x * f for x in row] for row, f in zip(rows, nu)],
            product(rows, regression),
        )
        require(
            gram(residual, weights, nu, 0) == variance,
            "independent regression residual Gram",
        )
        require(
            [congruence(m, basis) for m in moments]
            == [unpack(m) for m in record["transformed_moments"]],
            "moment congruence",
        )
        require(
            congruence(variance, basis) == unpack(record["transformed_variance"]),
            "variance congruence",
        )
        block = [a + b for a, b in zip(m0, m1)] + [a + b for a, b in zip(m1, m2)]
        check_minors(m0, record["moment0_positive_minors"], True)
        check_minors(block, record["block_positive_semidefinite_minors"])
        check_minors(variance, record["variance_positive_semidefinite_minors"])
        originals[record["id"]] = m0
        ranks.append(str(det(variance).re))
    require(
        ranks == ["0", "45309363075729/8557913953170404494528", "0"],
        "singular controls retained",
    )
    return originals, ranks


def reciprocal_records(records, originals):
    expected = [
        (i, r, str(t))
        for i, n in ((1, 2), (2, 2), (3, 3))
        for r in range(1, n)
        for t in (Q(3, 2), Q(2), Q(5))
    ]
    require(
        [(v["system"], v["quotient_dimension"], v["t"]) for v in records] == expected,
        "12 pairs coverage",
    )
    for record in records:
        m0, r, t = (
            originals[record["system"]],
            record["quotient_dimension"],
            Q(record["t"]),
        )
        n = len(m0)
        g, h = eye(n), add(eye(n), m0)
        q = subtract(quotient(h, r), eye(r))
        qr = subtract(quotient(scale(h, t), r), eye(r))
        require(m0 == unpack(record["R_t"]), "pair density")
        require(
            subtract(scale(h, t), g) == unpack(record["R_reciprocal"]), "paired density"
        )
        require(
            q == unpack(record["quotient_vacuum_difference"])
            and qr == unpack(record["reciprocal_difference"]),
            "inverse-metric quotient route",
        )
        require(
            q == add(scale(qr, 1 / t), scale(eye(r), 1 / t - 1)), "affine reciprocity"
        )
        change = eye(n)
        change[0][0], change[-1][-1], change[-1][0] = C(1, 1), C(2), C(Q(1, 2), 1)
        if r >= 2:
            change[0][1] = C(0, 1)
        require(change == unpack(record["adapted_basis"]), "flag basis")
        gn, hn = congruence(g, change), congruence(h, change)
        require(gn == unpack(record["transformed_vacuum"]), "transformed vacuum")
        qn = subtract(quotient(hn, r), quotient(gn, r))
        require(qn == unpack(record["transformed_difference"]), "transformed quotient")
        require(
            qn == congruence(q, [row[:r] for row in change[:r]]),
            "intrinsic flag congruence",
        )
        for mat, key in (
            (q, "positive_minors"),
            (qr, "reciprocal_positive_minors"),
            (qn, "congruence_positive_minors"),
        ):
            check_minors(mat, record[key], True)
        require(record["flag_dimension"] == n - r, "flag dimension")


def main():
    value = authenticate()
    rows = native(value["native"])
    negatives = all_derivatives(value["derivative_panel"])
    nodes = (Q(1, 3), Q(1, 2), Q(2, 3))
    kernel = matrix([[1 + (x * y) ** 2 / (1 + x * y) for y in nodes] for x in nodes])
    record = value["post_scout_kernel"]
    require(
        kernel == unpack(record["matrix"]) and det(kernel) == C(Q(-81, 8808800)),
        "kernel counterfeit",
    )
    leading = [C(1)] + [det([row[:r] for row in kernel[:r]]) for r in range(1, 4)]
    require(
        [str((leading[r] / leading[r - 1]).re) for r in range(1, 4)]
        == record["LDL_pivots"],
        "LDL",
    )
    require(all(2 * q * q < 1 for q in nodes), "kernel points in Omega")
    originals, determinants = feature_records(value["features"], rows)
    reciprocal_records(value["soft_reciprocal_pairs"], originals)
    print(
        json.dumps(
            {
                "verdict": "PASS",
                "science": SCIENCE,
                "source_pins": 7,
                "derivatives": 48,
                "negative_cells": negatives,
                "feature_systems": 3,
                "variance_determinants": determinants,
                "reciprocal_pairs": 12,
                "no_author_imports": True,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
