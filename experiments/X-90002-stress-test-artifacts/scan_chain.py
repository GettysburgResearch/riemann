#!/usr/bin/env python3
"""Full residual chain: V_g = debt norm of T^{g-1} b_X for g=1.. until support < 2.
Also longdouble cross-check to bound accumulated floating noise."""
import time, json, sys
import numpy as np
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad')
import cbvr
from cbvr import first_boundary, apply_T, debt_norms


def first_boundary_ld(X):
    """longdouble version of first_boundary (same algorithm)."""
    ld = np.longdouble
    M = (X + 1) // 2
    b = np.zeros(M + 2, dtype=ld)
    q_all = np.arange(2, M + 1)
    logX = np.log(ld(X))
    Q0 = min(M, 1024)
    for q in range(2, Q0 + 1):
        Kexp = max((X + 1) // (2 * q) + 2, 32)
        k = np.arange(1, Kexp + 1, dtype=ld)
        c = ld(2 * q - 1)
        aa = 2 * k * q - 1
        dd = (2 * k + 1) * q
        lc = np.log(c)
        b[q] = np.sum((np.log(np.minimum(aa, X)) - lc) / np.sqrt(aa)
                      - (np.log(np.minimum(dd, X)) - lc) / np.sqrt(dd))
    if M > Q0:
        qv = np.arange(Q0 + 1, M + 1, dtype=ld)
        lcv = np.log(2 * qv - 1)
        acc = np.zeros(len(qv), dtype=ld)
        KmaxB = max((X + 1) // (2 * (Q0 + 1)) + 2, 32)
        for k in range(1, KmaxB + 1):
            if k <= 32:
                sl = slice(0, len(qv))
            else:
                qhi = (X + 1) // (2 * (k - 2))
                if qhi <= Q0:
                    break
                sl = slice(0, min(len(qv), qhi - Q0))
            qs = qv[sl]
            aa = 2 * k * qs - 1
            dd = (2 * k + 1) * qs
            acc[sl] += (np.log(np.minimum(aa, X)) - lcv[sl]) / np.sqrt(aa) \
                     - (np.log(np.minimum(dd, X)) - lcv[sl]) / np.sqrt(dd)
        b[Q0 + 1: M + 1] = acc
    qf = q_all.astype(ld)
    Kexp_v = np.maximum((X + 1) // (2 * q_all) + 2, 32).astype(ld)
    K = Kexp_v + 1
    eps = 1 / (2 * qf)
    L = logX - np.log(2 * qf - 1)
    # EM tail (same as cbvr._em_tail but dtype-agnostic)
    a = K - eps; bb = K + ld(0.5)
    ra = 1 / np.sqrt(a); rb = 1 / np.sqrt(bb)
    tail_v = (2 * (np.sqrt(bb) - np.sqrt(a)) + 0.5 * (ra - rb)
              + (ra / a - rb / bb) / 12
              - (ld(15) / 8) * (ra / a**3 - rb / bb**3) / 720 * (-1)
              - (ld(945) / 32) * (ra / a**5 - rb / bb**5) / 30240 * (-1))
    # careful with signs: EM = int + f/2 - f'/12 + f'''/720 - f5/30240
    f1 = -0.5 * (ra / a - rb / bb)
    f3 = -(ld(15) / 8) * (ra / a**3 - rb / bb**3)
    f5 = -(ld(945) / 32) * (ra / a**5 - rb / bb**5)
    tail_v = 2 * (np.sqrt(bb) - np.sqrt(a)) + 0.5 * (ra - rb) - f1 / 12 + f3 / 720 - f5 / 30240
    b[2: M + 1] += L / np.sqrt(2 * qf) * tail_v
    return b, M


def chain(X, b1, M1, maxgen=64):
    out = []
    b, M = b1, M1
    g = 1
    while M >= 2 and g <= maxgen:
        V, N = debt_norms(b, M)
        sup = float(np.max(np.abs(b[2:M+1]))) if M >= 2 else 0.0
        out.append(dict(g=g, M=int(M), V=float(V), N=float(N), sup=sup))
        b, M = apply_T(b, M)
        g += 1
    return out


results = {}
for X in [1000, 4000, 16000, 64000, 250000, 1000000]:
    t0 = time.time()
    b1, M1 = first_boundary(X)
    ch = chain(X, b1, M1)
    results[X] = ch
    print(f"\n### X = {X} (logX={np.log(X):.2f})  [{time.time()-t0:.1f}s]")
    print(" g      M            V_g          N_g        sup|b_g|")
    for r in ch:
        print(f"{r['g']:2d} {r['M']:8d} {r['V']:14.6f} {r['N']:14.6f}  {r['sup']:.3e}")
    tot = sum(r['V'] for r in ch)
    print(f"   total sum_g V_g = {tot:.4f};  (logX)^2={np.log(X)**2:.1f}")

# longdouble cross-check at X=64000
X = 64000
b1d, M1 = first_boundary(X)
b1l, _ = first_boundary_ld(X)
print("\n=== longdouble cross-check X=64000 ===")
print(f"max |b1_f64 - b1_ld| = {float(np.max(np.abs(b1d - b1l.astype(np.float64)))):.3e}")
b, M = b1l, M1
bd, Md = b1d, M1
g = 1
while M >= 2 and g <= 40:
    Vl, _ = debt_norms(b.astype(np.longdouble), M)
    Vd, _ = debt_norms(bd, Md)
    print(f" g={g:2d}  V_f64={float(Vd):.10f}  V_ld={float(Vl):.10f}  rel diff={abs(float(Vd)-float(Vl))/max(abs(float(Vl)),1e-30):.2e}")
    # apply T in respective precisions
    bd, Md = apply_T(bd, Md)
    # longdouble T
    M2 = (M + 1) // 2
    out = np.zeros(M2 + 2, dtype=np.longdouble)
    for q in range(2, M2 + 1):
        kmax = (M + 1) // (2 * q) + 1
        k = np.arange(1, kmax + 1)
        aidx = 2 * k * q - 1
        didx = (2 * k + 1) * q
        av = np.where((aidx >= 2) & (aidx <= M), b[np.clip(aidx, 0, M)], 0)
        dv = np.where((didx >= 2) & (didx <= M), b[np.clip(didx, 0, M)], 0)
        out[q] = av.sum() - dv.sum()
    b, M = out, M2
    g += 1

with open('/tmp/claude-0/-home-user-riemann/d379fac9-baa2-5637-b561-9823a1c28acc/scratchpad/chain_results.json', 'w') as f:
    json.dump(results, f, indent=1)
