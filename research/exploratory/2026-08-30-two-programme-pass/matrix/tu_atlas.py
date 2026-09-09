"""C2 continuation — the TWO-PARAMETER deformation plane of 11a1:

    Z_{t,u}(s) = prod_{p != 11} (1 - t a_p p^{-s} + u p^{1-2s})^{-1},

the (t, u)-atlas over L-108511's trace-scaling line (= the u = 1
slice). Exact machine layer for L-108516. All arithmetic is integer /
Fraction / polynomial-in-(t,u) exact; standard library only.

Checks:
  M1  WEIGHTED HOMOGENEITY of every Dirichlet coefficient: b_n(t, u)
      is weighted-homogeneous of degree Omega(n) with wt(t) = 1,
      wt(u) = 2, for every good-support n <= 20000 (this single fact
      proves the fibration lemma, the Liouville parity lemma, and the
      parabola lemma of L-108516 at the coefficient level); plus
      b_n(1,1) = a_n (multiplicative reconstruction matches the
      point-count table on prime powers <= 20000).
  M2  DAHLQUIST AXIS (t = 0): Z_{0,u} * zeta_u^(11)(2s-1) ==
      zeta_{u^2}^(11)(4s-2) coefficientwise in Z[u] on all good n <=
      20000, where zeta_u(s) := prod (1 - u p^{-s})^{-1} =
      sum u^{Omega(n)} n^{-s} (the Dahlquist family).
  M3  THE POINT (0, -1): b_n(0,-1) = m if n = m^2 (11-coprime m),
      else 0 — i.e. Z_{0,-1} = zeta^(11)(2s-1) exactly, n <= 20000.
  M4  PURITY WEDGE, exact scan on all 9591 good primes p <= 1e5:
      local purity (equal root moduli) at (t, u) <=> t^2 a_p^2 <= 4 u p
      OR t a_p = 0. Grid over t in {0, +-1/2, +-1, +-3/2, +-2},
      u in {-1, 1/4, 1/2, 1, 9/4, 4}: expect ZERO impure primes
      exactly when u >= t^2 or t = 0, and count + first witness
      otherwise.
  M5  INTEGRALITY witnesses: first non-integral coefficient at
      (1/2, 1) and (1, 1/2) (the lemma proves the locus is exactly
      Z^2; a_5 = 1, a_2 = -2, a_3 = -1 drive the argument).

rh_established = false.
"""
import json
import time
from fractions import Fraction as Fr

HERE = 'matrix'
AP = {int(k): v for k, v in json.load(
    open(f'{HERE}/ap_table_11a1.json'))['a_p'].items()}
N_MAX = 20000
PRIMES = sorted(AP)


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---- polynomials in (t, u): dict {(i, j): int} ----------------------

def pmul_scal(P, c):
    return {k: v * c for k, v in P.items() if v * c != 0}


def pshift(P, di, dj):
    return {(i + di, j + dj): v for (i, j), v in P.items()}


def padd(P, Q):
    R = dict(P)
    for k, v in Q.items():
        w = R.get(k, 0) + v
        if w:
            R[k] = w
        else:
            R.pop(k, None)
    return R


def pmul(P, Q):
    R = {}
    for (i1, j1), v1 in P.items():
        for (i2, j2), v2 in Q.items():
            k = (i1 + i2, j1 + j2)
            w = R.get(k, 0) + v1 * v2
            if w:
                R[k] = w
            else:
                R.pop(k, None)
    return R


def peval(P, tv, uv):
    return sum(v * tv ** i * uv ** j for (i, j), v in P.items())


ONE = {(0, 0): 1}


def h_polys(p, kmax):
    """H_k(t, u) at prime p: H_k = t a_p H_{k-1} - u p H_{k-2}."""
    H = [dict(ONE), {(1, 0): AP[p]} if AP[p] else {}]
    for _ in range(2, kmax + 1):
        H.append(padd(pmul_scal(pshift(H[-1], 1, 0), AP[p]),
                      pmul_scal(pshift(H[-2], 0, 1), -p)))
    return H


def build_bn(nmax):
    """b_n(t,u) polys for all 11-coprime n <= nmax, plus Omega(n)."""
    spf = list(range(nmax + 1))
    for p in range(2, int(nmax ** 0.5) + 1):
        if spf[p] == p:
            for q in range(p * p, nmax + 1, p):
                if spf[q] == q:
                    spf[q] = p
    Hcache = {}
    b = {1: dict(ONE)}
    om = {1: 0}
    for n in range(2, nmax + 1):
        if n % 11 == 0:
            continue
        p = spf[n]
        k, m = 0, n
        while m % p == 0:
            m //= p
            k += 1
        if m % 11 == 0:
            continue
        if p not in Hcache:
            kmax = 1
            while p ** (kmax + 1) <= nmax:
                kmax += 1
            Hcache[p] = h_polys(p, kmax)
        b[n] = pmul(b[m], Hcache[p][k])
        om[n] = om[m] + k
    return b, om


