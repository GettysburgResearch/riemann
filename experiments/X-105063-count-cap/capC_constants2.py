import mpmath as mp
mp.mp.dps = 30
def negRe(n, u):   # -Re((u+i)^{-n})
    return -((mp.mpc(u,1))**(-n)).real
# kappa_n = max_u (-Re(u+i)^{-n})_+  (even in u; search u>=0)
def kappa(n):
    # coarse grid then refine critical point of d/du
    best, ubest = mp.mpf(0), 0
    for k in range(0, 4001):
        u = mp.mpf(k)/500
        val = negRe(n,u)
        if val > best: best, ubest = val, u
    d = lambda x: mp.diff(lambda uu: negRe(n,uu), x)
    ur = mp.findroot(d, ubest)
    return negRe(n, ur), ur
# G_n = 2 max_{v>=1} (v-1)^n * (-Re((v+i)^{-n}))_+
def G(n):
    fn = lambda vv: 2*(vv-1)**n * negRe(n,vv)
    best, vbest = mp.mpf(0), 1
    for k in range(1000, 8001):
        v = mp.mpf(k)/1000
        val = fn(v)
        if val > best: best, vbest = val, v
    d = lambda x: mp.diff(fn, x)
    vr = mp.findroot(d, vbest)
    return fn(vr), vr
k4,u4 = kappa(4); k6,u6 = kappa(6)
G4,v4 = G(4); G6,v6 = G(6)
print("kappa4 = %s at u=%s   (exact (11+5sqrt5)/64 = %s)" % (mp.nstr(k4,12), mp.nstr(u4,10), mp.nstr((11+5*mp.sqrt(5))/64,12)))
print("kappa6 = %s at u=%s" % (mp.nstr(k6,12), mp.nstr(u6,10)))
print("G4 = %s at v=%s" % (mp.nstr(G4,12), mp.nstr(v4,10)))
print("G6 = %s at v=%s   bound 2e^{-pi/2}=%s" % (mp.nstr(G6,12), mp.nstr(v6,10), mp.nstr(2*mp.e**(-mp.pi/2),10)))
# safety margins vs grid (enclosure sanity): perturb refined optimum
for name,(val,pt,n,fn) in {"k6":(k6,u6,6,lambda x:negRe(6,x)), "G6":(G6,v6,6,lambda x:2*(x-1)**6*negRe(6,x))}.items():
    eps=mp.mpf('1e-8')
    print(name, "local max check:", fn(pt)>=fn(pt+eps), fn(pt)>=fn(pt-eps))
# also p2 = max f''(s;1) positive part (for reference only) and check R4 sign claims
f2 = lambda s: -12*negRe(4,s)*(-1)  # f'' = -12 Re(s+i)^{-4}?? careful: f''=-12Re(s-i)^-4 = -12Re(s+i)^-4 (real part same, conj) 
f2v = lambda s: -12*((mp.mpc(s,1))**(-4)).real
R4 = 2+mp.sqrt(3)
print("at |s|=R4: f=%s f''=%s f''''=%s (all <=0 expected)" % (
    mp.nstr(2*(1-R4**2)/(1+R4**2)**2,8), mp.nstr(f2v(R4),8), mp.nstr(-240*((mp.mpc(R4,1))**(-6)).real,8)))
print("just beyond R4 (s=R4+0.01): f''''=", mp.nstr(-240*((mp.mpc(R4+mp.mpf('0.01'),1))**(-6)).real,8))
