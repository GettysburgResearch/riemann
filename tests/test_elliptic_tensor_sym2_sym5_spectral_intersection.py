"""Independent exact tests for the tensor-Sym2 / Sym5 intersection packet."""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_tensor_sym2_sym5_spectral_intersection as subject  # noqa: E402


def direct_symmetric_character(m: int, t: int, q: int) -> int:
    values = [1, t]
    if m < 2:
        return values[m]
    for _ in range(2, m + 1):
        values.append(t * values[-1] - q * values[-2])
    return values[m]


def independent_sym5_elementary(C: int, q: int) -> tuple[int, int, int]:
    return (
        C * (C * C - q) * (C * C - 3 * q),
        q * direct_symmetric_character(8, C, q)
        + q**3 * direct_symmetric_character(4, C, q)
        + q**5,
        q**3 * direct_symmetric_character(9, C, q)
        + q**5 * direct_symmetric_character(5, C, q)
        + q**6 * direct_symmetric_character(3, C, q),
    )


def independent_predicate(A: int, B: int, C: int, q: int) -> bool:
    return (
        B * B == C * C and q * A == C * (C * C - 3 * q)
    ) or (
        A == C and q * B * B == (C * C - 2 * q) ** 2
    )


class EllipticTensorSym2Sym5SpectralIntersectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_newton_and_raw_coefficient_formulas(self) -> None:
        residuals = subject.coefficient_identity_residuals()
        self.assertEqual(len(residuals), 6)
        self.assertTrue(all(not residual for residual in residuals.values()))

        for q in (3, 5, 9, 25):
            bound = math.isqrt(4 * q)
            for A in range(-bound, bound + 1):
                for B in range(-bound, bound + 1):
                    e1, e2, e3 = subject.tensor_sym2_elementary(A, B, q)
                    self.assertEqual(e1, A * (B * B - q))
                    self.assertEqual(
                        e2, q * (B * B - q) * (A * A + B * B - 3 * q)
                    )
                    self.assertEqual(
                        e3,
                        q**2
                        * A
                        * (q * A * A + B**4 - 2 * q * B * B - 2 * q * q),
                    )
            for C in range(-bound, bound + 1):
                self.assertEqual(
                    subject.sym5_elementary(C, q),
                    independent_sym5_elementary(C, q),
                )

    def test_weight_dilation_and_both_graph_identities(self) -> None:
        for q, triples in {
            3: [(0, 0, 0), (0, 3, 3), (0, -3, 3)],
            9: [(-6, -3, 3), (3, 3, 3), (0, 6, 0), (6, -6, 6)],
            81: [(-15, 7, -15), (12, 2, 12), (0, 18, 0)],
        }.items():
            for A, B, C in triples:
                with self.subTest(q=q, A=A, B=B, C=C):
                    tensor = subject.tensor_sym2_factor(A, B, q)
                    dilated = tuple(
                        coefficient * q**degree
                        for degree, coefficient in enumerate(tensor)
                    )
                    self.assertEqual(subject.dilated_tensor_factor(A, B, q), dilated)
                    self.assertEqual(dilated, subject.sym5_factor(C, q))
                    self.assertTrue(independent_predicate(A, B, C, q))

        negative = [(5, 1, 1, 1), (9, 1, 2, 1), (25, 3, 4, 5)]
        for q, A, B, C in negative:
            self.assertNotEqual(
                subject.dilated_tensor_factor(A, B, q), subject.sym5_factor(C, q)
            )

    def test_exact_groebner_and_cyclotomic_residual_certificates(self) -> None:
        guard = subject.ResourceGuard()
        certificate = subject.groebner_and_torsion_certificate(guard)
        self.assertEqual(
            certificate["main_leading_monomials"],
            [[3, 0, 0], [1, 2, 0], [1, 0, 4], [0, 6, 0], [0, 4, 6]],
        )
        self.assertEqual(certificate["branch_specialization_zero_residual_count"], 12)
        self.assertTrue(certificate["all_branch_specialization_residuals_zero"])
        self.assertEqual(certificate["runtime_symbolic_packages"], 0)
        self.assertIn("p7+(z)", certificate["elimination_factors"]["basis_product"])
        self.assertIn("x=0 or x=-z", certificate["algebraic_residuals"]["order_12"]["extra_points"])

        main = subject._reduced_groebner_basis(
            subject.coefficient_difference_generators()
        )
        self.assertEqual(main, subject.expected_main_groebner_basis())
        for left, right in ((1, 1), (-1, -1)):
            self.assertNotEqual(left**3 + left**2 - 2 * left - 1, 0)
            self.assertNotEqual(right**3 - right**2 - 2 * right + 1, 0)

    def test_all_m_weight_ladder_is_exact_beyond_bounded_fixture(self) -> None:
        for r in range(1, 41):
            row = subject.ladder_weight_certificate(r)
            target = row["target_weights"]
            self.assertEqual(row["Std(w^(r+1))_tensor_Symr(w)_weights"], target)
            self.assertEqual(row["Std(w)_tensor_Symr(w^2)_weights"], target)
            self.assertEqual(len(target), 2 * r + 2)
        ladder = self.fixture["universal_tensor_symmetric_power_ladder"]
        self.assertEqual(ladder["bounded_regression"]["maximum_r"], 12)
        self.assertIn("sufficient", ladder["classification_boundary"])
        self.assertIn("chosen sqrt(q)", ladder["raw_dilation"])

    def test_compact_moments_first_split_at_degree_six(self) -> None:
        moments = subject.compact_trace_moments(8)
        self.assertEqual(
            moments["Std_SU2_tensor_Sym2_SU2_independent_product"],
            [1, 0, 1, 0, 6, 0, 75, 0, 1274],
        )
        self.assertEqual(
            moments["Sym5_SU2"], [1, 0, 1, 0, 6, 0, 111, 0, 2666]
        )
        self.assertEqual(
            moments["Std_SU2_tensor_Sym2_SU2_independent_product"][:5],
            moments["Sym5_SU2"][:5],
        )
        self.assertNotEqual(
            moments["Std_SU2_tensor_Sym2_SU2_independent_product"][6],
            moments["Sym5_SU2"][6],
        )

    def test_locked_7975_triples_and_member_weights(self) -> None:
        replay = self.fixture["locked_trace_triple_replay"]
        self.assertEqual(replay["aggregate"]["ordered_trace_triples_checked"], 7975)
        expected = {
            3: (7, 5, 80),
            5: (9, 1, 8000),
            7: (11, 1, 74088),
            11: (13, 1, 10648000),
            13: (15, 1, 3796416),
        }
        for row in replay["families"]:
            q = row["q"]
            atoms, hits, weight = expected[q]
            self.assertEqual(row["trace_atom_count"], atoms)
            self.assertEqual(row["ordered_trace_triples_checked"], atoms**3)
            self.assertEqual(row["factor_equal_trace_triple_count"], hits)
            self.assertEqual(row["factor_equal_member_weight"], weight)
            for hit in row["hits"]:
                A, B, C = hit["A"], hit["B"], hit["C"]
                self.assertTrue(independent_predicate(A, B, C, q))
                self.assertEqual(
                    subject.dilated_tensor_factor(A, B, q),
                    subject.sym5_factor(C, q),
                )

    def test_all_q_hasse_count_and_nonsquare_second_branch(self) -> None:
        expected_counts = {
            (3, 1): 5,
            (5, 1): 1,
            (7, 1): 1,
            (3, 2): 15,
            (5, 2): 15,
            (3, 4): 31,
            (5, 6): 79,
        }
        for (p, exponent), expected in expected_counts.items():
            theorem = subject.hasse_lattice_count_theorem(p, exponent)
            self.assertEqual(theorem["union_distinct_triples"], expected)
            if exponent % 2:
                self.assertEqual(theorem["branch_two_distinct_triples"], 0)
            else:
                k = exponent // 2
                self.assertEqual(
                    theorem["square_q_closed_form"],
                    8 * p ** (k // 3) + 8 * p ** (k // 2) - 1,
                )

        synthetic = self.fixture["synthetic_q9_hasse_replay"]
        self.assertEqual(synthetic["ordered_trace_triples_checked"], 13**3)
        self.assertEqual(synthetic["factor_equal_trace_triple_count"], 15)
        self.assertEqual(
            synthetic["all_q_lattice_count_specialization"]["branch_overlap_distinct_triples"],
            4,
        )

        for q in (3, 5, 7, 11, 27, 125):
            bound = math.isqrt(4 * q)
            for A in range(-bound, bound + 1):
                for B in range(-bound, bound + 1):
                    for C in range(-bound, bound + 1):
                        branch_two = A == C and q * B * B == (C * C - 2 * q) ** 2
                        self.assertFalse(branch_two)

    def test_source_payload_file_hashes_and_conventions(self) -> None:
        locks = self.fixture["source_and_file_locks"]
        self.assertEqual(
            set(locks["source_locks"]),
            {"genus1", "sym5", "full_factor", "cyclotomic", "predecessor"},
        )
        for lock in locks["source_locks"].values():
            fixture_path = ROOT / lock["fixture_path"]
            producer_path = ROOT / lock["producer_path"]
            fixture_bytes = fixture_path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            producer_bytes = producer_path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                hashlib.sha256(fixture_bytes).hexdigest(),
                lock["fixture_sha256_lf_normalized"],
            )
            self.assertEqual(
                hashlib.sha256(producer_bytes).hexdigest(),
                lock["producer_sha256_lf_normalized"],
            )
        self.assertEqual(
            self.fixture["conventions"]["three_base_factors"],
            "P_t(T)=1-t*T+q*T^2 for geometric traces t=A,B,C",
        )

    def test_payload_resources_no_floats_and_owned_integrity(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))
        resources = stored["resource_contract"]
        self.assertEqual(resources["actual_locked_trace_triples"], 7975)
        self.assertLess(
            resources["accounted_work_unit_ledger"]["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertEqual(resources["field_curve_or_model_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)
        self.assertEqual(resources["runtime_symbolic_packages"], 0)

        def reject_floats(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_floats(item)
            elif isinstance(value, list):
                for item in value:
                    reject_floats(item)

        reject_floats(stored)
        for lock in stored["source_and_file_locks"]["owned_file_locks"].values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                hashlib.sha256(normalized).hexdigest(), lock["sha256_lf_normalized"]
            )

    def test_note_scope_and_integrity(self) -> None:
        text = subject.NOTE_PATH.read_text(encoding="utf-8")
        self.assertEqual(text.count(r"\["), text.count(r"\]"))
        self.assertEqual(text.count(r"\begin{aligned}"), text.count(r"\end{aligned}"))
        self.assertEqual(text.count("```"), 2)
        self.assertIsNone(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))
        for anchor in (
            "P_{A\\otimes\\operatorname{Sym}^2B}(qT)",
            "N\\bigl(p^{2k}\\bigr)",
            "7{,}975",
            "Orders 7 and 14",
            "all-\\(r\\) spectral ladder",
            "representation homomorphism",
            "RH, or GRH",
        ):
            self.assertIn(anchor, text)
        source = Path(subject.__file__).read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"(?m)^\s*assert\b", source))

    def test_strict_refusals_survive_optimized_python(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5, 7))
        for malformed in (True, Fraction(1), "1", 1.0, None):
            with self.subTest(value=malformed):
                with self.assertRaises(TypeError):
                    subject.tensor_sym2_elementary(malformed, 1, 3)
        for invalid_q in (2, 4, 8, 15, 21, 45):
            with self.subTest(q=invalid_q):
                with self.assertRaisesRegex(ValueError, "odd prime power"):
                    subject.graph_branches(0, 0, 0, invalid_q)
        for invalid_r in (0, -1):
            with self.assertRaisesRegex(ValueError, "positive"):
                subject.ladder_weight_certificate(invalid_r)
        for p, exponent in ((9, 1), (2, 1), (5, 0)):
            with self.assertRaises(ValueError):
                subject.hasse_lattice_count_theorem(p, exponent)
        with self.assertRaisesRegex(RuntimeError, "cap exceeded"):
            guard = subject.ResourceGuard()
            for _ in range(subject.LOCKED_TRIPLE_CAP_INCLUSIVE + 1):
                guard.charge_locked_triple()
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.ResourceGuard().charge(
                "deliberate_refusal", subject.ACCOUNTED_WORK_CAP_EXCLUSIVE
            )


if __name__ == "__main__":
    unittest.main()
