# EMPIRICAL / FLOATING_RECONNAISSANCE: family mean square of sextic-twisted Mobius sums over Z[w]
# A_u(D) = sum_{n sqfree primary, (n,6)=1} mu(n) chi_n(u) W(N n / D),  rows u: all nonzero elements with N(u)<=H.
import math, sys, numpy as np
def mul(x,y):
    a,b=x; c,d=y; return (a*c-b*d, a*d+b*c-b*d)
def norm(x): a,b=x; return a*a-a*b+b*b
def isp(m): return m>1 and all(m%k for k in range(2,int(m**.5)+1))
def primes_upto(B):
    P=[]
    for p in range(5,B+1):
        if not isp(p): continue
        if p%3==1:
            # find primary pi=c+dw with norm p, both conjugates
            found=set()
            r=int(math.isqrt(4*p//3))+2
            for c in range(-r,r+1):
                for d in range(-r,r+1):
                    if c*c-c*d+d*d==p and c%3==1 and d%3==0: found.add((c,d))
            for f in found: P.append(('s',f,p))
        elif p*p<=B: P.append(('i',(-p,0),p))
    return P
def sexpow_inert(x,e,q):
    # arithmetic in Z[w]/q
    def m(x,y):
        a,b=x; c,d=y; return ((a*c-b*d)%q, (a*d+b*c-b*d)%q)
    r=(1,0); x=(x[0]%q,x[1]%q)
    while e:
        if e&1: r=m(r,x)
        x=m(x,x); e>>=1
    return r
SIX=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]  # zeta6^k with zeta6=1+w=-w^2
def residue_table(P,U):
    # returns int8 array len(U): k in 0..5 with chi_P(u)=zeta6^k, or -1 if P|u
    kind,(c,d),p=P
    out=np.empty(len(U),dtype=np.int8)
    if kind=='s':
        w0=(-c*pow(d,-1,p))%p
        z=[(s[0]+s[1]*w0)%p for s in SIX]; lut={v:k for k,v in enumerate(z)}
        e=(p-1)//6
        for i,(a,b) in enumerate(U):
            x=(a+b*w0)%p
            out[i]=-1 if x==0 else lut[pow(x,e,p)]
    else:
        q=p; e=(q*q-1)//6
        lut={(s[0]%q,s[1]%q):k for k,s in enumerate(SIX)}
        for i,(a,b) in enumerate(U):
            if a%q==0 and b%q==0: out[i]=-1
            else: out[i]=lut[sexpow_inert((a,b),e,q)]
    return out
def W(y): # smooth bump on (1,2)
    t=np.where((y>1)&(y<2),(y-1)*(2-y),0.0)
    return np.where(t>0,np.exp(-1/np.maximum(t,1e-300)*0.25),0.0)
def run(D,theta=0.1):
    H=D**(1+theta)
    P=primes_upto(int(2*D))
    # squarefree products with norm in (D,2D)
    ns=[]
    def gen(i,cur,N,fs):
        if D<N<2*D: ns.append((N,fs))
        for j in range(i,len(P)):
            Np=P[j][2] if P[j][0]=='s' else P[j][2]**2
            if N*Np>=2*D: continue
            gen(j+1,mul(cur,P[j][1]),N*Np,fs+[j])
    # P sorted by norm
    P.sort(key=lambda t: t[2] if t[0]=='s' else t[2]**2)
    gen(0,(1,0),1,[])
    r=int(math.isqrt(int(4*H/3)))+2
    U=[(a,b) for a in range(-r,r+1) for b in range(-r,r+1) if 0<a*a-a*b+b*b<=H]
    used=sorted({j for _,fs in ns for j in fs})
    tab={j:residue_table(P[j],U) for j in used}
    zeta=np.exp(2j*np.pi*np.arange(6)/6)
    Amu=np.zeros(len(U),complex); Aone=np.zeros(len(U),complex)
    for N,fs in ns:
        w=float(W(np.array([N/D]))[0])
        if w==0: continue
        ex=np.zeros(len(U),dtype=np.int16); zero=np.zeros(len(U),bool)
        for j in fs:
            t=tab[j]; zero|=(t<0); ex+=np.where(t<0,0,t)
        v=np.where(zero,0,zeta[ex%6])*w
        Amu+=((-1)**len(fs))*v; Aone+=v
    Nu=np.array([a*a-a*b+b*b for a,b in U])
    # sixth-power rows: u = unit * m^6 ... identify rows where chi_n(u)=1 for all primes used (principal on support)
    allone=np.ones(len(U),bool)
    for j in used: allone&=(tab[j]==0)
    S=lambda A: float(np.sum(np.abs(A)**2))
    print(f"D={D:6d} H={H:9.0f} #n={len(ns):5d} #rows={len(U):6d} "
          f"mu: sum|A|^2/(DH)={S(Amu)/(D*H):7.4f} (principal rows share {S(Amu[allone])/max(S(Amu),1e-9):.3f}) | "
          f"ones: sum|A|^2/(DH)={S(Aone)/(D*H):7.4f} (principal rows share {S(Aone[allone])/S(Aone):.3f}) "
          f"|A_1|mu={abs(Amu[U.index((1,0))]):.1f} |A_1|ones={abs(Aone[U.index((1,0))]):.1f} #principal={int(allone.sum())}",flush=True)
for D in [int(x) for x in sys.argv[1:]]: run(D)
