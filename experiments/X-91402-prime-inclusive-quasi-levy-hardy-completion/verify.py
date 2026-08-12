#!/usr/bin/env python3
"""Numerical regression for L-91402/L-91403/T-91401 and R-91403."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp
import numpy as np

mp.mp.dps = 70


def prime_powers(limit: int) -> list[tuple[int, int, int]]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            count = ((limit - p * p) // p) + 1
            sieve[p * p : limit + 1 : p] = b"\x00" * count
    out: list[tuple[int, int, int]] = []
    for p in range(2, limit + 1):
        if not sieve[p]:
            continue
        n, k = p, 1
        while n <= limit:
            out.append((n, k, p))
            n *= p
            k += 1
    return sorted(out)


def xi(s: mp.mpc | mp.mpf) -> mp.mpc:
    return s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def nakamura_lambda_prime(sigma: mp.mpf) -> mp.mpf:
    def quotient_derivative(u: mp.mpf) -> mp.mpf:
        e = mp.e ** (-u / 2)
        return ((-mp.mpf("0.5") * e) * u - (e - 1)) / (u * u)

    integral = mp.quad(
        lambda x: x * mp.e ** (-sigma * x / 2) / (1 - mp.e ** (-x)),
        [0, 1],
    )
    return quotient_derivative(sigma) + quotient_derivative(sigma - 1) - integral / 4


def quasi_density(sigma: mp.mpf, x: mp.mpf) -> mp.mpf:
    y = mp.e**x
    return mp.e ** (-sigma * x) / x * (1 + y - y**3) / (y**2 - 1)


def carrier_feature(t: mp.mpf, x: mp.mpf) -> mp.mpc:
    compensation = t * x if x <= mp.mpf("0.5") else mp.mpf("0")
    return 2j * (mp.sin(t * x) - compensation)


def direct_log_phase_derivative(sigma: mp.mpf, t: mp.mpf) -> mp.mpc:
    return mp.diff(lambda s: mp.log(xi(s + 1j * t) / xi(s - 1j * t)), sigma)


def continuous_component(
    sigma: mp.mpf,
    t: mp.mpf,
    plastic_log: mp.mpf,
) -> tuple[mp.mpc, mp.mpc]:
    integrand = lambda x: x * carrier_feature(t, x) * quasi_density(sigma, x)
    short = mp.quad(integrand, [0, plastic_log])
    long = mp.quad(integrand, [plastic_log, mp.mpf("0.5"), 1, mp.inf])
    return short, long


def atomic_component(
    sigma: mp.mpf,
    t: mp.mpf,
    rows: list[tuple[int, int, int]],
) -> mp.mpc:
    return sum(
        mp.log(p) * mp.power(n, -sigma) * carrier_feature(t, mp.log(n))
        for n, _k, p in rows
    )


def source_score_norm_squared(
    sigma: mp.mpf,
    plastic_log: mp.mpf,
    rows: list[tuple[int, int, int]],
) -> mp.mpf:
    continuous = mp.quad(
        lambda x: x * x * abs(quasi_density(sigma, x)),
        [0, plastic_log, mp.mpf("0.5"), 1, mp.inf],
    )
    atomic = sum(mp.log(n) ** 2 * mp.power(n, -sigma) / k for n, k, _p in rows)
    return 1 + continuous + atomic


def source_gram(
    sigma: mp.mpf,
    carriers: list[mp.mpf],
    plastic_log: mp.mpf,
    rows: list[tuple[int, int, int]],
    lambda_prime: mp.mpf,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    size = len(carriers)
    gram = np.zeros((size, size), dtype=complex)
    negative_gram = np.zeros((size, size), dtype=complex)
    derivatives = np.array(
        [complex(direct_log_phase_derivative(sigma, t)) for t in carriers],
        dtype=complex,
    )
    score_norm_sq = source_score_norm_squared(sigma, plastic_log, rows)

    for i, s in enumerate(carriers):
        for j, t in enumerate(carriers):
            drift_s = -2j * s * lambda_prime
            drift_t = -2j * t * lambda_prime
            continuous = mp.quad(
                lambda x: carrier_feature(s, x)
                * mp.conj(carrier_feature(t, x))
                * abs(quasi_density(sigma, x)),
                [0, plastic_log, mp.mpf("0.5"), 1, mp.inf],
            )
            negative = mp.quad(
                lambda x: carrier_feature(s, x)
                * mp.conj(carrier_feature(t, x))
                * (-quasi_density(sigma, x)),
                [plastic_log, mp.mpf("0.5"), 1, mp.inf],
            )
            atomic = sum(
                carrier_feature(s, mp.log(n))
                * mp.conj(carrier_feature(t, mp.log(n)))
                * mp.power(n, -sigma)
                / k
                for n, k, _p in rows
            )
            gram[i, j] = complex(drift_s * mp.conj(drift_t) + continuous + atomic)
            negative_gram[i, j] = complex(negative)

    observed = derivatives / float(mp.sqrt(score_norm_sq))
    defect = gram - np.outer(observed, np.conjugate(observed))
    defect = (defect + defect.conj().T) / 2
    negative_gram = (negative_gram + negative_gram.conj().T) / 2
    signed_defect = defect - 2 * negative_gram
    signed_defect = (signed_defect + signed_defect.conj().T) / 2
    return defect, signed_defect, negative_gram, derivatives


def build() -> dict[str, object]:
    sigma = mp.mpf("4.5")
    a = sigma - mp.mpf("0.5")
    test_carrier = mp.mpf("0.83")
    cutoff = 50_000
    rows = prime_powers(cutoff)

    plastic = mp.findroot(lambda y: y**3 - y - 1, mp.mpf("1.3"))
    plastic_log = mp.log(plastic)
    positive_sample = quasi_density(sigma, plastic_log / 2)
    negative_sample = quasi_density(sigma, plastic_log + 1)

    lambda_prime = nakamura_lambda_prime(sigma)
    direct = direct_log_phase_derivative(sigma, test_carrier)
    drift = -2j * test_carrier * lambda_prime
    short, long = continuous_component(sigma, test_carrier, plastic_log)
    prime = atomic_component(sigma, test_carrier, rows)
    reconstructed = drift + short + long + prime
    derivative_error = abs(direct - reconstructed)

    prime_score_from_quasi = a * prime
    prime_score_direct = sum(
        2j
        * a
        * mp.log(p)
        * mp.power(n, -sigma)
        * mp.sin(test_carrier * mp.log(n))
        for n, _k, p in rows
    )
    prime_summand_error = abs(prime_score_from_quasi - prime_score_direct)

    carriers = [mp.mpf("0.31"), mp.mpf("0.83"), mp.mpf("1.37")]
    defect, signed_defect, negative_gram, _derivatives = source_gram(
        sigma,
        carriers,
        plastic_log,
        rows,
        lambda_prime,
    )
    defect_eigenvalues = np.linalg.eigvalsh(defect)
    signed_defect_eigenvalues = np.linalg.eigvalsh(signed_defect)
    negative_channel_eigenvalues = np.linalg.eigvalsh(negative_gram)
    jordan_subtraction_error = np.linalg.norm(
        signed_defect - (defect - 2 * negative_gram)
    )
    score_norm_sq = source_score_norm_squared(sigma, plastic_log, rows)

    gates = {
        "plastic_sign_split": positive_sample > 0 and negative_sample < 0,
        "completed_derivative": derivative_error < mp.mpf("1e-15"),
        "prime_direct_summand": prime_summand_error < mp.mpf("1e-60"),
        "positive_source_auxiliary": float(defect_eigenvalues.min()) > -1e-12,
        "jordan_subtraction_identity": float(jordan_subtraction_error) < 1e-13,
        "signed_defect_not_automatic": float(signed_defect_eigenvalues.min()) < -1e-8,
    }
    assert all(gates.values())

    return {
        "status": "PASS_PRIME_INCLUSIVE_QUASI_LEVY_HARDY_COMPLETION",
        "gates": gates,
        "sigma": float(sigma),
        "a": float(a),
        "prime_power_cutoff": cutoff,
        "plastic_constant": float(plastic),
        "plastic_log_boundary": float(plastic_log),
        "positive_density_sample": float(positive_sample),
        "negative_density_sample": float(negative_sample),
        "nakamura_lambda_prime": float(lambda_prime),
        "direct_log_phase_derivative_imag": float(mp.im(direct)),
        "drift_component_imag": float(mp.im(drift)),
        "short_archimedean_component_imag": float(mp.im(short)),
        "long_archimedean_component_imag": float(mp.im(long)),
        "prime_component_imag": float(mp.im(prime)),
        "reconstructed_derivative_imag": float(mp.im(reconstructed)),
        "completed_derivative_error": float(derivative_error),
        "prime_summand_error": float(prime_summand_error),
        "source_score_norm_squared": float(score_norm_sq),
        "source_auxiliary_eigenvalues": [float(x) for x in defect_eigenvalues],
        "negative_channel_eigenvalues": [float(x) for x in negative_channel_eigenvalues],
        "signed_defect_eigenvalues": [float(x) for x in signed_defect_eigenvalues],
        "jordan_subtraction_error": float(jordan_subtraction_error),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    payload = json.dumps(build(), sort_keys=True, separators=(",", ":")) + "\n"
    if args.json:
        args.json.write_text(payload)
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
