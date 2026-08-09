"""M1 — Stage 1 multiplicative reduction: EXACT exhaustive minimization of the
transported GFEP functional over the class H = {completely multiplicative +-1 sources}.

Source model: f(p) in {+-1} free on primes; f(k) = prod_{p|k} f(p) on squarefree k;
functional consumes f at squarefree k only (squarefree restriction = f*mu^2):
    Sigma^f_{X,n}(p) = sum_{k sf <= X/n} f(k) c^{X,n}_p(k),   c_p(k) >= 0 (T-90007 census).
True mu instance: f = lambda (all prime signs -1), since mu(k) = (-1)^{omega(k)} on sf k.

Exact minimization over H per exit:
  any sf k <= K has at most ONE prime factor > sqrt(K)  (two would give k > K).
  Core = primes <= sqrt(K); Big = primes in (sqrt(K), K]. Each q in Big appears only in
  k = q*m with m Core-only sf, and two Big primes never share a k => conditional on the
  2^|Core| core assignments the Big signs optimize INDEPENDENTLY:
     min_f Sigma^f = min_{s in {+-1}^Core} [ sum_m s(m) c(m)  -  sum_{q in Big} | sum_m s(m) c(qm) | ].
  Both inner objects over all 2^|Core| assignments are Walsh-Hadamard transforms of the
  c-vector placed at core factor-masks. Exact (float64); independent rechecks below.

Validation paths: (V1) full brute-force enumeration over ALL prime signs at small K;
(V2) value at f=lambda vs true-mu Sigma (and vs flow path); (V3) found minimizer
re-evaluated through the INDEPENDENT first-entrance flow recursion (mpmath dps30)
with sign vector f(k)*mu(k)^2 (squarefree restriction).
"""
import sys, os, time, json
import numpy as np
SCRATCH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRATCH)
from g3_adv import mobius_sieve, children, Gtab, coeffs, flow_sigma_exact
from mpmath import mp, mpf, log as mlog, sqrt as msqrt
mp.dps = 30

# ---------- basic sieves ----------
def primes_upto(N):
    if N < 2: return []
    s = np.ones(N+1, dtype=bool); s[:2] = False
    for i in range(2, int(N**0.5)+1):
        if s[i]: s[i*i::i] = False
    return [int(p) for p in np.nonzero(s)[0]]

def spf_sieve(N):
    spf = np.zeros(N+1, dtype=np.int64)
    for p in primes_upto(N):
        spf[p::p] = np.where(spf[p::p] == 0, p, spf[p::p])
    return spf

def factor_sf(k, spf):
    """prime factors of squarefree k (assumes squarefree)."""
    ps = []
    while k > 1:
        p = int(spf[k]); ps.append(p); k //= p
    return ps

# ---------- fast Walsh-Hadamard ----------
def wht(v):
    """in-place WHT: out[s] = sum_m (-1)^{popcount(s & m)} v[m]; len power of 2."""
    a = v.copy(); h = 1; n = len(a)
    while h < n:
        a = a.reshape(-1, 2*h)
        x = a[:, :h].copy(); y = a[:, h:2*h].copy()
        a[:, :h] = x + y; a[:, h:2*h] = x - y
        a = a.reshape(n); h *= 2
    return a

