#!/usr/bin/env python3
"""High-precision analytic U experiment; ordinary arithmetic, NOT certified.

All double integrals in U are evaluated with the full-source Laplace identity.
The gamma tail uses digamma partial fractions plus exponentially small terms.
Finite omission, transcendental evaluation and R quadrature are not enclosed.
"""

import argparse
import json
from pathlib import Path
import time

import mpmath as mp


def entire_f(z):
    return mp.expm1(z) / z if z else mp.mpf(1)


def entire_fp(z):
    return (mp.exp(z) * (z - 1) + 1) / z**2 if z else mp.mpf(".5")


class Source:
    def __init__(self, dps=60, gamma_exp_terms=50):
        mp.mp.dps = dps
        self.b = mp.mpf("1.5")
        self.cb = (1 - mp.euler - mp.log(2 * mp.pi)) / 3
        self.p2 = -mp.diff(mp.zeta, 2) / mp.zeta(2)
        self.q2 = mp.log(2) / mp.sqrt(2)
        self.d = mp.log(2)
        self.terms = gamma_exp_terms
        self.gb = mp.digamma(mp.mpf(".5"))
        self.gmb = mp.digamma(2)
        self.lp = (self.gb - self.gmb) / (2 * self.b)
        self.cache = {}

    def a(self, z):
        b = self.b
        if z == b:
            gp = -mp.polygamma(1, mp.mpf(".5")) / 2
            gpp = mp.polygamma(2, mp.mpf(".5")) / 4
            return -(gp - self.lp) / (4 * b), -gpp / (8 * b) + (gp - self.lp) / (8 * b**2)
        if z == -b:
            gp = -mp.polygamma(1, 2) / 2
            gpp = mp.polygamma(2, 2) / 4
            return (gp - self.lp) / (4 * b), gpp / (8 * b) + (gp - self.lp) / (8 * b**2)
        g = mp.digamma(mp.mpf("1.25") - z / 2)
        gp = -mp.polygamma(1, mp.mpf("1.25") - z / 2) / 2
        linear = ((z + b) * self.gb + (b - z) * self.gmb) / (2 * b)
        denominator = z * z - b * b
        av = -(g - linear) / (2 * denominator)
        ap = -(gp - self.lp) / (2 * denominator) + (g - linear) * z / denominator**2
        return av, ap

    def segment(self, z):
        d = self.d
        value = mp.exp(z * d) * (1 - d) * entire_f(z * (1 - d))
        deriv = mp.exp(z * d) * ((1 - d) * d * entire_f(z * (1 - d))
                                + (1 - d)**2 * entire_fp(z * (1 - d)))
        return value, deriv

    def laplace(self, z):
        if z in self.cache:
            return self.cache[z]
        b = self.b
        av, ap = self.a(z)
        exp_sum = mp.mpc(0)
        exp_sum_p = mp.mpc(0)
        for j in range(1, self.terms + 1):
            lam = 2 * j + mp.mpf(".5")
            base = mp.exp(-lam) / (lam * lam - b * b)
            exp_sum += base / (lam - z)
            exp_sum_p += base / (lam - z)**2
        gv = av - mp.exp(z) * exp_sum
        gp = ap - mp.exp(z) * (exp_sum + exp_sum_p)
        value = (entire_f(z + mp.mpf(".5")) / 2 + self.cb * entire_f(z - b) + gv
                 - self.p2 * (entire_f(z + b) + entire_f(z - b)) / (2 * b))
        deriv = (entire_fp(z + mp.mpf(".5")) / 2 + self.cb * entire_fp(z - b) + gp
                 - self.p2 * (entire_fp(z + b) + entire_fp(z - b)) / (2 * b))
        sp, spp = self.segment(z + b)
        sm, smp = self.segment(z - b)
        value += self.q2 * (mp.exp(-b * self.d) * sp - mp.exp(b * self.d) * sm) / (2 * b)
        deriv += self.q2 * (mp.exp(-b * self.d) * spp - mp.exp(b * self.d) * smp) / (2 * b)
        self.cache[z] = value, deriv
        return value, deriv

    def double(self, alpha, beta):
        s = alpha + beta
        ta, tpa = self.laplace(alpha)
        tb, tpb = self.laplace(beta)
        if s == 0:
            return ta + tb - tpa - tpb
        tma, _ = self.laplace(-alpha)
        tmb, _ = self.laplace(-beta)
        return (mp.exp(s) * (tma + tmb) - ta - tb) / s


