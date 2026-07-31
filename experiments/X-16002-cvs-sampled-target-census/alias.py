from mpmath import mp, mpf, mpc, exp, pi, zeta, gamma, cos, nstr, findroot, polyroots, log, sqrt
mp.dps = 30

def xi(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return xi(mpf(1)/2 + 1j*z)

def K(t):
    t = mpf(t); t = abs(t)          # K is even
    tot = mpf(0)
    for n in range(1, 60):
        term = (pi**2*n**4*exp(9*t/2) - mpf(3)*pi/2*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
        tot += term
        if n > 3 and abs(term) < mpf(10)**(-45)*max(abs(tot),1): break
    return tot

print("K(0) =", nstr(K(0),15), "  4*K(0)=Phi(0) =", nstr(4*K(0),15))
print("Xi(0) = xi(1/2) =", nstr(Xi(0),15))
print("K(t)>0 spot check:", [nstr(K(t),8) for t in [-3,-1,0,0.5,1,2,3]])
print()
print("POISSON / ALIASING IDENTITY TEST")
print(" delta * sum_m K(m*delta) e^{i m delta z}   ==?==  (1/4) sum_j Xi(z + 2 pi j/delta)")
for delta in [mpf('0.5'), mpf('0.25')]:
    for z in [mpf(0), mpf('5'), mpf('14.134725142')]:
        M = int(60/float(delta))
        lhs = delta*sum(K(m*delta)*exp(1j*m*delta*z) for m in range(-M, M+1))
        rhs = sum(Xi(z + 2*pi*j/delta) for j in range(-4,5))/4
        print(f"  delta={delta} z={nstr(z,10)}: LHS={nstr(lhs,14)}  RHS={nstr(rhs,14)}  rel.diff={nstr(abs(lhs-rhs)/max(abs(rhs),mpf('1e-40')),4)}")
print()
print("DOES THE SAMPLED FINITE FOURIER SUM HAVE REAL ZEROS AT ALL?")
print(" f(z)=sum_{m=-M}^{M} K(m d) e^{i m d z};  substitute w=e^{i d z}; g(w)=sum K(m d) w^{m+M}")
print(" real z  <=>  |w|=1.  Count roots with |w|=1 (real z) vs |w|!=1 (nonreal z).")
for delta in [mpf('1.0'), mpf('0.5'), mpf('0.25'), mpf('0.15')]:
    for M in [8, 14, 20]:
        coeffs = [K(m*delta) for m in range(M, -M-1, -1)]   # descending powers w^{2M}..w^0
        try:
            rts = polyroots(coeffs, maxsteps=300, extraprec=300)
        except Exception as e:
            print(f"  delta={delta} M={M}: polyroots failed {e}"); continue
        onc = sum(1 for r in rts if abs(abs(r)-1) < mpf('1e-12'))
        off = len(rts)-onc
        mods = sorted(set(round(float(abs(r)),6) for r in rts))
        print(f"  delta={float(delta):<5} M={M:<3} deg={len(rts):<3} |w|=1: {onc:<3} |w|!=1: {off:<3}  distinct |w| (first 6): {mods[:6]}")