def main():
    out = {"experiment": "tu_atlas (L-108516 machine layer)",
           "rh_established": False, "checks": {}}
    say("building b_n(t,u) polynomials to n = 20000 ...")
    b, om = build_bn(N_MAX)
    say(f"built {len(b)} coefficients")

    # M1 — weighted homogeneity + b_n(1,1) = a_n on prime powers
    homog_bad = [n for n, P in b.items()
                 if any(i + 2 * j != om[n] for (i, j) in P)]
    ppow_bad = []
    # Hecke reconstruction (u = t = 1 must equal the classical a_{p^k}):
    for p in PRIMES:
        if p > N_MAX:
            break
        a_prev, a_cur = 1, AP[p]
        pk = p
        k = 1
        while pk <= N_MAX:
            if peval(b[pk], 1, 1) != a_cur:
                ppow_bad.append(pk)
            a_prev, a_cur = a_cur, AP[p] * a_cur - p * a_prev
            pk *= p
            k += 1
    m1 = not homog_bad and not ppow_bad
    out["checks"]["M1_homogeneity_and_point11"] = {
        "ok": m1, "n_checked": len(b), "homog_bad": homog_bad[:5],
        "prime_power_bad": ppow_bad[:5]}
    say(f"M1 homogeneity + b(1,1)=a_n: {m1}")

    # M2 — Dahlquist axis: Z_{0,u} * zeta_u(2s-1) == zeta_{u^2}(4s-2)
    # zeta_u(2s-1) coefficients: at n = m^2 (11-coprime): u^Omega(m)*m
    # zeta_{u^2}(4s-2):          at n = m^4: u^{2 Omega(m)} * m^2
    say("M2 Dahlquist-axis convolution ...")
    lhs_bad = []
    zu = {}
    for m in range(1, int(N_MAX ** 0.5) + 1):
        if m % 11 == 0 or m * m > N_MAX:
            continue
        if m * m in b or m == 1:
            zu[m * m] = {(0, om.get(m, 0)): m} if m > 1 else dict(ONE)
    zu_keys = sorted(zu)
    for n in list(b):
        # conv_{d e = n} b_d(0,u) * zu_e   vs  rhs_n
        acc = {}
        for e in zu_keys:
            if e > n:
                break
            if n % e:
                continue
            d = n // e
            if d not in b:
                continue
            # b_d at t = 0: keep only monomials with i = 0
            P0 = {(0, j): v for (i, j), v in b[d].items() if i == 0}
            if P0:
                acc = padd(acc, pmul(P0, zu[e]))
        r = int(round(n ** 0.25))
        rhs = {}
        for m4 in (r - 1, r, r + 1):
            if m4 >= 1 and m4 ** 4 == n and m4 % 11 != 0:
                rhs = {(0, 2 * om.get(m4, 0)): m4 * m4} if m4 > 1 \
                    else dict(ONE)
        if acc != rhs:
            lhs_bad.append(n)
    m2 = not lhs_bad
    out["checks"]["M2_dahlquist_axis"] = {"ok": m2,
                                          "bad_n": lhs_bad[:5]}
    say(f"M2 Dahlquist axis identity: {m2}")

    # M3 — the point (0, -1) is zeta(2s-1)
    m3_bad = []
    for n, P in b.items():
        v = peval(P, 0, -1)
        r = int(round(n ** 0.5))
        expect = r if r * r == n and r % 11 != 0 else 0
        if v != expect:
            m3_bad.append((n, v, expect))
    m3 = not m3_bad
    out["checks"]["M3_point_0_minus1_is_zeta"] = {"ok": m3,
                                                  "bad": m3_bad[:5]}
    say(f"M3 (0,-1) = zeta(2s-1): {m3}")

    # M4 — purity wedge exact scan
    say("M4 purity wedge scan on 9591 primes ...")
    grid_t = [Fr(0), Fr(1, 2), Fr(-1, 2), Fr(1), Fr(-1),
              Fr(3, 2), Fr(-3, 2), Fr(2), Fr(-2)]
    grid_u = [Fr(-1), Fr(1, 4), Fr(1, 2), Fr(1), Fr(9, 4), Fr(4)]
    wedge = []
    m4 = True
    for t in grid_t:
        for u in grid_u:
            cnt = 0
            first = None
            for p in PRIMES:
                a = AP[p]
                pure = (t * a == 0) or (t * t * a * a <= 4 * u * p)
                if not pure:
                    cnt += 1
                    if first is None:
                        first = p
            inside = (u >= t * t) or (t == 0)
            expect_zero = inside
            ok = (cnt == 0) == expect_zero
            m4 = m4 and ok
            wedge.append({"t": str(t), "u": str(u),
                          "impure_primes": cnt, "first": first,
                          "inside_wedge": inside, "ok": ok})
    out["checks"]["M4_purity_wedge"] = {"ok": m4, "grid": wedge}
    say(f"M4 purity wedge (0 impure iff u >= t^2 or t = 0): {m4}")

    # M5 — integrality witnesses
    w1 = peval(b[5], Fr(1, 2), Fr(1))          # = a_5/2 = 1/2
    w2 = peval(b[9], Fr(1), Fr(1, 2))          # = a_3^2 - 3u = -1/2
    m5 = (w1 == Fr(1, 2) and w1.denominator != 1 and
          w2 == Fr(-1, 2) and w2.denominator != 1)
    out["checks"]["M5_integrality_witnesses"] = {
        "ok": m5, "b_5(1/2,1)": str(w1), "b_9(1,1/2)": str(w2)}
    say(f"M5 integrality witnesses: {m5}")

    allok = all(c["ok"] for c in out["checks"].values())
    out["all_ok"] = allok
    json.dump(out, open(f'{HERE}/tu_atlas.json', 'w'), indent=1)
    say("ALL OK" if allok else "FAILURES PRESENT")


if __name__ == "__main__":
    main()
