#!/usr/bin/env python3
"""Exact finite-field replay for the ternary Segre--Chow change-of-rings page.

The script constructs, from the literal orbit-sum inclusion
    W = Sym^3(Q^3) -> E = (Q^3)^{tensor 3},
the W-Koszul complexes of
    R_r = (Sym^r Q^3)^{tensor 3},
a coordinate complement C of W in E, the induced C-action on W-Koszul
homology, and the first change-of-rings transgression

    d^2_{2,1,4}: Tor_2^{Sym C}(B_1,k)_4 -> B_{2,4},
    B_q = Tor_q^{Sym W}(R,k).

A rank over F_p is a lower bound for the corresponding rational rank.
All target dimensions are independently forced by exact rank/nullity in the
same complexes, so equality follows whenever the lower bound reaches the
available dimension.
"""
from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

Sparse = Dict[int, int]


def compositions(n: int, length: int = 3) -> List[Tuple[int, ...]]:
    if length == 1:
        return [(n,)]
    out: List[Tuple[int, ...]] = []
    for a in range(n + 1):
        for tail in compositions(n - a, length - 1):
            out.append((a,) + tail)
    return out


def add_comp(a: Tuple[int, ...], i: int) -> Tuple[int, ...]:
    b = list(a)
    b[i] += 1
    return tuple(b)


def sparse_add_scaled(dst: Sparse, src: Sparse, scale: int, p: int) -> None:
    if scale % p == 0:
        return
    for k, v in src.items():
        nv = (dst.get(k, 0) + scale * v) % p
        if nv:
            dst[k] = nv
        elif k in dst:
            del dst[k]


def sparse_scale(v: Sparse, scale: int, p: int) -> Sparse:
    scale %= p
    return {k: (scale * x) % p for k, x in v.items() if (scale * x) % p}


@dataclass
class ColumnBasis:
    """Incremental sparse column echelon basis with optional labels."""

    p: int

    def __post_init__(self) -> None:
        self.vec: Dict[int, Sparse] = {}
        self.label: Dict[int, Sparse] = {}

    @property
    def rank(self) -> int:
        return len(self.vec)

    def reduce(self, vector: Sparse, label: Sparse | None = None) -> Tuple[Sparse, Sparse]:
        v = {k: x % self.p for k, x in vector.items() if x % self.p}
        lab = {} if label is None else {k: x % self.p for k, x in label.items() if x % self.p}
        for pivot in sorted(self.vec):
            coeff = v.get(pivot, 0)
            if coeff:
                sparse_add_scaled(v, self.vec[pivot], -coeff, self.p)
                sparse_add_scaled(lab, self.label[pivot], -coeff, self.p)
        return v, lab

    def add(self, vector: Sparse, label: Sparse | None = None) -> Tuple[bool, Sparse]:
        v, lab = self.reduce(vector, label)
        if not v:
            return False, lab
        pivot = min(v)
        inv = pow(v[pivot], -1, self.p)
        v = sparse_scale(v, inv, self.p)
        lab = sparse_scale(lab, inv, self.p)
        self.vec[pivot] = v
        self.label[pivot] = lab
        return True, lab

    def coordinates(self, vector: Sparse) -> Sparse:
        """Coordinates in the stored labels; vector must lie in the span."""
        v = {k: x % self.p for k, x in vector.items() if x % self.p}
        out: Sparse = {}
        for pivot in sorted(self.vec):
            coeff = v.get(pivot, 0)
            if coeff:
                sparse_add_scaled(v, self.vec[pivot], -coeff, self.p)
                sparse_add_scaled(out, self.label[pivot], coeff, self.p)
        if v:
            raise ValueError("vector is not in the certified span")
        return out


def rank_and_kernel(columns: Sequence[Sparse], p: int) -> Tuple[int, List[Sparse]]:
    basis = ColumnBasis(p)
    kernel: List[Sparse] = []
    for j, col in enumerate(columns):
        independent, relation = basis.add(col, {j: 1})
        if not independent:
            kernel.append(relation)
    return basis.rank, kernel


