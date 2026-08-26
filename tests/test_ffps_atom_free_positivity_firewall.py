from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_atom_free_positivity_firewall.py"
)
SPEC = importlib.util.spec_from_file_location("positivity_firewall", MODULE_PATH)
assert SPEC and SPEC.loader
positivity_firewall = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(positivity_firewall)


class AtomFreePositivityFirewallTest(unittest.TestCase):
    def test_signature_certificates_span(self) -> None:
        for quotient_order in (2, 4, 8):
            for coset_size in (1, 2, 5):
                row = positivity_firewall.signature_certificate(
                    quotient_order, coset_size
                )
                self.assertEqual(row["certificate_dimension"], row["atom_count"])
                self.assertEqual(row["positive_eigenvalue"], str(row["atom_count"]))
                self.assertEqual(
                    row["negative_eigenvalue"],
                    str(Fraction(-row["atom_count"], quotient_order - 1)),
                )
                self.assertEqual(
                    row["sharp_scalar_diagonal_repair"],
                    str(Fraction(row["atom_count"], quotient_order - 1)),
                )

    def test_kernel_deletes_whole_same_coset_blocks(self) -> None:
        kernel = positivity_firewall.off_coset_kernel(4, 3)
        for row in range(12):
            for column in range(12):
                expected = Fraction(0) if row // 3 == column // 3 else Fraction(4, 3)
                self.assertEqual(kernel[row][column], expected)

    def test_invalid_inputs(self) -> None:
        for bad in (True, 1, 16):
            with self.assertRaises(ValueError):
                positivity_firewall.off_coset_kernel(bad, 1)
        for bad in (True, 0, 6):
            with self.assertRaises(ValueError):
                positivity_firewall.off_coset_kernel(2, bad)

    def test_resource_caps(self) -> None:
        payload = positivity_firewall.run()
        caps = payload["resource_caps"]
        self.assertEqual(caps["maximum_matrix_size"], 40)
        self.assertEqual(caps["point_counts"], 0)
        self.assertEqual(caps["floating_point_operations"], 0)


if __name__ == "__main__":
    unittest.main()
