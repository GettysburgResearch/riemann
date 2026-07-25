from fractions import Fraction as Q
import importlib.util
from pathlib import Path
import sys
import unittest

SPEC = importlib.util.spec_from_file_location(
    "verify_toeplitz_box",
    Path(__file__).parents[1] / "verify_toeplitz_box.py",
)
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def fraction(value: Q) -> dict[str, str]:
    value = Q(value)
    return {
        "numerator": str(value.numerator),
        "denominator": str(value.denominator),
    }


def interval(lower: Q, upper: Q | None = None) -> dict[str, object]:
    if upper is None:
        upper = lower
    return {
        "lower": fraction(lower),
        "upper": fraction(upper),
    }


def gaussian(real: Q, imag: Q = Q(0)) -> dict[str, object]:
    return {
        "real": fraction(real),
        "imag": fraction(imag),
    }


def certificate(
    dimension: int,
    lags: list[tuple[Q | tuple[Q, Q], Q | tuple[Q, Q]]],
    *,
    alpha: Q = Q(0),
    correction: Q = Q(0),
    checks: list[dict[str, object]] | None = None,
) -> dict[str, object]:
    rows = []
    for lag, (real, imag) in enumerate(lags):
        real_box = interval(*real) if isinstance(real, tuple) else interval(real)
        imag_box = interval(*imag) if isinstance(imag, tuple) else interval(imag)
        rows.append(
            {
                "lag": lag,
                "real_interval": real_box,
                "imag_interval": imag_box,
            }
        )
    return {
        "schema": MOD.SCHEMA,
        "dimension": dimension,
        "alpha_interval": interval(alpha),
        "correction_operator_radius": fraction(correction),
        "lags": rows,
        "checks": checks or [],
    }


class ToeplitzBoxTests(unittest.TestCase):
    def test_fixed_vector_matches_direct_dense_form(self) -> None:
        data = certificate(
            2,
            [(Q(1), Q(0)), (Q(2), Q(0))],
            checks=[
                {
                    "id": "fixed",
                    "kind": "fixed-vector",
                    "vector": [gaussian(1, 1), gaussian(2, -1)],
                }
            ],
        )
        checked = MOD.verify(data)["checks"][0]
        # S=[[1,1],[1,1]], H=-S. For v=(1+i,2-i),
        # v*Hv=-|sum(v)|^2=-9.
        lower = MOD.fraction(checked["full_interval"]["lower"], "lower")
        upper = MOD.fraction(checked["full_interval"]["upper"], "upper")
        self.assertEqual(lower, Q(-9))
        self.assertEqual(upper, Q(-9))
        self.assertEqual(checked["status"], "CERTIFIED_NEGATIVE_MATRIX")

    def test_gram_cancels_shared_lag_uncertainty(self) -> None:
        # H=-S, c0=1/10 exact, c1 in [-1,1]. The two individual
        # intervals are unresolved. Their positive Gram sum has aggregate
        # lag-one autocorrelation exactly zero and certifies trace=-2/5.
        checks = [
            {
                "id": "plus",
                "kind": "fixed-vector",
                "vector": [gaussian(1), gaussian(1)],
            },
            {
                "id": "minus",
                "kind": "fixed-vector",
                "vector": [gaussian(1), gaussian(-1)],
            },
            {
                "id": "gram",
                "kind": "gram-portfolio",
                "terms": [
                    {
                        "weight": fraction(1),
                        "vector": [gaussian(1), gaussian(1)],
                    },
                    {
                        "weight": fraction(1),
                        "vector": [gaussian(1), gaussian(-1)],
                    },
                ],
            },
        ]
        data = certificate(
            2,
            [(Q(1, 10), Q(0)), ((Q(-1), Q(1)), Q(0))],
            checks=checks,
        )
        results = MOD.verify(data)["checks"]
        self.assertEqual(results[0]["status"], "UNRESOLVED")
        self.assertEqual(results[1]["status"], "UNRESOLVED")
        self.assertEqual(results[2]["status"], "CERTIFIED_NEGATIVE_MATRIX")
        upper = MOD.fraction(results[2]["full_interval"]["upper"], "upper")
        self.assertEqual(upper, Q(-2, 5))

    def test_whole_matrix_positive_control(self) -> None:
        # H=2I-S and S=I, so H=I. The exact delta=1/2 certificate succeeds.
        data = certificate(
            2,
            [(Q(1), Q(0)), (Q(0), Q(0))],
            alpha=Q(2),
            checks=[
                {
                    "id": "whole",
                    "kind": "whole-matrix-positive",
                    "delta": fraction(Q(1, 2)),
                }
            ],
        )
        checked = MOD.verify(data)["checks"][0]
        self.assertEqual(checked["status"], "CERTIFIED_POSITIVE_DEFINITE")

    def test_negative_gram_weight_is_rejected(self) -> None:
        data = certificate(
            1,
            [(Q(0), Q(0))],
            checks=[
                {
                    "id": "bad",
                    "kind": "gram-portfolio",
                    "terms": [
                        {
                            "weight": fraction(-1),
                            "vector": [gaussian(1)],
                        }
                    ],
                }
            ],
        )
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)

    def test_duplicate_check_id_is_rejected(self) -> None:
        data = certificate(
            1,
            [(Q(0), Q(0))],
            checks=[
                {"id": "x", "kind": "fixed-vector", "vector": [gaussian(1)]},
                {"id": "x", "kind": "fixed-vector", "vector": [gaussian(1)]},
            ],
        )
        with self.assertRaises(MOD.CertificateError):
            MOD.verify(data)


if __name__ == "__main__":
    unittest.main()
