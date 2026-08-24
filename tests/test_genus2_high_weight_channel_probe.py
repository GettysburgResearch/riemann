"""Focused checks for the bounded genus-two high-weight channel probe."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_high_weight_channel_probe as subject  # noqa: E402


class GenusTwoHighWeightChannelProbeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_character_identities_and_dimensions(self) -> None:
        certificate = self.fixture["character_certificate"]
        self.assertIn("Kostant C2", certificate["method"])
        channels = certificate["channels"]
        self.assertEqual(
            {name: row["dimension"] for name, row in channels.items()},
            {"chi_(0,3)": 30, "chi_(2,2)": 81, "chi_(0,4)": 55},
        )
        self.assertTrue(
            all(row["status"] == "EXACT_C2_CHARACTER_IDENTITY" for row in channels.values())
        )
        self.assertEqual(
            certificate["factorization"],
            "chi_(2,2)=((1-e)^2-t^2)*(t^2-e-1), where t=Tr(U), e=e_2(U)",
        )
        left = {(0, 0): 1, (0, 1): -2, (0, 2): 1, (2, 0): -1}
        right = {(2, 0): 1, (0, 1): -1, (0, 0): -1}
        product: dict[tuple[int, int], int] = {}
        for (ti, ei), ci in left.items():
            for (tj, ej), cj in right.items():
                monomial = (ti + tj, ei + ej)
                product[monomial] = product.get(monomial, 0) + ci * cj
        self.assertEqual(
            {key: value for key, value in product.items() if value},
            subject.CHANNEL_POLYNOMIALS["chi_(2,2)"],
        )

    def test_triangular_basis_is_exact_and_raw_moment_aligned(self) -> None:
        bridge = self.fixture["triangular_raw_moment_bridge"]
        self.assertEqual(bridge["status"], "EXACT_POINTWISE_FOR_EVERY_FAMILY_MEMBER")
        self.assertEqual(bridge["R3"]["only_new_raw_moment"], "b_D^3")
        self.assertEqual(
            bridge["R22"]["only_new_raw_moment"], "a_D^2*b_D^2"
        )
        self.assertEqual(bridge["R4"]["only_new_raw_moment"], "b_D^4")

        triangular = self.fixture["character_certificate"]["triangular_basis"]
        self.assertEqual(
            triangular["R3"]["character_combination"], {"chi_(0,3)": 1}
        )
        self.assertEqual(
            triangular["R22"]["character_combination"],
            {"chi_(0,3)": 1, "chi_(2,2)": 1},
        )
        self.assertEqual(
            triangular["R4"]["character_combination"],
            {"chi_(0,3)": 4, "chi_(2,2)": 3, "chi_(0,4)": 1},
        )
        self.assertEqual(
            {name: row["dimension_checksum"] for name, row in triangular.items()},
            {"R3": 30, "R22": 111, "R4": 418},
        )

    def test_b3_signature_census_and_primitive_noncancellation(self) -> None:
        roadmap = self.fixture["b_cubed_signature_roadmap"]
        self.assertEqual(
            roadmap["status"],
            "EXACT_SIGNATURE_ROADMAP_PRIMITIVE_AVERAGES_UNRESOLVED",
        )
        self.assertEqual(roadmap["signature_count"], 23)
        self.assertEqual(
            roadmap["radical_degree_signature_counts"],
            {"0": 4, "2": 10, "4": 5, "6": 4},
        )
        expected_polynomials = {
            "0": [0, 2, -6, 5],
            "2": [0, -16, 40, -36, 12],
            "4": [0, 30, -70, 63, -29, 6],
            "6": [0, -16, 36, -32, 17, -6, 1],
        }
        actual = {
            degree: [Fraction(*pair) for pair in coefficients]
            for degree, coefficients in roadmap[
                "radical_degree_tuple_polynomials_low_to_high"
            ].items()
        }
        self.assertEqual(
            actual,
            {
                degree: [Fraction(value) for value in coefficients]
                for degree, coefficients in expected_polynomials.items()
            },
        )
        generic = roadmap["generic_degree_six_rows"]
        self.assertEqual(
            [Fraction(*row["leading_mixture_weight"]) for row in generic],
            [Fraction(1, 8), Fraction(3, 8), Fraction(3, 8), Fraction(1, 8)],
        )
        self.assertEqual(
            [row["S5_p1_coefficient"] for row in generic],
            ["21-q^2", "11-q^2", "5-q^2", "3-q^2"],
        )
        self.assertEqual(
            [row["S5_p2_coefficient"] for row in generic],
            ["q-6", "q-4", "q-2", "q-0"],
        )
        self.assertIn("FAILED", roadmap["signature_level_cancellation_result"])

    def test_frozen_channels_reconstruct_H_and_sparse_candidates(self) -> None:
        expected = {
            3: ([74, 3**6], [37, 3**6], [-19, 3**7], [536, 3**7]),
            5: ([614, 5**6], [213, 5**6], [-51, 5**7], [7154, 5**7]),
            7: ([2386, 7**6], [621, 7**6], [-99, 7**7], [37652, 7**7]),
        }
        for row in self.fixture["finite_aggregate_controls"]:
            q = row["q"]
            channels = row["channel_means"]
            self.assertEqual(
                (
                    channels["chi_(0,3)"],
                    channels["chi_(2,2)"],
                    channels["chi_(0,4)"],
                    row["H_mean"],
                ),
                expected[q],
            )
            self.assertTrue(row["all_internal_bridges_match"])
        candidate = self.fixture["sparse_all_q_candidate"]
        self.assertEqual(
            candidate["status"],
            "CONJECTURE_MATCHING_ONLY_Q3_Q5_Q7_NOT_INTERPOLATION_THEOREM",
        )
        self.assertEqual(candidate["implied_H_rescaled_limit"], 2)
        self.assertIn("neither constant", candidate["relation_to_previous_9_over_4_nomination"])
        quotient = candidate["affine_quotient_trace_normalization"]
        self.assertEqual(quotient["candidate_T_(0,3)"], "q^4-2*q-1")
        self.assertEqual(quotient["candidate_T_(2,2)"], "2*q^3-q^2-2*q-2")
        self.assertEqual(quotient["candidate_T_(0,4)"], "-(2*q^2+1)")
        self.assertIn("not certified", quotient["geometric_handoff"])
        for q in (3, 5, 7, 9, 11):
            family_size = q**4 * (q - 1)
            means = subject._candidate_channel_means(q)
            self.assertEqual(
                Fraction(q**3 * family_size, q * (q - 1))
                * means["chi_(0,3)"],
                q**4 - 2 * q - 1,
            )
            self.assertEqual(
                Fraction(q**3 * family_size, q * (q - 1))
                * means["chi_(2,2)"],
                2 * q**3 - q**2 - 2 * q - 2,
            )
            self.assertEqual(
                Fraction(q**4 * family_size, q * (q - 1))
                * means["chi_(0,4)"],
                -(2 * q**2 + 1),
            )

    def test_fixture_replay_source_locks_and_firewalls(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "genus2_high_weight_channel_probe.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, self.fixture)
        payload = dict(stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(subject._canonical_sha256(payload), claimed)
        for source in stored["source_locks"].values():
            if "sha256_lf_normalized" not in source:
                continue
            path = ROOT / source["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                hashlib.sha256(normalized).hexdigest(),
                source["sha256_lf_normalized"],
            )

        resources = stored["resource_contract"]
        self.assertEqual(resources["field_enumeration"], "FORBIDDEN_AND_NOT_IMPORTED")
        self.assertLess(
            resources["exact_signature_operations_used"],
            resources["maximum_exact_signature_operations"],
        )
        self.assertTrue(any("not proved" in value for value in stored["firewalls"]))
        self.assertTrue(any("not interpolation" in value for value in stored["firewalls"]))
        source_text = Path(subject.__file__).read_text(encoding="utf-8")
        self.assertNotIn("import genus2_q_scan", source_text)
        self.assertNotIn("build_field_tables", source_text)
        self.assertNotIn("itertools.product", source_text)


if __name__ == "__main__":
    unittest.main()
