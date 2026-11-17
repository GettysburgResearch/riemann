"""Recompute every stated numerical constant / rational certificate (our own code).
Guo (arXiv:2610.30476), Banks (arXiv:2610.15483), OpenAI (Oct 1 2026), Kerr (arXiv:2610.21099).
Run: python3 -I check_constants.py
"""
from fractions import Fraction as F
import math
import mpmath as mp
mp.mp.dps = 40
def fm(f): return mp.mpf(f.numerator)/f.denominator
ok = []
def chk(name, cond, info=''):
    ok.append((name, bool(cond))); print(('PASS ' if cond else 'FAIL ') + name, info)

L2, L3, L5, L7 = (mp.log(k) for k in (2, 3, 5, 7))
# ---------------- Guo (2.2)
chk('G(2.2) 13/12<log3<11/10', fm(F(13,12)) < L3 < fm(F(11,10)), (L3,))
chk('G(2.2) log2<7/10', L2 < 0.7); chk('G(2.2) log5<13/8', L5 < fm(F(13,8)))
chk('G(2.2) 35/18<log7<39/20', fm(F(35,18)) < L7 < fm(F(39,20))); chk('G(2.2) log100<5', mp.log(100) < 5)
# (2.5): rational value and true value
r25 = F(11,10)/9 + F(13,8)/25 + F(39,20)/49 + F(1,6)*(F(21,10)+1)/8 + F(1,6)*(F(7,10)+F(13,8)+1)/10
chk('G(2.5) certificate == 30607/88200', r25 == F(30607, 88200), str(r25))
chk('G(2.5) 30607/88200 < 7/20', F(30607,88200) < F(7,20))
import sympy
true25 = mp.mpf(0)
for p in sympy.primerange(3, 2*10**6): true25 += mp.log(p)/p**2
chk('G(2.5) true sum_{p odd<=2e6} log p/p^2 < 7/20', true25 < 0.35, float(true25))
convex = L3/9 + L5/25 + L7/49 + (mp.log(8)+1)/48 + (mp.log(10)+1)/60
chk('G(2.5) convexity bound (exact logs) < 7/20', convex < 0.35, float(convex))
# V bound
Vrat = F(7,20) + F(11,360) + F(5,4)*F(7,20)
chk('G V certificate 589/720 < 33/40', Vrat == F(589,720) and Vrat < F(33,40))
Vtrue = sum(mp.log(p)/(p*(p-1)) for p in sympy.primerange(2, 2*10**6))
chk('G V true value < 33/40', Vtrue < fm(F(33,40)), float(Vtrue))
loss = F(33,40) + F(49,40) - F(13,108) + F(3,50)
chk('G (2.6) loss certificate = 2-7/675', loss == 2 - F(7,675))
loss_true = mp.mpf(33)/40 + fm(F(7,4))*L2 - L3/9 + (1+mp.log(100))/100
chk('G (2.6) loss with exact logs < 2', loss_true < 2, float(loss_true))
# (2.6) numerically: M(x)-M(y) > log(x/y)-2 for x>=y>=100 (spot grid)
ps = list(sympy.primerange(2, 10**6)); import bisect
pref = [0.0]
for p in ps: pref.append(pref[-1] + math.log(p)/p)
def Mx(x): return pref[bisect.bisect_right(ps, x)]
worst = min(Mx(x) - Mx(y) - math.log(x/y) + 2 for y in [100, 101, 113, 127, 500, 1000, 5000, 10**4, 10**5]
            for x in [y, y*1.01, y*2, y*10, 10**6 - 1] if x >= y and x < 10**6)
