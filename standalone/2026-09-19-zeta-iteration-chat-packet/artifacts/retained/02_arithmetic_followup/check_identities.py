#!/usr/bin/env python3
"""Small independent numerical consistency checks, not proofs of the theorems."""
import json, math
from pathlib import Path
import numpy as np
from rh_gram_followup import gram, w_table

rng = np.random.default_rng(20260917)
checks = []
for N in range(2, 11):
    period = math.lcm(*range(2, N + 1))
    n = np.arange(2, N + 1)
    k = np.arange(1, period + 1)
    B = (k[:, None] % n[None, :]) / n[None, :]
    mean = B.mean(axis=0)
    covariance = (B - mean).T @ (B - mean) / period
    prediction = np.array([[(math.gcd(int(m), int(q))**2 - 1) / (12*m*q) for q in n] for m in n])
    error = float(np.max(np.abs(covariance - prediction)))
    assert error < 1e-13
    G = gram(N, w_table(N))
    eig = float(np.linalg.eigvalsh(G)[0])
    harmonic = float(np.sum(1 / np.arange(1, N + 1)))
    assert eig >= max(1/(6*N**3), 1/(6*N**2*harmonic**2)) * (1-1e-12)
    c = rng.standard_normal(N-1)
    norm_squared = float(c @ G @ c)
    assert np.abs(c).sum()**2 <= 6*N**3*norm_squared
    assert np.sum(c**2/n**2) <= 6*harmonic**2*norm_squared
    periodic_energy = float(np.mean((B @ c)**2))
    assert periodic_energy <= N*N*(1+harmonic**3/2)*norm_squared
    checks.append(dict(N=N, period=period, covariance_max_error=error, smallest_eigenvalue=eig))
print(json.dumps(checks, indent=2))
