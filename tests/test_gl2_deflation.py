"""Focused exact tests for the GL(2) parity/rank-deflation pilot."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
GL2 = ROOT / "research" / "l-families" / "atlas" / "gl2"
sys.path.insert(0, str(GL2))

import deflation as subject  # noqa: E402
import verify  # noqa: E402


Q = Fraction


class ExactInputTests(unittest.TestCase):
    def test_exact_rejects_float(self) -> None:
        with self.assertRaisesRegex(TypeError, "floats are forbidden"):
            subject.exact(0.5)  # type: ignore[arg-type]

    def test_nodes_fail_closed_at_center_and_negative_axis(self) -> None:
        for nodes in ([0, 1], [-1, 2]):
            with self.subTest(nodes=nodes):
                with self.assertRaisesRegex(ValueError, "x_i > 0"):
                    subject.exact_nodes(nodes)

    def test_root_number_parity_contract(self) -> None:
        for sign, order in ((1, 0), (1, 2), (-1, 1), (-1, 3)):
            subject.validate_parity(sign, order)
        with self.assertRaisesRegex(ValueError, "parity"):
            subject.validate_parity(1, 1)
        with self.assertRaisesRegex(ValueError, "parity"):
            subject.validate_parity(-1, 2)


class AtomIdentityTests(unittest.TestCase):
    nodes = (Q(1), Q(2))

    def test_loewner_atom_has_negative_sign(self) -> None:
        self.assertEqual(
            subject.central_atom(self.nodes, 3, subject.LOEWNER_DIFFERENCE),
            [[Q(-3), Q(-3, 2)], [Q(-3, 2), Q(-3, 4)]],
        )

    def test_pick_sum_atom_has_positive_sign(self) -> None:
        self.assertEqual(
            subject.central_atom(self.nodes, 3, subject.PICK_SUM),
            [[Q(3), Q(3, 2)], [Q(3, 2), Q(3, 4)]],
        )

    def test_nonzero_atom_is_exactly_rank_one(self) -> None:
        for convention in subject.CONVENTIONS:
            with self.subTest(convention=convention):
                atom = subject.central_atom(self.nodes, 7, convention)
                self.assertEqual(subject.rank(atom), 1)
                expected = (
                    subject.Inertia(0, 1, 1)
                    if convention == subject.LOEWNER_DIFFERENCE
                    else subject.Inertia(1, 0, 1)
                )
                self.assertEqual(subject.inertia(atom), expected)

    def test_full_and_parity_deflation_are_distinct_at_rank_three(self) -> None:
        for convention in subject.CONVENTIONS:
            with self.subTest(convention=convention):
                packet = subject.make_packet(
                    nodes=self.nodes,
                    root_number=-1,
                    central_order=3,
                    c=1,
                    d=0,
                    convention=convention,
                )
                self.assertEqual(packet.forced_order, 1)
                self.assertEqual(packet.excess_order, 2)
                self.assertEqual(packet.fully_deflated, packet.background)
                self.assertEqual(
                    subject.subtract(packet.parity_deflated, packet.background),
                    subject.central_atom(self.nodes, 2, convention),
                )


class SyntheticBackgroundTests(unittest.TestCase):
    def test_background_is_exact_kernel_of_cz_plus_dz_cubed(self) -> None:
        nodes = (Q(1), Q(2))
        self.assertEqual(
            subject.synthetic_background(
                nodes, 2, 3, subject.LOEWNER_DIFFERENCE
            ),
            [[Q(11), Q(23)], [Q(23), Q(38)]],
        )
        self.assertEqual(
            subject.synthetic_background(nodes, 2, 3, subject.PICK_SUM),
            [[Q(5), Q(11)], [Q(11), Q(14)]],
        )

    def test_minimal_odd_control_exposes_convention_sign(self) -> None:
        loewner = subject.make_packet(
            nodes=(1, 2),
            root_number=-1,
            central_order=1,
            c=1,
            d=0,
            convention=subject.LOEWNER_DIFFERENCE,
        )
        pick_sum = subject.make_packet(
            nodes=(1, 2),
            root_number=-1,
            central_order=1,
            c=1,
            d=0,
            convention=subject.PICK_SUM,
        )
        self.assertEqual(subject.determinant(loewner.raw), Q(-1, 4))
        self.assertEqual(subject.inertia(loewner.raw), subject.Inertia(1, 1, 0))
        self.assertEqual(subject.determinant(pick_sum.raw), Q(1, 4))
        self.assertEqual(subject.inertia(pick_sum.raw), subject.Inertia(2, 0, 0))

    def test_hostile_background_stays_indefinite_after_full_deflation(self) -> None:
        for convention in subject.CONVENTIONS:
            packet = subject.make_packet(
                nodes=(1, 2, 4),
                root_number=-1,
                central_order=1,
                c=1,
                d=1,
                convention=convention,
            )
            signature = subject.inertia(packet.fully_deflated)
            self.assertGreater(signature.negative, 0)


class ExactLinearAlgebraTests(unittest.TestCase):
    def test_inertia_handles_zero_diagonal_two_by_two_pivot(self) -> None:
        self.assertEqual(
            subject.inertia([[0, 2, 0], [2, 0, 0], [0, 0, 0]]),
            subject.Inertia(1, 1, 1),
        )

    def test_inertia_rejects_nonsymmetric_input(self) -> None:
        with self.assertRaisesRegex(ValueError, "symmetric"):
            subject.inertia([[1, 2], [3, 4]])

    def test_determinant_is_affine_in_atom_multiplicity(self) -> None:
        nodes = (1, 2, 4)
        for convention in subject.CONVENTIONS:
            background = subject.synthetic_background(nodes, 1, 1, convention)
            for multiplicity in range(5):
                actual = subject.determinant(
                    subject.add(
                        background,
                        subject.central_atom(nodes, multiplicity, convention),
                    )
                )
                self.assertEqual(
                    actual,
                    subject.determinant_affine_prediction(
                        background, nodes, multiplicity, convention
                    ),
                )

    def test_frobenius_correction_identity(self) -> None:
        nodes = (1, 2, 4)
        self.assertEqual(subject.correction_norm_squared(nodes, 1), Q(441, 256))
        for convention in subject.CONVENTIONS:
            atom = subject.central_atom(nodes, 3, convention)
            self.assertEqual(
                subject.frobenius_norm_squared(atom),
                subject.correction_norm_squared(nodes, 3),
            )


class FixtureVerificationTests(unittest.TestCase):
    def test_all_labeled_controls_verify(self) -> None:
        report = verify.build_report()
        self.assertEqual(report["result"], "PASS")
        self.assertEqual(report["status"], "EXACT_RATIONAL_SYNTHETIC_CONTROL_ONLY")
        self.assertEqual(len(report["controls"]), 5)
        rejected = next(
            control
            for control in report["controls"]
            if control["id"] == "parity-mismatch-rejected"
        )
        self.assertEqual(rejected["result"], "EXPECTED_ERROR_CONFIRMED")


if __name__ == "__main__":
    unittest.main()
