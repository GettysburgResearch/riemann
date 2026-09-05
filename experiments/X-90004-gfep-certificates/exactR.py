"""Verify: R_X(m) = X^{-1/2} * int_{m/X}^{(m+1)/X} t^{-3/2} C_{N(t)}(log 1/t) dt exactly,
where N(t) = floor(1/t) (with knot handling), against the raw Mobius definition.
Also verify continuity of Utilde(theta) = X^{1/2} U_X(m) as function of theta at knots."""
from mpmath import mp, mpf, log, sqrt, quad
mp.dps = 30

def mobius_list(n):
    mu = [0]*(n+1); mu[1]=1
    for i in range(1, n+1):
        if mu[i]:
            for j in range(2*i, n+1, i):
                mu[j] -= mu[i]
    return mu

X = 997
mu = mobius_list(X+1)

def w(q):
    if q > X or q < 1: return mpf(0)
    return log(mpf(X)/q)/sqrt(q)

def U(m):
    if m > X: return mpf(0)
    return sum(mu[k]*w(m*k) for k in range(1, X//m + 1))

def C(N, L):
    return sum(mpf(mu[k])/sqrt(k)*(1 + (L - log(k))/2) for k in range(1, N+1))

def integrand(t):
    N = int(1/t)  # floor
    if abs(1/t - round(1/t)) < mp.mpf(10)**-25: N = int(round(1/t))-0  # knot: measure zero
    return t**mpf(-1.5)*C(N, log(1/t))

print("m, R_raw, R_integral, diff  (m chosen to cross knots: m/X near X/5, X/3, X/7)")
for m in [995, 899, 499, 498, 333, 332, 250, 249, 200, 199, 166, 143, 142, 124, 111, 100, 91, 50, 20]:
    Rraw = U(m) - U(m+1)
    a, b = mpf(m)/X, mpf(m+1)/X
    # split at knots 1/j inside (a,b)
    pts = [a] + [mpf(1)/j for j in range(int(1/b)+1, int(1/a)+1) if a < mpf(1)/j < b] + [b]
    pts = sorted(set(pts))
    Rint = sum(quad(integrand, [pts[i], pts[i+1]]) for i in range(len(pts)-1))/sqrt(X)
    print(f"{m:4d} {float(Rraw):+.12e} {float(Rint):+.12e} {float(abs(Rraw-Rint)):.2e}")

# continuity of scaled U at knots (theta -> 1/k): compare U at integers just left/right of X/k
print("\nknot continuity: U jumps at m near X/k are O(width), no O(1) jump:")
for k in [2,3,5,6,7]:
    mm = X//k
    print(f"k={k}: U({mm})={float(U(mm)):+.6f} U({mm+1})={float(U(mm+1)):+.6f}")
