"""Hostile exact replay of literal Segre/Chow maps, independent modular ranks."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/l-families/atlas/generalized/segre_chow_chain_comparison.py"
)
SPEC = importlib.util.spec_from_file_location("chain_comparison", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def mod_rank(columns, rows, prime=1009):
    """Independent dense finite-field lower certificate for the rational rank."""
    a = [[0] * len(columns) for _ in range(rows)]
    for j, col in enumerate(columns):
        for i, value in col:
            value = Fraction(value)
            a[i][j] = value.numerator * pow(value.denominator, -1, prime) % prime
    rank = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(rank, rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inverse = pow(a[rank][col], -1, prime)
        a[rank] = [x * inverse % prime for x in a[rank]]
        for i in range(rank + 1, rows):
            if a[i][col]:
                scalar = a[i][col]
                a[i] = [(x - scalar * y) % prime for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def poly_product(a, b):
    out = Counter()
    for u, x in a.items():
        for v, y in b.items():
            out[tuple(i + j for i, j in zip(u, v))] += x * y
    return Counter({weight: value for weight, value in out.items() if value})


def poly_power(a, exponent):
    out = Counter({(0, 0, 0): 1})
    for _ in range(exponent):
        out = poly_product(out, a)
    return out


def poly_scale(a, scalar):
    out = {}
    for weight, value in a.items():
        value = Fraction(value) * scalar
        if value:
            if value.denominator != 1:
                raise ValueError("nonintegral independent character")
            out[weight] = int(value)
    return out


def perm_power(perm, exponent):
    out = tuple(range(len(perm)))
    for _ in range(exponent):
        out = tuple(perm[out[i]] for i in range(len(perm)))
    return out


def trace_e(m, perm, eigen_power=1):
    out = Counter()
    for word in product(range(3), repeat=m):
        if tuple(word[perm[i]] for i in range(m)) == word:
            out[tuple(eigen_power * word.count(i) for i in range(3))] += 1
    return out


def trace_r(m, degree, perm):
    monos = list(combinations_with_replacement(range(3), degree))
    out = Counter()
    for row in product(monos, repeat=m):
        if tuple(row[perm[i]] for i in range(m)) == row:
            out[tuple(sum(part.count(i) for part in row) for i in range(3))] += 1
    return out


def independent_ambient_characters(m):
    classes = [tuple(range(m)), (1, 0, *range(2, m))]
    if m == 3:
        classes += [(1, 2, 0)]
    else:
        classes += [(1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0)]
    answer = {}
    for c, perm in enumerate(classes):
        e1 = trace_e(m, perm)
        e2 = trace_e(m, perm_power(perm, 2), 2)
        sym2 = poly_scale(Counter(poly_product(e1, e1)) + Counter(e2), Fraction(1, 2))
        ideal2 = Counter(sym2)
        ideal2.subtract(trace_r(m, 2, perm))
        answer[1, 2, c] = {w: x for w, x in ideal2.items() if x}
        if m == 3:
            e3 = trace_e(m, perm_power(perm, 3), 3)
            numerator = Counter(poly_power(e1, 3))
            for w, x in poly_product(e1, e2).items():
                numerator[w] += 3 * x
            for w, x in e3.items():
                numerator[w] += 2 * x
            sym3 = Counter(poly_scale(numerator, Fraction(1, 6)))
            tor2 = poly_product(e1, ideal2)
            tor2.subtract(sym3)
            tor2.update(trace_r(m, 3, perm))
            answer[2, 3, c] = {w: x for w, x in tor2.items() if x}
    return answer


class AlgebraTests(unittest.TestCase):
    def test_integer_bool_rejected(self):
        with self.assertRaises(ValueError):
            M.integer(True, 0, 4)

    def test_rational_float_rejected(self):
        with self.assertRaises(ValueError):
            M.rat(0.5)

    def test_zero_bool_vector_rejected(self):
        with self.assertRaises(ValueError):
            M.Span(1).reduce({0: False})

    def test_rational_bit_cap(self):
        with self.assertRaises(ValueError):
            M.rat(1 << 4096)

    def test_source_caps(self):
        for args in [(3, 5, 2), (3, 4, 3), (3, 3, 5), (True, 3, 2)]:
            with self.assertRaises(ValueError):
                M.Source(*args)

    def test_span_row_cap(self):
        with self.assertRaises(ValueError):
            M.Span(1153)

    def test_kernel_column_cap(self):
        with self.assertRaises(ValueError):
            M.kernel([{}] * 2049, 1)

    def test_fraction_rank_kernel(self):
        cols = [{0: Fraction(1, 2), 1: 1}, {0: 1, 1: 2}, {1: Fraction(2, 3)}]
        ker, rank = M.kernel(cols, 2)
        self.assertEqual((rank, len(ker)), (2, 1))
        self.assertEqual(M.apply_columns(cols, ker[0]), {})
        self.assertEqual(mod_rank([M.sparse(c) for c in cols], 2), rank)

    def test_boundary_lift(self):
        h = M.Homology([0, 1, 2], [{}, {}, {}], 0, [{0: 2, 1: 3}, {1: 1, 2: 1}])
        v = {0: Fraction(4), 1: Fraction(5), 2: Fraction(-1)}
        lift = h.boundary_lift(v)
        self.assertEqual(M.apply_columns([{0: 2, 1: 3}, {1: 1, 2: 1}], lift), v)
        with self.assertRaises(ValueError):
            h.boundary_lift({2: 1})

    def test_invalid_chain_composition(self):
        with self.assertRaises(ValueError):
            M.Homology([0], [{0: 1}], 1, [{0: 1}])

    def test_w_c_direct_sum(self):
        for power in (3, 4):
            source = M.Source(3, power, 0)
            words = {w: i for i, w in enumerate(source.words)}
            cols = [
                {words[w]: x for w, x in t.items()}
                for t in source.w_terms + source.c_terms
            ]
            ker, rank = M.kernel(cols, len(words))
            self.assertEqual(rank, 3**power)
            self.assertEqual(ker, [])
            self.assertTrue(all(sum(t.values()) == 0 for t in source.c_terms))

    def test_factor_permutation_preserves_complement(self):
        source = M.Source(3, 3, 0)
        for c, terms in enumerate(source.c_terms):
            expected = {tuple(w[i] for i in (1, 2, 0)): x for w, x in terms.items()}
            reconstructed = {}
            for j, scalar in source.c_permutation(c, (1, 2, 0)).items():
                for w, x in source.c_terms[j].items():
                    reconstructed[w] = reconstructed.get(w, 0) + scalar * x
            self.assertEqual({w: x for w, x in reconstructed.items() if x}, expected)

    def test_json_duplicate(self):
        with self.assertRaises(ValueError):
            M.strict_load(b'{"a":1,"a":2}')

    def test_json_inexact(self):
        for raw in (b"0.1", b"NaN", b"Infinity"):
            with self.assertRaises(ValueError):
                M.strict_load(raw)

    def test_json_depth_bytes(self):
        with self.assertRaises(ValueError):
            M.strict_load(b"[" * 50 + b"0" + b"]" * 50)
        with self.assertRaises(ValueError):
            M.strict_load(b" " * (M.MAX_BYTES + 1))

    def test_source_manifest_type_substitution(self):
        manifest = M.expected_manifest()
        manifest["parents"][0]["current_copy_required"] = 0
        with self.assertRaises(ValueError):
            M.authenticate_sources(manifest)

    def test_source_manifest_rebinding(self):
        manifest = M.expected_manifest()
        manifest["parents"][0]["sha256_lf"] = "0" * 64
        with self.assertRaises(ValueError):
            M.authenticate_sources(manifest)


class FullReplayTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fresh = M.build_report()
        cls.fixture = M.strict_load(M.lf_bytes(M.FIXTURE))

    def test_complete_fresh_replay(self):
        self.assertTrue(M.validate_report(self.fixture, self.fresh))

    def test_arithmetic_contract(self):
        self.assertEqual(self.fresh["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.fresh["arithmetic_components"],
            ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        )
        self.assertEqual(self.fresh["rounding"], "none")

    def test_all_source_bindings(self):
        self.assertEqual(len(M.authenticate_sources()["parents"]), 10)

    def test_complete_ambient_characters(self):
        p = self.fresh["payload"]
        self.assertGreater(M.check_ambient(p["main"], p["ambient3"]), 40)
        self.assertGreater(M.check_ambient(p["heldout"], p["ambient4"]), 20)

    def test_independent_cycle_formula_all_weights(self):
        for key in ("ambient3", "ambient4"):
            report = self.fresh["payload"][key]
            expected = independent_ambient_characters(report["m"])
            actual = {}
            for q, j, weight, dim, traces in report["W_homology"]:
                if (q, j) in {(1, 2), (2, 3)}:
                    for c, value in enumerate(traces):
                        if value:
                            actual[q, j, c, tuple(weight)] = value
            flat = {
                (q, j, c, w): value
                for (q, j, c), row in expected.items()
                for w, value in row.items()
            }
            self.assertEqual(actual, flat)

    def test_chow_degree_four_character(self):
        self.assertGreater(M.check_chow_characters(self.fresh["payload"]["main"]), 47)

    def test_main_preregistered_ranks(self):
        rows = self.fresh["payload"]["main"]["horizontal_ranks"]
        ranks = {tuple(x[:3]): x[3] for x in rows}
        self.assertEqual(ranks[1, 1, 3], 65)
        self.assertEqual(ranks[2, 0, 3], 187)
        self.assertEqual(ranks[2, 1, 4], 1105)

    def test_heldout_class_traces(self):
        rows = self.fresh["payload"]["heldout"]["E2_homology"]
        traces = [sum(row[-1][i] for row in rows if row[2] == 2) for i in range(5)]
        self.assertEqual(traces, [2025, 189, 45, 9, 3])

    def test_actual_transgression_rank(self):
        matrices = self.fresh["payload"]["transgression_matrices"]
        self.assertEqual(sum(row[3] for row in matrices), 65)
        for weight, cols, rows, rank, matrix in matrices:
            self.assertEqual(len(matrix), cols)
            self.assertEqual(mod_rank(matrix, rows), rank)

    def test_stored_horizontal_modular_ranks(self):
        for p, q, j, w, cols, rank, matrix in self.fresh["payload"]["literal_maps"][
            "horizontal_matrices"
        ]:
            rows = 1 + max((i for col in matrix for i, x in col), default=-1)
            self.assertEqual(mod_rank(matrix, rows), rank)

    def test_nonzero_zigzag_is_stored(self):
        z = self.fresh["payload"]["nonzero_zigzag"]
        self.assertTrue(z["target_homology"])
        self.assertTrue(z["boundary_lifts"])
        self.assertEqual(sum(z["weight"]), 12)

    def reject_resealed(self, mutate):
        bad = copy.deepcopy(self.fixture)
        mutate(bad)
        bad["payload_sha256"] = M.digest(bad["payload"])
        with self.assertRaises(ValueError):
            M.validate_report(bad, self.fresh)

    def test_resealed_zero_transgression(self):
        self.reject_resealed(lambda x: x["payload"]["transgression_matrices"].clear())

    def test_resealed_character_corruption(self):
        self.reject_resealed(
            lambda x: x["payload"]["main"]["W_homology"][0][-1].__setitem__(0, 2)
        )

    def test_resealed_missing_weight(self):
        self.reject_resealed(lambda x: x["payload"]["heldout"]["E2_homology"].pop())

    def test_resealed_boolean_rank(self):
        self.reject_resealed(
            lambda x: x["payload"]["main"]["E2_totals"][0].__setitem__(-1, True)
        )

    def test_resealed_map_corruption(self):
        self.reject_resealed(lambda x: x["payload"]["literal_maps"]["C_on_B12"].pop())

    def test_cap_taxonomy_scope_tamper(self):
        for key, value in [
            ("arithmetic_class", "EXACT"),
            ("rounding", "nearest"),
            ("scope", "general degeneration theorem"),
        ]:
            bad = copy.deepcopy(self.fixture)
            bad[key] = value
            with self.assertRaises(ValueError):
                M.validate_report(bad, self.fresh)

    def test_artifact_reseal_rejected(self):
        bad = copy.deepcopy(self.fixture)
        bad["artifacts_sha256_lf"][str(PATH.relative_to(M.ROOT)).replace("\\", "/")] = (
            "0" * 64
        )
        with self.assertRaises(ValueError):
            M.validate_report(bad, self.fresh)

    def test_extra_field_rejected(self):
        bad = copy.deepcopy(self.fixture)
        bad["unpaid_claim"] = True
        with self.assertRaises(ValueError):
            M.validate_report(bad, self.fresh)


if __name__ == "__main__":
    unittest.main()
