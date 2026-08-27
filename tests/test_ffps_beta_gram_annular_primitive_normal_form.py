from __future__ import annotations

import importlib.util
import json
import math
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_beta_gram_annular_primitive_normal_form.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("beta_annular_primitive", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load beta annular primitive producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FfpsBetaGramAnnularPrimitiveNormalFormTest(unittest.TestCase):
    def test_source_provenance(self) -> None:
        subject.check_source_blobs()
        self.assertEqual(len(subject.BASE_SOURCE_BLOBS), 4)
        self.assertEqual(len(subject.GEOMETRY_SOURCE_BLOBS), 4)

    def test_beta_local_profiles(self) -> None:
        prime = subject.EXCEPTIONAL_PRIME
        self.assertEqual(
            tuple(subject.beta(prime**exponent) for exponent in range(6)),
            (1, -2, 1, 0, 0, 0),
        )
        for value in range(1, 80):
            if value % prime:
                self.assertEqual(subject.beta(value), subject.mobius(value))

    def test_closed_radial_formula_including_exceptional_layers(self) -> None:
        pairs = (
            (1, 1),
            (2, 3),
            (5, 6),
            (subject.EXCEPTIONAL_PRIME, 1),
            (subject.EXCEPTIONAL_PRIME**2, 1),
            (subject.EXCEPTIONAL_PRIME, 2),
        )
        for pair in pairs:
            for bound in (0, 1, 5, 67, 70, 134):
                with self.subTest(pair=pair, bound=bound):
                    self.assertEqual(
                        subject.direct_radial_coefficient(*pair, bound),
                        subject.closed_radial_coefficient(*pair, bound),
                    )

    def test_every_active_radial_amplitude_has_primitive_beta_sign(self) -> None:
        for left in range(1, 24):
            for right in range(1, 24):
                if math.gcd(left, right) != 1:
                    continue
                primitive_product = subject.beta(left) * subject.beta(right)
                radial = subject.closed_radial_coefficient(left, right, 80)
                if primitive_product == 0:
                    self.assertEqual(radial, 0)
                else:
                    self.assertNotEqual(radial, 0)
                    self.assertEqual(
                        1 if radial > 0 else -1,
                        1 if primitive_product > 0 else -1,
                    )

    def test_exact_source_pair_and_primitive_ray_normal_forms_agree(self) -> None:
        direct = subject.direct_toy_prefix()
        primitive = subject.primitive_toy_prefix()
        self.assertEqual(direct, primitive)
        self.assertEqual(len(direct), 485)
        self.assertEqual(
            subject.canonical_digest(direct),
            "3cd628ce8a8f00e7fa5ad9fe330620d8730f63b6cb9aa02dc77b0d6f16a76f03",
        )

    def test_four_literal_beta_rays_realize_all_annular_phases(self) -> None:
        rows = [subject.witness_row(*row) for row in subject.WITNESS_PAIRS]
        observed = {(row["annulus"], row["ray_contribution_sign"]) for row in rows}
        self.assertEqual(
            observed,
            {("central", 1), ("central", -1), ("outer", 1), ("outer", -1)},
        )
        self.assertGreater(subject.physical_correlation(math.log(3 / 2)), 0)
        self.assertLess(subject.physical_correlation(math.log(3)), 0)

    def test_physical_four_channel_assembly_matches_literal_energy(self) -> None:
        for cap in (10, 24, subject.PHYSICAL_CHANNEL_CAP):
            channels = subject.physical_channel_totals(cap)
            direct = subject.direct_physical_energy(cap)
            self.assertTrue(
                math.isclose(channels["assembled"], direct, rel_tol=0.0, abs_tol=2e-12)
            )
            positive_mass = channels["C_plus"] + channels["O_minus"]
            negative_mass = channels["C_minus"] + channels["O_plus"]
            self.assertLess(negative_mass, positive_mass + channels["D"] / 2.0)
            for name in ("C_plus", "C_minus", "O_plus", "O_minus"):
                self.assertGreater(channels[name], 0)

    def test_annular_off_diagonal_block_is_indefinite(self) -> None:
        for value in (Fraction(2, 7), Fraction(-5, 9)):
            negative, positive = subject.off_diagonal_eigenvalues(value)
            self.assertEqual(negative, -abs(value))
            self.assertEqual(positive, abs(value))
            self.assertLess(negative, 0)
            self.assertGreater(positive, 0)

    def test_half_moment_regressions(self) -> None:
        half_zero = subject.half_moment(0)
        half_first = subject.half_moment(1)
        half_second = subject.half_moment(2)
        expected_first = (2.0 - math.sinh(2.0)) / (32.0 * math.sinh(0.5) ** 4)
        self.assertAlmostEqual(half_zero, 0.0, delta=2e-12)
        self.assertAlmostEqual(half_first, expected_first, delta=4e-11)
        self.assertAlmostEqual(half_second, -1.0, delta=2e-12)

    def test_fixture_and_strict_scope(self) -> None:
        for optimized in (False, True):
            command = ["python", "-B"]
            if optimized:
                command.append("-O")
            command.extend((str(SCRIPT), "--check"))
            completed = subprocess.run(
                command,
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=20,
            )
            self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["termwise_or_geometry_only_annular_positivity"],
            "REFUTED EXACTLY",
        )
        self.assertEqual(
            fixture["proof_ledger"]["central_or_outer_complete_prefix_sign"],
            "NOT DETERMINED",
        )
        self.assertEqual(
            fixture["proof_ledger"]["any_subpower_annular_cancellation"],
            "NOT PROVED",
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.beta(0)
        with self.assertRaises(ValueError):
            subject.closed_radial_coefficient(2, 4, 3)
        with self.assertRaises(ValueError):
            subject.squarefree_harmonic(-1, 67)
        with self.assertRaises(TypeError):
            subject.physical_correlation("0")
        with self.assertRaises(TypeError):
            subject.off_diagonal_eigenvalues(0.5)
        with self.assertRaises(ValueError):
            subject.off_diagonal_eigenvalues(Fraction(0))
        with self.assertRaises(ValueError):
            subject.half_moment(3)
        with self.assertRaises(ValueError):
            subject.half_moment(1, 3)


if __name__ == "__main__":
    unittest.main()
