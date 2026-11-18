import mpmath as mp
mp.mp.dps = 30
s2 = mp.sqrt(2)
def R(psi):
    I1 = mp.quad(psi, [-0.5, 0.5]); I2 = mp.quad(lambda x: psi(x)**2, [-0.5, 0.5])
    inner = lambda x: mp.quad(lambda y: abs(x-y)*psi(y), [-0.5, x, 0.5])
    I3 = mp.quad(lambda x: psi(x)*inner(x), [-0.5, 0.5])
    return (I2+I3)/I1**2
CMT = mp.mpf(1)/2 + mp.cot(1/s2)/s2
print("R(psi0) =", mp.nstr(R(lambda x: mp.mpf(1)), 25))
r = R(lambda x: mp.cos(s2*x)); print("R(psiMT)=", mp.nstr(r, 25), " C_MT=", mp.nstr(CMT,25), " diff=", mp.nstr(r-CMT,3))
# perturbation test: MT is a local minimiser among nonneg densities? try psi = cos(s2 x) + eps*h for a few even h
for eps in (0.05, -0.05):
    for name,h in (("x^2", lambda x: x**2-mp.mpf(1)/12), ("cos(2pi x)", lambda x: mp.cos(2*mp.pi*x)), ("x^4", lambda x: x**4-mp.mpf(1)/80)):
        print(" eps",eps,name, mp.nstr(R(lambda x: mp.cos(s2*x)+eps*h(x)) - CMT, 6))
