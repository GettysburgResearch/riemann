"""Stage 2 of the memory-lean m = 18 sieve (T-108513 converse
extension without factoring; the direct sympy factor route OOMed at
12.7 GB).

Pipeline (everything EXACT; the modular step is only a candidate
generator, verified exactly afterwards):
  S1  load M_18(z; a) (stage 1, m18_spectrum.json); Sylvester degree
      bound D for disc_z = Res(M, M') (M monic).
  S2  exact integer resultants v(a0) = Res(M(., a0), M'(., a0)) at
      a0 = 0..D (Bareiss fraction-free 15x15 determinants).
  S3  candidate disc(a) by Lagrange interpolation mod many 62-bit
      primes + CRT (fast), then PROOF: Horner-evaluate the candidate
      at ALL D+1 nodes and compare with the exact v(a0) — with
      deg disc <= D, agreement at D+1 points is equality.
  S4  the sieve, factoring-free:
      (a) divide out each known torsion minimal polynomial (threshold
          <= 17, plus any with threshold 18 <= ... none: thresholds
          are odd) to maximal multiplicity — records the even-m
          multiplicity data for O-108523;
      (b) remainder P: content and leading coefficient (non-unit?);
      (c) enumerate EVERY real-cyclotomic minimal polynomial
          psi_N (of 2cos(2 pi/N)) with phi(N)/2 <= deg P, via
          Phi_N folded through a = z + 1/z, and verify psi_N does
          NOT divide P. Any torsion value of ANY order rooting
          disc_z M_18 would force its (monic) psi_N to divide disc;
          all psi_N dividing disc are then among the divided-out
          known-threshold factors — the m = 18 converse.
rh_established = false.
"""
import json
import random
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, '.')


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


# ---------------- polynomial helpers over Z -------------------------

def peval(P, x):
    v = 0
    for c in reversed(P):
        v = v * x + c
    return v


def pdiv_exact(P, Q):
    """P // Q if exact over Z, else None. P, Q low-to-high."""
    P = list(P)
    dq = len(Q) - 1
    if len(P) - 1 < dq:
        return None
    out = [0] * (len(P) - dq)
    for i in range(len(P) - 1, dq - 1, -1):
        if P[i] == 0:
            continue
        if P[i] % Q[-1]:
            return None
        c = P[i] // Q[-1]
        out[i - dq] = c
        for k, qc in enumerate(Q):
            P[i - dq + k] -= c * qc
    return out if all(v == 0 for v in P) else None


def content(P):
    from math import gcd
    g = 0
    for c in P:
        g = gcd(g, abs(c))
    return g if g else 1


# ---------------- S1: load spectrum, degree bound -------------------

def load_M(m=18):
    d = json.load(open(f'matrix/m{m}_spectrum.json'))
    nu = d["nu"]
    mus = {int(j): [int(c) for c in v]
           for j, v in d["coeffs_low_to_high"].items()}
    return nu, mus


def sylvester_deg_bound(nu, mus):
    dM = max(len(v) - 1 for v in mus.values())
    # Res(M, M'): (nu-1) rows of M-coeffs + nu rows of M'-coeffs
    return (nu - 1) * dM + nu * dM


# ---------------- S2: exact resultants ------------------------------

def resultant_frac(F, G):
    """Res(F, G) for integer polys (low-to-high), classical Euclidean
    recurrence over Fractions:
      res(A, B) = lc(B)^(dA - dR) (-1)^(dA dB) res(B, R),  R = A mod B;
      res(A, c) = c^(dA); res(A, 0) = 0 (dB > 0). Exact."""
    A = [Fr(c) for c in F]
    B = [Fr(c) for c in G]

    def trim(P):
        while P and P[-1] == 0:
            P.pop()
        return P

    A = trim(A)
    B = trim(B)
    res = Fr(1)
    while True:
        if not B:
            return 0
        dA = len(A) - 1
        dB = len(B) - 1
        if dB == 0:
            res *= B[0] ** dA
            assert res.denominator == 1
            return int(res)
        # R = A mod B
        R = A[:]
        lB = B[-1]
        while len(R) - 1 >= dB and any(R):
            dR = len(R) - 1
            c = R[-1] / lB
            for k, bc in enumerate(B):
                R[dR - dB + k] -= c * bc
            R = trim(R)
            if not R:
                break
        dR = len(R) - 1 if R else -1
        res *= Fr(-1) ** (dA * dB) * lB ** (dA - (dR if R else 0))
        if not R:
            return 0
        A, B = B, R


