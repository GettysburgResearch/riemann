"""Independent exact tests for the SO(4)/Sym^3 spectral intersection packet."""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_so4_sym3_spectral_intersection as subject  # noqa: E402


def direct_curve(x: Fraction, y: Fraction) -> Fraction:
    return -(x**4) + x * x * y + x * x + y**3 - 2 * y * y


def direct_scaled_product(A: int, B: int, q: int) -> int:
    return (
        q * A * A - (B * B - 2 * q) ** 2
    ) * ((A * A - 2 * q) ** 2 - q * B * B)


def independent_graphs(A: int, B: int, q: int) -> list[tuple[str, int, int]]:
    s = math.isqrt(q)
    if s * s != q:
        return []
    output = []
    for epsilon in (-1, 1):
        if s * A == epsilon * (B * B - 2 * q):
            output.append(("u_from_v", epsilon, epsilon * B))
        if s * B == epsilon * (A * A - 2 * q):
            output.append(("v_from_u", epsilon, epsilon * A))
    return output


class EllipticSO4Sym3SpectralIntersectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_exact_pullback_factorization_and_symbolic_certificates(self) -> None:
        residuals = subject.symbolic_residuals()
        self.assertEqual(len(residuals), 25)
        self.assertTrue(all(not residual for residual in residuals.values()))
        self.assertIn("global_curve_factorization_residual", residuals)

        for u in (Fraction(-2), Fraction(-3, 2), Fraction(0), Fraction(1, 3), Fraction(2)):
            for v in (Fraction(-2), Fraction(-1), Fraction(0), Fraction(2, 3), Fraction(2)):
                x = u * v
                y = u * u + v * v - 2
                factored = (
                    (u - v * v + 2)
                    * (u + v * v - 2)
                    * (u * u - v - 2)
                    * (u * u + v - 2)
                )
                self.assertEqual(direct_curve(x, y), factored)

    def test_sign_bridge_normalized_spectra_and_raw_dilation(self) -> None:
        families = self.fixture["synthetic_square_q_hasse_lattice_replay"][
            "families"
        ]
        for family in families:
            q = family["q"]
            s = math.isqrt(q)
            for point in family["intersection_lattice_points"]:
                A, B = point["A"], point["B"]
                tensor = subject.tensor_coefficients(A, B, q)
                expected_graphs = independent_graphs(A, B, q)
                stored_graphs = [
                    (
                        branch["orientation"],
                        branch["epsilon"],
                        branch["sym3_geometric_trace_c"],
                    )
                    for branch in point["branches"]
                ]
                self.assertEqual(stored_graphs, expected_graphs)
                for branch in point["branches"]:
                    c = branch["sym3_geometric_trace_c"]
                    self.assertEqual(branch["sym3_source_base_coefficient_a"], -c)
                    sym3 = subject.sym3_coefficients_from_geometric_trace(c, q)
                    independent_dilation = tuple(
                        coefficient * s**degree
                        for degree, coefficient in enumerate(tensor)
                    )
                    self.assertEqual(independent_dilation, sym3)
                    self.assertEqual(subject.dilate_polynomial(tensor, s), sym3)
                    self.assertEqual(
                        subject.normalized_tensor_polynomial(A, B, q),
                        subject.normalized_sym3_polynomial(c, q),
                    )

    def test_scaled_integral_identity_and_nonsquare_obstruction(self) -> None:
        for q in (3, 5, 7, 11, 13, 27):
            bound = math.isqrt(4 * q)
            for A in range(-bound, bound + 1):
                for B in range(-bound, bound + 1):
                    x = Fraction(A * B, q)
                    y = Fraction(A * A + B * B - 2 * q, q)
                    direct = direct_curve(x, y) * q**4
                    self.assertEqual(direct.denominator, 1)
                    self.assertEqual(direct.numerator, direct_scaled_product(A, B, q))
                    self.assertEqual(
                        subject.scaled_intersection_residual(A, B, q),
                        direct.numerator,
                    )
                    self.assertNotEqual(direct, 0)
                    self.assertEqual(subject.graph_branches(A, B, q), [])

    def test_square_q_parameterization_union_and_incidence_counts(self) -> None:
        expected = {
            9: (12, 20),
            25: (12, 20),
            81: (44, 52),
        }
        for q, (expected_union, expected_incidence) in expected.items():
            s = math.isqrt(q)
            hits = 0
            incidences = 0
            for A in range(-2 * s, 2 * s + 1):
                for B in range(-2 * s, 2 * s + 1):
                    branches = independent_graphs(A, B, q)
                    on_curve = direct_scaled_product(A, B, q) == 0
                    self.assertEqual(on_curve, bool(branches))
                    hits += on_curve
                    incidences += len(branches)
            self.assertEqual((hits, incidences), (expected_union, expected_incidence))

        self.assertEqual(
            subject.square_prime_power_intersection_counts(5, 2)[
                "distinct_integral_hasse_lattice_points"
            ],
            76,
        )
        self.assertEqual(
            subject.square_prime_power_intersection_counts(5, 2)[
                "four_graph_branch_incidences"
            ],
            84,
        )

        for p in (3, 5, 7, 11):
            q = p**4
            A, B = 1 - 2 * p * p, p
            self.assertLessEqual(A * A, 4 * q)
            self.assertLessEqual(B * B, 4 * q)
            self.assertEqual(subject.scaled_intersection_residual(A, B, q), 0)
            classification = subject.waterhouse_intersection_classification(A, B, q)
            self.assertEqual(classification["stratum"], "integral_hasse_lattice_ghost")
            self.assertFalse(classification["both_tensor_input_traces_realized"])

    def test_waterhouse_realized_strata_and_mod_12_counts(self) -> None:
        expected_counts = {3: 12, 5: 8, 7: 8, 11: 12, 13: 4}
        for p, expected_count in expected_counts.items():
            q = p * p
            s = p
            special_pairs = [
                (A, B)
                for A in (-2 * s, -s, 0, s, 2 * s)
                for B in (-2 * s, -s, 0, s, 2 * s)
                if independent_graphs(A, B, q)
            ]
            self.assertEqual(len(special_pairs), 12)
            realized = [
                (A, B)
                for A, B in special_pairs
                if subject.waterhouse_intersection_classification(A, B, q)[
                    "both_tensor_input_traces_realized"
                ]
            ]
            self.assertEqual(len(realized), expected_count)
            theorem = subject.square_prime_power_intersection_counts(p, 1)
            self.assertEqual(theorem["waterhouse_realized_distinct_points"], expected_count)

        q9, q25 = self.fixture["synthetic_square_q_hasse_lattice_replay"][
            "families"
        ]
        self.assertEqual(q9["waterhouse_realized_intersection_point_count"], 12)
        self.assertEqual(q25["waterhouse_realized_intersection_point_count"], 8)

    def test_discriminant_restrictions_and_direct_resultants(self) -> None:
        for t in (
            Fraction(-2),
            Fraction(-3, 2),
            Fraction(-1),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1),
            Fraction(2),
        ):
            certificate = subject.discriminant_certificate_from_parameter(t)
            D = (t * t - 1) ** 2 * (t * t - 4) ** 2
            E = t * t * (t * t - 4) ** 2
            full = t**4 * (t * t - 1) ** 2 * (t * t - 4) ** 6
            self.assertEqual(certificate["coefficient_map_fold_D"], D)
            self.assertEqual(certificate["hasse_endpoint_factor_E"], E)
            self.assertEqual(certificate["full_quartic_root_discriminant"], full)
            self.assertEqual(certificate["direct_sylvester_resultant"], full)

        self.assertEqual(
            (
                subject.discriminant_certificate_from_parameter(2)["coefficient_map_fold_D"],
                subject.discriminant_certificate_from_parameter(2)["hasse_endpoint_factor_E"],
            ),
            (0, 0),
        )
        self.assertEqual(
            (
                subject.discriminant_certificate_from_parameter(1)["coefficient_map_fold_D"],
                subject.discriminant_certificate_from_parameter(1)["hasse_endpoint_factor_E"],
            ),
            (0, 9),
        )
        self.assertEqual(
            (
                subject.discriminant_certificate_from_parameter(0)["coefficient_map_fold_D"],
                subject.discriminant_certificate_from_parameter(0)["hasse_endpoint_factor_E"],
            ),
            (16, 0),
        )

    def test_all_645_locked_pairs_are_replayed_with_zero_hits(self) -> None:
        aggregate = self.fixture["locked_nonsquare_histogram_replay"]["aggregate"]
        self.assertEqual(aggregate["ordered_atom_pairs_checked"], 645)
        self.assertEqual(aggregate["intersection_atom_hit_count"], 0)
        self.assertEqual(aggregate["intersection_represented_mass"], 0)
        expected_atoms = {3: 7, 5: 9, 7: 11, 11: 13, 13: 15}
        for row in self.fixture["locked_nonsquare_histogram_replay"]["families"]:
            q = row["q"]
            self.assertEqual(row["source_trace_atom_count"], expected_atoms[q])
            self.assertEqual(row["ordered_atom_pairs_checked"], expected_atoms[q] ** 2)
            self.assertEqual(row["intersection_atom_hits"], [])

    def test_both_upstream_artifacts_are_authenticated_and_rederived(self) -> None:
        locks = self.fixture["producer_and_source_locks"]["locks"]
        self.assertEqual(set(locks), {"so4_fixture", "so4_producer", "sym3_fixture", "sym3_producer"})
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(lock["sha256_lf_normalized"], hashlib.sha256(normalized).hexdigest())
        self.assertEqual(locks["so4_fixture"]["schema"], subject.EXPECTED_SO4_SCHEMA)
        self.assertEqual(locks["sym3_fixture"]["schema"], subject.EXPECTED_SYM3_SCHEMA)
        audit = self.fixture["locked_sym3_factor_convention_audit"]
        self.assertEqual(audit["aggregate_raw_factor_atoms_checked"], 55)

    def test_payload_resource_contract_and_no_floats(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))
        resources = stored["resource_contract"]
        self.assertEqual(resources["actual_locked_source_histogram_atom_pairs"], 645)
        self.assertLess(
            resources["accounted_work_unit_ledger"]["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertEqual(resources["field_curve_or_model_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)

        def reject_floats(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_floats(item)
            elif isinstance(value, list):
                for item in value:
                    reject_floats(item)

        reject_floats(stored)

    def test_scope_literature_and_note_integrity(self) -> None:
        literature = self.fixture["literature_boundary"]
        self.assertIn("Waterhouse", literature["primary_reference"])
        self.assertIn("Theorem 4.1", literature["primary_reference"])
        self.assertIn("separate elliptic isogeny classes", self.fixture["synthetic_square_q_hasse_lattice_replay"]["realizability_boundary"])
        firewall = self.fixture["scope_firewall"]
        self.assertIn("do not supply", firewall["no_representation_homomorphism"])
        self.assertIn("unscaled", firewall["no_unscaled_raw_factor_identity"])
        self.assertIn("does not link", firewall["no_realizability_to_correspondence_upgrade"])
        self.assertIn("RH", firewall["no_RH_or_GRH_claim"])

        text = subject.NOTE_PATH.read_text(encoding="utf-8")
        self.assertEqual(text.count(r"\["), text.count(r"\]"))
        self.assertEqual(text.count(r"\begin{aligned}"), text.count(r"\end{aligned}"))
        self.assertEqual(text.count("```"), 2)
        self.assertIsNone(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))
        for anchor in (
            "16M-4",
            "P_{A\\otimes B}(sT)=P_{\\operatorname{Sym}^3,c}(T)",
            "645",
            "Waterhouse",
            "representation homomorphism",
            "3,334",
        ):
            self.assertIn(anchor, text)

    def test_strict_refusals_survive_optimized_python(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5, 7))
        for invalid_q in (2, 4, 8, 15, 21, 45):
            with self.subTest(q=invalid_q):
                with self.assertRaisesRegex(ValueError, "odd prime power"):
                    subject.so4_coordinates(1, 2, invalid_q)
        for malformed in (True, Fraction(1), "1", 1.0, None):
            with self.subTest(value=malformed):
                with self.assertRaises(TypeError):
                    subject.scaled_intersection_residual(malformed, 1, 5)
        with self.assertRaisesRegex(ValueError, "square q"):
            subject.normalized_sym3_polynomial(1, 5)
        with self.assertRaisesRegex(ValueError, "square q"):
            subject.waterhouse_intersection_classification(1, 1, 5)
        with self.assertRaisesRegex(ValueError, "odd prime"):
            subject.square_prime_power_intersection_counts(9, 1)
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.square_prime_power_intersection_counts(5, 0)
        with self.assertRaisesRegex(RuntimeError, "cap exceeded"):
            guard = subject.ResourceGuard()
            for _ in range(subject.ATOM_PAIR_CAP_INCLUSIVE + 1):
                guard.charge_pair()
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.ResourceGuard().charge(
                "deliberate_refusal", subject.ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE
            )


if __name__ == "__main__":
    unittest.main()
