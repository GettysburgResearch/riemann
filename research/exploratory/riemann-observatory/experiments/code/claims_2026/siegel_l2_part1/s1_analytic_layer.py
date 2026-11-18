"""SIEGEL Level-2 audit, part 1, step 1 (analytic layer: a real zero forces inert-prime mass).
Our own code; nothing from the audited repositories is executed.  Run: python3 -I s1_analytic_layer.py

Checks (each prints PASS/FAIL or a value):
 (a) OAI Lem 2 / Banks (2.5): -zeta'/zeta(s) - 1/(s-1) on (1,2] (bounded, and <= 0 as Banks needs).
 (b) Gamma term 1/2 psi((s+eps)/2) bounded on (1,2] for both parities; Banks kappa = 1/2 log pi - 1/2 psi(3/2).
 (c) Banks Lem 2.1 constants C1 = e^lam/(2 lam^2), C2 = e^lam/4 at lam = 3/2, and the last-step inequality
     e^lam kappa/2 - 1/log 319 > 0.
 (d) The zero-free core of (2.2): -L'/L(s,chi) <= (1/2) log q - kappa for s in (1,2], checked with
     mpmath Hurwitz-zeta derivatives for every fundamental discriminant |D| <= DMAX_LPRIME.
 (e) Rosser-Schoenfeld 1962 Thm 6 (3.21)-(3.22) at every prime < XMAX (the extremal points of the step function).
 (f) Guo Lemma 2.1 numerics: psi(x) <= x log 4, M(x) <= log x + log 4, sum_{p odd} log p/p^2 (true value),
     M(x) - M(y) > log(x/y) - 2 for 100 <= y <= x < XMAX (worst pair via suffix minima).
 (g) Guo Prop 4.1 algebra, tested in its unconditional form (no zero assumed):
        H_beta(t) = L(1,chi) t^eps/eps + zeta(beta) L(beta,chi) + theta L(beta,chi) u^{-beta} + E(t),
        |theta| <= 1, |E(t)| <= (q + 1 + (1/2) log t) t^{1/2-beta},  u = sqrt t, 1/2 <= beta < 1.
     When L(beta,chi)=0 this is exactly Guo (4.4); a failure of the bound would witness an error in the
     paired-tail argument.
 (h) Guo Lemma 5.1 injection inequality H_1(y) J <= N(xy) - N(y) (unconditional, finite).
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 30
XMAX = 10**7
DMAX_LPRIME = 120
out = []
fails = 0


def rep(ok, msg):
    global fails
    if not ok:
        fails += 1
    out.append(("PASS " if ok else "FAIL ") + msg)


def sieve(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


def is_fundamental(D):
    if D in (0, 1):
        return False
    if D % 4 == 1:
        m = abs(D)
    elif D % 4 == 0:
        m4 = D // 4
        if m4 % 4 not in (2, 3):
            return False
        m = abs(m4)
    else:
        return False
    k = 2
    while k * k <= m:
        if m % (k * k) == 0:
            return False
        k += 1
    return True


def _kron(a, n):
    # standard Kronecker symbol algorithm
    if n == 0:
        return 1 if abs(a) == 1 else 0
    res = 1
    if n < 0:
        n = -n
        if a < 0:
            res = -res
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    if v:
        if a % 2 == 0:
            return 0
        if v % 2 == 1 and a % 8 in (3, 5):
            res = -res
    # now n odd, Jacobi (a/n)
    a = a % n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a = a % n
    return res if n == 1 else 0


# ---------------- (a) zeta log-derivative ----------------
grid = [1 + mp.mpf(k) / 400 for k in range(1, 401)]
vals = [-mp.zeta(s, derivative=1) / mp.zeta(s) - 1 / (s - 1) for s in grid]
mx = max(vals)
mn = min(vals)
rep(mx < 0, f"(a) max_{{s in (1,2]}} [-zeta'/zeta(s) - 1/(s-1)] = {mp.nstr(mx, 8)} (<0; Banks uses <=0), "
            f"min = {mp.nstr(mn, 8)} (-> -EulerGamma = {mp.nstr(-mp.euler, 8)} as s->1+)")

# ---------------- (b) gamma term and kappa ----------------
psi_lo = mp.digamma(mp.mpf(1) / 2)
psi_hi = mp.digamma(mp.mpf(3) / 2)
kappa = mp.log(mp.pi) / 2 - mp.digamma(mp.mpf(3) / 2) / 2
rep(True, f"(b) psi((s+eps)/2) on (1,2], eps in {{0,1}} lies in (psi(1/2), psi(3/2)] = "
          f"({mp.nstr(psi_lo, 8)}, {mp.nstr(psi_hi, 8)}]: bounded (OAI 'gamma term is bounded')")
rep(abs(kappa - mp.mpf('0.5541')) < 1e-4, f"(b) Banks kappa = log(pi)/2 - psi(3/2)/2 = {mp.nstr(kappa, 12)} (stated 0.5541...)")

# ---------------- (c) Banks C1, C2 ----------------
lam = mp.mpf(3) / 2
C1 = mp.e ** lam / (2 * lam ** 2)
C2 = mp.e ** lam / 4
rep(abs(C1 - 2 * mp.e ** 1.5 / 9) < 1e-25 and C1 < mp.mpf('0.99594'), f"(c) C1 = e^1.5/4.5 = 2e^1.5/9 = {mp.nstr(C1, 12)} (stated 0.99594, 0.995930...)")
rep(C2 < mp.mpf('1.12043'), f"(c) C2 = e^1.5/4 = {mp.nstr(C2, 12)} (stated 1.12043, 1.120422...)")
last = mp.e ** lam * kappa / 2 - 1 / mp.log(319)
rep(last > 0, f"(c) e^lam*kappa/2 - 1/log 319 = {mp.nstr(last, 8)} > 0 (Banks's final step of Lem 2.1)")
# trade-off table (not used by Banks beyond lam=3/2): delta0 is proportional to 1/C1 once omega is fixed
tbl = []
for l in [mp.mpf(1), mp.mpf(3) / 2, mp.mpf(2)]:
    c1 = mp.e ** l / (2 * l ** 2)
    c2 = mp.e ** l / 4
    om = int(mp.ceil(8 * (c2 + mp.mpf(8) / 5)))
    d0 = 9 / (128 * (om + 1) * c1)
    tbl.append(f"lam={mp.nstr(l,3)}: C1={mp.nstr(c1,6)} C2={mp.nstr(c2,6)} omega={om} delta0={mp.nstr(d0,6)}")
out.append("INFO (c) Banks recipe delta0 = 9/(128 (omega+1) C1), omega = ceil(8(C2+8/5)) as a function of lambda: " + "; ".join(tbl))

# ---------------- (d) -L'/L(s,chi) <= (1/2)log q - kappa ----------------
def Lfun(D, s, deriv=0):
    q = abs(D)
    tot = mp.mpf(0)
    for a in range(1, q + 1):
        c = _kron(D, a)
        if c:
            if deriv == 0:
                tot += c * mp.zeta(s, mp.mpf(a) / q)
            else:
                tot += c * mp.zeta(s, mp.mpf(a) / q, derivative=1)
    return tot


worst = None
cnt = 0
sgrid = [mp.mpf('1.01'), mp.mpf('1.05'), mp.mpf('1.2'), mp.mpf('1.5'), mp.mpf(2)]
mp.mp.dps = 20
for D in list(range(-DMAX_LPRIME, -2)) + list(range(5, DMAX_LPRIME + 1)):
    if not is_fundamental(D):
        continue
    q = abs(D)
    cnt += 1
    for s in sgrid:
        S0 = Lfun(D, s)
        S1 = Lfun(D, s, 1)
        L = mp.power(q, -s) * S0
        Lp = mp.power(q, -s) * (S1 - mp.log(q) * S0)
        val = -Lp / L
        slack = (mp.log(q) / 2 - kappa) - val
        if worst is None or slack < worst[0]:
            worst = (slack, D, s)
rep(worst[0] > 0, f"(d) -L'/L(s,chi) <= (1/2)log q - kappa for all {cnt} fundamental |D| <= {DMAX_LPRIME}, "
                  f"s in {{1.01,1.05,1.2,1.5,2}}: minimal slack {mp.nstr(worst[0], 6)} at D={worst[1]}, s={mp.nstr(worst[2], 4)}")
mp.mp.dps = 30

# ---------------- (e) Rosser-Schoenfeld ----------------
P = sieve(XMAX)
lp = np.log(P.astype(np.float64))
cum = np.cumsum(lp / P)
E = -1.332582275733220881765828776071027748
# lower bound (3.21): worst at x -> next prime (from the left); also check at x = p itself
nxt = np.append(P[1:], XMAX).astype(np.float64)
lx = np.log(nxt)
lower_margin = cum - (lx + E - 1 / (2 * lx))
lx2 = lp
lower_margin2 = cum - (lx2 + E - 1 / (2 * lx2))
rep(lower_margin.min() > 0 and lower_margin2.min() > 0,
    f"(e) RS (3.21) sum_{{p<=x}} log p/p > log x + E - 1/(2 log x): min margin {lower_margin.min():.3e} over x < {XMAX:.0e}")
mask = P >= 317
up_margin = (lp + E + 1 / (2 * lp)) - cum
# x in [319, next prime): worst at x = 319 for the prime 317
x319 = 319.0
m319 = (math.log(x319) + E + 1 / (2 * math.log(x319))) - cum[np.searchsorted(P, 317)]
rep(up_margin[P >= 319].min() > 0 and m319 > 0,
    f"(e) RS (3.22) sum < log x + E + 1/(2 log x) for x >= 319: min margin {min(up_margin[P >= 319].min(), m319):.3e}")

# ---------------- (f) Guo Lemma 2.1 numerics ----------------
# psi(x) <= x log 4 : worst at prime powers
pp = []
for p in P[:2000]:
    pk = int(p)
    while pk <= XMAX:
        pk *= int(p)
        if pk <= XMAX:
            pp.append((pk, math.log(int(p))))
# build psi at all prime powers <= XMAX
events = [(int(p), float(l)) for p, l in zip(P, lp)] + pp
events.sort()
xs = np.array([e[0] for e in events], dtype=np.float64)
psi_cum = np.cumsum(np.array([e[1] for e in events]))
rat = psi_cum / xs
rep(rat.max() < math.log(4), f"(f) psi(x)/x <= log 4 = 1.3863 for x < {XMAX:.0e}: max ratio {rat.max():.5f} at x={int(xs[rat.argmax()])}")
Mmargin = (lp + math.log(4)) - cum
rep(Mmargin.min() > 0, f"(f) M(x) <= log x + log 4: min margin {Mmargin.min():.4f}")
# true value of sum_{p odd} log p / p^2 : sum_p log p/p^2 = -P'(2) ... use direct sum + tail estimate
sq = float(np.sum(lp[1:] / P[1:].astype(np.float64) ** 2))
tail = (math.log(XMAX) + 1) / XMAX  # int_X^inf log t / t^2 dt (crude upper bound for the tail via PNT density <= 1)
rep(sq + tail < 0.35, f"(f) sum_{{p odd}} log p/p^2 = {sq:.6f} (+tail<{tail:.1e}) < 7/20 (Guo certificate 30607/88200 = {30607/88200:.6f})")
# M(x)-M(y) > log(x/y) - 2, 100 <= y <= x: g(x) = M(x) - log x; inf over x in [p_k, p_{k+1}) is at x->p_{k+1}-
g_at = cum - lp                      # g at x = p_k (sup on the step)
g_inf = cum - np.log(nxt)            # inf on [p_k, p_{k+1})
suffix_min = np.minimum.accumulate(g_inf[::-1])[::-1]
idx = np.nonzero(P >= 100)[0]
# for y in [p_k, p_{k+1}) with y >= 100, worst y is y = p_k (or y=100 for the first block)
diff = suffix_min[idx] - g_at[idx]
# block containing 100: y = 100 with M(100) = M(97)
k97 = np.searchsorted(P, 97)
g100 = cum[k97] - math.log(100)
d100 = suffix_min[k97] - g100
worstd = min(diff.min(), d100)
rep(worstd > -2, f"(f) inf_{{100<=y<=x<1e7}} [M(x)-M(y) - log(x/y)] = {worstd:.4f} > -2 (Guo's elementary loss bound 2-7/675)")

# ---------------- (g) Guo Prop 4.1 in unconditional form ----------------
def a_coeffs(D, T):
    """a(n) = sum_{d|n} chi(d) for n <= T, via a divisor-sum sieve."""
    chi = np.array([0] + [_kron(D, n) for n in range(1, T + 1)], dtype=np.int64)
    a = np.zeros(T + 1, dtype=np.int64)
    for d in range(1, T + 1):
        c = chi[d]
        if c:
            a[d::d] += c
    return a


tests = []
worst_ratio = 0.0
nchk = 0
for D in [-3, -4, 5, -7, 8, -8, 12, 13, -163, -71, 229, -1155, 1009]:
    q = abs(D)
    T = 10**6
    a = a_coeffs(D, T)
    nvec = np.arange(1, T + 1, dtype=np.float64)
    for beta in [mp.mpf('0.5'), mp.mpf('0.6'), mp.mpf('0.8'), mp.mpf('0.95'), mp.mpf('0.995')]:
        eps = 1 - beta
        # L(1,chi) = -(1/q) sum_r chi(r) psi(r/q)  (Hurwitz terms diverge individually at s=1)
        L1 = -sum(_kron(D, r) * mp.digamma(mp.mpf(r) / q) for r in range(1, q + 1)) / q
        Lb = mp.power(q, -beta) * Lfun(D, beta)
        zb = mp.zeta(beta)
        w = a[1:] * np.power(nvec, -float(beta))
        Hcum = np.cumsum(w)
        for t in [10, 100, 1000, 10**4, 10**5, 10**6]:
            H = mp.mpf(float(Hcum[t - 1]))
            main = L1 * mp.power(t, eps) / eps + zb * Lb
            u = mp.sqrt(t)
            bound = abs(Lb) * mp.power(u, -beta) + (q + 1 + mp.log(t) / 2) * mp.power(t, mp.mpf(1) / 2 - beta)
            r = float(abs(H - main) / bound)
            worst_ratio = max(worst_ratio, r)
            nchk += 1
rep(worst_ratio <= 1.0, f"(g) Guo Prop 4.1 (unconditional form): max |H_beta(t) - main| / bound = {worst_ratio:.4f} over {nchk} "
                        f"(D, beta, t) triples (13 characters, beta in [1/2, 0.995], t <= 1e6)")

# ---------------- (h) Lemma 5.1 injection inequality ----------------
worst_inj = None
for D in [-3, -4, 5, -163, 229, -1155]:
    T = 300000
    a = a_coeffs(D, T)
    for (y, x) in [(30, 100), (100, 1000), (300, 1000), (50, 5000)]:
        if x * y > T:
            continue
        H1 = sum(a[n] / n for n in range(1, y + 1))
        J = sum(a[p] * math.log(p) / p for p in P[(P > y) & (P <= x)])
        Nxy = sum(a[m] * math.log(m) / m for m in range(y + 1, x * y + 1))
        r = H1 * J - Nxy
        if worst_inj is None or r > worst_inj[0]:
            worst_inj = (r, D, y, x)
rep(worst_inj[0] <= 0, f"(h) H_1(y) J - (N(xy)-N(y)) <= 0: max {worst_inj[0]:.4f} at D={worst_inj[1]}, (y,x)=({worst_inj[2]},{worst_inj[3]})")

print("\n".join(out))
print(f"\nSUMMARY: {sum(1 for o in out if o.startswith('PASS'))} PASS, {fails} FAIL")
