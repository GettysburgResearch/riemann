"""Discriminating test.  L-16005(iii) says the first IBP boundary term
-Phi(T) sin(omega T)/omega is 'genuinely present'.  It IS present in general --
but on the hard-window lattice omega_j T = 2 pi alpha j * 1/(2 alpha) = pi j, so
sin(omega_j T) = 0 identically.  Move T off the lattice and O(1/j) must reappear.
"""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, pi, sin, cos, nstr
from core import Phi, dPhi, E_j

mp.dps = 40
alpha = mpf('1.0')
print("alpha = 1, frequency omega_j = 2 pi j.  Vary the cutoff T.")
print()
for Tstr in ['0.5', '0.55', '0.625', '0.7']:
    T = mpf(Tstr)
    onlat = (2*pi*alpha*T/pi)
    print(f"--- T = {Tstr}   (omega_j T / pi = {nstr(onlat,6)} * j;  "
          f"{'ON lattice: sin = 0 always' if onlat == int(onlat) else 'OFF lattice'})")
    print(f"    Phi(T)={nstr(Phi(T),8)}  Phi'(T)={nstr(dPhi(T,1),8)}")
    print(f"{'j':>4} {'E_j':>22} {'j*|E_j|':>13} {'j^2*|E_j|':>13} {'pred 1st-order':>18} {'pred 2nd-order':>18}")
    for j in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]:
        w = 2*pi*alpha*j
        E = E_j(alpha, j, T=T)
        p1 = -2*Phi(T)*sin(w*T)/w                      # first boundary term only
        p2 = p1 - 2*dPhi(T, 1)*cos(w*T)/w**2           # + second boundary term
        print(f"{j:>4} {nstr(E,14):>22} {nstr(j*abs(E),7):>13} {nstr(j*j*abs(E),7):>13} "
              f"{nstr(p1,8):>18} {nstr(p2,8):>18}")
    print()