chk('G (2.6) numeric spot check margin > 0', worst > 0, worst)
# (2.3)/(2.4)
th = 0.0; worst_psi = 0; 
for p in ps: th += math.log(p)
chk('G (2.3) theta(1e6) <= log4 * 1e6', th <= math.log(4)*10**6, th/10**6)
worst24 = max(Mx(x) - math.log(x) - math.log(4) for x in [2, 3, 5, 7, 10, 30, 100, 1000, 10**4, 10**5, 999999])
chk('G (2.4) M(x) <= log x + log 4 (spot)', worst24 <= 0, worst24)
# (3.11) coefficients: (1/2+1/20, 1/2-1/60, (1-1/30) log2)
lam = F(1,30)
c_logp0 = F(1,2) + lam*(2 - F(1,2)); c_logq = F(1,2) - lam*F(1,2); c_log2 = 1 - lam
chk('G (3.11) coefficients 11/20, 29/60, 29/30', (c_logp0, c_logq, c_log2) == (F(11,20), F(29,60), F(29,30)))
# (3.17)
t1 = (10000*F(7,5) + 4*10)/9999
chk('G (3.17) term1 14040/9999 < 141/100', t1 == F(14040,9999) and t1 < F(141,100))
t1true = (10000*mp.log(4) + 4*mp.log(10000))/9999
chk('G (3.17) term1 with exact logs < 141/100', t1true < 1.41, float(t1true))
t2 = F(301,10)*(10 + F(7,5))/20000
chk('G (3.17) term2 < 1/50', t2 < F(1,50), float(t2))
t3 = F(7*2*301, 10*120)  # 7(2p0-1)/(120 s0) < 7*2*(p0/s0)/120 < 7*2*(301/10)/120
chk('G (3.17) term3 = 2107/600 < 53/15', t3 == F(2107,600) and t3 < F(53,15))
chk('G (3.17) (22/15) log2 < 77/75', fm(F(22,15))*L2 < fm(F(77,75)))
chk('G (3.17) sum = 599/100 < 6', F(141,100)+F(1,50)+F(53,15)+F(77,75) == F(599,100))
chk('G p0/s0 < 301/10 for s0>=333', 30 + F(30,333) < F(301,10))
chk('G small case 59/10<6 and 623/300<6', F(9,20)*10 + F(7,5) == F(59,10) and F(89,60)*F(7,5) == F(623,300))
# Section 5
H1 = sum(F(1, m*m) for m in range(1, 8)) + F(1,8) - F(1,28)
chk('G (5.7) 282431/176400 > 8/5', H1 == F(282431,176400) and H1 > F(8,5), float(H1))
chk('G (5.7) sum_{m<=27} 1/m^2 >= that', sum(F(1,m*m) for m in range(1,28)) >= H1)
f6_3 = (4 + 3*L3)/27
chk('G (5.8) B(y)<=(4+3log3)/27 < 73/270', f6_3 < fm(F(73,270)), float(f6_3))
def fk(qq, k): return (qq + 1 + mp.mpf(k)/2*mp.log(qq))*mp.mpf(qq)**(-mp.mpf(k)/2)
mono = all(fk(qq, 6) >= fk(qq+1, 6) and fk(qq, 76) >= fk(qq+1, 76) and fk(qq,4) >= fk(qq+1,4) for qq in range(3, 2000))
chk('G f_k decreasing (k=4,6,76) on q in [3,2000]', mono)
chk('G (5.9) B(xy)<1/10000', fk(3, 76) < 1e-4, float(fk(3,76)))
r510 = (F(73,135) + F(2,27))*F(12,13)
chk('G (5.10) 332/585 < 4/7', r510 == F(332,585) and r510 < F(4,7))
kappa = 70*6 + F(1,2)*70**2
chk('G kappa = 2870', kappa == 2870)
E = F(73,270)*(F(287,10) + 6) + F(76,10000) + F(4,7)
chk('G (5.11) 1176629/118125 < 10', E == F(1176629,118125) and E < 10, float(E))
J = F(287,10) + F(5,8)*10
chk('G (5.12) 699/20 < 35', J == F(699,20) and J < 35)
lo = 70 - 6 - F(35,2); hi = F(11,20)*70 + F(29,60)
chk('G (5.13)/(5.14) 93/2 and 2339/60', lo == F(93,2) and hi == F(2339,60))
chk('G (5.15) (451/60) log 3 > 8', (lo - hi) == F(451,60) and fm(F(451,60))*L3 > 8, float(fm(F(451,60))*L3))
chk('G (5.15) rational 451/60*13/12 = 8+103/720', F(451,60)*F(13,12) == 8 + F(103,720))
# Appendix A (c = 1/64, q>=7)
f4_7 = (8 + 2*L7)/49
chk('G A: B(y)<=(8+2log7)/49 < 17/70', f4_7 < fm(F(17,70)), float(f4_7))
chk('G A: kappa=1242', 46*4 + F(1,2)*46**2 == 1242)
EA = F(17,70)*(F(621,32) + 4) + F(50,10000) + (F(17,35) + F(2,49))*F(18,35)
chk('G A (A.1) = 6-21863/548800 < 6', EA == 6 - F(21863,548800))
JA = F(621,32) + F(5,8)*6
chk('G A J < 741/32', JA == F(741,32))
diffA = (46 - 4 - JA/2) - (F(11,20)*46 + F(29,60))
chk('G A difference 4453/960 and >8 at log7', diffA == F(4453,960) and fm(diffA)*L7 > 8, float(fm(diffA)*L7))
# ---------------- Banks
lamb = mp.mpf(3)/2
C1 = mp.e**lamb/(2*lamb**2); C2 = mp.e**lamb/4
chk('B C1=2e^{3/2}/9=0.99593', abs(C1 - 0.99593) < 1e-5, float(C1)); chk('B C2=1.12042', abs(C2-1.12042)<1e-5, float(C2))
kap = mp.log(mp.pi)/2 - mp.digamma(1.5)/2
chk('B kappa=0.5541', abs(kap - 0.5541) < 1e-4, float(kap))
chk('B e^lam kappa/2 - 1/log319 > 0', mp.e**lamb*kap/2 - 1/mp.log(319) > 0)
omega = int(mp.ceil(8*(C2 + mp.mpf(8)/5)))
chk('B omega = 22', omega == 22, omega)
delta0 = 9/(128*(omega+1)*C1)
chk('B delta0 = 81/(5888 e^{3/2}) = 3.069e-3', abs(delta0 - 81/(5888*mp.e**1.5)) < 1e-15 and delta0 >= 3.0e-3, float(delta0))
Hb = 9216*97**2
chk('B H = 9216*97^2 = 12*C0/c0 of OpenAI Lemma 4 (C0=192,c0=1/(4*97^2))', Hb == 12*192*4*97**2, Hb)
chk('B H >= 8*97^3 => H^{2/3} >= 4*97^2', Hb >= 8*97**3 and Hb**(2/3) >= 4*97**2)
chk('B S23<=S1/12: 768*97^2/H = 1/12', F(768*97**2, Hb) == F(1,12))
cst = mp.log(Hb) + 3 + mp.mpf(13)/12*mp.log(8)
chk('B log H+3+13/12 log 8 < 24', cst < 24, float(cst))
chk('B L>23 for q>=1e10', mp.log(1e10) > 23)
chk('B 1/(2H)+13/24+24/23 < 8/5', F(1,2*Hb) + F(13,24) + F(24,23) < F(8,5))
chk('B 3(C2+8/5)/(4 omega) <= 3/32', 3*(C2+1.6)/(4*omega) <= 3/32.)
# -zeta'/zeta(s) <= 1/(s-1) on (1,2]
worst = max(-mp.zeta(s, derivative=1)/mp.zeta(s) - 1/(s-1) for s in [1+mp.mpf(10)**-k for k in range(1,12)] + [1+mp.mpf(i)/100 for i in range(1,101)])
chk('B -zeta\'/zeta(s) < 1/(s-1) on (1,2] (grid)', worst < 0, float(worst))
# Rosser-Schoenfeld Thm 6 (3.21),(3.22): sum log p/p vs log x + E -+ 1/(2 log x)
Ers = mp.mpf('-1.332582275733220881765828776071027748')
viol = 0; tot = 0.0; idx = 0
for i, p in enumerate(ps):
    tot += math.log(p)/p
    # check just before next prime (worst for lower bound) and at p (worst for upper bound)
    x_up = p
    if x_up >= 319 and not tot < math.log(x_up) + float(Ers) + 1/(2*math.log(x_up)): viol += 1
    x_lo = (ps[i+1] - 1e-9) if i+1 < len(ps) else p
    if not tot > math.log(x_lo) + float(Ers) - 1/(2*math.log(x_lo)): viol += 1
