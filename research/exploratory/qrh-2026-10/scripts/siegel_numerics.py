#!/usr/bin/env python3
"""Light EMPIRICAL checks for "Uniform exclusion of Landau-Siegel zeros" (OpenAI, 1 Oct 2026).

  python3 -I siegel_numerics.py consts   # check the explicit Lemma 2 constant c(s) <= 0 on (1,2] (mpmath)
  python3 -I siegel_numerics.py bias     # prime bias for fields with long inert runs / small L(1,chi)
  python3 -I siegel_numerics.py det N d H  # exact interpolation determinant in Q(sqrt d, sqrt 2)

Arithmetic classes: 'consts' and 'bias' are FLOATING (double / mpmath 30 digits, no directed
rounding). 'det' is EXACT (Python integers in Z[sqrt d, sqrt 2]) except the greedy row selection,
which is done modulo three random 61-bit primes and accepted only if all three agree
(PROBABILISTIC for the selection; the determinant, its norm and its valuations are exact).
Nothing here is a proof; finite checks only.
"""
import math, random, sys, time

# ---------------------------------------------------------------- utilities
def primes_upto(n):
    s = bytearray([1]) * (n + 1); s[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(range(i*i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]

def kron(D, p):
    """Kronecker symbol (D/p) for a prime p."""
    if p == 2:
        if D % 2 == 0: return 0
        return 1 if D % 8 in (1, 7) else -1
    r = pow(D % p, (p - 1) // 2, p)
    return 0 if r == 0 else (1 if r == 1 else -1)

def is_fundamental(D):
    if D in (0, 1): return False
    def sqf(m):
        m = abs(m)
        i = 2
        while i * i <= m:
            if m % (i * i) == 0: return False
            i += 1
        return True
    if D % 4 == 1: return sqf(D)
    if D % 4 == 0:
        m = D // 4
        return m % 4 in (2, 3) and sqf(m)
    return False

def class_number_neg(D):
    """h(D) for fundamental D < -4 by counting reduced forms."""
    h = 0; a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a): continue
            c = (b * b - D) // (4 * a)
            if c < a: continue
            if c == a and b < 0: continue
            h += 1
        a += 1
    return h

# ---------------------------------------------------------------- consts
def cmd_consts():
    import mpmath as mp
    mp.mp.dps = 30
    worst = -mp.inf
    for i in range(1, 201):
        s = 1 + mp.mpf(i) / 200
        z = -mp.diff(mp.zeta, s) / mp.zeta(s) - 1 / (s - 1)
        for eps in (0, 1):
            c = z + mp.digamma((s + eps) / 2) / 2 - mp.log(mp.pi) / 2
            worst = max(worst, c)
    print(f"max over s in (1,2] (200-point grid), eps in {{0,1}} of c(s) = [-zeta'/zeta - 1/(s-1)] + psi((s+eps)/2)/2 - log(pi)/2: {mp.nstr(worst, 8)}")
    print("  (negative => -zeta'/zeta - L'/L(s,chi) <= (1/2) log q + 1/(s-1) - 1/(s-beta) with no extra constant)")

# ---------------------------------------------------------------- bias
def cmd_bias(PMAX=2_000_000):
    t0 = time.time()
    P = primes_upto(PMAX)
    small = P[:60]
    # search fundamental D (|D| <= 10^6) with the longest run of inert odd primes (least split prime)
    rec = {}
    for sign in (-1, 1):
        best = []
        for m in range(3, 1_000_001):
            D = sign * m
            if D % 4 not in (0, 1): continue
            # quick reject: first few odd primes must be inert
            ok = True
            for p in (3, 5, 7, 11, 13):
                if kron(D, p) != -1: ok = False; break
            if not ok or not is_fundamental(D): continue
            run = 0
            for p in small[1:]:
                if kron(D, p) == -1: run = p
                else: break
            best.append((run, D))
        best.sort(reverse=True)
        rec[sign] = best[:3]
    fields = [-163, -67, -43, -427] + [D for _, D in rec[-1][:2]] + [5, 8 * 0 + 13] + [D for _, D in rec[1][:2]]
    seen = []
    for D in fields:
        if D not in seen and is_fundamental(D): seen.append(D)
    print(f"[bias] primes to {PMAX:,}; longest inert odd-prime runs (|D|<=1e6): neg {rec[-1]}, pos {rec[1]}")
    E = math.e
    print("  For each D: q=|D|, l=log q. For X = q^lambda: phi_- = inert share of sum_{p<=X} log p/p;")
    print("  M+ = sum_{p<=X, chi(p)=+1} log p/p in units of l; Lemma-2 cap without a zero term is (e/4) l = 0.680 l;")
    print("  delta_req = smallest delta Lemma 2 allows given M+ (any real zero must have delta >= delta_req).")
    import numpy as np
    Parr = np.array(P, dtype=np.float64); logP = np.log(Parr); wP = logP / Parr
    for D in seen:
        q = abs(D); l = math.log(q)
        chi = np.array([kron(D, p) for p in P], dtype=np.int8)
        hinfo = ""
        if D < -4:
            h = class_number_neg(D); L1 = math.pi * h / math.sqrt(q)
            hinfo = f" h={h} L(1,chi)={L1:.4f} L(1,chi)*log q={L1*l:.3f}"
        firstsplit = next((p for p, c in zip(P, chi) if c == 1), None)
        print(f"\n  D={D} q={q} l={l:.3f} least split prime={firstsplit}{hinfo}")
        dreq_best = 0.0
        for lam in [0.5, 0.75, 1, 1.5, 2, 3, 4, 6, 8]:
            X = q ** lam
            if X > PMAX or X < 3: continue
            m = Parr <= X
            tot = wP[m].sum(); plus = wP[m & (chi == 1)].sum(); minus = wP[m & (chi == -1)].sum()
            lX = math.log(X)
            dreq = max(0.0, plus - (E / 4) * l) * l / ((E / 2) * lX * lX)
            dreq_best = max(dreq_best, dreq)
            print(f"    lambda={lam:<5} X={X:>12.0f} phi_-={minus/tot:.3f} M+/l={plus/l:.3f} delta_req={dreq:.3f}")
        # reverse Lemma 2 with the full truncated series (all prime powers <= PMAX), s on a grid
        pw_logs, pw_vals, pw_coef = [], [], []
        for p, c in zip(P, chi):
            if p * p > PMAX: break
            pk, ck = p * p, int(c) * int(c)
            while pk <= PMAX:
                pw_logs.append(math.log(p)); pw_vals.append(pk); pw_coef.append(1 + ck)
                pk *= p; ck *= int(c)
        pl, pv, pc = np.array(pw_logs), np.array(pw_vals, dtype=np.float64), np.array(pw_coef, dtype=np.float64)
        coef = (1 + chi.astype(np.float64)) * logP
        best, bests = 0.0, None
        for k in range(1, 81):
            s = 1 + k / 80
            T = float((coef * Parr ** (-s)).sum() + (pc * pl * pv ** (-s)).sum())
            W = l / 2 + 1 / (s - 1) - T
            gap = 1 / W - (s - 1)
            if gap > best: best, bests = gap, s
        print(f"    reverse Lemma 2 (series truncated at {PMAX:,}): no real zero in [1 - {best:.4f}, 1) (s={bests}); delta >= {best*l:.3f}")
    print(f"\n[bias] done in {time.time()-t0:.1f}s")

# ---------------------------------------------------------------- det
class Ring:
    """Z[a,b], a^2 = d, b^2 = 2; elements (c0, c1, c2, c3) = c0 + c1 a + c2 b + c3 ab."""
    def __init__(self, d): self.d = d
    def mul(self, x, y):
        d = self.d
        x0, x1, x2, x3 = x; y0, y1, y2, y3 = y
        return (x0*y0 + d*x1*y1 + 2*x2*y2 + 2*d*x3*y3,
                x0*y1 + x1*y0 + 2*(x2*y3 + x3*y2),
                x0*y2 + x2*y0 + d*(x1*y3 + x3*y1),
                x0*y3 + x3*y0 + x1*y2 + x2*y1)
    def sub(self, x, y): return tuple(u - v for u, v in zip(x, y))
    @staticmethod
    def sig(x): return (x[0], -x[1], x[2], -x[3])
    @staticmethod
    def tau(x): return (x[0], x[1], -x[2], -x[3])
    @staticmethod
    def sigtau(x): return (x[0], -x[1], -x[2], x[3])
    def conjprod(self, y):
        return self.mul(self.mul(self.sig(y), self.tau(y)), self.sigtau(y))
    def norm(self, y):
        z = self.mul(y, self.conjprod(y)); assert z[1] == z[2] == z[3] == 0; return z[0]
    def pw(self, x, e):
        r = (1, 0, 0, 0)
        while e:
            if e & 1: r = self.mul(r, x)
            x = self.mul(x, x); e >>= 1
        return r

def sqrt_mod(n, p):
    n %= p
    if n == 0: return 0
    assert pow(n, (p - 1) // 2, p) == 1
    if p % 4 == 3: return pow(n, (p + 1) // 4, p)
    # Tonelli-Shanks
    q, s = p - 1, 0
    while q % 2 == 0: q //= 2; s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1: z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        i, tt = 0, t
        while tt != 1: tt = tt * tt % p; i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c, t, r = i, b * b % p, t * b * b % p, r * b % p
    return r

def is_prime(n):
    if n < 2: return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0: return n == p
    dd, s = n - 1, 0
    while dd % 2 == 0: dd //= 2; s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, dd, n)
        if x in (1, n - 1): continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def greedy_mod(Pm, d, N, H, cols, maxw):
    ra, rb = sqrt_mod(d, Pm), sqrt_mod(2, Pm)
    th = [(n1 + n2*ra + n3*rb + n4*ra*rb) % Pm for (n1, n2, n3, n4) in cols]
    sg = [(n1 - n2*ra + n3*rb - n4*ra*rb) % Pm for (n1, n2, n3, n4) in cols]
    st = [(n1 - n2*ra - n3*rb + n4*ra*rb) % Pm for (n1, n2, n3, n4) in cols]
    M = len(cols)
    idx = sorted(((a1 + H*(a2 + a3), a2, a3, a1) for w in range(maxw + 1)
                  for a2 in range(w // H + 1) for a3 in range(w // H + 1 - a2)
                  for a1 in [w - H*(a2 + a3)] if a1 >= 0 and w == a1 + H*(a2+a3)))
    basis = {}   # pivot column -> normalized row
    kept = []
    for (w, a2, a3, a1) in idx:
        row = [pow(th[j], a1, Pm) * pow(sg[j], a2, Pm) % Pm * pow(st[j], a3, Pm) % Pm for j in range(M)]
        for pc, br in basis.items():
            f = row[pc]
            if f:
                row = [(x - f * y) % Pm for x, y in zip(row, br)]
        pc = next((j for j in range(M) if row[j]), None)
        if pc is None: continue
        inv = pow(row[pc], Pm - 2, Pm)
        row = [x * inv % Pm for x in row]
        for k in list(basis):
            f = basis[k][pc]
            if f: basis[k] = [(x - f * y) % Pm for x, y in zip(basis[k], row)]
        basis[pc] = row
        kept.append((a1, a2, a3))
        if len(kept) == M: return kept
    return None

def bareiss(Rg, A):
    A = [row[:] for row in A]; n = len(A); sign = 1
    prev = (1, 0, 0, 0); prevconj, prevnorm = (1, 0, 0, 0), 1
    zero = (0, 0, 0, 0)
    for k in range(n - 1):
        if A[k][k] == zero:
            sw = next((i for i in range(k + 1, n) if A[i][k] != zero), None)
            if sw is None: return zero
            A[k], A[sw] = A[sw], A[k]; sign = -sign
        akk = A[k][k]
        for i in range(k + 1, n):
            aik = A[i][k]
            for j in range(k + 1, n):
                num = Rg.sub(Rg.mul(akk, A[i][j]), Rg.mul(aik, A[k][j]))
                t = Rg.mul(num, prevconj)
                assert all(c % prevnorm == 0 for c in t)
                A[i][j] = tuple(c // prevnorm for c in t)
            A[i][k] = zero
        prev = akk; prevconj = Rg.conjprod(prev); prevnorm = Rg.norm(prev)
        if prevnorm < 0: prevnorm = -prevnorm; prevconj = tuple(-c for c in prevconj)
    det = A[n - 1][n - 1]
    return det if sign == 1 else tuple(-c for c in det)

def vp(n, p):
    n = abs(n); v = 0
    while n % p == 0: n //= p; v += 1
    return v

def cmd_det(N, d, H):
    t0 = time.time()
    Rg = Ring(d)
    D = d if d % 4 == 1 else 4 * d
    q = abs(D)
    cols = [(n1, n2, n3, n4) for n1 in range(N) for n2 in range(N) for n3 in range(N) for n4 in range(N)]
    M = len(cols)
    rng = random.Random(20261001 + 7 * N + d)
    sels = []
    while len(sels) < 3:
        Pm = rng.randrange(2**60, 2**61) | 1
        if not is_prime(Pm) or pow(d % Pm, (Pm - 1) // 2, Pm) != 1 or pow(2, (Pm - 1) // 2, Pm) != 1: continue
        sels.append(greedy_mod(Pm, d, N, H, cols, maxw=60 * N))
    agree = sels[0] is not None and all(s == sels[0] for s in sels)
    kept = sels[0]
    print(f"[det] N={N} M={M} d={d} (q={q}) H={H}: greedy selections agree mod 3 primes: {agree}")
    if not agree: return
    S1 = sum(a[0] for a in kept); S2 = sum(a[1] + a[2] for a in kept)
    wmax = max(a[0] + H*(a[1] + a[2]) for a in kept); a1max = max(a[0] for a in kept)
    U = N ** (4 / 3)
    print(f"  retained rows: S1={S1} S2={S2} S2/S1={S2/S1:.3f} max weight={wmax} max alpha1={a1max} (U={U:.2f}, bound 96 H^(2/3) U={96*H**(2/3)*U:.0f})")
    th = [(n1, n2, n3, n4) for (n1, n2, n3, n4) in cols]
    rows = []
    for (a1, a2, a3) in kept:
        rows.append([Rg.mul(Rg.mul(Rg.pw(t, a1), Rg.pw(Rg.sig(t), a2)), Rg.pw(Rg.sigtau(t), a3)) for t in th])
    Delta = bareiss(Rg, rows)
    Nm = Rg.norm(Delta)
    assert Nm != 0
    logN4 = math.log(abs(Nm)) / 4
    had = (M / 2) * math.log(M) + (S1 + S2) * math.log(8 * N * math.sqrt(q))
    print(f"  exact Delta != 0; (1/4) log|Nm Delta| = {logN4:.1f}; Hadamard upper bound (4.1) = {had:.1f}  [{time.time()-t0:.1f}s]")
    print("   p  class          chi(p) (2/p)  4E_p  v_p(Nm Delta)  predicted")
    lower = 0.0
    for p in primes_upto(max(a1max, 3)):
        if p == 2 or q % p == 0: continue
        c, c2 = kron(D, p), kron(8, p)
        Ep = sum(a[0] // p for a in kept)
        cls = "sigma" if (c == -1 and c2 == 1) else "sigma*tau" if c == -1 else "id (split)" if c2 == 1 else "tau"
        if c == -1 and p > H:
            pred = "Lemma 7: >= 4E_p"; lower += Ep * math.log(p)
        elif cls == "id (split)":
            pred = "PROPOSED ext.: >= 4E_p"
        else:
            pred = "(no Frobenius claim)"
        v = vp(Nm, p)
        flag = "" if (not pred.startswith(("Lemma", "PROPOSED")) or v >= 4 * Ep) else "  <-- VIOLATION"
        print(f"  {p:>3}  {cls:<13} {c:>6} {c2:>5} {4*Ep:>5} {v:>14}  {pred}{flag}")
    print(f"  admissible-prime lower bound sum E_p log p = {lower:.1f} <= (1/4)log|Nm| = {logN4:.1f} <= {had:.1f}")
    print(f"[det] done in {time.time()-t0:.1f}s")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "consts"
    if cmd == "consts": cmd_consts()
    elif cmd == "bias": cmd_bias()
    elif cmd == "det": cmd_det(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else: print(__doc__)
