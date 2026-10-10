#!/usr/bin/env python3
"""High-precision (mpmath, 40 dps) verification of the Corollary-C anchor
M_sc(1e6) and of full margins at x = 1e4 (independent of all float64 paths)."""
import mpmath as mp
from itertools import combinations
import common as C

mp.mp.dps = 40
PR = C.PRIMES


def divisors_upto(xlim):
    out = [(1, 1)]
    for p in PR:
        new = []
        for (v, mu) in out:
            w = v * p
            if w <= xlim:
                new.append((w, -mu))
        out += new
    out.sort()
    return out


def msc_hp(x_int):
    divs = divisors_upto(x_int)
    x = mp.mpf(x_int)
    D = mp.mpf(0)
    ev = []
    for (v, mu) in divs:
        T = (4 * mp.sqrt(x / v) - 3) / mp.sqrt(v)
        if mu == -1:
            D += T
        else:
            ev.append((v, T))
    So = mp.fsum(1 / mp.sqrt(mp.mpf(v)) for (v, mu) in divs if mu == -1)
    rem = D
    Se_used = mp.mpf(0)
    kstar = None
    for (v, T) in ev:
        take = min(T, rem)
        Se_used += (take / T) / mp.sqrt(mp.mpf(v))
        rem -= take
        if rem <= 0:
            kstar = v
            break
    assert rem <= 0, "fill incomplete?!"
    return mp.mpf(3) / 4 * (So - Se_used), kstar


def margins_hp(x_int):
    """Full margins incl. M_j by direct Q sums (small x only)."""
    divs = divisors_upto(x_int)
    x = mp.mpf(x_int)

    def Q(Y, j):
        M = int(mp.floor(Y))
        if M < j:
            return mp.mpf(0)
        tot = mp.mpf(0)
        for m in range(j, M + 1):
            if m == j:
                g = mp.mpf(j + 1) / (j - 1)
            elif m == j + 1:
                g = -mp.mpf((j + 1) * (j - 2)) / (j * (j - 1))
            else:
                g = mp.mpf(2) / (j * (j - 1))
            tot += g / mp.sqrt(mp.mpf(m)) * mp.log(Y / m)
        return tot

    D = mp.mpf(0); ev = []; odd = []
    for (v, mu) in divs:
        T = (4 * mp.sqrt(x / v) - 3) / mp.sqrt(v)
        if mu == -1:
            D += T; odd.append(v)
        else:
            ev.append((v, T))
    res = {}
    for j in (2, 3):
        qo = mp.fsum(Q(x / v, j) / mp.sqrt(mp.mpf(v)) for v in odd)
        rem = D; qe = mp.mpf(0)
        for (v, T) in ev:
            take = min(T, rem)
            qe += (take / T) * Q(x / v, j) / mp.sqrt(mp.mpf(v))
            rem -= take
            if rem <= 0:
                break
        res[f"M{j}"] = qe - qo
    res["M_sc"] = msc_hp(x_int)[0]
    return res


if __name__ == "__main__":
    v, ks = msc_hp(10**6)
    f = C.eval_point(1e6)
    print(f"HP  M_sc(1e6) = {mp.nstr(v, 20)}   (e* = {ks})")
    print(f"f64 M_sc(1e6) = {f['M_sc']:.15f} +- {f['eps_sc']:.2e}")
    print(f"|diff| = {mp.nstr(abs(v - mp.mpf(f['M_sc'])), 5)}  "
          f"within budget: {abs(v - mp.mpf(f['M_sc'])) < mp.mpf(f['eps_sc'])}")
    m = margins_hp(10**4)
    f4 = C.eval_point(1e4)
    for k in ("M2", "M3", "M_sc"):
        hp = m[k]
        print(f"x=1e4 {k}: HP={mp.nstr(hp, 18)} f64={f4[k]!r} "
              f"diff={mp.nstr(abs(hp - mp.mpf(f4[k])), 4)}")
