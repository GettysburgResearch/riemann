"""Core: Polya kernel Phi (repo normalization Phi = 4K, per L-16001(e)), its
derivatives, and a HIGH-PRECISION half-period-panel quadrature for

    E_j = 2 * int_T^inf Phi(t) cos(2 pi alpha j t) dt,   T = 1/(2 alpha).

The repo's own evaluator (experiments/X-16002-.../decay.py) uses
    quad(lambda t: Phi(t)*cos(w*t), [T, T+1, T+2, 4])
which for w = 2*pi*alpha*j with j up to 40 has ~40-160 oscillations inside a
single panel.  We instead subdivide at the half-periods of cos(w t) so every
panel is non-oscillatory, which is what lets us trust ~30+ digits at j = 40.
"""
from mpmath import mp, mpf, pi, exp, cos, quad, zeta, gamma, mpc

# ---------------------------------------------------------------- kernel


def Phi(t, nmax=None):
    """Phi(t) = sum_{n>=1} (4 pi^2 n^4 e^{9t/2} - 6 pi n^2 e^{5t/2}) e^{-pi n^2 e^{2t}}.
    Exactly the repo's evaluator (X-16002/decay.py, smooth.py, windowed_small.py)."""
    t = abs(t)
    u = exp(2 * t)
    e9 = exp(9 * t / 2)
    e5 = exp(5 * t / 2)
    if nmax is None:
        # truncate when pi n^2 u exceeds working precision demand
        need = mp.dps * 2.302585 + 60.0
        nmax = int((float(need) / float(pi * u)) ** 0.5) + 3
        nmax = max(nmax, 4)
    tot = mpf(0)
    for n in range(1, nmax + 1):
        n2 = mpf(n) ** 2
        tot += (4 * pi**2 * n2**2 * e9 - 6 * pi * n2 * e5) * exp(-pi * n2 * u)
    return tot


def dPhi(t, k=1, nmax=None):
    """k-th derivative of Phi at t>0, term-by-term in closed form.

    Write the n-th term as P_n(t) = A_n(t) * exp(-c_n e^{2t}) with
    A_n(t) = a e^{9t/2} + b e^{5t/2}, c_n = pi n^2.  We differentiate
    symbolically in the variable t using mpmath's `diff` on the *single term*
    would be slow/unstable, so instead we use the substitution-free route:
    represent each term as a finite combination of e^{r t} exp(-c e^{2t}) and
    differentiate that basis exactly.

    d/dt [ e^{rt} exp(-c e^{2t}) ] = (r - 2 c e^{2t}) e^{rt} exp(-c e^{2t}).

    So each term stays of the form  Q(e^{2t}) e^{rt} exp(-c e^{2t}) with Q a
    polynomial; we track Q as a coefficient list.
    """
    t = abs(t)
    u = exp(2 * t)
    if nmax is None:
        need = mp.dps * 2.302585 + 60.0
        nmax = int((float(need) / float(pi * u)) ** 0.5) + 3
        nmax = max(nmax, 4)
    tot = mpf(0)
    for n in range(1, nmax + 1):
        c = pi * mpf(n) ** 2
        for (amp, r) in ((4 * pi**2 * mpf(n) ** 4, mpf(9) / 2),
                         (-6 * pi * mpf(n) ** 2, mpf(5) / 2)):
            # start with Q(x) = 1 (x stands for e^{2t}); factor amp*e^{rt}*exp(-c x)
            Q = [mpf(1)]
            for _ in range(k):
                # d/dt [ Q(x) e^{rt} e^{-c x} ] with x = e^{2t}, dx/dt = 2x
                # = [ 2 x Q'(x) + r Q(x) - 2 c x Q(x) ] e^{rt} e^{-c x}
                newdeg = len(Q)  # degree grows by 1
                R = [mpf(0)] * (newdeg + 1)
                for i, q in enumerate(Q):
                    R[i] += r * q          # r Q
                    if i >= 1:
                        R[i] += 2 * i * q  # 2 x Q'(x)  -> shifts x^{i-1}*i -> x^i
                    R[i + 1] += -2 * c * q  # -2 c x Q
                Q = R
            val = mpf(0)
            xp = mpf(1)
            for q in Q:
                val += q * xp
                xp *= u
            tot += amp * val * exp(r * t) * exp(-c * u)
    return tot


# ---------------------------------------------------------------- Xi

def xi_(s):
    return mpf(1) / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)


def Xi(z):
    return (xi_(mpf(1) / 2 + mpc(0, 1) * mpf(z))).real


# ---------------------------------------------------------------- tail cutoff

def tail_cutoff():
    """t_end such that Phi(t) < 10^{-(dps+40)} for t > t_end.
    Phi(t) ~ 4 pi^2 e^{9t/2} exp(-pi e^{2t}); demand pi e^{2t} > need."""
    need = mp.dps * 2.302585 + 120.0
    from math import log
    return mpf(log(need / float(pi)) / 2.0) + mpf('0.4')


# ---------------------------------------------------------------- E_j

def E_j(alpha, j, T=None, maxdegree=6):
    """E_j = 2 int_T^inf Phi(t) cos(2 pi alpha j t) dt, T = 1/(2 alpha) by default.
    Panels aligned to the half-periods of cos(w t)."""
    alpha = mpf(alpha)
    if T is None:
        T = 1 / (2 * alpha)
    T = mpf(T)
    w = 2 * pi * alpha * j
    tend = tail_cutoff()
    if tend <= T:
        tend = T + 1
    half = pi / w
    # panel breakpoints: T, and then the zeros of cos(w t) beyond T
    # zeros at t = (pi/2 + k pi)/w
    import math
    k0 = math.ceil(float((w * T / pi) - mpf(1) / 2))
    pts = [T]
    k = k0
    while True:
        tk = (pi / 2 + k * pi) / w
        if tk <= T:
            k += 1
            continue
        if tk >= tend:
            break
        pts.append(tk)
        k += 1
        if len(pts) > 20000:
            raise RuntimeError("too many panels")
    pts.append(tend)
    tot = mpf(0)
    for a, b in zip(pts[:-1], pts[1:]):
        tot += quad(lambda t: Phi(t) * cos(w * t), [a, b], maxdegree=maxdegree)
    return 2 * tot


def E_asym(alpha, j, nterms=1, T=None):
    """Leading terms of the lattice asymptotic
       E_j = -2 (-1)^j sum_{m>=0} (-1)^m Phi^{(2m+1)}(T) / w^{2m+2}."""
    alpha = mpf(alpha)
    if T is None:
        T = 1 / (2 * alpha)
    T = mpf(T)
    w = 2 * pi * alpha * j
    s = mpf(0)
    for m in range(nterms):
        s += (-1) ** m * dPhi(T, 2 * m + 1) / w ** (2 * m + 2)
    return -2 * (-1) ** j * s
