import mpmath as mp
mp.mp.dps = 40
reals=[(0.0,1),(1.0,1),(-0.0657,1)]; pairs=[(0.737395,0.004023,2)]
def hp(t):
    s = mp.mpf(0)
    for r,m in reals: s -= m/(t-r)**2
    for x,y,m in pairs:
        u=t-x; s += m*2*(y**2-u**2)/(u**2+y**2)**2
    return s
x,y,_ = pairs[0]
lo, hi = x-3*y, x+3*y
prev=None; prevt=None; roots=[]
Nv=40000
for k in range(Nv+1):
    t = mp.mpf(lo)+(mp.mpf(hi)-mp.mpf(lo))*k/Nv
    v = hp(t)
    if prev is not None and v*prev < 0:
        r = mp.findroot(hp, (prevt, t), solver='bisect', tol=mp.mpf('1e-35'))
        roots.append(r)
    prev, prevt = v, t
print("I = (%.6f, %.6f)" % (x-y, x+y))
for r in roots:
    print("root:", mp.nstr(r,12), " in I:", x-y < r < x+y, " dist to edge/y:", mp.nstr((min(r-(x-y),(x+y)-r))/y,6))
