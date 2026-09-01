# Function-field control experiment: over F_q[T] the Riemann hypothesis for L(u,chi) is Weil's theorem.
# We build the exact analogue of the repository's cumulative Mobius detector
#     D(n) = sum_{deg f <= n} mu(f) chi(f) q^{-deg f / 2}
# for quadratic characters chi mod an irreducible Q of degree d (chi(f) = f^{(q^d-1)/2} mod Q),
# and ask whether "D(n) >= 0 for all large n" holds.  RH is TRUE for every such L-function.
import itertools, numpy as np, sys
q = int(sys.argv[1]); dmax = int(sys.argv[2]); NMAX = int(sys.argv[3]) if len(sys.argv)>3 else 20000
def pmul(a, b):
    r = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b): r[i+j] = (r[i+j] + x*y) % q
    return r
def pmod(a, m):  # m monic
    a = a[:]
    while len(a) >= len(m):
        c = a[-1]
        if c:
            for i in range(len(m)): a[len(a)-len(m)+i] = (a[len(a)-len(m)+i] - c*m[i]) % q
        a.pop()
    while len(a) > 1 and a[-1] == 0: a.pop()
    return a
def ppow(a, e, m):
    r = [1]; a = pmod(a, m)
    while e:
        if e & 1: r = pmod(pmul(r, a), m)
        a = pmod(pmul(a, a), m); e >>= 1
    return r
def monics(n):  # monic polys of degree n, low->high coeffs
    for c in itertools.product(range(q), repeat=n): yield list(c) + [1]
def is_irred(f):
    n = len(f)-1
    for k in range(1, n//2+1):
        for g in monics(k):
            if pmod(f, g) == [0]: return False
    return True
rows = []
for d in range(2, dmax+1):
    irr = [f for f in monics(d) if is_irred(f)]
    for Q in irr:
        e = (q**d - 1)//2
        L = []
        for n in range(d):   # L(u,chi) = sum_{n<d} (sum_{deg f = n} chi(f)) u^n
            s = 0
            for f in monics(n):
                r = ppow(f, e, Q)
                s += 1 if r == [1] else (-1 if r == [q-1] else 0)
            L.append(s)
        L = np.array(L, dtype=float)
        # reciprocal roots alpha_j of L(u): Weil says |alpha_j| = sqrt(q) (or a trivial root 1 for even chi)
        rr = np.roots(L[::-1]) if len(L) > 1 else np.array([])
        rr = 1.0/rr if len(rr) else rr
        # detector generating function: sum_n D(n) u^n = 1/((1-u) L(u/sqrt q))
        # coefficients of 1/L(u/sqrt q): recurrence
        Ls = L * q**(-np.arange(d)/2)
        a = np.zeros(NMAX+1); a[0] = 1.0/Ls[0]
        for n in range(1, NMAX+1):
            a[n] = -sum(Ls[k]*a[n-k] for k in range(1, min(d-1, n)+1))/Ls[0]
        D = np.cumsum(a)
        A = 1.0/np.polyval(Ls[::-1], 1.0)         # main term (residue at u=1)
        # unit-circle poles u_j = sqrt(q)/alpha_j and residues B_j
        uj = np.sqrt(q)/rr
        unit = np.abs(np.abs(uj)-1) < 1e-6
        B = []
        for j in np.where(unit)[0]:
            others = np.prod([1 - uj[j]/uj[i] for i in range(len(uj)) if i != j]) if len(uj) > 1 else 1.0
            B.append(1.0/((1-uj[j])*others))
        amp = float(np.sum(np.abs(B)))
        rows.append((d, Q, L.astype(int).tolist(), np.abs(rr).round(6).tolist(), A, amp, D[50:].min(), D[50:].max(), int((D[50:]<0).sum())))
print("q=%d; quadratic characters mod irreducible Q of degree d; detector D(n)=sum_{deg f<=n} mu(f)chi(f) q^{-deg f/2}" % q)
print("Weil RH holds for all rows.  A = main term 1/L(q^{-1/2},chi); amp = sum |B_j| over unit-circle poles;")
print("min/max over 50<=n<=%d; neg = number of n in that range with D(n)<0" % NMAX)
print("%3s %-14s %-24s %-26s %9s %9s %9s %9s %6s" % ("d","Q(low->high)","L(u,chi) coeffs","|alpha_j| (sqrt q=%.4f)" % q**0.5,"A","amp","min D","max D","neg"))
for d,Q,L,ab,A,amp,mn,mx,neg in rows:
    print("%3d %-14s %-24s %-26s %9.4f %9.4f %9.4f %9.4f %6d" % (d, "".join(map(str,Q)), str(L), str(ab), A, amp, mn, mx, neg))
tot = len(rows); evneg = sum(1 for r in rows if r[8] > 0)
print("\ncharacters: %d ; detector negative infinitely often (observed) : %d ; eventually nonnegative (observed): %d" % (tot, evneg, tot-evneg))
