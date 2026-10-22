from __future__ import annotations

import math
from pathlib import Path
import sys
import unittest

CODE = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE))

from phase_speiser_localization import (  # noqa: E402
    critical_point_field_integral,
    critical_point_poisson_field,
    critical_point_signed_index,
    finite_horizon_factor,
    finite_horizon_leakage_bound,
    finite_resolvent_energy,
    normalized_gamma_weight,
    prime_knot_jump,
    soft_band_scales,
)


class PhaseSpeiserLocalizationTests(unittest.TestCase):
    def test_prime_knot_signs(self) -> None:
        value = math.log(3.0) / math.sqrt(9.0)
        self.assertAlmostEqual(prime_knot_jump(2, math.log(3.0), 9), -value)
        self.assertAlmostEqual(prime_knot_jump(3, math.log(3.0), 9), value)

    def test_poisson_signed_index(self) -> None:
        points = (complex(-2, 0), complex(-1, 3), complex(4, -2))
        self.assertEqual(critical_point_signed_index(0.0, points), 1)
        self.assertAlmostEqual(critical_point_field_integral(0.0, points), math.pi)
        self.assertGreater(critical_point_poisson_field(0.0, 0.0, points), 0.0)

    def test_right_critical_points_give_negative_field(self) -> None:
        points = (complex(1, -2), complex(2, 0), complex(3, 5))
        for t in (-10.0, -1.0, 0.0, 2.0, 20.0):
            self.assertLess(critical_point_poisson_field(t, 0.0, points), 0.0)

    def test_soft_band_ratio(self) -> None:
        a, w, W, center, m = 1.0, 0.5, 3.0, 20.0, 6
        d_in, _d_out, eta = soft_band_scales(a, w, W)
        inside = normalized_gamma_weight(
            complex(0.49, center + w),
            a=a,
            center=center,
            m=m,
            d_in=d_in,
        )
        outside = normalized_gamma_weight(
            complex(-0.49, center + W),
            a=a,
            center=center,
            m=m,
            d_in=d_in,
        )
        self.assertGreaterEqual(abs(inside), 1.0 - 1e-12)
        self.assertLessEqual(abs(outside), eta**m * (1.0 + 1e-12))

    def test_finite_horizon_factor(self) -> None:
        self.assertAlmostEqual(finite_horizon_factor(0.0, 4.0), 2.0)
        self.assertAlmostEqual(
            finite_horizon_leakage_bound(
                0.25,
                sigma=0.5,
                horizon=4.0,
            ),
            0.5,
        )

    def test_filtered_energy_boundary(self) -> None:
        lambdas = (complex(0.2, 1), complex(0.2, -1))
        energy = finite_resolvent_energy(
            0.3,
            lambdas,
            q=complex(1.0, 2.0),
            m=2,
        )
        self.assertGreater(energy, 0.0)
        with self.assertRaises(ValueError):
            finite_resolvent_energy(
                0.2,
                lambdas,
                q=complex(1.0, 2.0),
                m=2,
            )


if __name__ == "__main__":
    unittest.main()
