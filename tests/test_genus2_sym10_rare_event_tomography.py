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
    / "genus2_sym10_rare_event_tomography.py"
)
OUTPUT_PATH = MODULE_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location(
    "genus2_sym10_rare_event_tomography", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Sym10 rare-event producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Genus2Sym10RareEventTomographyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = MODULE.build_fixture()
        cls.disk = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        cls.by_q = {
            row["q"]: row for row in cls.fixture["finite_tomography"]["families"]
        }

    def test_fixture_is_canonical(self) -> None:
        self.assertEqual(self.fixture, self.disk)
        claimed = self.fixture["payload_sha256"]
        payload = dict(self.fixture)
        payload.pop("payload_sha256")
        self.assertEqual(claimed, MODULE._canonical_sha256(payload))

    def test_reciprocal_polynomial_is_derived_exactly(self) -> None:
        guard = MODULE.ResourceGuard()
        tower = MODULE._derive_reciprocal_tower(guard)
        for q, a, b in ((3, -3, 7), (5, 0, 10), (7, 7, 24)):
            direct = [1]
            for endpoint in range(1, 11):
                value = -a * direct[endpoint - 1]
                if endpoint >= 2:
                    value -= b * direct[endpoint - 2]
                if endpoint >= 3:
                    value -= q * a * direct[endpoint - 3]
                if endpoint >= 4:
                    value -= q * q * direct[endpoint - 4]
                direct.append(value)
            self.assertEqual(
                MODULE._evaluate_polynomial(tower[10], a, b, q), direct[10]
            )
            recurrence_guard = MODULE.ResourceGuard()
            self.assertEqual(
                MODULE._evaluate_reciprocal_recurrence(a, b, q, 10, recurrence_guard),
                direct[10],
            )
            self.assertEqual(recurrence_guard.recurrence_updates, 10)

    def test_compact_resonance_and_ceiling_certificate(self) -> None:
        compact = self.fixture["compact_resonance_certificate"]
        self.assertEqual(compact["sym10_dimension"], 286)
        self.assertEqual(
            compact["equality_rigidity"]["only_equality_classes"], ["I", "-I"]
        )
        endpoint_ten = compact["central_quadratic_square_ladder"][-1]
        self.assertEqual(endpoint_ten["endpoint"], 10)
        self.assertEqual(endpoint_ten["P=(1+qT^2)^2"], -6)
        self.assertEqual(endpoint_ten["P=(1-qT^2)^2"], 6)

    def test_complete_sign_and_tail_laws(self) -> None:
        expected = {
            3: ((57, 18, 87), 401, 6, [401, 3958], [160801, 848976]),
            5: ((1125, 50, 1325), 11928, 36, [26046, 205711], [1281072, 2879041]),
            7: (
                (7980, 336, 6090),
                50300,
                168,
                [73709, 859163],
                [5773597990, 18244130049],
            ),
        }
        for q, (signs, threshold, members, l1_share, l2_share) in expected.items():
            row = self.by_q[q]
            self.assertEqual(
                (
                    row["sign_member_counts"]["negative"],
                    row["sign_member_counts"]["zero"],
                    row["sign_member_counts"]["positive"],
                ),
                signs,
            )
            tail = row["tied_outer_absolute_one_percent_tail"]
            self.assertEqual(tail["threshold"], threshold)
            self.assertEqual(tail["member_count"], members)
            self.assertEqual(tail["share_of_absolute_first_moment"], l1_share)
            self.assertEqual(tail["share_of_second_moment"], l2_share)

    def test_first_moment_tail_sensitivity_is_not_universal(self) -> None:
        self.assertEqual(self.by_q[3]["mean_r_10"], [638, 27])
        self.assertEqual(self.by_q[3]["trimmed_bulk"]["mean_r_10"], [237, 26])
        self.assertEqual(
            self.by_q[3]["tied_outer_absolute_one_percent_tail"][
                "share_of_signed_total"
            ],
            [401, 638],
        )
        self.assertEqual(
            self.by_q[5]["tied_outer_absolute_one_percent_tail"][
                "share_of_signed_total"
            ],
            [-5, 296],
        )
        self.assertEqual(
            self.by_q[7]["tied_outer_absolute_one_percent_tail"][
                "share_of_signed_total"
            ],
            [3724, 50271],
        )

    def test_split_repeated_and_central_strata(self) -> None:
        expected = {
            3: (27, 0, 0, 0),
            5: (705, 15, 15, 5),
            7: (3570, 84, 42, 42),
        }
        for q, (split, repeated, repeated_tail, central_plus) in expected.items():
            loci = self.by_q[q]["exceptional_loci"]
            self.assertEqual(loci["integral_split"]["member_count"], split)
            self.assertEqual(loci["repeated_factor"]["member_count"], repeated)
            self.assertEqual(
                loci["repeated_factor"]["tail_member_count"], repeated_tail
            )
            self.assertEqual(loci["central_plus"]["member_count"], central_plus)

    def test_zero_atoms_and_small_field_resonance(self) -> None:
        self.assertEqual(
            [
                (row["a_D"], row["b_D"], row["member_count"])
                for row in self.by_q[3]["zero_atoms"]
            ],
            [(-3, 6, 3), (0, 0, 12), (3, 6, 3)],
        )
        self.assertEqual(
            self.by_q[5]["zero_atoms"],
            [{"a_D": 0, "b_D": 0, "member_count": 50, "sym3_coefficient_curve": True}],
        )
        self.assertEqual(
            self.by_q[7]["zero_atoms"],
            [{"a_D": 0, "b_D": 0, "member_count": 336, "sym3_coefficient_curve": True}],
        )

    def test_sources_load_after_symbolic_certificate(self) -> None:
        events: list[str] = []
        original_tower = MODULE._derive_reciprocal_tower
        original_compact = MODULE._derive_compact_certificate
        original_load = MODULE._load_sources

        def observed_tower(guard: object) -> object:
            result = original_tower(guard)
            events.append("tower_closed")
            return result

        def observed_compact(tower: object, guard: object) -> object:
            result = original_compact(tower, guard)
            events.append("compact_closed")
            return result

        def observed_load(guard: object) -> object:
            events.append("sources_loaded")
            return original_load(guard)

        with (
            mock.patch.object(
                MODULE, "_derive_reciprocal_tower", side_effect=observed_tower
            ),
            mock.patch.object(
                MODULE, "_derive_compact_certificate", side_effect=observed_compact
            ),
            mock.patch.object(MODULE, "_load_sources", side_effect=observed_load),
        ):
            MODULE.build_fixture()
        self.assertLess(events.index("tower_closed"), events.index("sources_loaded"))
        self.assertLess(events.index("compact_closed"), events.index("sources_loaded"))

    def test_source_read_and_wall_caps_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "oversize.json"
            path.write_bytes(b"x" * 64)
            lock = {
                "path": path,
                "lf_sha256": "unused",
                "payload_sha256": "unused",
                "audited_commit": "unused",
            }
            with (
                mock.patch.object(MODULE, "MAX_SOURCE_BYTES", 8),
                mock.patch.object(MODULE, "SOURCE_LOCKS", {"oversize": lock}),
                self.assertRaisesRegex(RuntimeError, "before full read"),
            ):
                MODULE._load_sources(MODULE.ResourceGuard())

        events: list[str] = []
        original_hash = MODULE._canonical_sha256

        def observed_hash(value: object) -> str:
            if (
                isinstance(value, dict)
                and value.get("schema") == self.fixture["schema"]
            ):
                events.append("payload_hashed")
            return original_hash(value)

        with (
            mock.patch.object(MODULE, "_canonical_sha256", side_effect=observed_hash),
            mock.patch.object(MODULE.time, "perf_counter", side_effect=[0.0, 4.0]),
            self.assertRaisesRegex(RuntimeError, "wall cap"),
        ):
            MODULE.build_fixture()
        self.assertEqual(events, ["payload_hashed"])

    def test_atom_recurrence_and_symbolic_caps_fail_closed(self) -> None:
        cases = (
            ("source atoms", "MAX_SOURCE_ATOMS", 31, "source-atom cap"),
            ("recurrence", "MAX_RECURRENCE_UPDATES", 9, "recurrence-update cap"),
            ("formal algebra", "MAX_SYMBOLIC_OPERATIONS", 0, "symbolic-operation cap"),
            (
                "sparse oracle",
                "MAX_SYMBOLIC_OPERATIONS",
                self.fixture["source_order_firewall"][
                    "symbolic_operations_before_sources"
                ],
                "symbolic-operation cap",
            ),
        )
        for label, attribute, limit, message in cases:
            with (
                self.subTest(label=label),
                mock.patch.object(MODULE, attribute, limit),
                self.assertRaisesRegex(RuntimeError, message),
            ):
                MODULE.build_fixture()

    def test_source_hash_lock_fails_closed(self) -> None:
        locks = {name: dict(lock) for name, lock in MODULE.SOURCE_LOCKS.items()}
        locks["balanced_joint_law"]["lf_sha256"] = "0" * 64
        with (
            mock.patch.object(MODULE, "SOURCE_LOCKS", locks),
            self.assertRaisesRegex(RuntimeError, "LF-normalized source hash mismatch"),
        ):
            MODULE.build_fixture()


if __name__ == "__main__":
    unittest.main()
