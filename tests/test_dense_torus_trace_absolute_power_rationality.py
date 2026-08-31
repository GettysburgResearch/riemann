from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = ROOT / "research" / "l-families" / "atlas" / "generalized"
MODULE_PATH = PACKET_ROOT / "dense_torus_trace_absolute_power_rationality.py"
SPEC = importlib.util.spec_from_file_location(
    "dense_torus_trace_absolute_power_rationality", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load dense-torus trace packet")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def reject_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError(f"unexpected float {value!r}")
    if isinstance(value, dict):
        for child in value.values():
            reject_float(child)
    elif isinstance(value, (list, tuple)):
        for child in value:
            reject_float(child)


class DenseTorusTraceAbsolutePowerRationalityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_multinomial_controls(self) -> None:
        self.assertEqual(
            list(subject.weak_compositions(2, 2)), [(0, 2), (1, 1), (2, 0)]
        )
        self.assertEqual(list(subject.positive_compositions(3, 2)), [(1, 2), (2, 1)])
        self.assertEqual(subject.multinomial(4, (1, 2, 1)), 12)
        self.assertEqual(
            subject.exact_trace_coefficients(2, 2),
            {
                (-2, 2): 1,
                (-1, 1): 4,
                (0, 0): 6,
                (1, -1): 4,
                (2, -2): 1,
            },
        )
        rank_three = subject.exact_trace_coefficients(3, 1)
        self.assertEqual(rank_three[(0, 0, 0)], 3)
        self.assertEqual(len(rank_three), 7)
        self.assertEqual(sum(rank_three.values()), 9)

    def test_support_equals_independent_cube_enumeration(self) -> None:
        for n in range(2, 5):
            for m in range(4):
                coefficients = subject.exact_trace_coefficients(n, m)
                cube_support = {
                    exponent
                    for exponent in itertools.product(range(-m, m + 1), repeat=n)
                    if sum(exponent) == 0
                    and sum(value for value in exponent if value > 0) <= m
                }
                self.assertEqual(set(coefficients), cube_support)
                self.assertEqual(subject.root_lattice_ball(n, m), cube_support)
                self.assertEqual(subject.root_lattice_ball_count(n, m), len(cube_support))
                self.assertEqual(
                    subject.root_lattice_compact_count(n, m), len(cube_support)
                )
                self.assertTrue(all(value > 0 for value in coefficients.values()))
                self.assertEqual(sum(coefficients.values()), n ** (2 * m))

    def test_rank_two_and_rank_three_recoveries(self) -> None:
        for m in range(subject.MAX_ALLOWED_M + 1):
            self.assertEqual(subject.root_lattice_ball_count(2, m), 2 * m + 1)
            self.assertEqual(
                subject.root_lattice_ball_count(3, m), 1 + 3 * m * (m + 1)
            )
            self.assertEqual(subject.exact_support_row(2, m)["support_count"], 2 * m + 1)
        for s in range(1, subject.MAX_ALLOWED_M + 1):
            self.assertEqual(subject.root_lattice_shell_count(2, s), 2)
            self.assertEqual(subject.root_lattice_shell_count(3, s), 6 * s)
        for n in range(2, subject.MAX_ALLOWED_N + 1):
            self.assertEqual(subject.root_lattice_ball_count(n, 1), 1 + n * (n - 1))

    def test_held_out_ranks_outside_default_fixture(self) -> None:
        self.assertLess(subject.DEFAULT_MAX_N, 6)
        for n, m, expected in ((6, 4, 4251), (7, 3, 3067)):
            row = subject.exact_support_row(n, m)
            self.assertEqual(row["support_count"], expected)
            self.assertEqual(row["dense_orbit_minimal_order"], expected)
            self.assertEqual(row["full_torus_character_count"], expected)
            self.assertEqual(row["determinant_one_character_count"], expected)
            self.assertTrue(row["determinant_one_no_collisions"])

    def test_determinant_one_quotient_and_trace_zero_certificates(self) -> None:
        self.assertEqual(
            subject.determinant_one_character((2, -1, -1)),
            subject.determinant_one_character((3, 0, 0)),
        )
        for n in range(2, subject.MAX_ALLOWED_N + 1):
            certificate = subject.trace_zero_curve_certificate(n)
            exponents = certificate["q_eta_exponents_mod_2n"]
            self.assertEqual(len(set(exponents)), n)
            self.assertEqual(sum(exponents) % (2 * n), 0)
            self.assertEqual(certificate["geometric_ratio_order"], n)
            self.assertTrue(certificate["determinant_equals_one"])
            self.assertTrue(certificate["trace_derivative_nonzero"])
            self.assertNotEqual(exponents[0], exponents[1])
            self.assertEqual(
                (exponents[1] - exponents[0]) % (2 * n), 2
            )
            support = subject.root_lattice_ball(n, 2)
            quotient = {subject.determinant_one_character(row) for row in support}
            self.assertEqual(len(support), len(quotient))

    def test_sources_are_exact_git_objects_and_blob_contents(self) -> None:
        lock = subject.verify_sources_manifest()
        self.assertEqual(lock["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertTrue(lock["git_blob_contents_compared_to_working_tree"])
        self.assertEqual(
            lock["manifest_sha256_lf_normalized"], subject.EXPECTED_SOURCES_SHA256_LF
        )
        self.assertEqual(len(lock["verified_sources"]), 4)
        self.assertEqual(
            {row["path"]: row["git_blob"] for row in lock["verified_sources"]},
            subject.EXPECTED_SOURCE_OBJECTS,
        )
        for row in lock["verified_sources"]:
            content = subject._normalized_bytes(subject._git_blob_bytes(row["git_blob"]))
            self.assertEqual(
                hashlib.sha256(content).hexdigest(), row["file_sha256_lf_normalized"]
            )
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(
                subject.EXPECTED_BASE_COMMIT, "definitely_missing_dense_torus_source"
            )
        with self.assertRaisesRegex(RuntimeError, "git blob read failed"):
            subject._git_blob_bytes("0" * 40)

    def test_analytic_obligations_and_scope_guards(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.DENSE_TORUS_FINITE_CHARACTER",
                "GLO764.DENSE_UNITARY_TRACE_ABSOLUTE_GATE",
                "GLO764.TRACE_EVEN_POWER_ROOT_LATTICE_SUPPORT",
            },
        )
        obligations = self.fixture["analytic_proof_obligations"]
        self.assertIn("injective", obligations["character_evaluation"])
        self.assertIn("|t|^lambda", obligations["complex_cusp"])
        self.assertTrue(obligations["finite_replay_is_not_universal_proof"])
        for field, value in self.fixture["scope_firewall"].items():
            self.assertTrue(value, field)
        rows = self.fixture["exact_polynomial_controls"]["rows"]
        for row in rows:
            if row["m"] == 0:
                self.assertTrue(row["m_zero_is_polynomial_control_only"])
                self.assertFalse(row["analytic_positive_exponent_chamber"])
                self.assertIsNone(row["dense_orbit_minimal_order"])
            else:
                self.assertTrue(row["analytic_positive_exponent_chamber"])
                self.assertEqual(row["dense_orbit_minimal_order"], row["support_count"])

    def test_resource_caps_input_refusals_and_no_floats(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(
            resources["declared_work_units"],
            resources["expansion_pair_units"] + resources["root_vector_units"],
        )
        self.assertLess(
            resources["declared_work_units"], resources["work_unit_cap_exclusive"]
        )
        self.assertEqual(resources["float_operations"], 0)
        self.assertFalse(resources["external_symbolic_engine"])
        reject_float(self.fixture)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=resources["declared_work_units"])
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.exact_trace_coefficients(2, 1, resource_cap=4)
        with self.assertRaisesRegex(ValueError, "n"):
            subject.build_fixture(max_n=subject.MAX_ALLOWED_N + 1)
        with self.assertRaisesRegex(ValueError, "m"):
            subject.build_fixture(max_m=subject.MAX_ALLOWED_M + 1)
        with self.assertRaisesRegex(ValueError, "at least 2"):
            subject.exact_trace_coefficients(1, 2)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_n=True)
        with self.assertRaisesRegex(ValueError, "sum"):
            subject.multinomial(3, (1, 1))
        with self.assertRaisesRegex(TypeError, "integers"):
            subject.determinant_one_character((True, 0))
        minimal = subject.build_fixture(max_n=2, max_m=0)
        self.assertEqual(minimal["exact_polynomial_controls"]["row_count"], 1)

    def test_note_integrity_and_proof_hypotheses(self) -> None:
        raw = subject.NOTE_PATH.read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        self.assertNotIn(b"\r", raw)
        note = raw.decode("utf-8")
        self.assertEqual(note.count(r"\("), note.count(r"\)"))
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        self.assertGreaterEqual(len(re.findall(r"\\\[(.*?)\\\]", note, re.DOTALL)), 25)
        self.assertNotIn("(ngeq2)", note)
        for line in note.splitlines():
            self.assertEqual(line, line.rstrip(" \t"))
        for required in (
            r"\operatorname{Re}\lambda>0",
            "dense cyclic subgroup",
            "simple zero",
            "determinant-one collision",
            "no scalar cancellation",
            r"d_2(m)=2m+1",
            "not a priority claim",
            "Rank one",
        ):
            self.assertIn(required, note)

    def test_stored_fixture_and_producer_hashes(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        controls = stored["exact_polynomial_controls"]
        self.assertEqual(controls["rows_sha256"], subject._canonical_sha256(controls["rows"]))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (subject.NOTE_PATH, "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            self.assertEqual(producer[field], subject._lf_sha256(path))
        self.assertEqual(
            controls["degree_table"],
            [
                {"n": 2, "m_values": [0, 1, 2, 3, 4], "counts": [1, 3, 5, 7, 9]},
                {"n": 3, "m_values": [0, 1, 2, 3, 4], "counts": [1, 7, 19, 37, 61]},
                {"n": 4, "m_values": [0, 1, 2, 3, 4], "counts": [1, 13, 55, 147, 309]},
                {"n": 5, "m_values": [0, 1, 2, 3, 4], "counts": [1, 21, 131, 471, 1251]},
            ],
        )


if __name__ == "__main__":
    unittest.main()
