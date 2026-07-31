"""Independent cross-checks of E_j.

Route A (primary): direct tail quadrature 2 int_T^inf Phi cos(w t) dt, half-period panels.
Route B (independent): E_j = Xi(2 pi alpha j) - F,  F = 2 int_0^T Phi cos(w t) dt.
        Route B never touches the tail; it uses mpmath's zeta/gamma for Xi.
Also: precision robustness (dps 50/maxdeg 6  vs  dps 90/maxdeg 9).
"""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, pi, cos, quad, nstr
from core import Phi, dPhi, Xi, E_j, tail_cutoff


def F_head(alpha, j, maxdegree=6):
    alpha = mpf(alpha); T = 1/(2*alpha); w = 2*pi*alpha*j
    pts = [mpf(0)]
    k = 0
    while True:
        tk = (pi/2 + k*pi)/w
        if tk >= T:
            break
        pts.append(tk); k += 1
    pts.append(T)
    return 2*sum(quad(lambda t: Phi(t)*cos(w*t), [a, b], maxdegree=maxdegree)
                 for a, b in zip(pts[:-1], pts[1:]))


cases = [('1.0', 1), ('1.0', 4), ('1.0', 10), ('1.0', 25), ('1.0', 40),
         ('0.7', 10), ('0.7', 40), ('0.5', 10), ('0.5', 40), ('0.4', 10), ('0.4', 40)]

print("ROUTE A (tail quad) vs ROUTE B (Xi - head quad)   [dps=50]")
print(f"{'alpha':>6} {'j':>3} {'E_j route A':>26} {'E_j route B':>26} {'rel diff':>12}")
print('-'*80)
mp.dps = 50
resA = {}
for astr, j in cases:
    a = mpf(astr)
    EA = E_j(a, j)
    EB = Xi(2*pi*a*j) - F_head(a, j)
    resA[(astr, j)] = EA
    rd = abs(EA-EB)/abs(EA)
    print(f"{astr:>6} {j:>3} {nstr(EA,18):>26} {nstr(EB,18):>26} {nstr(rd,4):>12}")

print()
print("PRECISION ROBUSTNESS: dps=50/maxdeg=6  vs  dps=90/maxdeg=9")
print(f"{'alpha':>6} {'j':>3} {'rel diff':>12}")
print('-'*26)
mp.dps = 90
for astr, j in cases:
    a = mpf(astr)
    Ehi = E_j(a, j, maxdegree=9)
    rd = abs(Ehi - resA[(astr, j)])/abs(Ehi)
    print(f"{astr:>6} {j:>3} {nstr(rd,4):>12}")
