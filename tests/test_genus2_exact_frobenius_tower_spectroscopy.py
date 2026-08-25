"""Focused exact tests for marked genus-two Frobenius tower spectroscopy."""

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

import genus2_exact_frobenius_tower_spectroscopy as subject


class Genus2ExactFrobeniusTowerSpectroscopyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate = subject.build_certificate()

    def test_source_trace_polynomials_are_exact(self) -> None:
        self.assertEqual(subject.TRACE_POLYNOMIALS["chi_(0,3)"], (-1, -2, 0, 0, 1))
        self.assertEqual(subject.TRACE_POLYNOMIALS["chi_(2,2)"], (-2, -2, -1, 2))
        for prime in subject.CONTROL_PRIMES:
            for index in range(1, subject.TOWER_TERMS + 1):
                q = prime**index
                self.assertEqual(
                    subject.tower_trace("chi_(0,3)", prime, index), q**4 - 2 * q - 1
                )
                self.assertEqual(
                    subject.tower_trace("chi_(2,2)", prime, index),
                    2 * q**3 - q**2 - 2 * q - 2,
                )

    def test_virtual_spectra_reconstruct_every_tower_value(self) -> None:
        for channel in subject.TRACE_POLYNOMIALS:
            for prime in subject.CONTROL_PRIMES:
                spectrum = subject.virtual_tate_spectrum(channel, prime)
                for index in range(1, 10):
                    reconstructed = sum(
                        multiplicity * eigenvalue**index
                        for _, eigenvalue, multiplicity in spectrum
                    )
                    self.assertEqual(
                        reconstructed, subject.tower_trace(channel, prime, index)
                    )

    def test_data_recovery_matches_root_characteristic_polynomial(self) -> None:
        for channel in subject.TRACE_POLYNOMIALS:
            for prime in subject.CONTROL_PRIMES:
                guard = subject.OperationGuard()
                spectrum = subject.virtual_tate_spectrum(channel, prime)
                order = len(spectrum)
                roots = tuple(row[1] for row in spectrum)
                values = tuple(
                    subject.tower_trace(channel, prime, index)
                    for index in range(1, 2 * order + 1)
                )
                recovered = subject.recover_recurrence(values, order, guard)
                characteristic = subject.characteristic_polynomial(roots)
                self.assertEqual(recovered, tuple(map(Fraction, characteristic[:-1])))

    def test_hankel_minimality_certificate_is_exact(self) -> None:
        controls = self.certificate["exact_recovery_controls"]
        for row in controls:
            self.assertNotEqual(row["rank_r_Hankel_determinant"], [0, 1])
            self.assertEqual(row["rank_r_plus_1_Hankel_determinant"], [0, 1])
            self.assertTrue(row["held_out_predictions_exact"])
            self.assertEqual(
                row["held_out_indices"][1] - row["held_out_indices"][0] + 1,
                subject.HOLDOUT_TERMS,
            )

    def test_cross_characteristic_ambiguity_fails_first_tower_holdout(self) -> None:
        factor = lambda q: (q - 3) * (q - 5) * (q - 7)
        self.assertEqual([factor(q) for q in (3, 5, 7)], [0, 0, 0])
        self.assertEqual(factor(9), 48)
        self.assertEqual(factor(25), 7_920)

    def test_source_locks_and_tamper_rejection(self) -> None:
        for path in (subject.B3_PATH, subject.M22_PATH):
            lock = subject.SOURCE_LOCKS[path.name]
            self.assertEqual(subject._sha256_lf(path), lock["lf_sha256"])
            parsed = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(parsed["schema"], lock["schema"])
            self.assertEqual(parsed["payload_sha256"], lock["payload_sha256"])
        with tempfile.TemporaryDirectory() as directory:
            tampered = Path(directory) / subject.B3_PATH.name
            raw = bytearray(subject.B3_PATH.read_bytes())
            raw[-2] = (raw[-2] + 1) % 128
            tampered.write_bytes(raw)
            with self.assertRaises(ArithmeticError):
                subject._load_locked_json(
                    tampered, subject.SOURCE_LOCKS[subject.B3_PATH.name]
                )

    def test_scope_provenance_and_fixture(self) -> None:
        scope = self.certificate["scope"]
        self.assertTrue(scope["all_odd_prime_towers"])
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["curves_enumerated"], 0)
        resources = self.certificate["provenance"]["resource_contract"]
        self.assertLessEqual(
            resources["exact_operations_used"], resources["maximum_exact_operations"]
        )
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.certificate)
        for label, path in (
            ("producer_sha256_lf", Path(subject.__file__)),
            ("note_sha256_lf", subject.NOTE_PATH),
            ("test_sha256_lf", Path(__file__)),
        ):
            self.assertEqual(
                stored["provenance"][label],
                hashlib.sha256(
                    path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
                ).hexdigest(),
            )
        payload = dict(stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))

    def test_cli_replay_and_fail_closed_domains(self) -> None:
        for optimization in ([], ["-O"]):
            process = subprocess.run(
                [sys.executable, *optimization, str(Path(subject.__file__)), "--check"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )
            self.assertEqual(process.returncode, 0, process.stderr)
            self.assertIn(
                "PASS_GENUS2_EXACT_FROBENIUS_TOWER_SPECTROSCOPY", process.stdout
            )
        for arguments in (("unknown", 3, 1), ("chi_(0,3)", 9, 1), ("chi_(0,3)", 3, 0)):
            with self.assertRaises(ValueError):
                subject.tower_trace(*arguments)
        with self.assertRaises(ValueError):
            subject.recover_recurrence((1, 2, 3), 2, subject.OperationGuard())


if __name__ == "__main__":
    unittest.main()
