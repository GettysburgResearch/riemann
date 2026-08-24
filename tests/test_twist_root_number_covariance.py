"""Independent checks for the conductor-coprime 11.a2 root-number split."""

from __future__ import annotations

import copy
import io
import math
import sys
import unittest
from contextlib import redirect_stdout
from fractions import Fraction
from functools import lru_cache
from math import gcd
from pathlib import Path
from typing import Any
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
ATLAS = REPO_ROOT / "research" / "l-families" / "atlas"
CORE = ATLAS / "core"
sys.path.insert(0, str(CORE))

import twist_character_covariance as shared  # noqa: E402
import twist_root_number_covariance as subject  # noqa: E402
from atlas_core import read_json, semantic_identity, sha256_hex  # noqa: E402
from validate_atlas import SchemaStore, validate_instance  # noqa: E402


Q = Fraction
PRIMES = (2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43)
TRACES = (-2, -1, 1, -2, 4, -2, 0, -1, 0, 7, 3, -8, -6)
ODD_RESIDUES = {
    prime: frozenset(value * value % prime for value in range(1, prime))
    for prime in (*PRIMES, 11)
    if prime != 2
}
EXPECTED = {
    (256, "ROOT_NUMBER_PLUS"): (65, -251, 236),
    (256, "ROOT_NUMBER_MINUS"): (76, -255, 249),
    (512, "ROOT_NUMBER_PLUS"): (140, -511, 509),
    (512, "ROOT_NUMBER_MINUS"): (145, -503, 508),
    (1024, "ROOT_NUMBER_PLUS"): (281, -1016, 1021),
    (1024, "ROOT_NUMBER_MINUS"): (289, -1019, 1020),
    (2048, "ROOT_NUMBER_PLUS"): (568, -2047, 2044),
    (2048, "ROOT_NUMBER_MINUS"): (574, -2031, 2045),
}
EXPECTED_GRAM_CONTRASTS = {
    256: {
        "pair": (37, 41),
        "signed": Q(-83, 247),
        "mean_square": Q(22556369, 1903480800),
        "rms": "0.108858",
        "scaled_rms": "1.292617",
    },
    512: {
        "pair": (29, 41),
        "signed": Q(156, 1015),
        "mean_square": Q(398459, 91837200),
        "rms": "0.065869",
        "scaled_rms": "1.112000",
    },
    1024: {
        "pair": (7, 31),
        "signed": Q(9594, 81209),
        "mean_square": Q(815350219, 257201165559),
        "rms": "0.056304",
        "scaled_rms": "1.344228",
    },
    2048: {
        "pair": (5, 31),
        "signed": Q(3713, 40754),
        "mean_square": Q(3293698081, 2072788867968),
        "rms": "0.039862",
        "scaled_rms": "1.347092",
    },
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
    if prime == 2:
        if discriminant % 2 == 0:
            return 0
        return 1 if discriminant % 8 in {1, 7} else -1
    residue = discriminant % prime
    if residue == 0:
        return 0
    return 1 if residue in ODD_RESIDUES[prime] else -1


def independent_root_number(discriminant: int) -> int:
    if not independent_fundamental(discriminant) or gcd(discriminant, 11) != 1:
        raise ValueError("outside the independently replayed theorem domain")
    return (1 if discriminant > 0 else -1) * independent_character(discriminant, 11)


@lru_cache(maxsize=None)
def independent_family(bound: int) -> tuple[int, ...]:
    return tuple(
        value
        for value in range(-bound, bound + 1)
        if abs(value) > 1
        and gcd(value, 11) == 1
        and independent_fundamental(value)
    )


@lru_cache(maxsize=None)
def independent_partition(bound: int, partition: str) -> tuple[int, ...]:
    target = 1 if partition == "ROOT_NUMBER_PLUS" else -1
    return tuple(
        value
        for value in independent_family(bound)
        if independent_root_number(value) == target
    )


def fraction_value(record: dict[str, Any]) -> Fraction:
    return Q(record["numerator"], record["denominator"])


def recursive_keys(value: Any) -> set[str]:
    if isinstance(value, dict):
        return set(value) | set().union(*(recursive_keys(child) for child in value.values()))
    if isinstance(value, list):
        return set().union(*(recursive_keys(child) for child in value))
    return set()


@lru_cache(maxsize=1)
def generated_fixture() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    return subject.run(ATLAS)


class RootNumberFixture(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.spec, cls.detector, cls.evaluation, cls.result = generated_fixture()
        cls.summary_by_key = {
            (summary["bound"], summary["partition"]): summary
            for summary in cls.result["summaries"]
        }


class SignFormulaTests(RootNumberFixture):
    def test_hostile_sign_and_residue_cases(self) -> None:
        cases = {
            5: 1,
            8: -1,
            12: 1,
            -3: 1,
            -4: 1,
            -7: -1,
            -8: -1,
        }
        for discriminant, expected in cases.items():
            with self.subTest(discriminant=discriminant):
                self.assertEqual(subject.root_number_for_discriminant(discriminant), expected)
                self.assertEqual(independent_root_number(discriminant), expected)

        for excluded in (-11, 44, 3, 9, 0):
            with self.subTest(excluded=excluded):
                with self.assertRaises(ValueError):
                    subject.root_number_for_discriminant(excluded)

    def test_every_emitted_member_matches_independent_formula(self) -> None:
        family = independent_family(2048)
        observed = {
            sign: tuple(subject.root_number_partitions(2048)[sign])
            for sign in subject.PARTITIONS
        }
        self.assertEqual(
            observed["ROOT_NUMBER_PLUS"],
            independent_partition(2048, "ROOT_NUMBER_PLUS"),
        )
        self.assertEqual(
            observed["ROOT_NUMBER_MINUS"],
            independent_partition(2048, "ROOT_NUMBER_MINUS"),
        )
        self.assertEqual(
            sorted(observed["ROOT_NUMBER_PLUS"] + observed["ROOT_NUMBER_MINUS"]),
            list(family),
        )
        self.assertTrue(all(gcd(value, 11) == 1 for value in family))

    def test_exact_frozen_counts_endpoints_and_order(self) -> None:
        expected_order = [
            (bound, partition)
            for bound in subject.BOUNDS
            for partition in subject.PARTITIONS
        ]
        self.assertEqual(
            [(row["bound"], row["partition"]) for row in self.result["summaries"]],
            expected_order,
        )
        self.assertEqual(set(self.summary_by_key), set(EXPECTED))
        for key, expected in EXPECTED.items():
            family = independent_partition(*key)
            self.assertEqual((len(family), family[0], family[-1]), expected)
            summary = self.summary_by_key[key]
            self.assertEqual(
                (
                    summary["discriminant_count"],
                    summary["first_discriminant"],
                    summary["last_discriminant"],
                ),
                expected,
            )
        self.assertEqual(
            self.result["cohort_counts"],
            [
                {"bound": 256, "ROOT_NUMBER_PLUS": 65, "ROOT_NUMBER_MINUS": 76, "total": 141},
                {"bound": 512, "ROOT_NUMBER_PLUS": 140, "ROOT_NUMBER_MINUS": 145, "total": 285},
                {"bound": 1024, "ROOT_NUMBER_PLUS": 281, "ROOT_NUMBER_MINUS": 289, "total": 570},
                {"bound": 2048, "ROOT_NUMBER_PLUS": 568, "ROOT_NUMBER_MINUS": 574, "total": 1142},
            ],
        )


class IndependentCovarianceReplayTests(RootNumberFixture):
    def test_shared_summarizer_is_reused_without_a_shadow_copy(self) -> None:
        self.assertIs(subject.summarize_partition, shared.summarize_partition)
        self.assertEqual(tuple(self.result["primes"]), PRIMES)
        self.assertEqual(tuple(self.result["traces"]), TRACES)

    def test_all_sufficient_statistics_and_moment_displays_replay(self) -> None:
        for key, summary in self.summary_by_key.items():
            discriminants = independent_partition(*key)
            count = len(discriminants)
            columns = [
                [independent_character(discriminant, prime) for discriminant in discriminants]
                for prime in PRIMES
            ]
            sums = [sum(column) for column in columns]
            raw = [
                [
                    sum(left * right for left, right in zip(columns[i], columns[j], strict=True))
                    for j in range(len(PRIMES))
                ]
                for i in range(len(PRIMES))
            ]
            centered = [
                [count * raw[i][j] - sums[i] * sums[j] for j in range(len(PRIMES))]
                for i in range(len(PRIMES))
            ]
            self.assertEqual(summary["character_sums"], sums)
            self.assertEqual(
                summary["correlation_matrices"]["raw_gram"],
                {"denominator": count, "numerators": raw},
            )
            self.assertEqual(
                summary["correlation_matrices"]["centered_covariance"],
                {"denominator": count * count, "numerators": centered},
            )

            second_diagonal = sum(
                (Q(trace * trace * raw[i][i], count * prime) for i, (prime, trace) in enumerate(zip(PRIMES, TRACES, strict=True))),
                Q(),
            )
            variance_diagonal = sum(
                (Q(trace * trace * centered[i][i], count * count * prime) for i, (prime, trace) in enumerate(zip(PRIMES, TRACES, strict=True))),
                Q(),
            )
            moment = summary["unitary_prime_sum"]
            self.assertEqual(
                fraction_value(moment["second_moment_diagonal_rational"]),
                second_diagonal,
            )
            self.assertEqual(
                fraction_value(moment["centered_variance_diagonal_rational"]),
                variance_diagonal,
            )

            mean_decimal = sum(
                trace * sums[i] / (count * math.sqrt(prime))
                for i, (prime, trace) in enumerate(zip(PRIMES, TRACES, strict=True))
            )
            second_decimal = float(second_diagonal)
            variance_decimal = float(variance_diagonal)
            for i, (prime, trace) in enumerate(zip(PRIMES, TRACES, strict=True)):
                for j in range(i + 1, len(PRIMES)):
                    other_prime = PRIMES[j]
                    other_trace = TRACES[j]
                    second_decimal += (
                        2
                        * trace
                        * other_trace
                        * raw[i][j]
                        / (count * math.sqrt(prime * other_prime))
                    )
                    variance_decimal += (
                        2
                        * trace
                        * other_trace
                        * centered[i][j]
                        / (count * count * math.sqrt(prime * other_prime))
                    )
            self.assertEqual(moment["mean_decimal_display_only"], format(mean_decimal, ".12g"))
            self.assertEqual(
                moment["second_moment_decimal_display_only"],
                format(second_decimal, ".12g"),
            )
            self.assertEqual(
                moment["centered_variance_decimal_display_only"],
                format(variance_decimal, ".12g"),
            )

    def test_exact_root_cohort_gram_contrasts_replay_from_aligned_stats(self) -> None:
        certificate = self.result["root_cohort_gram_contrast"]
        self.assertEqual(certificate["pair_count"], 78)
        self.assertIn("emitted", certificate["source"])
        self.assertIn("not a fitted", certificate["firewall"])
        rows = {row["bound"]: row for row in certificate["summaries"]}
        self.assertEqual(list(row["bound"] for row in certificate["summaries"]), list(subject.BOUNDS))
        self.assertEqual(set(rows), set(EXPECTED_GRAM_CONTRASTS))
        for bound, expected in EXPECTED_GRAM_CONTRASTS.items():
            plus = self.summary_by_key[(bound, "ROOT_NUMBER_PLUS")]
            minus = self.summary_by_key[(bound, "ROOT_NUMBER_MINUS")]
            plus_raw = plus["correlation_matrices"]["raw_gram"]
            minus_raw = minus["correlation_matrices"]["raw_gram"]
            contrasts = []
            for left_index, left_prime in enumerate(PRIMES):
                for right_index in range(left_index + 1, len(PRIMES)):
                    value = Q(
                        plus_raw["numerators"][left_index][right_index],
                        plus_raw["denominator"],
                    ) - Q(
                        minus_raw["numerators"][left_index][right_index],
                        minus_raw["denominator"],
                    )
                    contrasts.append((left_prime, PRIMES[right_index], value))
            self.assertEqual(len(contrasts), 78)
            maximum = max(contrasts, key=lambda entry: abs(entry[2]))
            mean_square = sum((entry[2] ** 2 for entry in contrasts), Q()) / 78
            self.assertEqual((maximum[0], maximum[1]), expected["pair"])
            self.assertEqual(maximum[2], expected["signed"])
            self.assertEqual(mean_square, expected["mean_square"])

            row = rows[bound]
            maximum_record = row["maximum_absolute"]
            self.assertEqual((maximum_record["p"], maximum_record["r"]), expected["pair"])
            self.assertEqual(fraction_value(maximum_record["signed_value"]), expected["signed"])
            self.assertEqual(
                fraction_value(maximum_record["absolute_value"]), abs(expected["signed"])
            )
            self.assertEqual(fraction_value(row["mean_square"]), expected["mean_square"])
            self.assertEqual(row["rms_decimal_display_only"], expected["rms"])
            self.assertEqual(
                row["sqrt_total_count_times_rms_decimal_display_only"],
                expected["scaled_rms"],
            )
            total = plus["discriminant_count"] + minus["discriminant_count"]
            self.assertEqual(row["total_discriminant_count"], total)
            self.assertEqual(
                subject._sqrt_decimal_display(mean_square), expected["rms"]
            )
            self.assertEqual(
                subject._sqrt_decimal_display(total * mean_square),
                expected["scaled_rms"],
            )

    def test_exact_square_root_display_hostile_controls(self) -> None:
        self.assertEqual(subject._sqrt_decimal_display(Q()), "0.000000")
        self.assertEqual(subject._sqrt_decimal_display(Q(1, 4)), "0.500000")
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject._sqrt_decimal_display(Q(-1, 4))
        with self.assertRaisesRegex(ValueError, "digits"):
            subject._sqrt_decimal_display(Q(1), -1)

    def test_two_root_cohorts_pool_back_to_unconditioned_packet(self) -> None:
        _detector, _evaluation, unconditioned = shared.run(ATLAS)
        all_by_bound = {
            summary["bound"]: summary
            for summary in unconditioned["summaries"]
            if summary["partition"] == "ALL"
        }
        for bound in subject.BOUNDS:
            plus = self.summary_by_key[(bound, "ROOT_NUMBER_PLUS")]
            minus = self.summary_by_key[(bound, "ROOT_NUMBER_MINUS")]
            pooled = all_by_bound[bound]
            count = plus["discriminant_count"] + minus["discriminant_count"]
            sums = [
                left + right
                for left, right in zip(
                    plus["character_sums"], minus["character_sums"], strict=True
                )
            ]
            plus_raw = plus["correlation_matrices"]["raw_gram"]["numerators"]
            minus_raw = minus["correlation_matrices"]["raw_gram"]["numerators"]
            raw = [
                [
                    plus_raw[row][column] + minus_raw[row][column]
                    for column in range(len(PRIMES))
                ]
                for row in range(len(PRIMES))
            ]
            centered = [
                [count * raw[row][column] - sums[row] * sums[column] for column in range(len(PRIMES))]
                for row in range(len(PRIMES))
            ]
            self.assertEqual(pooled["discriminant_count"], count)
            self.assertEqual(pooled["character_sums"], sums)
            self.assertEqual(
                pooled["correlation_matrices"]["raw_gram"],
                {"denominator": count, "numerators": raw},
            )
            self.assertEqual(
                pooled["correlation_matrices"]["centered_covariance"],
                {"denominator": count * count, "numerators": centered},
            )


class ProvenanceAndSchemaTests(RootNumberFixture):
    def test_source_manifest_pins_theorem_normalization_and_negative_d(self) -> None:
        manifest = read_json(ATLAS / "sources" / "quadratic-twist-root-number.json")
        by_key = {source["key"]: source for source in manifest["sources"]}
        self.assertIn("Proposition 10", by_key["ROHRLICH_1996"]["pinpoint"])
        self.assertIn("printed pp. 337-338", by_key["ROHRLICH_1996"]["pinpoint"])
        self.assertIn("equation (19)", by_key["CONREY_EQ19"]["pinpoint"])
        self.assertIn("PDF p. 11", by_key["CONREY_EQ19"]["pinpoint"])
        self.assertEqual(
            manifest["character_conventions"]["negative_d_formula"],
            "chi_d(-N)=chi_d(-1)*chi_d(N)=sign(d)*(d/N) when gcd(d,N)=1",
        )
        self.assertEqual(
            manifest["specialization_11_a2"]["formula"],
            "epsilon_d=sign(d)*(d/11)",
        )
        self.assertIn(
            "chi_d(-N)",
            manifest["normalizations"]["conrey_unitary"]["functional_equation"],
        )

    def test_all_four_records_satisfy_their_strict_schemas(self) -> None:
        store = SchemaStore()
        pairs = (
            (self.spec, ATLAS / "schema" / "l-function-spec.schema.json"),
            (self.detector, ATLAS / "schema" / "detector-contract.schema.json"),
            (self.evaluation, ATLAS / "schema" / "evaluation-record.schema.json"),
            (
                self.result,
                ATLAS
                / "detectors"
                / "raw-schemas"
                / "twist-root-number-covariance-result.schema.json",
            ),
        )
        for record, schema_path in pairs:
            with self.subTest(schema=schema_path.name):
                self.assertEqual(
                    validate_instance(record, store.load(schema_path), schema_path, store),
                    [],
                )

        schema_path = (
            ATLAS
            / "detectors"
            / "raw-schemas"
            / "twist-root-number-covariance-result.schema.json"
        )
        schema = store.load(schema_path)
        mutated = copy.deepcopy(self.result)
        mutated["analytic_rank"] = 0
        self.assertTrue(
            any(
                "unexpected property 'analytic_rank'" in error
                for error in validate_instance(mutated, schema, schema_path, store)
            )
        )
        mutated = copy.deepcopy(self.result)
        mutated["summaries"][0]["partition"] = "POSITIVE"
        self.assertTrue(
            any("not in enum" in error for error in validate_instance(mutated, schema, schema_path, store))
        )
        mutated = copy.deepcopy(self.result)
        mutated["cohort_counts"][0]["ROOT_NUMBER_PLUS"] += 1
        self.assertTrue(
            any("expected const" in error for error in validate_instance(mutated, schema, schema_path, store))
        )
        mutated = copy.deepcopy(self.result)
        mutated["root_cohort_gram_contrast"]["summaries"][0]["mean_square"]["numerator"] += 1
        self.assertTrue(
            any("expected const" in error for error in validate_instance(mutated, schema, schema_path, store))
        )

    def test_spec_and_evaluation_bind_every_load_bearing_input(self) -> None:
        self.assertEqual(self.spec["record_state"], "DRAFT")
        self.assertEqual(self.spec["classification"]["object_type"], "QUADRATIC_TWIST_L")
        self.assertEqual(
            self.spec["conductor"]["value"],
            "11*d^2 for fundamental discriminants d with gcd(d,11)=1",
        )
        self.assertEqual(
            self.spec["functional_equation"]["root_number"],
            "epsilon_d=sign(d)*(d/11)",
        )
        self.assertEqual(self.spec["central_data"]["assertion"], "UNKNOWN")
        self.assertFalse(self.spec["central_data"]["parity_forced"])
        self.assertEqual(self.spec["zero_data"]["usage"], "NOT_USED")
        self.assertEqual(self.evaluation["rigor_level"], "DISCOVERY_ONLY")
        invariances = {entry["code"]: entry for entry in self.detector["invariances"]}
        self.assertEqual(
            invariances["ROOT_COHORT_GRAM_CONTRAST"]["status"], "PROVED"
        )
        self.assertIn(
            "do not establish",
            next(
                item["statement"]
                for item in self.evaluation["firewalls"]
                if item["code"] == "FINITE_NOT_ASYMPTOTIC"
            ),
        )

        input_paths = {binding["path"] for binding in self.evaluation["input_bindings"]}
        self.assertEqual(
            input_paths,
            {subject.ROOT_NUMBER_SOURCE, subject.CURVE_SOURCE},
        )
        adapter_paths = {binding["path"] for binding in self.evaluation["adapter_bindings"]}
        self.assertEqual(
            adapter_paths,
            {
                subject.IMPLEMENTATION,
                subject.SHARED_COVARIANCE_ADAPTER,
                subject.LOCAL_TRACE_ADAPTER,
            },
        )
        self.assertEqual(
            self.evaluation["lfunction_spec_bindings"],
            [{"semantic_id": self.spec["semantic_id"], "record_sha256": sha256_hex(self.spec)}],
        )
        forbidden = {"analytic_rank", "central_rank", "zero_ordinates", "zeros"}
        for record in (self.spec, self.detector, self.evaluation, self.result):
            self.assertTrue(forbidden.isdisjoint(recursive_keys(record)))


class ArtifactAndCheckModeTests(RootNumberFixture):
    def test_dynamic_ids_filenames_and_no_stale_same_slug_records(self) -> None:
        records = (
            (self.spec, "LFUNC", subject.FAMILY_SPEC_SLUG, ATLAS / "specs"),
            (self.detector, "DETECTOR", subject.DETECTOR_SLUG, ATLAS / "detectors"),
            (self.evaluation, "EVAL", subject.EVALUATION_SLUG, ATLAS / "evaluations"),
        )
        for record, kind, slug, directory in records:
            semantic_id, digest = semantic_identity(kind, slug, record["identity_kernel"])
            self.assertEqual((record["semantic_id"], record["identity_sha256"]), (semantic_id, digest))
            path = directory / f"{semantic_id}.json"
            self.assertTrue(path.is_file())
            self.assertEqual(read_json(path), record)
            matching = subject._records_with_slug(directory, slug)
            self.assertEqual(matching, [path])

        result_path = REPO_ROOT / self.evaluation["result"]["artifact"]["path"]
        self.assertTrue(result_path.is_file())
        self.assertEqual(read_json(result_path), self.result)
        self.assertEqual(
            self.evaluation["result"]["artifact"]["sha256"],
            sha256_hex(self.result),
        )
        self.assertEqual(
            subject._stale_paths(
                ATLAS,
                subject._artifact_paths(ATLAS, self.spec, self.detector, self.evaluation),
            ),
            [],
        )

    def test_check_mode_rebuilds_without_writing(self) -> None:
        output = io.StringIO()
        with patch.object(sys, "argv", [subject.IMPLEMENTATION, "--check"]):
            with redirect_stdout(output):
                subject.main()
        self.assertIn("artifacts match; stale=0", output.getvalue())


if __name__ == "__main__":
    unittest.main()
