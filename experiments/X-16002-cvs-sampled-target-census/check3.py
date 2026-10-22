from mpmath import mp, mpf, mpc, exp, pi, quad, zeta, gamma, nstr
mp.dps = 30
def xi(s): return mpf(1)/2*s*(s-1)*pi**(-s/2)*gamma(s/2)*zeta(s)
def Xi(z): return xi(mpf(1)/2 + 1j*z)
def K(t):
    t = abs(t); tot = mpf(0)
    for n in range(1, 40):
        term=(pi**2*n**4*exp(9*t/2)-mpf(3)*pi/2*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t))
        tot += term
        if n>3 and abs(term)<mpf(10)**(-50)*max(abs(tot),1): break
    return tot
# hat K(z) = int_{-inf}^{inf} K(t) e^{-i z t} dt ; K decays super-Gaussianly so [-3,3] suffices
print("Direct check of  hat k(z) = int K(t) e^{-izt} dt  vs  Xi(z)/4")
for z in [mpf(0), mpf('3.5'), mpf('14.134725141734693790'), mpc('2.0','0.4')]:
    a = quad(lambda t: K(t)*exp(-1j*z*t), [-3,-1,0,1,3])
    b = Xi(z)/4
    print(f"  z={nstr(z,12):<26} hatK={nstr(a,16):<40} Xi/4={nstr(b,16):<40} |diff|={nstr(abs(a-b),4)}")
print()
print("K(t)>0 over a wide range (Polya positivity of Phi=4K):")
tv=[mpf(x)/10 for x in range(-40,41,5)]
print("  min over t in [-4,4] step 0.5:", nstr(min(K(t) for t in tv),8), " all>0:", all(K(t)>0 for t in tv))
