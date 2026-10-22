import sys, time, json
sys.path.insert(0, '/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail')
from mpmath import mp, mpf, nstr, pi, sign, log
from core import Phi, dPhi, Xi, E_j, E_asym

mp.dps = 50
JS = list(range(1, 41))
out = {}
for astr in ['1.0', '0.7', '0.5', '0.4']:
    alpha = mpf(astr); T = 1/(2*alpha)
    C = 2*abs(dPhi(T, 1))/(2*pi*alpha)**2
    print("="*118)
    print(f"alpha={astr}  T={nstr(T,6)}  Phi(T)={nstr(Phi(T),8)}  Phi'(T)={nstr(dPhi(T,1),8)}  "
          f"C := 2|Phi'(T)|/(2 pi alpha)^2 = {nstr(C,10)}")
    print(f"{'j':>3} {'E_j (signed, 14 sig)':>24} {'sgn=(-1)^j?':>12} {'j*|E_j|':>13} {'j^2*|E_j|':>13} "
          f"{'j^2|E_j|/C':>11} {'loc.slope':>10} {'|Xi(2 pi a j)|':>15} {'|E_j|/|Xi_j|':>13}")
    print('-'*118)
    rows = []
    prev = None
    for j in JS:
        t0 = time.time()
        E = E_j(alpha, j)
        X = Xi(2*pi*alpha*j)
        ok = 'yes' if int(sign(E)) == (-1)**j else '** NO **'
        slope = ''
        if prev is not None:
            jp, Ep = prev
            slope = nstr(-(log(abs(E))-log(abs(Ep)))/(log(mpf(j))-log(mpf(jp))), 5)
        rows.append(dict(j=j, E=nstr(E, 20), absE=float(abs(E)), Xi=float(abs(X)),
                         sign_ok=(int(sign(E)) == (-1)**j)))
        print(f"{j:>3} {nstr(E,14):>24} {ok:>12} {nstr(j*abs(E),7):>13} {nstr(j*j*abs(E),7):>13} "
              f"{nstr(j*j*abs(E)/C,7):>11} {slope:>10} {nstr(abs(X),6):>15} {nstr(abs(E)/abs(X),6):>13}")
        prev = (j, E)
    out[astr] = dict(T=nstr(T, 20), Phi_T=nstr(Phi(T), 20), dPhi_T=nstr(dPhi(T, 1), 20),
                     C=nstr(C, 20), rows=rows)
with open('/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail/full.json', 'w') as f:
    json.dump(out, f, indent=1)
print("\nwrote full.json")
