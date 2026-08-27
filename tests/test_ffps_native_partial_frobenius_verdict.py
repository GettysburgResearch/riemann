from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_native_partial_frobenius_verdict.py"
)
SPEC = importlib.util.spec_from_file_location("native_partial_frobenius", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class NativePartialFrobeniusVerdictTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_centered_incidence_rank_formula(self) -> None:
        for residue_size in (3, 5, 7, 11):
            for cell_count in (
                residue_size,
                residue_size - 1,
                (residue_size - 1) // 2,
            ):
                with self.subTest(residue_size=residue_size, cell_count=cell_count):
                    matrix = subject.centered_incidence_scaled(residue_size, cell_count)
                    self.assertEqual(
                        subject.matrix_rank(matrix),
                        subject.expected_centered_rank(residue_size, cell_count),
                    )

    def test_fourier_gram_certificate(self) -> None:
        full = subject.fourier_gram_certificate(7, 7)
        sector = subject.fourier_gram_certificate(7, 3)
        self.assertEqual(full["gram_rank"], 6)
        self.assertEqual(sector["gram_rank"], 3)

    def test_bilateral_rank_multiplies(self) -> None:
        left = subject.centered_incidence_scaled(5, 4)
        right = subject.centered_incidence_scaled(7, 6)
        product = subject.kronecker_product(left, right)
        self.assertEqual(len(product), 24)
        self.assertEqual(subject.matrix_rank(product), 24)

    def test_degree_growth_is_exponential(self) -> None:
        panel = subject.rank_panel()
        growth = panel["degree_growth"]
        self.assertEqual(
            [row["residue_size"] for row in growth], [3, 9, 27, 81, 243, 729]
        )
        self.assertTrue(
            all(row["full_centered_rank"] == row["residue_size"] - 1 for row in growth)
        )

    def test_partial_frobenius_obstructions(self) -> None:
        certificate = subject.partial_frobenius_certificate(3, 9)
        self.assertFalse(certificate["supports_equal"])
        self.assertFalse(
            certificate["artin_schreier_h_axis"]["partial_isomorphism_exists"]
        )
        self.assertFalse(
            certificate["artin_schreier_x_axis"]["partial_isomorphism_exists"]
        )
        self.assertEqual(certificate["partial_graph_support"], [(0, 1), (9, 0)])
        with self.assertRaises(ValueError):
            subject.partial_frobenius_certificate(3, 6)
        with self.assertRaises(ValueError):
            subject.partial_frobenius_certificate(4, 4)

    def test_source_factor_graph_retains_crossed_phases(self) -> None:
        graph = subject.source_factor_graph()
        self.assertIn("e_ell(-h Qd^2)", graph["frozen_member"])
        self.assertIn("X=Pc^2", graph["nodes"]["left_physical"])
        self.assertTrue(any("crosses" in edge for edge in graph["edges"]))
        self.assertIn("omega=omega'", graph["wick_image"])

    def test_relative_cleanup_is_not_overclaimed(self) -> None:
        audit = subject.relative_cleanup_audit()
        self.assertFalse(audit["all_native_cleanups_proved_equivariant"])
        self.assertFalse(audit["common_relative_complex_constructed"])
        statuses = {row["status"] for row in audit["rows"]}
        self.assertIn("CONDITIONALLY EQUIVARIANT", statuses)
        self.assertIn("NOT AUDITED GLOBALLY", statuses)

    def test_full_verdict_scope(self) -> None:
        certificate = subject.run(check_sources=False)
        fixture = json.loads(MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8"))
        self.assertEqual(json.loads(json.dumps(certificate)), fixture)
        self.assertFalse(certificate["verdict"]["bounded_or_subpower_external_product"])
        self.assertFalse(
            certificate["verdict"][
                "commuting_partial_frobenius_on_natural_constituents"
            ]
        )
        self.assertIn("actual native image", certificate["verdict"]["scope"])
        self.assertEqual(
            certificate["resource_caps"]["largest_exact_matrix_dimension"], 24
        )
        self.assertEqual(
            certificate["resource_caps"]["finite_field_element_enumeration"], 0
        )
        self.assertEqual(
            certificate["proof_ledger"]["full_native_relative_complex"],
            "NOT CONSTRUCTED",
        )


if __name__ == "__main__":
    unittest.main()
