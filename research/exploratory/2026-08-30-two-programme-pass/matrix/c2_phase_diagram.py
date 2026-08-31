"""C2: the deformation phase diagram of the trace-scaling line
Z_t(s) = prod_p 1/(1 - t a_p p^{-s} + p^{1-2s})  (11a1 data, good primes).

Part 1 — temperedness phase transition (exact + statistical):
  |t| <= 1  =>  ZERO violations of t^2 a_p^2 <= 4p at every p (Hasse,
  exact); |t| > 1  =>  positive-density violation with the Sato-Tate
  closed form D(t) = (2 theta* - sin 2 theta*)/pi, theta* = arccos(1/|t|)
  (ST imported as labelled theorem; empirical convergence measured on
  9591 good primes <= 1e5).

Part 2 — EXACT strata identities at the integer points (good primes):
  t = 0:   Z_0(s)  = zeta^{(11)}(4s-2) / zeta^{(11)}(2s-1)
  t = -1:  Z_{-1}(s) = L^{(11)}(Sym^2 f, 2s) / (zeta^{(11)}(2s-1) L(f,s))
  both verified coefficient-by-coefficient on ALL good-support n <= 20000
  (exact integers; a complete proof is 3 lines of local algebra deposited
  in the findings doc — the check certifies the bookkeeping).
  Hence the ONE LINE {Z_t} crosses the full survival trichotomy:
  t=1 entire (imported modularity), t in {0,-1} meromorphic zeta-quotients
  with infinitely many poles (S2), t=2 the cube-defect bridge deformation
  with conjectural natural boundary (S3, conditional per T-108507).

Part 3 — rigidity data: integrality locus of the line is exactly t in Z
  (a_5 = 1 forces it); tempered+integral locus exactly {0, +-1}; first
  violating prime as a function of t on (1, 3].

EXACT_RATIONAL except the labelled float densities. Writes
matrix/c2_phase_diagram.json. rh_established = false.
"""
import json
import math
import sys
import time

N2 = 20000     # coefficient-verification range
BAD = 11


def say(m):
    print(f"[{time.strftime('%H:%M:%S')}] {m}", flush=True)


def load_ap():
    with open("matrix/ap_table_11a1.json") as f:
        t = json.load(f)
    return {int(p): v for p, v in t["a_p"].items()}


# ---------------- Part 1: phase transition --------------------------------

def st_density(t):
    if abs(t) <= 1:
        return 0.0
    th = math.acos(1.0 / abs(t))
    return (2 * th - math.sin(2 * th)) / math.pi


def part1(ap):
    say("Part 1: temperedness phase transition")
    ts = [0.5, 0.9, 1.0, 1.01, 1.05, 1.1, 1.25, 1.5, 1.75, 2.0, 2.25,
          2.5, 3.0]
    rows = {}
    primes = sorted(ap)
    for t in ts:
        emp = {}
        for X in (10 ** 4, 10 ** 5):
            ps = [p for p in primes if p <= X]
            v = sum(1 for p in ps if t * t * ap[p] * ap[p] > 4 * p)
            emp[str(X)] = {"violations": v, "n_primes": len(ps),
                           "density": v / len(ps)}
        rows[str(t)] = {"st_closed_form": st_density(t), "empirical": emp}
        say(f"  t={t}: ST={st_density(t):.4f} "
            f"emp(1e5)={emp['100000']['density']:.4f}")
    # exact statement for |t| <= 1: Hasse gives t^2 a_p^2 <= a_p^2 <= 4p
    # (checked exhaustively over the table as a bookkeeping certificate)
    exact_zero = all(ap[p] * ap[p] <= 4 * p for p in primes)
    return {"grid": rows, "hasse_exact_zero_violations_all_t_leq_1":
            exact_zero,
            "note": ("closed form D(t) = (2 th - sin 2 th)/pi, "
                     "th = arccos(1/|t|); Sato-Tate IMPORTED (labelled); "
                     "densities are floats, everything else exact")}


# ---------------- Part 2: exact strata identities -------------------------

