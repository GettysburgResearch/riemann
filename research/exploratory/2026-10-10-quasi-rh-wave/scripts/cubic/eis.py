"""Eisenstein-integer arithmetic for sextic/cubic residue symbols and Gauss sums.
Elements are (x, y) meaning x + y*omega, omega = e^{2 pi i/3}, omega^2 = -1 - omega.
N(x+y w) = x^2 - x y + y^2.  Primary: x = 1 mod 3, y = 0 mod 3.
Sextic symbol (u/pi)_6 = zeta6^k, zeta6 = -omega^2 = e^{i pi/3}.  We return k in 0..5, or -1 if pi | u.
e(z) = exp(4 pi i Im z / sqrt 3).
"""
import numpy as np
from math import gcd
from sympy import primerange, factorint, isprime

ZETA6 = np.exp(1j*np.pi/3)
OMEGA = np.exp(2j*np.pi/3)

def norm(x, y):
    return x*x - x*y + y*y

def mul(a, b):
    x1, y1 = a; x2, y2 = b
    return (x1*x2 - y1*y2, x1*y2 + x2*y1 - y1*y2)

def conj(a):
    x, y = a
    return (x - y, -y)

def is_primary(a):
    x, y = a
    return x % 3 == 1 and y % 3 == 0

def primary_assoc(a):
    """Return the primary associate of a (assumes a coprime to 3)."""
    units = [(1,0), (-1,0), (0,1), (0,-1), (-1,-1), (1,1)]  # 1,-1,w,-w,w^2,-w^2
    for u in units:
        b = mul(a, u)
        if is_primary(b):
            return b
    raise ValueError("not coprime to 3: %r" % (a,))