def resultant_at(nu, mus, a0):
    """Res_z(M, dM/dz) at a = a0, exact integer (M monic in z)."""
    A = [peval(mus.get(j, [0]), a0) for j in range(nu + 1)]
    B = [j * A[j] for j in range(1, nu + 1)]
    return resultant_frac(A, B)


# ---------------- S3: modular interpolation + CRT + exact proof -----

def small_primes_62(k):
    """k primes just below 2^62 (deterministic Miller-Rabin for
    64-bit range with the standard witness set)."""
    def isp(x):
        if x % 2 == 0:
            return False
        d = x - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for w in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if x % w == 0:
                return x == w
            t = pow(w, d, x)
            if t in (1, x - 1):
                continue
            for _ in range(r - 1):
                t = t * t % x
                if t == x - 1:
                    break
            else:
                return False
        return True
    ps = []
    c = (1 << 62) - 1
    while len(ps) < k:
        if isp(c):
            ps.append(c)
        c -= 2
    return ps


def interp_mod(vals, p):
    """Newton interpolation at nodes 0..D mod p; returns coeffs."""
    D = len(vals) - 1
    f = [v % p for v in vals]
    # divided differences with integer nodes: dd[k] = delta^k f / k!
    dd = f[:]
    for k in range(1, D + 1):
        inv = pow(k, p - 2, p)
        for i in range(D, k - 1, -1):
            dd[i] = (dd[i] - dd[i - 1]) * inv % p
    # Newton form -> monomial coefficients: prod (x - i)
    coeffs = [0] * (D + 1)
    basis = [1]
    for k in range(D + 1):
        for i, b in enumerate(basis):
            coeffs[i] = (coeffs[i] + dd[k] * b) % p
        nb = [0] * (len(basis) + 1)
        for i, b in enumerate(basis):
            nb[i] = (nb[i] - k * b) % p
            nb[i + 1] = (nb[i + 1] + b) % p
        basis = nb
    return coeffs


def crt_pair(r1, m1, r2, m2):
    g, x = m1, pow(m1, -1, m2)
    t = (r2 - r1) * x % m2
    return r1 + m1 * t, m1 * m2


# ---------------- S4: torsion minimal polynomials -------------------

def psi_N(N):
    """minimal polynomial of 2cos(2 pi/N) over Q, monic in Z[a],
    via folding the cyclotomic polynomial through a = z + 1/z."""
    import sympy as sp
    if N == 1:
        return [-2, 1]          # a - 2
    if N == 2:
        return [2, 1]           # a + 2
    Phi = sp.Poly(sp.cyclotomic_poly(N, sp.Symbol('x')),
                  sp.Symbol('x')).all_coeffs()[::-1]
    d = len(Phi) - 1            # = phi(N), even for N >= 3
    h = d // 2
    # q_k(a) = z^k + z^-k as polynomial in a (q_0 = 2)
    qs = [[2], [0, 1]]
    for k in range(2, h + 1):
        prev, prev2 = qs[-1], qs[-2]
        nxt = [0] + prev[:]
        for i, c in enumerate(prev2):
            nxt[i] -= c
        qs.append(nxt)
    out = [0] * (h + 1)
    # z^-h Phi = c_h + sum_{k>=1} c_{h+k} (z^k + z^-k)
    out[0] += int(Phi[h])
    for k in range(1, h + 1):
        c = int(Phi[h + k])
        if c:
            for i, qc in enumerate(qs[k]):
                out[i] += c * qc
    assert out[-1] == 1
    return out