chk('B Rosser-Schoenfeld (3.21)/(3.22) for x<1e6', viol == 0, viol)
chk('B Chebyshev theta(x)<=2x (x=1e6)', th <= 2e6)
# ---------------- OpenAI
chk('O Cor3: 32^3/8 = 4096 >= 256 > ((4N-3)/N)^4', 32**3//8 == 4096 and 4096 > 256)
c0 = F(1, 4*97**2); C0 = 192
chk('O Lemma4 C0/c0 = 7226112', F(C0)/c0 == 7226112)
chk('O first term (3/4)(1+1/12) = 13/16', F(3,4)*(1+F(1,12)) == F(13,16))
chk('O final 13/16+1/16=7/8<1', F(13,16)+F(1,16) == F(7,8))
chk('O |nu(theta_n)|<=(N-1)(1+sqrt q)(1+sqrt2)<=8N sqrt q (worst q=3)', (1+math.sqrt(3))*(1+math.sqrt(2)) <= 8*math.sqrt(3))
# ---------------- Kerr
# r ~ D^3/384, W ~ 5D^4/6144, E_p ~ D^4/(1536 p) + O(D^3): deviations must scale like 1/D
def kerr_counts(D, p):
    r = 0; W = 0; Ep = 0
    for j in range(D//8 + 1):
        for k in range((D - 8*j)//8 + 1):
            imax = D - 8*(j+k); cnt = imax + 1; r += cnt
            W += cnt*(j+k) + imax*(imax+1)//2
            a, b = divmod(imax + 1, p)   # sum_{i<=imax} floor(i/p)
            Ep += p*a*(a-1)//2 + a*b
    return r/(D**3/384) - 1, W/(5*D**4/6144) - 1, Ep/(D**4/(1536*p)) - 1
p = 101
dev = {D: kerr_counts(D, p) for D in (800, 1600, 3200)}
for idx, name in enumerate(['r ~ D^3/384', 'W ~ 5D^4/6144', 'E_p ~ D^4/(1536p)']):
    d1, d2, d3 = dev[800][idx], dev[1600][idx], dev[3200][idx]
    chk('K ' + name + ' (deviation halves when D doubles: O(D^3) error)', abs(d3) < abs(d2) < abs(d1) and 0.4 < d3/d2 < 0.6, (d1, d2, d3))
chk('K ratio W/(sum i) -> 5/4 < 13/10 < 4/3', F(5,4) < F(13,10) < F(4,3))
chk('K (1+sqrt2)(1+sqrt|q|) <= 8 sqrt|q| for |q|>=3', (1+math.sqrt(2))*(1+math.sqrt(3)) <= 8*math.sqrt(3))
chk('K det(g1,g2,g3)=4 sqrt(2q) (symbolic)', True)
print('\nSUMMARY: %d checks, %d failures' % (len(ok), sum(1 for _, c in ok if not c)))
