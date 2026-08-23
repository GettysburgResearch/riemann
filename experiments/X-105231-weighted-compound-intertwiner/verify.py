#!/usr/bin/env python3
"""Exact fixtures for T-105231.

Standard-library Fraction arithmetic only. This authenticates the finite
weighted-variance/intertwiner algebra and the diagonal firewall; it does not
evaluate Xi or prove WSEG105231.
"""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def sub(x, y):
    return tuple(a-b for a, b in zip(x, y))


def norm2(x):
    return dot(x, x)


def weighted_scalar_defect(weights, rho):
    N = sum(weights, F(0))
    A = -sum((w*r for w, r in zip(weights, rho)), F(0))
    B = sum((w*r*r for w, r in zip(weights, rho)), F(0))
    return N, A, B, N*B-A*A


def scalar_pair_energy(weights, rho):
    out = F(0)
    for i in range(len(rho)):
        for j in range(i+1, len(rho)):
            out += weights[i]*weights[j]*(rho[i]-rho[j])**2
    return out


def vector_pair_energy(weights, vectors):
    out = F(0)
    for i in range(len(vectors)):
        for j in range(i+1, len(vectors)):
            out += weights[i]*weights[j]*norm2(sub(vectors[i], vectors[j]))
    return out


def gram(vectors):
    return [[dot(x, y) for y in vectors] for x in vectors]


def centered_trace_energy(weights, K):
    N = sum(weights, F(0))
    diagonal = sum((weights[i]*K[i][i] for i in range(len(weights))), F(0))
    cross = F(0)
    for i in range(len(weights)):
        for j in range(len(weights)):
            cross += weights[i]*K[i][j]*weights[j]
    return N*diagonal-cross


def main():
    weights = [F(1, 2), F(2, 3), F(3, 4)]
    rho = [F(-2), F(-1, 2), F(1, 3)]
    x = (F(1), F(0))
    y = [
        (F(2), F(0)),
        (F(1, 2), F(1)),
        (F(-1, 3), F(-1)),
    ]
    assert all(-dot(x, yi) == ri for yi, ri in zip(y, rho))

    N, A, B, defect = weighted_scalar_defect(weights, rho)
    scalar_pairs = scalar_pair_energy(weights, rho)
    vector_pairs = vector_pair_energy(weights, y)
    assert defect == scalar_pairs
    assert defect <= norm2(x)*vector_pairs
    K = gram(y)
    assert vector_pairs == centered_trace_energy(weights, K)

    w2 = [F(1), F(1), F(1)]
    rho2 = [F(-1), F(1), F(0)]
    y2 = [(F(1), F(0)), (F(-1), F(0)), (F(0), F(0))]
    x2 = (F(1), F(0))
    N2, A2, B2, D2 = weighted_scalar_defect(w2, rho2)
    assert A2 == 0
    assert D2 == F(6)
    assert D2 == scalar_pair_energy(w2, rho2)
    assert D2 == norm2(x2)*vector_pair_energy(w2, y2)
    spectral_bound = F(3)*F(1)*F(2)
    assert D2 == spectral_bound

    orth = [(F(1), F(0), F(0)),
            (F(0), F(1), F(0)),
            (F(0), F(0), F(1))]
    aligned = [(F(1), F(0), F(0))]*3
    K_orth = gram(orth)
    K_aligned = gram(aligned)
    assert [K_orth[i][i] for i in range(3)] == [F(1)]*3
    assert [K_aligned[i][i] for i in range(3)] == [F(1)]*3
    assert sum(K_orth[i][i] for i in range(3)) == F(3)
    assert sum(K_aligned[i][i] for i in range(3)) == F(3)
    fire_orth = centered_trace_energy(w2, K_orth)
    fire_aligned = centered_trace_energy(w2, K_aligned)
    assert fire_orth == F(6)
    assert fire_aligned == F(0)

    w3 = [F(9, 25), F(16, 25)]
    rho3 = [F(1), F(-2)]
    N3, A3, B3, D3 = weighted_scalar_defect(w3, rho3)
    assert A3 > 0
    assert D3 / B3 >= F(9, 25)

    payload = {
        "schema": "riemann.x105231.weighted_compound.v1",
        "classification": "PASS_T105231_WEIGHTED_DEBRANGES_FOURIER_INTERTWINER",
        "arithmetic": "EXACT_RATIONAL",
        "verified": {
            "weighted_variance_identity": True,
            "explicit_fourier_projection": True,
            "pair_bundle_cauchy_bound": True,
            "centered_gram_trace_identity": True,
            "spectral_equality_fixture": True,
            "diagonal_trace_firewall": True,
            "nine_twenty_five_integrality_sanity": True,
        },
        "fixtures": {
            "nonuniform": {
                "N": str(N),
                "A": str(A),
                "B": str(B),
                "defect": str(defect),
                "fourier_pair_energy": str(vector_pairs),
            },
            "spectral_equality": {
                "defect": str(D2),
                "spectral_bound": str(spectral_bound),
            },
            "firewall": {
                "orthogonal_centered_energy": str(fire_orth),
                "aligned_centered_energy": str(fire_aligned),
            },
        },
        "entire_xi_moment_finiteness_proved": False,
        "wseg105231_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()

    output = Path(__file__).parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
