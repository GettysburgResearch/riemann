"""Full symbolic rank-5 square-defect corrections, factored (complete proof
of the rank-5 closed correction list). Writes matrix/rank5_symbolic.json"""
import json, sys
import sympy as sp
sys.path.insert(0, '.')

es = sp.symbols('e1 e2 e3 e4 e5')
T = sp.Symbol('T')
E = [sp.Integer(1)] + list(es)
d, r_sym, r_ext = 5, 15, 10

def h_seq(n):
    h = [sp.Integer(1)]
    for k in range(1, n):
        acc = sp.Integer(0)
        for i in range(1, min(k, d) + 1):
            acc += (-1) ** (i - 1) * E[i] * h[k - i]
        h.append(sp.expand(acc))
    return h

def power_sums(n):
    p = []
    for k in range(1, n + 1):
        acc = sp.Integer(0)
        for i in range(1, min(k - 1, d) + 1):
            acc += (-1) ** (i - 1) * E[i] * p[k - i - 1]
        if k <= d:
            acc += (-1) ** (k - 1) * E[k] * k
        p.append(sp.expand(acc))
    return p

def elem_from_ps(ps, r):
    e = [sp.Integer(1)]
    for k in range(1, r + 1):
        acc = sp.Integer(0)
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * ps[i - 1]
        e.append(sp.expand(sp.cancel(acc / k)))
    return e[1:]

ps = power_sums(2 * r_sym + 2)
ps_s2 = [sp.expand((ps[k-1]**2 + ps[2*k-1]) / 2) for k in range(1, r_sym + 1)]
ps_e2 = [sp.expand((ps[k-1]**2 - ps[2*k-1]) / 2) for k in range(1, r_ext + 1)]
e_s2 = elem_from_ps(ps_s2, r_sym)
D = [sp.Integer(1)] + [sp.expand((-1)**k * e_s2[k-1]) for k in range(1, r_sym + 1)]
e_x2 = elem_from_ps(ps_e2, r_ext)

n_terms = r_sym + r_ext + 3
h = h_seq(n_terms)
S = [sp.expand(x*x) for x in h]
N = []
for r in range(r_ext + 1):
    acc = sp.Integer(0)
    for u in range(r + 1):
        if r - u <= r_sym:
            acc += D[r - u] * S[u]
    N.append(sp.expand(acc))
    print(f"N[{r}] done", flush=True)
tail_ok = all(sp.expand(sum(D[r-u]*S[u] for u in range(max(0, r-r_sym), r+1))) == 0
              for r in range(r_ext + 1, n_terms - 1))
print("tail vanishing:", tail_ok, flush=True)
pred = [sp.Integer(1)] + [sp.expand((-1)**(j*(j-1)//2) * e_x2[j-1]) for j in range(1, r_ext+1)]
out = {"tail_ok": bool(tail_ok), "corrections_factored": {}, "rh_established": False}
for j in range(r_ext + 1):
    c = sp.factor(sp.expand(N[j] - pred[j]))
    out["corrections_factored"][str(j)] = str(c)
    print(f"corr[{j}] = {c}", flush=True)
json.dump(out, open('matrix/rank5_symbolic.json', 'w'), indent=1)
print("WROTE matrix/rank5_symbolic.json", flush=True)
