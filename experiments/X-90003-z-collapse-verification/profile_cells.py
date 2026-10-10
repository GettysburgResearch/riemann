"""T-90002 profile verification (Theorem P): per-cell margins, EM tail, c-Lipschitz, driver bracket.

All load-bearing inequalities of T-90002 sec.1 (P1-P4). 30-digit arithmetic; every
reported margin must exceed 1e-3 >> evaluation error. Exit nonzero on any failure.
"""
import mpmath as mp
import sys

mp.mp.dps = 30
OK = True
def check(name, cond, val):
    global OK
    print('%-52s %s  (%s)' % (name, 'PASS' if cond else 'FAIL', mp.nstr(val, 8)))
    OK = OK and cond

S = lambda N: mp.fsum(1/mp.sqrt(k) for k in range(1, N+1))
A = lambda N: mp.fsum(mp.log(k)/mp.sqrt(k) for k in range(1, N+1))
L2 = mp.log(2)

def coef(N):
    Np = N//2
    return (A(N)-A(Np)+4*(S(N)-S(Np))-(S(Np)+1)*L2, S(N)-S(Np), 4*(N-mp.sqrt(2)*Np))
def phiN(N, th):
    al, be, ga = coef(N); return al+be*mp.log(th)-ga*mp.sqrt(th)

# --- P1 cross-check vs raw definition of E ---
def E_raw(th):
    F = mp.fsum((mp.log(k*th)+4)/mp.sqrt(k*th)-4 for k in range(1, int(mp.floor(1/th))+1))
    return F - mp.log(1/th)/mp.sqrt(th)
for tt in ('0.13', '0.2', '0.34', '0.45', '0.071'):
    t = mp.mpf(tt); N = int(mp.floor(1/t))
    d = abs(phiN(N, t) - mp.sqrt(t)*(E_raw(t)-mp.sqrt(2)*E_raw(2*t)))
    check('P1 cell formula at theta=%s' % tt, d < mp.mpf('1e-25'), d)

# --- P3 cells 2..6: suprema negative ---
sup_neg = []
for N in range(2, 7):
    al, be, ga = coef(N)
    tc = (2*be/ga)**2
    lo, hi = mp.mpf(1)/(N+1), mp.mpf(1)/N
    cands = [lo, hi] + ([tc] if lo < tc <= hi else [])
    mx = max(phiN(N, t) for t in cands)
    sup_neg.append(mx)
    check('P3 cell %d sup(phi) < 0' % N, mx < -mp.mpf('0.004'), mx)

# --- P3 cell 7: strict decrease, endpoint signs, slope bound ---
al, be, ga = coef(7)
check('P3 cell7 2b/g < sqrt(1/8)', 2*be/ga < mp.sqrt(mp.mpf(1)/8), mp.sqrt(mp.mpf(1)/8)-2*be/ga)
check('P3 phi(1/8) > 0.0329', phiN(7, mp.mpf(1)/8) > mp.mpf('0.0329'), phiN(7, mp.mpf(1)/8))
check('P3 phi(1/7) < -0.00485', phiN(7, mp.mpf(1)/7) < -mp.mpf('0.00485'), phiN(7, mp.mpf(1)/7))
msl = min(ga/(2*mp.sqrt(t))-be/t for t in (mp.mpf(1)/8, mp.mpf(1)/7))
check('P3 -phi7\' >= 1.7306 on cell', msl >= mp.mpf('1.7305'), msl)
cstar = mp.findroot(lambda t: phiN(7, t), mp.mpf('0.14085'))
check('P3 c* = 0.1408520350138399...', abs(cstar-mp.mpf('0.140852035013839925440958')) < mp.mpf('1e-20'), cstar)

# --- P3 cells 8..17: endpoint minima ---
for N in range(8, 18):
    mn = min(phiN(N, mp.mpf(1)/(N+1)), phiN(N, mp.mpf(1)/N))
    check('P3 cell %d min endpoint > 0.0329' % N, mn > mp.mpf('0.0329'), mn)

