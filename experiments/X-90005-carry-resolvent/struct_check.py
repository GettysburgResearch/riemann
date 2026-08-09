"""Exact check of the structure theorem for the carry matrix B_T.

beta_{q,n} = floor(q/n)*(n-1-(q mod n))/(q+1),  q,n in {2..T}, lower triangular (row q, col n).

Claim chain (indices 2..T, zero-padding for virtual rows 0,1):
  b(q,n) := (q+1)*beta(q,n) = floor(q/n)*(n-1-(q mod n))
  Delta_q b(q,n)   = (q-1)*[n|q] - floor((q-1)/n)
  Delta_q^2 b(q,n) = (q-1)*([n|q] - [n|(q-1)])
Hence  N B = S^2 D_ Delta Z   with N=diag(q+1), S=lower-tri ones (cumsum),
D_=diag(q-1), Delta=I-shift, Z_{q,n}=[n|q].
=>  B^{-1} = M S D_^{-1} Delta^2 N,   M = Moebius matrix mu(q/n)[n|q]  (valid on {2..T}).
=>  row j of C := (B^T)^{-1}:
    c_j(n) = sum_{e|n} A_{j,e} mu(n/e)   with
    A_{j,e} = (j+1) * ( [e>=j]/(j-1) - 2*[e>=j+1]/j + [e>=j+2]/(j+1) )
            = (j+1)/(j-1)            if e==j
            = (j+1)(2-j)/(j(j-1))    if e==j+1
            = 2/(j(j-1))             if e>=j+2
Dirichlet symbol of row j:  (j+1)[2P_j(s)/j - P_{j-1}(s)/(j-1) - P_{j+1}(s)/(j+1)] / zeta(s),
P_k(s)=sum_{e<=k} e^{-s}.  For j=2,3 this must reproduce E_2, E_3 of L-32701 /(j(j-1)).
"""
from fractions import Fraction as F
from sympy import mobius

T = 60
idx = list(range(2, T + 1))
m = len(idx)

def beta(q, n):
    return F((q // n) * (n - 1 - q % n), q + 1)

B = [[beta(q, n) for n in idx] for q in idx]

# --- check Delta^2 identity
ok = True
def b(q, n):
    if q < 2: return F(0)
    return F((q // n) * (n - 1 - q % n))
for q in idx:
    for n in idx:
        d2 = b(q, n) - 2 * b(q - 1, n) + b(q - 2, n)
        pred = (q - 1) * ((1 if q % n == 0 else 0) - (1 if (q - 1) % n == 0 else 0))
        if d2 != pred:
            ok = False; print("D2 FAIL", q, n, d2, pred)
print("Delta^2 identity exact:", ok)

# --- exact inverse of B^T via back substitution (rationals)
# C * B^T = I  with B^T upper triangular: C_{j,n}
C = [[F(0)] * m for _ in range(m)]
BT = [[B[c][r] for c in range(m)] for r in range(m)]  # BT[r][c] = B[c][r]
for j in range(m):
    for n in range(j, m):
        if n == j:
            C[j][n] = 1 / BT[n][n]
        else:
            s = sum(C[j][k] * BT[k][n] for k in range(j, n))
            C[j][n] = -s / BT[n][n]

# --- predicted rows
def A(j, e):
    v = F(0)
    if e >= j:     v += F(j + 1, j - 1)
    if e >= j + 1: v -= F(2 * (j + 1), j)
    if e >= j + 2: v += F(1)
    return v

ok2 = True
for jj, j in enumerate(idx):
    for nn, n in enumerate(idx):
        pred = F(0)
        if n % 1 == 0:
            for e in range(2, n + 1):
                if n % e == 0:
                    pred += A(j, e) * int(mobius(n // e))
        if C[jj][nn] != pred:
            ok2 = False
            print("ROW FAIL", j, n, C[jj][nn], pred)
print("row formula c_j(n) = sum_{e|n} A_{j,e} mu(n/e) exact:", ok2)

# sample values
print("C[2,2..8] =", [C[0][k] for k in range(0, 7)])
print("C[3,3..9] =", [C[1][k] for k in range(1, 8)])
