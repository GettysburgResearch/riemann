from fractions import Fraction
import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from directed_shard import (
    higher_prime_powers,
    interval_json,
    parse_fraction,
    segment_primes,
    simple_primes,
    total_segments,
)
from freeze_finalist import dyadic_round, nearest_integer
from merge import parse_interval
from one_pass_finalize import (
    contract_boxes,
    inspect_shards,
)


class ExactHelperTests(unittest.TestCase):
    def test_nearest_integer_ties_to_even(self) -> None:
        self.assertEqual(nearest_integer(Fraction(1, 2)), 0)
        self.assertEqual(nearest_integer(Fraction(3, 2)), 2)
        self.assertEqual(nearest_integer(Fraction(-1, 2)), 0)
        self.assertEqual(nearest_integer(Fraction(-3, 2)), -2)
        self.assertEqual(dyadic_round(Fraction(1, 3), 4), 5)

    def test_prime_partition(self) -> None:
        base = simple_primes(100)
        whole = segment_primes(2, 1001, base)
        pieces = (
            segment_primes(2, 200, base)
            + segment_primes(200, 700, base)
            + segment_primes(700, 1001, base)
        )
        self.assertEqual(whole, pieces)
        self.assertEqual(len(whole), 168)
        self.assertEqual(whole[-1], 997)

    def test_higher_prime_powers(self) -> None:
        rows = list(higher_prime_powers(1000, simple_primes(31)))
        self.assertEqual(len(rows), len(set(rows)))
        self.assertIn((4, 2), rows)
        self.assertIn((8, 2), rows)
        self.assertIn((9, 3), rows)
        self.assertIn((961, 31), rows)
        self.assertTrue(all(q == p**round(__import__("math").log(q, p)) for q, p in rows))

    def test_segment_count(self) -> None:
        self.assertEqual(total_segments(1000, 100), 10)
        self.assertEqual(total_segments(100_000_000_000, 20_000_000), 5000)
        with self.assertRaises(ValueError):
            total_segments(1, 100)

    def test_interval_round_trip(self) -> None:
        from flint import arb, ctx

        ctx.prec = 128
        value = arb(2).sqrt()
        encoded = interval_json(value)
        lower, upper = parse_interval(encoded)
        self.assertLess(lower, upper)
        self.assertLess(lower * lower, 2)
        self.assertGreater(upper * upper, 2)

    def test_fraction_boolean_rejected(self) -> None:
        with self.assertRaises(ValueError):
            parse_fraction({"numerator": True, "denominator": 1})


class SyntheticSchemaTests(unittest.TestCase):
    def test_synthetic_finalist_shape(self) -> None:
        # The producer's proof input is intentionally simple: one exact vector,
        # its exact correlations, and immutable parameters.  This fixture checks
        # the required dimensional identities without invoking the expensive
        # target source discovery.
        bits = 8
        real = [256, 0, 0, 0]
        imag = [0, 0, 0, 0]
        correlations = []
        for lag in range(4):
            rr = ii = 0
            for index in range(4 - lag):
                rr += real[index] * real[index + lag] + imag[index] * imag[index + lag]
                ii += real[index] * imag[index + lag] - imag[index] * real[index + lag]
            correlations.append({"real_numerator": str(rr), "imag_numerator": str(ii)})
        fixture = {
            "schema": "riemann.piecewise-carrier-finalist.v1",
            "parameters": {
                "cutoff": 1000,
                "cells": 4,
                "carrier": {"numerator": "20", "denominator": "1"},
                "dyadic_bits": bits,
                "autocorrelation_denominator_power": 2 * bits,
            },
            "vector": [
                {"real_numerator": str(r), "imag_numerator": str(i)}
                for r, i in zip(real, imag)
            ],
            "autocorrelations": correlations,
            "norm_squared": {"numerator": "1", "denominator": "1"},
        }
        with tempfile.TemporaryDirectory() as directory:
            path = pathlib.Path(directory) / "finalist.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            loaded = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(len(loaded["vector"]), loaded["parameters"]["cells"])
        self.assertEqual(len(loaded["autocorrelations"]), loaded["parameters"]["cells"])
        self.assertEqual(parse_fraction(loaded["norm_squared"]), 1)


class OnePassCheckpointTests(unittest.TestCase):
    @staticmethod
    def coefficient_shard(
        start: int,
        end: int,
        *,
        include_higher: bool,
    ) -> dict[str, object]:
        prime_count = end - start
        higher_count = int(include_higher)
        zero = "0x0.0p+0"
        return {
            "schema": "riemann.mpfr-toeplitz-box-shard.v1",
            "cutoff": 100,
            "carrier": "20",
            "cells": 2,
            "precision_bits": 80,
            "segment_size": 50,
            "total_segments": 2,
            "segment_start": start,
            "segment_end": end,
            "include_higher_powers": include_higher,
            "prime_count": prime_count,
            "higher_prime_power_count": higher_count,
            "total_terms": prime_count + higher_count,
            "ambiguous_lags": 0,
            "lags": [
                {
                    "lag": lag,
                    "real_lower_hex": zero,
                    "real_upper_hex": zero,
                    "imag_lower_hex": zero,
                    "imag_upper_hex": zero,
                }
                for lag in range(2)
            ],
        }

    def test_partial_and_complete_checkpoint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = pathlib.Path(directory)
            first = root / "shard-0.json"
            second = root / "shard-1.json"
            first.write_text(
                json.dumps(
                    self.coefficient_shard(0, 1, include_higher=True)
                ),
                encoding="utf-8",
            )
            second.write_text(
                json.dumps(
                    self.coefficient_shard(1, 2, include_higher=False)
                ),
                encoding="utf-8",
            )

            _, _, partial = inspect_shards(
                [first], require_complete=False
            )
            self.assertFalse(partial["coverage"]["complete"])
            self.assertEqual(
                parse_fraction(partial["coverage"]["completion_fraction"]),
                Fraction(1, 2),
            )

            _, _, complete = inspect_shards(
                [second, first], require_complete=True
            )
            self.assertTrue(complete["coverage"]["complete"])
            self.assertEqual(complete["coverage"]["prime_count"], 2)
            self.assertEqual(
                complete["coverage"]["higher_prime_power_count"], 1
            )

    def test_exact_box_contraction(self) -> None:
        boxes = (
            [Fraction(1), Fraction(2)],
            [Fraction(1), Fraction(3)],
            [Fraction(0), Fraction(-2)],
            [Fraction(0), Fraction(-1)],
        )
        lower, upper = contract_boxes(
            boxes,
            correlation_real=[1, -2],
            correlation_imag=[0, 3],
            denominator_power=0,
        )
        self.assertEqual(lower, Fraction(-2))
        self.assertEqual(upper, Fraction(3))


if __name__ == "__main__":
    unittest.main()
