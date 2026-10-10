"""T3 redo in mpmath: Xi-like truncated product + planted pair, high-precision roots."""
from mpmath import mp, zetazero, mpf, mpc, polyroots
mp.dps = 60
gam = [zetazero(n).imag for n in range(1, 31)]
# Build poly coeffs (ascending in t^2 blocks) exactly in mp: F(t) = prod (1 - t^2/g^2) * pair quartic
# Represent as coefficient list in t (descending), start [1]
coeffs = [mpf(1)]
def mul(c1, c2):
    out = [mpf(0)]*(len(c1)+len(c2)-1)
    for i, a in enumerate(c1):
        for j, b in enumerate(c2):
            out[i+j] += a*b
    return out
for g in gam:
    coeffs = mul(coeffs, [-1/(g*g), mpf(0), mpf(1)])   # -t^2/g^2 ... descending [-1/g^2, 0, 1]
xp, yp = mpf(25), mpf('0.4')
zp2 = (mpc(xp, yp))**2
q1 = [-1/zp2, mpc(0), mpc(1)]
q2 = [-1/zp2.conjugate(), mpc(0), mpc(1)]
q = mul(q1, q2)
q = [c.real for c in q]  # real quartic
F = mul(coeffs, q)
# derivative (descending coeffs)
n = len(F) - 1
dF = [F[i]*(n - i) for i in range(n)]
rts = polyroots(dF, maxsteps=200, extraprec=200)
prs = [(xp, yp), (-xp, yp)]
bad = 0; found = 0; margins = []
for w in rts:
    if abs(w.imag) > mpf('1e-25'):
        found += 1
        m = max(y*y - w.imag**2 - (w.real - x)**2 for (x, y) in prs)
        margins.append((w, m))
        if m <= 0:
            bad += 1
            print("VIOLATION:", w, m)
print(f"T3(mp): nonreal deriv zeros={found}, violations={bad}")
for w, m in margins:
    print(f"  w=({mp.nstr(w.real,8)},{mp.nstr(w.imag,6)}) margin={mp.nstr(m,6)}")