def mult_series(local_coeffs, N):
    """Dirichlet-series coefficient array a[1..N] of a good-prime Euler
    product given local_coeffs(p) -> [u_0=1, u_1, u_2, ...] (list long
    enough that p^len > N)."""
    a = [0] * (N + 1)
    a[1] = 1
    for p in primes_upto(N):
        if p == BAD:
            continue
        u = local_coeffs(p)
        b = a[:]
        pk, k = p, 1
        while pk <= N:
            if k < len(u) and u[k] != 0:
                for n in range(1, N // pk + 1):
                    if b[n]:
                        a[n * pk] += u[k] * b[n]
            pk *= p
            k += 1
    return a


_PRIMES = None


def primes_upto(n):
    global _PRIMES
    if _PRIMES is None:
        s = bytearray([1]) * (n + 1)
        s[0:2] = b"\x00\x00"
        for i in range(2, int(n ** 0.5) + 1):
            if s[i]:
                s[i * i::i] = bytearray(len(s[i * i::i]))
        _PRIMES = [i for i in range(2, n + 1) if s[i]]
    return _PRIMES


def dirichlet_mul(A, B, N):
    c = [0] * (N + 1)
    for i in range(1, N + 1):
        if A[i] == 0:
            continue
        for j in range(1, N // i + 1):
            if B[j]:
                c[i * j] += A[i] * B[j]
    return c


def local_len(p, N):
    k, pk = 0, 1
    while pk <= N:
        pk *= p
        k += 1
    return k + 1


def part2(ap):
    say("Part 2: exact strata identities (good-support n <= %d)" % N2)
    out = {}

    # ---- t = 0 :  Z_0 = zeta(4s-2)/zeta(2s-1), good primes ----
    def lhs0(p):
        L = local_len(p, N2)
        u = [0] * L
        for k in range(0, L, 2):
            u[k] = (-p) ** (k // 2)        # 1/(1 + p^{1-2s}) locally
        return u

    Z0 = mult_series(lhs0, N2)

    def zeta4s2(p):                        # zeta(4s-2): at p^{4j} coeff p^{2j}
        L = local_len(p, N2)
        u = [0] * L
        for k in range(0, L, 4):
            u[k] = p ** (k // 2)
        return u

    def inv_zeta2s1(p):                    # 1/zeta(2s-1): 1 - p * p^{-2s}
        L = local_len(p, N2)
        u = [0] * L
        if L > 2:
            u[2] = -p
        return u

    R0 = dirichlet_mul(mult_series(zeta4s2, N2),
                       mult_series(inv_zeta2s1, N2), N2)
    ok0 = all(Z0[n] == R0[n] for n in range(1, N2 + 1) if n % BAD != 0)
    out["t0_identity_zeta_quotient"] = ok0
    say(f"  t=0: Z_0 = zeta(4s-2)/zeta(2s-1)  "
        f"{'CONFIRMED exactly' if ok0 else 'FAILED'}")

    # ---- t = -1 :  Z_{-1} = L(Sym^2, 2s) / (zeta(2s-1) L(f,s)) ----
    def lhsm1(p):
        L = local_len(p, N2)
        u = [0] * L
        u[0] = 1
        A = ap[p]
        if L > 1:
            u[1] = -A
        for k in range(2, L):
            u[k] = -A * u[k - 1] - p * u[k - 2]
        return u

    Zm1 = mult_series(lhsm1, N2)

    def sym2_2s(p):
        # 1/det(1 - Sym^2(A_p) X), X = p^{-2s}: h-sequence of Sym^2 at
        # p^{2j}; Sym^2 satake: e1 = a^2 - p, e2 = p(a^2 - p), e3 = p^3
        L = local_len(p, N2)
        u = [0] * L
        A = ap[p]
        e1, e2, e3 = A * A - p, p * (A * A - p), p ** 3
        h = [1]
        jmax = (L - 1) // 2
        for j in range(1, jmax + 1):
            v = e1 * h[j - 1]
            if j >= 2:
                v -= e2 * h[j - 2]
            if j >= 3:
                v += e3 * h[j - 3]
            h.append(v)
        for j in range(0, jmax + 1):
            u[2 * j] = h[j]
        return u

    def inv_Lf(p):                         # (1 - a_p p^{-s} + p^{1-2s})
        L = local_len(p, N2)
        u = [0] * L
        u[0] = 1
        if L > 1:
            u[1] = -ap[p]
        if L > 2:
            u[2] = p
        return u

    R = dirichlet_mul(mult_series(sym2_2s, N2),
                      mult_series(inv_zeta2s1, N2), N2)
    R = dirichlet_mul(R, mult_series(inv_Lf, N2), N2)
    okm1 = all(Zm1[n] == R[n] for n in range(1, N2 + 1) if n % BAD != 0)
    out["tm1_identity_sym2_quotient"] = okm1
    say(f"  t=-1: Z_-1 = L(Sym^2,2s)/(zeta(2s-1) L(f,s))  "
        f"{'CONFIRMED exactly' if okm1 else 'FAILED'}")

    out["strata_reading"] = {
        "t=1": "entire L-function (S1); IMPORTED modularity of 11a1",
        "t=-1": ("meromorphic on C as an automorphic quotient (S2): "
                 "infinitely many poles at zeros of L(f,s); Sym^2 "
                 "automorphy IMPORTED (Gelbart-Jacquet)"),
        "t=0": ("meromorphic on C as zeta(4s-2)/zeta(2s-1) (S2): "
                "infinitely many poles at zeros of zeta(2s-1)"),
        "t=2": ("the cube-defect bridge deformation (T-108507): "
                "CONJECTURAL natural boundary (S3), conditional on the "
                "Estermann/Kurokawa criteria"),
        "|t|>1 non-integer": "leaves the integral arithmetic class",
        "headline": ("one line through deformation space crosses the "
                     "entire survival trichotomy, with exact identities "
                     "at every integer point in [-1, 1]")}
    return out


# ---------------- Part 3: rigidity data -----------------------------------

def part3(ap):
    say("Part 3: rigidity of the line")
    primes = sorted(ap)
    import math as _m
    g = 0
    for p in primes[:50]:
        g = _m.gcd(g, ap[p])
    rows = {}
    for i in range(1, 41):
        t = 1 + i * 0.05
        first = None
        for p in primes:
            if t * t * ap[p] * ap[p] > 4 * p:
                first = p
                break
        rows[f"{t:.2f}"] = first
    return {"gcd_of_ap_first50": g,
            "integrality_lemma": ("t * a_5 = t must be an integer "
                                  "(a_5 = 1), and t in Z suffices: "
                                  "integrality locus of the line = Z"),
            "tempered_and_integral_locus": [0, 1, -1],
            "first_violating_prime_by_t": rows}


def main():
    ap = load_ap()
    primes_upto(N2)
    out = {"meta": {"curve": "11a1", "good_primes": len(ap),
                    "ap_limit": 100000, "coeff_check_limit": N2,
                    "arithmetic_class": ("EXACT_RATIONAL + labelled float "
                                         "densities"),
                    "rh_established": False}}
    out["part1_phase_transition"] = part1(ap)
    out["part2_exact_strata"] = part2(ap)
    out["part3_rigidity"] = part3(ap)
    with open("matrix/c2_phase_diagram.json", "w") as f:
        json.dump(out, f, indent=1)
    say("C2 done")


if __name__ == "__main__":
    main()
