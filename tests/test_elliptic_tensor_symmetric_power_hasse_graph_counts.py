"""Independent tests for the all-r tensor/symmetric-power Hasse graph counts."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from math import comb, isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_tensor_symmetric_power_hasse_graph_counts as subject  # noqa: E402


def independent_L(n: int, C: int, q: int) -> int:
    if n == 0:
        return 2
    total = 0
    for j in range(n // 2 + 1):
        coefficient = n * comb(n - j, j) // (n - j)
        total += (-1) ** j * coefficient * q**j * C ** (n - 2 * j)
    return total


def independent_square_graphs(
    p: int, k: int, r: int
) -> tuple[set[tuple[int, int, int]], set[tuple[int, int, int]]]:
    s = p**k
    q = s * s
    first: set[tuple[int, int, int]] = set()
    second: set[tuple[int, int, int]] = set()
    for C in range(-2 * s, 2 * s + 1):
        numerator = independent_L(r + 1, C, q)
        if numerator % s**r == 0:
            base_A = numerator // s**r
            for epsilon in (-1, 1):
                first.add((epsilon**r * base_A, epsilon * C, C))
        if (C * C - 2 * q) % s == 0:
            base_B = (C * C - 2 * q) // s
            for eta in (-1, 1):
                second.add((eta**r * C, eta * base_B, C))
    return first, second


def independent_closed_counts(p: int, k: int, r: int) -> dict[str, int]:
    first = 8 * p ** (k // (r + 1)) + (2 if r % 2 else 1)
    second = 8 * p ** (k // 2) + 2
    overlap = 4 + (4 if (r + 1) % 3 else 0)
    return {
        "first_graph": first,
        "second_graph": second,
        "overlap": overlap,
        "union": first + second - overlap,
    }


class EllipticTensorSymmetricPowerHasseGraphCountTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_homogeneous_dickson_matches_independent_closed_sum(self) -> None:
        for n in range(0, 25):
            for q in (2, 3, 9, 25):
                for C in (-9, -3, 0, 2, 7):
                    with self.subTest(n=n, q=q, C=C):
                        self.assertEqual(
                            subject.dickson_homogeneous_value(n, C, q),
                            independent_L(n, C, q),
                        )

    def test_square_first_graph_valuation_has_no_prime_exceptions(self) -> None:
        for p in (2, 3, 5):
            for k in range(1, 4):
                s = p**k
                q = s * s
                for r in range(1, 17):
                    divisor_exponent = (r * k + r) // (r + 1)
                    self.assertEqual(
                        subject.first_divisor_exponent_square(k, r),
                        divisor_exponent,
                    )
                    for C in range(-2 * s, 2 * s + 1):
                        divisible = (
                            independent_L(r + 1, C, q) % s**r == 0
                        )
                        predicted = C % p**divisor_exponent == 0
                        self.assertEqual(
                            divisible,
                            predicted,
                            (p, k, r, C, independent_L(r + 1, C, q)),
                        )

    def test_second_graph_integrality_threshold(self) -> None:
        for p in (2, 3, 5, 7):
            for k in range(1, 5):
                s = p**k
                threshold = (k + 1) // 2
                self.assertEqual(
                    subject.second_divisor_exponent_square(k), threshold
                )
                for C in range(-2 * s, 2 * s + 1):
                    self.assertEqual(
                        (C * C - 2 * s * s) % s == 0,
                        C % p**threshold == 0,
                    )

    def test_square_counts_sign_duplicates_and_overlap_period(self) -> None:
        for p in (2, 3, 5):
            for k in (1, 2):
                s = p**k
                for r in range(1, 19):
                    first, second = independent_square_graphs(p, k, r)
                    predicted = independent_closed_counts(p, k, r)
                    observed = {
                        "first_graph": len(first),
                        "second_graph": len(second),
                        "overlap": len(first & second),
                        "union": len(first | second),
                    }
                    self.assertEqual(observed, predicted)
                    self.assertEqual(subject.square_closed_counts(p, k, r), predicted)
                    self.assertEqual(
                        set(subject.first_graph_triples_square(p, k, r)), first
                    )
                    self.assertEqual(
                        set(subject.second_graph_triples_square(p, k, r)), second
                    )
                    self.assertEqual(set(subject.square_graph_union(p, k, r)), first | second)

                    normalized_overlap_C = {C // s for _, _, C in first & second}
                    expected_z = {-2, 2}
                    if (r + 1) % 3:
                        expected_z.update((-1, 1))
                    self.assertEqual(normalized_overlap_C, expected_z)
                    self.assertNotIn(0, normalized_overlap_C)

    def test_central_sign_zero_corners_are_counted_correctly(self) -> None:
        for r in range(1, 13):
            first = set(subject.first_graph_triples_square(3, 1, r))
            second = set(subject.second_graph_triples_square(3, 1, r))
            first_at_zero = {(A, B, C) for A, B, C in first if C == 0}
            second_at_zero = {(A, B, C) for A, B, C in second if C == 0}
            self.assertEqual(len(first_at_zero), 2 if r % 2 else 1)
            self.assertEqual(len(second_at_zero), 2)
            if r % 2:
                self.assertEqual({abs(A) for A, _, _ in first_at_zero}, {6})
            else:
                self.assertEqual(first_at_zero, {(0, 0, 0)})

    def test_r1_r2_r3_closed_formula_recoveries(self) -> None:
        for p in (3, 5, 7):
            for k in range(1, 4):
                scale = p ** (k // 2)
                expected = {
                    1: 16 * scale - 4,
                    2: 8 * p ** (k // 3) + 8 * scale - 1,
                    3: 8 * p ** (k // 4) + 8 * scale - 4,
                }
                for r, count in expected.items():
                    self.assertEqual(
                        subject.square_closed_counts(p, k, r)["union"], count
                    )
        rows = self.fixture["locked_predecessor_recoveries"]["rows"]
        self.assertEqual([row["r"] for row in rows], [1, 2, 3])
        self.assertTrue(all(row["locked_predecessor_formula_agrees"] for row in rows))

    def test_nonsquare_odd_prime_parity_theorem(self) -> None:
        for p in (3, 5, 7):
            for exponent in (1, 3):
                q = p**exponent
                H = isqrt(4 * q)
                for r in range(1, 17):
                    triples = set(
                        subject.nonsquare_first_graph_triples(p, exponent, r)
                    )
                    if r % 2:
                        self.assertFalse(triples)
                        self.assertEqual(
                            subject.nonsquare_closed_count(p, exponent, r), 0
                        )
                        for C in range(-H, H + 1):
                            self.assertNotEqual(independent_L(r + 1, C, q), 0)
                            self.assertNotEqual(C * C, 2 * q)
                    else:
                        threshold = -(
                            -(exponent * r) // (2 * (r + 1))
                        )
                        predicted_C = {
                            C
                            for C in range(-H, H + 1)
                            if C % p**threshold == 0
                        }
                        self.assertEqual({C for _, _, C in triples}, predicted_C)
                        self.assertEqual(
                            len(triples),
                            4 * (H // p**threshold) + 1,
                        )
                        self.assertEqual(
                            len(triples),
                            subject.nonsquare_closed_count(p, exponent, r),
                        )
                        self.assertTrue(all(abs(A) <= H for A, _, _ in triples))

    def test_locked_predecessors_and_owned_files(self) -> None:
        locks = self.fixture["predecessor_source_locks"]
        self.assertEqual(len(locks), 4)
        for lock in locks:
            fixture_path = ROOT / lock["fixture_path"]
            producer_path = ROOT / lock["producer_path"]
            fixture_bytes = fixture_path.read_bytes().replace(
                b"\r\n", b"\n"
            ).replace(b"\r", b"\n")
            producer_bytes = producer_path.read_bytes().replace(
                b"\r\n", b"\n"
            ).replace(b"\r", b"\n")
            self.assertEqual(
                hashlib.sha256(fixture_bytes).hexdigest(),
                lock["fixture_sha256_lf_normalized"],
            )
            self.assertEqual(
                hashlib.sha256(producer_bytes).hexdigest(),
                lock["producer_sha256_lf_normalized"],
            )
            predecessor = json.loads(fixture_path.read_text(encoding="utf-8"))
            self.assertEqual(predecessor["schema"], lock["fixture_schema"])
            self.assertEqual(
                predecessor["payload_sha256"], lock["fixture_payload_sha256"]
            )

        for owned in self.fixture["source_and_owned_file_locks"][
            "owned_file_locks"
        ].values():
            path = ROOT / owned["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(
                b"\r", b"\n"
            )
            self.assertEqual(
                hashlib.sha256(normalized).hexdigest(),
                owned["sha256_lf_normalized"],
            )

    def test_fixture_payload_resources_and_no_float_results(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        resource = stored["resource_contract"]
        ledger = resource["accounted_work_unit_ledger"]
        self.assertLess(
            ledger["total_accounted_work_units"],
            resource["exclusive_accounted_work_unit_cap"],
        )
        self.assertGreater(ledger["square_C_candidates"], 0)
        self.assertGreater(ledger["nonsquare_C_candidates"], 0)
        self.assertEqual(
            resource["field_curve_model_or_full_trace_cube_enumerations"], 0
        )
        self.assertEqual(resource["random_samples"], 0)
        self.assertEqual(resource["floating_point_results"], 0)
        self.assertEqual(resource["runtime_symbolic_packages"], 0)

        def reject_floats(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_floats(item)
            elif isinstance(value, list):
                for item in value:
                    reject_floats(item)

        reject_floats(stored)

    def test_note_scope_integrity_and_source_has_no_asserts(self) -> None:
        text = subject.NOTE_PATH.read_text(encoding="utf-8")
        display_open = sum(line.strip() == r"\[" for line in text.splitlines())
        display_close = sum(line.strip() == r"\]" for line in text.splitlines())
        self.assertEqual(display_open, display_close)
        self.assertIsNone(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))
        for anchor in (
            "no coefficient-prime exception",
            r"\delta_u+r\delta_v=0\pmod2",
            r"3\nmid(r+1)",
            "The first three rungs are recovered exactly",
            "Nonsquare odd prime powers",
            "20,000-unit cap",
            "full trace cube",
            "RH, or GRH",
        ):
            self.assertIn(anchor, text)
        source = Path(subject.__file__).read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"(?m)^\s*assert\b", source))

    def test_strict_refusals_and_resource_guard(self) -> None:
        for malformed in (True, Fraction(1), "1", None, 1.0):
            with self.subTest(value=malformed):
                with self.assertRaises(TypeError):
                    subject.square_closed_counts(malformed, 1, 1)
        for composite in (1, 4, 9, 15):
            with self.assertRaises(ValueError):
                subject.square_closed_counts(composite, 1, 1)
        with self.assertRaises(ValueError):
            subject.square_closed_counts(subject.MAX_PRIME + 2, 1, 1)
        for invalid_k in (0, subject.MAX_K + 1):
            with self.assertRaises(ValueError):
                subject.square_closed_counts(3, invalid_k, 1)
        for invalid_r in (0, subject.MAX_R + 1):
            with self.assertRaises(ValueError):
                subject.square_closed_counts(3, 1, invalid_r)
        with self.assertRaises(ValueError):
            subject.nonsquare_closed_count(2, 1, 2)
        with self.assertRaises(ValueError):
            subject.nonsquare_closed_count(3, 2, 2)
        with self.assertRaises(ValueError):
            subject.first_divisor_exponent_nonsquare(1, 3)
        with self.assertRaises(ValueError):
            subject.first_graph_triples_square(101, subject.MAX_K, 1)
        with self.assertRaises(ValueError):
            subject.second_graph_triples_square(101, subject.MAX_K, 1)
        with self.assertRaises(ValueError):
            subject.nonsquare_first_graph_triples(
                101, subject.MAX_EXPONENT, subject.MAX_R
            )

        guard = subject.ResourceGuard(2)
        guard.charge("one")
        with self.assertRaises(RuntimeError):
            guard.charge("two")

    def test_cli_write_check_staleness_and_optimized_refusals(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fixture.json"
            subject.main(["--write", str(path)])
            subject.main(["--check", str(path)])
            path.write_text("{}\n", encoding="utf-8")
            with self.assertRaises(SystemExit):
                subject.main(["--check", str(path)])

        script = (
            "import sys;"
            f"sys.path.insert(0,{str(FUNCTION_FIELD)!r});"
            "import elliptic_tensor_symmetric_power_hasse_graph_counts as m;"
            "\ntry:m.square_closed_counts(True,1,1)\n"
            "except TypeError:pass\n"
            "else:raise SystemExit(2)\n"
            "try:m.nonsquare_closed_count(2,1,2)\n"
            "except ValueError:pass\n"
            "else:raise SystemExit(3)\n"
            "try:m.nonsquare_first_graph_triples(101,m.MAX_EXPONENT,m.MAX_R)\n"
            "except ValueError:pass\n"
            "else:raise SystemExit(5)\n"
            "g=m.ResourceGuard(1)\n"
            "try:g.charge('x')\n"
            "except RuntimeError:pass\n"
            "else:raise SystemExit(4)\n"
        )
        completed = subprocess.run(
            [sys.executable, "-B", "-O", "-c", script],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main()
