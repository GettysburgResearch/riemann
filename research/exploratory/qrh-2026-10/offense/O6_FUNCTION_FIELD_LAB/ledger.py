"""ledger.py -- EXACT replay of Oct 5 Step 3 (Poisson in u, Gauss-sum dual, Moebius absorption,
Ramanujan-sum blocks, positivity, mean-square relaxation) in the function-field lab F_q[T].

Rows: all u in V_M = {deg u < M} (u != 0).  Columns: monic squarefree n, deg n = d, coefficient mu(n).
Pairs (n1, n2) = (g a, g b), (a, b) = 1, deg a = deg b = delta.  Exact dual (derived in README §3):
   M2 = sum_g q^{M-d} sum_{h in V_{d+delta-M}} c_g(h) I(g,h),
   I(g,h) = sum_{(a,b)=1} beta_h(a) chi_a(g) conj(beta_h(b) chi_b(g)),  beta_h(a) = chi0(Res(a,a')) conj(chi_a(h)),
where the Gauss sums have been absorbed with mu(a) g_a(chi_a) = (-g_1)^delta chi0(Res(a,a')) (gauss_exact.py),
and c_g(h) = sum_{e | (g,h)} mu(g/e) |e| (Ramanujan sum; f = g/e is the Oct 5 Moebius variable).
Ledger (all exact integers in Z[omega], printed as rational multiples of the primal diagonal):
   truth   Off   = M2 - Diag                                  (primal, direct; and dual, must agree)
   T1      = sum_{e,f} |Block(e,f)|,  Block(e,f) = q^{M-d}|e| sum_{e|h} I(ef,h)      (positivity in f)
   T2      = sum_{e,f} q^{M-d}|e| sum_{e|h} |sum_a beta_h(a) chi_a(g)|^2            (drop (a,b)=1: mean square)
   T2diag  = the a = b part of T2 (the "dual diagonal")
Usage: python3 ledger.py q d [M1,M2,...]   (default all M = 1..2d)
"""
import sys
import json
import numpy as np
from ffcommon import monics, resultant, deriv, dlog_table, primes_upto, mobius, deg, allpolys_below, pmod

W1 = np.array([1, 1, 0, -1, -1, 0], dtype=np.int64)   # zeta6^e = W1[e] + W2[e] * omega
W2 = np.array([0, 1, 1, 0, -1, -1], dtype=np.int64)


def zw_from_exp(E):
    """E: int array of exponents mod 6, -1 meaning 0 -> (re, om) int arrays."""
    m = E >= 0
    re = np.where(m, W1[np.where(m, E, 0)], 0)
    om = np.where(m, W2[np.where(m, E, 0)], 0)
    return re, om


def norm2(re, om):
    return re * re - re * om + om * om


