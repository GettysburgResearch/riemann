"""Adversarial re-derivation of T-90001 Section 2 (Moat Lemma chain)."""
import sympy as sp
from mpmath import mp, mpf, log, sqrt, quad
mp.dps = 40

th, u = sp.symbols('theta u', positive=True)
N = sp.symbols('N', positive=True, integer=True)

def g_expr(x):
    return (sp.log(x) + 4)/sp.sqrt(x) - 4

# ---------- (a) cell formula ----------
# F(th) = sum_{k=1}^N g(k th) on 1/(N+1) < th <= 1/N (floor(1/th)=N there)
k = sp.symbols('k', positive=True, integer=True)
SN, AN = sp.symbols('S_N A_N')  # S_N = sum k^{-1/2}, A_N = sum k^{-1/2} log k
# symbolic: g(k th) = (log k + log th + 4)/sqrt(k th) - 4
# sum -> th^{-1/2}(A_N + S_N log th + 4 S_N) - 4N ; E = F + th^{-1/2} log th
E_claimed = th**sp.Rational(-1,2)*(AN + (SN+1)*sp.log(th) + 4*SN) - 4*N

# numeric check of cell formula vs raw definition at random points, high precision
import random
random.seed(7)
def SnAn(n):
    S = sum(mpf(j)**mpf('-0.5') for j in range(1, n+1))
    A = sum(mpf(j)**mpf('-0.5')*log(j) for j in range(1, n+1))
    return S, A
def E_raw(t):
    n = int(mp.floor(1/t))
    return sum((log(j*t)+4)/sqrt(j*t) - 4 for j in range(1, n+1)) - log(1/t)/sqrt(t)
def E_cell(t):
    n = int(mp.floor(1/t))
    S, A = SnAn(n)
    return (A + (S+1)*log(t) + 4*S)/sqrt(t) - 4*n
maxerr = mpf(0)
for _ in range(60):
    n = random.randint(1, 200)
    t = mpf(1)/(n+1) + (mpf(1)/n - mpf(1)/(n+1))*mpf(random.random())
    maxerr = max(maxerr, abs(E_raw(t) - E_cell(t)))
print("(a) max |E_raw - E_cell| over 60 random pts N<=200:", mp.nstr(maxerr, 3))

# ---------- (b) continuity at knots ----------
print("(b) g(1) =", sp.simplify(g_expr(sp.Integer(1))))
# jump at th=1/N between cell N (left-inclusive at 1/N) and cell N-1:
Sm, Am = sp.symbols('S_m A_m')  # S_{N-1}, A_{N-1}
E_N   = th**sp.Rational(-1,2)*(AN + (SN+1)*sp.log(th) + 4*SN) - 4*N
E_Nm1 = th**sp.Rational(-1,2)*(Am + (Sm+1)*sp.log(th) + 4*Sm) - 4*(N-1)
jumpE = (E_N - E_Nm1).subs({AN: Am + sp.log(N)/sp.sqrt(N), SN: Sm + 1/sp.sqrt(N), th: sp.Rational(1,1)/N})
print("(b) E jump at th=1/N (symbolic):", sp.simplify(jumpE))

# ---------- (c) antiderivative, H closed form, J' identity, knot continuity ----------
# Claimed-implied closed form (derived by me): H(th) = -2 sqrt(th)[A_N+(S_N+1)log th+2S_N-2] + 4N th - 4
H_closed = -2*sp.sqrt(th)*(AN + (SN+1)*sp.log(th) + 2*SN - 2) + 4*N*th - 4
# check H' = -E on the cell
print("(c1) H' + E simplifies to:", sp.simplify(sp.diff(H_closed, th) + E_N))
# check H(1)=0 with N=1, S_1=1, A_1=0
print("(c2) H(1) with N=1:", sp.simplify(H_closed.subs({N:1, SN:1, AN:0, th:1})))
# knot continuity of H at th=1/N: cell N minus cell N-1
H_Nm1 = -2*sp.sqrt(th)*(Am + (Sm+1)*sp.log(th) + 2*Sm - 2) + 4*(N-1)*th - 4
jumpH = (H_closed - H_Nm1).subs({AN: Am + sp.log(N)/sp.sqrt(N), SN: Sm + 1/sp.sqrt(N), th: sp.Integer(1)/N})
print("(c3) H jump at th=1/N (symbolic):", sp.simplify(jumpH))
# J = H/sqrt(th); J' claimed = 2 th^{-3/2}[N th + 1 - (S_N+1) sqrt(th)]
J = H_closed/sp.sqrt(th)
Jp = sp.simplify(sp.diff(J, th))
Jp_claim = 2*th**sp.Rational(-3,2)*(N*th + 1 - (SN+1)*sp.sqrt(th))
print("(c4) J' - claimed:", sp.simplify(Jp - Jp_claim))
# lower bound: N th + 1 - (S_N+1) sqrt(th) - (sqrt(N th)-1)^2 = (2 sqrt(N) - 1 - S_N) sqrt(th)
diff_lb = sp.expand(N*th + 1 - (SN+1)*sp.sqrt(th) - (sp.sqrt(N*th)-1)**2)
print("(c5) middle-inequality slack:", sp.simplify(diff_lb))

