"""Independent replay tests for the Sym^3 exterior / Sym^4 bridge."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import sym3_exterior_sym4_plethysm_bridge as subject


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def multiply(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            output[left_degree + right_degree] += left_value * right_value
    return tuple(output)


def factor_from_roots(roots: tuple[int, ...]) -> tuple[int, ...]:
    coefficients = (1,)
    for root in roots:
        coefficients = multiply(coefficients, (1, -root))
    return coefficients


class Sym3ExteriorSym4PlethysmBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_rank_two_plethysm_by_independent_weight_multisets(self) -> None:
        sym3_weights = ((3, 0), (2, 1), (1, 2), (0, 3))
        wedge = Counter(
            (left[0] + right[0], left[1] + right[1])
            for left, right in itertools.combinations(sym3_weights, 2)
        )
        rhs = Counter({(3, 3): 1})
        rhs.update((degree + 1, 5 - degree) for degree in range(5))
        self.assertEqual(wedge, rhs)
        self.assertEqual(
            wedge,
            Counter({(5, 1): 1, (4, 2): 1, (3, 3): 2, (2, 4): 1, (1, 5): 1}),
        )
        certificate = self.fixture["rank_two_representation_identity"]
        self.assertEqual(certificate["dimension"], 6)
        self.assertIn("characteristic-zero", certificate["assumptions"])
        self.assertIn("S_(5,1)", certificate["Schur_functor_form"])

    def test_local_factor_bridge_by_direct_root_products(self) -> None:
        for alpha, beta in ((1, 3), (2, 5), (-1, -3), (-2, -5), (3, 7)):
            with self.subTest(alpha=alpha, beta=beta):
                t = alpha + beta
                q = alpha * beta
                Q = q**3
                sym3_roots = (
                    alpha**3,
                    alpha**2 * beta,
                    alpha * beta**2,
                    beta**3,
                )
                direct_sym3 = factor_from_roots(sym3_roots)
                self.assertEqual(subject.sym3_local_coefficients(t, q), direct_sym3)

                wedge_roots = tuple(
                    sym3_roots[first] * sym3_roots[second]
                    for first, second in itertools.combinations(range(4), 2)
                )
                direct_wedge = factor_from_roots(wedge_roots)
                primitive = subject.bridge_local_coefficients(t, q)
                self.assertEqual(direct_wedge, multiply((1, -Q), primitive))

                sym4_roots = (
                    alpha**4,
                    alpha**3 * beta,
                    alpha**2 * beta**2,
                    alpha * beta**3,
                    beta**4,
                )
                direct_sym4 = factor_from_roots(sym4_roots)
                self.assertEqual(subject.sym4_local_coefficients(t, q), direct_sym4)
                direct_twist = factor_from_roots(tuple(q * root for root in sym4_roots))
                self.assertEqual(primitive, direct_twist)
                self.assertEqual(
                    primitive,
                    subject.scale_local_variable(direct_sym4, q),
                )

        # Separate coefficient-algebra checks, including values that are not
        # supplied as products of positive Weil roots.
        for q in (1, 3, 5, 9, 25):
            for t in range(-8, 9):
                a3 = -t**3 + 2 * q * t
                b3 = q * (t**4 - 3 * q * t * t + 2 * q * q)
                C = t**4 - 3 * q * t * t + q * q
                D = q * (t * t - 2 * q) * C
                self.assertEqual(b3, q * (C + q * q))
                self.assertEqual(a3 * a3 - b3, (t * t - 2 * q) * C)
                expected = (1, -q * C, q**2 * D, -q**5 * D, q**10 * C, -q**15)
                self.assertEqual(
                    subject.primitive_exterior_coefficients(a3, b3, q**3),
                    expected,
                )
                self.assertEqual(subject.bridge_local_coefficients(t, q), expected)

        symbolic = self.fixture["local_factor_commutative_diagram"]["symbolic_certificate"]
        self.assertEqual(
            symbolic["R_Q_minus_P_Sym4_at_qT_residual_term_counts_T0_through_T5"],
            [0, 0, 0, 0, 0, 0],
        )

    def test_normalized_curve_identity_and_node_map(self) -> None:
        for x_squared in (Fraction(0), Fraction(1, 3), Fraction(1), Fraction(7, 2), Fraction(9)):
            for y in (Fraction(-2), Fraction(0), Fraction(2, 5), Fraction(1), Fraction(4)):
                F3 = -x_squared**2 + x_squared * y + x_squared + y**3 - 2 * y**2
                s = y - 1
                k = x_squared - y
                F4 = k**2 + s * k - s**2 - s**3
                self.assertEqual(F4, -F3)
                self.assertEqual(subject.sym4_curve_residual(s, k), -F3)

        expected_node_map = {
            (-1, 1): (0, 0),
            (0, 0): (-1, 0),
            (1, 1): (0, 0),
        }
        for (x, y), expected in expected_node_map.items():
            self.assertEqual(subject.primitive_coordinate_map(x * x, y), expected)

        # F4_s=k-2s-3s^2 and F4_k=2k+s.  The collapsed side-node
        # image is singular; the central ghost image has nonzero gradient.
        self.assertEqual((0 - 0 - 0, 0 + 0), (0, 0))
        s, k = -1, 0
        self.assertEqual((k - 2 * s - 3 * s * s, 2 * k + s), (-1, -1))
        self.assertEqual(2**2 + 2 - 1, 5)
        geometry = self.fixture["normalized_coefficient_diagram"]
        central = geometry["node_map"][2]
        self.assertEqual(central["Sym4_image"], [-1, 0])
        self.assertEqual(central["Sym4_parameter_w"], 0)
        self.assertEqual(central["Sym3_parameter_equation"], "t0^2=2")
        self.assertTrue(central["image_is_smooth"])
        self.assertIn("ghost remains", central["odd_q_arithmetic_status"])

    def test_all_251_source_atoms_are_independently_transformed(self) -> None:
        source = json.loads(subject.INTERSECTION_FIXTURE_PATH.read_text(encoding="utf-8"))
        transcript: list[list[int]] = []
        family_counts: dict[int, tuple[int, int, int, int]] = {}
        compressed_counts: dict[int, Counter[tuple[Fraction, Fraction]]] = {}
        for family in source["frozen_atom_transform"]["families"]:
            q = int(family["q"])
            hits = 0
            hit_members = 0
            members = 0
            compressed: Counter[tuple[Fraction, Fraction]] = Counter()
            for row in family["transformed_atoms"]:
                a = int(row["a_D"])
                b = int(row["b_D"])
                count = int(row["member_count"])
                members += count
                x2 = Fraction(a * a, q)
                y = Fraction(b, q)
                F3 = -x2**2 + x2 * y + x2 + y**3 - 2 * y**2
                s = y - 1
                k = x2 - y
                F4 = k**2 + s * k - s**2 - s**3
                hit = F3 == 0
                self.assertEqual(F4, -F3)
                self.assertEqual(F3 * q**3, row["scaled_curve_residual"])
                self.assertEqual(hit, row["on_compact_sym3_curve"])
                transcript.append(
                    [
                        q,
                        a,
                        b,
                        count,
                        s.numerator,
                        s.denominator,
                        k.numerator,
                        k.denominator,
                        F3.numerator,
                        F3.denominator,
                        F4.numerator,
                        F4.denominator,
                        int(hit),
                    ]
                )
                if hit:
                    hits += 1
                    hit_members += count
                    compressed[(s, k)] += count
            family_counts[q] = (len(family["transformed_atoms"]), members, hits, hit_members)
            compressed_counts[q] = compressed

        self.assertEqual(
            family_counts,
            {3: (32, 162, 3, 18), 5: (81, 2500, 2, 55), 7: (138, 14406, 2, 378)},
        )
        self.assertEqual(
            compressed_counts,
            {
                3: Counter({(Fraction(-1), Fraction(0)): 12, (Fraction(1), Fraction(1)): 6}),
                5: Counter({(Fraction(-1), Fraction(0)): 50, (Fraction(1), Fraction(-2)): 5}),
                7: Counter({(Fraction(-1), Fraction(0)): 336, (Fraction(1), Fraction(-2)): 42}),
            },
        )
        incidence = self.fixture["frozen_genus2_incidence"]
        self.assertEqual(len(transcript), 251)
        self.assertEqual(
            canonical_sha256(transcript),
            incidence["all_atom_transform_transcript_sha256"],
        )
        totals = incidence["aggregate_audit_totals"]
        self.assertEqual(totals["common_hit_signed_atom_count"], 7)
        self.assertEqual(totals["common_hit_member_count"], 451)
        self.assertEqual(totals["sign_compressed_hit_count"], 6)
        self.assertTrue(incidence["all_251_atoms_satisfy_F4_equals_minus_F3"])

    def test_exact_signed_hits_and_ghost_preservation(self) -> None:
        families = {
            row["q"]: row for row in self.fixture["frozen_genus2_incidence"]["families"]
        }
        expected_signed = {
            3: [(-3, 6, 3, [1, 1], [1, 1]), (0, 0, 12, [-1, 1], [0, 1]), (3, 6, 3, [1, 1], [1, 1])],
            5: [(0, 0, 50, [-1, 1], [0, 1]), (0, 10, 5, [1, 1], [-2, 1])],
            7: [(0, 0, 336, [-1, 1], [0, 1]), (0, 14, 42, [1, 1], [-2, 1])],
        }
        for q, expected in expected_signed.items():
            actual = [
                (
                    row["a_D"],
                    row["b_D"],
                    row["member_count"],
                    row["primitive_s"],
                    row["primitive_k"],
                )
                for row in families[q]["signed_hit_atoms"]
            ]
            self.assertEqual(actual, expected)
            self.assertTrue(families[q]["hit_sets_exactly_identical"])
            compressed = families[q]["sign_compressed_hits"]
            self.assertEqual(len(compressed), 2)
            ghost = next(row for row in compressed if row["primitive_s"] == [-1, 1])
            self.assertEqual(ghost["primitive_k"], [0, 1])
            self.assertTrue(ghost["arithmetic_ghost_preserved"])

    def test_source_locks_stored_fixture_firewalls_and_caps(self) -> None:
        note_integrity = subject.validate_note_integrity()
        self.assertEqual(note_integrity["forbidden_C0_control_count"], 0)
        self.assertTrue(note_integrity["known_escape_loss_patterns_absent"])
        self.assertGreater(note_integrity["display_math_pair_count"], 0)
        for name, lock in subject.SOURCE_PACKET_LOCKS.items():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashlib.sha256(normalized).hexdigest(), lock["file_sha256_lf_normalized"], name)
            source = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(source["schema"], lock["schema"])
            self.assertEqual(source["payload_sha256"], lock["payload_sha256"])
            unhashed_source = dict(source)
            claimed_source = unhashed_source.pop("payload_sha256")
            self.assertEqual(claimed_source, canonical_sha256(unhashed_source))

        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, canonical_sha256(unhashed))
        producer = stored["producer"]
        for path, field in (
            (Path(subject.__file__), "script_sha256_lf_normalized"),
            (subject.NOTE_PATH, "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashlib.sha256(normalized).hexdigest(), producer[field])

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(stored)
        resources = stored["resource_contract"]
        self.assertEqual(resources["field_or_curve_enumerations"], 0)
        self.assertEqual(resources["source_signed_atoms_transformed"], 251)
        self.assertLess(
            resources["accounted_work_unit_ledger"]["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        firewall = stored["weight_and_Tate_twist_firewall"]
        self.assertIn("P_Sym4(q*T), not P_Sym4(T)", firewall["load_bearing_rescaling"])
        self.assertIn("no second common Tate line", firewall["retained_middle_root"])
        boundary = stored["literature_and_priority_boundary"]
        self.assertIn("classical", boundary["classical_plethysm"])
        self.assertEqual(boundary["priority_claim"], "none; no claim of literature priority for the diagram or packaging")
        self.assertIn("no RH", boundary["analytic_claim"])
        self.assertIn("odd", stored["next_family_target"]["name"])

    def test_refusals(self) -> None:
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.sym3_local_coefficients(1, 0)
        with self.assertRaisesRegex(TypeError, "built-in int"):
            subject.sym4_local_coefficients(True, 3)
        with self.assertRaisesRegex(ValueError, "positive"):
            subject.primitive_exterior_coefficients(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "nonempty"):
            subject.multiply_coefficients((), (1, 2))
        guard = subject.ResourceGuard()
        with self.assertRaisesRegex(RuntimeError, "exclusive cap 512"):
            guard.charge("deliberate_refusal", 512)


if __name__ == "__main__":
    unittest.main()
