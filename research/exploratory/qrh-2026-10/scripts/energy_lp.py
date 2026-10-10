"""Exact sup of the reflected-energy exponent E_ref (Lemma 14.3, eq. 14.14) over admissible dyads,
for marked completed rows with row length M' and active slot length <= l' (Lemma 15.1 setting:
f=1, rho=1, completed scale N* = 1 + l').  Union of LPs over the max/min branches."""
import numpy as np
from scipy.optimize import linprog

# variable order: O, A0, H, za, v, lb, el, p   (p models -(Td - y)_+/2 via p<=0, p<= -(Td-y)/2)
def sup_energy(Mp, lp, tau=0.0, allow_S=True):
    best = -np.inf; arg = None
    for maxbr in ('H', 'v'):
        for ubr in ('v', 'za', 'avg'):
            # objective coefficients (maximize) : O/2 + max + za - u - lb - 2el/3 + p
            c = np.zeros(8)
            c[0] += 0.5
            if maxbr == 'H': c[2] += 1
            else: c[4] += 1; c[5] += 1
            c[3] += 1
            if ubr == 'v': c[4] -= 1
            elif ubr == 'za': c[3] -= 1
            else: c[4] -= 1/3; c[3] -= 1/3
            c[5] -= 1; c[6] -= 2/3; c[7] += 1
            A = []; b = []
            # Td = 2H + 2A0 + 2za - (1 + lp)   (N0=B0=S0=0: they only lower Td/E_ref)
            # p <= -(Td - y)/2  ->  p + H + A0 + za - (v + 3lb + el)/2 <= (1+lp)/2
            A.append([0, 1, 1, 1, -0.5, -1.5, -0.5, 1]); b.append((1 + lp)/2)
            # retained dyad: y <= Td + tau  -> v + 3lb + el - 2H - 2A0 - 2za <= -(1+lp) + tau
            A.append([0, -2, -2, -2, 1, 3, 1, 0]); b.append(-(1 + lp) + tau)
            # H <= Mp - O
            A.append([1, 0, 1, 0, 0, 0, 0, 0]); b.append(Mp)
            # 2 A0 <= O
            A.append([-1, 2, 0, 0, 0, 0, 0, 0]); b.append(0)
            # za <= lp
            A.append([0, 0, 0, 1, 0, 0, 0, 0]); b.append(lp)
            # branch consistency for max
            if maxbr == 'H':   # v + lb <= H
                A.append([0, 0, -1, 0, 1, 1, 0, 0]); b.append(0)
            else:              # H <= v + lb
                A.append([0, 0, 1, 0, -1, -1, 0, 0]); b.append(0)
            # branch consistency for u = min(v, za, (v+za)/3)
            if ubr == 'v':     # v <= za, v <= (v+za)/3 -> 2v <= za
                A.append([0, 0, 0, -1, 1, 0, 0, 0]); b.append(0)
                A.append([0, 0, 0, -1, 2, 0, 0, 0]); b.append(0)
            elif ubr == 'za':  # za <= v, za <= (v+za)/3 -> 2za <= v
                A.append([0, 0, 0, 1, -1, 0, 0, 0]); b.append(0)
                A.append([0, 0, 0, 2, -1, 0, 0, 0]); b.append(0)
            else:              # (v+za)/3 <= v and <= za -> za <= 2v, v <= 2za
                A.append([0, 0, 0, 1, -2, 0, 0, 0]); b.append(0)
                A.append([0, 0, 0, -2, 1, 0, 0, 0]); b.append(0)
            bounds = [(0, None)]*7 + [(None, 0)]
            res = linprog(-c, A_ub=np.array(A), b_ub=np.array(b), bounds=bounds, method='highs')
            if res.status == 0 and -res.fun > best:
                best = -res.fun; arg = (maxbr, ubr, res.x.round(5))
    return best, arg

if __name__ == '__main__':
    # check against the paper's closed form for M + l = 1
    for (M, l) in [(5/6, 1/6), (1.0, 0.0), (0.75, 0.25)]:
        for d in [0, 0.05, 1/6 if l >= 1/6 else l]:
            if d > l: continue
            Mp, lp = M - 2*d, l - d
            val, arg = sup_energy(Mp, lp)
            closed = max(Mp, (2*Mp + 1 + 3*lp)/4)
            print(f"M={M:.3f} l={l:.3f} d={d:.3f}: LP sup={val:.6f} closed={closed:.6f} {arg[:2]}")
    print("--- M + l > 1 ---")
    for (M, l) in [(5/6 + 0.02, 1/6 + 0.02), (0.9, 0.25), (1.0, 0.2)]:
        for d in [0, 0.05, 0.1]:
            if d > l: continue
            Mp, lp = M - 2*d, l - d
            val, arg = sup_energy(Mp, lp)
            closed = max(Mp, (2*Mp + 1 + 3*lp)/4)
            print(f"M={M:.3f} l={l:.3f} d={d:.3f}: LP sup={val:.6f} closed={closed:.6f} {arg}")
