import numpy as np, itertools, random
random.seed(7); rng=np.random.default_rng(7)
def f0(s,y): return 2*(y*y-s*s)/(s*s+y*y)**2
def f2(s,y): return -12*(s**4-6*s*s*y*y+y**4)/(s*s+y*y)**4
def f4(s,y): return -240*(s*s-y*y)*(s*s-4*s*y+y*y)*(s*s+4*s*y+y*y)/(s*s+y*y)**6

def hprime(t, reals, pairs):
    v=np.zeros_like(t)
    for (c,mn) in reals: v-=mn/(t-c)**2
    for (x,y,mm) in pairs: v+=mm*f0(t-x,y)
    return v
def absterms(t, reals, pairs):
    v=np.zeros_like(t)
    for (c,mn) in reals: v+=mn/(t-c)**2
    for (x,y,mm) in pairs: v+=np.abs(mm*f0(t-x,y))
    return v

def count_zeros(a,b,reals,pairs,N=800001):
    t=np.linspace(a+1e-6*(b-a), b-1e-6*(b-a), N)
    v=hprime(t,reals,pairs); A=absterms(t,reals,pairs)
    s=np.sign(v); mask=np.abs(v)>1e-11*A
    sv=s[mask]; tv=t[mask]
    idx=np.nonzero(sv[1:]*sv[:-1]<0)[0]
    return len(idx), tv[idx] if len(idx) else np.array([])

def triple_empty(deep, a, b, N=400001):
    t=np.linspace(a,b,N)
    L0=np.zeros_like(t);L2=np.zeros_like(t);L4=np.zeros_like(t)
    for (x,y,mm) in deep:
        s=t-x; L0+=mm*f0(s,y); L2+=mm*f2(s,y); L4+=mm*f4(s,y)
    T=(L0>0)&(L2>0)&(L4>0)
    return not T.any(), t[T] if T.any() else None

def budgets_ok(a,b,reals,pairs_shallow_nonov):
    # (L2)(L4)(L6) with only shallow-ov and non-ov in the budget (deep excluded)
    g=b-a; W_sh=V1=V2=0.0; ML4=MR4=ML6=MR6=0.0
    c8,c12=1+np.sqrt(2),2+np.sqrt(3)
    for (x,y,mm) in pairs_shallow_nonov:
        ov = (x-y<b) and (x+y>a)
        if ov and y>=g/2:
            w=(g/(2*y))**2; W_sh+=mm*w; V1+=mm*w*w; V2+=mm*w**3
        elif not ov:
            if x+y<=a:
                if a-x<c8*y: ML4+=mm
                if a-x<c12*y: ML6+=mm
            elif x-y>=b:
                if x-b<c8*y: MR4+=mm
                if x-b<c12*y: MR6+=mm
    kap=(11+5*np.sqrt(5))/64; G4=0.022543; G6=0.04631627
    return (W_sh<1) and (kap*V1+G4*(ML4+MR4)<1) and (V2+G6*(ML6+MR6)<1)

results=[]
viol=[]
NC=0
for trial in range(600):
    g=random.choice([1.0,4.0,16.0]); a,b=-g/2,g/2
    reals=[(a,random.choice([1,1,2])),(b,random.choice([1,1,3]))]
    for extra in range(random.randint(0,3)):
        side=random.choice([-1,1]); d=10**rng.uniform(-2,1)
        reals.append(((b if side>0 else a)+side*d, random.randint(1,3)))
    m=random.randint(1,5)
    deep=[]
    for j in range(m):
        y=10**rng.uniform(np.log10(g*1e-4), np.log10(g*0.49))
        x=rng.uniform(a-0.5*y, b+0.5*y)
        deep.append((x,y,random.randint(1,4)))
    other=[]
    for k in range(random.randint(0,3)):
        kind=random.choice(['sh','nonov'])
        if kind=='sh':
            y=g/2*10**rng.uniform(0,0.3); x=rng.uniform(a,b); mm=1
            if (g/(2*y))**2*mm<0.3: other.append((x,y,mm))
        else:
            y=10**rng.uniform(-2,0); side=random.choice([-1,1])
            x=(b if side>0 else a)+side*(y+10**rng.uniform(-2,0)*y); other.append((x,y,1))
    if not budgets_ok(a,b,reals,other): continue
    emp, Tpts = triple_empty(deep,a,b)
    NC+=1
    nz,zlocs=count_zeros(a,b,reals,deep+other)
    M=sum(mm for (_,_,mm) in deep)
    cap=16*len(deep)-10
    tag='EMPTY' if emp else 'NONEMPTY'
    results.append((tag,len(deep),M,nz))
    if emp and nz>cap: viol.append(('CAPVIOL',trial,len(deep),M,nz,cap))
    if nz>2*M+ (0 if len(deep)>0 else 1): viol.append(('2M-EXCEED',tag,trial,len(deep),M,nz))
    # confinement check: zeros within union of I_j
    for z in zlocs:
        if not any(abs(z-x)<y for (x,y,mm) in deep):
            # allow shallow overhang interiors too (Step1 only excludes when budgets incl. all)
            if not any(abs(z-x)<y for (x,y,mm) in other):
                viol.append(('CONF',trial,float(z)))
import collections
cnt=collections.Counter(r[0] for r in results)
mx={}
for tag,md,M,nz in results:
    mx.setdefault(tag,(0,0,0))
    if nz>mx[tag][2]: mx[tag]=(md,M,nz)
print("configs used:",NC, dict(cnt))
print("max Z(h') by regime (m,M,Z):",mx)
print("violations:",viol[:20], "n_viol=",len(viol))