def main():
    q, d = int(sys.argv[1]), int(sys.argv[2])
    g0, dl = dlog_table(q)
    primes = primes_upto(2 * d + 2, q)
    sq = {k: [n for n in monics(k, q) if mobius(n, q, primes) != 0] for k in range(0, d + 1)}
    sq[0] = [(1,)]

    def chi_e(n, x):
        if deg(n) == 0:
            return 0
        r = resultant(n, x, q)
        return dl[r] % 6 if r else -1

    def Dexp(a):
        if deg(a) == 0:
            return 0
        return dl[resultant(a, deriv(a, q), q)] % 6

    def coprime(a, b):
        if deg(a) == 0 or deg(b) == 0:
            return True
        return resultant(a, b, q) != 0

    def divides(e, h):
        if deg(e) == 0:
            return True
        if not h:
            return True
        return not pmod(h, e, q)

    def ramanujan_divisors(g):
        """list of (e, f=g/e, mu(f), |e|) over monic divisors e of squarefree g."""
        fac = [P for P in primes if deg(P) <= deg(g) and not pmod(g, P, q)] if deg(g) > 0 else []
        out = []
        for mask in range(1 << len(fac)):
            e = (1,)
            nf = 0
            from ffcommon import pmul
            for i, P in enumerate(fac):
                if mask >> i & 1:
                    e = pmul(e, P, q)
                else:
                    nf += 1
            out.append((e, (-1) ** nf, q ** deg(e)))
        return out

    # primal truth for rows V_M
    res = {}
    cols = sq[d]
    Ms = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 else list(range(1, 2 * d + 1))
    for M in Ms:
        rows = [u for u in allpolys_below(M, q) if u]
        Emat = np.array([[chi_e(n, u) for u in rows] for n in cols], dtype=np.int64)
        mu = np.array([mobius(n, q, primes) for n in cols], dtype=np.int64)
        re, om = zw_from_exp(Emat)
        A_re = mu @ re
        A_om = mu @ om
        M2 = int(norm2(A_re, A_om).sum())
        Diag = int((Emat >= 0).sum())
        # dual ledger
        tot_re = 0
        tot_om = 0
        T1 = 0
        T2 = 0
        T2diag = 0
        diag_dual = 0
        for delta in range(0, d + 1):
            K = d + delta - M
            hs = [h for h in allpolys_below(K, q)] if K > 0 else [()]
            for g in sq[d - delta]:
                As = [a for a in sq[delta] if coprime(a, g)]
                if not As:
                    continue
                # beta_h(a) chi_a(g) as exponent matrix [a, h]
                Bm = np.full((len(As), len(hs)), -1, dtype=np.int64)
                for i, a in enumerate(As):
                    De = Dexp(a)
                    cg = chi_e(a, g) if deg(a) > 0 else 0
                    for j, h in enumerate(hs):
                        if deg(a) == 0:
                            Bm[i, j] = 0
                            continue
                        ch = chi_e(a, h) if h else -1
                        if ch < 0 or cg < 0:
                            continue
                        Bm[i, j] = (De - ch + cg) % 6
                bre, bom = zw_from_exp(Bm)
                cbre, cbom = bre - bom, -bom          # conj(x + y w) = (x - y) - y w
                if delta > 0:
                    C = np.array([[1 if coprime(a, b) else 0 for b in As] for a in As], dtype=np.int64)
                else:
                    C = np.ones((1, 1), dtype=np.int64)
                # I(g,h) = sum_{a,b} B[a,h] C[a,b] conjB[b,h]
                Cc_re = C @ cbre
                Cc_om = C @ cbom
                I_re = (bre * Cc_re - bom * Cc_om).sum(axis=0)
                I_om = (bre * Cc_om + bom * Cc_re - bom * Cc_om).sum(axis=0)
                full = norm2(bre.sum(axis=0), bom.sum(axis=0))   # |sum_a beta|^2 per h
                dgl = (Bm >= 0).sum(axis=0)
                for (e, muf, abs_e) in ramanujan_divisors(g):
                    sel = np.array([divides(e, h) for h in hs])
                    b_re = q ** 0 * abs_e * int(I_re[sel].sum())
                    b_om = abs_e * int(I_om[sel].sum())
                    tot_re += muf * b_re
                    tot_om += muf * b_om
                    if delta > 0:
                        T1 += float(np.sqrt(float(b_re * b_re - b_re * b_om + b_om * b_om)))
                        T2 += abs_e * int(full[sel].sum())
                        T2diag += abs_e * int(dgl[sel].sum())
                    else:
                        diag_dual += muf * b_re
        scale = float(q) ** (M - d)
        dual_total = scale * tot_re
        res[M] = dict(M=M, rows=len(rows), M2=M2, Diag=Diag, Off=M2 - Diag,
                      dual_total=dual_total, dual_total_om=scale * tot_om, dual_diag=scale * diag_dual,
                      T1=scale * T1, T2=scale * T2, T2diag=scale * T2diag)
        r = res[M]
        print(f"q={q} d={d} M={M} rows={len(rows)}: M2={M2} Diag={Diag} Off/Diag={(M2-Diag)/Diag:+.4f} | "
              f"dual total={dual_total:.1f} (omega part {scale*tot_om:.1f}) dual zero-freq={scale*diag_dual:.1f} | "
              f"T1/Diag={r['T1']/Diag:.3f} T2/Diag={r['T2']/Diag:.3f} T2diag/Diag={r['T2diag']/Diag:.3f}", flush=True)
    json.dump(res, open(f'results/ledger_q{q}_d{d}_M{"-".join(map(str, Ms))}.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