# numeric: H closed form vs direct quadrature of raw E, incl across many cells
def H_num_closed(t):
    n = int(mp.floor(1/t))
    S, A = SnAn(n)
    return -2*sqrt(t)*(A + (S+1)*log(t) + 2*S - 2) + 4*n*t - 4
def H_num_quad(t):
    # integrate raw E from t to 1, splitting at knots
    n = int(mp.floor(1/t))
    pts = [t] + [mpf(1)/j for j in range(n, 0, -1)]
    tot = mpf(0)
    for a, b in zip(pts, pts[1:]):
        if b > a:
            tot += quad(E_raw, [a, b])
    return tot
for t in [mpf('0.9'), mpf('0.35'), mpf('0.141'), mpf('0.06'), mpf('0.013')]:
    print("(c6) t=%s  H_closed=%s  |closed-quad|=%s" % (
        mp.nstr(t,4), mp.nstr(H_num_closed(t),10), mp.nstr(abs(H_num_closed(t)-H_num_quad(t)),3)))
# J continuity at knots numerically (left/right limits)
eps = mpf('1e-25')
maxJjump = mpf(0)
for n in range(2, 60):
    tk = mpf(1)/n
    Jl = H_num_closed(tk)/sqrt(tk)                    # cell N=n value AT the knot (left-inclusive)
    Jr = H_num_closed(tk+eps)/sqrt(tk+eps)            # just above: cell N=n-1
    maxJjump = max(maxJjump, abs(Jl-Jr))
print("(c7) max |J right-limit - J value| at knots 1/N, N=2..59:", mp.nstr(maxJjump,3))

# ---------- (d) S_N <= 2 sqrt(N) - 1 ----------
bad = [n for n in range(1, 5001) if SnAn(n)[0] > 2*sqrt(n)-1 + mpf('1e-30')]
print("(d) violations N<=5000:", bad, "; induction step: 2(sqrt(N)-sqrt(N-1)) - N^{-1/2} >= 0 <=> sqrt(N)+sqrt(N-1) <= 2 sqrt(N): trivially true")

# ---------- (e) two-scale change of variables, numeric spot check ----------
def Hc_direct(t, c):
    # integrate E_c(u) = E(u) - c^{-1/2} E(u/c) 1_{u<=c} from t to 1 by quadrature
    def Ec(x):
        v = E_raw(x)
        if x <= c:
            v -= E_raw(x/c)/sqrt(c)
        return v
    # split at knots of E(u) and of E(u/c) and at c
    n = int(mp.floor(1/t))
    pts = set([t, mpf(1), c])
    for j in range(1, n+2):
        if t < mpf(1)/j < 1: pts.add(mpf(1)/j)
        if t < c/j < 1: pts.add(c/j)
    pts = sorted(p for p in pts if t <= p <= 1)
    return sum(quad(Ec, [a,b]) for a,b in zip(pts, pts[1:]))
def Hc_formula(t, c):
    if t > c: return H_num_closed(t)
    return H_num_closed(t) - sqrt(c)*H_num_closed(t/c)
for c in [mpf(1)/3, mpf('0.4'), mpf('0.5')]:
    for t in [mpf('0.07'), mpf('0.141'), c*mpf('0.999'), c, min(mpf('0.7'), mpf('0.99'))]:
        d = abs(Hc_direct(t,c) - Hc_formula(t,c))
        print("(e) c=%s t=%s |direct-formula|=%s" % (mp.nstr(c,4), mp.nstr(t,4), mp.nstr(d,3)))