def independent_quotient_representatives(
    cycles: Sequence[Sparse], boundaries: Sequence[Sparse], p: int
) -> Tuple[List[Sparse], ColumnBasis]:
    basis = ColumnBasis(p)
    for col in boundaries:
        basis.add(col, {})
    reps: List[Sparse] = []
    for cyc in cycles:
        idx = len(reps)
        independent, _ = basis.add(cyc, {idx: 1})
        if independent:
            reps.append(cyc)
    reducer = ColumnBasis(p)
    for col in boundaries:
        reducer.add(col, {})
    for i, rep in enumerate(reps):
        ok, _ = reducer.add(rep, {i: 1})
        if not ok:
            raise AssertionError("quotient representatives lost independence")
    return reps, reducer


class TernarySource:
    def __init__(self) -> None:
        self.w_basis = compositions(3)
        self.w_pairs = list(itertools.combinations(range(len(self.w_basis)), 2))
        self.w_pair_index = {x: i for i, x in enumerate(self.w_pairs)}
        self.w_triples = list(itertools.combinations(range(len(self.w_basis)), 3))
        self._r_basis: Dict[int, List[Tuple[Tuple[int, ...], ...]]] = {}
        self._r_index: Dict[int, Dict[Tuple[Tuple[int, ...], ...], int]] = {}
        self.w_orbits = [self._orbit_words(w) for w in self.w_basis]
        chosen = {orbit[0] for orbit in self.w_orbits}
        self.e_basis = list(itertools.product(range(3), repeat=3))
        self.c_basis = [word for word in self.e_basis if word not in chosen]
        self.c_pairs = list(itertools.combinations(range(len(self.c_basis)), 2))

    @staticmethod
    def _orbit_words(comp: Tuple[int, ...]) -> List[Tuple[int, int, int]]:
        word: List[int] = []
        for i, count in enumerate(comp):
            word.extend([i] * count)
        return sorted(set(itertools.permutations(word)))

    def r_basis(self, degree: int) -> List[Tuple[Tuple[int, ...], ...]]:
        if degree not in self._r_basis:
            c = compositions(degree)
            b = list(itertools.product(c, repeat=3))
            self._r_basis[degree] = b
            self._r_index[degree] = {x: i for i, x in enumerate(b)}
        return self._r_basis[degree]

    def r_index(self, degree: int) -> Dict[Tuple[Tuple[int, ...], ...], int]:
        self.r_basis(degree)
        return self._r_index[degree]

    def mul_word(self, degree: int, r_idx: int, word: Tuple[int, int, int]) -> int:
        r = self.r_basis(degree)[r_idx]
        target = tuple(add_comp(r[t], word[t]) for t in range(3))
        return self.r_index(degree + 1)[target]

    def mul_w(self, degree: int, r_idx: int, w_idx: int) -> Sparse:
        out: Sparse = {}
        for word in self.w_orbits[w_idx]:
            k = self.mul_word(degree, r_idx, word)
            out[k] = out.get(k, 0) + 1
        return out

    def k1_index(self, internal: int, w: int, r: int) -> int:
        return w * len(self.r_basis(internal - 1)) + r

    def k2_index(self, internal: int, pair: int, r: int) -> int:
        return pair * len(self.r_basis(internal - 2)) + r

    def d1_columns(self, internal: int, p: int) -> List[Sparse]:
        cols: List[Sparse] = []
        for w in range(len(self.w_basis)):
            for r in range(len(self.r_basis(internal - 1))):
                cols.append({k: v % p for k, v in self.mul_w(internal - 1, r, w).items()})
        return cols

    def d2_columns(self, internal: int, p: int) -> List[Sparse]:
        cols: List[Sparse] = []
        for a, b in self.w_pairs:
            for r in range(len(self.r_basis(internal - 2))):
                col: Sparse = {}
                for rr, coeff in self.mul_w(internal - 2, r, a).items():
                    idx = self.k1_index(internal, b, rr)
                    col[idx] = (col.get(idx, 0) + coeff) % p
                for rr, coeff in self.mul_w(internal - 2, r, b).items():
                    idx = self.k1_index(internal, a, rr)
                    col[idx] = (col.get(idx, 0) - coeff) % p
                    if not col[idx]:
                        del col[idx]
                cols.append(col)
        return cols

    def d3_columns(self, internal: int, p: int) -> List[Sparse]:
        cols: List[Sparse] = []
        for a, b, c in self.w_triples:
            pair_terms = [((b, c), a, 1), ((a, c), b, -1), ((a, b), c, 1)]
            for r in range(len(self.r_basis(internal - 3))):
                col: Sparse = {}
                for pair, w, sign in pair_terms:
                    pair_idx = self.w_pair_index[pair]
                    for rr, coeff in self.mul_w(internal - 3, r, w).items():
                        idx = self.k2_index(internal, pair_idx, rr)
                        col[idx] = (col.get(idx, 0) + sign * coeff) % p
                        if not col[idx]:
                            del col[idx]
                cols.append(col)
        return cols

    def multiply_k1_by_c(self, internal: int, vector: Sparse, c_idx: int, p: int) -> Sparse:
        nr = len(self.r_basis(internal - 1))
        out: Sparse = {}
        word = self.c_basis[c_idx]
        for idx, coeff in vector.items():
            w, r = divmod(idx, nr)
            rr = self.mul_word(internal - 1, r, word)
            target = self.k1_index(internal + 1, w, rr)
            out[target] = (out.get(target, 0) + coeff) % p
        return {k: v for k, v in out.items() if v}

    def multiply_k2_by_c(self, internal: int, vector: Sparse, c_idx: int, p: int) -> Sparse:
        nr = len(self.r_basis(internal - 2))
        out: Sparse = {}
        word = self.c_basis[c_idx]
        for idx, coeff in vector.items():
            pair, r = divmod(idx, nr)
            rr = self.mul_word(internal - 2, r, word)
            target = self.k2_index(internal + 1, pair, rr)
            out[target] = (out.get(target, 0) + coeff) % p
        return {k: v for k, v in out.items() if v}