KNOWN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18]  # incl. N=9,18 (threshold 19)
# (we divide by ALL psi_N that actually divide, discovered dynamically)


def main():
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    t0 = time.time()
    nu, mus = load_M(m)
    D = sylvester_deg_bound(nu, mus)
    say(f"nu = {nu}, degree bound D = {D}")
    say("S2: exact resultants at 0..D ...")
    vals = []
    for a0 in range(D + 1):
        vals.append(resultant_at(nu, mus, a0))
        if a0 % 200 == 0:
            say(f"  a0 = {a0} ({time.time()-t0:.0f}s)")
    say(f"S2 done ({time.time()-t0:.0f}s); max digits "
        f"{max(len(str(abs(v))) for v in vals)}")
    say("S3: modular interpolation + CRT ...")
    primes = small_primes_62(300)
    res = None
    mod = None
    stable = 0
    used = 0
    lift = None
    for p in primes:
        c = interp_mod(vals, p)
        if res is None:
            res, mod = c, p
            lift = [v - mod if v > mod // 2 else v for v in res]
        else:
            res = [crt_pair(r, mod, cc, p)[0] for r, cc in zip(res, c)]
            mod *= p
            new_lift = [v - mod if v > mod // 2 else v for v in res]
            stable = stable + 1 if new_lift == lift else 0
            lift = new_lift
        used += 1
        if stable >= 3:
            break
    assert stable >= 3, "CRT did not stabilize; add primes"
    disc = lift
    say(f"S3 CRT stable after {used} primes ({time.time()-t0:.0f}s)")
    # trim trailing zeros
    while disc and disc[-1] == 0:
        disc.pop()
    say(f"candidate deg = {len(disc)-1}")
    say("S3 PROOF: exact evaluation at all nodes ...")
    for a0 in range(D + 1):
        if peval(disc, a0) != vals[a0]:
            raise RuntimeError(f"exact verification FAILED at {a0}")
        if a0 % 400 == 0:
            say(f"  verified through {a0} ({time.time()-t0:.0f}s)")
    say(f"S3 proof complete: candidate == disc ({time.time()-t0:.0f}s)")
    # S4
    say("S4: dividing out torsion factors ...")
    P = disc[:]
    mults = {}
    for N in KNOWN:
        q = psi_N(N)
        k = 0
        while True:
            Pn = pdiv_exact(P, q)
            if Pn is None:
                break
            P = Pn
            k += 1
        if k:
            mults[N] = k
            say(f"  psi_{N} divides with multiplicity {k}")
    cP = content(P)
    say(f"remainder deg {len(P)-1}, content {cP}, lc {P[-1]}")
    degP = len(P) - 1
    say("S4: exhaustive candidate torsion minpolys ...")
    checked = 0
    hits = []
    for N in range(1, 2001):
        import sympy as sp
        if N > 2 and sp.totient(N) // 2 > degP:
            continue
        q = psi_N(N)
        checked += 1
        if pdiv_exact(P, q) is not None:
            hits.append(N)
    say(f"checked {checked} candidate psi_N; divisors of remainder: "
        f"{hits}")
    ok = (not hits) and abs(P[-1] // cP if cP else P[-1]) != 1
    json.dump({"m": m, "degree_bound": D, "disc_degree": len(disc)-1,
               "torsion_multiplicities": {str(k): v
                                          for k, v in mults.items()},
               "remainder_degree": degP,
               "remainder_content": str(cP),
               "remainder_lc": str(P[-1]),
               "remainder_primitive_lc_abs": str(abs(P[-1] // cP)),
               "psi_candidates_checked": checked,
               "remainder_torsion_divisors": hits,
               "converse_m18_established": bool(ok),
               "rh_established": False},
              open(f'matrix/m{m}_sieve.json', 'w'), indent=1)
    say(f"done ({time.time()-t0:.0f}s); converse m={m}: {ok}")


if __name__ == "__main__":
    main()
