"""Exact fail-closed tests for the marked-Weierstrass stack adapter."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_marked_weierstrass_stack_adapter as subject


class Genus2MarkedWeierstrassStackAdapterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = subject.build_certificate()

    def test_all_q_symbolic_group_orders_and_stack_mass(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
            row = subject.group_orders(q)
            self.assertEqual(row["H5"], q**4 * (q - 1))
            self.assertEqual(row["G_square"], q * (q - 1) // 2)
            self.assertEqual(row["G_lifted"], q * (q - 1))
            self.assertEqual(row["AGL_full"], q * (q - 1))
            self.assertEqual(row["marked_stack_mass"], q**3)

        exact = self.certificate["exact_cardinalities"]
        polynomials = exact["symbolic_polynomials_in_increasing_q_power"]
        self.assertEqual(
            polynomials["H5"],
            [[0, 1], [0, 1], [0, 1], [0, 1], [-1, 1], [1, 1]],
        )
        self.assertEqual(polynomials["G_square"], [[0, 1], [-1, 2], [1, 2]])
        self.assertEqual(polynomials["G_lifted"], [[0, 1], [-1, 1], [1, 1]])
        self.assertEqual(polynomials["stack_mass"], [[0, 1], [0, 1], [0, 1], [1, 1]])

    def test_prime_power_domain_is_fail_closed(self) -> None:
        for invalid in (0, 1, 6, 12, 15, 21):
            with self.assertRaises(ValueError):
                subject.group_orders(invalid)
        for even_prime_power in (2, 4, 8, 16):
            with self.assertRaises(ValueError):
                subject.group_orders(even_prime_power)

    def test_stabilizer_lift_and_central_parity(self) -> None:
        for stabilizer in (1, 2, 3, 5, 12):
            self.assertEqual(subject.automorphism_order(stabilizer), 2 * stabilizer)
        with self.assertRaises(ValueError):
            subject.automorphism_order(0)

        self.assertEqual(subject.central_weight((0, 3)), 6)
        self.assertEqual(subject.central_weight((2, 2)), 6)
        self.assertEqual(subject.central_weight((0, 4)), 8)
        self.assertEqual(subject.central_sign((0, 3)), 1)
        self.assertEqual(subject.central_sign((1, 0)), -1)
        self.assertEqual(subject.central_sign((3, 2)), -1)
        with self.assertRaises(ValueError):
            subject.central_weight((-1, 2))

    def test_three_even_channels_have_exact_adapter_not_values(self) -> None:
        channels = self.certificate["trace_theorem"]["even_channels_closed_by_adapter"]
        self.assertEqual(set(channels), {"chi_(0,3)", "chi_(2,2)", "chi_(0,4)"})
        self.assertEqual(channels["chi_(0,3)"]["local_system_weight"], 6)
        self.assertEqual(channels["chi_(2,2)"]["local_system_weight"], 6)
        self.assertEqual(channels["chi_(0,4)"]["local_system_weight"], 8)
        for row in channels.values():
            self.assertEqual(row["central_character"], 1)
            self.assertEqual(row["adapter_status"], "PROVED_BY_THIS_PACKET")
            self.assertEqual(row["candidate_value_status"], "NOT_PROVED_BY_THIS_PACKET")

        boundaries = self.certificate["claim_boundaries"]
        self.assertIn(
            "the conjectural polynomial values of those three channel traces",
            boundaries["not_proved"],
        )
        self.assertFalse(self.certificate["scope"]["rh_or_grh_claim"])

    def test_sign_convention_and_odd_twist_cancellation_are_explicit(self) -> None:
        convention = self.certificate["frobenius_convention"]
        self.assertEqual(convention["point_count"], "#C_D(F_q)=q+1+a_D")
        self.assertEqual(
            convention["normalized_standard_trace"], "Tr(U_D)=-a_D/sqrt(q)"
        )
        self.assertEqual(
            convention["normalized_second_elementary_coefficient"],
            "e_2(U_D)=b_D/q",
        )
        odd = self.certificate["odd_central_weight"]
        self.assertIn("total", odd["exact_result"])
        self.assertIn("does not assert", odd["scope_firewall"])

    def test_source_locks_and_internal_payload_hashes(self) -> None:
        for name in (
            "genus2_family_measures.json",
            "genus2_high_weight_channel_probe.json",
        ):
            lock = subject.SOURCE_LOCKS[name]
            path = FUNCTION_FIELD / name
            raw = path.read_bytes()
            actual_lf = hashlib.sha256(subject._lf_bytes(raw)).hexdigest()
            self.assertEqual(actual_lf, lock["lf_sha256"])
            parsed = json.loads(raw.decode("utf-8"))
            digest = parsed.pop("payload_sha256")
            self.assertEqual(digest, lock["canonical_payload_sha256"])
            self.assertEqual(subject._canonical_payload_sha256(parsed), digest)

        guarded_lock = subject.SOURCE_LOCKS[
            "guarded_cohomology_conjecture_inference.py"
        ]["lf_sha256"]
        self.assertEqual(
            subject._sha256_lf(subject.GUARDED_INFERENCE_PATH), guarded_lock
        )

    def test_locked_loader_rejects_tampering_and_bad_caps(self) -> None:
        source = subject.FAMILY_MEASURES_PATH
        lock = subject.SOURCE_LOCKS[source.name]
        with tempfile.TemporaryDirectory() as directory:
            tampered = Path(directory) / source.name
            raw = bytearray(source.read_bytes())
            raw[-2] = (raw[-2] + 1) % 128
            tampered.write_bytes(bytes(raw))
            with self.assertRaises(ArithmeticError):
                subject._load_locked_json(tampered, lock)
        with self.assertRaises(ValueError):
            subject._load_locked_json(source, lock, maximum_bytes=0)
        with self.assertRaises(ValueError):
            subject._load_locked_json(
                source, lock, maximum_bytes=subject.MAX_SOURCE_BYTES_EACH + 1
            )

    def test_exact_arithmetic_and_operation_cap(self) -> None:
        guard = subject.OperationGuard(limit=20)
        product = subject.polynomial_multiply(
            (Fraction(-1), Fraction(1)),
            (Fraction(0), Fraction(1)),
            guard,
        )
        self.assertEqual(product, (Fraction(0), Fraction(-1), Fraction(1)))
        self.assertLessEqual(guard.total, 20)
        with self.assertRaises(RuntimeError):
            guard.consume("forced_overflow", 21)

        resource = self.certificate["provenance"]["resource_contract"]
        self.assertEqual(resource["finite_fields_enumerated"], 0)
        self.assertEqual(resource["curves_enumerated"], 0)
        self.assertLessEqual(
            resource["exact_operations_used"], resource["exact_operation_cap"]
        )
        self.assertEqual(resource["exact_operation_cap"], 4_096)

    def test_fixture_is_canonical_and_self_hashed(self) -> None:
        checked_in = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(checked_in, self.certificate)
        without_digest = dict(checked_in)
        digest = without_digest.pop("payload_sha256")
        self.assertEqual(subject._canonical_payload_sha256(without_digest), digest)

        local_hashes = checked_in["provenance"]["source_hashes_lf_sha256"]
        paths = {
            "producer": Path(subject.__file__),
            "note": subject.NOTE_PATH,
            "test": Path(__file__),
        }
        for label, path in paths.items():
            self.assertEqual(local_hashes[label], subject._sha256_lf(path))

    def test_cli_check_passes_under_normal_and_optimized_python(self) -> None:
        command = [sys.executable, str(Path(subject.__file__)), "--check"]
        normal = subprocess.run(
            command,
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(normal.returncode, 0, normal.stderr)
        self.assertIn("PASS_GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER", normal.stdout)
        optimized = subprocess.run(
            [sys.executable, "-O", str(Path(subject.__file__)), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(optimized.returncode, 0, optimized.stderr)
        self.assertIn("PASS_GENUS2_MARKED_WEIERSTRASS_STACK_ADAPTER", optimized.stdout)


if __name__ == "__main__":
    unittest.main()
