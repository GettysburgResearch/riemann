import sys, time
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, nstr, pi, sign
from core import Phi, dPhi, Xi, E_j, E_asym

mp.dps = 50
alpha = mpf('1.0'); T = 1/(2*alpha)
print(f"PILOT: alpha=1, T=0.5, mp.dps={mp.dps}")
print(f"Phi(T)={nstr(Phi(T),10)}   Phi'(T)={nstr(dPhi(T,1),10)}   Phi'''(T)={nstr(dPhi(T,3),10)}")
C = 2*abs(dPhi(T,1))/(2*pi*alpha)**2
print(f"predicted asymptotic constant  C = 2|Phi'(T)|/(2 pi alpha)^2 = {nstr(C,12)}   (so |E_j| ~ C/j^2)")
print()
hdr = f"{'j':>3} {'E_j (signed)':>26} {'sign':>5} {'(-1)^j':>7} {'j*|E_j|':>14} {'j^2*|E_j|':>14} {'E_j/E_asym1':>14} {'E_j/E_asym2':>14} {'secs':>7}"
print(hdr); print('-'*len(hdr))
for j in [1,2,3,4,6,8,10,12,16]:
    t0=time.time()
    E = E_j(alpha, j)
    dt=time.time()-t0
    a1 = E_asym(alpha, j, 1); a2 = E_asym(alpha, j, 2)
    print(f"{j:>3} {nstr(E,16):>26} {int(sign(E)):>5} {(-1)**j:>7} {nstr(j*abs(E),8):>14} {nstr(j*j*abs(E),8):>14} {nstr(E/a1,8):>14} {nstr(E/a2,8):>14} {dt:>7.2f}")
