"""Lane B1 numerics: Xi_k(t) = i^k xi^{(k)}(1/2 + it) via Leibniz on xi = A * zeta,
A(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2).

A'/A = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2)  =: LA1
LA1' = -1/s^2 - 1/(s-1)^2 + (1/4)psi'(s/2)          =: LA2
LA2' =  2/s^3 + 2/(s-1)^3 + (1/8)psi''(s/2)         =: LA3
A'   = A LA1
A''  = A (LA1^2 + LA2)
A''' = A (LA1^3 + 3 LA1 LA2 + LA3)
xi^{(k)} = sum_j C(k,j) A^{(k-j)} zeta^{(j)}.
"""
import mpmath as mp

def xi_derivs_s(s, K=3):
    """Return [xi(s), xi'(s), ..., xi^{(K)}(s)] for complex s, K<=3."""
    s = mp.mpc(s)
    A  = mp.mpf('0.5')*s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)
    LA1 = 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.psi(0, s/2)/2
    Aj = [A, A*LA1]
    if K >= 2:
        LA2 = -1/s**2 - 1/(s-1)**2 + mp.psi(1, s/2)/4
        Aj.append(A*(LA1**2 + LA2))
    if K >= 3:
        LA3 = 2/s**3 + 2/(s-1)**3 + mp.psi(2, s/2)/8
        Aj.append(A*(LA1**3 + 3*LA1*LA2 + LA3))
    zj = [mp.zeta(s, 1, j) for j in range(K+1)]
    out = []
    for k in range(K+1):
        out.append(sum(mp.binomial(k, j)*Aj[k-j]*zj[j] for j in range(k+1)))
    return out

def Xi_all(t, K=3):
    """Return [Xi_0(t), ..., Xi_K(t)] for complex t."""
    s = mp.mpf('0.5') + mp.mpc(0, 1)*mp.mpc(t)
    xis = xi_derivs_s(s, K)
    I = mp.mpc(0, 1)
    return [ (I**k) * xis[k] for k in range(K+1) ]

def Xi_all_real(t, K=3):
    """Xi_k at real t; returns list of real mpf (asserts imaginary parts negligible)."""
    vals = Xi_all(mp.mpf(t), K)
    out = []
    for v in vals:
        m = abs(v)
        if m > 0:
            assert abs(v.imag) <= mp.mpf('1e-10')*m, (t, v)
        out.append(v.real)
    return out

if __name__ == '__main__':
    import time
    mp.mp.dps = 40
    # self-test: compare xi''' via Leibniz against mp.diff at s0 = 0.7+3j
    s0 = mp.mpc('0.7', '3.0')
    lz = xi_derivs_s(s0, 3)
    def xi0(s):
        return mp.mpf('0.5')*s*(s-1)*mp.power(mp.pi, -s/2)*mp.gamma(s/2)*mp.zeta(s)
    for k in range(4):
        nd = mp.diff(xi0, s0, k)
        rel = abs(lz[k]-nd)/abs(nd)
        print(f"k={k} leibniz={mp.nstr(lz[k],12)} diff={mp.nstr(nd,12)} rel={mp.nstr(rel,3)}")
    # functional equation check for derivatives: xi^{(k)}(s) = (-1)^k xi^{(k)}(1-s)
    l2 = xi_derivs_s(1-s0, 3)
    for k in range(4):
        rel = abs(lz[k] - (-1)**k * l2[k])/abs(lz[k])
        print(f"FE k={k} rel={mp.nstr(rel,3)}")
    # reality of Xi_k on real axis
    print([mp.nstr(v, 10) for v in Xi_all_real(mp.mpf(21.0), 3)])
    # timing at height 100
    t0 = time.time(); Xi_all(mp.mpc(100, -1), 3); t1 = time.time()
    print("time per Xi_all(K=3) at t=100-1j:", t1-t0, "s")
    t0 = time.time(); Xi_all(mp.mpf(97.3), 3); t1 = time.time()
    print("time per Xi_all(K=3) at t=97.3:", t1-t0, "s")
