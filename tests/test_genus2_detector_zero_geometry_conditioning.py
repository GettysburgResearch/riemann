"""Independent checks for exact detector/zero-geometry conditioning."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(FUNCTION_FIELD) not in sys.path:
    sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_detector_zero_geometry_conditioning as subject


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def rational(pair: list[int]) -> Fraction:
    return Fraction(pair[0], pair[1])


def assert_no_float(testcase: unittest.TestCase, value: object) -> None:
    testcase.assertNotIsInstance(value, float)
    if isinstance(value, dict):
        for item in value.values():
            assert_no_float(testcase, item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            assert_no_float(testcase, item)


class SourceAndAlgebraTests(unittest.TestCase):
    def test_all_dependency_hashes_are_authenticated(self) -> None:
        subject._verify_primitive_hashes()
        paths = {
            "histogram_fixture": subject.INPUT_PATH,
            "histogram_producer": subject.INPUT_PRODUCER_PATH,
            "coefficient_arithmetic": subject.COEFFICIENT_ARITHMETIC_PATH,
            "affine_action": subject.AFFINE_ACTION_PATH,
            "selector_producer": subject.SELECTOR_PRODUCER_PATH,
            "selector_note": subject.SELECTOR_NOTE_PATH,
            "note": subject.NOTE_PATH,
            "test": subject.TEST_PATH,
        }
        for name, path in paths.items():
            self.assertEqual(subject._lf_sha256(path), subject.EXPECTED_LF_SHA256[name])

    def test_source_and_selector_substitution_fail_closed(self) -> None:
        with (
            mock.patch.object(subject, "EXPECTED_INPUT_PAYLOAD_SHA256", "0" * 64),
            self.assertRaisesRegex(ValueError, "payload/source pin mismatch"),
        ):
            subject._validated_families()
        changed = dict(subject.EXPECTED_LF_SHA256)
        changed["selector_producer"] = "0" * 64
        with (
            mock.patch.object(subject, "EXPECTED_LF_SHA256", changed),
            self.assertRaisesRegex(ValueError, "digest mismatch"),
        ):
            subject._load_selector_module()

    def test_guard_refuses_above_inclusive_4096_cap(self) -> None:
        guard = subject.SourceAtomGuard()
        guard.preflight(4_096)
        with self.assertRaisesRegex(RuntimeError, "exceeds inclusive cap"):
            guard.preflight(4_097)
        guard.charge("atoms", 4_096)
        with self.assertRaisesRegex(RuntimeError, "would exceed"):
            guard.charge("one_more")

    def test_proxy_formulas_and_cosine_identities_are_exact(self) -> None:
        self.assertEqual(
            subject.spectral_proxies(5, 0, -10),
            {"C": Fraction(0), "G": Fraction(16)},
        )
        self.assertEqual(
            subject.spectral_proxies(5, 0, 10),
            {"C": Fraction(16), "G": Fraction(0)},
        )
        for x, y in (
            (Fraction(-1), Fraction(2, 3)),
            (Fraction(-2, 5), Fraction(1, 7)),
            (Fraction(0), Fraction(1)),
            (Fraction(11, 13), Fraction(-5, 17)),
        ):
            packet = subject.spectral_proxy_cosine_identities(x, y)
            self.assertEqual(packet["C_from_coefficients"], packet["C_from_cosines"])
            self.assertEqual(packet["G_from_coefficients"], packet["G_from_cosines"])


class FrozenConditioningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            int(row["q"]): row
            for row in cls.fixture["exact_frozen_member_weight_laws"]["families"]
        }

    def test_payload_mass_resource_accounting_and_no_floats(self) -> None:
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, canonical_sha256(payload))
        self.assertEqual(tuple(self.by_q), subject.FROZEN_Q_VALUES)
        self.assertEqual(
            self.fixture["resource_contract"]["source_atom_preflight_count"], 251
        )
        self.assertEqual(
            self.fixture["resource_contract"]["guarded_source_atom_visits"]["total"],
            251,
        )
        assert_no_float(self, self.fixture)
        for q, row in self.by_q.items():
            self.assertEqual(
                row["input_signed_source_atom_count"], subject.EXPECTED_ATOM_COUNTS[q]
            )
            self.assertEqual(
                sum(atom[-1] for atom in row["full_proxy_law"]["atoms"]),
                subject.EXPECTED_MEMBER_COUNTS[q],
            )

    def test_full_proxy_means_and_certificate_counts(self) -> None:
        expected = {
            3: (Fraction(1244, 243), Fraction(464, 81), 0, 0),
            5: (Fraction(17054, 3125), Fraction(3432, 625), 1, 15),
            7: (Fraction(94184, 16807), Fraction(12896, 2401), 0, 84),
        }
        for q, row in self.by_q.items():
            packet = row["full_proxy_law"]
            mean_c, mean_g, c_zero, g_zero = expected[q]
            self.assertEqual(tuple(map(rational, packet["mean_C_G"])), (mean_c, mean_g))
            counts = packet["certificate_member_counts"]
            self.assertEqual(counts["C_zero_endpoint_certificate"], c_zero)
            self.assertEqual(counts["G_zero_repeated_cosine_certificate"], g_zero)
            for atom in packet["atoms"]:
                self.assertGreaterEqual(Fraction(atom[0], atom[1]), 0)
                self.assertGreaterEqual(Fraction(atom[2], atom[3]), 0)

    def test_every_proxy_pushforward_reconstructs_directly_from_source_atoms(
        self,
    ) -> None:
        _, families = subject._validated_families()
        module = subject._load_selector_module()
        for family in families:
            q = int(family["q"])
            full: Counter[tuple[Fraction, Fraction]] = Counter()
            conditioned = {
                name: {sign: Counter() for sign in subject.SIGN_ORDER}
                for name in subject.SELECTOR_ORDER
            }
            for atom in family["joint_a_D_b_D_law"]["atoms"]:
                a = int(atom["a_D"])
                b = int(atom["b_D"])
                weight = int(atom["member_count"])
                # Deliberately use cleared source-coefficient formulas rather
                # than the producer's spectral_proxies helper.
                point = (
                    Fraction((2 * q + b) ** 2 - 4 * a * a * q, q * q),
                    Fraction(a * a - 4 * b + 8 * q, q),
                )
                full[point] += weight
                raw = module.selector_values_from_squared_first_elementary(
                    Fraction(a * a, q), Fraction(b, q)
                )
                for name, adapter_key in subject.ADAPTER_KEY_BY_SELECTOR.items():
                    conditioned[name][subject._sign(Fraction(raw[adapter_key]))][
                        point
                    ] += weight

            row = self.by_q[q]
            serialized_full = Counter(
                {
                    (Fraction(atom[0], atom[1]), Fraction(atom[2], atom[3])): atom[-1]
                    for atom in row["full_proxy_law"]["atoms"]
                }
            )
            self.assertEqual(serialized_full, full)
            for name in subject.SELECTOR_ORDER:
                for sign in subject.SIGN_ORDER:
                    law = row["selector_conditioning"][name]["sign_conditionals"][sign][
                        "proxy_law"
                    ]
                    serialized = (
                        Counter()
                        if law is None
                        else Counter(
                            {
                                (
                                    Fraction(atom[0], atom[1]),
                                    Fraction(atom[2], atom[3]),
                                ): atom[-1]
                                for atom in law["atoms"]
                            }
                        )
                    )
                    self.assertEqual(serialized, conditioned[name][sign])

    def test_every_sign_conditional_is_an_exact_complete_joint_law(self) -> None:
        for row in self.by_q.values():
            for name in subject.SELECTOR_ORDER:
                total = 0
                for sign in subject.SIGN_ORDER:
                    conditional = row["selector_conditioning"][name][
                        "sign_conditionals"
                    ][sign]
                    total += conditional["member_count"]
                    if conditional["proxy_law"] is None:
                        self.assertEqual(conditional["status"], "EMPTY_SIGN_STRATUM")
                        continue
                    law = conditional["proxy_law"]
                    self.assertEqual(
                        sum(atom[-1] for atom in law["atoms"]),
                        conditional["member_count"],
                    )
                    covariance = [
                        [rational(entry) for entry in matrix_row]
                        for matrix_row in law["covariance_matrix_C_G"]
                    ]
                    self.assertEqual(covariance[0][1], covariance[1][0])
                    self.assertGreaterEqual(covariance[0][0], 0)
                    self.assertGreaterEqual(covariance[1][1], 0)
                    self.assertGreaterEqual(
                        covariance[0][0] * covariance[1][1] - covariance[0][1] ** 2, 0
                    )
                self.assertEqual(total, row["member_count"])

    def test_stable_P_D_covariance_signs_and_field_specific_S_channel(self) -> None:
        for q, row in self.by_q.items():
            packets = row["selector_conditioning"]
            p_c, p_g = map(rational, packets["P"]["covariance_with_C_G"])
            d_c, d_g = map(rational, packets["D"]["covariance_with_C_G"])
            s_c, s_g = map(rational, packets["S"]["covariance_with_C_G"])
            self.assertGreater(p_c, 0)
            self.assertLess(p_g, 0)
            self.assertLess(d_c, 0)
            self.assertGreater(d_g, 0)
            self.assertLess(s_c, 0)
            self.assertEqual(s_g < 0, q == 3)

            for name, c_direction, g_direction in (("P", 1, -1), ("D", -1, 1)):
                contrast = tuple(
                    map(
                        rational,
                        packets[name]["positive_minus_negative_conditional_mean_C_G"],
                    )
                )
                self.assertGreater(c_direction * contrast[0], 0)
                self.assertGreater(g_direction * contrast[1], 0)

    def test_certificate_incidence_and_nonconverse(self) -> None:
        expected_g_zero = {
            3: {"P": (0, 0, 0), "D": (0, 0, 0), "S": (0, 0, 0)},
            5: {"P": (0, 5, 10), "D": (0, 0, 15), "S": (10, 0, 5)},
            7: {"P": (0, 42, 42), "D": (0, 0, 84), "S": (42, 0, 42)},
        }
        for q, row in self.by_q.items():
            for name in subject.SELECTOR_ORDER:
                actual = []
                for sign in subject.SIGN_ORDER:
                    law = row["selector_conditioning"][name]["sign_conditionals"][sign][
                        "proxy_law"
                    ]
                    actual.append(
                        0
                        if law is None
                        else law["certificate_member_counts"][
                            "G_zero_repeated_cosine_certificate"
                        ]
                    )
                self.assertEqual(tuple(actual), expected_g_zero[q][name])
        for q in (5, 7):
            d_positive = self.by_q[q]["selector_conditioning"]["D"][
                "sign_conditionals"
            ]["positive"]
            self.assertGreater(
                d_positive["member_count"],
                d_positive["proxy_law"]["certificate_member_counts"][
                    "G_zero_repeated_cosine_certificate"
                ],
            )

    def test_equal_detector_witnesses_reject_memberwise_recovery(self) -> None:
        q5p = self.by_q[5]["selector_conditioning"]["P"]["same_value_counterexamples"]
        strongest = q5p["strongest_distinct_proxy_pair_witness"]
        self.assertEqual(rational(strongest["selector_value"]), 0)
        self.assertEqual(strongest["distinct_proxy_pair_count_at_value"], 3)
        self.assertIsNotNone(q5p["same_value_C_certificate_vs_noncertificate_witness"])
        self.assertIsNotNone(q5p["same_value_G_certificate_vs_noncertificate_witness"])
        q5d = self.by_q[5]["selector_conditioning"]["D"]["same_value_counterexamples"]
        self.assertEqual(q5d["values_with_multiple_proxy_pairs"], 1)
        self.assertEqual(
            rational(q5d["strongest_distinct_proxy_pair_witness"]["selector_value"]),
            Fraction(16, 25),
        )
        self.assertEqual(
            self.by_q[3]["selector_conditioning"]["D"]["same_value_counterexamples"][
                "values_with_multiple_proxy_pairs"
            ],
            0,
        )
        self.assertEqual(
            self.by_q[7]["selector_conditioning"]["D"]["same_value_counterexamples"][
                "values_with_multiple_proxy_pairs"
            ],
            0,
        )

    def test_committed_fixture_is_exact_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(subject.Path(subject.__file__)), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("check: ok", completed.stdout)


if __name__ == "__main__":
    unittest.main()
