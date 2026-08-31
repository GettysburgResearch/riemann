"""Bounded source, grouped-event, modular-witness and composition controls."""

from __future__ import annotations

import copy
import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/riemann-structures/native-six-hour/native_event_minor.py"
SPEC = importlib.util.spec_from_file_location("native_event_minor", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def states(matrix):
    return {str(p): [[int(x) % p for x in row] for row in matrix] for p in M.MODULI}


class EventMinorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = M.calibration()
        cls.utilities, cls.helper, cls.minor, cls.old, *_ = M.source()

    def test_complete_base_matches_actual_frozen_matrix(self):
        M.equal(self.base["base_exact_matrix"], self.old["result"]["matrix"])
        self.assertTrue(self.base["base_exact_inverse_both_products"])
        self.assertTrue(self.base["endpoint_rank20_certified"])
        self.assertEqual(self.base["certified_integer_intervals"], [[900, 900]])

    def test_source_pins_before_compile_or_parse(self):
        with (
            patch.object(M, "authenticate", side_effect=ValueError("source pin")),
            patch("builtins.compile") as compiled,
            patch.object(M, "read_json") as parsed,
            self.assertRaises(ValueError),
        ):
            M.source()
        compiled.assert_not_called()
        parsed.assert_not_called()

    def test_both_declared_primes_have_complete_trial_certificates(self):
        for prime in M.MODULI:
            certificate = M.primality_certificate(prime)
            expected = [
                [d, prime % d] for d in range(2, certificate["trial_limit"] + 1)
            ]
            self.assertEqual(certificate["all_trial_divisor_residues"], expected)
            self.assertTrue(all(remainder for _, remainder in expected))
        with self.assertRaises(ValueError):
            M.primality_certificate(25)

    def test_actual_field_denominators_and_refusal(self):
        q = F(-17, 2**20 * 3**8 * 5**4)
        for prime in M.MODULI:
            value, residue = M.reduce_rational(q, prime)
            self.assertNotEqual(residue, 0)
            self.assertEqual(value * q.denominator % prime, q.numerator % prime)
        with self.assertRaises(ValueError):
            M.reduce_rational(F(1, 65521), 65521)
        with self.assertRaises(ValueError):
            M.reduce_rational(True, 65521)

    def test_lu_exact_determinant_and_singular_witness(self):
        p = 65521
        matrix = [[2, 3], [5, 7]]
        witness = M.modular_lu(matrix, p)
        self.assertEqual(witness["rank"], 2)
        self.assertEqual(witness["determinant_mod_p"], p - 1)
        self.assertEqual(witness["echelon"][1][0], 0)
        singular = M.modular_lu([[1, 2], [2, 4]], p)
        self.assertEqual(singular["rank"], 1)
        self.assertEqual(singular["determinant_mod_p"], 0)

    def test_declared_fallback_is_not_a_rank_counterexample(self):
        certificate = M.rank_certificate(states([[65521]]))
        self.assertEqual(certificate["status"], "PASS")
        self.assertEqual(certificate["chosen_modulus"], 1000003)
        self.assertEqual([a["rank"] for a in certificate["attempts"]], [0, 1])
        self.assertTrue(M.is_certified(certificate, 1))

    def test_both_singular_moduli_remain_unknown(self):
        certificate = M.rank_certificate(states([[0]]))
        self.assertEqual(certificate["status"], "UNKNOWN_MODULAR_RANK")
        self.assertIsNone(certificate["chosen_modulus"])
        self.assertFalse(M.is_certified(certificate, 1))
        changed = copy.deepcopy(certificate)
        changed["status"] = "PASS"
        changed["chosen_modulus"] = 65521
        with self.assertRaises(ValueError):
            M.is_certified(changed, 1)

    def test_simultaneous_updates_are_applied_before_rank(self):
        start = states([[1, 0], [0, 1]])
        first = {"row": 0, "modular_update": {str(p): [p - 1, 1] for p in M.MODULI}}
        second = {"row": 1, "modular_update": {str(p): [1, p - 1] for p in M.MODULI}}
        intermediate = copy.deepcopy(start)
        self.assertEqual(
            M.apply_group(intermediate, [first])["status"], "UNKNOWN_MODULAR_RANK"
        )
        actual = copy.deepcopy(start)
        certificate = M.apply_group(actual, [first, second])
        self.assertEqual(certificate["status"], "PASS")
        for prime in M.MODULI:
            self.assertEqual(actual[str(prime)], [[0, 1], [1, 0]])

    def test_complete_small_event_census_and_ties(self):
        ratios = [(2, 3), (3, 2)]
        addresses = M.event_addresses(self.utilities, ratios, 0, 54)
        self.assertEqual(
            addresses,
            [[6, 0, 1], [6, 1, 1], [24, 0, 2], [24, 1, 2], [54, 0, 3], [54, 1, 3]],
        )
        self.assertEqual(
            M.event_addresses(self.utilities, ratios, 24, 54), [[54, 0, 3], [54, 1, 3]]
        )

    def test_independent_literal_alias_census(self):
        for maximum in (10, 100, 1024):
            expected = []
            for g in range(1, maximum + 1):
                n = g
                for p in (2, 3, 5):
                    while n % p == 0:
                        n //= p
                if n == 1:
                    expected.append(g)
            self.assertEqual(self.utilities.supported_aliases(maximum), expected)

    def test_source_update_original_weight_and_denominator_records(self):
        row = 0
        update = M.source_update(self.utilities, self.helper, self.minor, row, 2)
        full = self.helper.decode_sparse(update["source_curvature"])
        for position, column in enumerate(self.minor["coordinate_indices"]):
            q = self.utilities.rational(update["exact_selected_update"][position])
            self.assertEqual(q, full[column] / 2)
            for prime in M.MODULI:
                value, residue = M.reduce_rational(q, prime)
                self.assertEqual(update["modular_update"][str(prime)][position], value)
                self.assertEqual(
                    update["denominator_residues"][str(prime)][position], residue
                )
        self.assertEqual(
            update["n"] * update["m"], 4 * update["ratio"][0] * update["ratio"][1]
        )

    def test_unknown_groups_leave_exact_integer_gaps(self):
        identity = [[int(i == j) for j in range(20)] for i in range(20)]
        good = M.rank_certificate(states(identity))
        bad = M.rank_certificate(states([[0] * 20 for _ in range(20)]))
        events = [
            {"horizon": 904, "rank_certificate": bad},
            {"horizon": 910, "rank_certificate": good},
        ]
        intervals, endpoint = M.certified_intervals(900, 915, True, events)
        self.assertEqual(intervals, [[901, 903], [910, 915]])
        self.assertTrue(endpoint)
        self.assertEqual(
            M.merge_intervals([[900, 900], *intervals]), [[900, 903], [910, 915]]
        )

    def test_no_events_preserves_only_the_known_interval(self):
        self.assertEqual(
            M.certified_intervals(900, 903, True, []), ([[901, 903]], True)
        )
        self.assertEqual(M.certified_intervals(900, 903, False, []), ([], False))

    def test_predecessor_and_power_guards_before_loading(self):
        with patch.object(M, "source") as load:
            for power, commit in (
                (9, "0" * 40),
                (49, "0" * 40),
                (10, None),
                (True, "0" * 40),
            ):
                with self.assertRaises(ValueError):
                    M.panel(power, commit)
        load.assert_not_called()
        with self.assertRaises(ValueError):
            M.collection([])

    def test_typed_json_and_full_body_digest(self):
        for raw in (b'{"n":1.0}', b'{"n":NaN}', b'{"n":1,"n":2}'):
            with self.assertRaises(ValueError):
                M.read_json(raw)
        with self.assertRaises(ValueError):
            M.equal({"n": True}, {"n": 1})
        M.body_check(self.base)
        changed = copy.deepcopy(self.base)
        changed["endpoint_states"]["65521"][0][0] ^= 1
        with self.assertRaises(ValueError):
            M.body_check(changed)

    def test_modular_state_types_and_limits(self):
        with self.assertRaises(ValueError):
            M.validate_state([[True]], 65521, 1)
        with self.assertRaises(ValueError):
            M.validate_state([[65521]], 65521, 1)
        with self.assertRaises(ValueError):
            M.reduce_rational(2**4096, 65521)
        self.assertEqual(self.helper.LOCAL_CUTOFF, 64)
        with self.assertRaises(ValueError):
            self.helper.local_source(81)

    def test_source_scope_is_curvature_not_ambient_or_energy(self):
        scope = self.base["scope"]
        self.assertEqual(scope["curvature_variation_dimension"], 20)
        self.assertEqual(scope["ambient_tensor_dimension"], 64)
        for key in (
            "ambient64_faithfulness_threshold_claimed",
            "infinite_tail_claimed",
            "new_energy_minimum_claimed",
            "native_gamma_decoder_claimed",
        ):
            self.assertFalse(scope[key])
        self.assertEqual(
            self.base["predecessor_proof_input"], "none_base_reconstructed"
        )

    def test_rank_witness_corruption_is_detectable(self):
        matrix = [[3, 5], [7, 11]]
        witness = M.modular_lu(matrix, 65521)
        changed = copy.deepcopy(witness)
        changed["steps"][0]["pivot_value"] += 1
        with self.assertRaises(ValueError):
            M.equal(changed, M.modular_lu(matrix, 65521))
        changed = copy.deepcopy(witness)
        changed["determinant_mod_p"] = 0
        certificate = {"status": "PASS", "chosen_modulus": 65521, "attempts": [changed]}
        with self.assertRaises(ValueError):
            M.is_certified(certificate, 2)


if __name__ == "__main__":
    unittest.main()
