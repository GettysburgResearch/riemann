"""Independent exact checks for the conductor-coprime twist-character pilot."""

from __future__ import annotations

import copy
import json
import math
import sys
import unittest
from fractions import Fraction
from functools import lru_cache
from math import gcd
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
ATLAS = REPO_ROOT / "research" / "l-families" / "atlas"
CORE = ATLAS / "core"
sys.path.insert(0, str(CORE))

import twist_character_covariance as subject  # noqa: E402
from atlas_core import read_json  # noqa: E402
from validate_atlas import SchemaStore, validate_instance  # noqa: E402


Q = Fraction
PRIMES = (2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43)
ODD_QUADRATIC_RESIDUES = {
    prime: frozenset(value * value % prime for value in range(1, prime))
    for prime in PRIMES
    if prime != 2
}
TRACES = {
    2: -2,
    3: -1,
    5: 1,
    7: -2,
    13: 4,
    17: -2,
    19: 0,
    23: -1,
    29: 0,
    31: 7,
    37: 3,
    41: -8,
    43: -6,
}
EXPECTED_PARTITIONS = {
    (256, "ALL"): (141, -255, 249),
    (256, "POSITIVE"): (69, 5, 249),
    (256, "NEGATIVE"): (72, -255, -3),
    (512, "ALL"): (285, -511, 509),
    (512, "POSITIVE"): (143, 5, 509),
    (512, "NEGATIVE"): (142, -511, -3),
    (1024, "ALL"): (570, -1019, 1021),
    (1024, "POSITIVE"): (283, 5, 1021),
    (1024, "NEGATIVE"): (287, -1019, -3),
    (2048, "ALL"): (1142, -2047, 2045),
    (2048, "POSITIVE"): (569, 5, 2045),
    (2048, "NEGATIVE"): (573, -2047, -3),
}


def independent_squarefree(value: int) -> bool:
    value = abs(value)
    if value == 0:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % (divisor * divisor) == 0:
            return False
        divisor += 1
    return True


def independent_fundamental(value: int) -> bool:
    if value == 0:
        return False
    if value % 4 == 1:
        return independent_squarefree(value)
    if value % 4 == 0:
        quotient = value // 4
        return quotient % 4 in {2, 3} and independent_squarefree(quotient)
    return False


def independent_character(discriminant: int, prime: int) -> int:
    """Kronecker symbol (d/p), using a residue-set check independent of Euler's criterion."""
    if prime == 2:
        if discriminant % 2 == 0:
            return 0
        return 1 if discriminant % 8 in {1, 7} else -1
    residue = discriminant % prime
    if residue == 0:
        return 0
    return 1 if residue in ODD_QUADRATIC_RESIDUES[prime] else -1


@lru_cache(maxsize=None)
def independent_family(bound: int) -> tuple[int, ...]:
    return tuple(
        value
        for value in range(-bound, bound + 1)
        if abs(value) > 1
        and gcd(value, 11) == 1
        and independent_fundamental(value)
    )


def fraction_value(record: dict[str, Any]) -> Fraction:
    return Q(record["numerator"], record["denominator"])


def partitions(bound: int) -> dict[str, list[int] | tuple[int, ...]]:
    family = independent_family(bound)
    return {
        "ALL": family,
        "POSITIVE": [value for value in family if value > 0],
        "NEGATIVE": [value for value in family if value < 0],
    }


@lru_cache(maxsize=1)
def generated_fixture() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    return subject.run(ATLAS)


def recursive_keys(value: Any) -> set[str]:
    if isinstance(value, dict):
        return set(value) | set().union(*(recursive_keys(child) for child in value.values()))
    if isinstance(value, list):
        return set().union(*(recursive_keys(child) for child in value))
    return set()


class ExactTwistFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.detector, cls.evaluation, cls.result = generated_fixture()
        cls.summary_by_key = {
            (summary["bound"], summary["partition"]): summary
            for summary in cls.result["summaries"]
        }
        cls.families = {
            (bound, name): values
            for bound in subject.BOUNDS
            for name, values in partitions(bound).items()
        }

    def assert_fraction_record(self, record: dict[str, Any], expected: Fraction) -> None:
        self.assertEqual(fraction_value(record), expected)
        self.assertGreater(record["denominator"], 0)
        self.assertEqual(gcd(abs(record["numerator"]), record["denominator"]), 1)
        self.assertEqual(record["text"], str(expected))


