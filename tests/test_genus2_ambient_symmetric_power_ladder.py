"""Focused exact tests for the marked ambient symmetric-power ladder."""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_ambient_symmetric_power_ladder.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_ambient_symmetric_power_ladder", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load ambient symmetric-power ladder producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def expression_to_polynomial(
    expression: list[dict[str, int]],
) -> dict[tuple[int, ...], int]:
    return {
        (
            row["L_power"],
            row["Delta_power"],
            row["f_(8,2)_power"],
            row["g_(10,2)_power"],
        ): row["coefficient"]
        for row in expression
    }


class Genus2AmbientSymmetricPowerLadderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        cls.rows = {row["r"]: row for row in cls.fixture["exact_proof"]["ladder"]}

    def test_fixture_is_canonical_and_payload_locked(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_all_five_ambient_formulas(self) -> None:
        self.assertEqual(
            self.fixture["theorem"]["formulas"],
            {
                "r=2": "-2*q",
                "r=4": "-3*q",
                "r=6": "1-3*q-q*Theta_(8,2)(q)",
                "r=8": "1-4*q-q*Theta_(10,2)(q)",
                "r=10": "2-4*q-2*q*Theta_Delta(q)",
            },
        )
        for r in MODULE.EVEN_RANKS:
            polynomial = expression_to_polynomial(self.rows[r]["ambient_expression"])
            self.assertEqual(
                MODULE.polynomial_channels(polynomial), MODULE.AMBIENT_COEFFICIENTS[r]
            )
            self.assertEqual(
                self.rows[r]["ambient_formula"], MODULE.FORMULAS["ambient"][r]
            )

    def test_boundary_is_rebuilt_row_by_row(self) -> None:
        for r in MODULE.EVEN_RANKS:
            guard = MODULE.ResourceGuard()
            boundary, rows = MODULE._boundary_for_rank(r, guard)
            self.assertEqual(
                MODULE.polynomial_channels(boundary), MODULE.BOUNDARY_COEFFICIENTS[r]
            )
            self.assertEqual(rows, self.rows[r]["branch_rows"])
            self.assertGreater(guard.exact_operations, 0)

    def test_branch_dimensions_and_odd_vanishing(self) -> None:
        expected_dimensions = {2: 10, 4: 35, 6: 84, 8: 165, 10: 286}
        for r, row in self.rows.items():
            self.assertEqual(row["symmetric_power_dimension"], expected_dimensions[r])
            self.assertEqual(row["branch_dimension_sum"], expected_dimensions[r])
            self.assertEqual(len(row["branch_rows"]), r + 1)
            for branch in row["branch_rows"]:
                self.assertEqual(
                    branch["vanishes_by_unmarked_central_involution"],
                    branch["i"] % 2 == 1,
                )
                if branch["i"] % 2:
                    self.assertEqual(branch["contribution"], [])
                else:
                    self.assertNotEqual(branch["contribution"], [])

    def test_elliptic_euler_inputs_and_cusp_dimensions(self) -> None:
        guard = MODULE.ResourceGuard()
        self.assertEqual(
            MODULE.polynomial_channels(MODULE.a1_euler(0, guard)), {"L": 1}
        )
        self.assertEqual(
            MODULE.polynomial_channels(MODULE.y0_euler(0, guard)),
            {"1": -1, "L": 1},
        )
        for degree in (1, 3, 5, 7, 9):
            self.assertEqual(MODULE.a1_euler(degree, guard), {})
            self.assertEqual(MODULE.y0_euler(degree, guard), {})
        self.assertEqual(
            MODULE.polynomial_channels(MODULE.level_one_cusp(12, guard)),
            {"Delta": 1},
        )
        self.assertEqual(
            MODULE.polynomial_channels(MODULE.level_two_cusp(8, guard)),
            {"f_(8,2)": 1},
        )
        self.assertEqual(
            MODULE.polynomial_channels(MODULE.level_two_cusp(10, guard)),
            {"g_(10,2)": 1},
        )
        self.assertEqual(
            MODULE.polynomial_channels(MODULE.level_two_cusp(12, guard)),
            {"Delta": 2},
        )

    def test_exact_channel_cancellations_and_shifts(self) -> None:
        expected_cancellations = {
            2: ["1"],
            4: ["1"],
            6: [],
            8: ["f_(8,2)"],
            10: ["Delta", "f_(8,2)", "g_(10,2)"],
        }
        for r, expected in expected_cancellations.items():
            self.assertEqual(
                self.rows[r]["channel_balance"]["exactly_canceled_channels"],
                expected,
            )
        shifts = {
            row["r"]: row["statement"]
            for row in self.fixture["exact_proof"]["channel_shift_ladder"]
        }
        self.assertIn("-L*f_(8,2)", shifts[6])
        self.assertIn("-L*g_(10,2)", shifts[8])
        self.assertIn("-2*L*Delta", shifts[10])

    def test_exact_q_controls(self) -> None:
        expected = {
            3: {"2": -6, "4": -9, "6": -44, "8": 457, "10": -1_522},
            5: {"2": -10, "4": -15, "6": 1_036, "8": -4_369, "10": -48_318},
            7: {"2": -14, "4": -21, "6": -7_132, "8": 6_637, "10": 234_390},
            9: {"2": -18, "4": -27, "6": 38_044, "8": 135_235, "10": 5_234_186},
        }
        controls = {
            row["q"]: row["ambient_traces"]
            for row in self.fixture["exact_proof"]["exact_controls"]
        }
        self.assertEqual(controls, expected)

    def test_committed_ambient_sym10_endpoint_is_independent_control(self) -> None:
        manifest = {row["id"]: row for row in self.fixture["source_manifest"]}
        ambient = manifest["ambient_sym10"]
        self.assertEqual(ambient["commit"], "50cbe644c6fa9cc4e6a7f5f03683883ffea83d49")
        self.assertEqual(
            ambient["git_blob"], "c639b41275264ba2a05c51448da5c1cfdf472264"
        )
        self.assertEqual(self.rows[10]["ambient_formula"], "2-4*L-2*L*Delta")

    def test_sources_are_hash_blob_schema_and_payload_locked(self) -> None:
        manifest = {row["id"]: row for row in self.fixture["source_manifest"]}
        self.assertEqual(set(manifest), set(MODULE.SOURCE_LOCKS))
        for name, lock in MODULE.SOURCE_LOCKS.items():
            path = lock["path"]
            self.assertIsInstance(path, Path)
            raw = path.read_bytes()
            self.assertEqual(MODULE._lf_sha256_bytes(raw), lock["lf_sha256"])
            self.assertEqual(MODULE._git_blob_sha1(raw), lock["git_blob"])
            value = json.loads(MODULE._lf_bytes(raw).decode("utf-8"))
            payload = dict(value)
            claimed = payload.pop("payload_sha256")
            self.assertEqual(claimed, lock["payload_sha256"])
            self.assertEqual(MODULE._canonical_sha256(payload), claimed)
            self.assertEqual(manifest[name]["bytes"], len(raw))

    def test_exact_ladder_closes_before_sources_are_read(self) -> None:
        events: list[str] = []
        original_exact = MODULE._build_exact_ladder
        original_sources = MODULE._read_locked_sources

        def observed_exact(guard: object) -> object:
            result = original_exact(guard)
            events.append("exact_closed")
            return result

        def observed_sources(guard: object, deadline: object) -> object:
            events.append("sources_read")
            return original_sources(guard, deadline)

        with (
            mock.patch.object(
                MODULE, "_build_exact_ladder", side_effect=observed_exact
            ),
            mock.patch.object(
                MODULE, "_read_locked_sources", side_effect=observed_sources
            ),
        ):
            MODULE.build_fixture()
        self.assertLess(events.index("exact_closed"), events.index("sources_read"))

    def test_resource_caps_and_packet_manifest(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertLessEqual(
            resources["actual_exact_operations"],
            resources["maximum_exact_operations"],
        )
        self.assertEqual(resources["actual_source_files"], len(MODULE.SOURCE_LOCKS))
        self.assertLessEqual(
            resources["actual_source_bytes"], resources["maximum_source_bytes_total"]
        )
        self.assertLessEqual(
            OUTPUT_PATH.stat().st_size, resources["maximum_output_bytes"]
        )
        self.assertEqual(resources["operation_counts"]["control_evaluation"], 44)
        for key in (
            "finite_fields_enumerated",
            "curves_enumerated",
            "abelian_surfaces_enumerated",
            "cohomology_groups_enumerated",
            "modular_symbols_enumerated",
        ):
            self.assertEqual(resources[key], 0)

        manifest = {row["path"]: row for row in self.fixture["packet_manifest"]}
        for path in (MODULE.NOTE_PATH, MODULE.SCRIPT_PATH, MODULE.TEST_PATH):
            relative = MODULE._relative(path)
            raw = path.read_bytes()
            self.assertIn(relative, manifest)
            self.assertEqual(manifest[relative]["bytes"], len(raw))
            self.assertEqual(
                manifest[relative]["lf_sha256"], MODULE._lf_sha256_bytes(raw)
            )

    def test_fail_closed_guards_and_sources(self) -> None:
        guard = MODULE.ResourceGuard()
        with self.assertRaises(RuntimeError):
            guard.operation("overflow", MODULE.MAX_EXACT_OPERATIONS + 1)
        with self.assertRaises(RuntimeError):
            MODULE.ResourceGuard().source(MODULE.MAX_SOURCE_BYTES_EACH + 1)
        for invalid in (-1, True, 0.5):
            with self.assertRaises(ValueError):
                MODULE.ResourceGuard().operation("invalid", invalid)
            with self.assertRaises(ValueError):
                MODULE.ResourceGuard().source(invalid)
        with self.assertRaises(ValueError):
            MODULE.level_one_cusp(14, MODULE.ResourceGuard())
        with self.assertRaises(ValueError):
            MODULE.level_two_cusp(2, MODULE.ResourceGuard())
        with self.assertRaises(ValueError):
            MODULE._boundary_for_rank(12, MODULE.ResourceGuard())

        tampered = {name: dict(lock) for name, lock in MODULE.SOURCE_LOCKS.items()}
        tampered["sym8"]["lf_sha256"] = "0" * 64
        with (
            mock.patch.object(MODULE, "SOURCE_LOCKS", tampered),
            self.assertRaises(RuntimeError),
        ):
            MODULE._read_locked_sources(MODULE.ResourceGuard(), MODULE.Deadline())

        expired = MODULE.Deadline(started=0.0)
        with self.assertRaises(RuntimeError):
            expired.check("expired control")

        with tempfile.TemporaryDirectory() as directory:
            oversized = Path(directory) / "oversized.json"
            oversized.write_bytes(b"x" * (MODULE.MAX_OUTPUT_BYTES + 1))
            with self.assertRaises(RuntimeError):
                MODULE._read_output_capped(oversized)

    def test_optimized_python_cannot_remove_guards_or_firewalls(self) -> None:
        script = MODULE.SCRIPT_PATH.read_text(encoding="utf-8")
        executable_asserts = [
            line for line in script.splitlines() if line.lstrip().startswith("assert ")
        ]
        self.assertEqual(executable_asserts, [])
        scope = self.fixture["scope"]
        self.assertTrue(scope["virtual_compact_support_trace"])
        self.assertFalse(scope["individual_cohomology_group_decomposition"])
        self.assertFalse(scope["motivic_isomorphism"])
        self.assertFalse(scope["rh_or_grh_claim"])


if __name__ == "__main__":
    unittest.main()
