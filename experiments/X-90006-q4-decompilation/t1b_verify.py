#!/usr/bin/env python3
"""T1b step 1-2: verify Chebyshev identity for I_2; reproduce n<=5000 ratio scan."""
import numpy as np, math

def sieve_mu_lambda(N):
    mu = np.ones(N+1, dtype=np.int64); mu[0] = 0
    lam = np.zeros(N+1)               # von Mangoldt
    comp = np.zeros(N+1, bool)
    for p in range(2, N+1):
        if not comp[p]:
            comp[p*p::p] = True if p*p <= N else comp[p*p::p]
            mu[p::p] *= -1
            pp = p*p
            if pp <= N:
                mu[pp::pp] = 0
            q = p
            while q <= N:
                lam[q::q] += 0  # placeholder
                q *= p
    # redo lambda properly
    lam = np.zeros(N+1)
    comp = np.zeros(N+1, bool)
    for p in range(2, N+1):
        if not comp[p]:
            if p*p <= N:
                comp[p*p::p] = True
            q = p
            lp = math.log(p)
            while q <= N:
                lam[q] = lp
                q *= p
    return mu, lam

MU, LAM = sieve_mu_lambda(4000)
PSI = np.cumsum(LAM)  # PSI[x] = psi(x)

def carry(n, j, d):
    return n//d - j//d - (n-j)//d

def b_odd(m):
    return int(MU[m]) if m % 2 == 1 else 0

def Q_odd_direct(n, j):
    # L_e(q_odd), q_odd(m) = -b_odd(m) log m
    s = 0.0
    for d in range(3, n+1, 2):
        c = carry(n, j, d)
        if c and MU[d]:
            s -= MU[d]*math.log(d)*c
    return s

def C2(x):
    return 0 if x <= 0 else x.bit_length()

def Y_odd(n, j):
    return C2(n) - C2(j) - C2(n-j)

def I2_direct(n, j):
    return Q_odd_direct(2*n, 2*j) - Q_odd_direct(n, j)

def I2_formula(n, j):
    k = n - j
    return PSI[2*n] - PSI[2*j] - PSI[2*k] - math.log(2)*Y_odd(n, j)

bad = 0
for n in range(2, 130):
    for j in range(1, n):
        a, b = I2_direct(n, j), I2_formula(n, j)
        if abs(a-b) > 1e-9*(1+abs(a)):
            bad += 1
            if bad < 5: print("MISMATCH", n, j, a, b)
print("identity check n<130:", "PASS" if bad == 0 else f"FAIL x{bad}")
