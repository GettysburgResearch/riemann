"""Final acceptance and independent arithmetic controls for both tail outcomes."""

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/riemann-structures/native-six-hour/native_physical_tail_certificate.py"
)
SPEC = importlib.util.spec_from_file_location("native_tail_final_tests", PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PhysicalTailFinalAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = MODULE.read_json(MODULE.FIXTURE.read_bytes())
        MODULE.body_check(cls.fixture)
        cls.calibration = cls.fixture["complete_acquisitions"]["calibration"]
        cls.heldout = cls.fixture["complete_acquisitions"]["heldout"]

    def test_complete_fresh_frozen_replay(self):
        MODULE.equal(MODULE.build(), self.fixture)

    def test_typed_fixture_numeric_counterfeits(self):
        for value in (True, 1.0):
            with self.assertRaises(ValueError):
                MODULE.equal({"rank": value}, {"rank": 1})
        changed = dict(self.fixture)
        changed["execution_status"] = "UNKNOWN"
        with self.assertRaises(ValueError):
            MODULE.body_check(changed)

    def test_duplicate_and_floating_json_refused(self):
        for raw in (b'{"x":1,"x":1}', b'{"x":1.0}', b'{"x":NaN}'):
            with self.assertRaises(ValueError):
                MODULE.read_json(raw)

    def test_authentication_precedes_parse_and_execution(self):
        with (
            patch.object(MODULE, "authenticate", side_effect=ValueError("source")),
            patch.object(MODULE, "read_json") as parse,
            patch("builtins.compile") as compile_source,
        ):
            with self.assertRaises(ValueError):
                MODULE.source()
            parse.assert_not_called()
            compile_source.assert_not_called()

    def test_distinct_declared_phases_not_interchangeable(self):
        with self.assertRaises(ValueError):
            MODULE.audit_pair(self.heldout, self.calibration)


class PhysicalTailIndependentArithmetic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        record = MODULE.read_json(MODULE.FIXTURE.read_bytes())
        cls.calibration = record["complete_acquisitions"]["calibration"]
        cls.heldout = record["complete_acquisitions"]["heldout"]

    def test_both_inverse_ranks_and_unknowns_rechecked(self):
        rows = MODULE.audit_pair(self.calibration, self.heldout)
        self.assertEqual([r["exact_minor_rank"] for r in rows], [20, 20])
        self.assertTrue(
            all(
                r["mathematical_status"] == "UNKNOWN_TAIL_NOT_CONTRACTIVE" for r in rows
            )
        )
        self.assertTrue(all(r["all_future_horizons_certified"] is False for r in rows))

    def test_a_changed_alias_weight_is_detected(self):
        panel = dict(self.calibration["result"])
        panel["rows"] = list(panel["rows"])
        row = dict(panel["rows"][0])
        panel["rows"][0] = row
        row["complete_aliases"] = list(row["complete_aliases"])
        alias = dict(row["complete_aliases"][0])
        row["complete_aliases"][0] = alias
        alias["g"] = 2
        with self.assertRaises(ValueError):
            MODULE.audit_panel(panel, self.calibration["selection"])

    def test_selected_coordinate_reordering_is_not_refitted(self):
        selection = dict(self.calibration["selection"])
        indices = list(selection["coordinate_indices"])
        indices[0], indices[1] = indices[1], indices[0]
        selection["coordinate_indices"] = indices
        with self.assertRaises(ValueError):
            MODULE.audit_panel(self.calibration["result"], selection)

    def test_same_positive_prefix_cannot_be_signed_sum(self):
        panel = dict(self.calibration["result"])
        panel["rows"] = list(panel["rows"])
        row = dict(panel["rows"][0])
        panel["rows"][0] = row
        row["positive_prefix"] = list(row["positive_prefix"])
        row["positive_prefix"][0] = str(F(row["positive_prefix"][0]) + 1)
        with self.assertRaises(ValueError):
            MODULE.audit_panel(panel, self.calibration["selection"])

    def test_inverse_forgery_fails_actual_product(self):
        panel = dict(self.calibration["result"])
        contraction = dict(panel["contraction"])
        panel["contraction"] = contraction
        inverse = dict(contraction["inverse"])
        contraction["inverse"] = inverse
        inverse["matrix"] = [list(row) for row in inverse["matrix"]]
        inverse["matrix"][0][0] = str(F(inverse["matrix"][0][0]) + 1)
        with self.assertRaises(ValueError):
            MODULE.audit_panel(panel, self.calibration["selection"])

    def test_unknown_cannot_be_promoted_to_pass(self):
        panel = dict(self.heldout["result"])
        panel["contraction"] = dict(panel["contraction"])
        panel["contraction"]["status"] = "PASS"
        panel["contraction"]["all_future_horizons_certified"] = True
        with self.assertRaises(ValueError):
            MODULE.audit_panel(panel, self.heldout["selection"])

    def test_numeric_aliases_and_noncanonical_rationals(self):
        panel = dict(self.calibration["result"])
        panel["horizon"] = 900.0
        with self.assertRaises(ValueError):
            MODULE.audit_panel(panel, self.calibration["selection"])
        for value in (True, 1, "2/2", "0.5"):
            with self.assertRaises(ValueError):
                MODULE.rational(value)
        with self.assertRaises(ValueError):
            MODULE.sparse36([[True, "1"]])

    def test_outward_diagnostics_never_decide_acceptance(self):
        for value in (F(0), F(1), F(1, 3), F(10**80, 7)):
            low, high = map(F, MODULE.display_interval(value))
            self.assertLessEqual(low, value)
            self.assertLess(value, high)
            self.assertEqual(high - low, F(1, 10**6))

    def test_no_new_selection_or_gap_claim(self):
        heldout = dict(self.heldout)
        heldout["selection"] = dict(heldout["selection"])
        heldout["selection"]["row_indices"] = list(
            reversed(heldout["selection"]["row_indices"])
        )
        with self.assertRaises(ValueError):
            MODULE.audit_pair(self.calibration, heldout)
        heldout = dict(self.heldout)
        heldout["scope"] = dict(heldout["scope"])
        heldout["scope"]["all_horizons_rank_equality_certified"] = True
        with self.assertRaises(ValueError):
            MODULE.audit_pair(self.calibration, heldout)


if __name__ == "__main__":
    unittest.main()
