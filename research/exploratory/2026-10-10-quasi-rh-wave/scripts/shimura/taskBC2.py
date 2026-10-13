"""Task B/C extended: cutoffs of different smoothness (sharp, Riesz C0 (1-x)_+, Riesz C1 (1-x)^2_+, Gaussian),
exact main-term subtraction for quadratic eta (r3), and the principal row extended via the verified Shimura
formula c(n) = (mu chi_{-4} * sigma)(n_odd) [r3] / (mu chi_{-4} * sigma)(n) [H row at |D|=4], sharp and smooth."""
import numpy as np, math, os, sys, time
OUT = os.path.dirname(os.path.abspath(__file__))
r3 = np.load(os.path.join(OUT,"r3.npy")).astype(np.float64); H = np.load(os.path.join(OUT,"H.npy"))
R3MAX=len(r3)-1; HMAX=len(H)-1

def primitive_root(q):
    for g in range(2,q):
        if len({pow(g,k,q) for k in range(1,q)})==q-1: return g
def characters(q):
    g=primitive_root(q); ind=np.zeros(q,dtype=np.int64)
    for k in range(q-1): ind[pow(g,k,q)]=k
    out=[]; seen=set()
    for j in range(1,q-1):
        order=(q-1)//math.gcd(j,q-1)
        if order in seen: continue   # one representative per order
        seen.add(order); tab=np.exp(2j*np.pi*j*ind/(q-1)); tab[0]=0; out.append((j,order,tab))
    return out
def fit(xs, ys):
    xs=np.asarray(xs,float); ys=np.asarray(ys,float); ok=(ys>0)&np.isfinite(ys); xs=xs[ok]; ys=ys[ok]
    if len(xs)<3: return float('nan'), float('nan')
    A=np.vstack([np.log(xs),np.ones(len(xs))]).T; coef=np.linalg.lstsq(A,np.log(ys),rcond=None)[0]
    pred=A@coef; dof=max(len(xs)-2,1)
    se=np.sqrt(np.sum((np.log(ys)-pred)**2)/dof/np.sum((np.log(xs)-np.log(xs).mean())**2))
    return coef[0], se
def dyadic_rms(vals, lo, hi):
    xs=[];ys=[]
    for j in range(lo,hi+1):
        a,b=2**j,min(2**(j+1),len(vals))
        if a>=b: break
        xs.append(np.sqrt(a*b)); ys.append(np.sqrt(np.mean(np.abs(vals[a:b])**2)))
    return np.array(xs),np.array(ys)

# ---------- principal-row coefficients by formula, n <= NP ----------
NP = 10**6
mu = np.ones(NP+1,dtype=np.int8); isp=np.ones(NP+1,dtype=bool); isp[:2]=False
for p in range(2,int(NP**0.5)+1):
    if isp[p]: isp[p*p::p]=False
for p in np.nonzero(isp)[0]:
    mu[p::p]*=-1
    if p*p<=NP: mu[p*p::p*p]=0