# ---------- exact class minimization ----------
def min_mult_class(cvec, K, mu, verbose=False):
    """Exact min over H of sum_{k sf <= K} f(k) cvec[k].
    Returns (minval, prime_sign_dict, diagnostics)."""
    P = primes_upto(K)
    core = [p for p in P if p*p <= K]
    big = [p for p in P if p*p > K]
    ncore = len(core); Nass = 1 << ncore
    cidx = {p: i for i, p in enumerate(core)}
    spf = spf_sieve(K)
    sf = [k for k in range(1, K+1) if mu[k] != 0]
    mask = {}
    for k in sf:
        ps = factor_sf(k, spf)
        bigp = [p for p in ps if p in set(big)]
        if len(bigp) >= 2: raise RuntimeError("two big primes in one k: impossible")
        m = 0
        for p in ps:
            if p in cidx: m |= (1 << cidx[p])
        mask[k] = (m, bigp[0] if bigp else None)
    # core-only part
    vcore = np.zeros(Nass)
    for k in sf:
        m, bq = mask[k]
        if bq is None: vcore[m] += cvec[k]
    tot = wht(vcore)
    # fold big primes
    inner_store = {}
    for q in big:
        vq = np.zeros(Nass)
        for k in sf:
            m, bq = mask[k]
            if bq == q: vq[m] += cvec[k]
        iq = wht(vq)
        inner_store[q] = iq
        tot = tot - np.abs(iq)
    s_star = int(np.argmin(tot)); val = float(tot[s_star])
    signs = {}
    for p in core:
        signs[p] = -1 if (s_star >> cidx[p]) & 1 else +1
    for q in big:
        iq = inner_store[q][s_star]
        signs[q] = -1 if iq >= 0 else +1   # tie -> -1 (mu-like)
    # value at f = lambda for reference (all -1): index with all core bits set, big signs -1
    s_lam = Nass - 1
    val_lam = float(wht(vcore)[s_lam] - sum(inner_store[q][s_lam] * (-1) * (-1) if False else -abs(0) for q in big)) if False else None
    diag = dict(ncore=ncore, nbig=len(big), tot=tot)
    return val, signs, diag

def eval_mult(cvec, K, mu, signs, spf=None):
    """direct evaluation sum_{k sf} f(k) c(k) from prime signs."""
    if spf is None: spf = spf_sieve(K)
    tot = 0.0
    for k in range(1, K+1):
        if mu[k] == 0: continue
        f = 1
        for p in factor_sf(k, spf): f *= signs[p]
        tot += f * cvec[k]
    return tot

def brute_force_min(cvec, K, mu):
    """full enumeration over all prime sign vectors (only for small prime counts)."""
    P = primes_upto(K); npr = len(P)
    assert npr <= 16, "too many primes for brute force"
    spf = spf_sieve(K)
    sf = [k for k in range(1, K+1) if mu[k] != 0]
    pidx = {p: i for i, p in enumerate(P)}
    kmask = []
    for k in sf:
        m = 0
        for p in factor_sf(k, spf): m |= (1 << pidx[p])
        kmask.append(m)
    kmask = np.array(kmask); cs = np.array([cvec[k] for k in sf])
    best = None; bs = None
    for s in range(1 << npr):
        # parity of popcount(s & kmask)
        x = np.bitwise_and(kmask, s)
        par = np.zeros(len(kmask), dtype=np.int64)
        xx = x.copy()
        while xx.any():
            par ^= (xx & 1); xx >>= 1
        v = float(np.sum(np.where(par == 1, -cs, cs)))
        if best is None or v < best: best, bs = v, s
    return best, bs