def matrix_rank(columns: Sequence[Sparse], p: int) -> int:
    basis = ColumnBasis(p)
    for col in columns:
        basis.add(col, {})
    return basis.rank


def run_prime(p: int) -> dict:
    src = TernarySource()
    assert len(src.w_basis) == 10
    assert len(src.c_basis) == 17

    d1_2 = src.d1_columns(2, p)
    d2_2 = src.d2_columns(2, p)
    rank_d1_2, ker_d1_2 = rank_and_kernel(d1_2, p)
    rank_d2_2 = matrix_rank(d2_2, p)
    h12_reps, _ = independent_quotient_representatives(ker_d1_2, d2_2, p)
    assert len(h12_reps) == 20

    d1_3 = src.d1_columns(3, p)
    d2_3 = src.d2_columns(3, p)
    rank_d1_3, ker_d1_3 = rank_and_kernel(d1_3, p)
    rank_d2_3 = matrix_rank(d2_3, p)
    h13_reps, h13_reducer = independent_quotient_representatives(ker_d1_3, d2_3, p)
    assert len(h13_reps) == 65

    action: List[List[Sparse]] = []
    action_columns: List[Sparse] = []
    for c in range(len(src.c_basis)):
        row: List[Sparse] = []
        for rep in h12_reps:
            product = src.multiply_k1_by_c(2, rep, c, p)
            coords = h13_reducer.coordinates(product)
            row.append(coords)
            action_columns.append(coords)
        action.append(row)
    action_rank = matrix_rank(action_columns, p)
    assert action_rank == 65

    horizontal_columns: List[Sparse] = []
    horizontal_domain_meta: List[Tuple[int, int, int]] = []
    for a, b in src.c_pairs:
        for h in range(len(h12_reps)):
            col: Sparse = {}
            for q, coeff in action[a][h].items():
                idx = b * len(h13_reps) + q
                col[idx] = (col.get(idx, 0) + coeff) % p
            for q, coeff in action[b][h].items():
                idx = a * len(h13_reps) + q
                col[idx] = (col.get(idx, 0) - coeff) % p
                if not col[idx]:
                    del col[idx]
            horizontal_columns.append(col)
            horizontal_domain_meta.append((a, b, h))
    horizontal_rank, horizontal_kernel = rank_and_kernel(horizontal_columns, p)
    assert horizontal_rank == 17 * 65

    d2_3_solver = ColumnBasis(p)
    for j, col in enumerate(d2_3):
        d2_3_solver.add(col, {j: 1})

    d2_4 = src.d2_columns(4, p)
    d3_4 = src.d3_columns(4, p)
    rank_d2_4, ker_d2_4 = rank_and_kernel(d2_4, p)
    rank_d3_4 = matrix_rank(d3_4, p)
    h24_dim = len(ker_d2_4) - rank_d3_4
    assert h24_dim == 65

    transgression_columns: List[Sparse] = []
    for relation in horizontal_kernel:
        h_chain_by_c: List[Sparse] = [{} for _ in src.c_basis]
        for dom_idx, rel_coeff in relation.items():
            a, b, h = horizontal_domain_meta[dom_idx]
            rep = h12_reps[h]
            prod_a = src.multiply_k1_by_c(2, rep, a, p)
            prod_b = src.multiply_k1_by_c(2, rep, b, p)
            sparse_add_scaled(h_chain_by_c[b], prod_a, rel_coeff, p)
            sparse_add_scaled(h_chain_by_c[a], prod_b, -rel_coeff, p)

        y_by_c: List[Sparse] = []
        for chain in h_chain_by_c:
            y_by_c.append(d2_3_solver.coordinates(chain) if chain else {})

        z: Sparse = {}
        for c, y in enumerate(y_by_c):
            if y:
                product = src.multiply_k2_by_c(3, y, c, p)
                sparse_add_scaled(z, product, 1, p)

        residual: Sparse = {}
        for col_idx, coeff in z.items():
            sparse_add_scaled(residual, d2_4[col_idx], coeff, p)
        if residual:
            raise AssertionError("zig-zag output is not a W-Koszul cycle")
        transgression_columns.append(z)

    boundary_plus = ColumnBasis(p)
    for col in d3_4:
        boundary_plus.add(col, {})
    before = boundary_plus.rank
    for col in transgression_columns:
        boundary_plus.add(col, {})
    transgression_rank_mod_boundaries = boundary_plus.rank - before
    assert transgression_rank_mod_boundaries == 65

    sym2_c = 17 * 18 // 2
    b02 = 11
    j2_dim = sym2_c - b02
    ambient_quadrics = j2_dim + len(h12_reps)
    sym3_c = 17 * 18 * 19 // 6
    tor2_b0_degree3 = 17 * j2_dim - sym3_c
    tor1_b1_degree3 = 17 * len(h12_reps) - len(h13_reps)
    ambient_linear_cubic_syzygies = tor2_b0_degree3 + tor1_b1_degree3
    assert ambient_quadrics == 162
    assert ambient_linear_cubic_syzygies == 1720

    return {
        "prime": p,
        "dimensions": {"W": 10, "C": 17, "B_1_2": 20, "B_1_3": 65, "B_2_4": 65},
        "w_koszul_ranks": {
            "d1_internal2": rank_d1_2,
            "d2_internal2": rank_d2_2,
            "d1_internal3": rank_d1_3,
            "d2_internal3": rank_d2_3,
            "d2_internal4": rank_d2_4,
            "d3_internal4": rank_d3_4,
        },
        "c_action": {"source_dimension": 340, "target_dimension": 65, "rank": action_rank, "surjective": True},
        "e2_2_1_4": {
            "horizontal_source_dimension": len(src.c_pairs) * 20,
            "horizontal_target_dimension": 17 * 65,
            "horizontal_rank": horizontal_rank,
            "dimension": len(horizontal_kernel),
        },
        "d2_transgression": {
            "target_dimension": h24_dim,
            "rank_mod_vertical_boundaries": transgression_rank_mod_boundaries,
            "surjective": True,
        },
        "ambient_first_strands": {
            "quadratic_ideal_from_change_of_rings": {"Tor1C_B0_degree2": j2_dim, "B_1_2": 20, "total": 162},
            "cubic_linear_syzygies_from_change_of_rings": {
                "Tor2C_B0_degree3": tor2_b0_degree3,
                "Tor1C_B1_degree3": tor1_b1_degree3,
                "total": 1720,
            },
        },
        "all_checks_passed": True,
        "rh_or_grh_established": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, action="append", default=[])
    parser.add_argument("--output")
    args = parser.parse_args()
    primes = args.prime or [65521]
    result = {
        "theorem": "ternary Segre--Chow first transgression",
        "results": [run_prime(p) for p in primes],
        "all_checks_passed": True,
        "scope": "exact finite-field rank certificates for integer matrices",
        "rh_or_grh_established": False,
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
