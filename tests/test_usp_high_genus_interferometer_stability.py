"""Independent exact tests for high-genus interferometer stability."""

from __future__ import annotations

import importlib
import itertools
import json
import math
import subprocess
import sys
import tempfile
import unittest
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(FUNCTION_FIELD) not in sys.path:
    sys.path.insert(0, str(FUNCTION_FIELD))

subject = importlib.import_module("usp_high_genus_interferometer_stability")


def independent_interferometer(left: int, right: int) -> dict[tuple[int, ...], int]:
    return {tuple(sorted((left, right))): 1, (left + right,): -1}


def independent_linear_combination(
    terms: list[tuple[int, dict[tuple[int, ...], int]]],
) -> dict[tuple[int, ...], int]:
    output: dict[tuple[int, ...], int] = defaultdict(int)
    for scale, polynomial in terms:
        for monomial, coefficient in polynomial.items():
            output[tuple(sorted(monomial))] += scale * coefficient
    return {
        monomial: coefficient for monomial, coefficient in output.items() if coefficient
    }


def independent_product(
    left: dict[tuple[int, ...], int],
    right: dict[tuple[int, ...], int],
) -> dict[tuple[int, ...], int]:
    output: dict[tuple[int, ...], int] = defaultdict(int)
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            output[tuple(sorted(left_monomial + right_monomial))] += (
                left_coefficient * right_coefficient
            )
    return dict(output)


