"""Directed arithmetic certificate for the 32-mode Weil matrix in the companion note."""

import hashlib
import json
from math import isqrt

import flint
from flint import arb, ctx


PRIME_CUTOFF = 50000
MODE_COUNT = 32
PRECISION = 160


def prime_power_stream(limit):
    is_prime = bytearray([1]) * (limit + 1)
    is_prime[:2] = bytes(2)
    for prime in range(2, isqrt(limit) + 1):
        if is_prime[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                is_prime[multiple] = 0
    stream = []
    for prime in range(2, limit + 1):
        if not is_prime[prime]:
            continue
        power = prime
        while power <= limit:
            stream.append((power, prime))
            power *= prime
    stream.sort()

    # The integer identity prod_{q|n, q a prime power} base(q)=n authenticates
    # the complete finite stream used by the weighted matrix.
    products = [1] * (limit + 1)
    for power, prime in stream:
        for multiple in range(power, limit + 1, power):
            products[multiple] *= prime
    if any(products[n] != n for n in range(1, limit + 1)):
        raise ArithmeticError("Prime-power coverage check failed")
    return stream


def positive_pivots(matrix):
    """Symmetric Schur elimination. Every pivot must have positive lower endpoint."""
    size = len(matrix)
    pivots = []
    for j in range(size):
        pivot = matrix[j][j]
        if not pivot > 0:
            raise ArithmeticError(f"Uncertified pivot at index {j}: {pivot}")
        pivots.append(pivot)
        for i in range(j + 1, size):
            factor = matrix[i][j] / pivot
            for k in range(j + 1, i + 1):
                matrix[i][k] -= factor * matrix[k][j]
    return pivots


def main():
    ctx.prec = PRECISION
    cutoff = PRIME_CUTOFF
    dimension = MODE_COUNT
    pi = arb.pi()
    width = arb(cutoff).log()
    center = 2 * pi * cutoff
    frequencies = [
        center + (2 * j - dimension + 1) * pi / width
        for j in range(dimension)
    ]
    stream = prime_power_stream(cutoff)
    sine_sum = [arb(0) for _ in frequencies]
    diagonal_sum = [arb(0) for _ in frequencies]
    checked_pairs = [(0, 31), (1, 3), (12, 13), (9, 22)]
    overlap_sum = {pair: arb(0) for pair in checked_pairs}
    for power, prime in stream:
        log_power = arb(power).log()
        log_fraction = log_power / width
        weight = arb(prime).log() / arb(power).sqrt()
        for j, frequency in enumerate(frequencies):
            sine, cosine = (frequency * log_power).sin_cos()
            sine_sum[j] += weight * sine
            diagonal_sum[j] += 2 * weight * (1 - log_fraction) * cosine
        for j, k in checked_pairs:
            diff = j - k
            phase = (frequencies[j] + frequencies[k]) * log_power / 2
            overlap = (pi * diff * (1 - log_fraction)).sinc()
            overlap_sum[j, k] += (
                2 * weight * (1 - log_fraction) * phase.cos() * overlap
            )

    threshold = arb(3) / 20
    matrix = [[arb(0) for _ in frequencies] for _ in frequencies]
    for j in range(dimension):
        matrix[j][j] = width - diagonal_sum[j] - threshold
        for k in range(j):
            matrix[j][k] = (sine_sum[j] - sine_sum[k]) / (pi * (j - k))
    for j, k in checked_pairs:
        direct_prime = overlap_sum[j, k] * (-1 if (j - k) % 2 else 1)
        if not (direct_prime + matrix[k][j]).contains(0):
            raise ArithmeticError("Direct autocorrelation check failed")
    pivots = positive_pivots(matrix)

    frequency_width = (dimension - 1) * pi / width
    near_radius = center / 50
    cutoff_transition = arb(1) / cutoff**3
    gram_loss = 4 * dimension * cutoff_transition / width
    tail_mass = 4 * dimension / (pi * width * (near_radius - frequency_width))
    near_gamma = (1 - near_radius / center).log() - 4 / (3 * (center - near_radius))
    # mu is at least width+near_gamma in the central band, and at least -7 everywhere.
    gamma_loss = -near_gamma + (width + near_gamma) * gram_loss
    gamma_loss += (width + near_gamma + 7) * tail_mass
    pole_loss = 8 * dimension * arb(cutoff).sqrt() / (width * (center - frequency_width)**2)
    # Use sum_{n<=cutoff} Lambda(n)/sqrt(n) <= cutoff*log(cutoff).
    smooth_prime_loss = 16 * dimension * cutoff * cutoff_transition
    total_loss = gamma_loss + pole_loss + smooth_prime_loss
    guaranteed_gap = threshold - total_loss
    if not guaranteed_gap > arb(1) / 10:
        raise ArithmeticError("Final arithmetic lower bound failed")
    stream_bytes = "".join(f"{power}\t{prime}\n" for power, prime in stream).encode()
    print(json.dumps({
        "python_flint": flint.__version__,
        "precision_bits": PRECISION,
        "prime_cutoff": cutoff,
        "mode_count": dimension,
        "prime_powers": len(stream),
        "stream_sha256": hashlib.sha256(stream_bytes).hexdigest(),
        "checked_autocorrelations": len(checked_pairs),
        "positive_pivots": len(pivots),
        "minimum_pivot_lower_in_thousandths": int((1000 * min(p.lower() for p in pivots)).floor().fmpz()),
        "gamma_loss_enclosure": gamma_loss.str(12),
        "pole_loss_enclosure": pole_loss.str(12),
        "smooth_prime_loss_enclosure": smooth_prime_loss.str(12),
        "resulting_gap_enclosure": guaranteed_gap.str(12),
        "strict_certified_lower_bound": "1/10",
    }, indent=2))


if __name__ == "__main__":
    main()
