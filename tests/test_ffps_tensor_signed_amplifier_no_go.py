"""Focused exact tests for the FFPS signed tensor-amplifier no-go."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_tensor_signed_amplifier_no_go.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "ffps_tensor_signed_amplifier_no_go", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load FFPS signed-amplifier producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FFPSTensorSignedAmplifierNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical_and_payload_locked(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_local_and_tensor_inverse_are_exact(self) -> None:
        for panel in ((3,), (5,), (7,), (3, 5), (5, 7), (3, 5, 7)):
            guard = MODULE.ResourceGuard()
            gram = MODULE.tensor_gram(panel, guard)
            inverse = MODULE.tensor_inverse(panel, guard)
            product = MODULE.matrix_multiply(gram, inverse, guard)
            expected = tuple(
                tuple(Fraction(row == column) for column in range(len(gram)))
                for row in range(len(gram))
            )
            self.assertEqual(product, expected)

    def test_exact_complex_pythagorean_identity(self) -> None:
        vectors = (
            tuple(MODULE.gaussian(value) for value in (2, 0, 1, 0, 2, 1)),
            (
                MODULE.gaussian(1, 1),
                MODULE.gaussian(1, -1),
                MODULE.gaussian(1),
                MODULE.gaussian(1),
                MODULE.gaussian(1),
                MODULE.gaussian(1),
            ),
            (
                MODULE.gaussian(Fraction(3, 2), Fraction(1, 3)),
                MODULE.gaussian(Fraction(1, 2), Fraction(-1, 3)),
                MODULE.gaussian(1),
                MODULE.gaussian(1),
                MODULE.gaussian(1),
                MODULE.gaussian(1),
            ),
        )
        for panel in ((5, 7), (3, 5, 7)):
            for alpha in vectors:
                analysis = MODULE.analyze_amplifier(panel, alpha)
                self.assertEqual(
                    analysis.direct_energy,
                    analysis.coherent_baseline + analysis.excess_energy,
                )
                self.assertEqual(analysis.excess_energy, analysis.mode_penalty_sum)
                self.assertGreater(analysis.excess_energy, 0)

    def test_uniform_is_the_unique_exact_complex_extremizer(self) -> None:
        for panel in MODULE.CONTROL_PANELS:
            dimension = MODULE.tensor_dimension(panel)
            uniform = (MODULE.gaussian(1),) * dimension
            analysis = MODULE.analyze_amplifier(panel, uniform)
            self.assertEqual(analysis.direct_energy, MODULE.coherent_baseline(panel))
            self.assertEqual(analysis.excess_energy, 0)
            self.assertTrue(all(value == MODULE.gaussian() for value in analysis.beta))

            perturbation = list(uniform)
            perturbation[0] = MODULE.gaussian(1, Fraction(1, 2))
            perturbation[1] = MODULE.gaussian(1, Fraction(-1, 2))
            moved = MODULE.analyze_amplifier(panel, perturbation)
            self.assertGreater(moved.direct_energy, analysis.direct_energy)

    def test_mode_eigenvalues_multiplicities_and_penalties(self) -> None:
        self.assertEqual(
            self.fixture["theorem"]["mode_multiplicity"],
            "product_(p in A)(m_p-1)",
        )
        expected_57 = {
            (): (1, Fraction(12)),
            (5,): (1, Fraction(20)),
            (7,): (2, Fraction(21)),
            (5, 7): (2, Fraction(35)),
        }
        self.assertEqual(
            {
                tuple(row["active_sum_zero_primes"]): (
                    row["multiplicity"],
                    Fraction(*row["gram_eigenvalue"]),
                )
                for row in self.fixture["mode_spectra"][0]["rows"]
            },
            expected_57,
        )
        expected_357 = {
            (): (1, Fraction(24)),
            (3,): (0, Fraction(36)),
            (5,): (1, Fraction(40)),
            (7,): (2, Fraction(42)),
            (3, 5): (0, Fraction(60)),
            (3, 7): (0, Fraction(63)),
            (5, 7): (2, Fraction(70)),
            (3, 5, 7): (0, Fraction(105)),
        }
        self.assertEqual(
            {
                tuple(row["active_sum_zero_primes"]): (
                    row["multiplicity"],
                    Fraction(*row["gram_eigenvalue"]),
                )
                for row in self.fixture["mode_spectra"][1]["rows"]
            },
            expected_357,
        )

    def test_product_and_cross_prime_entangled_controls_are_distinct(self) -> None:
        controls = {
            row["label"]: row
            for row in self.fixture["exact_gaussian_rational_controls"]
        }
        self.assertTrue(
            controls["uniform_unique_extremizer"]["rank_one_under_2_by_3_flattening"]
        )
        self.assertTrue(controls["complex_product"]["rank_one_under_2_by_3_flattening"])
        for label in (
            "real_nonproduct",
            "complex_nonproduct",
            "fractional_complex_nonproduct",
            "three_prime_complex_nonproduct",
        ):
            self.assertFalse(controls[label]["rank_one_under_2_by_3_flattening"])
            analysis = controls[label]["analysis"]
            self.assertGreater(Fraction(*analysis["positive_excess"]), 0)
            self.assertEqual(
                Fraction(*analysis["direct_dual_energy"]),
                Fraction(*analysis["coherent_baseline"])
                + Fraction(*analysis["positive_excess"]),
            )

    def test_complete_metric_is_not_restricted_gram_inversion(self) -> None:
        # For p=5 and alpha=(2,0), the complete inverse gives 16/15.
        complete = MODULE.analyze_amplifier(
            (5,), (MODULE.gaussian(2), MODULE.gaussian(0))
        ).direct_energy
        # Physical deletion retains the 1x1 Gram [4], hence gives 2^2/4=1.
        restricted = Fraction(2 * 2, 4)
        self.assertEqual(complete, Fraction(16, 15))
        self.assertEqual(restricted, 1)
        self.assertNotEqual(complete, restricted)
        distinction = self.fixture["metric_distinction"]
        self.assertIn("need not equal", distinction["noncommutation"])

    def test_correlated_joint_deletion_can_improve_restricted_metric(self) -> None:
        row = self.fixture["correlated_joint_deletion_counterexample"]
        self.assertEqual(row["primes"], [5, 7])
        self.assertEqual(row["retained_flat_indices"], [0, 2, 3, 4])
        self.assertEqual(
            row["retained_joint_coordinates"], [[0, 0], [0, 2], [1, 0], [1, 1]]
        )
        gram = MODULE.tensor_gram((5, 7))
        retained = tuple(row["retained_flat_indices"])
        restricted = tuple(
            tuple(gram[left][right] for right in retained) for left in retained
        )
        denominator = sum((sum(matrix_row) for matrix_row in restricted), Fraction(0))
        self.assertEqual(denominator, 74)
        weights = tuple(Fraction(*value) for value in row["restricted_optimal_weights"])
        self.assertEqual(weights, (Fraction(45, 37), Fraction(66, 37)) * 2)
        self.assertEqual(sum(weights), 6)
        dual_representative = (MODULE.gaussian(Fraction(3, 37)),) * 4
        self.assertEqual(
            MODULE.matrix_vector(restricted, dual_representative),
            tuple(MODULE.gaussian(value) for value in weights),
        )
        restricted_energy = Fraction(*row["restricted_optimal_dual_energy"])
        self.assertEqual(restricted_energy, Fraction(18, 37))
        self.assertLess(restricted_energy, MODULE.coherent_baseline((5, 7)))

        zero_extended = tuple(
            MODULE.gaussian(weights[retained.index(index)])
            if index in retained
            else MODULE.gaussian()
            for index in range(6)
        )
        complete_energy = MODULE.analyze_amplifier((5, 7), zero_extended).direct_energy
        self.assertEqual(complete_energy, Fraction(8181, 13690))
        self.assertGreater(complete_energy, MODULE.coherent_baseline((5, 7)))
        self.assertFalse(
            self.fixture["scope"][
                "arbitrary_correlated_restricted_gram_deletion_ruled_out"
            ]
        )

    def test_corrected_source_provenance_and_lf_locks(self) -> None:
        frontier = self.fixture["source_frontier"]
        self.assertEqual(frontier["pr"], 751)
        dependency = frontier["dependency_snapshot"]
        self.assertEqual(dependency["commit"], MODULE.DEPENDENCY_SNAPSHOT_COMMIT_751)
        self.assertEqual(dependency["git_blob_ids"], MODULE.DEPENDENCY_SOURCE_BLOBS_751)
        live = frontier["live_audit"]
        self.assertEqual(live["head_commit"], MODULE.LIVE_AUDITED_HEAD_751)
        self.assertEqual(live["git_blob_ids"], MODULE.LIVE_SOURCE_BLOBS_751)
        self.assertEqual(live["gate_status"], MODULE.LIVE_GATE_STATUS_751)
        self.assertEqual(
            MODULE.DEPENDENCY_SOURCE_BLOBS_751["L-106024"],
            MODULE.LIVE_SOURCE_BLOBS_751["L-106024"],
        )
        self.assertIn("WITHDRAWN", live["gate_status"]["BTMS106121"])
        self.assertIn("WITHDRAWN", live["gate_status"]["BTDS106121"])
        self.assertIn("T-106140", live["gate_status"]["preferred_live_repair"])
        manifest = {row["id"]: row for row in self.fixture["source_manifest"]}
        self.assertEqual(set(manifest), set(MODULE.SOURCE_LOCKS))
        for name, lock in MODULE.SOURCE_LOCKS.items():
            path = lock["path"]
            self.assertIsInstance(path, Path)
            raw = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            digest = hashlib.sha256(raw).hexdigest()
            self.assertEqual(digest, lock["sha256_lf"])
            self.assertEqual(manifest[name]["sha256_lf_normalized"], digest)

    def test_dependencies_are_read_only_after_symbolic_theorem_closes(self) -> None:
        events: list[str] = []
        original_symbolic = MODULE._build_symbolic_certificate
        original_read = MODULE._read_locked_sources

        def observed_symbolic(guard: object) -> object:
            result = original_symbolic(guard)
            events.append("symbolic_closed")
            return result

        def observed_read(guard: object) -> object:
            events.append("source_read")
            return original_read(guard)

        with (
            mock.patch.object(
                MODULE, "_build_symbolic_certificate", side_effect=observed_symbolic
            ),
            mock.patch.object(
                MODULE, "_read_locked_sources", side_effect=observed_read
            ),
        ):
            MODULE.build_fixture()
        self.assertLess(events.index("symbolic_closed"), events.index("source_read"))

    def test_packet_manifest_and_resource_caps(self) -> None:
        manifest = {row["path"]: row for row in self.fixture["packet_manifest"]}
        for path in (MODULE.NOTE_PATH, MODULE.SCRIPT_PATH, MODULE.TEST_PATH):
            relative = MODULE._relative(path)
            self.assertIn(relative, manifest)
            self.assertEqual(
                manifest[relative]["sha256_lf_normalized"], MODULE._lf_sha256(path)
            )
        resources = self.fixture["resource_contract"]
        self.assertLessEqual(
            resources["actual_matrix_cells"], resources["maximum_matrix_cells"]
        )
        self.assertLessEqual(
            resources["actual_exact_operations"], resources["maximum_exact_operations"]
        )
        self.assertEqual(resources["actual_source_files"], len(MODULE.SOURCE_LOCKS))
        self.assertLessEqual(
            resources["actual_source_bytes"], resources["maximum_source_bytes"]
        )
        self.assertEqual(resources["characters_enumerated"], 0)
        self.assertEqual(resources["finite_fields_enumerated"], 0)

    def test_fail_closed_domains_caps_and_source_locks(self) -> None:
        for panel in ((), (2,), (9,), (5, 5), (37,), (11, 13)):
            with self.assertRaises(ValueError):
                MODULE.tensor_gram(panel)
        with (
            mock.patch.object(
                MODULE,
                "_is_prime",
                side_effect=AssertionError(
                    "primality ran before the declared prime cap"
                ),
            ),
            self.assertRaises(ValueError),
        ):
            MODULE.tensor_gram((10**100 + 39,))
        with self.assertRaises(ValueError):
            MODULE.analyze_amplifier((5,), (MODULE.gaussian(1),))
        with self.assertRaises(ValueError):
            MODULE.analyze_amplifier((5,), (MODULE.gaussian(2), MODULE.gaussian(1)))
        with self.assertRaises(ValueError):
            MODULE.mode_eigenvalue((5, 7), (3,))
        with self.assertRaises(ValueError):
            MODULE.is_rank_one_two_by_three((MODULE.gaussian(1),))

        resource = MODULE.ResourceGuard()
        with self.assertRaises(RuntimeError):
            resource.operation(MODULE.MAX_EXACT_OPERATIONS + 1)
        with self.assertRaises(RuntimeError):
            resource.matrix(1, MODULE.MAX_MATRIX_CELLS + 1)
        with self.assertRaises(RuntimeError):
            resource.source(MODULE.MAX_SOURCE_BYTES + 1)
        for invalid in (-1, True, Fraction(1, 2)):
            with self.assertRaises(ValueError):
                MODULE.ResourceGuard().matrix(invalid, 1)
            with self.assertRaises(ValueError):
                MODULE.ResourceGuard().source(invalid)
        with self.assertRaises(RuntimeError):
            MODULE._check_wall(0.0, MODULE.MAX_WALL_SECONDS + Fraction(1, 10))

        tampered = {name: dict(lock) for name, lock in MODULE.SOURCE_LOCKS.items()}
        tampered["principal_json"]["sha256_lf"] = "0" * 64
        with (
            mock.patch.object(MODULE, "SOURCE_LOCKS", tampered),
            self.assertRaises(RuntimeError),
        ):
            MODULE._read_locked_sources(MODULE.ResourceGuard())

    def test_optimized_python_cannot_remove_guards(self) -> None:
        script = MODULE.SCRIPT_PATH.read_text(encoding="utf-8")
        executable_asserts = [
            line for line in script.splitlines() if line.lstrip().startswith("assert ")
        ]
        self.assertEqual(executable_asserts, [])
        scope = self.fixture["scope"]
        self.assertFalse(scope["varying_conductor_moment_proved"])
        self.assertFalse(scope["principal_member_individualized"])
        self.assertFalse(scope["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
