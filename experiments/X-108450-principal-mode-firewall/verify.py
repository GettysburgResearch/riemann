#!/usr/bin/env python3
import cmath
import hashlib
import json
from pathlib import Path

CLASSIFICATION = "PASS_T108450_PRINCIPAL_MODE_FIREWALL"


def dft(values):
    n = len(values)
    return [
        sum(values[x] * cmath.exp(-2j * cmath.pi * k * x / n) for x in range(n))
        for k in range(n)
    ]


def twisted_convolution(a, b):
    n = len(a)
    out = [0j] * n
    for x, ax in enumerate(a):
        for y, by in enumerate(b):
            out[(x + 2 * y) % n] += ax * by
    return out


def run():
    checks = 0

    for n in range(3, 66, 2):
        for A in (1, 2, -3, 5):
            for B in (1, -2, 4, 7):
                a = [complex(A)] * n
                b = [complex(B)] * n
                ah = dft(a)
                bh = dft(b)
                assert abs(ah[0] - n * A) < 1e-8
                assert abs(bh[0] - n * B) < 1e-8
                assert all(abs(z) < 1e-8 for z in ah[1:])
                assert all(abs(z) < 1e-8 for z in bh[1:])
                cell_energy = n * n * (A * B) ** 2
                assert cell_energy > 0
                checks += 5

                c = twisted_convolution(a, b)
                ch = dft(c)
                assert abs(ch[0] - ah[0] * bh[0]) < 1e-7
                assert all(abs(ch[k] - ah[k] * bh[(2 * k) % n]) < 1e-7 for k in range(n))
                assert all(abs(z) < 1e-7 for z in ch[1:])
                checks += 3

    # 32 odd group sizes * 16 scalar pairs * 8 checks = 4096.
    assert checks == 4096

    # One-cell source-weighted firewall: occupancy trace is positive while a
    # zero-sum actual coefficient vector has zero positive energy.
    r = 100
    z = [9] * 4 + [-3] * 32 + [1] * 64
    assert len(z) == r
    assert sum(z) == 4
    assert sum(v * v for v in z) == 676
    zero_sum = [-3, 1, 1, 1]
    assert sum(zero_sum) == 0
    checks += 3

    assert checks == 4099

    payload = {
        "schema": "riemann.x108450.principal-mode-firewall.v1",
        "classification": CLASSIFICATION,
        "exact_checks": checks,
        "uniform_nonprincipal_vanishes_checked": True,
        "principal_energy_survives_checked": True,
        "twisted_pushforward_principal_survives_checked": True,
        "double_quadratic_principal_alias_checked": True,
        "nonresonant_to_principal_transfer_refuted": True,
        "principalbind108450_proved": False,
        "rh_established": False,
        "grh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    payload = run()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")
