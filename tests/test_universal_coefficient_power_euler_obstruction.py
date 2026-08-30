"""Independent bounded controls for the universal Euler obstruction packet."""

from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    REPO_ROOT / "research" / "l-families" / "atlas" / "generalized"
    / "universal_coefficient_power_euler_obstruction.py"
)
spec = importlib.util.spec_from_file_location("universal_euler_obstruction", MODULE_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("cannot load universal Euler obstruction producer")
subject = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subject)


def reject_float(value: object) -> None:
    if isinstance(value, float):
        raise AssertionError("floating-point fixture value")
    if isinstance(value, dict):
        for item in value.values():
            reject_float(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            reject_float(item)


def brute_descents(n: int, k: int) -> list[int]:
    """Small exhaustive word cube, independent of the cached recursion."""
    e = (n - 1) * k
    if k**e >= 100_000:
        raise ValueError("test word cube reaches its exclusive cap")
    result = [0] * (e + 1)
    for word in itertools.product(range(k), repeat=e):
        if any(word.count(letter) != n - 1 for letter in range(k)):
            continue
        descents = sum(left > right for left, right in zip(word, word[1:]))
        result[descents] += 1
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


class UniversalEulerObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_smallest_witness_and_exact_positive_two_jet_gap(self) -> None:
        row = subject.identity_row(2, 2)
        self.assertEqual([subject.identity_coefficient(2, 2, r) for r in range(3)], [1, 4, 9])
        self.assertEqual(row["first_coefficient_forced_virtual_dimension"], 4)
        self.assertEqual(row["exact_identity_pole_order"], 3)
        self.assertEqual(row["second_coefficient_defect"], 1)
        self.assertEqual(row["identity_numerator"], [1, 1])
        for n in range(2, subject.MAX_ALLOWED_N + 1):
            for k in range(2, subject.MAX_ALLOWED_K + 1):
                row = subject.identity_row(n, k)
                dimension = n**k
                target = (n * (n + 1) // 2) ** k
                forced = dimension * (dimension + 1) // 2
                self.assertGreater(forced, target)
                self.assertEqual(row["second_coefficient_defect"], forced - target)
                self.assertEqual(
                    sum(piece["dimension"] for piece in row["omitted_even_flip_summands"]),
                    forced - target,
                )
                self.assertGreater(row["pole_order_gap"], 0)

    def test_exception_chambers_and_polynomial_zero_power(self) -> None:
        for n, k in [(n, k) for n in range(1, 6) for k in (0, 1)] + [(1, k) for k in range(6)]:
            row = subject.identity_row(n, k)
            self.assertFalse(row["no_go_chamber"])
            self.assertEqual(row["identity_numerator"], [1])
            self.assertEqual(row["pole_order_gap"], 0)
            self.assertEqual(row["second_coefficient_defect"], 0)
        minimal = subject.build_fixture(max_n=1, max_k=0)
        self.assertEqual(minimal["identity_controls"]["row_count"], 1)
        self.assertEqual(minimal["constructive_controls"]["row_count"], 0)

    def test_independent_word_cube_and_stable_sort_coefficient_recovery(self) -> None:
        for n, k in ((3, 0), (1, 3), (2, 4), (3, 3), (4, 2), (3, 4)):
            enumerated = brute_descents(n, k)
            finite_difference, _ = subject.finite_difference_numerator(n, k)
            dynamic, _ = subject.multiset_descent_numerator(n, k)
            self.assertEqual(enumerated, finite_difference)
            self.assertEqual(enumerated, dynamic)
            e = (n - 1) * k
            for r in range(6):
                recovered = sum(
                    count * math.comb(r - descents + e, e)
                    for descents, count in enumerate(enumerated) if r >= descents
                )
                self.assertEqual(recovered, subject.identity_coefficient(n, k, r))
        with self.assertRaisesRegex(ValueError, "exclusive cap"):
            brute_descents(5, 5)

    def test_known_and_held_out_eulerian_segre_numerators(self) -> None:
        expected = {
            (2, 3): [1, 4, 1],
            (2, 4): [1, 11, 11, 1],
            (3, 2): [1, 4, 1],
            (3, 3): [1, 20, 48, 20, 1],
            (5, 3): [1, 112, 1828, 8464, 13840, 8464, 1828, 112, 1],
            (3, 5): [1, 232, 5158, 27664, 47290, 27664, 5158, 232, 1],
        }
        self.assertLess(subject.DEFAULT_MAX_N, 5)
        self.assertLess(subject.DEFAULT_MAX_K, 5)
        for (n, k), numerator in expected.items():
            row = subject.identity_row(n, k)
            self.assertEqual(row["identity_numerator"], numerator)
            self.assertEqual(sum(numerator), row["numerator_at_one_multiset_word_count"])
        for n in range(1, subject.MAX_ALLOWED_N + 1):
            numerator, _ = subject.finite_difference_numerator(n, 2)
            self.assertEqual(numerator, [math.comb(n - 1, j) ** 2 for j in range(n)])

    def test_balanced_weights_against_independent_tensor_basis_enumeration(self) -> None:
        for n, m in ((2, 1), (2, 2), (3, 1), (3, 2)):
            coefficients = subject.balanced_weights(n, m)
            enumerated: dict[tuple[int, ...], int] = {}
            for indices in itertools.product(range(n), repeat=2 * m):
                exponent = tuple(
                    indices[:m].count(i) - indices[m:].count(i) for i in range(n)
                )
                enumerated[exponent] = enumerated.get(exponent, 0) + 1
            self.assertEqual(coefficients, enumerated)
            self.assertEqual(sum(coefficients.values()), n ** (2 * m))
        self.assertEqual(subject.balanced_weights(2, 2), {
            (-2, 2): 1, (-1, 1): 4, (0, 0): 6, (1, -1): 4, (2, -2): 1,
        })

    def test_balanced_repair_keeps_rank_multiplicity_and_exact_rationals(self) -> None:
        for n, m, rank, support in ((2, 1, 4, 3), (2, 2, 16, 5), (3, 2, 81, 19), (5, 2, 625, 131)):
            row = subject.balanced_trace_row(n, m)
            self.assertEqual(row["representation_rank_and_euler_denominator_degree"], rank)
            self.assertEqual(row["distinct_character_count_dense_scalar_recurrence_degree"], support)
            self.assertGreater(rank, support)
            self.assertEqual(row["determinant_character_exponent"], [0] * n)
            self.assertTrue(row["sample_is_nonunitary_algebraic_trace_pair_not_absolute_trace"])
            self.assertTrue(row["independent_determinant_coefficients_equal"])
            traces = [Fraction(*value) for value in row["balanced_power_traces"]]
            exponential = [Fraction(*value) for value in row["exponential_coefficients"]]
            self.assertEqual(traces[0], rank)
            self.assertEqual(exponential[0], 1)
            self.assertEqual(exponential[1], traces[1])
            self.assertEqual(exponential[2], (traces[1] ** 2 + traces[2]) / 2)
            self.assertEqual(row["identity_scalar_recurrence_degree"], 1)
            self.assertEqual(row["identity_euler_denominator_degree"], rank)
        self.assertEqual(subject.balanced_trace_row(1, 2)["exponential_coefficients"], [[1, 1]] * 5)

    def test_unitary_exact_sign_controls_and_scalar_twists(self) -> None:
        for diagonal in ((1, -1), (1, 1, -1)):
            n = len(diagonal)
            for m in (1, 2):
                weights = subject.balanced_weights(n, m)
                for r in range(5):
                    trace = sum(z**r for z in diagonal)
                    # Integral unitary roots avoid any floating-point absolute-value test.
                    weight_trace = sum(
                        count * math.prod(
                            Fraction(z) ** (r * v) for z, v in zip(diagonal, exponent)
                        )
                        for exponent, count in weights.items()
                    )
                    self.assertEqual(weight_trace, abs(trace) ** (2 * m))
                for exponent in weights:
                    self.assertEqual(sum(exponent), 0)
                    self.assertEqual(
                        math.prod(Fraction(3 * z) ** v for z, v in zip(diagonal, exponent)),
                        math.prod(Fraction(z) ** v for z, v in zip(diagonal, exponent)),
                    )

    def test_authenticated_sources_and_fail_closed_drift(self) -> None:
        lock = subject.verify_sources_manifest()
        self.assertEqual(lock["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertTrue(lock["git_blob_contents_compared_to_working_tree"])
        self.assertEqual(len(lock["verified_sources"]), 3)
        for row in lock["verified_sources"]:
            content = subject._normalized_bytes(subject._git_blob_bytes(row["git_blob"]))
            self.assertEqual(hashlib.sha256(content).hexdigest(), row["file_sha256_lf_normalized"])
        with mock.patch.object(subject, "_git_blob_bytes", return_value=b"wrong blob bytes\n"):
            with self.assertRaisesRegex(RuntimeError, "Git blob content hash mismatch"):
                subject.verify_sources_manifest()
        with mock.patch.object(subject, "_lf_sha256", return_value="0" * 64):
            with self.assertRaisesRegex(RuntimeError, "manifest hash mismatch"):
                subject.verify_sources_manifest()
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(subject.EXPECTED_BASE_COMMIT, "missing-universal-Euler-source")
        with self.assertRaisesRegex(RuntimeError, "git blob read failed"):
            subject._git_blob_bytes("0" * 40)

    def test_strict_resource_bounds_refusals_and_no_float_payloads(self) -> None:
        resources = self.fixture["resource_contract"]
        declared = resources["declared_work_upper_bound"]
        self.assertEqual(declared, resources["identity_work_upper_bound"] + resources["constructive_work_upper_bound"])
        self.assertLess(declared, resources["work_unit_cap_exclusive"])
        self.assertEqual(resources["float_operations"], 0)
        self.assertFalse(resources["external_symbolic_engine"])
        reject_float(self.fixture)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=declared)
        row_bound = subject.identity_work_bound(2, 2)["declared_work_upper_bound"]
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.multiset_descent_numerator(2, 2, resource_cap=row_bound)
        self.assertEqual(subject.multiset_descent_numerator(2, 2, resource_cap=row_bound + 1)[0], [1, 1])
        balanced_bound = subject.balanced_work_bound(2, 1)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.balanced_weights(2, 1, resource_cap=balanced_bound)
        self.assertEqual(sum(subject.balanced_weights(2, 1, resource_cap=balanced_bound + 1).values()), 4)
        for kwargs in ({"max_n": 6}, {"max_k": 6}, {"max_n": 0}, {"max_k": -1}):
            with self.assertRaises(ValueError):
                subject.build_fixture(**kwargs)
        for kwargs in ({"max_n": True}, {"max_k": 1.5}):
            with self.assertRaises(TypeError):
                subject.build_fixture(**kwargs)
        with self.assertRaises(ValueError):
            subject.identity_coefficient(2, 2, 100)
        with self.assertRaises(ValueError):
            subject.balanced_weights(2, 3)
        with self.assertRaises(ValueError):
            list(subject._compositions(100, 2))

    def test_note_claims_scope_and_math_text_integrity(self) -> None:
        raw = subject.NOTE_PATH.read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        note = raw.decode("utf-8")
        self.assertEqual(note.count(r"\("), note.count(r"\)"))
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        self.assertGreaterEqual(len(re.findall(r"\\\[(.*?)\\\]", note, re.DOTALL)), 25)
        for claim in self.fixture["claims"]:
            self.assertIn(claim, note)
        for required in (
            "Zariski-dense", "stable sorting", "self-dual", "unitarity",
            "not a priority claim", "not a new automorphic lift",
            "n^{2m}", "scalar recurrence", "Negative virtual multiplicities",
        ):
            self.assertIn(required, note)
        for field, value in self.fixture["scope_firewall"].items():
            self.assertTrue(value, field)
        self.assertTrue(
            self.fixture["universal_proof_obligations"]["finite_rows_do_not_prove_universal_quantifiers"]
        )

    def test_stored_fixture_and_all_artifact_hashes(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        for field in ("identity_controls", "constructive_controls"):
            self.assertEqual(stored[field]["rows_sha256"], subject._canonical_sha256(stored[field]["rows"]))
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (subject.NOTE_PATH, "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            self.assertEqual(stored["producer"][field], subject._lf_sha256(path))
        self.assertEqual(stored["identity_controls"]["row_count"], 20)
        self.assertEqual(stored["identity_controls"]["no_go_row_count"], 9)
        self.assertEqual(stored["constructive_controls"]["row_count"], 6)


if __name__ == "__main__":
    unittest.main()