class FundamentalDiscriminantTests(ExactTwistFixture):
    def test_hostile_fundamental_discriminants(self) -> None:
        accepted = (-24, -11, -8, -7, -4, -3, 1, 5, 8, 12, 13, 17, 24)
        rejected = (-12, -5, -1, 0, 2, 3, 4, 9, 16, 20, 32)
        for value in accepted:
            with self.subTest(value=value):
                self.assertTrue(independent_fundamental(value))
                self.assertTrue(subject.is_fundamental_discriminant(value))
        for value in rejected:
            with self.subTest(value=value):
                self.assertFalse(independent_fundamental(value))
                self.assertFalse(subject.is_fundamental_discriminant(value))

        # One is a fundamental discriminant, but the declared nontrivial cohort excludes it.
        self.assertTrue(subject.is_fundamental_discriminant(1))
        self.assertNotIn(1, subject.fundamental_discriminants(13, 11))

    def test_conductor_coprime_cohort_is_deliberate(self) -> None:
        self.assertEqual(
            subject.fundamental_discriminants(13, 11),
            [-8, -7, -4, -3, 5, 8, 12, 13],
        )
        self.assertNotIn(-11, subject.fundamental_discriminants(13, 11))
        self.assertNotIn(44, subject.fundamental_discriminants(64, 11))
        family = independent_family(2048)
        unrestricted = [
            value
            for value in range(-2048, 2049)
            if abs(value) > 1 and independent_fundamental(value)
        ]
        self.assertEqual((len(family), len(unrestricted)), (1142, 1248))
        self.assertTrue(all(gcd(value, 11) == 1 for value in family))

    def test_invalid_enumeration_parameters_fail_closed(self) -> None:
        for bound, coprime_to in ((1, 11), (16, 0), (16, -11)):
            with self.subTest(bound=bound, coprime_to=coprime_to):
                with self.assertRaises(ValueError):
                    subject.fundamental_discriminants(bound, coprime_to)

    def test_prime_kronecker_hostile_cases_and_independent_replay(self) -> None:
        self.assertEqual(subject.kronecker_at_prime(5, 2), -1)
        self.assertEqual(subject.kronecker_at_prime(-7, 2), 1)
        self.assertEqual(subject.kronecker_at_prime(8, 2), 0)
        self.assertEqual(subject.kronecker_at_prime(5, 5), 0)
        self.assertEqual(subject.kronecker_at_prime(5, 3), -1)
        self.assertEqual(subject.kronecker_at_prime(13, 3), 1)
        self.assertEqual(subject.kronecker_at_prime(-4, 3), -1)
        for nonprime in (1, 4, 9):
            with self.subTest(nonprime=nonprime):
                with self.assertRaisesRegex(ValueError, "must be prime"):
                    subject.kronecker_at_prime(5, nonprime)
        for discriminant in independent_family(256):
            for prime in PRIMES:
                self.assertEqual(
                    subject.kronecker_at_prime(discriminant, prime),
                    independent_character(discriminant, prime),
                )


