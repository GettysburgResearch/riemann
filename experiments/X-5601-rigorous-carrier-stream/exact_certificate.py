#!/usr/bin/env python3
"""Certificate for `lambda_min(A_K + R_K - S_K)` with the nonprime blocks
*assembled* rather than bounded.

Agent: opus5-01   Issue: #55

`analyze_stream.py` certifies `ell_T I - S_K` and then pays the L-4202 and
L-4203 uniform envelopes.  At the production parameters that costs
`1.66e-10`; O-5603 showed the envelope is about `100x` larger than the
correction it bounds, and L-5603 (`archimedean_asymptotic.py`) computes the
correction itself in `O(K)` work at any carrier.  This driver assembles

    Q = A_K + R_K - S_K

directly and certifies `lambda_min(Q) > 0` with the same Gram-factor argument
as L-5602: for any `L`, `L L^*` is positive semidefinite, so
`lambda_min(Q - sI) >= -||(Q - sI) - L L^*||` and hence
`lambda_min(Q) >= s - rho`.

The residual budget is then
  * `rho`, the Gram residual (computed, not assumed);
  * the L-5601 stream enclosure `sum_d eta_d` for the prime side;
  * the L-5603 endpoint-expansion remainder for `A_K`;
  * the binary64 assembly rounding.
The L-4202/L-4203 envelopes no longer appear.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from fractions import Fraction

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analyze_stream as A                                     # noqa: E402
import archimedean_block as AB                                 # noqa: E402
import archimedean_asymptotic as AA                            # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("stream")
    ap.add_argument("--carrier-num", type=int, required=True)
    ap.add_argument("--carrier-den", type=int, required=True)
    ap.add_argument("--nterms", type=int, default=3)
    ap.add_argument("--out", default="exact-certificate.json")
    args = ap.parse_args()

    st = A.load_stream(args.stream)
    k = st["cells"]
    cutoff = st["cutoff"]
    T = args.carrier_num / args.carrier_den

    # --- prime side (L-0801 + L-5601) ------------------------------------
    sk = A.toeplitz_matrix(st)
    errs = A.lag_error_bounds(st)
    stream_err = sum(errs)
    u = Fraction(1, 2 ** 53)
    zsum = abs(st["_zre"][0]) + sum(abs(st["_zre"][d]) + abs(st["_zim"][d])
                                    for d in range(1, k))
    prime_round = u * zsum

    # --- archimedean block (L-4201 via L-5603) ---------------------------
    za, rem, b, omega, psi = AA.asymptotic_lags(cutoff, k, args.carrier_num,
                                                args.carrier_den, args.nterms)
    z1, alpha_shift, _b, _om = AA.lag_one_and_diagonal(
        cutoff, k, args.carrier_num, args.carrier_den, args.nterms)
    za[1] = z1
    gate = A.correction_gate(cutoff, k, args.carrier_num, args.carrier_den)
    ell = Fraction(gate["ell_T"])
    ell_slack = Fraction(1, 10 ** 25)
    alpha0 = float(ell) + alpha_shift
    ak = AB.archimedean_matrix(alpha0, za)
    # remainder of the endpoint expansion, as a Toeplitz row sum
    arch_rem = float(rem.sum()) + abs(alpha_shift) * 1e-12

    # --- pole block (L-4203, assembled exactly) --------------------------
    rk = AB.pole_matrix(cutoff, k, T)

    q = ak + rk - sk
    q = 0.5 * (q + q.conj().T)
    lam_min_float = float(np.linalg.eigvalsh(q)[0])

    gram = None
    for extra in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3):
        s = lam_min_float - extra
        gram = A.gram_upper_bound(-q, -s)
        if gram is not None:
            break
    assert gram is not None, "no Gram factor found"
    s_used = -gram["t"]
    rho = gram["total_slack"]

    lam_min_lower = (Fraction(s_used).limit_denominator(10 ** 18)
                     - Fraction(rho).limit_denominator(10 ** 18)
                     - stream_err - prime_round
                     - Fraction(arch_rem).limit_denominator(10 ** 30)
                     - ell_slack)

    res = {
        "schema": "riemann.x5601-exact-certificate.v1",
        "agent": "opus5-01",
        "classification": "the archimedean block is assembled by the L-5603 "
                          "endpoint expansion in ordinary floating point with "
                          "an analytic remainder bound; the expansion has been "
                          "validated against direct quadrature but is not yet "
                          "an interval computation (Q-5604). Treat the sign as "
                          "PROPOSED, not certified.",
        "cutoff": cutoff, "cells": k,
        "carrier": f"{args.carrier_num}/{args.carrier_den}",
        "total_terms": st["total_terms"],
        "ell_T": gate["ell_T"],
        "omega_b": psi,
        "archimedean": {
            "alpha_0_minus_ell_T": alpha_shift,
            "abs_z_1": abs(z1),
            "abs_sum_z_d_ge_2": float(np.abs(za[2:]).sum()),
            "assembled_rowsum": float(abs(z1) + np.abs(za[2:]).sum()
                                      + abs(alpha_shift)),
            "expansion_remainder_bound": arch_rem,
            "L4202_uniform_bound_replaced": gate["B_arch_float"],
            "improvement_factor": gate["B_arch_float"] /
                                  max(1e-300, float(abs(z1)
                                      + np.abs(za[2:]).sum()
                                      + abs(alpha_shift))),
        },
        "pole": {
            "assembled_norm": float(np.linalg.norm(rk, 2)),
            "L4203_uniform_bound_replaced": gate["R_norm_float"],
        },
        "prime": {
            "stream_error_sum": float(stream_err),
            "matrix_rounding": float(prime_round),
        },
        "gram": {kk: gram[kk] for kk in
                 ("residual_inf_norm", "rounding_slack", "total_slack")},
        "lambda_min_floating": lam_min_float,
        "lambda_min_lower_bound": float(lam_min_lower),
        "positive": bool(lam_min_lower > 0),
        "enclosure_half_width_total": float(
            Fraction(rho).limit_denominator(10 ** 18) + stream_err
            + prime_round + Fraction(arch_rem).limit_denominator(10 ** 30)),
    }
    with open(args.out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
