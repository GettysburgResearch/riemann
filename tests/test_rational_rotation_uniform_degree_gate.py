from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET_ROOT = ROOT / "research" / "l-families" / "atlas" / "generalized"
MODULE_PATH = PACKET_ROOT / "rational_rotation_uniform_degree_gate.py"
SPEC = importlib.util.spec_from_file_location(
    "rational_rotation_uniform_degree_gate", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load rational-rotation uniform-degree gate")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def reject_float(value: object) -> None:
    if isinstance(value, float):
        raise TypeError(f"unexpected float {value!r}")
    if isinstance(value, dict):
        for child in value.values():
            reject_float(child)
    elif isinstance(value, list):
        for child in value:
            reject_float(child)


class RationalRotationUniformDegreeGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_first_absolute_power_has_full_spectrum(self) -> None:
        for b in range(2, 61):
            spectrum = subject.first_absolute_power_spectrum(b)
            self.assertEqual(spectrum["nonzero_mode_count"], b)
            self.assertEqual(spectrum["minimal_recurrence_order"], b)
            for k in range(b):
                row = subject.first_absolute_power_mode_certificate(b, k)
                self.assertTrue(row["dft_mode_nonzero"])
                self.assertTrue(row["both_geometric_denominators_nonzero"])
                self.assertTrue(row["difference_numerator_nonzero"])
                self.assertEqual(
                    row["forward_geometric_ratio_eta_exponent_mod_2b"] % 2,
                    1,
                )
                self.assertEqual(
                    row["backward_geometric_ratio_eta_exponent_mod_2b"] % 2,
                    1,
                )

    def test_integer_power_uniform_bound_and_sharpness(self) -> None:
        for b in range(2, 19):
            for a in range(1, b):
                if math.gcd(a, b) != 1:
                    continue
                for k in range(1, 15):
                    spectrum = subject.PARENT.integer_power_spectrum(a, b, k)
                    order = spectrum["minimal_recurrence_order"]
                    self.assertLessEqual(order, k + 1)
                    if b > k:
                        self.assertEqual(order, k + 1)
        census = self.fixture["integer_polynomial_controls"]
        self.assertEqual(census["maximum_order_minus_k_plus_1"], 0)
        self.assertGreater(census["collision_free_sharp_row_count"], 0)

    def test_exact_alias_controls(self) -> None:
        self.assertEqual(
            subject.alias_support({-2: 1, 0: -2, 2: 1}, 7),
            {0: -2, 2: 1, 5: 1},
        )
        self.assertEqual(subject.alias_support({0: 1, 3: -1}, 3), {})
        self.assertEqual(
            subject.scaled_sine_power_modes(3),
            {3: 1, 1: -3, -1: 3, -3: -1},
        )
        self.assertEqual(
            subject.alias_support(subject.scaled_sine_power_modes(3), 11),
            {1: -3, 3: 1, 8: -1, 10: 3},
        )

    def test_sources_manifest_and_exact_git_objects(self) -> None:
        source = subject.verify_sources_manifest()
        self.assertEqual(source["base_commit"], subject.EXPECTED_BASE_COMMIT)
        self.assertEqual(
            source["file_sha256_lf_normalized"],
            subject.EXPECTED_SOURCES_SHA256_LF,
        )
        self.assertEqual(len(source["verified_sources"]), 6)
        self.assertEqual(
            {row["path"]: row["git_blob"] for row in source["verified_sources"]},
            subject.EXPECTED_SOURCE_OBJECTS,
        )
        references = source["external_references"]
        self.assertEqual(len(references), 2)
        self.assertEqual(references[0]["authors"], "Oliver Knill and John Lesieutre")
        self.assertIn("NIST", references[1]["authors"])
        with self.assertRaisesRegex(RuntimeError, "git object lookup failed"):
            subject._git_blob_at(
                subject.EXPECTED_BASE_COMMIT,
                "research/l-families/atlas/generalized/definitely_missing",
            )

    def test_claims_analytic_obligations_and_firewalls(self) -> None:
        self.assertEqual(
            set(self.fixture["claims"]),
            {
                "GLO764.PERIODIC_DFT_MINIMAL_ORDER",
                "GLO764.SAMPLED_MODE_PERSISTENCE",
                "GLO764.ABSOLUTE_UNIFORM_DEGREE_GATE",
                "GLO764.FIXED_BRANCH_UNIFORM_DEGREE_GATE",
                "GLO764.ABSOLUTE_FIRST_POWER_FULL_SPECTRUM",
            },
        )
        obligations = self.fixture["analytic_proof_obligations"]
        self.assertIn("Riemann sum", obligations["fixed_mode_grid_limit"])
        self.assertTrue(obligations["finite_replay_is_not_universal_proof"])
        boundary = self.fixture["uniform_state_space_boundary"]
        self.assertIn("Sym^k", boundary["integer_signed_parent"])
        self.assertIn("no dimension bound", boundary["noninteger_rational_orbits"])
        firewall = self.fixture["scope_firewall"]
        for field in (
            "one_unramified_determinant_one_local_recurrence",
            "tempered_rational_rotations_only",
            "fixed_exponent_with_strictly_positive_real_part",
            "lambda_zero_convention_family_excluded",
            "finite_dimensional_constant_state_space_obstruction_only",
            "no_quantitative_degree_growth_rate",
            "no_prime_indexed_global_family_constructed",
            "no_ramified_factors_completion_or_functional_equation",
            "no_automorphy_motive_or_infinite_dimensional_no_go",
            "no_RH_GRH_or_zero_distribution_consequence",
            "external_novelty_unreviewed",
        ):
            self.assertTrue(firewall[field])

    def test_resource_refusals_and_no_floats(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["arithmetic_class"], "EXACT_INTEGER_ROOT_EXPONENT")
        self.assertEqual(resources["float_operations"], 0)
        self.assertFalse(resources["external_symbolic_engine"])
        self.assertLess(
            resources["declared_work_units"], resources["work_unit_cap_exclusive"]
        )
        reject_float(self.fixture)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=1)
        with self.assertRaisesRegex(ValueError, "max_b"):
            subject.build_fixture(max_b=33)
        with self.assertRaisesRegex(ValueError, "max_k"):
            subject.build_fixture(max_k=25)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(max_b=True)
        with self.assertRaisesRegex(ValueError, "smaller"):
            subject.first_absolute_power_mode_certificate(5, 5)
        with self.assertRaisesRegex(TypeError, "frequencies"):
            subject.alias_support({True: 1}, 3)

    def test_note_integrity_and_proof_gates(self) -> None:
        raw = (PACKET_ROOT / "RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md").read_bytes()
        self.assertFalse([byte for byte in raw if byte < 32 and byte not in (9, 10)])
        self.assertNotIn(b"\r", raw)
        note = raw.decode("utf-8")
        for command in (
            r"\operatorname",
            r"\mathbb",
            r"\widetilde",
            r"\Longleftrightarrow",
        ):
            self.assertIn(command, note)
        self.assertFalse(
            [
                line_number
                for line_number, line in enumerate(note.splitlines(), start=1)
                if line.rstrip(" \t") != line
            ]
        )
        self.assertEqual(note.count(r"\("), note.count(r"\)"))
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertGreaterEqual(len(displays), 20)
        for required in (
            "reduced local degrees",
            "Riemann sum",
            "arbitrarily many modes",
            "sharp supremum",
            "full-spectrum hostile witness",
            "finite-dimensional constant-state-space obstruction",
            "not a priority claim",
        ):
            self.assertIn(required, note)

    def test_stored_fixture_payload_and_producer_hashes(self) -> None:
        stored_path = PACKET_ROOT / "rational_rotation_uniform_degree_gate.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                PACKET_ROOT / "RATIONAL_ROTATION_UNIFORM_DEGREE_GATE.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())


if __name__ == "__main__":
    unittest.main()
