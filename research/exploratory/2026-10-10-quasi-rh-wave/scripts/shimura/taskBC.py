"""Task B/C: direct side D(Z)=sum_{N<=Z} a(N) eta(N) for nonprincipal eta mod q, sharp+smooth cutoffs,
growth exponents; principal row P(Z)=sum_{n<=sqrt Z} [a(n^2)/a(1)] eta(n^2); ratio |P|/|D|."""
import numpy as np, time, os, sys, cmath, math
OUT = os.path.dirname(os.path.abspath(__file__))
r3 = np.load(os.path.join(OUT,"r3.npy")).astype(np.float64); H = np.load(os.path.join(OUT,"H.npy"))
R3MAX=len(r3)-1; HMAX=len(H)-1

def primitive_root(q):
    for g in range(2,q):
        if len({pow(g,k,q) for k in range(1,q)})==q-1: return g
def characters(q):
    g = primitive_root(q); ind = np.zeros(q, dtype=np.int64)
    for k in range(q-1): ind[pow(g,k,q)] = k
    chars=[]
    for j in range(1,q-1):
        order = (q-1)//math.gcd(j,q-1)
        tab = np.exp(2j*np.pi*j*ind/(q-1)); tab[0]=0
        chars.append((j, order, tab))
    return chars
def fit(xs, ys):
    xs=np.asarray(xs,float); ys=np.asarray(ys,float); ok=ys>0; xs=xs[ok]; ys=ys[ok]
    A = np.vstack([np.log(xs), np.ones(len(xs))]).T
    coef = np.linalg.lstsq(A, np.log(ys), rcond=None)[0]
    pred=A@coef; dof=max(len(xs)-2,1)
    se = np.sqrt(np.sum((np.log(ys)-pred)**2)/dof/np.sum((np.log(xs)-np.log(xs).mean())**2))
    return coef[0], se
def dyadic_rms(vals, lo, hi):
    xs=[];ys=[]
    for j in range(lo,hi+1):
        a,b=2**j,min(2**(j+1),len(vals))
        if a>=b: break
        xs.append(np.sqrt(a*b)); ys.append(np.sqrt(np.mean(np.abs(vals[a:b])**2)))
    return np.array(xs),np.array(ys)

