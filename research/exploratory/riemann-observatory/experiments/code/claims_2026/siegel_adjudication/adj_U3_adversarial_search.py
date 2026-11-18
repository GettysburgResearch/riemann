# Find fundamental discriminants d, 4e5 < |d| <= 1e10, d = 5 mod 8, with chi_d(p) = -1 for every prime p <= P,
# P as large as possible. These have unusually small L(1, chi_d) and are the natural hardest cases for LZZ's test.
import sys, math, json
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # the run copy inserted the scratchpad path instead
import numpy as np
from sympy import factorint, primerange
from adj_U3_lzz_predicate import kron

S = [3, 5, 7, 11, 13, 17, 19, 23]
M = 8
res = np.array([5], dtype=np.int64)
for p in S:
    nonres = [a for a in range(1, p) if pow(a, (p - 1) // 2, p) == p - 1]
    # CRT combine: x = res mod M, x = a mod p
    inv = pow(M % p, -1, p)
    new = []
    for a in nonres:
        t = ((a - res) % p) * inv % p
        new.append(res + M * t)
    res = np.concatenate(new)
    M *= p
print("modulus", M, "classes", len(res))
cands = []
for k in range(-12, 12):
    d = res + k * M
    m = (np.abs(d) > 400_000) & (np.abs(d) <= 10 ** 10)
    cands.append(d[m])
d = np.concatenate(cands)
print("candidates", len(d))
runlen = {}
P = list(primerange(29, 2000))
alive = d.copy()
prev_p = 23
for p in P:
    a = np.mod(alive, p)
    e = (p - 1) // 2
    # vectorized pow with scalar modulus
    r = np.ones_like(a); b = a.copy(); ee = e
    while ee:
        if ee & 1: r = (r * b) % p
        b = (b * b) % p; ee >>= 1
    keep = (r == p - 1)
    if keep.sum() == 0:
        print(f"no candidate survives p={p}; survivors through previous prime: {len(alive)}")
        break
    # record run length (largest p with all -1) for d that drop out now, when few remain
    if len(alive) <= 400:
        for x in alive[~keep]:
            runlen[int(x)] = prev_p
    alive = alive[keep]
    prev_p = p
for x in alive:
    runlen[int(x)] = prev_p
def sqfree(n):
    return all(e == 1 for e in factorint(abs(n)).values())
ranked = sorted(runlen.items(), key=lambda kv: -kv[1])
out = []
for x, pl in ranked:
    if sqfree(x):
        out.append((x, pl))
    if len(out) >= 12: break
print("top fundamental discriminants (d, largest P with chi_d(p)=-1 for all p<=P):")
for x, pl in out: print(x, pl)
json.dump(out, open(sys.argv[1], 'w'))
