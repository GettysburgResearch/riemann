"""T-90002 discrete verification: exact s_X(q) signs, window, identity (Thm Q), floor ratio.

Usage: python3 discrete_check.py [X ...]   (default: 100001 199999 200000)
"""
import numpy as np, math, sys
import mpmath as mp
mp.mp.dps = 25

CSTAR = 0.140852035013839925
W = 52

def vq_all(X):
    m = np.arange(0, X+2, dtype=np.float64)
    b = np.zeros(X+2); mm = m[2:X+1]
    b[2:X+1] = 2*np.sqrt(mm)*(np.log(X/mm) - 2*(1-np.sqrt(mm/X)))
    Db = b[:-1]-b[1:]
    v = np.zeros(X+1)
    for d in range(2, X+1):
        v[d] = Db[d::d].sum()
    return v

Sfun = lambda N: mp.fsum(1/mp.sqrt(k) for k in range(1, N+1))
Afun = lambda N: mp.fsum(mp.log(k)/mp.sqrt(k) for k in range(1, N+1))
def E_cell(th):
    N = int(mp.floor(1/th))
    return (Afun(N)+(Sfun(N)+1)*mp.log(th)+4*Sfun(N))/mp.sqrt(th)-4*N
def Ec(th, c):
    r = E_cell(th)
    if th <= c: r -= E_cell(th/c)/mp.sqrt(c)
    return r

def run(X):
    Y = X//2; L = math.log(X/Y)
    vX, vY = vq_all(X), vq_all(Y)
    q = np.arange(2, Y+1, dtype=np.float64)
    s = (vX[2:Y+1]-np.log(X/q)/np.sqrt(q)) - (vY[2:Y+1]-np.log(Y/q)/np.sqrt(q))
    qi = q.astype(int); thr = CSTAR*X
    flips = qi[:-1][np.sign(s[:-1]) != np.sign(s[1:])]
    below = qi < thr-W; above = qi > thr+W
    exc = list(qi[below & (s <= 0)]) + list(qi[above & (s >= 0)])
    print('X=%d  sign flips at %s (thr=%.2f)  exceptions outside +-%d window: %s'
          % (X, list(flips), thr, W, exc if exc else 'NONE'))
    # Theorem Q lower bound on q <= X/110
    sm = qi <= X//110
    lb = 0.319093/np.sqrt(q[sm]) - 3.22/math.sqrt(X)
    print('   ThmQ slack min over q<=X/110: %.6f (>0 required)' % (s[sm]-lb).min())
    # identity spot checks (exact, incl q|Y correction)
    bz = lambda m, Z: (2*math.sqrt(m)*(math.log(Z/m)-2*(1-math.sqrt(m/Z))) if 2 <= m <= Z else 0.0)
    for qq in (2, 3, 7, 101):
        if qq > Y//2: continue
        KY, KX = Y//qq, X//qq
        t1 = -2*L*sum(math.sqrt(k*qq+1)-math.sqrt(k*qq) for k in range(1, KY+1))
        t2 = 4*KY*(Y**-0.5-X**-0.5)
        t3 = sum(bz(k*qq, X)-bz(k*qq+1, X) for k in range(KY+1, KX+1))
        beta = 0.0
        if Y % qq == 0:
            beta = 2*math.sqrt(Y+1)*(2*(math.sqrt(1+1/Y)-1)-math.log(1+1/Y))
        ident = t1+t2+t3-L/math.sqrt(qq)-beta
        print('   identity q=%d: |ident-s| = %.2e' % (qq, abs(ident-s[qq-2])))
    # floor-bound ratio on a sample
    z32 = float(mp.zeta(mp.mpf('1.5'))); c = mp.mpf(Y)/X
    worst = 0.0
    for i in np.linspace(0, len(qi)-1, 200).astype(int):
        qq = int(qi[i])
        prof = float(Ec(mp.mpf(qq)/X, c))/math.sqrt(X)
        worst = max(worst, abs(s[i]-prof)/(z32*qq**-1.5*(2+math.log(X/qq))))
    print('   floor-bound ratio max = %.3f (<1 required)' % worst)

if __name__ == '__main__':
    for X in ([int(a) for a in sys.argv[1:]] or [100001, 199999, 200000]):
        run(X)
