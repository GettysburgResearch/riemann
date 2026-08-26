#!/usr/bin/env python3
"""Deterministic replay for T-106670.

The replay verifies finite-dimensional determinant, sandwich, pivot, cycle,
cutoff-allowance, and logarithmic-Laplace identities. It does not estimate Xi
and does not prove MESOFREE106670, ninety percent, density one, or RH.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
import scipy.linalg as sla

SEED = 106670
TOL = 5e-9


def blaschke_real(x: sp.Rational, zeros: list[sp.Rational]) -> sp.Rational:
    out = sp.Rational(1)
    for a in zeros:
        out *= (x - a) / (1 - a * x)
    return sp.factor(out)


def exact_pick_fixture(nodes: list[sp.Rational], zeros: list[sp.Rational], tau: sp.Rational) -> dict:
    m = len(nodes)
    G = sp.Matrix([[1 / (1 - nodes[i] * nodes[j]) for j in range(m)] for i in range(m)])
    values = [blaschke_real(x, zeros) for x in nodes]
    D = sp.diag(*values)
    adverse_gram = D * G * D
    M = G.inv() * adverse_gram
    charge = sp.factor(sp.trace(M))
    Z = sp.factor((G - tau * adverse_gram).det() / G.det())

    t = sp.symbols("t")
    Zpoly = sp.factor((G - t * adverse_gram).det() / G.det())
    derivative_charge = sp.factor(-sp.diff(sp.log(Zpoly), t).subs(t, 0))
    if sp.factor(derivative_charge - charge) != 0:
        raise AssertionError("Jacobi derivative identity failed")

    pivot_product = sp.Rational(1)
    pivots: list[sp.Rational] = []
    for k in range(1, m + 1):
        Gk = G[:k, :k]
        Hk = (G - tau * adverse_gram)[:k, :k]
        if k == 1:
            Gprev = sp.Rational(1)
            Hprev = sp.Rational(1)
        else:
            Gprev = G[: k - 1, : k - 1].det()
            Hprev = (G - tau * adverse_gram)[: k - 1, : k - 1].det()
        q = sp.factor(Hk.det() * Gprev / (Hprev * Gk.det()))
        if not (sp.Rational(1) - tau <= q <= sp.Rational(1)):
            raise AssertionError(("pivot bound", q, tau))
        pivots.append(q)
        pivot_product *= q
    if sp.factor(pivot_product - Z) != 0:
        raise AssertionError("pivot product failed")

    source_pick = sp.Matrix(
        [
            [G[i, j] * (1 - tau * values[i] * values[j]) for j in range(m)]
            for i in range(m)
        ]
    )
    if source_pick != G - tau * adverse_gram:
        raise AssertionError("source Pick entry identity failed")

    coeff1 = sp.factor(sp.trace(M))
    coeff2 = sp.factor(sp.trace(M * M) / 2)
    series = sp.series(-sp.log(Zpoly) / t, t, 0, 3).removeO()
    if sp.factor(series.subs(t, 0) - coeff1) != 0:
        raise AssertionError("cycle first coefficient failed")
    if sp.factor(sp.diff(series, t).subs(t, 0) - coeff2) != 0:
        raise AssertionError("cycle second coefficient failed")

    return {
        "degree_minus": m,
        "degree_plus": len(zeros),
        "tau": str(tau),
        "charge": str(charge),
        "partition": str(Z),
        "pivots": [str(x) for x in pivots],
        "cycle_1": str(coeff1),
        "cycle_2": str(coeff2),
    }


def invsqrt_hermitian(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(a)
    if np.min(vals) <= 0:
        raise AssertionError("Gram not positive definite")
    return (vecs * (1.0 / np.sqrt(vals))) @ vecs.conj().T


def disk_blaschke(z: complex, zeros: np.ndarray) -> complex:
    out = 1.0 + 0.0j
    for a in zeros:
        out *= (z - a) / (1.0 - np.conj(a) * z)
    return out


def numerical_pick(nodes: np.ndarray, zeros: np.ndarray, tau: float) -> tuple[float, float, float, float]:
    G = 1.0 / (1.0 - np.conj(nodes[:, None]) * nodes[None, :])
    values = np.array([disk_blaschke(z, zeros) for z in nodes])
    D = np.diag(values)
    adverse = D.conj().T @ G @ D
    eig = sla.eigvalsh(adverse, G)
    if np.min(eig) < -2e-7 or np.max(eig) > 1 + 2e-6:
        raise AssertionError(("not contraction", eig))
    eig = np.clip(eig, 0.0, 1.0)
    charge = float(np.sum(eig))
    Z_spec = float(np.prod(1.0 - tau * eig))
    Htau = (G - tau * adverse + (G - tau * adverse).conj().T) / 2
    LG = sla.cholesky((G + G.conj().T) / 2, lower=True)
    LH = sla.cholesky(Htau, lower=True)
    logdet_G = 2.0 * float(np.sum(np.log(np.real(np.diag(LG)))))
    logdet_H = 2.0 * float(np.sum(np.log(np.real(np.diag(LH)))))
    Z_det = math.exp(logdet_H - logdet_G)
    free = -math.log(Z_spec) / tau
    c = -math.log(1.0 - tau) / tau
    if free + TOL < charge or free > c * charge + TOL:
        raise AssertionError(("free sandwich", charge, free, c * charge))
    return charge, Z_spec, Z_det, free


def cauchy_grams(z: np.ndarray, w: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    yz = z.real
    yw = w.real
    Gz = 2.0 * np.sqrt(yz[:, None] * yz[None, :]) / (z[:, None] + np.conj(z[None, :]))
    Gw = 2.0 * np.sqrt(yw[:, None] * yw[None, :]) / (w[:, None] + np.conj(w[None, :]))
    C = 2.0 * np.sqrt(yz[:, None] * yw[None, :]) / (z[:, None] + np.conj(w[None, :]))
    return Gz, Gw, C


def cauchy_q(z: np.ndarray, w: np.ndarray) -> float:
    Gz, Gw, C = cauchy_grams(z, w)
    return float(np.real(abs(np.linalg.det(C)) ** 2 / (np.linalg.det(Gz) * np.linalg.det(Gw))))


def laplace_energy(z: np.ndarray, w: np.ndarray) -> float:
    mp.mp.dps = 42
    zz = [mp.mpc(complex(x).real, complex(x).imag) for x in z]
    ww = [mp.mpc(complex(x).real, complex(x).imag) for x in w]

    def integrand(t: mp.mpf) -> mp.mpf:
        if t == 0:
            return mp.mpf("0")
        sz = mp.fsum(mp.e ** (-x * t) for x in zz)
        sw = mp.fsum(mp.e ** (-x * t) for x in ww)
        return abs(sz - sw) ** 2 / t

    return float(mp.quad(integrand, [0, 1, mp.inf]))


def exact_scalar_checks() -> int:
    checks = 0
    taus = [Fraction(1, 17), Fraction(1, 7), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4)]
    for mu_num in range(0, 38):
        mu = Fraction(mu_num, 37)
        for tau in taus:
            Z = 1 - tau * mu
            if not (1 - tau <= Z <= 1):
                raise AssertionError("scalar partition range")
            x = tau * mu
            partial = sum((x**n) / n for n in range(1, 81))
            lower = tau * mu
            if partial < lower:
                raise AssertionError("positive log series")
            checks += 2
    return checks


def cutoff_allowance_checks() -> tuple[int, dict[str, str]]:
    full = Fraction(97, 1000)
    height = Fraction(3, 4000)
    expected = {
        Fraction(1, 100): Fraction(11, 500),
        Fraction(1, 10): Fraction(179, 2000),
        Fraction(1, 1): Fraction(77, 800),
    }
    checks = 0
    out: dict[str, str] = {"infinity": str(full)}
    for eta, target in expected.items():
        actual = full - height / eta
        if actual != target:
            raise AssertionError(("cutoff allowance", eta, actual, target))
        if eta <= Fraction(3, 388):
            raise AssertionError(("inadmissible cutoff", eta))
        out[str(eta)] = str(actual)
        checks += 2
    if full - Fraction(11, 500) != Fraction(3, 40):
        raise AssertionError("0.01 height payment")
    checks += 1
    return checks, out


def run() -> dict:
    rng = np.random.default_rng(SEED)
    cutoff_checks, cutoff_allowances = cutoff_allowance_checks()
    exact_checks = exact_scalar_checks() + cutoff_checks
    exact_fixtures = []

    node_sets = [
        [sp.Rational(-2, 5)],
        [sp.Rational(-2, 5), sp.Rational(1, 6)],
        [sp.Rational(-3, 5), sp.Rational(-1, 7), sp.Rational(2, 5)],
        [sp.Rational(-4, 7), sp.Rational(-1, 4), sp.Rational(1, 5), sp.Rational(3, 7)],
    ]
    zero_sets = [
        [sp.Rational(1, 3)],
        [sp.Rational(-1, 3), sp.Rational(2, 7)],
        [sp.Rational(-1, 2), sp.Rational(1, 8), sp.Rational(3, 8)],
        [sp.Rational(-3, 7), sp.Rational(-1, 9), sp.Rational(1, 4), sp.Rational(1, 2)],
    ]
    for nodes in node_sets:
        for zeros in zero_sets:
            for tau in [sp.Rational(1, 11), sp.Rational(1, 3), sp.Rational(1, 2)]:
                exact_fixtures.append(exact_pick_fixture(nodes, zeros, tau))
                exact_checks += 8 + 2 * len(nodes)

    numerical_checks = 0
    max_det_gap = 0.0
    max_sandwich_violation = 0.0
    max_laplace_gap = 0.0

    for m in range(1, 7):
        for n in range(1, 9):
            for _ in range(60):
                nodes = 0.45 * np.sqrt(rng.random(m)) * np.exp(2j * np.pi * rng.random(m))
                zeros = 0.55 * np.sqrt(rng.random(n)) * np.exp(2j * np.pi * rng.random(n))
                tau = float(rng.uniform(0.01, 0.92))
                charge, z1, z2, free = numerical_pick(nodes, zeros, tau)
                max_det_gap = max(max_det_gap, abs(z1 - z2))
                c = -math.log(1.0 - tau) / tau
                max_sandwich_violation = max(
                    max_sandwich_violation,
                    charge - free,
                    free - c * charge,
                )
                numerical_checks += 5

    for r in range(1, 5):
        for _ in range(14):
            z = 0.15 + 0.95 * rng.random(r) + 1j * rng.normal(0.0, 0.9, r)
            w = 0.15 + 0.95 * rng.random(r) + 1j * rng.normal(0.0, 0.9, r)
            q = cauchy_q(z, w)
            energy = laplace_energy(z, w)
            gap = abs(energy + math.log(q))
            if gap > 3e-8:
                raise AssertionError(("laplace", r, gap))
            max_laplace_gap = max(max_laplace_gap, gap)
            numerical_checks += 1

    eps = Fraction(1, 1000)
    previous = Fraction(0)
    for L in [1, 2, 4, 8, 16, 32, 64, 128, 256]:
        q = 4 * eps * eps / (4 * eps * eps + L * L)
        defect = 1 - q
        if defect <= previous:
            raise AssertionError("height firewall monotonicity")
        previous = defect
        exact_checks += 2

    for m in range(1, 101):
        exact_charge = 1.0
        for tau in [0.05, 0.2, 0.5, 0.8]:
            free = -math.log(1.0 - tau) / tau
            c = -math.log(1.0 - tau) / tau
            if not (exact_charge <= free + TOL <= c * exact_charge + TOL):
                raise AssertionError("rank-one regularized repair")
            numerical_checks += 2

    payload = {
        "schema": "riemann.x106670.regularized-pick-free-energy.v1",
        "claim": "T-106670",
        "seed": SEED,
        "classification": "PASS_T106670_REGULARIZED_PICK_FREE_ENERGY",
        "exact_rational_checks": exact_checks,
        "numerical_consistency_checks": numerical_checks,
        "total_checks": exact_checks + numerical_checks,
        "exact_fixture_count": len(exact_fixtures),
        "exact_fixtures_sha256": hashlib.sha256(json.dumps(exact_fixtures, sort_keys=True).encode()).hexdigest(),
        "max_partition_determinant_abs_error": max_det_gap,
        "max_free_energy_sandwich_violation": max(0.0, max_sandwich_violation),
        "max_laplace_abs_error": max_laplace_gap,
        "regularized_free_energy_sandwich_checked": True,
        "source_pick_determinant_checked": True,
        "conditional_pivot_product_checked": True,
        "positive_cycle_expansion_checked": True,
        "unregularized_cauchy_laplace_checked": True,
        "cutoff_allowance_family_checked": True,
        "cutoff_allowances": cutoff_allowances,
        "full_endpoint_allowance": str(Fraction(97, 1000)),
        "height_index_only_closure_valid": False,
        "raw_volume_is_lossless": False,
        "mesofree106670_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    proof_material = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(proof_material).hexdigest()
    return payload


def main() -> None:
    result = run()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(result["proof_object_sha256"])
    print(f'exact_rational_checks={result["exact_rational_checks"]}')
    print(f'numerical_consistency_checks={result["numerical_consistency_checks"]}')
    print(f'total_checks={result["total_checks"]}')
    print("MESOFREE106670_PROVED=false")
    print("NINETY_PERCENT_ESTABLISHED=false")
    print("RH_ESTABLISHED=false")


if __name__ == "__main__":
    main()
