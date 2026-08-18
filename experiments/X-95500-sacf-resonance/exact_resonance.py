#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction


def q2_json(a: Fraction, b: Fraction) -> dict[str, str]:
    return {"rational": str(a), "sqrt2": str(b)}


certificate = {
    "schema": "riemann.q4.95500.critical-resonance.v1",
    "base_pr": 580,
    "base_sha": "812e7fcbaff2dd1c2c53c885def7b6c0d0e68a05",
    "critical_gcd_local_states": {
        "absent": "1",
        "a": "-u",
        "b": "-v",
        "common_divisor": "+uv",
        "sum": "1-u-v+uv=(1-u)(1-v)",
    },
    "critical_exponents": {
        "a": "s1",
        "b": "s2",
        "common_divisor": "s1+s2",
    },
    "dual_frequency": "M_odd(sigma+it) M_odd(sigma-it)=|M_odd(sigma+it)|^2",
    "j0_mellin_at_zero": q2_json(Fraction(7, 128), Fraction(7, 256)),
    "j0_zero_free_strip": "0<Re(z)<1/2",
    "unconditional_classical_gain": "SACF << X log^2 X exp(-c sqrt(log X)) + polylog",
    "power_dictionary": {
        "SACF_O_X_2theta": "zeta zeros satisfy Re(rho)<=1/2+theta",
        "SACF_O_X_1_minus_delta": "zeta zeros satisfy Re(rho)<=1-delta/2",
        "SACF_polylog": "RH",
    },
    "carry_imported": False,
    "scientific_status": "SACF, FOCC, OCHD and RH remain unproved",
}

print(json.dumps(certificate, indent=2, sort_keys=True))
