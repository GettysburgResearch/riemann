import sys, math, random, json, time
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # the run copy inserted the scratchpad path instead
import numpy as np
from sympy import factorint, jacobi_symbol
from adj_U3_lzz_predicate import kron, test_d, primes_upto_count

def kron_ref(d, p):
    if p == 2:
        if d % 2 == 0: return 0
        return 1 if d % 8 in (1, 7) else -1
    return jacobi_symbol(d % p, p)

# 1) validate the vectorized Kronecker symbol
rng = random.Random(20261117)
P = primes_upto_count(3000)
P_big = np.array([2147483647, 2147483629, 2700000023 if False else 2147483587], dtype=np.int64)
bad = 0
for _ in range(200):
    d = rng.choice([-1, 1]) * rng.randrange(400_001, 10_000_000_001)
    v = kron(d, P)
    for i in range(0, len(P), 37):
        if v[i] != kron_ref(d, int(P[i])): bad += 1
    vb = kron(d, P_big)
    for i, pp in enumerate(P_big):
        if vb[i] != kron_ref(d, int(pp)): bad += 1
print("kronecker mismatches:", bad)

def is_fund(d):
    if d % 4 == 1:
        return all(e == 1 for e in factorint(abs(d)).values())
    if d % 4 == 0:
        m = d // 4
        return m % 4 in (2, 3) and all(e == 1 for e in factorint(abs(m)).values())
    return False

# 2) random sample of fundamental discriminants, log-uniform in (4e5, 1e10]
sample = []
while len(sample) < int(sys.argv[1]):
    q = int(math.exp(rng.uniform(math.log(400_001), math.log(1e10))))
    d = rng.choice([-1, 1]) * q
    if 400_000 < q <= 10 ** 10 and is_fund(d):
        sample.append(d)
t0 = time.time()
res = []
for d in sample:
    res.append(test_d(d))
fails = [x for x in res if "fail_at_N0" in x]
ok = [x for x in res if "n_primes" in x]
row1 = [x["n_primes"] for x in ok if x["row"] == 1.6]
print(f"tested {len(res)} random fundamental discriminants in {time.time()-t0:.1f}s; verified {len(ok)}, not verified {len(fails)}")
from collections import Counter
print("row used:", Counter(x["row"] for x in ok))
if row1:
    print("row-1 primes needed: median", int(np.median(row1)), "mean", int(np.mean(row1)), "max", max(row1))
print("min excess at crossing:", min(x["excess"] for x in ok))
for x in sorted(ok, key=lambda x: -x["n_primes"])[:5]: print("hardest:", x)
for x in fails: print("FAIL:", x)
json.dump(res, open(sys.argv[2], 'w'))