results = {}
FORMS=[("r3", r3, R3MAX), ("H", H, HMAX)]
if len(sys.argv)>1: FORMS=[f for f in FORMS if f[0] in sys.argv[1:]]
for name, a, ZMAX in FORMS:
    N = np.arange(0, ZMAX+1)
    grid = np.unique(np.logspace(4, np.log10(ZMAX), 300).astype(np.int64))
    jlo, jhi = 14, int(np.log2(ZMAX))-1
    # trivial bound
    T = np.cumsum(np.abs(a)); slT,seT = fit(grid, T[grid])
    print(f"\n######## form {name}: ZMAX={ZMAX}; trivial bound sum|a(N)|: exponent {slT:.4f}+-{seT:.4f}; T(ZMAX)/ZMAX^1.5={T[ZMAX]/ZMAX**1.5:.5f}  (r3: 4pi/3={4*np.pi/3:.5f}; H: pi/18={np.pi/18:.5f})")
    # principal row coefficients c(n)=a(n^2)/a(1) (r3) or a(4n^2)/a(4) (H, D=-4 row)
    if name=="r3":
        nmax = int(np.sqrt(ZMAX)); n = np.arange(1,nmax+1); c = a[n*n]/a[1]
    else:
        nmax = int(np.sqrt(ZMAX//4)); n = np.arange(1,nmax+1); c = a[4*n*n]/a[4]
    print(f"principal row: c(n)=a({'n^2' if name=='r3' else '4n^2'})/a({1 if name=='r3' else 4}), n<={nmax}")
    print("q  j  order  | sharp D(Z): LS slope   dyadicRMS slope   runmax slope | smooth(Gauss) slope | P(Z) slope (LS, runmax) | |P|/|D| at Z=1e4,1e5,1e6,1e7 | D(ZMAX)/ZMAX^1.5 (quadratic: predicted)")
    for q in [5,7,11,13]:
        for (j, order, tab) in characters(q):
            eta = tab[N % q]
            Dz = np.cumsum(a*eta)           # D(Z) for Z=0..ZMAX
            absD = np.abs(Dz)
            s1,e1 = fit(grid, absD[grid]); xs,ys = dyadic_rms(Dz, jlo, jhi); s2,e2 = fit(xs,ys)
            s3,e3 = fit(grid, np.maximum.accumulate(absD)[grid])
            # smooth cutoff: W(x)=exp(-x^2), Z in geometric grid up to ZMAX/6
            Zs = np.logspace(4, np.log10(ZMAX/6), 25); sm=[]
            prod = a*eta
            for Z in Zs:
                sm.append(abs(np.sum(prod*np.exp(-(N/Z)**2))))
            sm=np.array(sm); s4,e4 = fit(Zs, sm)
            # principal row
            eta2 = tab[(n*n) % q]; P = np.cumsum(c*eta2); absP=np.abs(P)   # P indexed by n=1..nmax -> Z=n^2
            Zp = n.astype(float)**2
            okp = Zp>=1e4; s5,e5 = fit(Zp[okp], absP[okp]); s6,e6 = fit(Zp[okp], np.maximum.accumulate(absP)[okp])
            ratios=[]
            for Z in [10**4,10**5,10**6,10**7]:
                if Z<=ZMAX:
                    k=int(np.sqrt(Z)) if name=='r3' else int(np.sqrt(Z/4)); ratios.append(absP[k-1]/absD[Z] if absD[Z]>0 else float('inf'))
            if order==2:
                etam1 = tab[q-1].real
                pred = (4*np.pi/3)*etam1*(q-1)/q**2 if name=="r3" else float('nan')
                lastcol = f"{(Dz[ZMAX]/ZMAX**1.5).real:+.5f} (pred {pred:+.5f})"
            else:
                lastcol = f"{abs(Dz[ZMAX])/ZMAX**1.5:.2e}"
            print(f"{q:2d} {j:2d} {order:3d}    | {s1:+.3f}+-{e1:.3f}  {s2:+.3f}+-{e2:.3f}  {s3:+.3f}+-{e3:.3f} | {s4:+.3f}+-{e4:.3f} | {s5:+.3f}+-{e5:.3f} {s6:+.3f}+-{e6:.3f} | " + " ".join(f"{r:.2e}" for r in ratios) + f" | {lastcol}")
            results[(name,q,j)] = dict(order=order, sharp=(s1,e1,s2,e2,s3,e3), smooth=(s4,e4), P=(s5,e5,s6,e6), ratios=ratios)
            sys.stdout.flush()
    # also: |D(Z)| table at Z = 1e4..ZMAX for a quadratic and a cubic/quartic example
    print("\n  Sample values, form", name)
    for q,jsel in [(5,[1,2]),(7,[2,3]),(13,[3,4,6])]:
        for (j,order,tab) in characters(q):
            if j not in jsel: continue
            eta = tab[N%q]; Dz=np.cumsum(a*eta); eta2=tab[(n*n)%q]; P=np.cumsum(c*eta2)
            Zl=[Z for Z in [10**4,10**5,10**6,10**7] if Z<=ZMAX]
            print(f"   q={q} j={j} order={order}: |D(Z)| = " + ", ".join(f"{abs(Dz[Z]):.3e}" for Z in Zl) + 
                  "  ; |D|/Z^(3/4) = " + ", ".join(f"{abs(Dz[Z])/Z**0.75:.3f}" for Z in Zl) +
                  "  ; |P(Z)| = " + ", ".join(f"{abs(P[(int(np.sqrt(Z)) if name=='r3' else int(np.sqrt(Z/4)))-1]):.3e}" for Z in Zl))
import pickle; pickle.dump(results, open(os.path.join(OUT,"resultsBC_%s.pkl"%"_".join(f[0] for f in FORMS)),"wb"))
print("done")
