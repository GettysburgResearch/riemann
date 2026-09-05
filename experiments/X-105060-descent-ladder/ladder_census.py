"""Lane B1 census: real-zero counts by sign changes + total counts by winding
around rectangle [eta, T] x [-1, 1], for Xi_0..Xi_3, T in {50, 100}.
Also: edge sub-lemma check and constants.
Outputs results.json and human-readable tables.
"""
import json, time
import mpmath as mp
from xi_ladder import Xi_all, Xi_all_real

mp.mp.dps = 40
K = 3
ETA = mp.mpf(2)

# ---------- real zero scan ----------
def scan_real_zeros(t_lo, t_hi, step, K=3):
    """Sign-change count and refined zero locations for Xi_0..Xi_K on (t_lo, t_hi]."""
    n = int(mp.ceil((t_hi - t_lo)/step))
    grid = [t_lo + step*i for i in range(n+1)]
    if grid[-1] < t_hi: grid.append(mp.mpf(t_hi))
    vals = [Xi_all_real(t, K) for t in grid]
    zeros = {k: [] for k in range(K+1)}
    for k in range(K+1):
        for i in range(len(grid)-1):
            a, b = vals[i][k], vals[i+1][k]
            if a == 0:
                zeros[k].append(grid[i])  # exact grid hit (unlikely)
            elif a*b < 0:
                # bisect
                lo, hi, flo = grid[i], grid[i+1], a
                for _ in range(50):
                    midt = (lo+hi)/2
                    fm = Xi_all_real(midt, K)[k]
                    if fm == 0: lo = hi = midt; break
                    if flo*fm < 0: hi = midt
                    else: lo, flo = midt, fm
                zeros[k].append((lo+hi)/2)
    return zeros

# ---------- winding ----------
def winding_rect(eta, T, K=3, tol=1.0, maxdepth=48):
    """Winding numbers of Xi_0..Xi_K around rectangle [eta,T]x[-1,1], CCW.
    Adaptive phase tracking; refine while any |dphi| > tol."""
    corners = [mp.mpc(eta, -1), mp.mpc(T, -1), mp.mpc(T, 1), mp.mpc(eta, 1), mp.mpc(eta, -1)]
    # initial subdivisions per edge
    def seed(a, b):
        L = abs(b - a)
        n = max(4, int(L/mp.mpf('0.5')))
        return [a + (b-a)*mp.mpf(i)/n for i in range(n)]  # exclude b (next edge adds it)
    pts = []
    for e in range(4):
        pts += seed(corners[e], corners[e+1])
    pts.append(corners[4])
    cache = {}
    def F(t):
        key = (mp.nstr(t.real, 30), mp.nstr(t.imag, 30))
        if key not in cache:
            cache[key] = Xi_all(t, K)
        return cache[key]
    total = [mp.mpf(0)]*(K+1)
    nrefine = [0]
    def dphi(v1, v2, k):
        return mp.arg(v2[k]/v1[k])
    def walk(a, b, va, vb, depth):
        d = [dphi(va, vb, k) for k in range(K+1)]
        if all(abs(x) <= tol for x in d) or depth >= maxdepth:
            if depth >= maxdepth: nrefine[0] = -999  # flag failure
            for k in range(K+1): total[k] += d[k]
            return
        m = (a+b)/2; vm = F(m); nrefine[0] += 1
        walk(a, m, va, vm, depth+1)
        walk(m, b, vm, vb, depth+1)
    vs = [F(p) for p in pts]
    for i in range(len(pts)-1):
        walk(pts[i], pts[i+1], vs[i], vs[i+1], 0)
    wind = [float(total[k]/(2*mp.pi)) for k in range(K+1)]
    return wind, len(cache), nrefine[0]

# ---------- edge sub-lemma check ----------
def edge_check(xs, K=3):
    """|xi^{(k+1)}/xi^{(k)}(3/2+ix) - l(s)| for k=0..K-1, plus |l(s)|."""
    rows = []
    for x in xs:
        s = mp.mpc(1.5, x)
        from xi_ladder import xi_derivs_s
        xs_d = xi_derivs_s(s, K)
        l = mp.log(s/(2*mp.pi))/2
        row = {'x': float(x), 'abs_l': float(abs(l))}
        for k in range(K):
            E = xs_d[k+1]/xs_d[k] - l
            row[f'E{k}'] = float(abs(E))
            row[f'ratio{k}'] = float(abs(E)/abs(l))
        rows.append(row)
    return rows

def main():
    res = {}
    t0 = time.time()
    # constants
    Z1 = float(-mp.zeta(mp.mpf('1.25'), 1, 1)/mp.zeta(mp.mpf('1.25')))
    Zhalf = float(-mp.zeta(mp.mpf('1.5'), 1, 1)/mp.zeta(mp.mpf('1.5')))
    res['Z1_minus_zetaprime_over_zeta_5_4'] = Z1
    res['minus_zetaprime_over_zeta_3_2'] = Zhalf
    print("Z1 = -zeta'/zeta(5/4) =", Z1, " ; -zeta'/zeta(3/2) =", Zhalf)

    # small-t real zeros on (0.02, 2]
    print("scanning (0.02, 2] ...")
    z_small = scan_real_zeros(mp.mpf('0.02'), mp.mpf(2), mp.mpf('0.02'), K)
    res['real_zeros_(0.02,2]'] = {k: [float(t) for t in v] for k, v in z_small.items()}
    print({k: len(v) for k, v in z_small.items()})

    # main scans
    for T in [50, 100]:
        print(f"scanning (2, {T}] ...")
        z = scan_real_zeros(ETA, mp.mpf(T), mp.mpf('0.25'), K)
        res[f'real_zeros_T{T}'] = {k: [float(t) for t in v] for k, v in z.items()}
        res[f'real_counts_T{T}'] = {k: len(v) for k, v in z.items()}
        print("real counts (2,%d]:" % T, res[f'real_counts_T{T}'])
        print(f"winding rect [2,{T}]x[-1,1] ...")
        w, nev, nref = winding_rect(ETA, mp.mpf(T), K)
        res[f'winding_T{T}'] = w
        res[f'winding_T{T}_evals'] = nev
        print("winding:", w, "evals:", nev, "refines:", nref)

    # edge check
    print("edge sub-lemma check ...")
    res['edge_check'] = edge_check([mp.mpf(x) for x in [20, 50, 100, 200, 500]], K)
    for r in res['edge_check']:
        print(r)

    res['dps'] = mp.mp.dps
    res['elapsed_s'] = time.time() - t0
    with open('results.json', 'w') as f:
        json.dump(res, f, indent=1, default=str)
    print("elapsed", res['elapsed_s'])

if __name__ == '__main__':
    main()
