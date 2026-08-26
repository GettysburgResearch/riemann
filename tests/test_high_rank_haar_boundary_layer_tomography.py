"""Exact regression tests for SU(2) high-rank boundary-layer tomography."""

from __future__ import annotations

import ast
import importlib.util
import json
import subprocess
import sys
import tempfile
import time
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
    / "high_rank_haar_boundary_layer_tomography.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")
NOTE_PATH = MODULE_PATH.with_name("HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY.md")

SPEC = importlib.util.spec_from_file_location(
    "high_rank_haar_boundary_layer_tomography", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load high-rank Haar tomography producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class HighRankHaarBoundaryLayerTomographyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical_and_payload_locked(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))
        self.assertEqual(
            self.fixture["status"],
            "PROVED_UNIFORM_HAAR_BOUNDARY_LAYER_TOMOGRAPHY",
        )

    def test_normalized_character_series_is_exact(self) -> None:
        guard = MODULE.ResourceGuard()
        self.assertEqual(
            MODULE.normalized_character_series(2, guard),
            (Fraction(1), Fraction(-1, 2), Fraction(1, 24)),
        )
        self.assertEqual(
            MODULE.normalized_character_series(3, guard),
            (Fraction(1), Fraction(-4, 3), Fraction(4, 9)),
        )
        for dimension in range(2, 20):
            series = MODULE.normalized_character_series(dimension, guard)
            self.assertEqual(series[1], Fraction(-(dimension**2 - 1), 6))
            self.assertEqual(
                series[2],
                Fraction(
                    3 * dimension**4 - 10 * dimension**2 + 7,
                    360,
                ),
            )

    def test_tail_constant_certificate_uses_exact_two_ninths_integral(self) -> None:
        theorem = self.fixture["exact_theorems"]["uniform_mesoscopic_tail"]
        self.assertEqual(theorem["integral_y3_over_sqrt_1_minus_y2"], [2, 3])
        self.assertEqual(theorem["integral_y2_arccos_y"], [2, 9])
        self.assertEqual(
            theorem["tail_constant"],
            {"pi_power": -2, "rational": [16, 9]},
        )
        self.assertIn("both x and N/x", theorem["theorem"])

    def test_uniform_statement_and_exact_tail_coordinate_are_explicit(self) -> None:
        theorem = self.fixture["exact_theorems"]["finite_N_tail_coordinate"]
        self.assertIn("arcsin(1/x)", theorem["theta_form"])
        self.assertIn("4/(pi*x^3)", theorem["unit_interval_form"])
        self.assertEqual(theorem["hard_cap"], "zero for x>=N")
        note = NOTE_PATH.read_text(encoding="utf-8")
        self.assertIn("\\sup_{A\\le x\\le N/A}", note)
        self.assertIn("\\lim_{A\\to\\infty}", note)

    def test_crossover_matches_both_edge_constants(self) -> None:
        theorem = self.fixture["exact_theorems"]["ceiling_crossover"]
        self.assertIn("integral_0^(1/lambda)", theorem["function"])
        self.assertEqual(
            theorem["small_lambda"]["constant"],
            {"pi_power": -2, "rational": [16, 9]},
        )
        self.assertEqual(
            theorem["near_ceiling"]["constant"],
            {
                "pi_power": -1,
                "radical": "sqrt(6)",
                "rational": [8, 1],
            },
        )
        self.assertIn("(1-lambda)^(3/2)", theorem["near_ceiling"]["statement"])

    def test_finite_rank_ceiling_coefficient_has_correct_quadratic_drop(self) -> None:
        theorem = self.fixture["exact_theorems"]["finite_N_ceiling"]
        controls = {row["N"]: row for row in theorem["controls"]}
        self.assertEqual(controls[2]["ceiling_quadratic_drop"], [1, 2])
        self.assertEqual(controls[3]["ceiling_quadratic_drop"], [4, 3])
        self.assertEqual(controls[4]["ceiling_quadratic_drop"], [5, 2])
        self.assertEqual(
            controls[2]["ceiling_probability_coefficient"]["N_squared_minus_one"], 3
        )
        self.assertIn("(N^2-1)^(3/2)", theorem["statement"])

    def test_supercritical_truncated_and_winsorized_constants(self) -> None:
        rows = {
            row["p"]: row
            for row in self.fixture["exact_theorems"]["truncated_moments"][
                "supercritical_rows"
            ]
        }
        self.assertEqual(
            rows[4]["hard_truncated_coefficient"],
            {"pi_power": -2, "rational": [16, 3]},
        )
        self.assertEqual(
            rows[4]["winsorized_coefficient"],
            {"pi_power": -2, "rational": [64, 9]},
        )
        self.assertEqual(
            rows[6]["hard_truncated_coefficient"],
            {"pi_power": -2, "rational": [16, 9]},
        )
        for row in rows.values():
            hard = Fraction(*row["hard_truncated_coefficient"]["rational"])
            winsor = Fraction(*row["winsorized_coefficient"]["rational"])
            tail = Fraction(*row["capped_tail_difference"]["rational"])
            self.assertEqual(hard + tail, winsor)

    def test_critical_cubic_log_and_scale_tomography_constants(self) -> None:
        critical = self.fixture["exact_theorems"]["truncated_moments"]["critical"]
        self.assertEqual(critical["integral_0_pi_sin_cubed"], [4, 3])
        self.assertEqual(
            critical["period_mean"],
            {"pi_power": -1, "rational": [4, 3]},
        )
        self.assertEqual(
            critical["full_log_coefficient"],
            {"pi_power": -2, "rational": [16, 3]},
        )
        self.assertIn("fraction 1-beta", critical["scale_tomography"])

    def test_endpoint_tomography_separates_three_moment_regimes(self) -> None:
        theorem = self.fixture["exact_theorems"]["endpoint_tomography"]
        self.assertIn("N^(3-p)", theorem["fixed_scaled_window"])
        self.assertIn("integral_0^a", theorem["profile"])
        self.assertIn("infinity", theorem["supercritical_total"])
        self.assertEqual(
            theorem["critical_fraction"],
            "1-beta in the window D<=N^(-beta)",
        )
        transition = theorem["phase_transition"]
        self.assertIn("lower order", transition["p_less_than_3"])
        self.assertIn("logarithmic", transition["p_equals_3"])
        self.assertIn("O(1/N)", transition["p_greater_than_3"])

    def test_source_files_are_exactly_hash_and_payload_locked(self) -> None:
        manifest = {
            row["id"]: row for row in self.fixture["source_contract"]["sources"]
        }
        self.assertEqual(set(manifest), set(MODULE.SOURCE_LOCKS))
        for source_id, lock in MODULE.SOURCE_LOCKS.items():
            raw = lock["path"].read_bytes()
            self.assertEqual(MODULE._lf_sha256_bytes(raw), lock["lf_sha256"])
            self.assertEqual(MODULE._git_blob_sha1(raw), lock["git_blob"])
            completed = subprocess.run(
                [
                    "git",
                    "rev-parse",
                    (f"{lock['commit']}:{lock['path'].relative_to(ROOT).as_posix()}"),
                ],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
                timeout=2.0,
            )
            self.assertEqual(completed.stdout.strip(), lock["git_blob"])
            self.assertEqual(manifest[source_id]["git_blob"], lock["git_blob"])
        self.assertEqual(
            MODULE.SOURCE_LOCKS["moment_json"]["payload_sha256"],
            "0eba593b98d1cdb10cd79354ef15b9352291be1c28d85e961ed35fcd17aed088",
        )

    def test_note_contains_proofs_not_scout_language(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "Uniform mesoscopic cubic tail",
            "The full \\(x\\asymp N\\) crossover",
            "An exact finite-\\(N\\) ceiling coefficient",
            "Truncated and Winsorized moments",
            "Endpoint tomography",
            "16\\over9\\pi^2",
            "8\\sqrt6\\over\\pi",
            "1-\\beta",
            "Not proved",
        ):
            self.assertIn(marker, note)

    def test_scope_does_not_promote_compact_results_to_arithmetic(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["compact_group"], "Haar SU(2) only")
        for item in (
            "arithmetic-family equidistribution uniform in rank",
            "finite-field trace estimate",
            "Euler-product or zero-statistic theorem",
            "RH",
            "GRH",
            "external novelty",
        ):
            self.assertIn(item, scope["not_proved"])
        self.assertIn("uniformly", scope["arithmetic_gate"])

    def test_resource_caps_are_small_real_and_fail_closed(self) -> None:
        budget = self.fixture["resource_budget"]
        used = budget["used"]
        limits = budget["limits"]
        self.assertLess(used["exact_operations"], limits["exact_operations"])
        self.assertEqual(used["source_files"], limits["source_files"])
        self.assertLess(used["source_bytes"], limits["source_bytes_total"])
        self.assertLess(used["control_rows"], limits["control_rows"])
        self.assertFalse(budget["heavy_computation"])
        self.assertFalse(budget["numerical_quadrature"])
        self.assertEqual(budget["root_searches"], 0)
        self.assertEqual(budget["random_samples"], 0)

        operations = MODULE.ResourceGuard(exact_operations=MODULE.MAX_EXACT_OPERATIONS)
        with self.assertRaises(RuntimeError):
            operations.operation("overflow")
        sources = MODULE.ResourceGuard(source_files=MODULE.MAX_SOURCE_FILES)
        with self.assertRaises(RuntimeError):
            sources.source(1)
        rows = MODULE.ResourceGuard(control_rows=MODULE.MAX_CONTROL_ROWS)
        with self.assertRaises(RuntimeError):
            rows.row()
        expired = MODULE.Deadline(started=time.monotonic() - 10)
        with self.assertRaises(RuntimeError):
            expired.check("test")

    def test_series_division_rejects_invalid_inputs(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.series_divide((), (), MODULE.ResourceGuard())
        with self.assertRaises(ValueError):
            MODULE.series_divide(
                (Fraction(1),),
                (Fraction(0),),
                MODULE.ResourceGuard(),
            )
        with self.assertRaises(ValueError):
            MODULE.series_divide(
                (Fraction(1), Fraction(2)),
                (Fraction(1),),
                MODULE.ResourceGuard(),
            )
        with self.assertRaises(ValueError):
            MODULE.normalized_character_series(0, MODULE.ResourceGuard())

    def test_no_python_assert_statements_and_optimized_replay(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn(
            "PASS_HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY",
            completed.stdout,
        )

    def test_check_mode_is_read_only_and_detects_drift(self) -> None:
        before = OUTPUT_PATH.read_bytes()
        completed = subprocess.run(
            [sys.executable, str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn(
            "PASS_HIGH_RANK_HAAR_BOUNDARY_LAYER_TOMOGRAPHY",
            completed.stdout,
        )
        self.assertEqual(before, OUTPUT_PATH.read_bytes())

        with tempfile.TemporaryDirectory() as directory:
            drifted = Path(directory) / "fixture.json"
            drifted.write_text("{}\n", encoding="utf-8")
            with mock.patch.object(MODULE, "OUTPUT_PATH", drifted):
                original = sys.argv
                try:
                    sys.argv = [str(MODULE_PATH), "--check"]
                    with self.assertRaises(SystemExit):
                        MODULE.main()
                finally:
                    sys.argv = original


if __name__ == "__main__":
    unittest.main()
