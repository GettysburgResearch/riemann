"""Independent exact tests for the tensor/symmetric-power moment ladder."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import unittest
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_tensor_symmetric_power_moment_ladder as subject  # noqa: E402


def independent_weight_invariant(n: int, half_order: int) -> int:
    weights = tuple(n - 2 * j for j in range(n + 1))
    multiplicities = Counter({0: 1})
    for _ in range(2 * half_order):
        next_multiplicities: Counter[int] = Counter()
        for total, count in multiplicities.items():
            for weight in weights:
                next_multiplicities[total + weight] += count
        multiplicities = next_multiplicities
    return multiplicities[0] - multiplicities[2]


def independent_partition_neighbors(
    partition: tuple[int, ...], rank: int
) -> set[tuple[int, ...]]:
    output: set[tuple[int, ...]] = set()
    for row in range(len(partition) + 1):
        candidate = list(partition)
        if row == len(partition):
            if row < rank:
                candidate.append(1)
                output.add(tuple(candidate))
        elif row == 0 or partition[row] < partition[row - 1]:
            candidate[row] += 1
            output.add(tuple(candidate))
    for row, size in enumerate(partition):
        if row == len(partition) - 1 or size > partition[row + 1]:
            candidate = list(partition)
            candidate[row] -= 1
            if candidate[row] == 0:
                candidate.pop()
            output.add(tuple(candidate))
    return output


def independent_usp_moments(rank: int) -> dict[int, int]:
    paths: dict[tuple[int, ...], int] = {(): 1}
    output = {0: 1}
    for step in range(1, 9):
        next_paths: defaultdict[tuple[int, ...], int] = defaultdict(int)
        for partition, count in paths.items():
            for neighbor in independent_partition_neighbors(partition, rank):
                next_paths[neighbor] += count
        paths = dict(next_paths)
        if step % 2 == 0:
            output[step] = paths.get((), 0)
    return output


def lf_hash(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


class EllipticTensorSymmetricPowerMomentLadderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_weight_difference_and_closed_formulas_independently(self) -> None:
        for n in range(0, 11):
            for half_order in range(1, 5):
                direct = independent_weight_invariant(n, half_order)
                self.assertEqual(
                    subject.su2_weight_difference_multiplicity(n, half_order), direct
                )
                self.assertEqual(
                    subject.su2_closed_even_moment(n, half_order), direct
                )

        expected_n5 = {0: 1, 2: 1, 4: 6, 6: 111, 8: 2666}
        self.assertEqual(subject.su2_cg_even_moments(5), expected_n5)

    def test_closed_product_principal_ladder_and_positive_gaps(self) -> None:
        for r in range(1, subject.FROZEN_MAX_R + 1):
            rows = subject.product_and_principal_moment_rows(r)
            product = rows["independent_product"]
            principal = rows["principal_symmetric_power"]
            gaps = subject.moment_gap_formulas(r)
            self.assertEqual(product[:6], principal[:6])
            self.assertEqual(principal[6] - product[6], gaps[6])
            self.assertEqual(principal[8] - product[8], gaps[8])
            self.assertGreater(gaps[6], 0)
            self.assertGreater(gaps[8], 0)
            self.assertEqual(product[4], 2 * (r + 1))

    def test_locked_r1_r2_r3_rows_are_reproduced(self) -> None:
        expected = {
            1: (
                [1, 0, 1, 0, 4, 0, 25, 0, 196],
                [1, 0, 1, 0, 4, 0, 34, 0, 364],
            ),
            2: (
                [1, 0, 1, 0, 6, 0, 75, 0, 1274],
                [1, 0, 1, 0, 6, 0, 111, 0, 2666],
            ),
            3: (
                [1, 0, 1, 0, 8, 0, 170, 0, 5096],
                [1, 0, 1, 0, 8, 0, 260, 0, 11096],
            ),
        }
        for r, (product, principal) in expected.items():
            rows = subject.product_and_principal_moment_rows(r)
            self.assertEqual(rows["independent_product"], product)
            self.assertEqual(rows["principal_symmetric_power"], principal)

    def test_generic_usp_rank_exceptions_and_stable_range(self) -> None:
        expected = {
            2: {0: 1, 2: 1, 4: 3, 6: 14, 8: 84},
            3: {0: 1, 2: 1, 4: 3, 6: 15, 8: 104},
            4: {0: 1, 2: 1, 4: 3, 6: 15, 8: 105},
            8: {0: 1, 2: 1, 4: 3, 6: 15, 8: 105},
        }
        for rank, row in expected.items():
            self.assertEqual(independent_usp_moments(rank), row)
            self.assertEqual(subject.usp_standard_even_moments(rank), row)
            self.assertEqual(subject.usp_closed_even_moments(rank), row)

        for r in range(1, subject.FROZEN_MAX_R + 1):
            structured = subject.product_and_principal_moment_rows(r)
            generic = subject.usp_closed_even_moments(r + 1)
            self.assertEqual(structured["independent_product"][2], generic[2])
            self.assertEqual(structured["principal_symmetric_power"][2], generic[2])
            self.assertNotEqual(structured["independent_product"][4], generic[4])
            self.assertNotEqual(structured["principal_symmetric_power"][4], generic[4])

    def test_source_locks_payloads_hashes_and_semantics(self) -> None:
        sources = subject.load_locked_sources()
        self.assertEqual(
            set(sources),
            {
                "all_r_subtorus_rigidity",
                "r3_tensor_sym3_sym7",
                "r2_tensor_sym2_sym5",
                "r1_so4_rankin_moments",
            },
        )
        locks = self.fixture["source_and_owned_file_locks"]["source_locks"]
        for name, lock in locks.items():
            fixture_path = ROOT / lock["fixture_path"]
            producer_path = ROOT / lock["producer_path"]
            self.assertEqual(
                lf_hash(fixture_path), lock["fixture_sha256_lf_normalized"]
            )
            self.assertEqual(
                lf_hash(producer_path), lock["producer_sha256_lf_normalized"]
            )
            fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
            unhashed = dict(fixture)
            claimed = unhashed.pop("payload_sha256")
            self.assertEqual(claimed, lock["fixture_payload_sha256"])
            self.assertEqual(claimed, subject._canonical_sha256(unhashed))
            self.assertEqual(fixture["schema"], lock["schema"])
            self.assertEqual(fixture, sources[name])

    def test_payload_owned_hashes_and_resource_contract(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        owned = stored["source_and_owned_file_locks"]["owned_file_locks"]
        for lock in owned.values():
            self.assertEqual(lf_hash(ROOT / lock["path"]), lock["sha256_lf_normalized"])

        resources = stored["resource_contract"]
        ledger = resources["accounted_work_unit_ledger"]
        self.assertEqual(
            sum(value for key, value in ledger.items() if key != "total_accounted_work_units"),
            ledger["total_accounted_work_units"],
        )
        self.assertLess(
            ledger["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertLessEqual(
            resources["actual_Clebsch_Gordan_transitions"],
            resources["inclusive_Clebsch_Gordan_transition_cap"],
        )
        self.assertEqual(resources["floating_point_results"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["runtime_symbolic_packages"], 0)
        self.assertEqual(resources["numerical_integrations"], 0)
        self.assertEqual(resources["finite_fields_curves_or_models_enumerated"], 0)

        def reject_floats(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_floats(item)
            elif isinstance(value, list):
                for item in value:
                    reject_floats(item)

        reject_floats(stored)

    def test_strict_input_and_resource_refusals(self) -> None:
        for bad in (True, 1.0, "2", None):
            with self.assertRaises(TypeError):
                subject.product_and_principal_moment_rows(bad)
        for bad in (0, subject.FROZEN_MAX_R + 1):
            with self.assertRaises(ValueError):
                subject.product_and_principal_moment_rows(bad)
        with self.assertRaises(ValueError):
            subject.su2_weight_difference_multiplicity(
                subject.WEIGHT_FORMULA_MAX_N + 1, 2
            )
        with self.assertRaises(ValueError):
            subject.su2_weight_difference_multiplicity(2, 5)
        with self.assertRaises(ValueError):
            subject.su2_cg_even_moments(subject.CG_REGRESSION_MAX_N + 1)
        with self.assertRaises(ValueError):
            subject.usp_standard_even_moments(1)
        with self.assertRaises(RuntimeError):
            subject.su2_cg_even_moments(4, subject.ResourceGuard(cap=10))

    def test_note_states_proofs_caveats_and_boundaries(self) -> None:
        note = subject.NOTE_PATH.read_text(encoding="utf-8")
        required = (
            "Universal first-split theorem",
            "weight difference",
            "triangle inequalities",
            "oscillating tableaux",
            "stable range",
            "polarization caveat",
            "compact Haar laws, not finite-field family moments",
            "No literature-priority claim",
        )
        for phrase in required:
            self.assertIn(phrase, note)
        self.assertNotIn("TODO", note)
        self.assertNotIn("PLACEHOLDER", note)

    def test_cli_check_succeeds_normally_and_optimized(self) -> None:
        producer = str(Path(subject.__file__).resolve())
        for flags in (["-B"], ["-B", "-O"]):
            completed = subprocess.run(
                [sys.executable, *flags, producer, "--check"],
                cwd=ROOT,
                check=False,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("PASS", completed.stdout)
            self.assertIn(self.fixture["payload_sha256"], completed.stdout)


if __name__ == "__main__":
    unittest.main()
