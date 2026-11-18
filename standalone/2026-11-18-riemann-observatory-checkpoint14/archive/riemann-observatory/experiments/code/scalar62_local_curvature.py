"""Exact sign of the quadratic energy gap at complete coalescence."""
import json
from math import comb
from pathlib import Path


def curvature_numerator(degree, window):
    """Use the common coefficient denominator window**degree."""
    assert degree >= 2 and window >= 1
    residual_negated = [0] * (degree + window)
    moment = [0] * len(residual_negated)
    for k in range(degree + 1):
        elementary = (-1) ** k * comb(degree, k)
        subset_moment = k * (degree - k) * (degree + 1)
        for j in range(window):
            coefficient = elementary * comb(degree + j - 1, j) * (window - j) ** degree
            composition_moment = j * (j + degree) * (degree - 1)
            residual_negated[k + j] += coefficient
            moment[k + j] += coefficient * (subset_moment + composition_moment)
    return sum(c * v for c, v in zip(residual_negated, moment))


def main():
    degrees = list(range(2, 21)) + [24, 32, 48, 64, 96, 128]
    windows = list(range(1, 21)) + [24, 32, 48, 64, 96, 128, 192, 256]
    assert curvature_numerator(2, 1) == 12
    assert curvature_numerator(3, 2) == 4464

    zero = []
    negative = []
    for degree in degrees:
        for window in windows:
            numerator = curvature_numerator(degree, window)
            if numerator == 0:
                zero.append([degree, window])
            if numerator < 0:
                negative.append([degree, window, str(numerator)])

    result = {
        "degrees": degrees,
        "windows": windows,
        "exact_integer_cases": len(degrees) * len(windows),
        "zero": zero,
        "negative": negative,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "scalar62_local_curvature.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