def basis(count, removed=15):
    out = []
    labels = []
    for j in range(1, removed + 1):
        out.append([(mp.j * mp.pi * j, -mp.j / 2), (-mp.j * mp.pi * j, mp.j / 2)])
        labels.append(f"sin({j}*pi*t)")
    out.extend([[(mp.mpf(".5"), mp.mpf(1))], [(mp.mpf("-.5"), mp.mpf(1))],
                [(mp.mpf("1.5"), mp.mpf(".5")), (mp.mpf("-1.5"), mp.mpf(".5"))]])
    labels.extend(["exp(t/2)", "exp(-t/2)", "cosh(3*t/2)"])
    for j in range(removed + 1, removed + count + 1):
        out.append([(mp.j * mp.pi * j, -mp.j / 2), (-mp.j * mp.pi * j, mp.j / 2)])
        labels.append(f"sin({j}*pi*t)")
    return out, labels


def build(count, dps=60, removed=15):
    began = time.monotonic()
    source = Source(dps=dps)
    funcs, labels = basis(count, removed)
    n = len(funcs)
    q = mp.matrix(n)
    gram = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            qv = mp.mpc(0)
            gv = mp.mpc(0)
            for a, ca in funcs[i]:
                for b, cb in funcs[j]:
                    qv += ca * cb * source.double(a, b)
                    gv += ca * cb * entire_f(a + b)
            assert abs(qv.imag) < mp.mpf(10) ** (-dps + 10)
            assert abs(gv.imag) < mp.mpf(10) ** (-dps + 10)
            q[i, j] = q[j, i] = source.b * qv.real
            gram[i, j] = gram[j, i] = gv.real
    dim = removed + 3
    g_ee = gram[:dim, :dim]
    orth = mp.inverse(mp.cholesky(g_ee).T)
    q_ee = orth.T * q[:dim, :dim] * orth
    if count:
        constraint = orth.T * gram[:dim, dim:]
        q_eh = orth.T * q[:dim, dim:]
        q_vv = (q[dim:, dim:] - constraint.T * q_eh - q_eh.T * constraint
                + constraint.T * q_ee * constraint)
        q_ve = q_eh.T - constraint.T * q_ee
        corrections = mp.inverse(q_vv) * q_ve
        u = q_ee - q_ve.T * corrections
        zcoeffs = mp.matrix(n, dim)
        top = orth * (mp.eye(dim) + constraint * corrections)
        for i in range(dim):
            for j in range(dim):
                zcoeffs[i, j] = top[i, j]
        for i in range(count):
            for j in range(dim):
                zcoeffs[i + dim, j] = -corrections[i, j]
    else:
        u = q_ee
        zcoeffs = orth
    return {
        "status": "EMPIRICAL_ANALYTIC_NOT_CERTIFIED",
        "dps": dps,
        "gamma_exponential_terms": source.terms,
        "trial_mode_count": count,
        "complement_dimension": dim,
        "basis_labels": labels,
        "u_matrix_decimal": [[mp.nstr(u[i, j], dps - 10) for j in range(dim)] for i in range(dim)],
        "z_coefficients_decimal": [[mp.nstr(zcoeffs[i, j], dps - 10) for j in range(dim)] for i in range(n)],
        "elapsed_seconds": time.monotonic() - began,
        "limitations": ["ordinary high precision", "digamma and zeta derivative not enclosed",
                        "omitted gamma exponential tail not enclosed", "R not computed here"],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--trial-modes", type=int, default=40)
    parser.add_argument("--dps", type=int, default=60)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.trial_modes, dps=args.dps)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    import numpy as np
    u = np.array(result["u_matrix_decimal"], dtype=float)
    print(json.dumps({"status": result["status"], "elapsed_seconds": result["elapsed_seconds"],
                      "u_eigenvalues": np.linalg.eigvalsh(u).tolist()}, indent=2))
