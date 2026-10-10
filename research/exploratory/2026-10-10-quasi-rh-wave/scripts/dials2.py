import numpy as np
def Rstar(delta, x, alpha=5/6, c=2/9, sM=1/2, ideal=False):
    if ideal: return 1 - delta + 0*x
    aI0, aI1 = 2*x*sM, 1 - 2*x*sM
    s0, s1 = 2*x*c, (2 - 4*x*c)
    # Rshort(t) = 1 - delta(aI0 + aI1 r*(t)),  r*(t) = (s0 + s1 t - aI0)/(aI1+s1)  (affine in t, decreasing R)
    # L(t) = 1 - delta + (alpha-delta)(t-1) increasing. Crossing:
    # delta(aI0 + aI1 r*(t)) = delta - (alpha-delta)(t-1)
    A = delta*aI1*s1/(aI1+s1); Bc = delta*(aI0 + aI1*(s0 - aI0)/(aI1+s1))
    # delta(aI0+aI1 r*) = Bc + A t ; L: 1 - delta + (alpha-delta)(t-1)
    # 1 - (Bc + A t) = 1 - delta + (alpha-delta)(t-1)  ->  -Bc - A t = -delta + (alpha-delta) t - (alpha-delta)
    t = (delta - Bc + (alpha - delta))/(A + (alpha - delta) + 1e-300)
    t = np.clip(t, 1, 1.5)
    Rs = 1 - (Bc + A*t); L = 1 - delta + (alpha-delta)*(t-1)
    return np.maximum(Rs, L)
def E(b, ell, delta, x, floor_save=0.0, **kw):
    C0 = -1/4 + 5*ell/4 + b/6
    h = (1 + b + 3*ell)/2
    return C0 - floor_save*h + delta*(1/2 + ell) + x*delta*ell - h*(1 - Rstar(delta, x, **kw))
ds = np.linspace(0, 5/6, 121); xs = np.linspace(0, 1/2, 121); D, X = np.meshgrid(ds, xs, indexing='ij')
def Emax(b, ell, **kw):
    v = E(b, ell, D, X, **kw); i = np.unravel_index(np.argmax(v), v.shape); return v[i], ds[i[0]], xs[i[1]]
B = lambda ell: 11/12 - ell/4
def bestB(**kw):
    best = (None, -1)
    for b in np.linspace(0.001, 0.3, 40):
        lo, hi = 0.0, 0.8
        for _ in range(30):
            mid = (lo+hi)/2
            if Emax(b, mid, **kw)[0] <= 0: lo = mid
            else: hi = mid
        if lo > best[1]: best = (b, lo)
    b, l = best; em = Emax(b, l, **kw)
    return f"b={b:.4f} ell={l:.5f} B={B(l):.6f} active(delta={em[1]:.3f}, x={em[2]:.2f})"
print("paper check Emax(1/8,1/6) =", Emax(1/8, 1/6))
print("baseline (alpha=5/6,c=2/9,sM=1/2):", bestB())
print("ideal counts R*=1-delta       :", bestB(ideal=True))
for a in [0.8, 0.75, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.01]:
    print(f"alpha={a:.2f}:", bestB(alpha=a))
for c in [0.25, 0.3, 0.4, 0.5, 1.0]:
    print(f"c={c:.2f} (plain capacity):", bestB(c=c))
for s in [0.6, 0.75, 1.0]:
    print(f"sM={s:.2f} (inverse capacity):", bestB(sM=s))
for fs in [0.1, 0.25, 0.5]:
    print(f"floor_save={fs} ideal counts  :", bestB(ideal=True, floor_save=fs))
    print(f"floor_save={fs} baseline counts:", bestB(floor_save=fs))
