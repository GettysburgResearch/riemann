# quick diagnostic: size of sum_{s sf primary, Y<=Ns<=2Y} gamma_1(s) * conj chi_s(-m) [* c(s)] vs sqrt(#s)
import sys, os, math, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import na_model as M
X = int(sys.argv[1])
P = M.make_primes(X); sf = M.sf_elements(P, X)
print('n sf', len(sf))
data = []
for el, N, fac in sf:
    if N < 2: continue
    g1 = M.gamma_sf(P, fac, 1)
    kb = M.chi_exp_el(P, fac, (2, -2)); cs = M.ZETA[kb] * np.conj(M.xi_el(el))
    data.append((N, g1, cs, el, fac))
for m in [(1, 0), (-1, 0), (2, 0), (1, 3), (5, 2)]:
    row = []
    for Y in [250, 1000, 4000, X // 2]:
        sel = [(g1, cs, el, fac) for (N, g1, cs, el, fac) in data if Y <= N <= 2 * Y]
        t0 = 0; t1 = 0
        for g1, cs, el, fac in sel:
            k = M.chi_exp_el(P, fac, (-m[0], -m[1]))
            if k < 0: continue
            v = g1 * np.conj(M.ZETA[k])
            t0 += v; t1 += v * cs
        row.append((Y, len(sel), round(abs(t0) / math.sqrt(len(sel)), 2), round(abs(t1) / math.sqrt(len(sel)), 2)))
    print(m, row)
