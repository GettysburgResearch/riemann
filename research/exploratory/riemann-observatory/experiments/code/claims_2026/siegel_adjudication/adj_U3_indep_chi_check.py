#!/usr/bin/env python3
"""U3 adjudication, pass 2: check the Euler-criterion chi_d(p) used by both predicate implementations
against a different algorithm (binary Jacobi symbol with quadratic reciprocity, pure Python integers),
for the 20 discriminants of adj_U3_indep_lzz_crosscheck, on primes p <= 10^5 and on 2000 random primes
in [10^8, 2.2*10^9]. Our own code. Usage: python3 -I adj_U3_indep_chi_check.py"""
import random
import numpy as np

DS = [-1170487, 321197109, -767859, -532423, -534027695, 5317693, -31508468, 556907356, -127576987,
      -6523943, -1479711, -39736243, 912163105, -5121298747, 112209653, -647457640, -433572483,
      578729093, -411366547, 9447241877]


def kronecker(d, n):
    res = 1
    while n % 2 == 0:
        n //= 2
        if d % 2 == 0:
            return 0
        if d % 8 in (3, 5):
            res = -res
    a = d % n
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def chi_euler_vec(d, p):  # same algorithm as adj_U3_indep_lzz_crosscheck.chi_vec (copied, not imported)
    out = np.empty(p.shape, dtype=np.int64)
    odd = p != 2
    po = p[odd]
    a = np.mod(np.int64(d), po)
    e = (po - 1) // 2
    res = np.ones_like(po)
    base = a.copy()
    while np.any(e > 0):
        m = (e & 1) == 1
        res = np.where(m, (res * base) % po, res)
        base = (base * base) % po
        e >>= 1
    out[odd] = np.where(a == 0, 0, np.where(res == 1, 1, -1))
    if np.any(~odd):
        out[~odd] = 0 if d % 2 == 0 else (1 if d % 8 in (1, 7) else -1)
    return out


def is_prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    dd, s = n - 1, 0
    while dd % 2 == 0:
        dd //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):  # deterministic for n < 3.3e24
        x = pow(a, dd, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


sieve = np.ones(100001, dtype=bool); sieve[:2] = False
for i in range(2, 317):
    if sieve[i]:
        sieve[i * i::i] = False
small = np.nonzero(sieve)[0].astype(np.int64)
rng = random.Random(20261117)
big = []
while len(big) < 2000:
    n = rng.randrange(10**8, 22 * 10**8)
    if is_prime(n):
        big.append(n)
P = np.concatenate([small, np.array(big, dtype=np.int64)])
mism = 0
for d in DS:
    v = chi_euler_vec(d, P)
    for p, x in zip(P.tolist(), v.tolist()):
        if kronecker(d, p) != x:
            mism += 1
print(f"discriminants {len(DS)}, primes per d {len(P)} ({len(small)} <= 1e5, {len(big)} random in [1e8, 2.2e9]);"
      f" Euler-vs-Jacobi mismatches: {mism}")
