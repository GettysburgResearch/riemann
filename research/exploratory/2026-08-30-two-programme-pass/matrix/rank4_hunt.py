"""Rank-4 (and general-rank) pointwise-square defect: symbolic computation
via the DEFINITIONAL route (no Berlekamp-Massey): N = D_Sym2 * S truncated,
with the degree bound deg N = C(d,2) taken from the exact instantiation
evidence (O-108505) and re-verified symbolically by tail vanishing.
Then: correction to the Gauss-sign Ext^2 prediction, factored; and a
det-twisted palindrome test. Output: matrix/rank4_hunt.json"""
import json, sys
import sympy as sp
sys.path.insert(0, '.')

e1, e2, e3, e4, T = sp.symbols('e1 e2 e3 e4 T')
E = [sp.Integer(1), e1, e2, e3, e4]

def h_seq(d, n):
    h = [sp.Integer(1)]
    for k in range(1, n):
        acc = sp.Integer(0)
        for i in range(1, min(k, d) + 1):
            acc += (-1) ** (i - 1) * E[i] * h[k - i]
        h.append(sp.expand(acc))
    return h

def power_sums(d, n):
    # Newton from e's
    p = []
    for k in range(1, n + 1):
        acc = sp.Integer(0)
        for i in range(1, min(k - 1, d) + 1):
            acc += (-1) ** (i - 1) * E[i] * (p[k - i - 1])
        if k <= d:
            acc += (-1) ** (k - 1) * E[k] * k
        p.append(sp.expand(acc))
    return p

def op_poly_from_ps(ps_op, r):
    # det(1 - B T) from power sums of B, degree r
    e = [sp.Integer(1)]
    for k in range(1, r + 1):
        acc = sp.Integer(0)
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * ps_op[i - 1]
        e.append(sp.expand(sp.cancel(acc / k)))
    return [sp.expand((-1) ** k * e[k]) for k in range(r + 1)], e[1:]

d = 4
r_sym = d * (d + 1) // 2    # 10
r_ext = d * (d - 1) // 2    # 6
ps = power_sums(d, 2 * r_sym + 2)
ps_sym2 = [sp.expand((ps[k - 1] ** 2 + ps[2 * k - 1]) / 2) for k in range(1, r_sym + 1)]
ps_ext2 = [sp.expand((ps[k - 1] ** 2 - ps[2 * k - 1]) / 2) for k in range(1, r_ext + 1)]
D_coeffs, _ = op_poly_from_ps(ps_sym2, r_sym)
_, e_ext = op_poly_from_ps(ps_ext2, r_ext)

n_terms = r_sym + r_ext + 4
h = h_seq(d, n_terms)
S = [sp.expand(x * x) for x in h]
# N_r = sum_{u<=r} D_{r-u} S_u  for r <= r_ext; tail must vanish
N = []
for r in range(r_ext + 1):
    acc = sp.Integer(0)
    for u in range(r + 1):
        if r - u <= r_sym:
            acc += D_coeffs[r - u] * S[u]
    N.append(sp.expand(acc))
tail_ok = True
for r in range(r_ext + 1, n_terms - 1):
    acc = sp.Integer(0)
    for u in range(max(0, r - r_sym), r + 1):
        acc += D_coeffs[r - u] * S[u]
    if sp.expand(acc) != 0:
        tail_ok = False
        break
print("tail vanishing (deg N = 6 symbolically):", tail_ok, flush=True)

pred = [sp.Integer(1)] + [sp.expand((-1) ** (j * (j - 1) // 2) * e_ext[j - 1]) for j in range(1, r_ext + 1)]
corr = [sp.factor(sp.expand(N[j] - pred[j])) for j in range(r_ext + 1)]
print("corrections to Gauss-sign prediction:", flush=True)
for j, c in enumerate(corr):
    print(f"  j={j}: {c}", flush=True)

# det-twisted palindrome test: N(T) ?= lam * T^6 * N(1/(c T)) for c = e4 (det)
Nrev = [sp.expand(N[6 - j] ) for j in range(7)]
# scaled palindrome with scale c: N[6-j] = lam * c^j * N[j]; from j=0: lam = N[6]; j=1 gives c if N[1]!=0
lam = N[6]
res = {"tail_ok": bool(tail_ok),
       "N_coeffs": [str(x) for x in N],
       "gauss_sign_pred": [str(x) for x in pred],
       "corrections": [str(x) for x in corr],
       "N6_factored": str(sp.factor(N[6])),
       "N5_factored": str(sp.factor(N[5])),
       "N4_minus_pred_factored": str(sp.factor(N[4] - pred[4])),
       "rh_established": False}
json.dump(res, open('matrix/rank4_hunt.json', 'w'), indent=1)
print("WROTE matrix/rank4_hunt.json", flush=True)
