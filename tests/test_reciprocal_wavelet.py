from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
ATLAS_ROOT = REPO_ROOT / "research" / "l-families" / "atlas"
CORE = ATLAS_ROOT / "core"
sys.path.insert(0, str(CORE))

from atlas_core import read_json  # noqa: E402
from reciprocal_wavelet import (  # noqa: E402
    EXPECTED_NUMBER_FIELD_SLUGS,
    filter_controls,
    metadata_for_specs,
    qsqrt2_sign,
    reciprocal_coefficients,
    wavelet_rows,
)
from validate_atlas import SchemaStore, validate_instance, validate_parameter_values  # noqa: E402


def mobius(value: int) -> int:
    remaining = value
    prime = 2
    factors = 0
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        factors += 1
    return -1 if factors % 2 else 1


class FilterAlgebraTests(unittest.TestCase):
    def test_expansion_and_three_roots(self) -> None:
        controls = filter_controls()
        self.assertEqual(
            controls["expanded_coefficients"],
            [
                {"rational": 1, "sqrt2": 0},
                {"rational": -2, "sqrt2": -1},
                {"rational": 1, "sqrt2": 2},
                {"rational": 0, "sqrt2": -1},
            ],
        )
        zero = {"rational": 0, "sqrt2": 0}
        self.assertEqual(controls["P_of_1"], zero)
        self.assertEqual(controls["P_prime_of_1"], zero)
        self.assertEqual(controls["P_of_inverse_sqrt2"], zero)
        self.assertTrue(controls["controls_pass"])

    def test_exact_sign_hostile_pairs(self) -> None:
        cases = {
            (1, -1): -1,
            (-1, 1): 1,
            (2, -1): 1,
            (-2, 1): -1,
            (0, 1): 1,
            (0, -1): -1,
            (1, 0): 1,
            (-1, 0): -1,
            (0, 0): 0,
        }
        for coordinates, expected in cases.items():
            self.assertEqual(qsqrt2_sign(*coordinates), expected)

    def test_endpoint_contract_fails_closed(self) -> None:
        coefficients = [0] * 17
        coefficients[1] = 1
        for endpoints in ([], [0], [-8], [8, 7], [8, 8], [24]):
            with self.assertRaises(ValueError):
                wavelet_rows(coefficients, endpoints)


class ReciprocalCoefficientTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        manifest = read_json(ATLAS_ROOT / "sources" / "lmfdb-curves.json")
        cls.metadata = metadata_for_specs(manifest)

    def test_zeta_coefficients_are_mobius(self) -> None:
        coefficients = reciprocal_coefficients(self.metadata["ZETA.RIEMANN"], 256)
        self.assertEqual(coefficients[1:], [mobius(value) for value in range(1, 257)])

    def test_quadratic_coefficients_are_mobius_times_character(self) -> None:
        coefficients = reciprocal_coefficients(self.metadata["DIRICHLET.QUADRATIC.MOD5"], 256)
        expected = []
        for value in range(1, 257):
            residue = value % 5
            character = 0 if residue == 0 else (1 if residue in {1, 4} else -1)
            expected.append(mobius(value) * character)
        self.assertEqual(coefficients[1:], expected)

    def test_good_and_bad_elliptic_prime_powers(self) -> None:
        curve = reciprocal_coefficients(self.metadata["EC.11.R0"], 256)
        self.assertEqual((curve[2], curve[4], curve[8]), (2, 2, 0))
        self.assertEqual(curve[6], curve[2] * curve[3])
        self.assertEqual((curve[11], curve[121]), (-1, 0))
        curve37 = reciprocal_coefficients(self.metadata["EC.37.R1"], 256)
        self.assertEqual(curve37[37], 1)


class WrappedWaveletTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.evaluation_path = next(
            (ATLAS_ROOT / "evaluations").glob("ATLAS.EVAL.RECIPROCAL_L.NUMBER_FIELD_PHASE0.MINIMAL_FILTER.*.json")
        )
        cls.evaluation = read_json(cls.evaluation_path)
        cls.result_path = REPO_ROOT / cls.evaluation["result"]["artifact"]["path"]
        cls.result = read_json(cls.result_path)
        cls.metadata = metadata_for_specs(read_json(ATLAS_ROOT / "sources" / "lmfdb-curves.json"))

    def test_frozen_subject_set_and_normalization_maps(self) -> None:
        self.assertEqual(
            [subject["identity_slug"] for subject in self.result["subjects"]],
            list(EXPECTED_NUMBER_FIELD_SLUGS),
        )
        maps = {subject["identity_slug"]: subject["classical_to_unitary_map"] for subject in self.result["subjects"]}
        self.assertEqual(maps["ZETA.RIEMANN"], "mu_unitary(n)=mu_classical(n)")
        self.assertEqual(maps["EC.11.R0"], "mu_unitary(n)=mu_classical(n)/sqrt(n)")

    def test_raw_result_schema_is_strict(self) -> None:
        schema_path = ATLAS_ROOT / "detectors" / "raw-schemas" / "reciprocal-wavelet-result.schema.json"
        store = SchemaStore()
        self.assertEqual(validate_instance(self.result, store.load(schema_path), schema_path, store), [])

    def test_rows_recompute_from_partial_sums(self) -> None:
        for subject in self.result["subjects"]:
            for row in subject["rows"]:
                m0, m1, m2, m3 = row["partial_sums_X_X2_X4_X8"]
                rational = m0 - 2 * m1 + m2
                sqrt2 = -m1 + 2 * m2 - m3
                self.assertEqual(row["wavelet_qsqrt2"], {"rational": rational, "sqrt2": sqrt2})
                self.assertEqual(row["field_norm"], rational * rational - 2 * sqrt2 * sqrt2)
                self.assertEqual(row["real_sign"], qsqrt2_sign(rational, sqrt2))

    def test_artifact_replays_from_primitive_coefficients(self) -> None:
        endpoints = [32, 64, 128, 256]
        for subject in self.result["subjects"]:
            coefficients = reciprocal_coefficients(self.metadata[subject["identity_slug"]], 256)
            self.assertEqual(subject["rows"], wavelet_rows(coefficients, endpoints))
            self.assertEqual(subject["nonzero_coefficient_count"], sum(value != 0 for value in coefficients[1:]))

    def test_local_arithmetic_dependency_is_content_bound(self) -> None:
        paths = {binding["path"] for binding in self.evaluation["adapter_bindings"]}
        self.assertIn("research/l-families/atlas/core/reciprocal_wavelet.py", paths)
        self.assertIn("research/l-families/atlas/core/local_euler.py", paths)

    def test_endpoint_parameter_rejects_invalid_values(self) -> None:
        detector_id = self.evaluation["detector_contract_binding"]["semantic_id"]
        detector = read_json(ATLAS_ROOT / "detectors" / f"{detector_id}.json")
        for endpoints in ([], [0], [-8], [8, 7], [8, 8]):
            errors = validate_parameter_values(
                detector,
                {"endpoints": endpoints, "endpoint_convention": "INCLUSIVE_FLOOR_DYADIC"},
            )
            self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
