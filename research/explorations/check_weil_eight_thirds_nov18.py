"""Positive supersolution for the compressed prime translations at radius 41/15."""

import hashlib
import json
from fractions import Fraction

import flint
from flint import arb, ctx

from check_weil_50000_nov18 import prime_power_stream


def apply_row_majorant(vector, shifts):
    cells = len(vector)
    result = [0] * cells
    maxima = [vector[0]] + [
        max(vector[i - 1], vector[i]) for i in range(1, cells)
    ] + [vector[-1]]
    for shift, weight in shifts:
        for i in range(cells - shift):
            result[i] += weight * maxima[i + shift + 1]
            result[i + shift] += weight * maxima[i]
    return result


def main():
    ctx.prec = 160
    cells = 1024
    denominator = 10**8
    radius = arb(41) / 15
    limit = int((2 * radius).exp().floor().fmpz())
    powers = prime_power_stream(limit)
    shifts = []
    for power, prime in powers:
        displacement = arb(power).log() * cells / (2 * radius)
        shift = int(displacement.floor().fmpz())
        weight = int((denominator * arb(prime).log() / arb(power).sqrt()).ceil().fmpz())
        shifts.append((shift, weight))
    # The iterations only propose a positive integer vector. The last row test
    # certifies it independently of convergence or any eigenvector hypothesis.
    width = 10**6
    vector = [width] * cells
    for _ in range(90):
        rows = apply_row_majorant(vector, shifts)
        next_vector = [r + 18 * denominator * v for r, v in zip(rows, vector)]
        maximum = max(next_vector)
        vector = [width * v // maximum for v in next_vector]
    assert min(vector) > 0
    rows = apply_row_majorant(vector, shifts)
    schur = max(Fraction(r, denominator * v) for r, v in zip(rows, vector))
    if not schur < Fraction(87, 5):
        raise ArithmeticError(f"Uncertified Schur bound: {schur}")

    # Scalar budgets in the accompanying proof. Powers with billion-sized
    # exponents are compared in logarithmic form using positive Arb inputs.
    L = arb(8) / 3
    m = 3_600_000_000
    R = 90 * m
    T = 3_000_175_332_800
    t1 = 255_000_000
    pi = arb.pi()
    M = int(2 * 8 * R // 3) + 1
    base = arb(1).exp() * (M + 2 * m) / (2 * m)
    prefactor = (M + 2 * m) * (2 * m + 1)
    floor_log = -arb(prefactor).log() - 2 * m * base.log()
    gamma_at_cut = (arb(t1) / (2 * pi)).log() - arb(4) / (3 * t1)
    if not gamma_at_cut > arb(87) / 5 + arb(1) / 10:
        raise ArithmeticError("Archimedean threshold failed")
    low_base = (arb(8) / 3).sqrt() * t1 / R
    high_base = 9 * (arb(1001) * R / (1000 * T))**4
    norm_square_bound = 2 * L * L.exp()
    low_loss_log = arb(52).log() + 2 * m * low_base.log()
    pole_loss_log = (16 * norm_square_bound).log() + m * arb(8).log() - 2 * m * arb(R).log()
    high_loss_log = (20 * norm_square_bound * T * arb(2*T).log()).log() + 2 * m * high_base.log()
    target_log = floor_log - arb(60).log()
    if not all(error < target_log for error in (low_loss_log, pole_loss_log, high_loss_log)):
        raise ArithmeticError("One of the three loss budgets failed")
    vector_hash = hashlib.sha256(",".join(map(str, vector)).encode()).hexdigest()
    print(json.dumps({
        "python_flint": flint.__version__,
        "precision_bits": ctx.prec,
        "cell_count": cells,
        "prime_power_cutoff": limit,
        "prime_powers": len(powers),
        "schur_ratio": str(schur),
        "schur_enclosure": (arb(schur.numerator) / schur.denominator).str(12),
        "integer_supersolution_sha256": vector_hash,
        "gamma_lower_enclosure_at_cut": gamma_at_cut.str(12),
        "floor_base_enclosure": base.str(12),
        "low_base_enclosure": low_base.str(12),
        "exterior_base_enclosure": high_base.str(12),
        "all_three_losses_below_floor_over_60": True
    }, indent=2))


if __name__ == "__main__":
    main()