class CohortAndCorrelationTests(ExactTwistFixture):
    def test_exact_partition_counts_endpoints_and_prime_traces(self) -> None:
        self.assertEqual(self.result["bounds"], list(subject.BOUNDS))
        self.assertEqual(self.result["primes"], list(PRIMES))
        self.assertEqual(self.result["traces"], [TRACES[prime] for prime in PRIMES])
        self.assertEqual(set(self.summary_by_key), set(EXPECTED_PARTITIONS))
        for key, expected in EXPECTED_PARTITIONS.items():
            with self.subTest(key=key):
                summary = self.summary_by_key[key]
                family = self.families[key]
                self.assertEqual(
                    (
                        summary["discriminant_count"],
                        summary["first_discriminant"],
                        summary["last_discriminant"],
                    ),
                    expected,
                )
                self.assertEqual((len(family), family[0], family[-1]), expected)

    def test_omitted_marginals_reconstruct_from_sums_and_gram_diagonal(self) -> None:
        for key, summary in self.summary_by_key.items():
            discriminants = self.families[key]
            count = len(discriminants)
            raw_diagonal = summary["correlation_matrices"]["raw_gram"]["numerators"]
            self.assertEqual(len(summary["character_sums"]), len(PRIMES))
            for index, prime in enumerate(PRIMES):
                values = [independent_character(value, prime) for value in discriminants]
                negative = values.count(-1)
                zero = values.count(0)
                positive = values.count(1)
                signed_sum = summary["character_sums"][index]
                nonzero_count = raw_diagonal[index][index]
                reconstructed_positive = (nonzero_count + signed_sum) // 2
                reconstructed_negative = (nonzero_count - signed_sum) // 2
                reconstructed_zero = count - nonzero_count
                self.assertEqual(
                    (reconstructed_negative, reconstructed_zero, reconstructed_positive),
                    (negative, zero, positive),
                )
                self.assertEqual(signed_sum, positive - negative)
                self.assertEqual(nonzero_count, positive + negative)
                mean = Q(signed_sum, count)
                density = Q(nonzero_count, count)
                target = Q(prime, prime + 1)
                self.assertEqual(mean, Q(sum(values), count))
                self.assertEqual(density, Q(sum(value * value for value in values), count))
                self.assertEqual(density - target, Q(nonzero_count, count) - target)

    def test_compact_gram_covariance_matrices_and_summaries_replay(self) -> None:
        for key, summary in self.summary_by_key.items():
            discriminants = self.families[key]
            count = len(discriminants)
            characters = {
                prime: [independent_character(value, prime) for value in discriminants]
                for prime in PRIMES
            }
            means = {prime: Q(sum(characters[prime]), count) for prime in PRIMES}
            character_sums = {prime: sum(characters[prime]) for prime in PRIMES}
            expected_raw_numerators = [
                [
                    sum(
                        left * right
                        for left, right in zip(
                            characters[prime], characters[other_prime], strict=True
                        )
                    )
                    for other_prime in PRIMES
                ]
                for prime in PRIMES
            ]
            expected_centered_numerators = [
                [
                    count * expected_raw_numerators[row_index][column_index]
                    - character_sums[prime] * character_sums[other_prime]
                    for column_index, other_prime in enumerate(PRIMES)
                ]
                for row_index, prime in enumerate(PRIMES)
            ]
            matrices = summary["correlation_matrices"]
            self.assertEqual(
                summary["character_sums"],
                [character_sums[prime] for prime in PRIMES],
            )
            self.assertEqual(matrices["raw_gram"]["denominator"], count)
            self.assertEqual(
                matrices["raw_gram"]["numerators"], expected_raw_numerators
            )
            self.assertEqual(
                matrices["centered_covariance"]["denominator"], count * count
            )
            self.assertEqual(
                matrices["centered_covariance"]["numerators"],
                expected_centered_numerators,
            )

            expected_pairs: list[tuple[Fraction, int, int, Fraction, Fraction]] = []
            for index, prime in enumerate(PRIMES):
                for other_index, other_prime in enumerate(PRIMES[index + 1 :], index + 1):
                    raw = Q(expected_raw_numerators[index][other_index], count)
                    centered = Q(
                        expected_centered_numerators[index][other_index], count * count
                    )
                    expected_pairs.append((abs(raw), prime, other_prime, raw, centered))

            # Both matrices are exact symmetric Gram matrices. Their diagonals encode
            # local density and centered variance, not an assumed unit diagonal.
            for index, prime in enumerate(PRIMES):
                signed_sum = summary["character_sums"][index]
                density = Q(expected_raw_numerators[index][index], count)
                mean = Q(signed_sum, count)
                self.assertEqual(
                    density,
                    Q(sum(value * value for value in characters[prime]), count),
                )
                self.assertEqual(
                    Q(expected_centered_numerators[index][index], count * count),
                    density - mean * mean,
                )
                for other_index in range(len(PRIMES)):
                    self.assertEqual(
                        expected_raw_numerators[index][other_index],
                        expected_raw_numerators[other_index][index],
                    )
                    self.assertEqual(
                        expected_centered_numerators[index][other_index],
                        expected_centered_numerators[other_index][index],
                    )

            off_diagonal = summary["off_diagonal"]
            self.assertEqual(off_diagonal["pair_count"], 78)
            maximum_raw = max(expected_pairs, key=lambda item: (item[0], item[1], item[2], item[3]))
            maximum_centered = max(
                expected_pairs,
                key=lambda item: (abs(item[4]), item[1], item[2], item[4]),
            )
            for field, maximum, value_index in (
                ("max_absolute_raw", maximum_raw, 3),
                ("max_absolute_centered", maximum_centered, 4),
            ):
                record = off_diagonal[field]
                self.assertEqual((record["p"], record["q"]), (maximum[1], maximum[2]))
                self.assert_fraction_record(record["value"], maximum[value_index])
                self.assert_fraction_record(record["absolute_value"], abs(maximum[value_index]))
            mean_square_raw = sum((item[3] ** 2 for item in expected_pairs), Q()) / 78
            mean_square_centered = sum((item[4] ** 2 for item in expected_pairs), Q()) / 78
            self.assert_fraction_record(off_diagonal["mean_square_raw"], mean_square_raw)
            self.assert_fraction_record(
                off_diagonal["mean_square_centered"], mean_square_centered
            )

        control = self.summary_by_key[(1024, "ALL")]
        self.assertEqual(
            (
                control["off_diagonal"]["max_absolute_raw"]["p"],
                control["off_diagonal"]["max_absolute_raw"]["q"],
                control["off_diagonal"]["max_absolute_raw"]["value"]["text"],
            ),
            (13, 37, "-7/95"),
        )

    def test_all_partition_is_exact_weighted_union(self) -> None:
        for bound in subject.BOUNDS:
            all_summary = self.summary_by_key[(bound, "ALL")]
            positive = self.summary_by_key[(bound, "POSITIVE")]
            negative = self.summary_by_key[(bound, "NEGATIVE")]
            all_count = all_summary["discriminant_count"]
            positive_count = positive["discriminant_count"]
            negative_count = negative["discriminant_count"]
            self.assertEqual(all_count, positive_count + negative_count)

            self.assertEqual(
                all_summary["character_sums"],
                [
                    positive_value + negative_value
                    for positive_value, negative_value in zip(
                        positive["character_sums"], negative["character_sums"], strict=True
                    )
                ],
            )

            all_matrix = all_summary["correlation_matrices"]["raw_gram"]
            positive_matrix = positive["correlation_matrices"]["raw_gram"]
            negative_matrix = negative["correlation_matrices"]["raw_gram"]
            self.assertEqual(all_matrix["denominator"], all_count)
            self.assertEqual(positive_matrix["denominator"], positive_count)
            self.assertEqual(negative_matrix["denominator"], negative_count)
            for row_index in range(len(PRIMES)):
                for column_index in range(len(PRIMES)):
                    # Common-denominator numerators are unnormalized character sums,
                    # so the ALL numerator is literally the sum of the sign strata.
                    self.assertEqual(
                        all_matrix["numerators"][row_index][column_index],
                        positive_matrix["numerators"][row_index][column_index]
                        + negative_matrix["numerators"][row_index][column_index],
                    )


