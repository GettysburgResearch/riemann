"""Coarse Segre bridge identity, symbolic machine check over Q(a,b):

    K_m(A,T) := det(1 - V^{tensor m} T) * sum_r h_r(A)^m T^r

is a POLYNOMIAL and equals

    N_m(T) * prod_{k>=1} det(1 - Sym^{m-2k}(A) b^k T)^{c_k},
    c_k = C(m,k) - C(m,k-1)   (ballot numbers),

with N_m the T-108500 defect numerator. Symbolic in the inverse roots
(alpha, beta); both sides expanded and compared coefficientwise, plus a
tail window of 4 vanishing coefficients past degree 2^m. m = 2..4
complete in minutes; m = 5, 6 are heavy (the m=6 side has 64 tensor
weights) -- the stdlib replay X-108515 covers m = 5, 6 by exact integer
instantiation through an independent matrix route instead.
rh_established = false.
"""
import sys
from itertools import product
from math import comb

import sympy as sp

a, b, T = sp.symbols('a b T')
al, be = sp.symbols('alpha beta')


def h_seq(n):
    h = [sp.Integer(1), a]
    for _ in range(2, n + 1):
        h.append(sp.expand(a * h[-1] - b * h[-2]))
    return h


def det_one_minus(weights):
    p = sp.Integer(1)
    for w in weights:
        p = sp.expand(p * (1 - w * T))
    return p


def sym_weights(m):
    return [al ** i * be ** (m - i) for i in range(m + 1)]


def main(mrange):
    sys.path.insert(0, 'matrix')
    from c1_defect_atlas import defect_numerator
    for m in mrange:
        tensor_weights = []
        for bits in product([0, 1], repeat=m):
            w = sp.Integer(1)
            for t in bits:
                w *= (al if t == 0 else be)
            tensor_weights.append(w)
        D_full = det_one_minus(tensor_weights)
        h = h_seq(2 ** m + m + 6)
        hab = [sp.expand(v.subs({a: al + be, b: al * be})) for v in h]
        deg = 2 ** m
        Dc = [sp.expand(D_full.coeff(T, i)) for i in range(deg + 1)]
        K = []
        for r in range(deg + 5):
            s = sp.Integer(0)
            for i in range(min(r, deg) + 1):
                s += Dc[i] * hab[r - i] ** m
            K.append(sp.expand(s))
        tail_ok = all(v == 0 for v in K[deg + 1:])
        N = defect_numerator(m)
        Npoly = sum(sp.expand(c.subs({a: al + be, b: al * be})) * T ** i
                    for i, c in enumerate(N))
        R = Npoly
        for k in range(1, m // 2 + 1):
            ck = comb(m, k) - comb(m, k - 1)
            wts = [w * (al * be) ** k for w in sym_weights(m - 2 * k)]
            R = sp.expand(R * det_one_minus(wts) ** ck)
        Kpoly = sum(K[i] * T ** i for i in range(deg + 1))
        diff = sp.expand(Kpoly - R)
        print(f"m={m}: K polynomial (tail zero): {tail_ok}; "
              f"K == N_m * excess: {diff == 0}", flush=True)


if __name__ == "__main__":
    args = [int(x) for x in sys.argv[1:]] or list(range(2, 5))
    main(args)
