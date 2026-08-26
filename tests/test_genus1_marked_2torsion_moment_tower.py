from __future__ import annotations

import importlib.util
import json
import sys
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
    / "genus1_marked_2torsion_moment_tower.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus1_marked_2torsion_moment_tower", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load marked-two-torsion moment producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus1MarkedTwoTorsionMomentTowerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        claimed = self.fixture["payload_sha256"]
        payload = dict(self.fixture)
        payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_source_locks_pin_committed_packets(self) -> None:
        rows = {row["id"]: row for row in self.fixture["source_manifest"]}
        genus1 = rows["genus1_cubic_family_laws"]
        sym8 = rows["genus2_sym8_marked_trace_average"]
        self.assertEqual(genus1["commit"], "955ea1e25160075fb4b498018319c80f7e4db9d5")
        self.assertEqual(
            genus1["payload_sha256"],
            "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df",
        )
        self.assertEqual(sym8["commit"], "dc63f02d0897e10936ef0767a1c8e6f15ac49e06")
        self.assertEqual(
            sym8["payload_sha256"],
            "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae",
        )

        genus1_lock = MODULE.SOURCE_PACKETS["genus1_cubic_family_laws"]
        with (
            mock.patch.dict(genus1_lock, {"json_lf_sha256": "0" * 64}),
            self.assertRaisesRegex(RuntimeError, "JSON source lock failed"),
        ):
            MODULE._load_source_packets()
        with (
            mock.patch.dict(genus1_lock, {"payload_sha256": "0" * 64}),
            self.assertRaisesRegex(ValueError, "unexpected source payload"),
        ):
            MODULE._load_source_packets()

    def test_all_weight_theorem_and_ballot_coefficients(self) -> None:
        theorem = self.fixture["theorem"]
        self.assertEqual(
            theorem["theorem"],
            "J_(2n)/(q*(q-1))=C_n*q^n*(q-1)"
            "-sum_(j=1)^n c(n,j)*q^(n-j)"
            "*(2+Theta_(2j+2,Gamma0(2))(q))",
        )
        self.assertEqual(MODULE.catalan(5), 42)
        self.assertEqual(
            [MODULE.ballot_coefficient(5, index) for index in range(6)],
            [42, 90, 75, 35, 9, 1],
        )
        regressions = theorem["su2_exact_regressions"]
        self.assertEqual(regressions[-1]["half_degree"], 12)
        self.assertEqual(regressions[-1]["verified_polynomial"], "a^24")

    def test_explicit_rows_through_tenth_moment(self) -> None:
        rows = {
            row["half_degree"]: row
            for row in self.fixture["theorem"]["explicit_rows_through_n_5"]
        }
        expected_formulas = {
            0: "J_0=q*(q-1)*(q-1)",
            1: "J_2=q*(q-1)*(q^2-q-2)",
            2: "J_4=q*(q-1)*(2*q^3-2*q^2-6*q-2)",
            3: "J_6=q*(q-1)*(5*q^4-5*q^3-18*q^2-10*q-2-Theta_f(q))",
            4: (
                "J_8=q*(q-1)*(14*q^5-14*q^4-56*q^3-40*q^2-14*q-2"
                "-7*q*Theta_f(q)-Theta_g(q))"
            ),
            5: (
                "J_10=q*(q-1)*(42*q^6-42*q^5-180*q^4-150*q^3-70*q^2"
                "-18*q-2-35*q^2*Theta_f(q)-9*q*Theta_g(q)"
                "-2*Theta_Delta(q))"
            ),
        }
        self.assertEqual(
            {half_degree: row["formula"] for half_degree, row in rows.items()},
            expected_formulas,
        )
        self.assertEqual(
            rows[4]["normalized_tate_polynomial_low_to_high"],
            [-2, -14, -40, -56, -14, 14],
        )

    def test_full_cusp_trace_old_new_multiplicities(self) -> None:
        spaces = {
            row["weight"]: row
            for row in self.fixture["modular_form_certificate"][
                "spaces_through_weight_12"
            ]
        }
        self.assertEqual(
            [spaces[weight]["full_cusp_dimension"] for weight in (4, 6, 8, 10, 12)],
            [0, 0, 1, 1, 2],
        )
        self.assertEqual(spaces[8]["new_dimension"], 1)
        self.assertEqual(spaces[10]["new_dimension"], 1)
        self.assertEqual(spaces[12]["old_dimension"], 2)
        self.assertEqual(spaces[12]["new_dimension"], 0)
        self.assertEqual(spaces[12]["trace"], "2*Theta_Delta(q)")

    def test_weight_ten_form_and_prime_power_trace(self) -> None:
        forms = self.fixture["modular_form_certificate"]
        self.assertEqual(
            forms["g_coefficients_d_0_through_d_9"],
            [0, 1, 16, -156, 256, 870, -2496, -952, 4096, 4653],
        )
        self.assertEqual(
            forms["required_g_coefficients"],
            {"g_3": -156, "g_5": 870, "g_7": -952, "g_9": 4653},
        )
        traces = forms["q_9_prime_power_traces"]
        self.assertEqual(traces["Theta_f(9)"], -4230)
        self.assertEqual(traces["Theta_g(9)"], -15030)
        self.assertEqual(traces["Theta_Delta(9)"], -290790)
        self.assertEqual(traces["Theta_g_identity"], "4653-3^9=-15030")
        self.assertEqual(traces["Theta_(12,Gamma0(2))(9)"], -581580)

    def test_q9_consequences_do_not_enumerate_field(self) -> None:
        row = self.fixture["q_9_consequences"]
        self.assertEqual(row["J_8_over_q_q_minus_1"], 972160)
        self.assertEqual(row["J_8"], 69995520)
        self.assertEqual(row["J_10"], 2328145920)
        self.assertEqual(row["status"], "THEOREM_CONSEQUENCE_NOT_FIELD_ENUMERATION")
        self.assertFalse(self.fixture["resource_contract"]["q_9_field_enumerated"])

    def test_held_out_prime_enumerations(self) -> None:
        rows = self.fixture["held_out_finite_regressions"]
        self.assertEqual([row["q"] for row in rows], [3, 5, 7])
        self.assertEqual(sum(row["candidate_cubics"] for row in rows), 495)
        self.assertEqual(
            [row["observed_J_8"] for row in rows],
            [1536, 668160, 5526528],
        )
        self.assertEqual(
            [row["observed_J_10"] for row in rows],
            [6144, 10536960, 88166400],
        )
        self.assertTrue(
            all(row["J_8_difference"] == row["J_10_difference"] == 0 for row in rows)
        )

    def test_controls_are_loaded_after_symbolic_and_fourier_work(self) -> None:
        events: list[str] = []
        original_source = MODULE._load_source_packets
        original_symbolic = MODULE._build_symbolic_theorem
        original_forms = MODULE._build_modular_form_certificate
        original_controls = MODULE._enumerate_held_out

        def source() -> object:
            result = original_source()
            events.append("sources")
            return result

        def symbolic(*args: object, **kwargs: object) -> object:
            result = original_symbolic(*args, **kwargs)
            events.append("symbolic")
            return result

        def forms(*args: object, **kwargs: object) -> object:
            result = original_forms(*args, **kwargs)
            events.append("forms")
            return result

        def controls(*args: object, **kwargs: object) -> object:
            events.append("controls")
            return original_controls(*args, **kwargs)

        with (
            mock.patch.object(MODULE, "_load_source_packets", side_effect=source),
            mock.patch.object(MODULE, "_build_symbolic_theorem", side_effect=symbolic),
            mock.patch.object(
                MODULE, "_build_modular_form_certificate", side_effect=forms
            ),
            mock.patch.object(MODULE, "_enumerate_held_out", side_effect=controls),
        ):
            MODULE.build_fixture()
        self.assertEqual(events, ["sources", "symbolic", "forms", "controls"])

    def test_resource_caps_and_refusal(self) -> None:
        contract = self.fixture["resource_contract"]
        self.assertLessEqual(
            contract["actual_exact_operations"], contract["maximum_exact_operations"]
        )
        self.assertEqual(contract["actual_candidate_cubics"], 495)
        self.assertLessEqual(
            contract["actual_point_evaluations"],
            contract["maximum_point_evaluations"],
        )
        forms = self.fixture["modular_form_certificate"]
        with self.assertRaisesRegex(ValueError, "candidate cap"):
            MODULE._enumerate_held_out((11,), forms, MODULE.ResourceGuard())

        candidate_guard = MODULE.ResourceGuard(
            candidate_cubics=MODULE.MAX_CANDIDATE_CUBICS
        )
        with self.assertRaisesRegex(ValueError, "cumulative.*candidate cap"):
            MODULE._enumerate_held_out((3,), forms, candidate_guard)
        self.assertEqual(candidate_guard.candidate_cubics, MODULE.MAX_CANDIDATE_CUBICS)

        point_guard = MODULE.ResourceGuard(
            point_evaluations=MODULE.MAX_POINT_EVALUATIONS
        )
        with self.assertRaisesRegex(ValueError, "cumulative.*point-evaluation cap"):
            MODULE._enumerate_held_out((3,), forms, point_guard)
        self.assertEqual(point_guard.point_evaluations, MODULE.MAX_POINT_EVALUATIONS)

        guarded_increments = (
            ("operation", "exact_operations", MODULE.MAX_EXACT_OPERATIONS),
            ("candidate", "candidate_cubics", MODULE.MAX_CANDIDATE_CUBICS),
            ("point", "point_evaluations", MODULE.MAX_POINT_EVALUATIONS),
        )
        for method_name, attribute, maximum in guarded_increments:
            with self.subTest(method=method_name):
                guard = MODULE.ResourceGuard(**{attribute: maximum})
                with self.assertRaises(RuntimeError):
                    getattr(guard, method_name)()
                self.assertEqual(getattr(guard, attribute), maximum)

    def test_final_wall_time_cap_covers_fixture_assembly(self) -> None:
        with (
            mock.patch.object(
                MODULE.time,
                "monotonic",
                side_effect=[0.0, MODULE.MAX_WALL_SECONDS + 1.0],
            ),
            self.assertRaisesRegex(RuntimeError, "wall-time cap exceeded"),
        ):
            MODULE.build_fixture()

    def test_firewalls(self) -> None:
        text = " ".join(self.fixture["firewalls"])
        self.assertIn("full cusp-space trace", text)
        self.assertIn("No novelty claim", text)
        self.assertIn("no RH, GRH", text)
        self.assertIn("not proof inputs", text)


if __name__ == "__main__":
    unittest.main()
