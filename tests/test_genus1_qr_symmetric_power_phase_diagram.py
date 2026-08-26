"""Independent checks for the locked genus-one q-versus-r phase diagram."""

from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus1_qr_symmetric_power_phase_diagram as subject


def as_fraction(value: list[int]) -> Fraction:
    return Fraction(value[0], value[1])


def independent_symmetric_power_trace(trace: int, q: int, rank: int) -> int:
    """Closed Dickson-polynomial sum, independent of the producer recurrence."""

    return sum(
        (-1) ** index
        * math.comb(rank - index, index)
        * q**index
        * trace ** (rank - 2 * index)
        for index in range(rank // 2 + 1)
    )


class Genus1QrSymmetricPowerPhaseDiagramTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {row["q"]: row for row in cls.fixture["frozen_q3_q5_q7_facts"]}

    def test_integral_recurrence_and_normalized_squares(self) -> None:
        for q in (3, 5, 7):
            for trace in subject.EXPECTED_HISTOGRAMS[q]:
                values = [
                    subject.symmetric_power_trace(trace, q, rank)
                    for rank in range(subject.RANK_CAP + 1)
                ]
                self.assertEqual(values[0], 1)
                self.assertEqual(values[1], trace)
                for rank, value in enumerate(values):
                    self.assertEqual(
                        value, independent_symmetric_power_trace(trace, q, rank)
                    )
                    self.assertEqual(
                        subject.normalized_trace_square(trace, q, rank),
                        Fraction(value**2, q**rank),
                    )
                for rank in range(2, len(values)):
                    self.assertEqual(
                        values[rank], trace * values[rank - 1] - q * values[rank - 2]
                    )
        with self.assertRaises(ValueError):
            subject.symmetric_power_trace(1, 3, -1)
        with self.assertRaises(ValueError):
            subject.symmetric_power_trace(1, 0, 1)

    def test_locked_masses_supports_and_uniform_bounds(self) -> None:
        expected = {
            3: (18, 3, Fraction(1, 9), Fraction(4)),
            5: (100, 4, Fraction(1, 10), Fraction(5)),
            7: (294, 5, Fraction(1, 21), Fraction(28, 3)),
        }
        for q, (mass, endpoint, endpoint_mass, bound_square) in expected.items():
            row = self.by_q[q]
            extreme = row["extreme_observed_source_trace_classes"]
            self.assertEqual(row["source_model_count"], mass)
            self.assertEqual(extreme["absolute_trace"], endpoint)
            self.assertEqual(as_fraction(extreme["combined_mass"]), endpoint_mass)
            self.assertEqual(
                as_fraction(extreme["uniform_character_square_upper_bound"]),
                bound_square,
            )
            for rank in range(subject.RANK_CAP + 1):
                for trace in subject.EXPECTED_HISTOGRAMS[q]:
                    self.assertLessEqual(
                        subject.normalized_trace_square(trace, q, rank), bound_square
                    )

    def test_sign_tail_bounded_and_trimmed_diagnostics_are_exact(self) -> None:
        for q, q_row in self.by_q.items():
            histogram = subject.EXPECTED_HISTOGRAMS[q]
            mass = sum(histogram.values())
            endpoint = max(abs(trace) for trace in histogram)
            endpoint_mass = sum(
                count for trace, count in histogram.items() if abs(trace) == endpoint
            )
            for rank in range(subject.RANK_CAP + 1):
                row = q_row["rank_rows_0_through_32"][rank]
                signs = {"negative": 0, "zero": 0, "positive": 0}
                tails = {level: 0 for level in (1, 2, 3, 4)}
                capped = {level: Fraction(0) for level in (1, 2, 4)}
                raw = {order: Fraction(0) for order in (2, 4, 6)}
                trimmed = {order: Fraction(0) for order in (2, 4, 6)}
                endpoint_sums = {order: Fraction(0) for order in (2, 4, 6)}
                endpoint_square = None
                for trace, count in histogram.items():
                    value = independent_symmetric_power_trace(trace, q, rank)
                    sign = (
                        "positive" if value > 0 else "negative" if value < 0 else "zero"
                    )
                    signs[sign] += count
                    square = Fraction(value * value, q**rank)
                    for level in tails:
                        if square > level * level:
                            tails[level] += count
                    for level in capped:
                        capped[level] += count * min(square, Fraction(level * level))
                    is_endpoint = abs(trace) == endpoint
                    if is_endpoint:
                        if endpoint_square is None:
                            endpoint_square = square
                        else:
                            self.assertEqual(endpoint_square, square)
                    for order in raw:
                        term = count * square ** (order // 2)
                        raw[order] += term
                        if is_endpoint:
                            endpoint_sums[order] += term
                        else:
                            trimmed[order] += term
                self.assertEqual(row["sign_counts"], signs)
                for sign, count in signs.items():
                    self.assertEqual(
                        as_fraction(row["sign_masses"][sign]), Fraction(count, mass)
                    )
                for level, count in tails.items():
                    tail = row["strict_tail_abs_gt"][str(level)]
                    self.assertEqual(tail["count"], count)
                    self.assertEqual(as_fraction(tail["mass"]), Fraction(count, mass))
                for level, total in capped.items():
                    self.assertEqual(
                        as_fraction(
                            row["bounded_capped_square_means"][
                                f"min_x2_{level * level}"
                            ]
                        ),
                        total / mass,
                    )
                self.assertIsNotNone(endpoint_square)
                self.assertEqual(
                    as_fraction(
                        row["endpoint_trace_classes"]["normalized_trace_square"]
                    ),
                    endpoint_square,
                )
                for order, raw_total in raw.items():
                    key = str(order)
                    self.assertEqual(
                        as_fraction(row["raw_even_moments"][key]), raw_total / mass
                    )
                    self.assertEqual(
                        as_fraction(
                            row["endpoint_trace_classes"][
                                "raw_even_moment_contributions"
                            ][key]
                        ),
                        endpoint_sums[order] / mass,
                    )
                    self.assertEqual(
                        as_fraction(
                            row["endpoint_trace_classes"]["shares_of_raw_even_moments"][
                                key
                            ]
                        ),
                        endpoint_sums[order] / raw_total,
                    )
                    self.assertEqual(
                        as_fraction(
                            row["endpoint_trimmed_conditional_even_moments"][key]
                        ),
                        trimmed[order] / (mass - endpoint_mass),
                    )
                self.assertEqual(
                    as_fraction(row["haar_boundary_scalings"]["raw_fourth_over_N"]),
                    raw[4] / mass / (rank + 1),
                )
                self.assertEqual(
                    as_fraction(
                        row["haar_boundary_scalings"]["raw_sixth_over_N_cubed"]
                    ),
                    raw[6] / mass / (rank + 1) ** 3,
                )

    def test_parity_and_finite_q_resonance_certificates(self) -> None:
        expected_zero_masses = {3: 4, 5: 20, 7: 42}
        for q, q_row in self.by_q.items():
            for rank in range(1, subject.RANK_CAP + 1, 2):
                counts = q_row["rank_rows_0_through_32"][rank]["sign_counts"]
                self.assertEqual(counts["positive"], counts["negative"])
                baseline = expected_zero_masses[q]
                if q == 3 and rank % 6 == 5:
                    baseline += 2
                self.assertEqual(counts["zero"], baseline)
        for trace in (-3, 3):
            zeros = [
                rank
                for rank in range(33)
                if independent_symmetric_power_trace(trace, 3, rank) == 0
            ]
            self.assertEqual(zeros, [5, 11, 17, 23, 29])
        for q in (5, 7):
            for trace in subject.EXPECTED_HISTOGRAMS[q]:
                if trace != 0:
                    self.assertFalse(
                        any(
                            independent_symmetric_power_trace(trace, q, rank) == 0
                            for rank in range(33)
                        )
                    )

    def test_bounded_summaries_and_displayed_values(self) -> None:
        expected_r2 = {
            3: ("14/27", "23/27", 0, "503/243", "432/503", "71/216"),
            5: ("71/125", "217/250", 10, "8459/3125", "1331/1538", "253/625"),
            7: ("86/147", "877/1029", 14, "48047/16807", "34992/48047", "1119/1372"),
        }
        expected_endpoint_maxima = {
            3: (9, Fraction(1162261467, 1163419244)),
            5: (
                22,
                Fraction(
                    113569194615186406896871905621841,
                    126405984394988239400887513953418,
                ),
            ),
            7: (
                12,
                Fraction(12467261263346438421601, 13371541175844726981621),
            ),
        }
        expected_first_decreases = {3: (2, 3), 5: (2, 3), 7: (4, 5)}
        expected_display_ranges = {
            3: ("0.065265", "2.959292"),
            5: ("0.179863", "3.443174"),
            7: ("0.394064", "5.903370"),
        }
        note = (
            FUNCTION_FIELD / "GENUS1_QR_SYMMETRIC_POWER_PHASE_DIAGRAM.md"
        ).read_text(encoding="utf-8")

        def first_change(
            values: list[Fraction], direction: str
        ) -> tuple[int, int, Fraction, Fraction]:
            for rank in range(1, len(values)):
                changed = (
                    values[rank] > values[rank - 1]
                    if direction == "increase"
                    else values[rank] < values[rank - 1]
                )
                if changed:
                    return rank - 1, rank, values[rank - 1], values[rank]
            self.fail(f"no adjacent {direction} found")

        for q, q_row in self.by_q.items():
            rows = q_row["rank_rows_0_through_32"]
            r2 = rows[2]
            actual_r2 = (
                str(as_fraction(r2["bounded_capped_square_means"]["min_x2_1"])),
                str(as_fraction(r2["bounded_capped_square_means"]["min_x2_4"])),
                r2["strict_tail_abs_gt"]["2"]["count"],
                str(as_fraction(r2["raw_even_moments"]["4"])),
                str(
                    as_fraction(
                        r2["endpoint_trace_classes"]["shares_of_raw_even_moments"]["4"]
                    )
                ),
                str(as_fraction(r2["endpoint_trimmed_conditional_even_moments"]["4"])),
            )
            self.assertEqual(actual_r2, expected_r2[q])
            for token in expected_r2[q]:
                self.assertIn(str(token), note)

            fourth_values = [as_fraction(row["raw_even_moments"]["4"]) for row in rows]
            endpoint_shares = [
                as_fraction(
                    row["endpoint_trace_classes"]["shares_of_raw_even_moments"]["4"]
                )
                for row in rows
            ]
            capped_values = [
                as_fraction(row["bounded_capped_square_means"]["min_x2_4"])
                for row in rows
            ]
            summary = q_row["bounded_cap_summary"]
            for name, values, target in (
                ("raw_fourth_moment_minimum", fourth_values, min(fourth_values)),
                ("raw_fourth_moment_maximum", fourth_values, max(fourth_values)),
                (
                    "endpoint_fourth_share_maximum",
                    endpoint_shares,
                    max(endpoint_shares),
                ),
                ("capped_square_level_2_minimum", capped_values, min(capped_values)),
                ("capped_square_level_2_maximum", capped_values, max(capped_values)),
            ):
                self.assertEqual(as_fraction(summary[name]["value"]), target)
                self.assertEqual(
                    summary[name]["ranks"],
                    [rank for rank, value in enumerate(values) if value == target],
                )
            maximum_rank, maximum_value = expected_endpoint_maxima[q]
            self.assertEqual(
                summary["endpoint_fourth_share_maximum"]["ranks"], [maximum_rank]
            )
            self.assertEqual(
                as_fraction(summary["endpoint_fourth_share_maximum"]["value"]),
                maximum_value,
            )
            self.assertIn(str(maximum_value), note)
            first_decrease = summary["first_raw_fourth_moment_decrease"]
            self.assertEqual(
                (first_decrease["from_rank"], first_decrease["to_rank"]),
                expected_first_decreases[q],
            )
            for token in expected_display_ranges[q]:
                self.assertIn(token, note)
            for name, values, direction in (
                ("first_raw_fourth_moment_decrease", fourth_values, "decrease"),
                (
                    "first_capped_square_level_2_decrease",
                    capped_values,
                    "decrease",
                ),
                (
                    "first_capped_square_level_2_increase",
                    capped_values,
                    "increase",
                ),
            ):
                from_rank, to_rank, from_value, to_value = first_change(
                    values, direction
                )
                certificate = summary[name]
                self.assertEqual(certificate["from_rank"], from_rank)
                self.assertEqual(certificate["to_rank"], to_rank)
                self.assertEqual(as_fraction(certificate["from_value"]), from_value)
                self.assertEqual(as_fraction(certificate["to_value"]), to_value)
            for rank in (8, 16, 32):
                self.assertEqual(
                    summary["Haar_scaled_moment_snapshots"][str(rank)],
                    rows[rank]["haar_boundary_scalings"],
                )

            expected_resonances = []
            for trace, count in subject.EXPECTED_HISTOGRAMS[q].items():
                if trace == 0:
                    continue
                zero_ranks = [
                    rank
                    for rank in range(subject.RANK_CAP + 1)
                    if independent_symmetric_power_trace(trace, q, rank) == 0
                ]
                if zero_ranks:
                    expected_resonances.append(
                        {
                            "trace": trace,
                            "source_count": count,
                            "zero_ranks_through_cap": zero_ranks,
                        }
                    )
            self.assertEqual(
                summary["nonzero_trace_zero_resonances"], expected_resonances
            )

    def test_fixed_q_scaling_obstruction_and_common_tail_cutoff(self) -> None:
        for q_row in self.by_q.values():
            bound_square = as_fraction(
                q_row["extreme_observed_source_trace_classes"][
                    "uniform_character_square_upper_bound"
                ]
            )
            for row in q_row["rank_rows_0_through_32"]:
                self.assertLessEqual(
                    as_fraction(row["raw_even_moments"]["4"]), bound_square**2
                )
                self.assertLessEqual(
                    as_fraction(row["raw_even_moments"]["6"]), bound_square**3
                )
                self.assertEqual(row["strict_tail_abs_gt"]["4"]["count"], 0)
        comparator = self.fixture["fixed_q_versus_Haar_high_rank"]
        self.assertIn(
            "division by r+1 is exactly 1",
            comparator["Haar_comparator"]["fourth_moment"],
        )
        self.assertIn("neither assumes nor proves", comparator["interpretation"])

    def test_source_locks_payload_hash_caps_and_no_floats(self) -> None:
        source_text = subject.SOURCE_FIXTURE.read_text(encoding="utf-8").replace(
            "\r\n", "\n"
        )
        self.assertEqual(
            hashlib.sha256(source_text.encode()).hexdigest(),
            subject.EXPECTED_SOURCE_FILE_SHA256_LF,
        )
        source = json.loads(source_text)
        unhashed_source = dict(source)
        source_payload_hash = unhashed_source.pop("payload_sha256")
        self.assertEqual(source_payload_hash, subject.EXPECTED_SOURCE_PAYLOAD_SHA256)
        self.assertEqual(
            source_payload_hash, subject._canonical_sha256(unhashed_source)
        )
        self.assertEqual(
            subject._lf_sha256(subject.HAAR_NOTE),
            subject.EXPECTED_HAAR_NOTE_SHA256_LF,
        )
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["source_histogram_atoms_consumed"], 27)
        self.assertEqual(resources["transformed_source_atom_visits"], 891)
        self.assertLessEqual(
            resources["transformed_source_atom_visits"],
            resources["transformed_source_atom_cap"],
        )
        self.assertIn("reuse the same 891", resources["cap_semantics"])
        self.assertEqual(resources["new_finite_field_or_curve_enumerations"], 0)
        with mock.patch.object(
            subject,
            "symmetric_power_trace",
            wraps=subject.symmetric_power_trace,
        ) as traced_transform:
            self.assertEqual(subject.build_fixture(), self.fixture)
            self.assertEqual(traced_transform.call_count, 891)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(self.fixture)
        for invalid_cap in (subject.RANK_CAP - 1, subject.RANK_CAP + 1):
            with (
                self.subTest(rank_cap=invalid_cap),
                self.assertRaisesRegex(ValueError, "locked cap"),
            ):
                subject.build_fixture(invalid_cap)

    def test_tampered_sources_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temporary_source = Path(directory) / "source.json"
            text = subject.SOURCE_FIXTURE.read_text(encoding="utf-8")
            temporary_source.write_text(
                text.replace('"-3": 1', '"-3": 2', 1), encoding="utf-8"
            )
            with self.assertRaisesRegex(RuntimeError, "file hash changed"):
                subject.build_fixture(source_fixture=temporary_source)

            temporary_note = Path(directory) / "haar.md"
            temporary_note.write_text(
                subject.HAAR_NOTE.read_text(encoding="utf-8") + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(RuntimeError, "Haar note hash changed"):
                subject.build_fixture(haar_note=temporary_note)

    def test_stored_fixture_and_normal_optimized_cli_replay(self) -> None:
        stored_path = FUNCTION_FIELD / "genus1_qr_symmetric_power_phase_diagram.json"
        stored = json.loads(stored_path.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        self.assertEqual(subject.build_fixture(), self.fixture)
        producer = self.fixture["producer"]
        for path, field in (
            (Path(subject.__file__), "source_sha256_lf_normalized"),
            (
                FUNCTION_FIELD / "GENUS1_QR_SYMMETRIC_POWER_PHASE_DIAGRAM.md",
                "note_sha256_lf_normalized",
            ),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            self.assertEqual(producer[field], subject._lf_sha256(path))
        for optimize in (False, True):
            command = [sys.executable]
            if optimize:
                command.append("-O")
            command.extend([str(Path(subject.__file__)), "--check", str(stored_path)])
            completed = subprocess.run(
                command, capture_output=True, text=True, check=False, timeout=30
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertIn("OK: exact q-r phase diagram", completed.stdout)


if __name__ == "__main__":
    unittest.main()
