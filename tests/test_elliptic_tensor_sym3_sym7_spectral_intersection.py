"""Independent exact tests for the tensor-Sym3 / Sym7 intersection packet."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_tensor_sym3_sym7_spectral_intersection as subject  # noqa: E402


FIXTURE_PATH = (
    FUNCTION_FIELD / "elliptic_tensor_sym3_sym7_spectral_intersection.json"
)
NOTE_PATH = (
    FUNCTION_FIELD / "ELLIPTIC_TENSOR_SYM3_SYM7_SPECTRAL_INTERSECTION.md"
)
PRODUCER_PATH = (
    FUNCTION_FIELD / "elliptic_tensor_sym3_sym7_spectral_intersection.py"
)
TEST_PATH = Path(__file__).resolve()


def canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


class EllipticTensorSym3Sym7SpectralIntersectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_payload_and_owned_file_authentication(self) -> None:
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(canonical_sha256(payload), claimed)
        self.assertEqual(
            self.fixture["schema"],
            "riemann.function_field.elliptic_tensor_sym3_sym7_spectral_intersection.v1",
        )
        locks = self.fixture["source_and_file_locks"]["owned_file_locks"]
        expected = {
            "producer": PRODUCER_PATH,
            "note": NOTE_PATH,
            "test": TEST_PATH,
        }
        for role, path in expected.items():
            self.assertEqual(locks[role]["sha256_lf_normalized"], lf_sha256(path))

    def test_normalized_newton_generators_are_frozen_exactly(self) -> None:
        generators = subject.normalized_coefficient_generators()
        certificate = self.fixture["exact_elimination_certificate"]
        self.assertEqual([len(item) for item in generators], [6, 13, 14, 17])
        self.assertEqual(
            [subject._poly_total_degree(item) for item in generators],
            [7, 12, 15, 16],
        )
        self.assertEqual(
            [subject._poly_serialize(item) for item in generators],
            certificate["generators_serialized"],
        )
        expected_f1 = {
            (1, 3, 0): 1,
            (1, 1, 0): -2,
            (0, 0, 7): -1,
            (0, 0, 5): 6,
            (0, 0, 3): -10,
            (0, 0, 1): 4,
        }
        self.assertEqual(generators[0], subject._poly_clean(expected_f1))

    def test_small_elimination_certificate_replays(self) -> None:
        replay = subject.elimination_certificate()
        frozen = self.fixture["exact_elimination_certificate"]
        self.assertEqual(
            replay["cleared_factorizations"]["A_sha256"],
            "8dfd20df07bd51688fec4e24ce6949bc90d411e2542f76296300aa9ec803c24f",
        )
        self.assertEqual(
            replay["cleared_factorizations"]["B_sha256"],
            "1d4755d0cb0fc12448f97b2110bf25be199315ca2ba0933f6fe8e86a00eb309b",
        )
        self.assertEqual(
            replay["cleared_factorizations"]["C_sha256"],
            "11b9e448ae95a8b2b790080073e76ee46c249e6822b45aefc05b2473f744c6d2",
        )
        self.assertEqual(
            replay["squarefree_residual_candidate_serialized"],
            frozen["squarefree_residual_candidate_serialized"],
        )
        self.assertIn(
            "A-B=-(V-2)",
            replay["small_ideal_membership_identity"],
        )
        self.assertIn(
            "Z^3-5Z^2+6Z-1",
            replay["squarefree_residual_candidate_containment"],
        )

    def test_special_and_generic_residual_witnesses(self) -> None:
        witnesses = subject.residual_witness_certificate()
        self.assertEqual(witnesses["all_zero_remainder_checks"], 56)
        self.assertEqual(
            witnesses["zero_remainder_checks"],
            {
                "N14": 8,
                "N16_u_zero": 8,
                "N16_v_squared_2": 16,
                "N9_18": 8,
                "N20": 8,
                "N8": 8,
            },
        )
        frozen = self.fixture["exact_elimination_certificate"]
        self.assertEqual(
            witnesses,
            frozen["verified_genuine_residual_strata"],
        )
        self.assertNotIn(
            "Z*(",
            frozen["exact_nongraph_Z_support"],
        )

    def test_Z_zero_original_system_stratification(self) -> None:
        certificate = subject.Z_zero_stratification_certificate()
        self.assertTrue(certificate["all_solutions_are_graph_points"])
        self.assertEqual(
            certificate["solutions"],
            [
                {"u": -2, "v": 0},
                {"u": 2, "v": 0},
                {"u": 0, "v": -2},
                {"u": 0, "v": 2},
            ],
        )
        self.assertEqual(
            certificate,
            self.fixture["exact_elimination_certificate"][
                "Z_zero_original_system_stratification"
            ],
        )

    def test_signed_graph_weight_and_coefficient_identities(self) -> None:
        certificate = subject.graph_weight_certificate()
        target = [-7, -5, -3, -1, 1, 3, 5, 7]
        self.assertEqual(certificate["target_weights"], target)
        self.assertEqual(
            certificate["Std(w^4)_tensor_Sym3(w)_weights"],
            target,
        )
        self.assertEqual(
            certificate["Std(w)_tensor_Sym3(w^2)_weights"],
            target,
        )
        self.assertEqual(
            certificate["signed_graph_coefficient_zero_residuals"],
            16,
        )
        self.assertIn(
            "coupled central sign",
            certificate["same_epsilon_reason"],
        )

    def test_compact_trace_moment_context(self) -> None:
        certificate = subject.compact_trace_moment_certificate()
        self.assertEqual(
            certificate["Std_SU2_tensor_Sym3_SU2_independent_product"],
            [1, 0, 1, 0, 8, 0, 170, 0, 5096],
        )
        self.assertEqual(
            certificate["Sym7_SU2"],
            [1, 0, 1, 0, 8, 0, 260, 0, 11096],
        )
        self.assertEqual(certificate["alias_through_degree"], 4)
        self.assertEqual(
            certificate["generic_USp8_standard_degree_4_moment"],
            3,
        )
        self.assertIn("not arithmetic-origin", certificate["firewall"])

    def test_raw_factor_reciprocity_and_frozen_values(self) -> None:
        samples = [
            (1, -2, 3),
            (-3, 3, 9),
            (4, 1, 5),
        ]
        for A, B, q in samples:
            tensor = subject.tensor_sym3_factor(A, B, q)
            target = subject.sym7_factor(A, q)
            self.assertEqual(len(tensor), 9)
            self.assertEqual(len(target), 9)
            for degree in range(5):
                self.assertEqual(
                    tensor[8 - degree],
                    q ** (4 * (4 - degree)) * tensor[degree],
                )
                self.assertEqual(
                    target[8 - degree],
                    q ** (7 * (4 - degree)) * target[degree],
                )
        self.assertEqual(
            subject.tensor_sym3_factor(1, -2, 3),
            (
                1,
                -4,
                78,
                936,
                -1053,
                75816,
                511758,
                -2125764,
                43046721,
            ),
        )
        self.assertEqual(
            subject.sym7_factor(1, 3),
            (
                1,
                35,
                -1365,
                -98280,
                -530712,
                -214938360,
                -6528752685,
                366112362105,
                22876792454961,
            ),
        )

    def test_typed_raw_identity_on_all_small_square_graphs(self) -> None:
        for q in (9, 25, 81):
            p, exponent = subject.prime_power_data(q)
            triples = subject.square_graph_triples(q)
            theorem = subject.hasse_lattice_count_theorem(p, exponent)
            self.assertEqual(len(triples), theorem["union_distinct_triples"])
            for A, B, C in triples:
                self.assertTrue(subject.integral_graph_predicate(A, B, C, q))
                self.assertTrue(subject.typed_factor_equal(A, B, C, q))

    def test_nonsquare_typed_basis_and_empty_graphs(self) -> None:
        for q in (3, 5, 7, 11, 13, 27):
            self.assertEqual(subject.square_graph_triples(q), set())
            for A, B in ((0, 0), (1, -1), (2, 3)):
                signature = subject.typed_tensor_signature(A, B, q)
                for degree, pair in enumerate(signature):
                    if degree % 2:
                        self.assertEqual(pair[0], 0)
                    else:
                        self.assertEqual(pair[1], 0)

    def test_p_adic_divisibility_and_count_formula(self) -> None:
        for p in (3, 5):
            for k in range(1, 6):
                s = p**k
                q = s * s
                first_divisor = p ** ((3 * k + 3) // 4)
                second_divisor = p ** ((k + 1) // 2)
                for C in range(-2 * s, 2 * s + 1):
                    F = C**4 - 4 * q * C**2 + 2 * q**2
                    G = C**2 - 2 * q
                    self.assertEqual(F % s**3 == 0, C % first_divisor == 0)
                    self.assertEqual(G % s == 0, C % second_divisor == 0)
                theorem = subject.hasse_lattice_count_theorem(p, 2 * k)
                expected = 8 * p ** (k // 4) + 8 * p ** (k // 2) - 4
                self.assertEqual(theorem["union_distinct_triples"], expected)
                self.assertEqual(theorem["closed_formula"], expected)
        for p, exponent in ((3, 1), (5, 3), (7, 5)):
            self.assertEqual(
                subject.hasse_lattice_count_theorem(p, exponent)[
                    "union_distinct_triples"
                ],
                0,
            )

    def test_eight_point_overlap_is_exact(self) -> None:
        for q in (9, 25, 81):
            s = math.isqrt(q)
            triples = subject.square_graph_triples(q)
            overlap = [
                triple
                for triple in triples
                if len(subject.graph_branches(*triple, q)) == 2
            ]
            self.assertEqual(len(overlap), 8)
            self.assertEqual(sorted({C // s for _, _, C in overlap}), [-2, -1, 1, 2])

    def test_locked_and_synthetic_replays_and_resource_cap(self) -> None:
        locked = self.fixture["locked_trace_support_replay"]
        self.assertEqual(
            locked["aggregate"],
            {
                "q_values": [3, 5, 7, 11, 13],
                "ordered_trace_triples_checked": 7975,
                "factor_equal_trace_triple_count": 0,
                "factor_equal_member_weight": 0,
            },
        )
        synthetic = self.fixture["synthetic_square_q_replay"]
        self.assertEqual(
            [
                (row["q"], row["ordered_trace_triples_checked"], row["factor_equal_trace_triple_count"])
                for row in synthetic["rows"]
            ],
            [(9, 2197, 12), (25, 9261, 12)],
        )
        resource = self.fixture["resource_contract"]
        self.assertEqual(resource["actual_locked_trace_triples"], 7975)
        self.assertEqual(resource["actual_synthetic_trace_triples"], 11458)
        total = resource["accounted_work_unit_ledger"]["total_accounted_work_units"]
        self.assertLess(total, resource["exclusive_accounted_work_unit_cap"])
        self.assertEqual(resource["runtime_symbolic_packages"], 0)
        self.assertEqual(resource["runtime_Groebner_basis_runs"], 0)
        self.assertEqual(resource["field_curve_or_model_enumerations"], 0)
        self.assertEqual(resource["floating_point_results"], 0)
        self.assertEqual(resource["random_samples"], 0)

    def test_source_locks_and_scope_firewalls(self) -> None:
        locks = self.fixture["source_and_file_locks"]["source_locks"]
        self.assertEqual(
            set(locks),
            {"genus1", "full_factor", "cyclotomic", "all_r_ladder"},
        )
        for lock in locks.values():
            self.assertEqual(len(lock["fixture_payload_sha256"]), 64)
            self.assertEqual(len(lock["fixture_sha256_lf_normalized"]), 64)
            self.assertEqual(len(lock["producer_sha256_lf_normalized"]), 64)
        firewall = self.fixture["scope_firewall"]
        self.assertIn("not claimed complete", firewall["no_complete_algebraic_residual_claim"])
        self.assertIn("no motive", firewall["no_local_to_global_upgrade"])
        self.assertIn("no zero-free region", firewall["no_RH_or_GRH_claim"])

    def test_strict_refusals_and_no_executable_asserts(self) -> None:
        for invalid in (True, False, 3.0, "3", None):
            with self.assertRaises(TypeError):
                subject.tensor_sym3_factor(invalid, 0, 3)
            with self.assertRaises(TypeError):
                subject.sym7_factor(invalid, 3)
        for invalid_q in (1, 2, 4, 6, 15, -3):
            with self.assertRaises(ValueError):
                subject.prime_power_data(invalid_q)
        with self.assertRaises(ValueError):
            subject.build_fixture((3, 5))
        guard = subject.ResourceGuard(locked_cap=1, synthetic_cap=1, work_cap=3)
        guard.charge_triple(locked=True)
        with self.assertRaises(RuntimeError):
            guard.charge_triple(locked=True)
        guard.charge_triple(locked=False)
        with self.assertRaises(RuntimeError):
            guard.charge("would_hit_exclusive_cap")

        source = PRODUCER_PATH.read_text(encoding="utf-8")
        self.assertNotIn("import sympy", source)
        self.assertNotIn("import numpy", source)
        self.assertNotIn("import random", source)
        executable_assert_lines = [
            line
            for line in source.splitlines()
            if line.lstrip().startswith("assert ")
        ]
        self.assertEqual(executable_assert_lines, [])


if __name__ == "__main__":
    unittest.main()
