#!/usr/bin/env python3
"""NRC32 twists: exact checker for (C1) the twisted Newton adapter and centered
cubic-mesh compression, and (C2) the character content of the coarse kernel.

Status: EXPLORATORY checker for research/exploratory/qrh-2026-10/NRC32_TWISTS.md.
Standard library only. Acceptance uses exact integer / rational arithmetic in
cyclotomic fields Q(zeta_N); no floating value enters any `require`.

Character values of the primitive characters mod q <= 12 lie in Q (orders 1,2),
Q(i) (order 4), Q(zeta_3) (orders 3,6) and Q(zeta_5) (orders 5,10). Only the
mod-5 complex characters are Gaussian; mod 7, 9, 11 need Q(zeta_3), Q(zeta_5).
Signs of real numbers are decided exactly: real elements of Q(i), Q(zeta_3)
are rational, and real elements of Q(zeta_5) are A + B*sqrt(5), A, B in Q.

What this checker certifies (finite statements only):
  C1  for all 27 primitive characters chi mod q <= 12 and Y in the panel:
      twisted Newton coefficients v_chi(n) = mu(n) chi(n) for all n < (Y+1)^2
      (producer uses mu only through Y; a separate sieve is the comparison);
      z_chi = chi * z (equivariance); the twisted adapter pointwise and the
      twisted block-mean formula with A^chi_d(t) = t H_chi(r) - d C_chi(r)
      (deep panels); exact orthogonal split annular F = S + D, the pair
      identity, increments |v_chi(k)/k| <= 1/k, D_I <= h(h^2-1)/(12a^2),
      Z < 5/6, and centre-invariance of D at several exact test centres.
  C2  zero-class form of the kernel; Phi_I strictly decreasing, hence
      r -> K_I(r,s) not q-periodic for q <= Y-1 (Y <= 15); the Ramanujan-sum
      expansion of H_floor(k/d) and its twisted version; Hoelder/von Sterneck
      formula and principal-only content of Ramanujan sums; the separated form
      m(k) = 2m(Y) - sum_q R_q(k) Z_q with Z_q given by principal-character
      Mobius sums, and its twisted version (twist on the Mobius-free side);
      the Euler-factor transfer identity; integer reciprocity and
      the Gauss-sum expansion of additive characters; |tau(chi)|^2 = conductor
      for squarefree moduli; Parseval of the coarse split over all characters
      mod q (progression energies).
It does NOT verify any infinite or asymptotic statement.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Fr
import functools
import hashlib
import itertools
import json
from math import gcd
import sys

COUNTS: dict[str, int] = {}
MUTATION = "none"


def require(ok: bool, label: str) -> None:
    if not ok:
        raise ValueError(label)
    key = label.split(":", 1)[0]
    COUNTS[key] = COUNTS.get(key, 0) + 1


def lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def lcm_upto(n: int) -> int:
    out = 1
    for j in range(2, n + 1):
        out = lcm(out, j)
    return out


# ---------------------------------------------------------------- arithmetic

def mobius_trial(nmax: int) -> list[int]:
    """Producer input (trial division); only queried through the prefix Y."""
    out = [0] * (nmax + 1)
    for n in range(1, nmax + 1):
        r, p, value = n, 2, 1
        while p * p <= r:
            if r % p == 0:
                r //= p
                value = -value
                if r % p == 0:
                    value = 0
                    break
            p += 1
        if value and r > 1:
            value = -value
        out[n] = value
    if MUTATION == "flip_prefix_mobius" and nmax >= 6:
        out[6] = -out[6]
    return out


def mobius_sieve(nmax: int) -> list[int]:
    """Independent full-length sieve, used only for comparison."""
    out, composite = [1] * (nmax + 1), bytearray(nmax + 1)
    out[0] = 0
    for p in range(2, nmax + 1):
        if not composite[p]:
            for n in range(p, nmax + 1, p):
                composite[n] = 1
                out[n] = -out[n]
            for n in range(p * p, nmax + 1, p * p):
                out[n] = 0
    return out


def totient(n: int) -> int:
    return sum(1 for a in range(1, n + 1) if gcd(a, n) == 1)


@functools.lru_cache(maxsize=None)
def divisors(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def prime_factors(n: int) -> list[int]:
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


# ---------------------------------------------------------- cyclotomic fields

_CYC: dict[int, list[int]] = {}


def cyclotomic(n: int) -> list[int]:
    """Integer coefficients (low to high) of the n-th cyclotomic polynomial."""
    if n in _CYC:
        return _CYC[n]
    num = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            b = cyclotomic(d)
            a = num[:]
            q = [0] * (len(a) - len(b) + 1)
            for i in range(len(a) - len(b), -1, -1):
                c = a[i + len(b) - 1]
                q[i] = c
                if c:
                    for j, bj in enumerate(b):
                        a[i + j] -= c * bj
            if any(a):
                raise ValueError("cyclotomic division not exact")
            num = q
    _CYC[n] = num
    return num


class Field:
    """Q(zeta_N) with basis 1, zeta, ..., zeta^(deg-1); elements are lists."""

    def __init__(self, n: int):
        self.N = n
        phi = cyclotomic(n)
        self.deg = deg = len(phi) - 1
        self.phi = phi
        maxj = max(2 * deg, n + 1)
        cur = [1] + [0] * (deg - 1)
        pw = [cur]
        for _ in range(maxj):
            top = cur[-1]
            nxt = [0] + cur[:-1]
            if top:
                for i in range(deg):
                    nxt[i] -= top * phi[i]
            pw.append(nxt)
            cur = nxt
        self.pw = pw

    def zero(self) -> list:
        return [0] * self.deg

    def const(self, c) -> list:
        out = [0] * self.deg
        out[0] = c
        return out

    def root(self, j: int) -> list:
        return self.pw[j % self.N][:]

    def add(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def sub(self, a, b):
        return [x - y for x, y in zip(a, b)]

    def scale(self, a, c):
        return [x * c for x in a]

    def mul(self, a, b):
        deg = self.deg
        prod = [0] * (2 * deg - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    if y:
                        prod[i + j] += x * y
        out = prod[:deg]
        for j in range(deg, 2 * deg - 1):
            c = prod[j]
            if c:
                pj = self.pw[j]
                for i in range(deg):
                    out[i] += c * pj[i]
        return out

    def conj(self, a):
        out = [0] * self.deg
        for i, x in enumerate(a):
            if x:
                pj = self.pw[(-i) % self.N]
                for t in range(self.deg):
                    out[t] += x * pj[t]
        return out

    def norm2(self, a):
        return self.mul(a, self.conj(a))

    def real_pair(self, a) -> tuple[Fr, Fr]:
        """Exact real value A + B sqrt(5) of a REAL element (N in 1,3,4,5)."""
        if self.N in (1, 2):
            return Fr(a[0]), Fr(0)
        if self.N in (3, 4, 6):
            require(a[1] == 0, "real_element")
            return Fr(a[0]), Fr(0)
        if self.N in (5, 10):
            if self.N == 10:
                raise ValueError("use N=5 for order-10 values")
            require(a[1] == 0 and a[2] == a[3], "real_element")
            return Fr(a[0]) - Fr(a[2], 2), -Fr(a[2], 2)
        raise ValueError("real_pair not implemented for this field")


def pair_sign(p: tuple[Fr, Fr]) -> int:
    """Exact sign of A + B sqrt(5)."""
    a, b = p
    if b == 0:
        return (a > 0) - (a < 0)
    if a >= 0 and b >= 0:
        return 1
    if a <= 0 and b <= 0:
        return -1
    if a * a > 5 * b * b:
        return 1 if a > 0 else -1
    return 1 if b > 0 else -1


def padd(p, q):
    return (p[0] + q[0], p[1] + q[1])


def pscale(p, c):
    return (p[0] * c, p[1] * c)


def pfloat(p) -> float:
    return float(p[0]) + float(p[1]) * 5 ** 0.5


# -------------------------------------------------------- Dirichlet characters

class Character:
    def __init__(self, q: int, e: int, table: dict[int, int], label: str):
        self.q, self.e, self.table, self.label = q, e, table, label
        orders = [e // gcd(e, k) for k in table.values()]
        o = 1
        for x in orders:
            o = lcm(o, x)
        self.order = o
        self.fieldN = o if (o % 2 == 1 or o % 4 == 0) else o // 2

    def exp(self, n: int):
        """chi(n) = exp(2 pi i k/e) with k returned, or None if chi(n)=0."""
        return self.table.get(n % self.q) if self.q > 1 else 0

    def value(self, F: Field, n: int):
        k = self.exp(n)
        if k is None:
            return F.zero()
        return root_in_field(F, k, self.e)


def root_in_field(F: Field, k: int, e: int):
    """exp(2 pi i k/e) as an element of F = Q(zeta_N)."""
    n = F.N
    m = n if n % 2 == 0 else 2 * n
    if (k * m) % e:
        raise ValueError("root of unity not in field")
    j = (k * m // e) % m
    if m == n:
        return F.root(j)
    # n odd: zeta_{2n} = -zeta_n^((n+1)/2)
    out = F.root(j * (n + 1) // 2)
    return out if j % 2 == 0 else [-x for x in out]


def all_characters(q: int) -> list[Character]:
    if q == 1:
        return [Character(1, 1, {0: 0}, "chi_1.1")]
    units = [a for a in range(1, q) if gcd(a, q) == 1]

    def order(a):
        k, x = 1, a
        while x != 1:
            x = x * a % q
            k += 1
        return k

    e = 1
    for a in units:
        e = lcm(e, order(a))
    gens, sub = [], {1}
    for a in units:
        if a not in sub:
            gens.append(a)
            frontier = list(sub)
            while frontier:
                x = frontier.pop()
                for g in gens:
                    y = x * g % q
                    if y not in sub:
                        sub.add(y)
                        frontier.append(y)
    chars = []
    for ks in itertools.product(range(e), repeat=len(gens)):
        val, stack, ok = {1: 0}, [1], True
        while stack and ok:
            x = stack.pop()
            for g, k in zip(gens, ks):
                y, kv = x * g % q, (val[x] + k) % e
                if y in val:
                    if val[y] != kv:
                        ok = False
                        break
                else:
                    val[y] = kv
                    stack.append(y)
        if ok and len(val) == len(units):
            for a in units:
                for b in units:
                    require((val[a] + val[b]) % e == val[a * b % q], "character_homomorphism")
            chars.append(val)
    require(len(chars) == len(units), "character_count")
    require(len({tuple(sorted(c.items())) for c in chars}) == len(chars), "character_distinct")
    return [Character(q, e, c, f"chi_{q}.{i}") for i, c in enumerate(chars)]


def conductor(chi: Character) -> int:
    q = chi.q
    for f in divisors(q):
        if all(chi.table[n] == 0 for n in chi.table if n % f == 1 % f):
            return f
    return q


def primitive_characters(qmax: int) -> list[Character]:
    out = []
    for q in range(1, qmax + 1):
        for chi in all_characters(q):
            if conductor(chi) == q:
                out.append(chi)
    return out


# ------------------------------------------------------------- NRC32 mesh

def icbrt(n: int) -> int:
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid ** 3 <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def mesh(b: int) -> list[tuple[int, int]]:
    """NRC32 (4.4), precision 1: h = min(Lambda-a, floor((a^2/b)^(1/3)))."""
    a, stop, blocks = b, b * b, []
    while a < stop:
        h = min(max(1, icbrt(a * a // b)), stop - a)
        require(h >= 1 and h ** 3 * b <= a * a, "mesh_step")
        blocks.append((a, h))
        a += h
    require(a == stop and len(blocks) < 10 * b, "mesh_cover_count")
    return blocks


# ------------------------------------------------------- (C1) twisted panels

def block_energies(F: Field, X: list, blocks, L: int, deep: bool):
    """Exact annular F, coarse S, detail D (as A + B sqrt5 pairs), times L^2."""
    zero = (Fr(0), Fr(0))
    fa, s, d = zero, zero, zero
    for a, h in blocks:
        T = F.zero()
        e1 = zero
        for k in range(a, a + h):
            T = F.add(T, X[k])
            e1 = padd(e1, F.real_pair(F.norm2(X[k])))
        t2 = F.real_pair(F.norm2(T))
        dsum = zero
        for k in range(a, a + h):
            dsum = padd(dsum, F.real_pair(F.norm2(F.sub(F.scale(X[k], h), T))))
        require(pscale(e1, h * h) == padd(pscale(t2, h), dsum), "block_orthogonal_split")
        if deep:
            pairs = zero
            for i in range(a, a + h):
                for j in range(i + 1, a + h):
                    pairs = padd(pairs, F.real_pair(F.norm2(F.sub(X[j], X[i]))))
            require(dsum == pscale(pairs, h), "block_pair_identity")
        # D_I <= h(h^2-1)/(12 a^2):  12 a^2 dsum <= L^2 h^3 (h^2-1)
        diff = (Fr(L * L * h ** 3 * (h * h - 1)) - 12 * a * a * dsum[0], -12 * a * a * dsum[1])
        require(pair_sign(diff) >= 0, "block_detail_budget")
        fa = padd(fa, e1)
        s = padd(s, pscale(t2, Fr(1, h)))
        d = padd(d, pscale(dsum, Fr(1, h * h)))
    return fa, s, d


def twisted_panel(chi: Character, Y: int, mu_sieve: list[int], deep: bool) -> dict:
    F = Field(chi.fieldN)
    b = Y + 1
    end = b * b - 1
    L = lcm_upto(end)
    mu_p = mobius_trial(Y)
    val = [F.zero()] + [chi.value(F, n) for n in range(1, end + 1)]
    # producer: g_chi = mu chi on [1, Y] only
    g = [F.zero()] + [F.scale(val[n], mu_p[n]) for n in range(1, Y + 1)]
    z_chi: dict[int, list] = {}
    z_plain: dict[int, int] = {}
    for r in range(1, Y + 1):
        if not mu_p[r]:
            continue
        for s in range(1, Y + 1):
            if not mu_p[s]:
                continue
            z_chi[r * s] = F.add(z_chi.get(r * s, F.zero()), F.mul(g[r], g[s]))
            z_plain[r * s] = z_plain.get(r * s, 0) + mu_p[r] * mu_p[s]
    for dd, zd in z_chi.items():
        require(zd == F.scale(val[dd], z_plain[dd]), "twist_equivariance_z")
    # v_chi = 2 g_chi - chi * z_chi on [1, end]
    v = [F.zero() for _ in range(end + 1)]
    for r in range(1, Y + 1):
        v[r] = F.add(v[r], F.scale(g[r], 2))
    for dd, zd in z_chi.items():
        if not any(zd):
            continue
        for j in range(1, end // dd + 1):
            cj = val[j]
            if MUTATION == "untwisted_harmonic":
                cj = F.const(1)
            if any(cj):
                v[dd * j] = F.sub(v[dd * j], F.mul(zd, cj))
    for n in range(1, end + 1):
        require(v[n] == F.scale(val[n], mu_sieve[n]), "twisted_newton_coefficient")
        nv = F.real_pair(F.norm2(v[n]))
        require(nv in ((Fr(0), Fr(0)), (Fr(1), Fr(0))), "increment_unimodular")
    # X_k = L m_chi(k), produced from the Newton output v (not from the sieve)
    X = [F.zero()]
    for n in range(1, end + 1):
        X.append(F.add(X[-1], F.scale(v[n], L // n)))
    blocks = mesh(b)
    if deep:
        # twisted harmonic numbers H_chi and character sums C_chi
        LH = [F.zero()]
        C = [F.zero()]
        for j in range(1, end + 1):
            LH.append(F.add(LH[-1], F.scale(val[j], L // j)))
            C.append(F.add(C[-1], val[j]))
        # pointwise adapter: X_k = 2 X_Y - sum_d z_chi(d) L H_chi(floor(k/d))/d
        hd = {}
        for dd in z_chi:
            arr = [F.zero()]
            for j in range(1, end // dd + 1):
                arr.append(F.add(arr[-1], F.scale(val[j], L // (j * dd))))
            hd[dd] = arr
        for k in range(b, end + 1):
            rhs = F.scale(X[Y], 2)
            for dd, zd in z_chi.items():
                if k // dd:
                    rhs = F.sub(rhs, F.mul(zd, hd[dd][k // dd]))
            require(rhs == X[k], "twisted_adapter_pointwise")
        # A^chi_d(t) = sum_{k<t} H_chi(floor(k/d)) = t H_chi(r) - d C_chi(r)
        for dd in range(1, min(Y * Y, 12) + 1):
            acc = F.zero()
            for t in range(1, min(end, 120) + 1):
                acc = F.add(acc, LH[(t - 1) // dd])
                r = (t - 1) // dd
                lin = F.zero() if MUTATION == "drop_character_sum" else F.scale(C[r], dd * L)
                require(acc == F.sub(F.scale(LH[r], t), lin), "twisted_harmonic_primitive")

        def LA(dd, t):  # L A^chi_d(t) / d
            r = (t - 1) // dd
            lin = F.zero() if MUTATION == "drop_character_sum" else F.scale(C[r], L)
            return F.sub(F.scale(hd[dd][r], t), lin)

        for a, h in blocks:
            lhs = F.zero()
            for k in range(a, a + h):
                lhs = F.add(lhs, X[k])
            rhs = F.scale(X[Y], 2 * h)
            for dd, zd in z_chi.items():
                rhs = F.sub(rhs, F.mul(zd, F.sub(LA(dd, a + h), LA(dd, a))))
            require(lhs == rhs, "twisted_block_mean_formula")
    fa, s, d = block_energies(F, X, blocks, L, deep)
    require(fa == padd(s, d), "annular_split_4_1")
    zb = sum((Fr(h * (h * h - 1), 12 * a * a) for a, h in blocks), Fr(0))
    require(zb < Fr(5, 6), "mesh_budget_below_five_sixths")
    dn = pscale(d, Fr(1, L * L))
    require(pair_sign(dn) >= 0 and pair_sign((zb - dn[0], -dn[1])) >= 0, "detail_within_budget")
    require(sum(h for _, h in blocks) == end + 1 - b, "mesh_cover_length")
    # centre invariance: test centres c with L c integral
    m = F.N if F.N % 2 == 0 else 2 * F.N
    centres = [F.const(1), root_in_field(F, 1, m),
               F.scale(F.sub(F.const(1), root_in_field(F, 1, m)), Fr(1, 2))]
    for c in centres:
        Lc = [x * L for x in c]
        require(all(Fr(x).denominator == 1 for x in Lc), "centre_integral")
        Lc = [int(x) for x in Lc]
        Xc = [F.sub(x, Lc) for x in X]
        fac, sc, dc = block_energies(F, Xc, blocks, L, False)
        require(dc == d, "centred_detail_invariant")
        require(fac == padd(sc, dc), "centred_annular_split")
    fy = (Fr(0), Fr(0))
    for k in range(1, Y + 1):
        fy = padd(fy, F.real_pair(F.norm2(X[k])))
    sc = lambda p: pscale(p, Fr(1, L * L))
    return {"chi": chi.label, "q": chi.q, "order": chi.order, "Y": Y,
            "blocks": len(blocks), "deep": deep,
            "F_Y_uncentred": pfloat(sc(fy)), "annular_F": pfloat(sc(fa)),
            "coarse_S": pfloat(sc(s)), "detail_D": pfloat(dn), "Z_budget": float(zb)}


# ------------------------------------------------------------- (C2) checks

def harmonic(n: int) -> list[Fr]:
    h = [Fr(0)]
    for j in range(1, n + 1):
        h.append(h[-1] + Fr(1, j))
    return h


def ramanujan_vs(q: int, n: int, mu: list[int]) -> int:
    """von Sterneck: c_q(n) = sum_{e | (q,n)} e mu(q/e)."""
    return sum(e * mu[q // e] for e in divisors(gcd(q, n)))


def c2_checks(mu: list[int]) -> dict:
    out = {}
    # (a) zero-class form of the coarse kernel
    for Y in (2, 3, 5, 7):
        b = Y + 1
        hs = harmonic(b * b)
        for a, h in mesh(b):
            for d in range(1, Y * Y + 1):
                lhs = sum((hs[k // d] for k in range(a, a + h)), Fr(0))
                rhs = sum((Fr(d, n) * (a + h - max(n, a))
                           for n in range(d, a + h, d)), Fr(0))
                require(lhs == rhs, "kernel_zero_class")
    # (a') Phi_I(d) = kappa_I(d)/d strictly decreasing on [1, a+h-1], zero beyond;
    #      hence r -> K_I(r,s) = Phi_I(rs) is not q-periodic on [1,Y] for q <= Y-1
    for Y in range(2, 16):
        b = Y + 1
        hs = harmonic(b * b)
        for a, h in mesh(b):
            phi = [None] + [sum((hs[k // d] for k in range(a, a + h)), Fr(0)) / (h * d)
                            for d in range(1, Y * Y + 1)]
            if MUTATION == "flat_kernel":
                phi = [None] + [Fr(1)] * (Y * Y)
            for d in range(1, Y * Y):
                if d + 1 <= a + h - 1:
                    require(phi[d + 1] < phi[d], "kernel_strictly_decreasing")
                else:
                    require(phi[d + 1] == 0, "kernel_zero_beyond_block")
            for s in range(1, Y + 1):
                for q in range(1, Y):
                    require(phi[s] > phi[(1 + q) * s], "kernel_not_q_periodic")
    # (b) Ramanujan sums: cyclotomic definition = von Sterneck = Hoelder
    for q in range(1, 25):
        F = Field(q)
        for n in range(0, 2 * q + 1):
            c = F.zero()
            for a in range(1, q + 1):
                if gcd(a, q) == 1:
                    c = F.add(c, F.root(a * n))
            vs = ramanujan_vs(q, n, mu) if n else totient(q)
            require(c == F.const(vs), "ramanujan_cyclotomic")
    for q in range(1, 61):
        for n in range(1, 121):
            g = gcd(n, q)
            hold = Fr(mu[q // g] * totient(q), totient(q // g))
            require(ramanujan_vs(q, n, mu) == hold, "ramanujan_hoelder")
    for q in range(1, 25):
        for n in range(1, 49):
            for u in range(1, q + 1):
                if gcd(u, q) == 1:
                    require(ramanujan_vs(q, u * n, mu) == ramanujan_vs(q, n, mu),
                            "ramanujan_unit_invariant")
    # principal-only: sum_u chi(u) c_q(u n) = 0 for nonprincipal chi mod q
    for q in range(2, 13):
        for chi in all_characters(q):
            if all(k == 0 for k in chi.table.values()):
                continue
            F = Field(chi.fieldN)
            for n in range(1, 2 * q + 1):
                acc = F.zero()
                for u in chi.table:
                    acc = F.add(acc, F.scale(chi.value(F, u), ramanujan_vs(q, u * n, mu)))
                require(acc == F.zero(), "ramanujan_principal_only")
    # (b') H_floor(k/d) = sum_{q|d} sum_{n<=k} c_q(n)/n
    hs = harmonic(121)
    for d in range(1, 41):
        R = {q: [Fr(0)] for q in divisors(d)}
        for n in range(1, 121):
            for q in R:
                R[q].append(R[q][-1] + Fr(ramanujan_vs(q, n, mu), n))
        for k in range(1, 121):
            require(hs[k // d] == sum((R[q][k] for q in R), Fr(0)), "ramanujan_floor_expansion")
    # twisted: for (d,q_chi)=1, H_chi(floor(k/d)) = conj chi(d) sum_{e|d} sum_{n<=k} c_e(n) chi(n)/n
    for chi in primitive_characters(12):
        F = Field(chi.fieldN)
        Hc = [F.zero()]
        for j in range(1, 151):
            Hc.append(F.add(Hc[-1], F.scale(chi.value(F, j), Fr(1, j))))
        Rc = {}
        for e in range(1, 31):
            arr = [F.zero()]
            for n in range(1, 151):
                c = ramanujan_vs(e, n, mu)
                arr.append(F.add(arr[-1], F.scale(chi.value(F, n), Fr(c, n))) if c else arr[-1])
            Rc[e] = arr
        for d in range(1, 31):
            if chi.exp(d) is None:
                continue
            cd = F.conj(chi.value(F, d))
            for k in range(1, 151):
                acc = F.zero()
                for e in divisors(d):
                    acc = F.add(acc, Rc[e][k])
                require(F.mul(cd, acc) == Hc[k // d], "twisted_ramanujan_floor")
    # (c) separated form m(k) = 2m(Y) - sum_q R_q(k) Z_q, Z_q via principal characters
    for Y in (2, 3, 4, 5, 6, 7):
        b = Y + 1
        end = b * b - 1
        m = [Fr(0)]
        for n in range(1, end + 1):
            m.append(m[-1] + Fr(mu[n], n))
        z = {}
        for r in range(1, Y + 1):
            for s in range(1, Y + 1):
                if mu[r] and mu[s]:
                    z[r * s] = z.get(r * s, 0) + mu[r] * mu[s]
        Zq = {q: sum((Fr(zd, dd) for dd, zd in z.items() if dd % q == 0), Fr(0))
              for q in range(1, Y * Y + 1)}
        for q, zq in Zq.items():
            alt = Fr(0)
            for r in range(1, Y + 1):
                if not mu[r]:
                    continue
                e = q // gcd(q, r)
                if not mu[e]:
                    continue
                mp = sum((Fr(mu[t], t) for t in range(1, Y // e + 1) if gcd(t, e) == 1), Fr(0))
                if MUTATION == "drop_principal_euler":
                    mp = m[Y // e]
                alt += Fr(mu[r], r) * Fr(mu[e], e) * mp
            require(alt == zq, "separated_Z_principal_characters")
        R = {q: [Fr(0)] for q in Zq}
        for n in range(1, end + 1):
            for q in R:
                R[q].append(R[q][-1] + Fr(ramanujan_vs(q, n, mu), n))
        for k in range(b, end + 1):
            rhs = 2 * m[Y] - sum((R[q][k] * Zq[q] for q in Zq), Fr(0))
            require(rhs == m[k], "separated_form_ramanujan")
    # (c') twisted separated form: m_chi(k) = 2 m_chi(Y) - sum_e R^chi_e(k) Z^(q)_e with
    #      R^chi_e(k) = sum_{n<=k} c_e(n) chi(n)/n and the UNTWISTED, principal-mod-q
    #      arithmetic side Z^(q)_e = sum_{e|d, (d,q)=1} z(d)/d.
    for chi in primitive_characters(12):
        F = Field(chi.fieldN)
        for Y in (2, 3, 4, 5):
            b = Y + 1
            end = b * b - 1
            mc = [F.zero()]
            for n in range(1, end + 1):
                mc.append(F.add(mc[-1], F.scale(chi.value(F, n), Fr(mu[n], n))))
            z = {}
            for r in range(1, Y + 1):
                for s in range(1, Y + 1):
                    if mu[r] and mu[s]:
                        z[r * s] = z.get(r * s, 0) + mu[r] * mu[s]
            Zq = {e: sum((Fr(zd, dd) for dd, zd in z.items()
                          if dd % e == 0 and chi.exp(dd) is not None), Fr(0))
                  for e in range(1, Y * Y + 1)}
            for k in range(b, end + 1):
                rhs = F.scale(mc[Y], 2)
                for e, ze in Zq.items():
                    if ze:
                        acc = F.zero()
                        for n in range(1, k + 1):
                            c = ramanujan_vs(e, n, mu)
                            if c:
                                acc = F.add(acc, F.scale(chi.value(F, n), Fr(c, n)))
                        rhs = F.sub(rhs, F.scale(acc, ze))
                require(rhs == mc[k], "twisted_separated_form")
    # (d) Euler-factor transfer: m_{chi0,e}(k) = sum_{u | e^inf} m(floor(k/u))/u
    K = 300
    m = [Fr(0)]
    for n in range(1, K + 1):
        m.append(m[-1] + Fr(mu[n], n))
    worst = 0.0
    for e in range(1, 31):
        ps = prime_factors(e)
        smooth = [u for u in range(1, K + 1) if all(p in ps for p in prime_factors(u))]
        me = [Fr(0)]
        for n in range(1, K + 1):
            me.append(me[-1] + (Fr(mu[n], n) if gcd(n, e) == 1 else 0))
        for k in range(1, K + 1):
            require(me[k] == sum((m[k // u] / u for u in smooth if u <= k), Fr(0)),
                    "euler_transfer_identity")
        # float sanity of F_Y(chi0,e) <= prod_{p|e}(1-p^-1/2)^-2 F_Y (proved, not acceptance)
        fe = float(sum((x * x for x in me[1:]), Fr(0)))
        f0 = float(sum((x * x for x in m[1:]), Fr(0)))
        bound = f0
        for p in ps:
            bound /= (1 - p ** -0.5) ** 2
        worst = max(worst, fe / bound)
    out["euler_transfer_max_ratio_float"] = worst
    # (e) reciprocity  s sbar + r rbar == 1 mod rs
    for r in range(1, 61):
        for s in range(1, 61):
            if gcd(r, s) == 1:
                sb = pow(s, -1, r) if r > 1 else 0
                rb = pow(r, -1, s) if s > 1 else 0
                require((s * sb + r * rb) % (r * s) == 1 % (r * s), "additive_reciprocity")
    # (f) Gauss expansion  phi(r) e(y/r) = sum_chi tau(chi) conj chi(y), and |tau|^2 = conductor
    for r in range(1, 16):
        chars = all_characters(r)
        e = chars[0].e
        F = Field(lcm(r, e))
        N = F.N
        taus = []
        for chi in chars:
            tau = F.zero()
            for a in (chi.table if r > 1 else {0: 0}):
                tau = F.add(tau, F.mul(F.root(chi.table[a] * N // e), F.root(a * N // r)))
            taus.append(tau)
            sqfree = all(r % (p * p) for p in prime_factors(r))
            if sqfree:
                require(F.norm2(tau) == F.const(conductor(chi)), "gauss_norm_conductor")
        if r <= 12:
            for y in (chars[0].table if r > 1 else {0: 0}):
                acc = F.zero()
                for chi, tau in zip(chars, taus):
                    acc = F.add(acc, F.mul(tau, F.root(-chi.table[y] * N // e)))
                require(acc == F.scale(F.root(y * N // r), totient(r)), "gauss_expansion")
    # (g) Parseval of the coarse split over all characters mod q
    for q in (3, 4, 5, 7, 8, 9, 12):
        chars = all_characters(q)
        fieldN = chars[0].e if (chars[0].e % 2 == 1 or chars[0].e % 4 == 0) else chars[0].e // 2
        F = Field(fieldN)
        for Y in (3, 5):
            b = Y + 1
            end = b * b - 1
            L = lcm_upto(end)
            blocks = mesh(b)
            tot_s = (Fr(0), Fr(0))
            tot_d = (Fr(0), Fr(0))
            for chi in chars:
                X = [F.zero()]
                for n in range(1, end + 1):
                    X.append(F.add(X[-1], F.scale(root_in_field(F, chi.exp(n), chi.e)
                                                  if chi.exp(n) is not None else F.zero(),
                                                  mu[n] * (L // n))))
                _, s, d = block_energies(F, X, blocks, L, False)
                tot_s, tot_d = padd(tot_s, s), padd(tot_d, d)
            ap_s = ap_d = Fr(0)
            for a in chars[0].table:
                X = [0]
                for n in range(1, end + 1):
                    X.append(X[-1] + (mu[n] * (L // n) if n % q == a else 0))
                Fq = Field(1)
                _, s, d = block_energies(Fq, [[x] for x in X], blocks, L, False)
                ap_s += s[0]
                ap_d += d[0]
            require(tot_s == (ap_s * totient(q), Fr(0)), "parseval_coarse_S")
            require(tot_d == (ap_d * totient(q), Fr(0)), "parseval_detail_D")
    return out


# ------------------------------------------------------------------ driver

def build(quick: bool) -> dict:
    COUNTS.clear()
    prims = primitive_characters(12)
    require(len(prims) == 27, "primitive_count_27")
    ys = (1, 2, 3, 4, 5, 7) if quick else tuple(range(1, 17)) + (20, 24, 31)
    deep_max = 5 if quick else 8
    nmax = (max(ys) + 1) ** 2
    mu = mobius_sieve(max(nmax, 400))
    panels = []
    for chi in prims:
        for Y in ys:
            panels.append(twisted_panel(chi, Y, mu, Y <= deep_max))
    extra = c2_checks(mu)
    return {"packet": "NRC32_TWISTS (exploratory)",
            "status": "finite exact checks; no asymptotic claim",
            "primitive_characters": [(c.label, c.q, c.order, c.fieldN) for c in prims],
            "Y_panel": list(ys), "deep_max_Y": deep_max, "quick": quick,
            "counts": dict(sorted(COUNTS.items())), "c2_extra": extra,
            "panels": panels}


def main() -> None:
    global MUTATION
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--write")
    ap.add_argument("--mutation", default="none",
                    choices=("none", "flip_prefix_mobius", "untwisted_harmonic",
                             "drop_character_sum", "drop_principal_euler",
                             "flat_kernel"))
    args = ap.parse_args()
    MUTATION = args.mutation
    rep = build(args.quick)
    text = json.dumps(rep, sort_keys=True, indent=1) + "\n"
    if args.write:
        with open(args.write, "w") as fh:
            fh.write(text)
    print(json.dumps({"status": "PASS", "mutation": MUTATION,
                      "sha256": hashlib.sha256(text.encode()).hexdigest(),
                      "counts": rep["counts"]}, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        sys.exit(1)
