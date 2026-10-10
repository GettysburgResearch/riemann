#!/usr/bin/env python3
"""Aggregate-license repair: core fibre machinery.
rho_j(k) = Q_{x/k}(j)/(4 sqrt(x/k)-3);  Q per L-99240.2;  s(k)=g(sqrt(x/k)).
Exact reduction: feasibility <=> greedy prefix-fill c* passes 3 aggregate tests.
"""
import numpy as np
from math import sqrt, log

def sieve_mu(N):
    mu = np.ones(N+1, dtype=np.int8); mu[0] = 0
    primes = []
    is_comp = np.zeros(N+1, dtype=bool)
    for i in range(2, N+1):
        if not is_comp[i]:
            primes.append(i); mu[i] = -1
        for p in primes:
            if i*p > N: break
            is_comp[i*p] = True
            if i % p == 0:
                mu[i*p] = 0; break
            else:
                mu[i*p] = -mu[i]
    return mu, primes

def gamma_j(j, m):
    if m < j: return 0.0
    if m == j: return (j+1)/(j-1)
    if m == j+1: return -((j+1)*(j-2))/(j*(j-1))
    return 2.0/(j*(j-1))

def Q(Y, j):
    """Q_Y(j) = sum_{m<=Y} gamma_j(m)/sqrt(m) log(Y/m)  (L-99240.2)."""
    if Y < j: return 0.0
    M = int(np.floor(Y))
    tot = 0.0
    for m in range(j, M+1):
        tot += gamma_j(j, m)/sqrt(m)*log(Y/m)
    return tot

def fibre(x, mu):
    ks = [k for k in range(1, int(np.floor(x))+1) if mu[k] != 0]
    T = {k: (4*sqrt(x/k)-3)/sqrt(k) for k in ks}
    E = [k for k in ks if mu[k] == 1]
    O = [k for k in ks if mu[k] == -1]
    return ks, E, O, T

def profiles(x, ks, js=(2,3)):
    rho = {j: {} for j in js}; s = {}
    for k in ks:
        Y = x/k
        den = 4*sqrt(Y)-3
        for j in js:
            rho[j][k] = Q(Y, j)/den
        z = sqrt(Y)
        s[k] = (5*z-3)/(4*z-3)
    return rho, s

def greedy_margins(x, mu, js=(2,3)):
    """Exact feasibility test by the reduction theorem.
    Returns dict with TB, row margins (j=2,3), score margin, fill threshold."""
    ks, E, O, T = fibre(x, mu)
    rho, s = profiles(x, ks, js)
    D = sum(T[o] for o in O)               # total demand
    capE = sum(T[e] for e in E)
    TB = capE - D                          # total balance
    K = {j: sum(T[o]*rho[j][o] for o in O) for j in js}
    Ks = sum(T[o]*s[o] for o in O)
    # greedy prefix fill: smallest evens first (rho_j max, s min)
    Es = sorted(E)
    c = {}
    rem = D
    estar = None
    for e in Es:
        take = min(T[e], rem)
        c[e] = take; rem -= take
        if rem <= 1e-15 and estar is None:
            estar = e
    feas_base = (rem <= 1e-9*max(1.0, D))
    m_row = {j: sum(c[e]*rho[j][e] for e in Es) - K[j] for j in js}
    m_sc = Ks - sum(c[e]*s[e] for e in Es)
    G = {j: sum(T[e]*rho[j][e] for e in Es) - K[j] for j in js}  # = signed row
    return dict(x=x, TB=TB, feas_base=feas_base, m2=m_row[2], m3=m_row[3],
                m_sc=m_sc, G2=G[2], G3=G[3], estar=estar, D=D,
                nE=len(E), nO=len(O))

def nested_prefix_deficit(x, mu):
    """max_t (-H_t(x))_+ (nested-license deficit), argmax t."""
    ks, E, O, T = fibre(x, mu)
    acc = 0.0; worst = (0.0, None)
    for k in sorted(ks):
        acc += int(mu[k])*T[k]
        if mu[k] == -1 and -acc > worst[0]:
            worst = (-acc, k)
    return worst

if __name__ == "__main__":
    mu, _ = sieve_mu(1200)
    # sanity: Q asymptotics Q_Y(j) ~ 4 C_j sqrt(Y), C_2=1, C_3=1/3
    for j in (2,3):
        Cj = 2.0/(j*(j-1))
        for Y in (10, 100, 1000):
            print(f"Q_{Y}({j}) = {Q(Y,j):.6f}   4C_j sqrt(Y) = {4*Cj*sqrt(Y):.6f}")
    # rho monotone decreasing in k, s increasing: spot check x=88
    ks, E, O, T = fibre(88.0, mu)
    rho, s = profiles(88.0, ks)
    kk = sorted(ks)
    mono_rho = all(rho[2][kk[i]] >= rho[2][kk[i+1]] - 1e-14 and
                   rho[3][kk[i]] >= rho[3][kk[i+1]] - 1e-14 for i in range(len(kk)-1))
    mono_s = all(s[kk[i]] <= s[kk[i+1]] + 1e-14 for i in range(len(kk)-1))
    print("x=88: rho_2,rho_3 nonincreasing:", mono_rho, "  s nondecreasing:", mono_s)
    # L-105021 continuity check: nested first failure (89,88,13), deficit 0.010592047
    d, t = nested_prefix_deficit(88.0, mu)
    print(f"nested deficit at x=88: {d:.9f} at t={t}   (L-105021: 0.010592047 at 13)")
    # aggregate greedy at x=88
    r = greedy_margins(88.0, mu)
    print({k: (round(v,9) if isinstance(v,float) else v) for k,v in r.items()})
