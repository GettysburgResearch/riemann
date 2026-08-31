"""Exact native Segre maps and recurrence/specialization controls; no fitted ranks."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "SEGRE_RECURRENCE_SYZYGY_BRIDGE.md"
MANIFEST = HERE / "segre_recurrence_syzygy_bridge.sources.json"
FIXTURE = HERE / "segre_recurrence_syzygy_bridge.json"
TEST = ROOT / "tests/test_segre_recurrence_syzygy_bridge.py"
MAX_BYTES = 2097152
MAX_JSON_DEPTH = 32
MAX_BITS = 4096
MAX_POLY = 129
MAX_WORDS = 19683
MAX_BLOCK_ROWS = 216
MAX_BLOCK_COLS = 512
EXPECTED_MANIFEST = json.loads(r"""{
  "schema": "segre-recurrence-syzygy-sources-v1",
  "parents": [
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/SEGRE_KOSZUL_LIE_PARENT.md",
      "git_blob": "6036546493e416fdb44e57e6c9746e9a92844a5c",
      "sha256_lf": "7cbc3f7f069168fd38203c8fe5fdddd15bd60f326a329c2401b87caaeb4a6b3d",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/segre_koszul_lie_parent.py",
      "git_blob": "d7452ee72b35aa0fa15a2cd1d20cb55d696bb236",
      "sha256_lf": "58c95e9840d8aff56fb45ffea795fe66fe029a1da9cb9d09974c169bd898bed0",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/segre_koszul_lie_parent.json",
      "git_blob": "9836bf23250087bedacee2877bf44da07f61637b",
      "sha256_lf": "d61ae323b519658491e60b89d9332a3b605b439a590f667f2f3ece172e4e3f1c",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/segre_koszul_lie_parent.sources.json",
      "git_blob": "635f70f3b4833cff5aac9b83fdab2824d15446cb",
      "sha256_lf": "2712c1a6722e01b64d4c63c3ff54e3cdba2b70a5bcb8fa5c023b22bccedcaf72",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "tests/test_segre_koszul_lie_parent.py",
      "git_blob": "c5d13f16d7cb3e2ff1f6982f4e26871de43df7af",
      "sha256_lf": "2613530f60069d5c30c7f40f561135c7ff18eaff8a8570e7512aa9729c85e37c",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/SEGRE_KOSZUL_LIE_PARENT_AUDIT.md",
      "git_blob": "60ba829647a91df764f819617828d33f5f213b20",
      "sha256_lf": "637219e38945c0f5c53b63693922222ac9b4bae5da498a91d2bddfec24bd1406",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md",
      "git_blob": "3932273279d43ffa34d929247152cb43b932fa1d",
      "sha256_lf": "50daa223c5b6d0f061d771f24775a0a7a2d470f9185a1d6304f3b49e9fc799bc",
      "current_copy_required": true
    },
    {
      "commit": "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e",
      "path": "research/l-families/atlas/generalized/GRADED_PARENT_GLOBAL_BOUNDARY.md",
      "git_blob": "1a49f7075b590e16c8367c7b2ef8b8d5b77c9819",
      "sha256_lf": "c545339d97aead843ed6591a8a2b8dadc27e0518607fa03b4d7d68b088ec1eef",
      "current_copy_required": true
    },
    {
      "commit": "64c8664a2fee08ae2e249743d6f784a7bec61b83",
      "path": "research/l-families/atlas/generalized/SEGRE_RECURRENCE_SYZYGY_BRIDGE.md",
      "git_blob": "dbdf5185b6458c1a1cd9d13a3708c4b90e773e97",
      "sha256_lf": "f3462a9815a8b426749f1fa5db9c2a8746315e532b364899f199ac07b667edb0",
      "current_copy_required": false
    }
  ],
  "prior_art": [
    {
      "id": "SNOWDEN",
      "title": "Syzygies of Segre embeddings",
      "url": "https://websites.umich.edu/~asnowden/papers/segre-111810.pdf",
      "locator": "section 1.1; Lemma 3.3; section 4.7 Figure 1",
      "role": "canonical Tor modules; additive equivariant Hilbert numerator; classical cubic character"
    },
    {
      "id": "GORBOUNOV_SCHECHTMAN",
      "title": "Homological Algebra and Divergent Series",
      "url": "https://sigma-journal.com/2009/034/sigma09-034.pdf",
      "locator": "sections 3.4.1--3.4.5",
      "role": "classical infinite Koszul--Lie Euler product, not a finite syzygy superdeterminant"
    }
  ],
  "external_context": {
    "repository": "gfreund123/riemann",
    "commit": "d4fa9dcc88beddbf0dbb978e1c64091086bd8825",
    "compared_base": "ac1cc5eaf229087b6d805e908897c7c8c99a58b7",
    "changed_algebraic_files": 0,
    "role": "read-only comparison and terminology context, not an imported theorem or machine-authenticated dependency",
    "paths": [
      "standalone/2026-08-31-deformation-spectrum/PROOF.md",
      "standalone/2026-08-31-defect-codimension-law/PROOF.md"
    ]
  }
}""")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high, name="integer"):
    require(type(value) is int and low <= value <= high, "invalid " + name)
    return value


def exact(value, bits=MAX_BITS):
    require(type(value) in (int, Fraction), "exact scalar type")
    value = Fraction(value)
    require(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= bits,
        "exact scalar bit cap",
    )
    return value


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode()


def render(value):
    """Keep exact weight-block rows compact without obscuring the report tree."""

    def pretty(item, level):
        compact = canonical(item).decode()
        if len(compact) <= 180 or type(item) not in (dict, list):
            return compact
        indent = "  " * (level + 1)
        if type(item) is list:
            rows = [pretty(child, level + 1) for child in item]
            opening, closing = "[", "]"
        else:
            rows = [
                canonical(key).decode() + ": " + pretty(item[key], level + 1)
                for key in sorted(item)
            ]
            opening, closing = "{", "}"
        return (
            opening
            + "\n"
            + indent
            + (",\n" + indent).join(rows)
            + "\n"
            + "  " * level
            + closing
        )

    return pretty(value, 0) + "\n"


def same_json(actual, expected):
    require(canonical(actual) == canonical(expected), "typed canonical replay differs")


def digest(raw):
    require(type(raw) is bytes, "digest bytes type")
    return hashlib.sha256(raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def bounded_bytes(path):
    require(path.stat().st_size <= MAX_BYTES, "file byte cap")
    with path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    require(len(raw) <= MAX_BYTES, "file byte cap")
    return raw


def strict_json(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap/type")
    depth = 0
    quoted = escaped = False
    for byte in raw:
        if quoted:
            if escaped:
                escaped = False
            elif byte == 92:
                escaped = True
            elif byte == 34:
                quoted = False
        elif byte == 34:
            quoted = True
        elif byte in (91, 123):
            depth += 1
            require(depth <= MAX_JSON_DEPTH, "JSON nesting cap")
        elif byte in (93, 125):
            depth -= 1
            require(depth >= 0, "JSON unmatched close")

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def bad(value):
        raise ValueError("floating/nonfinite JSON scalar")

    def parse_int(value):
        require(len(value) <= 1234, "JSON integer length cap")
        return integer(int(value), -(1 << MAX_BITS), 1 << MAX_BITS)

    try:
        return json.loads(
            raw,
            object_pairs_hook=pairs,
            parse_float=bad,
            parse_constant=bad,
            parse_int=parse_int,
        )
    except (RecursionError, UnicodeError) as error:
        raise ValueError("invalid JSON encoding/depth") from error


def source_locks():
    same_json(strict_json(bounded_bytes(MANIFEST)), EXPECTED_MANIFEST)
    for row in EXPECTED_MANIFEST["parents"]:
        target = row["commit"] + ":" + row["path"]
        try:
            blob = subprocess.check_output(
                ["git", "rev-parse", "--verify", target], cwd=ROOT, text=True
            ).strip()
            require(blob == row["git_blob"], "frozen source blob mismatch")
            size = int(
                subprocess.check_output(
                    ["git", "cat-file", "-s", blob], cwd=ROOT, text=True
                )
            )
            require(size <= MAX_BYTES, "frozen source byte cap")
            raw = subprocess.check_output(["git", "show", target], cwd=ROOT)
        except subprocess.CalledProcessError as error:
            raise ValueError("frozen source unavailable") from error
        require(
            len(raw) <= MAX_BYTES and digest(raw) == row["sha256_lf"],
            "frozen source digest mismatch",
        )
        if row["current_copy_required"]:
            require(
                digest(bounded_bytes(ROOT / row["path"])) == row["sha256_lf"],
                "current parent source mismatch",
            )
    return EXPECTED_MANIFEST


def preflight(ranks):
    require(type(ranks) in (tuple, list) and 1 <= len(ranks) <= 3, "rank vector")
    ranks = tuple(integer(n, 1, 3, "rank") for n in ranks)
    size = prod(ranks)
    require(size**3 <= MAX_WORDS, "cubic word cap")
    return ranks, size


def sparse_basis(columns, rows):
    integer(rows, 0, MAX_BLOCK_ROWS, "matrix rows")
    require(type(columns) is list and len(columns) <= MAX_BLOCK_COLS, "matrix columns")
    pivots = {}
    for raw in columns:
        require(type(raw) is dict, "sparse column")
        column = {}
        for key, value in raw.items():
            integer(key, 0, rows - 1, "row index")
            value = exact(value)
            if value:
                column[key] = value
        while column:
            pivot = min(column)
            if pivot not in pivots:
                unit = column[pivot]
                pivots[pivot] = {a: exact(b / unit) for a, b in column.items()}
                break
            multiple = column[pivot]
            for a, b in pivots[pivot].items():
                value = exact(column.get(a, Fraction(0)) - multiple * b)
                if value:
                    column[a] = value
                else:
                    column.pop(a, None)
    return pivots


def character_rows(character):
    return [
        {"weight": [list(block) for block in weight], "multiplicity": value}
        for weight, value in sorted(character.items())
        if value
    ]


def predicted_character(ranks, degree):
    """Independent tableau/Schur construction, never a matrix-rank oracle."""
    ranks, _ = preflight(ranks)
    require(len(ranks) == 3, "three-factor character only")
    integer(degree, 2, 3, "character degree")

    def schur(n, shape):
        result = Counter()
        if shape == "s":
            for row in combinations_with_replacement(range(n), degree):
                result[row] += 1
        elif shape == "a":
            for row in combinations(range(n), degree):
                result[row] += 1
        else:
            require(degree == 3 and shape == "b", "tableau shape")
            for a, b, c in product(range(n), repeat=3):
                if a <= b and a < c:
                    result[tuple(sorted((a, b, c)))] += 1
        return result

    shapes = (
        [("s", "a", "a")]
        if degree == 2
        else [("s", "b", "a"), ("b", "b", "a"), ("b", "a", "a")]
    )
    result = Counter()
    for shape in shapes:
        for ordered in sorted(set(permutations(shape))):
            blocks = [schur(n, s) for n, s in zip(ranks, ordered)]
            for weight in product(*(block.keys() for block in blocks)):
                result[weight] += prod(block[key] for block, key in zip(blocks, weight))
    if degree == 3:
        blocks = [schur(n, "b") for n in ranks]
        for weight in product(*(block.keys() for block in blocks)):
            result[weight] += 2 * prod(block[key] for block, key in zip(blocks, weight))
    return result


def native_cubic(ranks=(3, 3, 3)):
    ranks, size = preflight(ranks)
    axes = list(product(*(range(n) for n in ranks)))

    def weight(word):
        return tuple(tuple(sorted(axes[a][i] for a in word)) for i in range(len(ranks)))

    pairgroups = defaultdict(list)
    for pair in combinations_with_replacement(range(size), 2):
        pairgroups[weight(pair)].append(pair)
    quadrics = [(pair, pairs[0]) for pairs in pairgroups.values() for pair in pairs[1:]]
    qchar = Counter(weight(pair) for pair, _ in quadrics)
    cubic = defaultdict(list)
    for monomial in combinations_with_replacement(range(size), 3):
        cubic[weight(monomial)].append(monomial)
    syzcols = defaultdict(list)
    for x in range(size):
        for left, right in quadrics:
            a, b = tuple(sorted((x,) + left)), tuple(sorted((x,) + right))
            syzcols[weight(a)].append({a: 1, b: -1})

    ordered_pairs = defaultdict(list)
    triples = defaultdict(list)
    for pair in product(range(size), repeat=2):
        ordered_pairs[weight(pair)].append(pair)
    for word in product(range(size), repeat=3):
        triples[weight(word)].append(word)
    dualcols = defaultdict(list)
    for pairs in ordered_pairs.values():
        for c in range(size):
            left = {(a, b, c): 1 for a, b in pairs}
            right = {(c, a, b): 1 for a, b in pairs}
            dualcols[weight(next(iter(left)))].append(left)
            dualcols[weight(next(iter(right)))].append(right)

    syzchar, liechar, dualchar = Counter(), Counter(), Counter()
    blocks = []
    totals = Counter()
    for w, words in sorted(triples.items()):
        comm = cubic[w]
        ci = {monomial: i for i, monomial in enumerate(comm)}
        sc = [
            {ci[monomial]: value for monomial, value in col.items()}
            for col in syzcols[w]
        ]
        sr = len(sparse_basis(sc, len(comm)))
        require(sr == len(comm) - 1, "quadrics do not span cubic ideal")
        syz = len(sc) - sr
        syzchar[w] = syz
        wi = {word: i for i, word in enumerate(words)}
        dc = [{wi[word]: value for word, value in col.items()} for col in dualcols[w]]
        dr = len(sparse_basis(dc, len(words)))
        brackets = []
        for a, b, c in words:
            col = Counter()
            for word, sign in (
                ((a, b, c), 1),
                ((a, c, b), 1),
                ((b, c, a), -1),
                ((c, b, a), -1),
            ):
                col[wi[word]] += sign
            brackets.append(dict(col))
        after = len(sparse_basis(dc + brackets, len(words)))
        liechar[w] = after - dr
        dualchar[w] = len(words) - dr

        # Independent bar d3 is an incidence matrix, with one +1 and one -1.
        vertices = {}
        edges = []
        for a, b, c in words:
            left = (0, weight((a, b)), c)
            right = (1, a, weight((b, c)))
            for vertex in (left, right):
                if vertex not in vertices:
                    vertices[vertex] = len(vertices)
            edges.append((vertices[left], vertices[right]))
        parent = list(range(len(vertices)))

        def find(a, forest=parent):
            while forest[a] != a:
                forest[a] = forest[forest[a]]
                a = forest[a]
            return a

        for a, b in edges:
            a, b = find(a), find(b)
            parent[a] = b
        components = len({find(a) for a in range(len(vertices))})
        require(components == 1, "bar off-diagonal homology")
        bar_rank = len(vertices) - components
        require(bar_rank == dr, "bar/dual independent rank mismatch")
        require(after - dr == syz, "Lie/ambient-syzygy character mismatch")
        blocks.append(
            {
                "weight": [list(x) for x in w],
                "symmetric_cubic_rows": len(comm),
                "syzygy_columns": len(sc),
                "syzygy_map_rank": sr,
                "tensor_words": len(words),
                "dual_columns": len(dc),
                "dual_ideal_rank": dr,
                "cubic_lie_dimension": after - dr,
                "bar_vertices": len(vertices),
                "bar_components": components,
            }
        )
        totals.update(
            {
                "symmetric_cubic_rows": len(comm),
                "syzygy_columns": len(sc),
                "syzygy_map_rank": sr,
                "tensor_words": len(words),
                "dual_columns": len(dc),
                "dual_ideal_rank": dr,
                "cubic_lie_dimension": after - dr,
                "bar_vertices": len(vertices),
            }
        )
    if len(ranks) == 3:
        require(+qchar == +predicted_character(ranks, 2), "quadratic Schur prediction")
        require(+syzchar == +predicted_character(ranks, 3), "cubic Schur prediction")
    return {
        "ranks": list(ranks),
        "generators": size,
        "quadrics": len(quadrics),
        "totals": dict(totals),
        "cubic_syzygies": sum(syzchar.values()),
        "cubic_dual_algebra": sum(dualchar.values()),
        "quadratic_character": character_rows(qchar),
        "cubic_character": character_rows(syzchar),
        "cubic_dual_character": character_rows(dualchar),
        "blocks": blocks,
    }


def poly(values):
    require(
        type(values) in (tuple, list) and 1 <= len(values) <= MAX_POLY, "polynomial cap"
    )
    values = [exact(v) for v in values]
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def padd(a, b):
    a, b = poly(a), poly(b)
    return poly(
        [
            (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
            for i in range(max(len(a), len(b)))
        ]
    )


def pscale(a, scalar):
    scalar = exact(scalar)
    return poly([v * scalar for v in poly(a)])


def pmul(a, b):
    a, b = poly(a), poly(b)
    require(len(a) + len(b) - 1 <= MAX_POLY, "product degree cap")
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = exact(out[i + j] + x * y)
    return poly(out)


def ppow(a, exponent):
    exponent = integer(exponent, 0, 27, "polynomial exponent")
    out = [Fraction(1)]
    for _ in range(exponent):
        out = pmul(out, a)
    return out


def pdiv(a, b):
    a, b = poly(a), poly(b)
    require(b != [0], "zero polynomial divisor")
    quotient = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        j = len(a) - len(b)
        c = exact(a[-1] / b[-1])
        quotient[j] = exact(quotient[j] + c)
        a = padd(a, [0] * j + pscale(b, -c))
    return poly(quotient), poly(a)


def reduced(numerator, denominator):
    numerator, denominator = poly(numerator), poly(denominator)
    require(numerator[0] == denominator[0] == 1, "constant-one normalization")
    a, b = numerator, denominator
    while b != [0]:
        a, b = b, pdiv(a, b)[1]
    common = pscale(a, 1 / a[0])
    p, rp = pdiv(numerator, common)
    q, rq = pdiv(denominator, common)
    require(rp == rq == [0], "gcd division")
    return p, q, common


def series(denominator, count):
    denominator = poly(denominator)
    count = integer(count, 1, 33, "series length")
    require(denominator[0] == 1, "series normalization")
    answer = [Fraction(1)]
    for r in range(1, count):
        answer.append(
            exact(
                -sum(
                    denominator[j] * answer[r - j]
                    for j in range(1, min(r + 1, len(denominator)))
                )
            )
        )
    return answer


def encoded(values):
    return [[v.numerator, v.denominator] for v in poly(values)]


def weak(total, length):
    if length == 1:
        return [(total,)]
    return [
        (a,) + tail for a in range(total + 1) for tail in weak(total - a, length - 1)
    ]


def recurrence_panel(eigenvalues, power):
    require(
        type(eigenvalues) in (tuple, list) and 1 <= len(eigenvalues) <= 3,
        "eigenvalue vector",
    )
    eigenvalues = tuple(exact(v, 32) for v in eigenvalues)
    require(all(v != 0 for v in eigenvalues), "invertible input required")
    power = integer(power, 1, 3, "coefficient power")
    source = [Fraction(1)]
    for value in eigenvalues:
        source = pmul(source, [1, -value])
    weights = [
        prod(v**a for v, a in zip(eigenvalues, nu))
        for nu in weak(power, len(eigenvalues))
    ]
    denominator = [Fraction(1)]
    for value in weights:
        denominator = pmul(denominator, [1, -value])
    h = series(source, 2 * len(weights) + 1)
    coefficients = [exact(v**power) for v in h]
    product_coeff = pmul(denominator, coefficients)
    numerator = poly(product_coeff[: len(weights)])
    require(
        all(v == 0 for v in product_coeff[len(weights) : len(coefficients)]),
        "universal recurrence prefix failed",
    )
    p, q, common = reduced(numerator, denominator)
    require(len(q) - len(p) == len(eigenvalues), "backward codimension")
    hankel_columns = [
        {i: coefficients[i + j] for i in range(len(weights))}
        for j in range(len(weights))
    ]
    hankel_rank = len(sparse_basis(hankel_columns, len(weights)))
    require(hankel_rank == len(q) - 1, "finite Hankel recurrence order")
    return {
        "eigenvalues": encoded(list(eigenvalues)),
        "power": power,
        "finite_Hankel_rank": hankel_rank,
        "universal_denominator": encoded(denominator),
        "universal_numerator": encoded(numerator),
        "reduced_denominator": encoded(q),
        "reduced_numerator": encoded(p),
        "cancelled_factor": encoded(common),
    }


def slice_polynomials(x):
    x = exact(x, 32)
    require(abs(x) <= 16, "slice magnitude cap")
    cj = (x, x * x - 2, x * x * x - 3 * x)
    denominator = [Fraction(1), Fraction(-1)]
    for c in cj:
        denominator = pmul(denominator, [1, -c, 1])
    b = 2 * x * x + 5 * x + 2
    c = x * x * x + 6 * x * x + 7 * x + 2
    numerator = poly([1, b, c, b, 1])
    source = poly([1, -(x + 1), x + 1, -1])
    coefficients = [value**3 for value in series(source, 21)]
    observed = pmul(denominator, coefficients)
    require(
        observed[:5] == numerator and not any(observed[5 : len(coefficients)]),
        "held-out slice polynomial formula",
    )
    p, q, common = reduced(numerator, denominator)
    return {
        "x": encoded([x])[0],
        "source": encoded(source),
        "denominator": encoded(denominator),
        "numerator": encoded(numerator),
        "reduced_numerator": encoded(p),
        "reduced_denominator": encoded(q),
        "cancelled_factor": encoded(common),
    }


def evaluate(a, x):
    out = Fraction(0)
    for value in reversed(poly(a)):
        out = exact(out * x + value)
    return out


def symbolic_slice_control():
    # Polynomials in T with coefficients in Q[x]; no interpolation in x.
    def multiply(a, b):
        require(len(a) + len(b) <= 20, "bivariate degree cap")
        out = [[Fraction(0)] for _ in range(len(a) + len(b) - 1)]
        for i, left in enumerate(a):
            for j, right in enumerate(b):
                out[i + j] = padd(out[i + j], pmul(left, right))
        return out

    e = [1, 1]
    h = [[Fraction(1)]]
    for r in range(1, 13):
        value = pmul(e, h[r - 1])
        if r >= 2:
            value = padd(value, pscale(pmul(e, h[r - 2]), -1))
        if r >= 3:
            value = padd(value, h[r - 3])
        h.append(value)
    coefficients = [ppow(value, 3) for value in h]
    denominator = [[1], [-1]]
    for cj in ([0, 1], [-2, 0, 1], [0, -3, 0, 1]):
        denominator = multiply(denominator, [[1], pscale(cj, -1), [1]])
    b, c = poly([2, 5, 2]), poly([2, 7, 6, 1])
    predicted = [poly([1]), b, c, b, poly([1])]
    for r in range(13):
        observed = [0]
        for j in range(min(r + 1, len(denominator))):
            observed = padd(observed, pmul(denominator[j], coefficients[r - j]))
        require(
            observed == (predicted[r] if r < 5 else [0]),
            "symbolic slice coefficient identity",
        )
    delta = padd(ppow(b, 2), pscale(padd(c, [-2]), -4))
    require(delta == poly([4, -8, 9, 16, 4]), "symbolic spectrum discriminant")
    minus = padd(padd(c, [2]), pscale(b, -2))
    plus = padd(padd(c, [2]), pscale(b, 2))
    require(minus == pmul(pmul([0, 1], [3, 1]), [-1, 1]), "M(-2) factorization")
    require(plus == pmul(ppow([1, 1], 2), [8, 1]), "M(2) factorization")
    return {
        "coefficient_identities": 13,
        "sampled_x_for_identity": 0,
        "numerator_Qx_coefficients": [encoded(row) for row in predicted],
        "M_minus2": encoded(minus),
        "M_plus2": encoded(plus),
    }


def scalar_controls(native):
    generic = [
        recurrence_panel(values, power)
        for values, power in [
            ((2, 3), 2),
            ((2, 3), 3),
            ((2, 3, 5), 3),
            ((1, 1, 1), 3),
            ((1, -1), 3),
        ]
    ]
    slice_x = [
        Fraction(-8),
        Fraction(-3),
        Fraction(-2),
        Fraction(-5, 3),
        Fraction(-13, 8),
        Fraction(-3, 2),
        Fraction(-1),
        Fraction(-1, 2),
        Fraction(0),
        Fraction(1, 2),
        Fraction(1),
        Fraction(2),
        Fraction(3),
    ]
    slices = [slice_polynomials(x) for x in slice_x]
    counts = Counter()
    for row in native["cubic_character"]:
        counts[sum(sum(block) for block in row["weight"]) % 3] += row["multiplicity"]
    require(
        [counts[i] for i in range(3)] == [568, 576, 576],
        "preregistered cyclic syzygy spectrum",
    )
    monomial_classes = Counter((nu[1] + 2 * nu[2]) % 3 for nu in weak(3, 3))
    require(
        [monomial_classes[i] for i in range(3)] == [4, 3, 3], "cyclic Sym3 spectrum"
    )
    cyclic_d = pmul([1, -1], ppow([1, 0, 0, -1], 3))
    cyclic_n = pmul([1, -1], ppow([1, 0, 0, -1], 2))
    cp, cq, _ = reduced(cyclic_n, cyclic_d)
    require(cp == [1] and cq == [1, 0, 0, -1], "cyclic reduction")
    delta = [4, -8, 9, 16, 4]
    require(evaluate(delta, Fraction(-5, 3)) == Fraction(-71, 81), "left root bracket")
    require(
        evaluate(delta, Fraction(-13, 8)) == Fraction(1, 1024), "right root bracket"
    )
    # Derivative after x=y-2 has positive Bernstein coefficients on [0,1].
    bernstein = [20, 26, 16, 6]
    reconstructed = [0]
    for j, c in enumerate(bernstein):
        term = pmul([0] * j + [1], ppow([1, -1], 3 - j))
        reconstructed = padd(reconstructed, pscale(term, comb(3, j) * c))
    require(reconstructed == poly([20, 18, -48, 16]), "Bernstein derivative identity")
    # Delta=(2x²+4x−1)²+3(1−x²), positive on [-1,0].
    require(
        padd(ppow([-1, 4, 2], 2), [3, 0, -3]) == poly(delta), "second interval identity"
    )
    return {
        "rational_recurrence_panels": generic,
        "self_dual_slice_panels": slices,
        "symbolic_slice": symbolic_slice_control(),
        "cyclic_syzygy_multiplicities": [counts[i] for i in range(3)],
        "cyclic_syzygy_trace": -8,
        "cyclic_universal_numerator": encoded(cyclic_n),
        "cyclic_universal_denominator": encoded(cyclic_d),
        "cyclic_ambient_K": encoded(ppow([1, 0, 0, -1], 8)),
        "purity_discriminant": delta,
        "positive_Bernstein_coefficients": bernstein,
        "root_bracket_values": [
            encoded([Fraction(-71, 81)])[0],
            encoded([Fraction(1, 1024)])[0],
        ],
    }


def build_report():
    sources = source_locks()
    native = native_cubic()
    require(
        (native["quadrics"], native["cubic_syzygies"], native["cubic_dual_algebra"])
        == (162, 1720, 9019),
        "preregistered cubic dimensions",
    )
    scalar = scalar_controls(native)
    artifacts = {
        path.relative_to(ROOT).as_posix(): digest(bounded_bytes(path))
        for path in (NOTE, SCRIPT, MANIFEST, TEST)
    }
    report = {
        "schema": "segre-recurrence-syzygy-controls-v1",
        "claims": [
            "GLO764.SEGRE_RECURRENCE_DICTIONARY_V1",
            "GLO764.SEGRE_CUBIC_SELF_DUAL_SLICE_V1",
            "GLO764.SEGRE_SYZYGY_SUPERDET_BOUNDARY_V1",
        ],
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        },
        "scope": "bounded native algebra; all-parameter theorems are written proofs",
        "coverage": {
            "native_rank_panel": [3, 3, 3],
            "internal_degrees": [2, 3],
            "fitted_matrix_ranks": 0,
            "sampled_primes": 0,
            "complete_product_torus_characters": True,
        },
        "resources": {
            "max_bytes": MAX_BYTES,
            "max_fraction_bits": MAX_BITS,
            "max_JSON_depth": MAX_JSON_DEPTH,
            "max_cubic_words": MAX_WORDS,
            "max_block_rows": MAX_BLOCK_ROWS,
            "max_block_columns": MAX_BLOCK_COLS,
            "semantics": "preallocation structural and per-operation bit caps",
        },
        "sources": sources,
        "artifact_sha256_lf": artifacts,
        "native_cubic_maps": native,
        "scalar_controls": scalar,
        "verdict": "EXACT_LOCAL_ALGEBRA_NO_FINITE_NATURAL_SYZYGY_SUPERDET",
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report)).hexdigest()
    require(len(render(report).encode()) <= MAX_BYTES, "report byte cap")
    return report


def check_fixture():
    actual = strict_json(bounded_bytes(FIXTURE))
    expected = build_report()
    same_json(actual, expected)
    return {
        "status": "PASS",
        "payload_sha256": expected["payload_sha256"],
        "native_cubic_syzygies": 1720,
        "analytic_completion_constructed": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    print(render(check_fixture() if args.check else build_report()), end="")


if __name__ == "__main__":
    main()
