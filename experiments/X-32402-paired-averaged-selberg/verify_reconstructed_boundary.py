#!/usr/bin/env python3
"""Exact directed replay for L-32408.

This intentionally reuses the arithmetic and interval machinery of verify.py.
Importing it runs the base paired-Selberg replay first; the checks below only
strengthen the finite gate from positivity to coefficient-one absorption of the
fully reconstructed Möbius boundary.
"""
from __future__ import annotations

import hashlib
import json
import runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
ns = runpy.run_path(str(HERE / "verify.py"))

NFIN = ns["NFIN"]
SCALE = ns["SCALE"]
scalar_mean_defect_lower = ns["scalar_mean_defect_lower"]
actual_average_defect_lower = ns["actual_average_defect_lower"]

# For the fully Bézout-reconstructed source, 1*mu=epsilon.  Hence every
# nontrivial split has carry charge -1 and the normalized row energy is
# (n-1)/(n+1).  We compare without division:
#
#   R_pair(n) > (n-1)/(n+1)
# iff
#   (n+1) * R_pair(n) > n-1.

minimum_margin = None
for n in range(6, NFIN):
    reserve_lo = scalar_mean_defect_lower(n)
    margin_scaled = (n + 1) * reserve_lo - (n - 1) * SCALE
    assert margin_scaled > 0, (n, reserve_lo, margin_scaled)
    if minimum_margin is None or margin_scaled < minimum_margin[0]:
        minimum_margin = (margin_scaled, n, reserve_lo)

small = {}
for n in (2, 4, 5):
    reserve_lo = actual_average_defect_lower(n)
    margin_scaled = (n + 1) * reserve_lo - (n - 1) * SCALE
    assert margin_scaled > 0, (n, reserve_lo, margin_scaled)
    small[n] = {
        "reserve_lower_scaled": str(reserve_lo),
        "margin_scaled": str(margin_scaled),
        "reserve_decimal_lower": f"{reserve_lo / SCALE:.15f}",
        "boundary_energy": f"{(n - 1) / (n + 1):.15f}",
    }

# n=3 is the declared fixed bottom exception: the paired reserve is exactly
# zero while the reconstructed Mobius boundary energy is 1/2.
assert ns["actual_average_defect_lower"](3) == 0

result = {
    "schema": "riemann.x32402.reconstructed-mobius-boundary.v1",
    "verified": True,
    "verdict": "PASS_EXACT_COEFFICIENT_ONE_RECONSTRUCTED_BOUNDARY_ABSORPTION",
    "checks": {
        "finite_rows": {
            "start": 6,
            "stop": NFIN - 1,
            "count": NFIN - 6,
        },
        "minimum_directed_margin": {
            "n": minimum_margin[1],
            "scaled_integer": str(minimum_margin[0]),
            "reserve_lower_scaled": str(minimum_margin[2]),
            "reserve_decimal_lower": f"{minimum_margin[2] / SCALE:.15f}",
            "boundary_energy": f"{(minimum_margin[1] - 1) / (minimum_margin[1] + 1):.15f}",
        },
        "small_direct_rows": small,
        "n3_fixed_bottom_exception": {
            "reserve": "0",
            "boundary_energy": "1/2",
        },
        "tail_start": NFIN,
        "tail_argument": (
            "L-32407 gives R_pair(n)>=n^2 log^2(2)/30-36n-42n log n; "
            "the written proof checks this exceeds 174 at n=30000 and is "
            "increasing, while (n-1)/(n+1)<1."
        ),
    },
    "proof_boundary": (
        "Exact directed finite replay through n=29999 plus the written "
        "elementary cofinal tail.  This certifies the carry-row boundary "
        "absorption only; it does not certify the source-convolved physical "
        "localization or RH."
    ),
}
canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
print(json.dumps(result, indent=2, sort_keys=True))
