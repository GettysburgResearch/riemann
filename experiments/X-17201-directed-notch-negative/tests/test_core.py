from __future__ import annotations

import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from filter_core import (  # noqa: E402
    FilterSpec,
    convolution_square_density_interval,
    log_integer_interval,
    manifest_digest,
    prime_power_events,
    reciprocal_sqrt_integer_interval,
    standard_spec,
)
from rh_bound import certificate, trivial_zero_bound, zero_sum_bound  # noqa: E402


Q = Fraction


class ExactCoreTests(unittest.TestCase):
    def test_log_enclosures(self) -> None:
        for n in (1, 2, 3, 17, 10_000_019):
            lo, hi = log_integer_interval(n, 50)
            target = math.log(n)
            self.assertLessEqual(float(lo), target)
            self.assertGreaterEqual(float(hi), target)
            self.assertLess(float(hi - lo), 1e-40)

    def test_reciprocal_sqrt_enclosures(self) -> None:
        for n in (1, 2, 9, 99991):
            lo, hi = reciprocal_sqrt_integer_interval(n, 100)
            self.assertLessEqual(n * lo * lo, 1)
            self.assertGreaterEqual(n * hi * hi, 1)

    def test_prime_power_manifest(self) -> None:
        events = prime_power_events(30)
        self.assertEqual(len(events), len(set(events)))
        self.assertIn((8, 2, 3), events)
        self.assertIn((27, 3, 3), events)
        self.assertNotIn((12, 2, 0), events)
        self.assertEqual(
            manifest_digest(events),
            "05d234df0fba874789042651bb2df23eb19245fc7402c3f641593df130856eda",
        )

    def test_one_box_triangular_density(self) -> None:
        widths = (Q(1, 2),)
        self.assertEqual(
            convolution_square_density_interval((Q(1, 4), Q(1, 4)), widths),
            (Q(1), Q(1)),
        )
        self.assertEqual(
            convolution_square_density_interval((Q(1, 2), Q(1, 2)), widths),
            (Q(2), Q(2)),
        )
        self.assertEqual(
            convolution_square_density_interval((Q(3, 4), Q(3, 4)), widths),
            (Q(1), Q(1)),
        )

    def test_notch_support_is_doubled_by_convolution_square(self) -> None:
        base = standard_spec(dyadic_level=3, notch_count=0)
        one = standard_spec(dyadic_level=3, notch_count=1)
        added = one.widths[-1]
        self.assertEqual(one.profile_length - base.profile_length, added)
        base_hi = base.support_max_interval(50)
        one_hi = one.support_max_interval(50)
        self.assertEqual(one_hi[0] - base_hi[0], 2 * added)
        self.assertEqual(one_hi[1] - base_hi[1], 2 * added)

    def test_exact_rh_bound_is_positive_and_reproducible(self) -> None:
        spec = standard_spec(
            dyadic_level=4,
            notch_count=1,
            highpass_order=4,
            highpass_delta=Q(1, 32),
        )
        z1, zd1 = zero_sum_bound(spec)
        z2, zd2 = zero_sum_bound(spec)
        t1, td1 = trivial_zero_bound(spec)
        self.assertEqual(z1, z2)
        self.assertEqual(zd1, zd2)
        self.assertGreater(z1, 0)
        self.assertGreater(t1, 0)
        cert = certificate(spec)
        total = Q(int(cert["B_G"]["numerator"]), int(cert["B_G"]["denominator"]))
        self.assertGreaterEqual(total, z1 + t1)
        self.assertEqual(td1["total_fingerprint"]["decimal"], float(t1))

    def test_filter_shift_ledger_l1_normalization(self) -> None:
        spec = FilterSpec((Q(1, 2), Q(1, 4)), highpass_order=5)
        # Pole difference has absolute coefficient sum 3; normalized repeated
        # difference has absolute coefficient sum 1.
        total = sum(abs(c) for c, _shift, _branch in spec.physical_shift_ledger())
        self.assertEqual(Q(total, 1 << spec.highpass_order), 3)


if __name__ == "__main__":
    unittest.main()
