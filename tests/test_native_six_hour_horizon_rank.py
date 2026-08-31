"""Independent acceptance controls for the frozen original-source horizon atlas."""

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_horizon_rank_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_horizon_certificate_test", PATH)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


class NativeHorizonRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source, cls.captures, cls.provenance = C.load_source()
        cls.rows, cls.decoded = C.validate_records(cls.captures["heldout"], 900)
        cls.panel50 = next(
            row
            for row in cls.captures["heldout"]["all_declared_thresholds"]
            if row["horizon"] == 50
        )

    def test_01_complete_replayed_certificate(self):
        result = C.build()
        self.assertEqual([row["panel_count"] for row in result["phases"]], [18, 65])
        self.assertEqual(result["phases"][1]["complete_records"], 954)
        self.assertEqual(result["first_full_rank_horizon_in_declared_range"], 450)
        self.assertIs(result["physical_equality_beyond_900_claimed"], False)
        self.assertIs(result["native_gamma_decoder_claimed"], False)

    def test_02_two_acquisition_freezes_and_theorem(self):
        self.assertEqual(len(self.provenance), 7)
        self.assertEqual(self.provenance[0]["commit"], C.CALIBRATION)
        self.assertEqual(self.provenance[3]["commit"], C.HELDOUT)
        self.assertEqual(self.provenance[-1]["commit"], C.THEORY)
        self.assertEqual(self.provenance[0]["blob"], self.provenance[3]["blob"])
        self.assertEqual(self.provenance[1]["blob"], self.provenance[4]["blob"])

    def test_03_all_literal_jumps(self):
        self.assertEqual(
            [(row["horizon"], row["jump"]) for row in C.literal_jumps()],
            [
                (6, 1),
                (10, 1),
                (12, 1),
                (15, 1),
                (18, 1),
                (20, 1),
                (30, 2),
                (45, 1),
                (50, 1),
                (60, 2),
                (75, 1),
                (90, 2),
                (150, 2),
                (180, 1),
                (300, 1),
                (450, 1),
            ],
        )
        self.assertEqual(
            [C.literal_dimension(h) for h in (25, 50, 60, 449, 450, 900)],
            [6, 10, 12, 19, 20, 20],
        )

    def test_04_supported_products_and_between_thresholds(self):
        values = C.supported_numbers(900)
        self.assertEqual(len(values), 83)
        self.assertIn(720, values)
        self.assertNotIn(700, values)
        self.assertEqual(C.literal_dimension(31), C.literal_dimension(32))
        for value in (True, 900.0, 0, 901):
            with self.assertRaises(ValueError):
                C.supported_numbers(value)

    def test_05_independent_modular_rank_and_bad_denominator(self):
        matrix = [{0: F(1, 2), 1: F(1, 3)}, {0: F(1), 1: F(2, 3)}, {2: F(5, 7)}]
        self.assertEqual(C.modular_rank(matrix)["rank"], 2)
        self.assertEqual(C.modular_rank([])["rank"], 0)
        with self.assertRaises(ValueError):
            C.modular_rank([{0: F(1, C.MODULUS)}])
        with self.assertRaises(ValueError):
            C.modular_rank([{True: F(1)}])

    def test_06_sparse_and_rational_type_counterfeits(self):
        self.assertEqual(
            C.sparse_row([[0, "1/2"], [35, "-2"]]), {0: F(1, 2), 35: F(-2)}
        )
        for row in (
            [[True, "1"]],
            [[0, "1"], [0, "2"]],
            [[0, "0"]],
            [[0, "2/4"]],
            [[0, 1.0]],
            [[36, "1"]],
        ):
            with self.assertRaises(ValueError):
                C.sparse_row(row)

    def test_07_json_duplicate_float_and_nonfinite(self):
        for raw in (b'{"x":1,"x":2}', b'{"x":1.0}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.assertRaises(ValueError):
                C.read_json(raw)

    def test_08_canonical_numeric_alias_counterfeits(self):
        for actual, expected in (({"x": True}, {"x": 1}), ({"x": 1.0}, {"x": 1})):
            with self.assertRaises(ValueError):
                C.replay_equal(actual, expected)

    def test_09_scope_flags_fail_before_digest(self):
        for key, value in (
            ("native_gamma_decoder_claimed", True),
            ("all_height_physical_rank_theorem_claimed", True),
            ("predicted_rank_is_not_assigned", 1),
        ):
            changed = dict(self.captures["heldout"])
            changed[key] = value
            with self.assertRaises(ValueError):
                C.validate_header(changed, "heldout")

    def test_10_complete_threshold_coverage(self):
        changed = copy.deepcopy(self.captures["calibration"])
        changed["all_declared_thresholds"].pop()
        core = {k: v for k, v in changed.items() if k != "proof_object_sha256"}
        changed["proof_object_sha256"] = C.sha256(
            C.canonical(core).encode()
        ).hexdigest()
        with self.assertRaisesRegex(ValueError, "threshold coverage"):
            C.certify_phase(changed, "calibration")

    def test_11_omitted_actual_source_record(self):
        changed = dict(self.captures["heldout"])
        changed["complete_source_records"] = self.rows[:-1]
        with self.assertRaisesRegex(ValueError, "source census"):
            C.validate_records(changed, 900)

    def test_12_wrong_physical_alias_weight(self):
        wrong = {}
        for index in self.panel50["complete_record_indices"]:
            row = self.rows[index]
            target = wrong.setdefault((row["a"], row["b"]), {})
            for column, value in self.decoded[index].items():
                target[column] = target.get(column, F()) + value
        changed = copy.deepcopy(self.panel50)
        changed["all_physical_curvature_rows"] = [
            {"ratio": list(ratio), "coordinates": C.sparse_value(wrong[ratio])}
            for ratio in sorted(wrong)
        ]
        self.assertNotEqual(
            changed["all_physical_curvature_rows"],
            self.panel50["all_physical_curvature_rows"],
        )
        with self.assertRaisesRegex(ValueError, "complete replay"):
            C.audit_panel(changed, self.rows, self.decoded)

    def test_13_panel_coverage_and_actual_rank_corruption(self):
        changed = copy.deepcopy(self.panel50)
        changed["complete_record_indices"].pop()
        with self.assertRaises(ValueError):
            C.audit_panel(changed, self.rows, self.decoded)
        changed = copy.deepcopy(self.panel50)
        changed["physical_rank"]["rank"] = 9
        with self.assertRaisesRegex(ValueError, "lower bound"):
            C.audit_panel(changed, self.rows, self.decoded)

    def test_14_boolean_rank_and_bad_record_labels(self):
        changed = copy.deepcopy(self.panel50)
        changed["source_rank"]["rank"] = True
        with self.assertRaisesRegex(ValueError, "literal bounded integer"):
            C.audit_panel(changed, self.rows, self.decoded)
        changed = dict(self.captures["heldout"])
        changed["complete_source_records"] = copy.deepcopy(self.rows)
        changed["complete_source_records"][0]["n"] = True
        with self.assertRaisesRegex(ValueError, "literal bounded integer"):
            C.validate_records(changed, 900)


if __name__ == "__main__":
    unittest.main()