class RadicalMomentTests(ExactTwistFixture):
    def test_every_omitted_multiquadratic_coordinate_reconstructs_exactly(self) -> None:
        self.assertEqual(self.result["exact_coordinate_formulas"], subject.COORDINATE_FORMULAS)
        self.assertIn(
            "reconstruct every exact multiquadratic",
            self.result["exact_coordinate_formulas"]["reconstruction"],
        )
        for key, summary in self.summary_by_key.items():
            discriminants = self.families[key]
            count = len(discriminants)
            characters = {
                prime: [independent_character(value, prime) for value in discriminants]
                for prime in PRIMES
            }
            means = {prime: Q(sum(characters[prime]), count) for prime in PRIMES}
            densities = {
                prime: Q(sum(value * value for value in characters[prime]), count)
                for prime in PRIMES
            }
            sums = summary["character_sums"]
            raw = summary["correlation_matrices"]["raw_gram"]
            centered = summary["correlation_matrices"]["centered_covariance"]
            moment = summary["unitary_prime_sum"]

            reconstructed_mean = {
                prime: Q(TRACES[prime] * sums[index], count * prime)
                for index, prime in enumerate(PRIMES)
                if TRACES[prime] * sums[index]
            }
            direct_mean = {
                prime: Q(
                    sum(TRACES[prime] * value for value in characters[prime]),
                    count * prime,
                )
                for prime in PRIMES
                if TRACES[prime] * sum(characters[prime])
            }
            self.assertEqual(reconstructed_mean, direct_mean)

            reconstructed_second_diagonal = sum(
                (
                    Q(
                        TRACES[prime] ** 2 * raw["numerators"][index][index],
                        raw["denominator"] * prime,
                    )
                    for index, prime in enumerate(PRIMES)
                ),
                Q(),
            )
            reconstructed_variance_diagonal = sum(
                (
                    Q(
                        TRACES[prime] ** 2
                        * centered["numerators"][index][index],
                        centered["denominator"] * prime,
                    )
                    for index, prime in enumerate(PRIMES)
                ),
                Q(),
            )
            direct_second_diagonal = sum(
                (Q(TRACES[prime] ** 2, prime) * densities[prime] for prime in PRIMES),
                Q(),
            )
            direct_variance_diagonal = sum(
                (
                    Q(TRACES[prime] ** 2, prime)
                    * (densities[prime] - means[prime] ** 2)
                    for prime in PRIMES
                ),
                Q(),
            )
            self.assertEqual(reconstructed_second_diagonal, direct_second_diagonal)
            self.assertEqual(reconstructed_variance_diagonal, direct_variance_diagonal)
            self.assert_fraction_record(
                moment["second_moment_diagonal_rational"],
                reconstructed_second_diagonal,
            )
            self.assert_fraction_record(
                moment["centered_variance_diagonal_rational"],
                reconstructed_variance_diagonal,
            )

            reconstructed_second: dict[int, Fraction] = {}
            reconstructed_variance: dict[int, Fraction] = {}
            direct_second: dict[int, Fraction] = {}
            direct_variance: dict[int, Fraction] = {}
            for index, prime in enumerate(PRIMES):
                for other_index, other_prime in enumerate(PRIMES[index + 1 :], index + 1):
                    scale = Q(
                        2 * TRACES[prime] * TRACES[other_prime],
                        prime * other_prime,
                    )
                    raw_direct = Q(
                        sum(
                            left * right
                            for left, right in zip(
                                characters[prime], characters[other_prime], strict=True
                            )
                        ),
                        count,
                    )
                    centered_direct = raw_direct - means[prime] * means[other_prime]
                    raw_from_matrix = Q(
                        raw["numerators"][index][other_index], raw["denominator"]
                    )
                    centered_from_matrix = Q(
                        centered["numerators"][index][other_index],
                        centered["denominator"],
                    )
                    radicand = prime * other_prime
                    if scale * raw_from_matrix:
                        reconstructed_second[radicand] = scale * raw_from_matrix
                    if scale * centered_from_matrix:
                        reconstructed_variance[radicand] = scale * centered_from_matrix
                    if scale * raw_direct:
                        direct_second[radicand] = scale * raw_direct
                    if scale * centered_direct:
                        direct_variance[radicand] = scale * centered_direct

            self.assertEqual(reconstructed_second, direct_second)
            self.assertEqual(reconstructed_variance, direct_variance)
            self.assertTrue(
                all(radicand % 19 and radicand % 29 for radicand in reconstructed_second)
            )
            self.assertTrue(
                all(radicand % 19 and radicand % 29 for radicand in reconstructed_variance)
            )

            second_decimal = float(reconstructed_second_diagonal) + sum(
                coefficient.numerator / coefficient.denominator * math.sqrt(radicand)
                for radicand, coefficient in reconstructed_second.items()
            )
            variance_decimal = float(reconstructed_variance_diagonal) + sum(
                coefficient.numerator / coefficient.denominator * math.sqrt(radicand)
                for radicand, coefficient in reconstructed_variance.items()
            )
            mean_decimal = sum(
                coefficient.numerator / coefficient.denominator * math.sqrt(radicand)
                for radicand, coefficient in reconstructed_mean.items()
            )
            self.assertEqual(
                moment["mean_decimal_display_only"], format(mean_decimal, ".12g")
            )
            self.assertEqual(
                moment["second_moment_decimal_display_only"],
                format(second_decimal, ".12g"),
            )
            self.assertEqual(
                moment["centered_variance_decimal_display_only"],
                format(variance_decimal, ".12g"),
            )

            # Coordinatewise Var(W)=E(W^2)-E(W)^2 in the multiquadratic basis.
            self.assertEqual(
                reconstructed_second_diagonal - reconstructed_variance_diagonal,
                sum(
                    (Q(TRACES[p] ** 2, p) * means[p] ** 2 for p in PRIMES),
                    Q(),
                ),
            )
            for index, prime in enumerate(PRIMES):
                for other_prime in PRIMES[index + 1 :]:
                    radicand = prime * other_prime
                    difference = reconstructed_second.get(
                        radicand, Q()
                    ) - reconstructed_variance.get(radicand, Q())
                    self.assertEqual(
                        difference,
                        Q(
                            2 * TRACES[prime] * TRACES[other_prime],
                            prime * other_prime,
                        )
                        * means[prime]
                        * means[other_prime],
                    )

        control = self.summary_by_key[(1024, "ALL")]["unitary_prime_sum"]
        self.assertEqual(control["mean_decimal_display_only"], "0.0813677515253")
        self.assertEqual(control["second_moment_decimal_display_only"], "7.61946775764")
        self.assertEqual(control["centered_variance_decimal_display_only"], "7.61284704665")


