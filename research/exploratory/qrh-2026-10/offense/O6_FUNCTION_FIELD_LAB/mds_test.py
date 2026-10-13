"""mds_test.py -- rationality tests for the 'multiple Dirichlet series of 1/L' (README §8). EXACT (Fractions).

Input: lab_mds output. For each exact row degree k (the y^k coefficient of Z):
  * x-direction, reciprocal:  s_k(d) = sum_{deg u = k} |[x^d] 1/L(x,psi_u)|^2  (diagonal of Z_k(x1,x2)),
                              f_k(d) = sum_{deg u = k}  [x^d] 1/L(x,psi_u)    (first moment), d = 0..dmax.
    Minimal linear recurrence (Berlekamp-Massey over Q, exact) = degree of the reduced denominator of the
    rational function sum_d s_k(d) t^d. A finite-group MDS needs these denominators to come from a fixed,
    finite set of polar divisors; generic (non-CM) members would give order ~ (number of rows) * (k-1)^2.
  * x-direction, control:     the same for L itself: polynomials of degree < k (order 0 beyond k-1).
  * y-direction at fixed d:   the sequence k -> s_k(d), k = 0..kmax, and its ratios to q^k.
Usage: python3 mds_test.py lab_mds_output [q]
"""
import sys
from fractions import Fraction


def bm(seq):
    """Berlekamp-Massey over Q: return (L, connection polynomial C) with C[0]=1."""
    s = [Fraction(x) for x in seq]
    C = [Fraction(1)]; B = [Fraction(1)]; L = 0; m = 1; b = Fraction(1)
    for n in range(len(s)):
        dlt = s[n] + sum(C[i] * s[n - i] for i in range(1, L + 1) if i < len(C))
        if dlt == 0:
            m += 1
            continue
        T = C[:]
        coef = dlt / b
        C = C + [Fraction(0)] * max(0, len(B) + m - len(C))
        for i in range(len(B)):
            C[i + m] -= coef * B[i]
        if 2 * L <= n:
            L = n + 1 - L; B = T; b = dlt; m = 1
        else:
            m += 1
    return L, C[:L + 1]


def main():
    path = sys.argv[1]
    M2 = {}; F1 = {}; C2 = {}
    q = None
    for line in open(path):
        t = line.split()
        if line.startswith('#'):
            q = int(t[1].split('=')[1]); continue
        if t[0] == 'F1':
            F1[(int(t[1]), int(t[2]))] = (int(t[3]), int(t[4]))
        elif t[0] == 'C1':
            C2[(int(t[1]), int(t[2]))] = int(t[6])
        else:
            M2[(int(t[1]), int(t[0]))] = int(t[3])
    kmax = max(k for k, _ in M2); dmax = max(d for _, d in M2)
    print(f'q={q}, row degrees k<=kmax={kmax}, column degrees d<=dmax={dmax} (terms available: {dmax+1})')
    print('| k (y-degree) | rows | BM order of s_k(d)=sum|[x^d]1/L|^2 | certified? | BM order of Re/omega parts of f_k(d)=sum [x^d]1/L | control: sum|[x^e]L|^2 nonzero only for e < k |')
    print('|---|---|---|---|---|---|')
    for k in range(0, kmax + 1):
        s = [M2[(k, d)] for d in range(dmax + 1)]
        L, C = bm(s)
        cert = 2 * L + 2 <= len(s)
        fa = [F1[(k, d)][0] for d in range(dmax + 1)]; fb = [F1[(k, d)][1] for d in range(dmax + 1)]
        La, _ = bm(fa); Lb, _ = bm(fb)
        ctrl = [C2.get((k, e), 0) for e in range(k)]
        print(f'| {k} | {q**k} | {L} | {"yes" if cert else "no (needs " + str(2*L+2) + " terms)"} | {La}, {Lb} | {ctrl} |')
        if cert and L <= 12:
            # print reduced denominator coefficients, scaled: C(t) = sum C_i t^i ; show C(t/q) coefficients
            Cs = [c * Fraction(1) for c in C]
            print(f'|   | denominator C(t) (t = x1 x2 on the diagonal): {[str(c) for c in Cs]} |  |  |  |')
    print('\ny-direction at fixed column degree d: s_k(d)/q^k for k = 0..kmax')
    for d in range(0, 5):
        print(f'd={d}: ' + ', '.join(str(Fraction(M2[(k, d)], q ** k)) for k in range(kmax + 1)))


if __name__ == '__main__':
    main()