# ---------- pretentious distances ----------
def kronecker(D, p):
    """Kronecker symbol (D/p) for prime p."""
    if p == 2:
        if D % 2 == 0: return 0
        r = D % 8
        return 1 if r in (1, 7) else -1
    if D % p == 0: return 0
    return pow(D % p, (p-1)//2, p) == 1 and 1 or -1

def distances(signs, K, label=""):
    P = [p for p in primes_upto(K)]
    out = {}
    out['D2_to_lambda'] = sum((1 - signs[p]*(-1))/p for p in P)
    out['D2_to_one'] = sum((1 - signs[p]*1)/p for p in P)
    # to n^{it}
    best = None; bt = 0.0
    ts = np.arange(0, 40.0, 0.005)
    lp = np.array([np.log(p) for p in P]); ip = np.array([1.0/p for p in P])
    sg = np.array([signs[p] for p in P], dtype=float)
    for t in ts:
        d2 = float(np.sum((1 - sg*np.cos(t*lp))*ip))
        if best is None or d2 < best: best, bt = d2, float(t)
    out['D2_to_nit_min'] = best; out['argmin_t'] = bt
    # to real characters chi_D (fundamental discriminants |D|<=40) and to lambda*chi_D
    fund = [-3,-4,5,-7,8,-8,-11,12,13,-15,17,-19,-20,21,-23,24,-24,28,29,-31,33,-35,37,-39,40,-40]
    dch = {}
    for D in fund:
        d2c = sum((1 - signs[p]*kronecker(D, p))/p for p in P)          # f ~ chi_D
        d2lc = sum((1 - signs[p]*(-1)*kronecker(D, p))/p for p in P)    # f ~ lambda*chi_D
        dch[D] = (d2c, d2lc)
    Dbest = min(dch, key=lambda D: dch[D][0]); Lbest = min(dch, key=lambda D: dch[D][1])
    out['best_chi'] = (Dbest, dch[Dbest][0]); out['best_lambda_chi'] = (Lbest, dch[Lbest][1])
    return out

# ---------- per-(X,n) run ----------
def run_point(X, n, do_flow=True, brute=False):
    t0 = time.time()
    mu = mobius_sieve(X)
    w = [mpf(0)]*(X+2)
    for q in range(1, X+1): w[q] = mlog(mpf(X)/q)/msqrt(mpf(q))
    K = X//n
    W = list(range(n, min(2*n, X+1)))
    print(f"== ({X},{n})  Kmax={K}  |W|={len(W)}  primes<=K: {len(primes_upto(K))} "
          f"(core {len([p for p in primes_upto(K) if p*p<=K])})")
    C = {p: coeffs(X, n, p, w) for p in W}
    spf = spf_sieve(K)
    # per-exit exact class min
    res = {}
    for p in W:
        val, signs, diag = min_mult_class(C[p], K, mu, verbose=False)
        true_val = sum(mu[k]*C[p][k] for k in range(1, K+1) if mu[k] != 0)
        free_min = C[p][1] - sum(abs(C[p][k]) for k in range(2, K+1) if mu[k] != 0)
        res[p] = dict(minH=val, signs=signs, true=true_val, free=free_min)
    pworst = min(W, key=lambda p: res[p]['minH'])
    r = res[pworst]
    print(f"   min_p min_H Sigma^f = {r['minH']:+.6f} at exit p={pworst}   "
          f"(true mu value there {r['true']:+.6f}; global true min {min(res[p]['true'] for p in W):+.6f})")
    print(f"   FREE min at that exit = {r['free']:+.6f}  (class-H rescue factor {r['minH']/r['free']:+.4f})")
    plus = sorted([p for p, s in r['signs'].items() if s == +1])
    print(f"   minimizer prime signs: +1 at {plus if plus else 'NONE (= lambda = true mu)'}")
    # aggregate one-scalar over the window
    cagg = np.zeros(K+1)
    for p in W: cagg += np.array([0]+[C[p][k] for k in range(1, K+1)])
    aval, asigns, _ = min_mult_class(cagg, K, mu)
    atrue = sum(mu[k]*cagg[k] for k in range(1, K+1) if mu[k] != 0)
    aplus = sorted([p for p, s in asigns.items() if s == +1])
    print(f"   window aggregate: min_H = {aval:+.6f} (true {atrue:+.6f}); +1 primes {aplus if aplus else 'NONE'}")
    # validation V1: brute force
    if brute:
        bf, bs = brute_force_min(C[pworst], K, mu)
        print(f"   V1 brute-force full enumeration: min = {bf:+.6f}  (match {abs(bf-r['minH']):.2e})")
    # validation V2: eval_mult at minimizer matches
    ev = eval_mult(C[pworst], K, mu, r['signs'], spf)
    print(f"   V2 direct re-eval of minimizer: {ev:+.6f} (delta {abs(ev-r['minH']):.2e})")
    # validation V3: independent flow path at the found global minimizer
    if do_flow:
        sgn = [0]*(X+2)
        for k in range(1, K+1):
            if mu[k] == 0: continue
            f = 1
            for q in factor_sf(k, spf): f *= r['signs'][q]
            sgn[k] = f
        Sig = flow_sigma_exact(X, n, sgn)
        print(f"   V3 flow recheck (mpmath dps30): Sigma^f({pworst}) = {float(Sig[pworst]):+.8f}  "
              f"(coeff path {r['minH']:+.8f}; delta {abs(float(Sig[pworst])-r['minH']):.2e}); "
              f"min over W = {float(min(Sig.values())):+.8f}")
    # distances of the minimizer
    dd = distances(r['signs'], K)
    print(f"   distances of minimizer: D2(f,lambda)={dd['D2_to_lambda']:.4f}  D2(f,1)={dd['D2_to_one']:.4f}  "
          f"min_t D2(f,n^it)={dd['D2_to_nit_min']:.4f} at t={dd['argmin_t']:.3f}")
    print(f"      best chi_D: D={dd['best_chi'][0]} D2={dd['best_chi'][1]:.4f};  "
          f"best lambda*chi_D: D={dd['best_lambda_chi'][0]} D2={dd['best_lambda_chi'][1]:.4f}")
    # single-flip rigidity spectrum at binding exit: delta(q) = Sigma^{f_q} - Sigma^{lambda},
    # f_q = lambda except f(q)=+1;  delta(q) = 2*sum_{m sf, q coprime m, qm<=K} lambda(m) c(qm)
    # (each prime fiber is the SAME mu-functional one level down: self-similarity)
    cb = C[pworst]; Pl = primes_upto(K)
    deltas = {}
    for q in Pl:
        s = 0.0
        for m in range(1, K//q + 1):
            if mu[m] == 0 or m % q == 0: continue
            s += mu[m] * cb[q*m] * (-1)   # lambda(m) = mu(m) on sf; sign: -2*lambda(qm)c = +2*lambda(m)c... net below
        deltas[q] = -2*s
    qmin = min(deltas, key=lambda q: deltas[q])
    dsort = sorted(deltas.items(), key=lambda kv: kv[1])[:6]
    print(f"   single-flip spectrum at p={pworst}: min delta(q) = {deltas[qmin]:+.4f} at q={qmin}; "
          f"smallest: {[(q, round(d,4)) for q,d in dsort]}")
    nbeat = sum(1 for p in W if res[p]['minH'] < res[p]['true'] - 1e-10)
    print(f"   exits where some f in H beats lambda: {nbeat}/{len(W)}")
    # binding-family table: minH per exit (first 12)
    l1 = "   p:    " + " ".join(f"{p:7d}" for p in W[:12])
    l2 = "   minH: " + " ".join(f"{res[p]['minH']:+7.3f}" for p in W[:12])
    l3 = "   true: " + " ".join(f"{res[p]['true']:+7.3f}" for p in W[:12])
    print(l1); print(l2); print(l3)
    nneg = sum(1 for p in W if res[p]['minH'] < 0)
    print(f"   exits with min_H < 0: {nneg}/{len(W)}   scaled sqrt(n)*min = {np.sqrt(n)*r['minH']:+.4f}   "
          f"[{time.time()-t0:.1f}s]")
    return res, pworst

if __name__ == "__main__":
    pts = [(2000,20), (3000,25), (3000,100), (4000,15), (6000,15), (10000,20)]
    if len(sys.argv) > 1:
        pts = [tuple(map(int, a.split(','))) for a in sys.argv[1:]]
    for (X, n) in pts:
        brute = (X, n) in [(3000,100)]
        run_point(X, n, do_flow=(X <= 6000), brute=brute)
        print()
