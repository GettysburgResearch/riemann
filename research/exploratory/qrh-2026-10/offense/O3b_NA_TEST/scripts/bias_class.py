# diagnostic: Gauss-sum bias of sum gamma_1(s) restricted to ray classes s mod 4 (and mod 8), s primary sf.
import sys, os, math, numpy as np
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import na_model as M
X = int(sys.argv[1]); mod = int(sys.argv[2]); j = int(sys.argv[3]) if len(sys.argv) > 3 else 1
P = M.make_primes(X); sf = M.sf_elements(P, X)
acc = defaultdict(lambda: defaultdict(lambda: [0j, 0]))
for el, N, fac in sf:
    if N < 2: continue
    g = M.gamma_sf(P, fac, j)
    cl = (el[0] % mod, el[1] % mod)
    for Y in [X // 16, X // 8, X // 4, X // 2]:
        if Y <= N <= 2 * Y:
            acc[cl][Y][0] += g; acc[cl][Y][1] += 1
for cl in sorted(acc):
    print(cl, [(Y, v[1], round(abs(v[0]) / math.sqrt(max(v[1], 1)), 2), round(np.angle(v[0]) / np.pi * 6, 2)) for Y, v in sorted(acc[cl].items())])
