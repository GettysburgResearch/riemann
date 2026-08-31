"""Prefix-only tests; they do not execute or certify the full grade-seven path."""

import copy
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research/l-families/atlas/generalized/segre-hadamard-source/composed_grade7_replay.py"
)
SPEC = importlib.util.spec_from_file_location("composed_grade7_prefix_tests", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class ComposedPrefixAcceptance(unittest.TestCase):
    def test_authentication_precedes_every_parse_and_import(self):
        with (
            patch.object(M, "authenticate", side_effect=ValueError("source")),
            patch.object(M, "read_json") as parse,
            patch.object(M, "compile_helper") as execute,
        ):
            with self.assertRaises(ValueError):
                M.source()
            parse.assert_not_called()
            execute.assert_not_called()

    def test_numeric_alias_json_and_duplicate_keys(self):
        for raw in (b'{"a":1.0}', b'{"a":NaN}', b'{"a":1,"a":2}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        for value in (True, 1.0):
            with self.assertRaises(ValueError):
                M.equal({"a": value}, {"a": 1})

    def test_canonical_body_is_checked(self):
        payload = {"stage": 6}
        payload["proof_object_sha256"] = M.digest(payload)
        M.body_check(payload)
        payload["stage"] = 7
        with self.assertRaises(ValueError):
            M.body_check(payload)

    def test_manifest_uses_exact_literal_pins(self):
        paths = []
        for freeze, pins in M.GROUPS:
            self.assertEqual(len(freeze), 40)
            for name, blob in pins.items():
                self.assertEqual(len(blob), 40)
                self.assertTrue(all(c in "0123456789abcdef" for c in blob))
                paths.append(name)
        self.assertEqual(len(paths), len(set(paths)))
        self.assertIn("resolution_stage5.cache.json", paths)
        self.assertIn("GLOBAL_EXACTNESS_FROM_CERTIFIED_KERNELS.md", paths)

    def test_coefficient_type_and_bit_caps(self):
        for value in (True, 1.0, 0, 1 << 4096):
            with self.assertRaises(ValueError):
                M.checked_coefficient(value)
        self.assertEqual(M.checked_coefficient(-7), -7)

    def test_literal_integer_domain(self):
        for value in (False, 6.0, -1, 8):
            with self.assertRaises(ValueError):
                M.integer(value, 0, 7)


class ComposedActualPrefix(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.context = M.source()

    def test_actual_prefix_is_not_a_new_rank_result(self):
        result = M.prefix_result(self.context)
        self.assertIs(result["grade7_constructed"], False)
        self.assertIs(result["new_kernel_rank_claimed"], False)
        self.assertIs(
            result["inherited_proofs"]["lower_stage_elimination_replayed"], False
        )
        self.assertIs(
            result["inherited_proofs"]["coordinate_acquisition_replayed"], False
        )

    def test_all_actual_polynomial_compositions_and_weights(self):
        checks = self.context.prefix_checks
        self.assertEqual(checks["D1D2"]["upper_columns"], 85)
        self.assertEqual(checks["D2D3"]["upper_columns"], 28)
        self.assertIs(checks["D1D2"]["all_compositions_zero"], True)
        self.assertIs(checks["D2D3"]["all_compositions_zero"], True)
        self.assertEqual(
            [
                checks["full_dual_weight_checks"][k]["dimension"]
                for k in ("D2_degree4", "D2_degree5", "D3_degree5", "D3_degree6")
            ],
            [65, 20, 11, 17],
        )

    def test_exact_accepted_source_identities(self):
        c = self.context
        M.equal(c.maps["F0_generators"], c.presentation["result"]["generators"])
        M.equal(c.maps["D1_columns"], c.presentation["result"]["D1_columns"])
        self.assertEqual(c.inherited["grade6_freeze"], M.GRADE6)
        self.assertEqual(c.coordinate["domain_columns"], 3775)

    def test_new_context_does_not_call_old_prefix_contracts(self):
        original = M.compile_helper

        def guarded(raw, name):
            module = original(raw, name)
            for attribute in (
                "verified_source",
                "verify_cache",
                "coordinate_check",
                "build_maps",
                "source",
            ):
                if hasattr(module, attribute):
                    setattr(
                        module,
                        attribute,
                        lambda *args, **kwargs: self.fail("old prefix replay called"),
                    )
            return module

        with patch.object(M, "compile_helper", side_effect=guarded):
            result = M.prefix_result(M.source())
        self.assertIs(result["grade7_constructed"], False)

    def test_changed_actual_d3_coefficient_breaks_composition(self):
        column = copy.deepcopy(self.context.maps["D3_columns"][0])
        column["terms"][0]["coefficient"] += 2
        with self.assertRaises(ValueError):
            M.compose(self.context.maps["D2_columns"], [column])

    def test_changed_source_weight_refused(self):
        columns = copy.deepcopy(self.context.maps["D2_columns"])
        columns[0]["weight"][0] += 1
        with self.assertRaises(ValueError):
            M.validate_map(
                self.context.helper,
                self.context.maps["D1_columns"],
                columns,
                {4: 65, 5: 20},
            )

    def test_duplicate_actual_polynomial_term_refused(self):
        columns = copy.deepcopy(self.context.maps["D2_columns"])
        columns[0]["terms"].append(copy.deepcopy(columns[0]["terms"][0]))
        with self.assertRaises(ValueError):
            M.validate_map(
                self.context.helper,
                self.context.maps["D1_columns"],
                columns,
                {4: 65, 5: 20},
            )

    def test_zero_degree_or_float_coefficient_refused(self):
        for field, value in (("S_exponent", [0] * 10), ("coefficient", 1.0)):
            columns = copy.deepcopy(self.context.maps["D2_columns"])
            columns[0]["terms"][0][field] = value
            with self.assertRaises(ValueError):
                M.validate_map(
                    self.context.helper,
                    self.context.maps["D1_columns"],
                    columns,
                    {4: 65, 5: 20},
                )

    def test_complete_source_columns_not_a_dimension_fit(self):
        columns = self.context.maps["D2_columns"][:-1]
        with self.assertRaises(ValueError):
            M.validate_map(
                self.context.helper,
                self.context.maps["D1_columns"],
                columns,
                {4: 65, 5: 20},
            )

    def test_prefix_keeps_old_caps_and_new_ownership(self):
        self.assertEqual(self.context.streamed.MAX_COLUMNS, 640)
        self.assertEqual(self.context.streamed.MAX_ROWS, 4096)
        self.assertEqual(self.context.helper.MAX_BITS, 4096)
        self.assertEqual(
            set(self.context.source_provenance["composed_algorithm"]),
            set(M.algorithm_bindings()),
        )
        self.assertIs(
            self.context.cache_provenance["fresh_cache_verification_performed"], False
        )


if __name__ == "__main__":
    unittest.main()
