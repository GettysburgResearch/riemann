"""Lane B4 evaluator: Xi_k(t) = i^k xi^(k)(1/2 + i t), k = 0..K (K <= 6 tested).

xi(s) = P(s) E(s) G(s) Z(s), P = s(s-1)/2, E = pi^(-s/2), G = Gamma(s/2), Z = zeta(s).
Multinomial Leibniz over the four factors; Gamma derivatives via complete Bell
polynomials in polygamma values (exact), zeta derivatives via mpmath.zeta(s, derivative=j).

Budgeted error model (NOT interval arithmetic):
  each returned value comes with scale = sum of |Leibniz terms|;
  assumed abs error <= scale * EPS_BUDGET, EPS_BUDGET = 10^-(dps-5).
  The imaginary part of i^k xi^(k)(1/2+it) (exactly 0 for real t) is asserted
  below scale * EPS_BUDGET at every call — an end-to-end consistency check.
"""
import mpmath as mp
from math import comb

def _binom(n, i):
    return comb(n, i)

def gamma_derivs_at(z, K):
    """Return [Gamma(z), Gamma'(z), ..., Gamma^(K)(z)] via Bell polynomial recurrence.
    B_0 = 1; B_{n+1} = sum_{i=0}^n C(n,i) B_{n-i} x_{i+1}, x_m = psi^{(m-1)}(z).
    Gamma^{(j)}(z) = Gamma(z) * B_j."""
    g = mp.gamma(z)
    psis = [mp.psi(m, z) for m in range(K)]  # psi^(0), ..., psi^(K-1)
    B = [mp.mpf(1)]
    for n in range(K):
        s = mp.mpf(0)
        for i in range(n + 1):
            s += _binom(n, i) * B[n - i] * psis[i]
        B.append(s)
    return [g * B[j] for j in range(K + 1)]

def xi_block(t, K):
    """Xi_k(t) for k=0..K at real t (mpf). Returns (vals, scales) where
    vals[k] = Re(i^k xi^(k)(1/2+it)) as mpf, scales[k] = sum |Leibniz terms| (mpf).
    Asserts |Im| <= scales[k]*EPS_BUDGET * 10 (fail-closed)."""
    t = mp.mpf(t)
    s = mp.mpc(mp.mpf('0.5'), t)
    eps_budget = mp.mpf(10) ** (-(mp.mp.dps - 5))
    # factor derivative lists 0..K
    P = [s * (s - 1) / 2, s - mp.mpf('0.5'), mp.mpf(1)] + [mp.mpf(0)] * max(0, K - 2)
    P = P[:K + 1]
    lp = -mp.log(mp.pi) / 2
    E0 = mp.power(mp.pi, -s / 2)
    E = [E0 * lp ** j for j in range(K + 1)]
    Ghalf = gamma_derivs_at(s / 2, K)          # d^j/dz^j Gamma(z) at z=s/2
    G = [Ghalf[j] * mp.mpf(2) ** (-j) for j in range(K + 1)]  # d^j/ds^j Gamma(s/2)
    Z = [mp.zeta(s) if j == 0 else mp.zeta(s, derivative=j) for j in range(K + 1)]
    vals, scales = [], []
    ik = mp.mpc(1)  # i^k
    for k in range(K + 1):
        tot = mp.mpc(0)
        sc = mp.mpf(0)
        # multinomial over a+b+c+d = k
        fk = mp.factorial(k)
        for a in range(min(k, 2) + 1):
            for b in range(k - a + 1):
                for c in range(k - a - b + 1):
                    d = k - a - b - c
                    coeff = fk / (mp.factorial(a) * mp.factorial(b) * mp.factorial(c) * mp.factorial(d))
                    term = coeff * P[a] * E[b] * G[c] * Z[d]
                    tot += term
                    # error scale: zeta evals have ABSOLUTE error ~eps*max(1,|Z|)
                    # (relative accuracy collapses at zeta zeros) -> ballast |Z_d|+1.
                    sc += abs(coeff * P[a] * E[b] * G[c]) * (abs(Z[d]) + 1)
        v = ik * tot
        assert abs(v.imag) <= 10 * sc * eps_budget, (
            "Im consistency fail at t=%s k=%d: im=%s scale=%s" % (mp.nstr(t, 25), k, mp.nstr(v.imag, 5), mp.nstr(sc, 5)))
        vals.append(v.real)
        scales.append(sc)
        ik *= mp.mpc(0, 1)
    return vals, scales

def xi_k(t, k):
    """Single Xi_k(t) (with scale)."""
    vals, scales = xi_block(t, k)
    return vals[k], scales[k]

def sign_margin(val, scale, factor=10):
    """Return +1/-1 if sign certified with margin factor*scale*eps, else 0."""
    eps_budget = mp.mpf(10) ** (-(mp.mp.dps - 5))
    if abs(val) > factor * scale * eps_budget:
        return 1 if val > 0 else -1
    return 0
