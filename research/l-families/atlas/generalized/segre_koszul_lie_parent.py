"""Bounded native Segre bar/Lie controls for a classical Koszul realization."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement, product
from math import comb, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT = Path(__file__).resolve()
NOTE = HERE / "SEGRE_KOSZUL_LIE_PARENT.md"
MANIFEST = HERE / "segre_koszul_lie_parent.sources.json"
FIXTURE = HERE / "segre_koszul_lie_parent.json"
TEST = ROOT / "tests/test_segre_koszul_lie_parent.py"
MAX_FACTORS = 3
MAX_RANK = 3
MAX_DEGREE = 4
MAX_TOTAL_BASIS = 12000
MAX_LIE_GENERATORS = 9
MAX_BYTES = 262144
BAR_PANELS = ((2,), (2, 2), (2, 3), (2, 2, 2))
LIE_PANELS = ((2,), (2, 2), (2, 3), (3, 3), (2, 2, 2))
EXPECTED_MANIFEST = {
    "schema": "segre-koszul-lie-sources-v1",
    "parents": [
        {
            "commit": "4597d652b8be56f14339c7689f932289b7fe3ab2",
            "path": "research/l-families/atlas/generalized/FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION.md",
            "git_blob": "3932273279d43ffa34d929247152cb43b932fa1d",
            "sha256_lf": "50daa223c5b6d0f061d771f24775a0a7a2d470f9185a1d6304f3b49e9fc799bc",
            "role": "formal-virtual-grade-uniqueness-and-exact-finite-parent-exceptions",
        },
        {
            "commit": "4597d652b8be56f14339c7689f932289b7fe3ab2",
            "path": "research/l-families/atlas/generalized/GRADED_PARENT_GLOBAL_BOUNDARY.md",
            "git_blob": "1a49f7075b590e16c8367c7b2ef8b8d5b77c9819",
            "sha256_lf": "c545339d97aead843ed6591a8a2b8dadc27e0518607fa03b4d7d68b088ec1eef",
            "role": "unchanged-global-natural-boundary-and-completion-firewall",
        },
    ],
    "prior_art": [
        {
            "id": "GORBOUNOV_SCHECHTMAN_2009",
            "title": "Homological Algebra and Divergent Series",
            "url": "https://sigma-journal.com/2009/034/sigma09-034.pdf",
            "locator": "sections 3.4.1--3.4.5; equation (3.13), printed pp.26--29",
            "role": "classical-odd-Lie-dual-Chevalley-resolution-alternating-Euler-and-character-mechanism",
        },
        {
            "id": "CEDERWALL_ET_AL_2024",
            "title": "Canonical Supermultiplets and Their Koszul Duals",
            "url": "https://link.springer.com/article/10.1007/s00220-024-04990-z",
            "locator": "sections 3.2.1--3.2.3; equations (42)--(45)",
            "role": "classical-commutative-quadratic-Lie-duality-and-highest-weight-orbit-context",
        },
        {
            "id": "MORALES_2013",
            "title": "Segre embeddings, Hilbert series and Newcomb's problem",
            "url": "https://arxiv.org/pdf/1306.6910",
            "locator": "Lemma 3 and Theorem 4, section 3.1, printed pp.8--9",
            "role": "classical-coordinatewise-sorting-Groebner-basis; native-proof-also-in-note",
        },
        {
            "id": "PRIDDY_1970",
            "title": "Koszul resolutions",
            "url": "https://math.mit.edu/~hrm/palestine/priddy-koszul-resolutions.pdf",
            "locator": "Theorem 5.3, printed p.51; Koszul complex in section 3",
            "role": "imported-quadratic-PBW-implies-Koszul-theorem",
        },
        {
            "id": "GORODENTSEV_KHOROSHKIN_RUDAKOV",
            "title": "On syzygies of highest weight orbits",
            "url": "https://arxiv.org/pdf/math/0602316",
            "locator": "sections 3.1--3.6, especially Theorem 3.6.1",
            "role": "prior-art-only-general-Lie-cohomology-syzygy-relationship",
        },
    ],
    "external_authentication": "URLs and locators declared; no external theorem or infinite conclusion machine-proved",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, name: str, low: int, high: int) -> int:
    require(type(value) is int and low <= value <= high, f"invalid {name}")
    return value


def ranks_input(value: object) -> tuple[int, ...]:
    require(type(value) in (tuple, list), "ranks must be a tuple/list")
    require(1 <= len(value) <= MAX_FACTORS, "factor count cap")
    return tuple(integer(n, "factor rank", 1, MAX_RANK) for n in value)


def canonical(value: object) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False
    ).encode("utf-8")


def render(value: object) -> str:
    return json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")).hexdigest()


def same_json(actual: object, expected: object) -> None:
    require(canonical(actual) == canonical(expected), "typed canonical replay differs")


def bounded_bytes(path: Path) -> bytes:
    require(path.stat().st_size <= MAX_BYTES, "file byte cap")
    raw = path.read_bytes()
    require(len(raw) <= MAX_BYTES, "file byte cap")
    return raw


def _pairs_no_duplicates(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def _reject_constant(value: str) -> None:
    raise ValueError(f"nonfinite JSON constant: {value}")


def strict_json(raw: bytes) -> object:
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap/type")
    return json.loads(
        raw, object_pairs_hook=_pairs_no_duplicates, parse_constant=_reject_constant
    )


def source_locks() -> dict:
    manifest = strict_json(bounded_bytes(MANIFEST))
    same_json(manifest, EXPECTED_MANIFEST)
    for row in EXPECTED_MANIFEST["parents"]:
        target = row["commit"] + ":" + row["path"]
        try:
            blob = subprocess.check_output(
                ["git", "rev-parse", "--verify", target], cwd=ROOT, text=True
            ).strip()
            raw = subprocess.check_output(["git", "show", target], cwd=ROOT)
        except subprocess.CalledProcessError as error:
            raise ValueError("frozen parent unavailable") from error
        require(blob == row["git_blob"], "frozen parent blob mismatch")
        require(len(raw) <= MAX_BYTES, "frozen parent byte cap")
        require(digest(raw) == row["sha256_lf"], "frozen parent digest mismatch")
        require(
            digest(bounded_bytes(ROOT / row["path"])) == row["sha256_lf"],
            "current parent bytes mismatch",
        )
    return manifest


def _compositions(degree: int, length: int) -> tuple:
    if length == 1:
        return ((degree,),) if degree >= 1 else ()
    return tuple(
        (a,) + tail
        for a in range(1, degree)
        for tail in _compositions(degree - a, length - 1)
    )


def _ring_dimension(ranks: tuple, degree: int) -> int:
    return prod(comb(n + degree - 1, degree) for n in ranks)


def bar_preflight(ranks: object, degree: object, cap: object = MAX_TOTAL_BASIS) -> dict:
    sizes = ranks_input(ranks)
    level = integer(degree, "internal degree", 1, MAX_DEGREE)
    limit = integer(cap, "basis cap", 1, MAX_TOTAL_BASIS)
    dimensions = [
        sum(
            prod(_ring_dimension(sizes, part) for part in composition)
            for composition in _compositions(level, length)
        )
        for length in range(1, level + 1)
    ]
    total = sum(dimensions)
    require(total < limit, "total bar basis must be strictly below cap")
    return {"chain_dimensions": dimensions, "total_basis_slots": total}


def lie_preflight(ranks: object) -> dict:
    sizes = ranks_input(ranks)
    generators = prod(sizes)
    require(generators <= MAX_LIE_GENERATORS, "Lie generator cap")
    return {
        "generators": generators,
        "tensor_degree3": generators**3,
        "quadratic_dual_relations": _ring_dimension(sizes, 2),
    }


def _weak(rank: int, degree: int) -> tuple:
    if rank == 1:
        return ((degree,),)
    return tuple(
        (a,) + tail for a in range(degree + 1) for tail in _weak(rank - 1, degree - a)
    )


def _ring_basis(ranks: tuple, degree: int) -> tuple:
    return tuple(
        tuple(value for block in blocks for value in block)
        for blocks in product(*(_weak(n, degree) for n in ranks))
    )


def _add(a: tuple, b: tuple) -> tuple:
    return tuple(x + y for x, y in zip(a, b))


def _total(word: tuple) -> tuple:
    return tuple(map(sum, zip(*word)))


def _sparse_rank(columns: list[dict]) -> int:
    """Internal exact Gaussian rank, used only after public allocation caps."""
    pivots = {}
    for raw in columns:
        column = {a: Fraction(b) for a, b in raw.items() if b}
        while column:
            pivot = min(column)
            if pivot not in pivots:
                unit = column[pivot]
                pivots[pivot] = {a: b / unit for a, b in column.items()}
                break
            multiple = column[pivot]
            for a, b in pivots[pivot].items():
                value = column.get(a, Fraction(0)) - multiple * b
                if value:
                    column[a] = value
                else:
                    column.pop(a, None)
    return len(pivots)


def bar_control(ranks: object, degree: object, cap: object = MAX_TOTAL_BASIS) -> dict:
    plan = bar_preflight(ranks, degree, cap)
    sizes = ranks_input(ranks)
    rb = {j: _ring_basis(sizes, j) for j in range(1, degree + 1)}
    spaces = {}
    for length in range(1, degree + 1):
        group = defaultdict(list)
        for parts in _compositions(degree, length):
            for word in product(*(rb[p] for p in parts)):
                group[_total(word)].append(word)
        spaces[length] = group
    diffs = {}
    rank = {1: 0, degree + 1: 0}
    for length in range(2, degree + 1):
        diff = {}
        for weight, words in spaces[length].items():
            index = {word: i for i, word in enumerate(spaces[length - 1][weight])}
            columns = []
            for word in words:
                column = {}
                for i in range(length - 1):
                    target = word[:i] + (_add(word[i], word[i + 1]),) + word[i + 2 :]
                    key = index[target]
                    column[key] = column.get(key, 0) + (-1) ** i
                columns.append({a: b for a, b in column.items() if b})
            diff[weight] = columns
        diffs[length] = diff
        rank[length] = sum(_sparse_rank(columns) for columns in diff.values())
    square_columns = 0
    for length in range(3, degree + 1):
        for weight, columns in diffs[length].items():
            previous = diffs[length - 1][weight]
            for column in columns:
                result = defaultdict(int)
                for j, value in column.items():
                    for i, entry in previous[j].items():
                        result[i] += entry * value
                require(not any(result.values()), "bar differential square")
                square_columns += 1
    dimensions = [sum(map(len, spaces[i].values())) for i in range(1, degree + 1)]
    require(dimensions == plan["chain_dimensions"], "bar basis coverage")
    homology = [dimensions[i - 1] - rank[i] - rank[i + 1] for i in range(1, degree + 1)]
    require(all(h == 0 for h in homology[:-1]), "off-diagonal Tor is nonzero")
    require(homology[-1] >= 0, "negative diagonal homology")
    return {
        "ranks": list(sizes),
        "internal_degree": degree,
        "chain_dimensions": dimensions,
        "differential_ranks_d1_through_dj": [rank[i] for i in range(1, degree + 1)],
        "homology_H1_through_Hj": homology,
        "square_zero_columns": square_columns,
        "allocation": plan,
    }


def lie3_control(ranks: object) -> dict:
    plan = lie_preflight(ranks)
    sizes = ranks_input(ranks)
    axes = list(product(*(range(n) for n in sizes)))
    size = len(axes)

    def weight(word: tuple) -> tuple:
        return tuple(tuple(sorted(axes[a][i] for a in word)) for i in range(len(sizes)))

    pairgroups = defaultdict(list)
    for a, b in product(range(size), repeat=2):
        pairgroups[weight((a, b))].append((a, b))
    require(
        len(pairgroups) == plan["quadratic_dual_relations"], "dual relation coverage"
    )
    triples = defaultdict(list)
    for word in product(range(size), repeat=3):
        triples[weight(word)].append(word)
    group_rel = defaultdict(list)
    for pairs in pairgroups.values():
        for c in range(size):
            left = {(a, b, c): 1 for a, b in pairs}
            right = {(c, a, b): 1 for a, b in pairs}
            group_rel[weight(next(iter(left)))].append(left)
            group_rel[weight(next(iter(right)))].append(right)
    quotient_dim = lie_dim = ideal_rank = 0
    positive_dual_weights = []
    for torus_weight, words in sorted(triples.items()):
        index = {word: i for i, word in enumerate(words)}
        relations = [
            {index[word]: value for word, value in col.items()}
            for col in group_rel[torus_weight]
        ]
        before = _sparse_rank(relations)
        brackets = []
        for a, b, c in words:
            terms = defaultdict(int)
            for word, sign in (
                ((a, b, c), 1),
                ((a, c, b), 1),
                ((b, c, a), -1),
                ((c, b, a), -1),
            ):
                terms[index[word]] += sign
            brackets.append(dict(terms))
        after = _sparse_rank(relations + brackets)
        multiplicity = after - before
        require(multiplicity >= 0, "negative Lie quotient dimension")
        if multiplicity:
            positive_dual_weights.append(
                {
                    "weight": [list(block) for block in torus_weight],
                    "multiplicity": multiplicity,
                }
            )
        ideal_rank += before
        quotient_dim += len(words) - before
        lie_dim += multiplicity
    return {
        "ranks": list(sizes),
        **plan,
        "g2": size * (size + 1) // 2 - len(pairgroups),
        "ideal_degree3_rank": ideal_rank,
        "U_g_degree3": quotient_dim,
        "g3": lie_dim,
        "g3_dual_positive_weights": positive_dual_weights,
    }


def _poly_add(target: dict, source: dict, scalar: int = 1) -> None:
    for monomial, value in source.items():
        total = target.get(monomial, 0) + scalar * value
        if total:
            target[monomial] = total
        else:
            target.pop(monomial, None)


def _variable_times(poly: dict, index: int) -> dict:
    answer = {}
    for monomial, value in poly.items():
        powers = list(monomial)
        powers[index] += 1
        answer[tuple(powers)] = value
    return answer


def linear_syzygy_control() -> dict:
    # Actual 2x3 minors bf-ce, cd-af, ae-bd, with variables a,b,c,d,e,f.
    def term(i: int, j: int) -> tuple:
        powers = [0] * 6
        powers[i] += 1
        powers[j] += 1
        return tuple(powers)

    minors = [
        {term(1, 5): 1, term(2, 4): -1},
        {term(2, 3): 1, term(0, 5): -1},
        {term(0, 4): 1, term(1, 3): -1},
    ]
    monomials = []
    for indices in combinations_with_replacement(range(6), 3):
        powers = [0] * 6
        for index in indices:
            powers[index] += 1
        monomials.append(tuple(powers))
    index = {monomial: i for i, monomial in enumerate(monomials)}
    columns = [
        {index[monomial]: value for monomial, value in _variable_times(q, x).items()}
        for x in range(6)
        for q in minors
    ]
    identities = []
    for offset in (0, 3):
        result = {}
        for i, q in enumerate(minors):
            _poly_add(result, _variable_times(q, i + offset))
        require(not result, "native linear syzygy failed")
        identities.append("zero")
    rank = _sparse_rank(columns)
    require(rank == 16, "unequal-rank linear syzygy rank")
    return {
        "ranks": [2, 3],
        "ambient_degree3": len(monomials),
        "variable_times_minor_columns": len(columns),
        "rank": rank,
        "linear_syzygies": len(columns) - rank,
        "native_identities": identities,
    }


def build_report() -> dict:
    for sizes in BAR_PANELS:
        for degree in range(1, MAX_DEGREE + 1):
            bar_preflight(sizes, degree)
    for sizes in LIE_PANELS:
        lie_preflight(sizes)
    sources = source_locks()
    bar = [
        bar_control(sizes, degree)
        for sizes in BAR_PANELS
        for degree in range(1, MAX_DEGREE + 1)
    ]
    lie = [lie3_control(sizes) for sizes in LIE_PANELS]
    syzygies = linear_syzygy_control()
    unequal = next(row for row in lie if row["ranks"] == [2, 3])
    require(
        unequal["g3_dual_positive_weights"]
        == [
            {"weight": [[0, 0, 1], [0, 1, 2]], "multiplicity": 1},
            {"weight": [[0, 1, 1], [0, 1, 2]], "multiplicity": 1},
        ],
        "held-out unequal-rank cubic character",
    )
    require(unequal["g3"] == syzygies["linear_syzygies"], "independent syzygy bridge")
    for row in bar:
        if row["internal_degree"] == 3:
            dual = next(item for item in lie if item["ranks"] == row["ranks"])
            require(
                row["homology_H1_through_Hj"][-1] == dual["U_g_degree3"],
                "independent bar and dual-relations degree-three comparison",
            )
    artifacts = {
        str(path.relative_to(ROOT)).replace("\\", "/"): digest(bounded_bytes(path))
        for path in (NOTE, SCRIPT, TEST, MANIFEST)
    }
    report = {
        "schema": "segre-koszul-lie-controls-v1",
        "claims": [
            "GLO764.SEGRE_KOSZUL_LIE_REALIZATION_V1",
            "GLO764.SEGRE_STRICT_ALL_GRADE_SIGNS_V1",
        ],
        "scope": "bounded exact algebra; infinite theorem is prose plus declared classical dependencies",
        "arithmetic": {
            "class": "MIXED",
            "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding": "none",
        },
        "coverage": {
            "bar_rank_panels": [list(sizes) for sizes in BAR_PANELS],
            "bar_internal_degrees_inclusive": [1, MAX_DEGREE],
            "bar_complexes": len(bar),
            "lie_rank_panels": [list(sizes) for sizes in LIE_PANELS],
            "lie_tensor_degree": 3,
            "fitted_Hilbert_series_ranks": 0,
            "prime_samples": 0,
        },
        "resources": {
            "max_factors": MAX_FACTORS,
            "max_rank": MAX_RANK,
            "max_internal_degree": MAX_DEGREE,
            "bar_basis_slots_exclusive": MAX_TOTAL_BASIS,
            "lie_generators_inclusive": MAX_LIE_GENERATORS,
            "max_bytes": MAX_BYTES,
            "semantics": "pre-allocation structural caps, not CPU or bit-complexity certificates",
        },
        "sources": sources,
        "artifact_sha256_lf": artifacts,
        "bar_controls": bar,
        "actual_lie_quotients": lie,
        "linear_syzygy_control": syzygies,
        "verdict": "EXACT_BOUNDED_ALGEBRA_PASS_NO_ANALYTIC_COMPLETION",
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report)).hexdigest()
    require(len(render(report).encode()) <= MAX_BYTES, "report byte cap")
    return report


def check_fixture() -> dict:
    actual = strict_json(bounded_bytes(FIXTURE))
    expected = build_report()
    same_json(actual, expected)
    return {
        "status": "PASS",
        "payload_sha256": expected["payload_sha256"],
        "infinite_theorem_machine_proved": False,
        "analytic_completion_constructed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    print(render(check_fixture() if args.check else build_report()), end="")


if __name__ == "__main__":
    main()