mu[0]=0
sig=np.zeros(NP+1,dtype=np.int64)
for d in range(1,NP+1): sig[d::d]+=d
chi4=np.array([0,1,0,-1])
cH=np.zeros(NP+1,dtype=np.int64)       # (mu chi_{-4} * sigma)(n)
for m in range(1,NP+1):
    w=int(mu[m])*int(chi4[m%4])
    if w==0: continue
    k=np.arange(1,NP//m+1); cH[m*k]+=w*sig[k]
nn=np.arange(0,NP+1); nodd=nn.copy()
while True:
    e=(nodd%2==0)&(nodd>0)
    if not e.any(): break
    nodd[e]//=2
cR=cH[nodd]; cR[0]=0
# verify against data
n=np.arange(1,int(np.sqrt(R3MAX))+1); assert np.max(np.abs(r3[n*n]/r3[1]-cR[n]))==0
n=np.arange(1,int(np.sqrt(HMAX//4))+1); assert np.max(np.abs(H[4*n*n]/H[4]-cH[n]))<1e-9
print("principal-row formula verified against data; extended to n<=",NP)

for name,a,ZMAX,cP in [("r3",r3,R3MAX,cR),("H",H,HMAX,cH)]:
    N=np.arange(0,ZMAX+1).astype(np.float64)
    grid=np.unique(np.logspace(4,np.log10(ZMAX),300).astype(np.int64))
    jlo,jhi=14,int(np.log2(ZMAX))-1
    print(f"\n######## form {name}: ZMAX={ZMAX}")
    print("q ord | sharp: LS  dyRMS | Riesz C0 (1-x)_+: LS dyRMS | Riesz C1 (1-x)^2_+: LS dyRMS | Gauss: |D_W| at Z=1e4,1e5,1e6 and ratio to roundoff floor 1e-16*sum|a|W")
    for q in [5,7,11,13]:
        for (j,order,tab) in characters(q):
            eta=tab[(np.arange(0,ZMAX+1))%q]; prod=a*eta
            C0=np.cumsum(prod); C1=np.cumsum(prod*N); C2=np.cumsum(prod*N*N)
            Zg=grid.astype(np.float64)
            D_sharp=C0[grid]; D_r0=C0[grid]-C1[grid]/Zg; D_r1=C0[grid]-2*C1[grid]/Zg+C2[grid]/Zg**2
            if order==2 and name=="r3":
                etam1=tab[q-1].real; c=(4*np.pi/3)*etam1*(q-1)/q**2
                # main terms: sharp c Z^{3/2}; Riesz C0: c Z^{3/2}*(1-3/5)=c*(2/5)Z^{3/2}; C1: c Z^{3/2}*(1-2*3/5+3/7)
                D_sharp=D_sharp-c*Zg**1.5; D_r0=D_r0-c*(2/5)*Zg**1.5; D_r1=D_r1-c*(1-6/5+3/7)*Zg**1.5
                full=C0-c*(np.arange(0,ZMAX+1)**1.5)
                note="(main term c Z^{3/2} subtracted, c=%.5f)"%c
            elif order==2:
                # fit c on top decade and subtract
                top=grid[grid>=ZMAX/10]; c=np.mean((C0[top]/top**1.5).real)
                D_sharp=D_sharp-c*Zg**1.5; D_r0=D_r0-c*(2/5)*Zg**1.5; D_r1=D_r1-c*(1-6/5+3/7)*Zg**1.5
                full=C0-c*(np.arange(0,ZMAX+1)**1.5)
                note="(fitted main term subtracted, c=%.5f; D(Z)/Z^1.5 at 1e4,1e5,1e6: %s)"%(c, ", ".join(f"{(C0[Z]/Z**1.5).real:.5f}" for Z in [10**4,10**5,10**6] if Z<=ZMAX))
            else:
                full=C0; note=""
            s1,e1=fit(grid,np.abs(D_sharp)); xs,ys=dyadic_rms(full,jlo,jhi); s2,e2=fit(xs,ys)
            s3,e3=fit(grid,np.abs(D_r0)); s5,e5=fit(grid,np.abs(D_r1))
            gs=[]
            for Z in [1e4,1e5,1e6]:
                w=np.exp(-(N/Z)**2); v=abs(np.sum(prod*w)); fl=1e-16*np.sum(np.abs(a)*w); gs.append((v,v/fl))
            print(f"{q:2d} {order:3d} | {s1:+.3f}+-{e1:.3f} {s2:+.3f}+-{e2:.3f} | {s3:+.3f}+-{e3:.3f} | {s5:+.3f}+-{e5:.3f} | "+
                  " ".join(f"{v:.1e}({r:.0f}x)" for v,r in gs)+" "+note)
            sys.stdout.flush()
    # ---------- principal row, extended ----------
    print(f"\n  principal row for form {name}: P(Z)=sum_{{n<=Y}} c(n) eta(n)^2, Y=sqrt(Z), c from formula, Y<=1e6 (Z<=1e12)")
    print("  q ord | sharp P: LS slope in Z (Y in [1e2,1e6]) , runmax | C0 Riesz | smooth Gauss P_W(Y): slope in Z | |P_W(Y)| at Y=1e2,1e3,1e4,1e5 | sharp |P(Z)| at Z=1e4..1e7 (data range)")
    nP=np.arange(0,NP+1).astype(np.float64)
    for q in [5,7,11,13]:
        for (j,order,tab) in characters(q):
            eta2=tab[(np.arange(0,NP+1)**2)%q]; prodP=cP*eta2
            S0=np.cumsum(prodP); S1=np.cumsum(prodP*nP)
            Ys=np.unique(np.logspace(2,6,200).astype(np.int64)); Zs=Ys.astype(float)**2
            sharpP=np.abs(S0[Ys]); r0P=np.abs(S0[Ys]-S1[Ys]/Ys)
            if order==2:
                # main term from pole of L(s-1,eta^2) at s=2: sum_{n<=Y} c(n) eta^2(n) ~ C Y^2; subtract fitted C
                top=Ys[Ys>=1e5]; Cc=np.mean(S0[top].real/top**2)
                sharpP=np.abs(S0[Ys]-Cc*Ys**2); r0P=np.abs(S0[Ys]-S1[Ys]/Ys-Cc*Ys**2/3)
                noteP=f"(main term C Y^2 = C Z subtracted, C={Cc:.5f})"
            else: noteP=""
            sP,eP=fit(Zs,sharpP); sPm,ePm=fit(Zs,np.maximum.accumulate(sharpP)); sR,eR=fit(Zs,r0P)
            Yg=np.logspace(2,5,16); PW=[]
            for Y in Yg:
                w=np.exp(-(nP/Y)**2); v=np.sum(prodP*w)
                if order==2: v=v-Cc*Y**2*(math.sqrt(math.pi)/4)*2   # int_0^inf 2x e^{-x^2} dx * Y^2 = Y^2 ... (approx main term)
                PW.append(abs(v))
            PW=np.array(PW); sW,eW=fit(Yg**2,PW)
            vals=[abs(S0[int(np.sqrt(Z))]) for Z in [10**4,10**5,10**6,10**7] if Z<=ZMAX]
            print(f"  {q:2d} {order:3d} | {sP:+.3f}+-{eP:.3f} {sPm:+.3f}+-{ePm:.3f} | {sR:+.3f}+-{eR:.3f} | {sW:+.3f}+-{eW:.3f} | "+
                  " ".join(f"{PW[k]:.2e}" for k in [0,5,10,15])+" | "+" ".join(f"{v:.2e}" for v in vals)+" "+noteP)
            sys.stdout.flush()
print("done")