# --- P2/P3 tail: Xi(N) <= 0.319093-0.0231 for 18<=N<=400, envelope beyond ---
RS = lambda N: mp.mpf(1)/16/N**mp.mpf('2.5') + mp.mpf(1)/24/N**mp.mpf('1.5')
RA = lambda N: (mp.mpf(1)/12)*((mp.mpf('2.75')+mp.mpf('0.75')*mp.log(N))/N**mp.mpf('2.5')
                               + (mp.mpf('2.1667')+mp.mpf('0.5')*mp.log(N))/N**mp.mpf('1.5'))
D = lambda N: mp.mpf('0.67')/N**mp.mpf('1.5') + RA(N) + RS(N)*(mp.log(N)+4) \
              + mp.mpf('0.5')/N**mp.mpf('1.5') + RS(N)/N
drv_lo = mp.mpf('0.3190934298')   # certified below
mmarg = min(drv_lo - (2/mp.sqrt(N//2)-2/mp.sqrt(N)+D(N)+D(N//2)) for N in range(18, 401))
check('P3 tail margin >= 0.0231 (N=18..400)', mmarg >= mp.mpf('0.0231'), mmarg)
env = 2*mp.sqrt(2)/mp.sqrt(399)-mp.mpf(2)/20+2*D(200)
check('P3 tail envelope N>400 < 0.043', env < mp.mpf('0.043'), env)
# D(N) really dominates |delta_N|: spot check
kappa_num = 4*mp.zeta(mp.mpf('0.5'))-mp.zeta(mp.mpf('0.5'), derivative=1)
a_num = 1+mp.zeta(mp.mpf('0.5'))
for N in (8, 12, 18, 40, 160):
    wrst = mp.mpf(0)
    for j in range(40):
        t = mp.mpf(1)/(N+1) + (mp.mpf(1)/N - mp.mpf(1)/(N+1))*(j+1)/40
        NN = int(mp.floor(1/t)); assert NN == N
        psi = A(N)+(S(N)+1)*mp.log(t)+4*S(N)-4*N*mp.sqrt(t)
        wrst = max(wrst, abs(psi-(a_num*mp.log(t)+kappa_num+2/mp.sqrt(N))))
    check('P2 |delta_%d| <= D' % N, wrst <= D(N), D(N)-wrst)

# --- P4 Lipschitz in c ---
def phic(th, c):
    def E_cell(x):
        N = int(mp.floor(1/x)); return (A(N)+(S(N)+1)*mp.log(x)+4*S(N))/mp.sqrt(x)-4*N
    r = E_cell(th)
    if th <= c: r -= E_cell(th/c)/mp.sqrt(c)
    return mp.sqrt(th)*r
mx = mp.mpf(0)
for c0 in ('0.49', '0.495', '0.4999'):
    c = mp.mpf(c0)
    for j in range(200):
        t = mp.mpf('0.01') + (c-mp.mpf('0.0101'))*j/199
        mx = max(mx, abs(phic(t, c)-phic(t, mp.mpf(1)/2))/(mp.mpf(1)/2-c))
check('P4 c-Lipschitz <= 1.28', mx <= mp.mpf('1.28'), mx)

# --- driver bracket via P2 sigma at N=1e6 ---
N = 10**6
SN = mp.fsum(1/mp.sqrt(k) for k in range(1, N+1))
z_lo = SN-2*mp.sqrt(N)-1/(2*mp.sqrt(N)); z_hi = z_lo+RS(N)
d_lo = -(1+z_hi)*L2; d_hi = -(1+z_lo)*L2
check('driver in [0.3190934298, 0.3190934299]',
      d_lo >= mp.mpf('0.3190934298') and d_hi <= mp.mpf('0.3190934299'), d_lo)

print('\nALL PASS' if OK else '\nFAILURES PRESENT'); sys.exit(0 if OK else 1)