def independent_monomial_expectation(monomial: tuple[int, ...]) -> int:
    """Brute-expand Gaussian/shift choices, independently of the producer."""

    total = 0
    for choices in itertools.product(("shift", "gaussian"), repeat=len(monomial)):
        gaussian_counts: Counter[int] = Counter()
        contribution = 1
        for frequency, choice in zip(monomial, choices):
            if choice == "shift":
                contribution *= -int(frequency % 2 == 0)
            else:
                gaussian_counts[frequency] += 1
        if not contribution or any(count % 2 for count in gaussian_counts.values()):
            continue
        for frequency, count in gaussian_counts.items():
            contribution *= frequency ** (count // 2) * math.prod(range(1, count, 2))
        total += contribution
    return total


def independent_expectation(polynomial: dict[tuple[int, ...], int]) -> int:
    return sum(
        coefficient * independent_monomial_expectation(monomial)
        for monomial, coefficient in polynomial.items()
    )


def independent_selectors() -> dict[str, dict[tuple[int, ...], int]]:
    return {
        "P": independent_linear_combination(
            [
                (1, independent_interferometer(2, 2)),
                (-1, independent_interferometer(4, 4)),
            ]
        ),
        "D": independent_linear_combination(
            [
                (-1, independent_interferometer(1, 1)),
                (2, independent_interferometer(1, 5)),
                (1, independent_interferometer(4, 4)),
            ]
        ),
        "S": independent_linear_combination([(-2, independent_interferometer(2, 8))]),
    }


class UspHighGenusInterferometerStabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_imported_theorem_and_scope_are_explicit(self) -> None:
        dependency = self.fixture["literature_dependency"]
        self.assertEqual(dependency["identifier"], "arXiv:2409.04844v1")
        self.assertIn("2g+1", dependency["imported_theorem"])
        self.assertIn("imported, not reproved", dependency["proof_status"])
        scope = self.fixture["scope"]
        self.assertFalse(scope["arithmetic_claims"])
        self.assertFalse(scope["novelty_claim"])
        self.assertIn("increasing-genus", self.fixture["firewall"])

    def test_closed_interferometer_mean_formula(self) -> None:
        guard = subject.WickGuard()
        engine = subject.GaussianMomentEngine(guard)
        for left in range(1, 11):
            for right in range(left, 11):
                self.assertEqual(
                    engine.expectation(subject.interferometer(left, right)),
                    subject.stable_interferometer_mean(left, right),
                )
        self.assertLessEqual(guard.total, guard.cap)

    def test_selector_means_and_thresholds_by_independent_expansion(self) -> None:
        selectors = independent_selectors()
        means = tuple(independent_expectation(selectors[name]) for name in selectors)
        self.assertEqual(means, (-2, 6, -4))
        packet = self.fixture["selectors"]
        self.assertEqual(packet["USp4_means"], [0, 0, 0])
        self.assertEqual(packet["stable_means"], list(means))
        self.assertEqual(packet["mean_stable_from_genus"], {"P": 4, "D": 4, "S": 5})
        self.assertEqual(
            {
                name: subject.stable_genus(polynomial)
                for name, polynomial in selectors.items()
            },
            {"P": 4, "D": 4, "S": 5},
        )

    def test_covariance_by_independent_wick_expansion(self) -> None:
        selectors = independent_selectors()
        names = tuple(selectors)
        means = tuple(independent_expectation(selectors[name]) for name in names)
        second = tuple(
            tuple(
                independent_expectation(
                    independent_product(selectors[left], selectors[right])
                )
                for right in names
            )
            for left in names
        )
        covariance = tuple(
            tuple(
                second[row][column] - means[row] * means[column] for column in range(3)
            )
            for row in range(3)
        )
        self.assertEqual(
            second,
            ((64, -64, 16), (-64, 140, -36), (16, -36, 160)),
        )
        self.assertEqual(covariance, subject.EXPECTED_SELECTOR_STABLE_COVARIANCE)
        packet = self.fixture["selectors"]
        self.assertEqual(
            packet["stable_covariance_matrix"], [list(row) for row in covariance]
        )
        self.assertEqual(packet["whole_second_moment_matrix_stable_from_genus"], 10)
        self.assertEqual(
            packet["covariance_entrywise_stable_from_genus"],
            [[8, 8, 9], [8, 8, 9], [9, 9, 10]],
        )
        self.assertEqual(packet["whole_covariance_stable_from_genus"], 10)
        self.assertEqual(
            packet["covariance_positive_definite_leading_minors"],
            [60, 3536, 503872],
        )

    def test_inverse_pool_winner_and_null_lattice(self) -> None:
        packet = self.fixture["inverse_raw_pool"]
        self.assertEqual(packet["USp4_means"], [0, 0, 0, 0])
        self.assertEqual(packet["stable_means"], [1, 1, 2, 2])
        self.assertEqual(packet["all_pool_means_stable_from_genus"], 5)
        self.assertEqual(packet["winner"]["stable_mean"], 6)
        self.assertEqual(packet["winner"]["stable_from_genus"], 5)
        lattice = packet["simultaneous_USp4_and_stable_null_lattice"]
        self.assertEqual(lattice["equation"], "c1+c2+2*c3+2*c4=0")
        self.assertEqual(lattice["rank"], 3)
        for row in lattice["primitive_Z_basis_rows"]:
            self.assertEqual(sum(a * b for a, b in zip(row, (1, 1, 2, 2))), 0)
        self.assertEqual(
            packet["winner"]["stable_mean"],
            sum(a * b for a, b in zip((2, 4, -1, 1), (1, 1, 2, 2))),
        )

    def test_locked_usp4_replay_and_source_hashes(self) -> None:
        source = self.fixture["source_locked_genus_two_packet"]
        self.assertEqual(source["source_commit"], subject.SOURCE_COMMIT)
        replay = source["replayed_USp4"]
        self.assertEqual(replay["selector_means"], [0, 0, 0])
        self.assertEqual(replay["inverse_pool_means"], [0, 0, 0, 0])
        self.assertEqual(
            replay["selector_covariance"],
            [list(row) for row in subject.EXPECTED_SOURCE_USP4_COVARIANCE],
        )
        self.assertGreater(replay["source_accounted_operations"], 0)
        observed = subject._verify_source_locks()
        self.assertEqual(observed, subject.EXPECTED_SOURCE_HASHES)

    def test_source_lock_fails_closed_on_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            paths = {}
            for name, source in {
                "note": subject.SOURCE_NOTE,
                "producer": subject.SOURCE_PRODUCER,
                "test": subject.SOURCE_TEST,
            }.items():
                target = temporary / source.name
                target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
                paths[name] = target
            paths["note"].write_text(
                paths["note"].read_text(encoding="utf-8") + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RuntimeError, "note hash changed"):
                subject._verify_source_locks(paths)

    def test_resource_payload_and_no_floats(self) -> None:
        resource = self.fixture["resource_contract"]
        self.assertFalse(resource["randomness"])
        self.assertFalse(resource["floating_point"])
        self.assertFalse(resource["finite_field_or_curve_enumeration"])
        self.assertLessEqual(
            resource["Wick_contraction_branches_used"],
            resource["Wick_contraction_branch_cap"],
        )
        self.assertLessEqual(resource["Wick_contraction_branch_cap"], 4096)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(self.fixture)

    def test_document_and_fixture_stay_synchronized(self) -> None:
        note = subject.NOTE.read_text(encoding="utf-8")
        for token in (
            "(-2,6,-4)",
            "60&-52&8",
            "503872",
            "c_1+c_2+2c_3+2c_4=0",
            "g>=10",
            "arithmetic increasing-genus",
        ):
            self.assertIn(token, note)
        self.assertEqual(
            self.fixture["producer"]["note_sha256_lf_normalized"],
            subject._lf_sha256(subject.NOTE),
        )

    def test_validation_remains_active_under_optimized_python(self) -> None:
        with self.assertRaises(TypeError):
            subject.interferometer(True, 2)
        with self.assertRaises(ValueError):
            subject.interferometer(2, 1)
        with self.assertRaises(ValueError):
            subject.GaussianMomentEngine(subject.WickGuard()).shifted_moment(2, -1)
        with self.assertRaises(RuntimeError):
            guard = subject.WickGuard(cap=1)
            guard.charge("first")
            guard.charge("second")

    def test_stored_fixture_and_normal_optimized_cli(self) -> None:
        stored = json.loads(subject.DEFAULT_OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        for path, field in (
            (Path(subject.__file__), "source_sha256_lf_normalized"),
            (subject.NOTE, "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            self.assertEqual(self.fixture["producer"][field], subject._lf_sha256(path))
        for optimized in (False, True):
            command = [sys.executable]
            if optimized:
                command.append("-O")
            command.extend(
                [str(Path(subject.__file__)), "--check", str(subject.DEFAULT_OUTPUT)]
            )
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn(
                "OK: exact high-genus interferometer stability", completed.stdout
            )


if __name__ == "__main__":
    unittest.main()
