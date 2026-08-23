# B1 census_check.py — cross-checks against X-105061 (T0=500 census) + refined Sum w_k.
import json, mpmath as mp
mp.mp.dps = 30
base = '/home/user/riemann/experiments/X-105061-xi-derivative-census/'
res = json.load(open(base + 'results.json'))
z   = json.load(open(base + 'zeros.json'))

print("== census: real-zero counts and pair evidence (T0=500) ==")
for k in ['k0','k1','k2','k3']:
    zz = [mp.mpf(s) for s in res['per_k'][k]['zeros']]
    n  = res['per_k'][k]['count']
    gaps = [float(b-a) for a,b in zip(zz, zz[1:])]
    print(f"{k}: count={n} listed={len(zz)} maxgap={max(gaps):.3f} mingap={min(gaps):.3f}")
print("keys per_k extra:", {k: [x for x in res['per_k'][k] if x!='zeros'] for k in ['k0']})
print("top-level keys:", [x for x in res if x != 'per_k'])
# Non-real pairs observed? (census claim: none; W_k(500)=0, all gaps C-0, D_res=0 below 500)
led = json.load(open(base + 'ledger.json'))
print("ledger keys:", list(led.keys())[:10] if isinstance(led, dict) else ('list', len(led)))
s = json.dumps(led)
print("ledger mentions 'pair':", s.count('pair'), " 'defect':", s.count('defect'), " 'X_0':", s.count('X_0'))

print("\n== refined Sum w_k with per-rung c_k (W6: w_k <= (3/(2 c_k)) (1-c_k)) ==")
Z23 = mp.mpf('0.6725007036794117')
alpha = {0: mp.mpf('0.3658'), 1: mp.mpf('0.8137'), 2: mp.mpf('0.9584'),
         3: mp.mpf('0.9873'), 4: mp.mpf('0.9948'), 5: mp.mpf('0.9970')}
def wbound(c): return (3/(2*c))*(1-c)
# variant A: with Z23 import (c_k = max(Z23, alpha_k)); variant B: import-free (pure Conrey/Levinson)
for name, c0 in [("A (Z23 import, mod upstream review)", Z23), ("B (import-free, Conrey alpha_0=0.3658)", alpha[0])]:
    head = wbound(c0) + sum(wbound(max(alpha[k], Z23 if name.startswith('A') else 0)) for k in range(1,6))
    # k>=6: c_k >= 1 - 1/k^2 (Conrey printed log F_m(1) <= m^-2; machine-checked each m, m^2 logF < 0.524)
    tailC1   = mp.mpf(3)/2 * mp.nsum(lambda k: (1/(k**2))/(1-1/k**2), [6, mp.inf])   # C=1
    tailC524 = mp.mpf(3)/2 * mp.nsum(lambda k: (mp.mpf('0.524')/k**2)/(1-mp.mpf('0.524')/k**2), [6, mp.inf])
    print(f"variant {name}: head(k<=5)={mp.nstr(head,6)}  tail(C=1)={mp.nstr(tailC1,6)}"
          f"  tail(C=0.524)={mp.nstr(tailC524,6)}")
    print(f"   => Sum_k w_k <= {mp.nstr(head+tailC1,6)} (C=1)   <= {mp.nstr(head+tailC524,6)} (C=0.524 machine)")
print("check telescoping Sum_{k>=6} 1/(k^2-1) = (1/2)(1/5+1/6) =", mp.nstr((mp.mpf(1)/5+mp.mpf(1)/6)/2,6))

print("\n== Conrey asymptote refinement: m^2 log F_m(1) -> pi/6? ==")
def conrey_F(m):
    mp.mp.dps = 40
    psi  = lambda x: (1-x)*(1-2*x)**m
    dpsi = lambda x: -(1-2*x)**(m-1)*((2*m+1)-(2*m+2)*x)
    Phi  = mp.quad(lambda x: mp.e**(2*x)*psi(x)**2,  [0, mp.mpf(1)/2, 1])
    Phip = mp.quad(lambda x: mp.e**(2*x)*dpsi(x)**2, [0, mp.mpf(1)/2, 1])
    Lam  = mp.sqrt((Phip - 1 - Phi)/(4*Phi))
    F    = mp.mpf(1)/2 + 2*Phi*Lam*mp.coth(Lam)
    return None, None, F, mp.log(F)
for m in [2000, 4000]:
    _,_,_, lf = conrey_F(m)
    print(f"m={m}: m^2 logF = {mp.nstr(m**2*lf, 10)}   pi/6 = {mp.nstr(mp.pi/6, 10)}")
