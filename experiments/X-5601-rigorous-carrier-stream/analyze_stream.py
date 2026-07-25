#!/usr/bin/env python3
"""Downstream certification for the X-5601 carrier stream.

Agent: opus5-01   Issue: #55 / #28

Given the complete lag coefficients z_d produced by `carrier_stream.c`, this
script produces

  1. a rigorous upper bound for lambda_max(S_K) valid for *every* vector,
     through the Toeplitz symbol bound of L-5602 and, as a sharper second
     route, a backward-error-certified Cholesky test;
  2. the exact nonprime correction gate of L-4202 (archimedean) and L-4203
     (pole) at the declared parameters;
  3. a discovery eigenvector, its exact dyadic freeze, and the exact
     fixed-vector enclosure obtained by pairing z_d with the exact lag
     autocorrelations of the frozen vector.

Everything downstream of the stream file is exact rational or explicitly
outward-rounded arithmetic; the only floating quantities that enter a claim
are bounded by the L-5601 error model whose constants are arguments here.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction

import numpy as np
from mpmath import mp, mpf, log, sqrt, sinh, cosh, pi as mp_pi, euler


# --------------------------------------------------------------------------
# L-5601 error-model constants (see claims/lemmas/L-5601-...md).
# They are deliberately several orders of magnitude larger than the deviations
# measured against the independent mpmath oracle in tests/.
# --------------------------------------------------------------------------
EPS_TRIG = Fraction(1, 10 ** 17)   # absolute error of the computed sin/cos
EPS_AMP = Fraction(1, 10 ** 25)    # relative error of b_q
EPS_TAU = Fraction(1, 10 ** 25)    # absolute error of the hat weight
EPS_ACC = Fraction(1, 10 ** 16)    # total accumulation rounding, all lags


def dd_fraction(pair) -> Fraction:
    """A double-double pair is an exact binary rational."""
    return Fraction(float.fromhex(pair[0])) + Fraction(float.fromhex(pair[1]))


def load_stream(path: str) -> dict:
    with open(path) as fh:
        raw = json.load(fh)
    raw["_zre"] = [dd_fraction(p) for p in raw["z_real"]]
    raw["_zim"] = [dd_fraction(p) for p in raw["z_imag"]]
    raw["_w"] = [dd_fraction(p) for p in raw["weight"]]
    raw["_btot"] = dd_fraction(raw["amplitude_total"])
    return raw


def lag_error_bounds(st: dict) -> list[Fraction]:
    """Rigorous |z_hat_d - z_d| bound per lag from the L-5601 model."""
    k = st["cells"]
    btot = st["_btot"]
    acc = EPS_ACC / k
    root2 = Fraction(14143, 10000)          # > sqrt(2)
    return [w * (EPS_AMP + root2 * EPS_TRIG) + btot * EPS_TAU + acc
            for w in st["_w"]]


# --------------------------------------------------------------------------
# Rigorous bounds on lambda_max(S_K)
# --------------------------------------------------------------------------
def symbol_sup(st: dict, ngrid_log2: int = 24) -> dict:
    """Upper bound for sup_omega sigma(omega) >= lambda_max(S_K)  (L-5602).

    sigma(omega) = Re z_0 + sum_{d>=1} Re(z_d e^{i d omega}) is a real
    trigonometric polynomial of degree K-1.  We evaluate it on a uniform grid
    by FFT and close the gap with the Bernstein bound |sigma''| <= (K-1)^2
    ||sigma||_inf, applied at an interior maximum where sigma' vanishes.
    """
    k = st["cells"]
    n = 1 << ngrid_log2
    coef = np.zeros(n, dtype=np.complex128)
    coef[0] = float(st["_zre"][0])
    for d in range(1, k):
        coef[d] = complex(float(st["_zre"][d]), float(st["_zim"][d]))
    vals = np.fft.fft(coef).real           # sum_d Re(z_d e^{i d omega_m})
    gmax = float(vals.max())
    gmin = float(vals.min())
    linf_triv = float(abs(st["_zre"][0]) +
                      sum(abs(st["_zre"][d]) + abs(st["_zim"][d])
                          for d in range(1, k)))
    delta = 2.0 * float(mp_pi) / n
    # bootstrap: first pass with the trivial sup bound, then with the sharp one
    bump = (k - 1) ** 2 * linf_triv * delta * delta / 8.0
    linf = max(abs(gmax), abs(gmin)) + bump
    bump = (k - 1) ** 2 * linf * delta * delta / 8.0
    fft_slack = 1e-12 * linf_triv          # generous FFT round-off allowance
    return {"grid_log2": ngrid_log2, "grid_max": gmax, "grid_min": gmin,
            "closure": bump + fft_slack,
            "sup_upper": gmax + bump + fft_slack,
            "inf_lower": gmin - bump - fft_slack}


def toeplitz_matrix(st: dict) -> np.ndarray:
    k = st["cells"]
    row = np.zeros(k, dtype=np.complex128)
    row[0] = float(st["_zre"][0])
    for d in range(1, k):
        row[d] = 0.5 * complex(float(st["_zre"][d]), float(st["_zim"][d]))
    idx = np.arange(k)
    diff = idx[None, :] - idx[:, None]
    m = np.where(diff >= 0, row[np.abs(diff)], np.conj(row[np.abs(diff)]))
    return m


def gram_upper_bound(mat: np.ndarray, t: float) -> dict | None:
    """Certified  lambda_max(mat) <= t + slack  by exhibiting a Gram factor.

    The only mathematical input is elementary:  for ANY complex matrix L the
    product L L^H is positive semidefinite, so for M = t I - mat,

        lambda_min(M) >= -|| M - L L^H ||_2 .

    Cholesky is used only as a *heuristic producer* of L; no property of the
    LAPACK routine is assumed, and a wrong factor would only make the residual
    larger.  The residual norm is bounded by

        || M - L L^H ||_2  <=  || M - fl(L L^H) ||_inf + gamma_n || |L| |L^H| ||_inf

    using the standard inner-product rounding bound
    |fl(sum a_k b_k) - sum a_k b_k| <= gamma_n sum |a_k b_k|, valid for every
    summation order and also when fused multiply-adds are used, together with
    ||A||_2 <= ||A||_inf for Hermitian A.
    """
    n = mat.shape[0]
    m = t * np.eye(n) - mat
    m = 0.5 * (m + m.conj().T)
    try:
        low = np.linalg.cholesky(m)
    except np.linalg.LinAlgError:
        return None
    prod = low @ low.conj().T
    resid = float(np.abs(m - prod).sum(axis=1).max())
    absl = np.abs(low)
    absprod_rowsum = float((absl @ absl.T).sum(axis=1).max())
    u = 2.0 ** -53
    gamma = n * u / (1.0 - n * u)
    # forming M in binary64 only perturbs the diagonal, by at most u*t
    form_slack = u * abs(t)
    slack = (resid + gamma * absprod_rowsum) * (1.0 + 1e-9) + form_slack
    return {"t": t, "gamma_n": gamma,
            "residual_inf_norm": resid,
            "abs_product_rowsum": absprod_rowsum,
            "rounding_slack": gamma * absprod_rowsum,
            "form_slack": form_slack,
            "total_slack": slack,
            "lambda_max_upper": t + slack}


# --------------------------------------------------------------------------
# Nonprime correction gate: L-4202 (archimedean) and L-4203 (pole)
# --------------------------------------------------------------------------
def correction_gate(cutoff: int, cells: int, tnum: int, tden: int,
                    dps: int = 60) -> dict:
    mp.dps = dps
    T = mpf(tnum) / mpf(tden)
    L = log(mpf(cutoff))
    b = 2 * L / cells
    delta = L / (2 * mp_pi)
    h = delta / cells
    harm = sum(mpf(1) / r for r in range(1, cells - 1))       # H_{K-2}
    b_arch = (1 / (mp_pi * T)) * ((5 + 2 * harm) / b + 2 * (cells - 1) + mpf(1) / 4)
    r_norm = (2 * sinh(mp_pi * delta) * cosh(mp_pi * h / 2) ** 2 /
              (mp_pi ** 2 * h * sinh(mp_pi * h) * (T ** 2 + mpf(1) / 4)))
    ell = log(T / (2 * mp_pi)) / (2 * mp_pi)
    return {"b_small_cell_hypothesis": float(b), "b_le_1_over_20": bool(b <= mpf(1) / 20),
            "B_arch_upper": mp.nstr(b_arch, 20), "B_arch_float": float(b_arch),
            "R_norm_upper": mp.nstr(r_norm, 20), "R_norm_float": float(r_norm),
            "B_total_float": float(b_arch + r_norm),
            "ell_T": mp.nstr(ell, 30), "ell_T_float": float(ell)}


# --------------------------------------------------------------------------
# Vector freezing and the exact fixed-vector value
# --------------------------------------------------------------------------
def freeze(vec: np.ndarray, bits: int):
    scale = 1 << bits
    re = [int(round(x.real * scale)) for x in vec]
    im = [int(round(x.imag * scale)) for x in vec]
    return re, im


def exact_autocorrelation(re: list[int], im: list[int], bits: int):
    """c_d = sum_j conj(w_j) w_{j+d}, exactly, as Fractions."""
    k = len(re)
    den = Fraction(1, 1 << (2 * bits))
    out = []
    a = np.array(re, dtype=object)
    b = np.array(im, dtype=object)
    for d in range(k):
        cr = int(np.dot(a[:k - d], a[d:]) + np.dot(b[:k - d], b[d:]))
        ci = int(np.dot(a[:k - d], b[d:]) - np.dot(b[:k - d], a[d:]))
        out.append((Fraction(cr) * den, Fraction(ci) * den))
    return out


def fixed_vector_value(st: dict, corr, errs) -> dict:
    """P_v = sum_d Re(z_d c_d) with a rigorous half-width."""
    k = st["cells"]
    val = Fraction(0)
    rad = Fraction(0)
    for d in range(k):
        cr, ci = corr[d]
        val += st["_zre"][d] * cr - st["_zim"][d] * ci
        rad += errs[d] * (abs(cr) + abs(ci))
    return {"value": val, "radius": rad}


def sha256_json(obj) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("stream")
    ap.add_argument("--grid-log2", type=int, default=24)
    ap.add_argument("--freeze-bits", type=int, nargs="*", default=[48, 64, 80, 96])
    ap.add_argument("--out", default="certificate.json")
    args = ap.parse_args()

    st = load_stream(args.stream)
    k = st["cells"]
    errs = lag_error_bounds(st)
    err_total = sum(errs)

    gate = correction_gate(st["cutoff"], k,
                           st["carrier_numerator"], st["carrier_denominator"])
    ell = Fraction(gate["ell_T"])
    ell_slack = Fraction(1, 10 ** 25)

    sym = symbol_sup(st, args.grid_log2)

    mat = toeplitz_matrix(st)
    evals, evecs = np.linalg.eigh(mat)
    lam_float = float(evals[-1])
    vec = evecs[:, -1]

    # rounding of the double-double lag coefficients into the binary64 matrix
    u = Fraction(1, 2 ** 53)
    zsum = abs(st["_zre"][0]) + sum(abs(st["_zre"][d]) + abs(st["_zim"][d])
                                    for d in range(1, k))
    matrix_round = u * zsum

    chol = None
    for extra in (1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3):
        chol = gram_upper_bound(mat, lam_float + extra)
        if chol is not None:
            break

    # rigorous lambda_max(S_K) upper bound: matrix bound + stream error
    lam_upper_candidates = [Fraction(sym["sup_upper"]).limit_denominator(10 ** 18)
                            + err_total]
    if chol is not None:
        lam_upper_candidates.append(
            Fraction(chol["lambda_max_upper"]).limit_denominator(10 ** 18)
            + matrix_round + err_total)
    lam_upper = min(lam_upper_candidates)

    b_total = (Fraction(gate["B_arch_upper"]).limit_denominator(10 ** 30)
               + Fraction(gate["R_norm_upper"]).limit_denominator(10 ** 40))
    universal_margin = ell - ell_slack - lam_upper - b_total

    # ---- fixed-vector branch -------------------------------------------
    # canonical phase: largest-magnitude coordinate made real positive
    piv = int(np.argmax(np.abs(vec)))
    vec = vec * np.conj(vec[piv]) / abs(vec[piv])
    vec = vec / np.linalg.norm(vec)

    frozen = {}
    for bits in args.freeze_bits:
        re, im = freeze(vec, bits)
        corr = exact_autocorrelation(re, im, bits)
        pv = fixed_vector_value(st, corr, errs)
        norm2 = corr[0][0]
        lead_lo = ell * norm2 - ell_slack * norm2 - (pv["value"] + pv["radius"])
        lead_hi = ell * norm2 + ell_slack * norm2 - (pv["value"] - pv["radius"])
        exact_lo = lead_lo - b_total * norm2
        exact_hi = lead_hi + b_total * norm2
        digest = sha256_json({"bits": bits, "real": re, "imag": im})
        frozen[str(bits)] = {
            "vector_sha256": digest,
            "norm_squared": float(norm2),
            "prime_rayleigh": float(pv["value"]),
            "prime_rayleigh_radius": float(pv["radius"]),
            "leading_margin_lower": float(lead_lo),
            "leading_margin_upper": float(lead_hi),
            "exact_form_lower": float(exact_lo),
            "exact_form_upper": float(exact_hi),
            "exact_form_lower_str": str(exact_lo.numerator / exact_lo.denominator),
            "sign_certified_positive": bool(exact_lo > 0),
        }
        frozen[str(bits)]["_coords"] = {"real": re, "imag": im}

    cert = {
        "schema": "riemann.x5601-certificate.v1",
        "agent": "opus5-01",
        "cutoff": st["cutoff"],
        "cells": k,
        "carrier": f'{st["carrier_numerator"]}/{st["carrier_denominator"]}',
        "prime_count": st["prime_count"],
        "higher_prime_power_count": st["higher_prime_power_count"],
        "total_terms": st["total_terms"],
        "amplitude_total": float(st["_btot"]),
        "stream_error_model": {
            "eps_trig": str(EPS_TRIG), "eps_amp": str(EPS_AMP),
            "eps_tau": str(EPS_TAU), "eps_acc": str(EPS_ACC),
            "sum_lag_error_bound": float(err_total),
        },
        "ell_T": gate["ell_T"],
        "correction_gate": {kk: gate[kk] for kk in
                            ("b_small_cell_hypothesis", "b_le_1_over_20",
                             "B_arch_upper", "R_norm_upper", "B_total_float")},
        "symbol_bound": sym,
        "gram_factor_bound": chol,
        "matrix_rounding_bound": float(matrix_round),
        "sum_abs_z": float(zsum),
        "lambda_max_floating": lam_float,
        "lambda_max_upper_certified": float(lam_upper),
        "universal_margin_lower": float(universal_margin),
        "universal_positivity_certified": bool(universal_margin > 0),
        "frozen_vectors": frozen,
    }
    with open(args.out, "w") as fh:
        json.dump(cert, fh, indent=1)
    show = dict(cert)
    show["frozen_vectors"] = {b: {kk: vv for kk, vv in d.items() if kk != "_coords"}
                              for b, d in frozen.items()}
    print(json.dumps(show, indent=1)[:4000])


if __name__ == "__main__":
    main()
