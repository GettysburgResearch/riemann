"""C5 experiment E3: inertia of the function-field Weil/Toeplitz form (THEOREM C5-T3 check).

THEOREM C5-T3 (report): let P satisfy (F1)-(F2) with distinct reciprocal roots alpha_1..alpha_{2g}
(P squarefree), beta_i = alpha_i/sqrt q, t_k = sum_i beta_i^k (k in Z; t_{-k} = t_k), and
T_N = (t_{|m-n|})_{0<=m,n<N}.  For every N >= 2g:
      n_-(T_N) = #{i : |beta_i| > 1},  n_0(T_N) = N - 2g,  n_+(T_N) = 2g - n_-(T_N).
In particular RH <=> T_{2g} >= 0.

This script enumerates all admissible P (conditions F1-F3 of ff_fake_census.py, certified for all
d) for several (q,g), and compares the inertia of T_{2g} and T_{2g+1} (Arb-certified eigenvalue
enclosures via acb_mat.eig(algorithm='rump'); numpy fallback flagged non-rigorous) with the exact
count n_out = #{|beta|>1} obtained from Sturm sequences (ff_common.rh_exact).
"""
import json, os, sys, time, hashlib, platform, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import flint, sympy, numpy as np
from ff_common import P_from_h, power_sums, place_counts, rh_exact, positivity_all_degrees

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'results', 'C5-function-field-transfer')
flint.ctx.prec = 512


def admissible_list(q, g):
    bounds = [math.comb(g, k) * (q + 1) ** k for k in range(g + 1)]
    res = []

    def rec(prefix):
        k = len(prefix)
        if k == g + 1:
            hcoef = list(reversed(prefix))
            P = P_from_h(hcoef, q)
            if positivity_all_degrees(P, q, g)['status'] == 'positive_all_d':
                res.append((hcoef, P))
            return
        for c in range(-bounds[k], bounds[k] + 1):
            pre = prefix + [c]
            hp = list(reversed(pre + [0] * (g + 1 - len(pre))))
            s, N, B = place_counts(P_from_h(hp, q), q, k)
            if all(B[d] >= 0 for d in range(1, k + 1)):
                rec(pre)
    rec([1])
    return res


def inertia(P, q, N):
    s = power_sums(P, N)
    qa = flint.arb(q)
    t = [flint.arb(s[k]) / qa ** (flint.arb(k) / 2) for k in range(N)]
    M = flint.acb_mat([[t[abs(m - n)] for n in range(N)] for m in range(N)])
    try:
        ev = M.eig(algorithm='rump')
        neg = sum(1 for e in ev if e.real < 0)
        pos = sum(1 for e in ev if e.real > 0)
        zer = N - neg - pos
        return neg, zer, pos, True
    except Exception:
        pass
    # second rigorous route (Jacobi's rule): if all leading principal minors D_1..D_N are
    # certified nonzero, n_- = number of sign changes in (1, D_1, ..., D_N).
    dets = []
    okj = True
    for k in range(1, N + 1):
        Dk = flint.arb_mat([[t[abs(m - n)] for n in range(k)] for m in range(k)]).det()
        if Dk.contains(0):
            okj = False
            break
        dets.append(1 if Dk > 0 else -1)
    if okj:
        seq = [1] + dets
        neg = sum(1 for a, b in zip(seq, seq[1:]) if a != b)
        return neg, 0, N - neg, True
    if True:
        tf = np.array([[float(s[abs(m - n)]) / q ** (abs(m - n) / 2) for n in range(N)] for m in range(N)])
        w = np.linalg.eigvalsh(tf)
        tol = 1e-9 * max(1, abs(w).max())
        return int((w < -tol).sum()), int((abs(w) <= tol).sum()), int((w > tol).sum()), False


def main():
    cases = [(3, 2), (4, 2), (5, 2), (7, 2), (2, 3), (3, 3)]
    t0 = time.time()
    summary = []
    x = sympy.symbols('x')
    for q, g in cases:
        t1 = time.time()
        L = admissible_list(q, g)
        stats = dict(q=q, g=g, admissible=len(L), squarefree=0, checked=0, agree_2g=0, agree_2g1=0,
                     rigorous_2g=0, rigorous_2g1=0, disagreements=[], nonsquarefree_examples=[])
        for hcoef, P in L:
            R = sympy.Poly(list(P), x)   # P descending? P is ascending -> reverse for R(T)=T^{2g}P(1/T)
            Rr = sympy.Poly(list(P), x)  # coefficients of R(T) descending == P ascending
            sqfree = sympy.gcd(Rr, Rr.diff(x)).degree() == 0
            rh, nreal, nout = rh_exact(hcoef, q)
            n_out = nout + (g - nreal)
            if not sqfree:
                if len(stats['nonsquarefree_examples']) < 5:
                    stats['nonsquarefree_examples'].append(dict(h_asc=hcoef, n_out=n_out,
                                                                 inertia_2g=inertia(P, q, 2 * g)))
                continue
            stats['squarefree'] += 1
            stats['checked'] += 1
            a = inertia(P, q, 2 * g)
            b = inertia(P, q, 2 * g + 1)
            stats['rigorous_2g'] += a[3]
            stats['rigorous_2g1'] += b[3]
            ok_a = (a[0] == n_out and a[1] == 0 and a[2] == 2 * g - n_out)
            ok_b = (b[0] == n_out and b[1] == 1 and b[2] == 2 * g - n_out)
            stats['agree_2g'] += ok_a
            stats['agree_2g1'] += ok_b
            if not (ok_a and ok_b) and len(stats['disagreements']) < 10:
                stats['disagreements'].append(dict(h_asc=hcoef, n_out=n_out, inertia_2g=a, inertia_2g1=b))
        stats['runtime_s'] = round(time.time() - t1, 1)
        print(stats, flush=True)
        summary.append(stats)
    meta = dict(script='ff_inertia_check.py', python=platform.python_version(), flint=flint.__version__,
                sympy=sympy.__version__, numpy=np.__version__, arb_prec_bits=512,
                runtime_s=round(time.time() - t0, 1),
                note='zero-eigenvalue count for N=2g+1 = balls not excluding 0 (rump enclosure)')
    fn = os.path.join(OUT, 'inertia_check.json')
    with open(fn, 'w') as f:
        json.dump(dict(meta=meta, cases=summary), f, indent=1, default=str)
    print('wrote', fn, hashlib.sha256(open(fn, 'rb').read()).hexdigest())


if __name__ == '__main__':
    main()