class SchemaAndFirewallTests(ExactTwistFixture):
    def test_generated_result_satisfies_raw_schema(self) -> None:
        schema_path = ATLAS / "detectors" / "raw-schemas" / "twist-character-covariance-result.schema.json"
        store = SchemaStore()
        errors = validate_instance(
            self.result,
            store.load(schema_path),
            schema_path,
            store,
        )
        self.assertEqual(errors, [])

        mutated = copy.deepcopy(self.result)
        mutated["root_number"] = "+1"
        errors = validate_instance(mutated, store.load(schema_path), schema_path, store)
        self.assertTrue(any("unexpected property 'root_number'" in error for error in errors))

        mutated = copy.deepcopy(self.result)
        mutated["summaries"][0]["partition"] = "ROOT_NUMBER_PLUS"
        errors = validate_instance(mutated, store.load(schema_path), schema_path, store)
        self.assertTrue(any("not in enum" in error for error in errors))

        pretty_size = len(
            (json.dumps(self.result, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        )
        self.assertLess(pretty_size, 150_000)
        self.assertNotIn("character_rows", recursive_keys(self.result))
        self.assertNotIn("radical_terms", recursive_keys(self.result))
        self.assertNotIn("off_diagonal_radicals", recursive_keys(self.result))

    def test_every_fraction_record_is_reduced_and_text_consistent(self) -> None:
        records: list[dict[str, Any]] = []

        def visit(value: Any) -> None:
            if isinstance(value, dict):
                if set(value) == {"numerator", "denominator", "text"}:
                    records.append(value)
                for child in value.values():
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)

        visit(self.result)
        self.assertGreater(len(records), 50)
        for record in records:
            self.assert_fraction_record(record, fraction_value(record))

    def test_no_root_number_or_zero_data_leaks_into_finite_character_result(self) -> None:
        forbidden_keys = {
            "root_number",
            "epsilon",
            "analytic_rank",
            "central_rank",
            "zero_ordinates",
        }
        for record in (self.result, self.detector, self.evaluation):
            self.assertTrue(forbidden_keys.isdisjoint(recursive_keys(record)))

        self.assertIn("gcd(d,11)=1", self.result["family_definition"])
        self.assertIn("no root-number split", self.result["family_definition"])
        self.assertEqual(
            self.result["family"],
            {
                "parameter": "fundamental_discriminant",
                "absolute_value_minimum_exclusive": 1,
                "absolute_value_bounds": [256, 512, 1024, 2048],
                "coprime_to": 11,
                "measure": "UNIFORM",
                "partitions": ["ALL", "POSITIVE", "NEGATIVE"],
                "root_number_partition": "NONE",
            },
        )
        self.assertEqual(
            {summary["partition"] for summary in self.result["summaries"]},
            {"ALL", "POSITIVE", "NEGATIVE"},
        )
        self.assertIn(
            "NO_ROOT_SPLIT",
            {firewall["code"] for firewall in self.evaluation["firewalls"]},
        )
        root_split_adapter = next(
            adapter
            for adapter in self.detector["family_adapters"]
            if adapter["family"] == "EC11A2_ROOT_NUMBER_SPLIT"
        )
        self.assertEqual(root_split_adapter["status"], "REQUIRED_OPEN")
        self.assertIsNone(root_split_adapter["adapter_path"])

    def test_result_rebuild_is_deterministic(self) -> None:
        source_manifest = read_json(ATLAS / "sources" / "lmfdb-curves.json")
        self.assertEqual(subject.build_result(source_manifest), self.result)


if __name__ == "__main__":
    unittest.main()
