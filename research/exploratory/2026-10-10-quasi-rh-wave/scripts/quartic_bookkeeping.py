# Part-I-type bookkeeping. Probe: completed length Z, rows m of norm Q0 = X*Y = Z^rho, X=Z^a, Y=Z^b.
# Direct bound exponent D = -rho/2 + (max(rho,2b)-b)/2 + E/2, where E = log_Z of row energy sum_m |C(Z;m)|^2.
# Principal row exponent C = beta - 1 + 1/N + (1/2-1/N)*a.  Zero-free for beta > sigma0 := 1-1/N-(1/2-1/N)a + D.
# Poisson-side (nonprincipal rows) heuristic constraint: (Z/X)^{1-1/N} Y^{-1/2} (Z/X)^{-kappa} <= 1, kappa = cancellation
# exponent in the u-sum (kappa=1/2: square-root).  (1-a)(1-1/N-kappa) <= b/2.
import itertools
def E_cubic(rho):            # reflection to quadratic coupling, dual length M^2/Z
    return max(rho, 2*rho-1)
def E_quartic_direct_BGL(rho):   # BGL n=4 sieve, rows Z^rho vs c<=Z
    return max(rho, 1.0, 2*(rho+1)/3)
def E_quartic_direct_conj(rho):  # DFDH conjecture (sharp for Gauss-sum sequences)
    return max(rho, 1.0, 3*rho/4+0.5, rho/2+0.75)
def E_quartic_routeB_BGL(rho):   # Kubota FE at frequency m^3: conductor Z^{3rho}, dual length Z^{3rho-1}
    d = 3*rho-1
    if d <= 0: return rho
    return max(rho, d, 2*(rho+d)/3)
def E_quartic_routeB_conj(rho):
    d = 3*rho-1
    if d <= 0: return rho
    return max(rho, d, 0.75*rho+0.5*d, 0.5*rho+0.75*d)
def sigma0(N, a, b, Efun):
    rho = a+b
    E = Efun(rho)
    D = -rho/2 + (max(rho,2*b)-b)/2 + E/2
    return 1-1/N-(0.5-1/N)*a + D
def scan(N, Efun, kappa, label):
    best=None
    grid=[i/200 for i in range(0,401)]
    for a in grid:
        for b in grid:
            if a<=0 or b<=0: continue
            if (1-a)*(1-1/N-kappa) > b/2 + 1e-12: continue   # Poisson-side constraint
            s=sigma0(N,a,b,Efun)
            if best is None or s<best[0]-1e-12: best=(s,a,b)
    print(f"{label}: N={N} kappa={kappa}: min sigma0={best[0]:.5f} at a={best[1]:.3f} b={best[2]:.3f} (rho={best[1]+best[2]:.3f}); balanced a=b=1/2 gives {sigma0(N,0.5,0.5,Efun):.5f}")
print("--- sanity: cubic/sextic N=6 with reflection energy ---")
for k in (0.5, 0.25, 0.0): scan(6, E_cubic, k, "cubic refl")
print("--- quartic N=4 ---")
for k in (0.5, 0.25, 0.0):
    scan(4, E_quartic_direct_BGL, k, "quartic direct sieve BGL")
    scan(4, E_quartic_direct_conj, k, "quartic direct sieve DFDH-conj")
    scan(4, lambda r: min(E_quartic_direct_BGL(r), E_quartic_routeB_BGL(r)), k, "quartic min(direct,RouteB) BGL")
    scan(4, lambda r: min(E_quartic_direct_conj(r), E_quartic_routeB_conj(r)), k, "quartic min(direct,RouteB) conj")
    scan(4, lambda r: max(r, 2*r-1), k, "quartic HYPOTHETICAL quadratic-coupling reflection (E=max(rho,2rho-1))")
print("--- general-N Part I at balance with E=1: 1/2-1/(2N)+1/2 ---")
for N in (4,6,8): print(N, 1-1/(2*N))
print("--- Part II formula from C note: B_N(l)=1-1/(2N)-3l/(2N); floor C0 ---")
