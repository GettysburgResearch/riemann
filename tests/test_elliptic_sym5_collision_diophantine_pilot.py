from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import re
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
MODULE_PATH = FUNCTION_FIELD / "elliptic_sym5_collision_diophantine_pilot.py"
SPEC = importlib.util.spec_from_file_location(
    "elliptic_sym5_collision_diophantine_pilot", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def independent_e5(t: int, q: int) -> int:
    return t * (t * t - q) * (t * t - 3 * q)


def independent_power_sum(order: int, t: int, q: int) -> int:
    if order == 0:
        return 2
    previous_previous, previous = 2, t
    for _ in range(2, order + 1):
        previous_previous, previous = previous, t * previous - q * previous_previous
    return previous


def independent_tau(m: int, t: int, q: int) -> int:
    if m == 0:
        return 1
    previous_previous, previous = 1, t
    for _ in range(2, m + 1):
        previous_previous, previous = previous, t * previous - q * previous_previous
    return previous


def independent_sym5_factor(t: int, q: int) -> tuple[int, ...]:
    power_sums = [0] + [
        independent_tau(5, independent_power_sum(order, t, q), q**order)
        for order in range(1, 7)
    ]
    coefficients = [1]
    for degree in range(1, 7):
        numerator = -sum(
            coefficients[degree - order] * power_sums[order]
            for order in range(1, degree + 1)
        )
        if numerator % degree:
            raise AssertionError("independent Newton reconstruction lost integrality")
        coefficients.append(numerator // degree)
    return tuple(coefficients)


def independent_is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % divisor for divisor in range(3, math.isqrt(n) + 1, 2))


def independent_quartic_discriminant(
    a: int, b: int, c: int, d: int, e: int
) -> int:
    return (
        256 * a**3 * e**3
        - 192 * a * a * b * d * e * e
        - 128 * a * a * c * c * e * e
        + 144 * a * a * c * d * d * e
        - 27 * a * a * d**4
        + 144 * a * b * b * c * e * e
        - 6 * a * b * b * d * d * e
        - 80 * a * b * c * c * d * e
        + 18 * a * b * c * d**3
        + 16 * a * c**4 * e
        - 4 * a * c**3 * d * d
        - 27 * b**4 * e * e
        + 18 * b**3 * c * d * e
        - 4 * b**3 * d**3
        - 4 * b * b * c**3 * e
        + b * b * c * c * d * d
    )


def independent_prime_power(q: int) -> tuple[int, int] | None:
    if q < 3 or q % 2 == 0:
        return None
    for p in range(3, math.isqrt(q) + 1, 2):
        if q % p:
            continue
        if not independent_is_prime(p):
            return None
        residue, exponent = q, 0
        while residue % p == 0:
            residue //= p
            exponent += 1
        return (p, exponent) if residue == 1 else None
    return (q, 1) if independent_is_prime(q) else None


class EllipticSym5CollisionDiophantinePilotTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_sym5_factor_quotient_and_elimination_identities(self) -> None:
        for q in (1, 3, 5, 9, 31, 1_021):
            for t in range(-9, 10):
                self.assertEqual(subject.e5_trace(t, q), independent_e5(t, q))
                self.assertEqual(
                    subject.sym5_local_factor(t, q), independent_sym5_factor(t, q)
                )
            for x in range(-7, 8):
                for y in range(-7, 8):
                    quotient = subject.collision_quotient(x, y, q)
                    if x != y:
                        self.assertEqual(
                            subject.e5_trace(x, q) - subject.e5_trace(y, q),
                            (x - y) * quotient,
                        )
                    square, quartic = subject.elimination_pair(x, y, q)
                    self.assertEqual(square - quartic, 3 * quotient)

    def test_zero_fiber_classification_and_full_factor_sign_cases(self) -> None:
        for q in range(3, subject.MAX_Q + 1, 2):
            prime_power = independent_prime_power(q)
            if prime_power is None:
                continue
            p, exponent = prime_power
            bound = math.isqrt(4 * q)
            actual = {t for t in range(-bound, bound + 1) if independent_e5(t, q) == 0}
            expected = {0}
            if exponent % 2 == 0:
                root = p ** (exponent // 2)
                expected.update((-root, root))
            if p == 3 and exponent % 2 == 1:
                root = 3 ** ((exponent + 1) // 2)
                expected.update((-root, root))
            self.assertEqual(actual, expected, (q, prime_power))

        for q, t in ((9, 3), (25, 5), (81, 9)):
            positive = subject.sym5_local_factor(t, q)
            negative = subject.sym5_local_factor(-t, q)
            self.assertNotEqual(positive, negative)
            self.assertEqual(positive[2], negative[2])
            self.assertNotEqual(positive[3], negative[3])
            self.assertEqual(positive[3], 2 * q**7 * t)

        for q, t in ((3, 3), (27, 9), (243, 27)):
            self.assertEqual(t * t, 3 * q)
            self.assertEqual(
                subject.sym5_local_factor(t, q), subject.sym5_local_factor(-t, q)
            )
            self.assertNotEqual(
                subject.sym5_local_factor(0, q), subject.sym5_local_factor(t, q)
            )

    def test_weighted_scaling_and_prime_power_towers(self) -> None:
        bases = (
            (31, -7, 3),
            (1_021, -40, 19),
            (subject.LARGE_PRIME, -290_364_080, 756_187_719),
        )
        for q, x, y in bases:
            self.assertEqual(subject.collision_quotient(x, y, q), 0)
            self.assertNotEqual(
                subject.sym5_second_coefficient(x, q),
                subject.sym5_second_coefficient(y, q),
            )
            for d in (1, q):
                scaled_q = d * d * q
                self.assertEqual(
                    subject.collision_quotient(d * x, d * y, scaled_q),
                    d**4 * subject.collision_quotient(x, y, q),
                )
                self.assertEqual(
                    subject.e5_trace(d * x, scaled_q),
                    d**5 * subject.e5_trace(x, q),
                )
                self.assertEqual(
                    subject.sym5_second_coefficient(d * x, scaled_q),
                    d**10 * subject.sym5_second_coefficient(x, q),
                )
                self.assertEqual(scaled_q, q**3 if d == q else q)

    def test_discriminant_first_census_is_complete_through_2000(self) -> None:
        max_q = subject.MAX_Q
        trace_bound = math.isqrt(4 * max_q)
        independent_solutions: set[tuple[int, int, int]] = set()
        unordered_pairs = square_pairs = q_branches = 0
        for x in range(-trace_bound, trace_bound + 1):
            for y in range(x + 1, trace_bound + 1):
                unordered_pairs += 1
                quartic = (
                    x**4
                    + 5 * x**3 * y
                    + 9 * x * x * y * y
                    + 5 * x * y**3
                    + y**4
                )
                z = math.isqrt(quartic)
                if z * z != quartic:
                    continue
                square_pairs += 1
                h_value = x * x + x * y + y * y
                for signed_z in (-z, z):
                    q_branches += 1
                    numerator = 2 * h_value + signed_z
                    if numerator % 3:
                        continue
                    q = numerator // 3
                    if not 3 <= q <= max_q or q % 2 == 0:
                        continue
                    if x * x > 4 * q or y * y > 4 * q:
                        continue
                    if independent_prime_power(q) is None:
                        continue
                    if independent_e5(x, q) != independent_e5(y, q):
                        raise AssertionError("independent sieve admitted a false collision")
                    independent_solutions.add((q, x, y))

        census = self.fixture["finite_census"]
        stored_solutions = {
            (int(row["q"]), int(pair["x"]), int(pair["y"]))
            for row in census["rows"]
            for pair in row["pairs"]
        }
        self.assertEqual(stored_solutions, independent_solutions)
        self.assertEqual(unordered_pairs, 15_931)
        self.assertEqual(square_pairs, 295)
        self.assertEqual(q_branches, 590)
        self.assertEqual(len(independent_solutions), 61)
        self.assertEqual(census["q_with_collisions_count"], 21)
        self.assertEqual(
            census["class_counts"],
            {"general": 4, "sign_pair": 19, "zero_nonzero": 38},
        )
        self.assertEqual(census["full_local_factor_equal_pair_count"], 3)

        general = sorted(
            (q, x, y)
            for q, x, y in independent_solutions
            if x != -y and x != 0 and y != 0
        )
        self.assertEqual(
            general,
            [
                (31, -7, 3),
                (31, -3, 7),
                (1_021, -40, 19),
                (1_021, -19, 40),
            ],
        )

    def test_birational_map_and_exact_elliptic_sequence(self) -> None:
        expected = {
            2: ((Fraction(5), Fraction(-10)), (-7, 3, 19, 31)),
            3: (
                (Fraction(22, 49), Fraction(531, 343)),
                (-40, 19, -661, 1_021),
            ),
            4: (
                (Fraction(761, 400), Fraction(-5_491, 8_000)),
                (669, 91, 610_321, 547_921),
            ),
            5: (
                (Fraction(49_222, 49_729), Fraction(-1_949_259, 11_089_567)),
                (-23_541, 26_440, -618_264_781, 626_640_421),
            ),
            6: (
                (
                    Fraction(3_282_805, 1_535_121),
                    Fraction(2_654_992_430, 1_902_014_919),
                ),
                (-370_357, 3_646_273, 10_124_188_817_779, 11_429_428_518_271),
            ),
            7: (
                (
                    Fraction(9_557_518, 811_623_121),
                    Fraction(-51_336_505_396_347, 23_122_331_094_169),
                ),
                (
                    -290_364_080,
                    756_187_719,
                    -218_292_125_261_757_961,
                    subject.LARGE_PRIME,
                ),
            ),
        }
        rows = {
            int(row["multiple"]): row
            for row in self.fixture["elliptic_curve_bridge"]["multiples_2_through_7"]
        }
        self.assertEqual(set(rows), set(expected))
        for multiple, (point, integral) in expected.items():
            self.assertEqual(subject.elliptic_multiple(multiple), point)
            x_coordinate, y_coordinate = point
            self.assertEqual(
                y_coordinate * y_coordinate,
                x_coordinate**3 - 6 * x_coordinate + 5,
            )
            r, w = subject.inverse_elliptic_map(point)
            self.assertEqual(subject.forward_elliptic_map(r, w), point)
            x, y, z, q = integral
            self.assertEqual(r, Fraction(x, y))
            self.assertEqual(w, Fraction(z, x * y))
            self.assertEqual(z * z, subject.collision_quartic(x, y))
            self.assertEqual(subject.collision_quotient(x, y, q), 0)
            self.assertEqual(rows[multiple]["primitive_traces"], [x, y])
            self.assertEqual(rows[multiple]["q"], q)
            self.assertEqual(rows[multiple]["gcd_of_traces"], 1)
            self.assertTrue(rows[multiple]["both_traces_outside_scalar_zero_fiber"])
            self.assertEqual(rows[multiple]["first_separating_coefficient_degree"], 2)

        bridge = self.fixture["elliptic_curve_bridge"]
        self.assertEqual(independent_quartic_discriminant(1, 5, 9, 5, 1), 189)
        self.assertEqual(bridge["quartic_polynomial_discriminant"], 189)
        self.assertEqual(-16 * (4 * (-6) ** 3 + 27 * 5**2), 3_024)
        self.assertEqual(bridge["weierstrass_discriminant"], 3_024)
        for multiple in range(2, 13):
            point = subject.elliptic_multiple(multiple)
            if point is None or point[0] * point[0] == 4:
                continue
            r, w = subject.inverse_elliptic_map(point)
            u = r + 1 / r
            self.assertEqual(w * w, u * u + 5 * u + 7)
            self.assertEqual(subject.forward_elliptic_map(r, w), point)
        rank = bridge["infinite_order_certificate"]
        self.assertEqual(rank["two_Q"], [5, -10])
        self.assertEqual(rank["two_Q_y_squared"], 100)
        self.assertEqual(100 % rank["lutz_nagell_divisor_abs_4A3_plus_27B2"], 100)
        self.assertFalse(rank["divides"])

    def test_factorizations_and_large_prime_certificate_are_exact(self) -> None:
        sequence = self.fixture["elliptic_curve_bridge"]["multiples_2_through_7"]
        for row in sequence:
            factors = {int(p): int(e) for p, e in row["q_factorization"].items()}
            product = 1
            for prime, exponent in factors.items():
                if prime == subject.LARGE_PRIME:
                    self.assertTrue(subject.verify_large_prime_certificate())
                else:
                    self.assertTrue(independent_is_prime(prime))
                product *= prime**exponent
            self.assertEqual(product, row["q"])

        certificate = self.fixture["large_prime_certificate"]
        n = int(certificate["n"])
        factors = {
            int(prime): int(exponent)
            for prime, exponent in certificate["n_minus_one_factorization"].items()
        }
        self.assertEqual(
            math.prod(prime**exponent for prime, exponent in factors.items()), n - 1
        )
        for prime in factors:
            self.assertTrue(independent_is_prime(prime))
        witness = int(certificate["witness"])
        self.assertEqual(pow(witness, n - 1, n), 1)
        for prime in factors:
            self.assertEqual(
                math.gcd(pow(witness, (n - 1) // prime, n) - 1, n), 1
            )
        self.assertTrue(certificate["verified"])

    def test_prime_field_realization_boundary_and_factor_separation(self) -> None:
        boundary = self.fixture["prime_field_realization_boundary"]
        rows = boundary["realized_rows"]
        self.assertEqual(
            [row["q"] for row in rows], [31, 1_021, subject.LARGE_PRIME]
        )
        for row in rows:
            q = int(row["q"])
            self.assertTrue(row["hasse_admissible"])
            self.assertTrue(row["each_trace_coprime_to_q"])
            for trace in row["traces"]:
                self.assertLessEqual(int(trace) ** 2, 4 * q)
                self.assertEqual(math.gcd(abs(int(trace)), q), 1)

        # Waterhouse's five cases rule out every nonzero scaled trace in the
        # p^(2k+1), k>=1 towers for these p>3 prime bases.
        for row in rows:
            p = int(row["q"])
            self.assertGreater(p, 3)
            for k in range(1, 4):
                exponent = 2 * k + 1
                q = p**exponent
                for base_trace in row["traces"]:
                    trace = p**k * int(base_trace)
                    self.assertNotEqual(trace, 0)
                    self.assertEqual(trace % p, 0)  # not Waterhouse case (1)
                    self.assertEqual(exponent % 2, 1)  # not cases (2) or (3)
                    self.assertNotIn(p, (2, 3))  # not case (4)
                    self.assertLessEqual(trace * trace, 4 * q)
        self.assertIn(
            "not realized",
            boundary["weighted_odd_exponent_towers_beyond_the_prime_base"][
                "status"
            ],
        )

        # For q=p^(2k), Waterhouse cases (3) and (5) impose independent
        # congruence conditions on +/-sqrt(q) and 0 respectively.
        for p in (3, 5, 7, 11, 13, 17, 19):
            q = p**2
            root = p
            root_realized = p % 3 != 1
            zero_realized = p % 4 != 1
            self.assertEqual(root_realized, p % 3 in (0, 2))
            self.assertEqual(zero_realized, p % 4 in (0, 2, 3))
            self.assertEqual(independent_e5(root, q), 0)
            self.assertEqual(independent_e5(0, q), 0)

        sequence = {
            int(row["q"]): row
            for row in self.fixture["elliptic_curve_bridge"]["multiples_2_through_7"]
        }
        expected_differences = {
            31: 17_595_600,
            1_021: 1_000_879_891_757_823,
            subject.LARGE_PRIME: (
                -1_620_192_813_624_169_633_910_265_836_205_726_569_335_028_011_351_531_571_574_961_914_860_221_400_367_970_613_546_757
            ),
        }
        for q, expected_difference in expected_differences.items():
            left, right = sequence[q]["second_coefficients"]
            self.assertEqual(left - right, expected_difference)
            self.assertNotEqual(left, right)

    def test_source_lock_resources_firewalls_and_primary_boundaries(self) -> None:
        source = json.loads(subject.SOURCE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(source["schema"], subject.EXPECTED_SOURCE_SCHEMA)
        self.assertEqual(
            source["payload_sha256"], subject.EXPECTED_SOURCE_PAYLOAD_SHA256
        )
        unhashed = dict(source)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["new_curve_or_field_enumerations"], 0)
        self.assertEqual(resources["maximum_q_in_frozen_census"], 2_000)
        self.assertFalse(resources["larger_blind_search_performed_by_producer"])
        self.assertLess(
            resources["accounted_work_units"],
            resources["accounted_work_unit_cap_exclusive"],
        )
        self.assertEqual(resources["accounted_work_units"], 16_966)

        firewall = self.fixture["scope_firewall"]
        self.assertTrue(firewall["scalar_collision_is_not_full_factor_equality"])
        self.assertTrue(firewall["no_integral_point_classification"])
        self.assertTrue(firewall["no_claim_of_infinitely_many_prime_q"])
        self.assertTrue(firewall["no_global_compatible_family_or_euler_product_constructed"])
        self.assertTrue(
            firewall["weighted_prime_power_towers_are_not_curve_realization_towers"]
        )
        self.assertTrue(firewall["square_q_zero_fibers_are_not_automatically_realized"])
        self.assertTrue(firewall["project_relative_discovery_not_literature_priority"])
        references = self.fixture["literature_boundary"]["references"]
        self.assertEqual(
            [reference["url"] for reference in references],
            [
                "https://doi.org/10.1515/crll.1937.177.238",
                "https://numdam.org/articles/10.24033/asens.1183/",
            ],
        )
        self.assertIn("cases (1)-(5)", references[1]["use"])
        self.assertIn("nonrealization", references[1]["use"])

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for child in value.values():
                    reject_float(child)
            elif isinstance(value, list):
                for child in value:
                    reject_float(child)

        reject_float(self.fixture)

    def test_note_math_delimiters_controls_and_bytes_are_clean(self) -> None:
        note_path = (
            FUNCTION_FIELD / "ELLIPTIC_SYM5_COLLISION_DIOPHANTINE_PILOT.md"
        )
        raw = note_path.read_bytes()
        self.assertFalse(
            [byte for byte in raw if byte < 32 and byte not in (9, 10, 13)]
        )
        note = raw.decode("utf-8")
        self.assertFalse(
            [
                line_number
                for line_number, line in enumerate(note.splitlines(), start=1)
                if line.rstrip(" \t") != line
            ]
        )
        self.assertEqual(note.count(r"\["), note.count(r"\]"))
        self.assertEqual(note.count(r"\["), 18)
        self.assertNotIn(",quad", note)
        self.assertNotIn(",qquad", note)
        displays = re.findall(r"\\\[(.*?)\\\]", note, flags=re.DOTALL)
        self.assertEqual(len(displays), 18)
        for display in displays:
            for control_word in (
                "begin",
                "cdot",
                "end",
                "frac",
                "mathbin",
                "mathcal",
                "pm",
                "quad",
                "qquad",
                "sqrt",
                "text",
            ):
                self.assertIsNone(
                    re.search(rf"(?<!\\)\b{control_word}\b", display),
                    (control_word, display),
                )

    def test_stored_fixture_hashes_and_refusals_are_optimized_safe(self) -> None:
        stored_path = FUNCTION_FIELD / "elliptic_sym5_collision_diophantine_pilot.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        producer = self.fixture["producer"]
        for path, field in (
            (MODULE_PATH, "script_sha256_lf_normalized"),
            (
                FUNCTION_FIELD / "ELLIPTIC_SYM5_COLLISION_DIOPHANTINE_PILOT.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(producer[field], hashlib.sha256(normalized).hexdigest())

        with self.assertRaisesRegex(ValueError, "requires max_q=2000"):
            subject.build_fixture(1_999)
        with self.assertRaisesRegex(ValueError, "3..2000"):
            subject.discriminant_first_census(2_001)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.build_fixture(resource_cap=100)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.build_fixture(True)
        with self.assertRaisesRegex(TypeError, "integer"):
            subject.e5_trace(1, True)
        with self.assertRaisesRegex(ValueError, "positive and odd"):
            subject.e5_trace(1, 2)
        with self.assertRaisesRegex(ValueError, "exceptional"):
            subject.inverse_elliptic_map((Fraction(2), Fraction(1)))
        with self.assertRaisesRegex(ValueError, "r=0"):
            subject.forward_elliptic_map(Fraction(0), Fraction(1))


if __name__ == "__main__":
    unittest.main()