def exact_div(a, b):
    """a / b in Z[w], assuming b | a."""
    nb = norm(*b)
    num = mul(a, conj(b))
    assert num[0] % nb == 0 and num[1] % nb == 0, (a, b)
    return (num[0]//nb, num[1]//nb)

# ---------- primes ----------
def split_prime_above(p):
    """Return primary pi = (a,b) with N(pi) = p, p = 1 mod 3 (one of the two; the other is its conjugate)."""
    # find a^2 - ab + b^2 = p with a = 1, b = 0 mod 3
    import math
    B = int(math.isqrt(4*p//3)) + 2
    for b in range(0, B+1, 3):
        for sgn in (1, -1):
            bb = sgn*b
            # a^2 - a bb + bb^2 - p = 0 -> a = (bb +- sqrt(4p - 3bb^2))/2
            disc = 4*p - 3*bb*bb
            if disc < 0: continue
            s = math.isqrt(disc)
            if s*s != disc: continue
            for a in ((bb + s)//2, (bb - s)//2):
                if a*a - a*bb + bb*bb == p and a % 3 == 1 and bb % 3 == 0:
                    return (a, bb)
    raise ValueError(p)

def primary_primes(X, include_inert=True, exclude_two=False):
    """All primary primes pi with N(pi) <= X (coprime to 3). Returns list of dicts."""
    out = []
    for p in primerange(2, X+1):
        if p == 3: continue
        if p % 3 == 1:
            pi = split_prime_above(p)
            out.append(dict(el=pi, p=p, N=p, split=True))
            out.append(dict(el=conj(pi), p=p, N=p, split=True))
        elif include_inert and p*p <= X:
            if p == 2 and exclude_two: continue
            out.append(dict(el=(-p, 0), p=p, N=p*p, split=False))
    out.sort(key=lambda d: (d['N'], d['el']))
    return out

# ---------- residue field data ----------
def split_data(pi):
    a, b = pi
    p = norm(a, b)
    r = (-a * pow(b, -1, p)) % p          # omega -> r
    assert (r*r + r + 1) % p == 0
    # zeta6 = -omega^2 -> -r^2
    z = (-r*r) % p
    tab = {}
    v = 1
    for k in range(6):
        tab[v] = k
        v = (v*z) % p
    return p, r, tab

def sextic_scalar(u, pr):
    """(u/pi)_6 exponent k (zeta6^k) or -1."""
    x, y = u
    if pr['split']:
        p = pr['p']
        if 'tab' not in pr:
            _, r, tab = split_data(pr['el']); pr['r'] = r; pr['tab'] = tab
        v = (x + y*pr['r']) % p
        if v == 0: return -1
        if (p-1) % 6 != 0: raise ValueError
        w = pow(v, (p-1)//6, p)
        return pr['tab'][w]
    else:
        p = pr['p']
        x %= p; y %= p
        if x == 0 and y == 0: return -1
        q = p*p
        if (q-1) % 6 != 0: raise ValueError("sextic symbol undefined at 2")
        w = fq_pow((x, y), (q-1)//6, p)
        tab = {(1,0):0, (1,1):1, (0,1):2, (p-1,0):3, (p-1,p-1):4, (0,p-1):5}
        return tab[w]

def cubic_scalar(u, pr):
    """(u/pi)_3 exponent j (omega^j) or -1.  Works also at pi = -2."""
    x, y = u
    if pr['split']:
        p = pr['p']
        if 'tab' not in pr:
            _, r, tab = split_data(pr['el']); pr['r'] = r; pr['tab'] = tab
        v = (x + y*pr['r']) % p
        if v == 0: return -1
        w = pow(v, (p-1)//3, p)
        r = pr['r']
        return {1:0, r:1, (r*r)%p:2}[w]
    else:
        p = pr['p']
        x %= p; y %= p
        if x == 0 and y == 0: return -1
        q = p*p
        w = fq_pow((x, y), (q-1)//3, p)
        return {(1,0):0, (0,1):1, (p-1,p-1):2}[w]

def fq_mul(a, b, p):
    x1, y1 = a; x2, y2 = b
    return ((x1*x2 - y1*y2) % p, (x1*y2 + x2*y1 - y1*y2) % p)

def fq_pow(a, e, p):
    res = (1, 0); base = a
    while e:
        if e & 1: res = fq_mul(res, base, p)
        base = fq_mul(base, base, p); e >>= 1
    return res

# ---------- vectorized symbol tables ----------
def dlog_table(p, g):
    """arr[v] = log_g v for v in 1..p-1 (arr[0] = -1)."""
    arr = np.full(p, -1, dtype=np.int64)
    v = 1
    pw = np.empty(p-1, dtype=np.int64)
    for j in range(p-1):
        pw[j] = v; v = (v*g) % p
    arr[pw] = np.arange(p-1)
    return arr

def primitive_root(p):
    from sympy import primitive_root as pr
    return pr(p)

def sextic_table_split(pr):
    """Returns (p, r, K) with K[v] = sextic exponent of v in F_p (K[0] = -1)."""
    p, r, tab = split_data(pr['el'])
    g = primitive_root(p)
    dl = dlog_table(p, g)
    k0 = tab[pow(g, (p-1)//6, p)]       # g^{(p-1)/6} = zeta6^{k0}
    K = np.where(dl >= 0, (dl * k0) % 6, -1).astype(np.int8)
    return p, r, K

def sextic_vec(pr, X, Y):
    """Vectorized (u/pi)_6 exponents for arrays X, Y (u = X + Y w). Returns int8 array, -1 where pi | u."""
    if pr['split']:
        if 'K' not in pr:
            p, r, K = sextic_table_split(pr); pr['K'] = K; pr['r'] = r
        p = pr['p']
        v = (X % p + (Y % p) * pr['r']) % p
        return pr['K'][v]
    else:
        p = pr['p']; q = p*p
        if 'K2' not in pr:
            # table over F_{p^2} indexed by x*p + y
            K2 = np.full(q, -1, dtype=np.int8)
            for x in range(p):
                for y in range(p):
                    if x == 0 and y == 0: continue
                    K2[x*p+y] = sextic_scalar((x, y), pr)
            pr['K2'] = K2
        idx = (X % p) * p + (Y % p)
        return pr['K2'][idx]

# ---------- enumeration ----------
def primary_elements(X, coprime_to_2=False):
    """All primary (x,y) with N <= X, sorted by norm. Returns arrays x, y, N."""
    import math
    A = int(math.isqrt(4*X//3)) + 3
    xs = np.arange(-A, A+1); ys = np.arange(-A, A+1)
    xs = xs[xs % 3 == 1]; ys = ys[ys % 3 == 0]
    XX, YY = np.meshgrid(xs, ys, indexing='ij')
    NN = XX*XX - XX*YY + YY*YY
    m = (NN <= X) & (NN > 0)
    if coprime_to_2:
        m &= ~((XX % 2 == 0) & (YY % 2 == 0))
    XX, YY, NN = XX[m], YY[m], NN[m]
    o = np.lexsort((YY, XX, NN))
    return XX[o], YY[o], NN[o]

def all_elements(X, nonzero=True):
    import math
    A = int(math.isqrt(4*X//3)) + 3
    xs = np.arange(-A, A+1)
    XX, YY = np.meshgrid(xs, xs, indexing='ij')
    NN = XX*XX - XX*YY + YY*YY
    m = (NN <= X)
    if nonzero: m &= (NN > 0)
    XX, YY, NN = XX[m], YY[m], NN[m]
    o = np.lexsort((YY, XX, NN))
    return XX[o], YY[o], NN[o]

# ---------- Gauss sums at primes ----------
def gauss_split(pr, j):
    """Normalized Gauss sum gamma_j(pi) = p^{-1/2} sum_{d in F_p} chi_pi(d)^j e(d/pi), pi = a + b w split.
    e(d/pi) = exp(-2 pi i b d / p)."""
    if 'K' not in pr:
        p, r, K = sextic_table_split(pr); pr['K'] = K; pr['r'] = r
    a, b = pr['el']; p = pr['p']
    d = np.arange(1, p)
    k = pr['K'][d].astype(np.int64)
    ch = ZETA6 ** ((j*k) % 6)
    return np.sum(ch * np.exp(-2j*np.pi*b*d/p)) / np.sqrt(p)

def gauss_inert(pr, j):
    """gamma_j(-p) = p^{-1} sum_{d in F_{p^2}} chi(d)^j e(d/(-p)), e(d/(-p)) = exp(-2 pi i y/p), d = x + y w."""
    p = pr['p']; q = p*p
    if p == 2:
        # only cubic character defined (j even)
        assert j % 2 == 0
        vals = 0j
        for x in range(2):
            for y in range(2):
                if x == 0 and y == 0: continue
                c = cubic_scalar((x, y), pr)
                vals += OMEGA**((j//2*c) % 3) * np.exp(-2j*np.pi*y/p)
        return vals / p
    X = np.repeat(np.arange(p), p); Y = np.tile(np.arange(p), p)
    k = sextic_vec(pr, X, Y).astype(np.int64)
    m = k >= 0
    ch = ZETA6 ** ((j*k[m]) % 6)
    return np.sum(ch * np.exp(-2j*np.pi*Y[m]/p)) / p

def gauss_prime(pr, j):
    return gauss_split(pr, j) if pr['split'] else gauss_inert(pr, j)

def symbol_val(u, pr, j=1):
    """chi_pi(u)^j as complex (0 if pi | u).  For p=2 only j even."""
    if pr['p'] == 2 and not pr['split']:
        c = cubic_scalar(u, pr)
        return 0 if c < 0 else OMEGA**((j//2*c) % 3)
    k = sextic_scalar(u, pr)
    return 0 if k < 0 else ZETA6**((j*k) % 6)

# ---------- factorization of primary elements ----------
def spf_sieve(X):
    spf = np.zeros(X+1, dtype=np.int64)
    for i in range(2, X+1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf

def factor_primary(el, N, spf, prime_lookup):
    """Return list of (prime_record, multiplicity) for primary el with norm N.
    prime_lookup: dict p -> list of prime records above p."""
    x, y = el
    out = []
    n = N
    while n > 1:
        p = int(spf[n]); e = 0
        while n % p == 0: n //= p; e += 1
        if p % 3 == 2:
            out.append((prime_lookup[p][0], e//2))
        else:
            recs = prime_lookup[p]
            # multiplicity of each
            for pr in recs:
                v = 0; cur = (x, y)
                while True:
                    r = pr['r'] if 'r' in pr else split_data(pr['el'])[1]
                    pr['r'] = r
                    if (cur[0] + cur[1]*r) % p != 0: break
                    cur = exact_div(cur, pr['el']); v += 1
                if v: out.append((pr, v))
    return out

def dlog_table_fast(p, g):
    """arr[v] = log_g v, via chunked powers (numpy)."""
    B = 1024
    small = np.empty(min(B, p-1), dtype=np.int64)
    v = 1
    for j in range(len(small)):
        small[j] = v; v = (v*g) % p
    gB = v if len(small) == B else None
    nchunks = (p - 2)//B + 1
    big = np.empty(nchunks, dtype=np.int64)
    w = 1
    for k in range(nchunks):
        big[k] = w
        if gB is not None: w = (w*gB) % p
    allp = (big[:, None] * small[None, :]) % p      # g^{kB + j}
    idx = (np.arange(nchunks)[:, None]*B + np.arange(len(small))[None, :])
    allp = allp.ravel(); idx = idx.ravel()
    m = idx < p-1
    arr = np.full(p, -1, dtype=np.int64)
    arr[allp[m]] = idx[m]
    return arr

def sextic_table_split(pr):
    p, r, tab = split_data(pr['el'])
    g = primitive_root(p)
    dl = dlog_table_fast(p, g)
    k0 = tab[pow(g, (p-1)//6, p)]
    K = np.where(dl >= 0, (dl * k0) % 6, -1).astype(np.int8)
    return p, r, K

def ray9(x, y):
    """(s, t) mod 3 with (u-1)/3 = s + t w for primary u = x + y w."""
    return ((x-1)//3) % 3, (y//3) % 3

def xi9(x, y, a, b):
    s, t = ray9(x, y)
    return OMEGA ** ((a*s + b*t) % 3)

def fq_pow_vec(X, Y, e, p):
    """Vectorized (X + Y w)^e in F_p[w]."""
    rx = np.ones_like(X); ry = np.zeros_like(X)
    bx = X % p; by = Y % p
    while e:
        if e & 1:
            rx, ry = (rx*bx - ry*by) % p, (rx*by + bx*ry - ry*by) % p
        bx, by = (bx*bx - by*by) % p, (2*bx*by - by*by) % p
        e >>= 1
    return rx, ry

def sextic_vec(pr, X, Y):
    """Vectorized (u/pi)_6 exponents for arrays X, Y (u = X + Y w). int8, -1 where pi | u."""
    if pr['split']:
        if 'K' not in pr:
            p, r, K = sextic_table_split(pr); pr['K'] = K; pr['r'] = r
        p = pr['p']
        v = (X % p + (Y % p) * pr['r']) % p
        return pr['K'][v]
    p = pr['p']; q = p*p
    X = np.asarray(X) % p; Y = np.asarray(Y) % p
    wx, wy = fq_pow_vec(X, Y, (q-1)//6, p)
    out = np.full(X.shape, -1, dtype=np.int8)
    for (ax, ay), k in {(1,0):0, (1,1):1, (0,1):2, (p-1,0):3, (p-1,p-1):4, (0,p-1):5}.items():
        out[(wx == ax) & (wy == ay)] = k
    out[(X == 0) & (Y == 0)] = -1
    return out

def cubic_vec(pr, X, Y):
    """Vectorized cubic exponent j ((u/pi)_3 = omega^j), -1 where pi | u.  Works at -2."""
    if pr['split']:
        k = sextic_vec(pr, X, Y)
        return np.where(k >= 0, (2*k) % 6 // 2, -1).astype(np.int8)
    p = pr['p']; q = p*p
    X = np.asarray(X) % p; Y = np.asarray(Y) % p
    wx, wy = fq_pow_vec(X, Y, (q-1)//3, p)
    out = np.full(X.shape, -1, dtype=np.int8)
    for (ax, ay), k in {(1,0):0, (0,1):1, (p-1,p-1):2}.items():
        out[(wx == ax) & (wy == ay)] = k
    out[(X == 0) & (Y == 0)] = -1
    return out

def gauss_inert(pr, j):
    p = pr['p']; q = p*p
    X = np.repeat(np.arange(p), p); Y = np.tile(np.arange(p), p)
    if j % 2 == 0:
        c = cubic_vec(pr, X, Y).astype(np.int64); m = c >= 0
        ch = OMEGA ** (((j//2)*c[m]) % 3)
    else:
        k = sextic_vec(pr, X, Y).astype(np.int64); m = k >= 0
        ch = ZETA6 ** ((j*k[m]) % 6)
    return np.sum(ch * np.exp(-2j*np.pi*Y[m]/p)) / p

def fit_exponent(Xg, S):
    """Least-squares slope of log S vs log X with standard error."""
    lx = np.log(Xg); ly = np.log(S)
    A = np.vstack([lx, np.ones_like(lx)]).T
    coef, res, _, _ = np.linalg.lstsq(A, ly, rcond=None)
    n = len(lx)
    if n > 2:
        resid = ly - A @ coef
        s2 = np.sum(resid**2)/(n-2)
        cov = s2 * np.linalg.inv(A.T @ A)
        se = np.sqrt(cov[0,0])
    else:
        se = float('nan')
    return coef[0], se

def rms_window(Nsorted, S, X, frac=0.5):
    """rms of |S| over indices with X*frac < N <= X."""
    lo = np.searchsorted(Nsorted, X*frac, side='right'); hi = np.searchsorted(Nsorted, X, side='right')
    if hi <= lo: return np.nan
    return np.sqrt(np.mean(np.abs(S[lo:hi])**2))
