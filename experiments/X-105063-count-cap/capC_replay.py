import numpy as np, math, random
ns = {}
import os as _os
exec(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'capC_scanC.py')).read(), ns)   # reruns scan, seed fixed
g,reals,pairs,q,ex,nzp,per = ns['best']
print("CONFIG g=%s reals=%s" % (g,reals))
for p in pairs: print("  pair", p)
import mpmath as mp
mp.mp.dps = 40
def h(t):
    s=mp.mpf(0)
    for r,m in reals: s += m/(t-r)
    for x,y,m in pairs:
        u=t-x; s += m*2*u/(u**2+y**2)
    return s
# count zeros of h in (0,g): fine scan + bisect, refined near deep intervals
roots=[]
segs=[(mp.mpf('1e-9'), mp.mpf(g)-mp.mpf('1e-9'), 200000)]
for x,y,m in pairs:
    if 0<x<g and y<g/2: segs.append((mp.mpf(x)-2*y, mp.mpf(x)+2*y, 40000))
found=[]
for lo,hi,N in segs:
    prev=None; prevt=None
    for k in range(N+1):
        t = lo+(hi-lo)*k/N
        v = h(t)
        if prev is not None and v*prev<0:
            r = mp.findroot(h, (prevt,t), solver='bisect', tol=mp.mpf('1e-35'))
            found.append(r)
        prev,prevt=v,t
uniq=[]
for r in sorted(found):
    if not uniq or abs(r-uniq[-1])>mp.mpf('1e-20'): uniq.append(r)
print("mpmath: distinct zeros of h in G =", len(uniq), " => extra =", len(uniq)-1, " (float64 said", ex,")")
