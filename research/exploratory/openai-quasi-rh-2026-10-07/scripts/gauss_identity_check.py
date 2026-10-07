# Numerical check of Lemma (arithmetic identities) in OpenAI's 11/12 quasi-RH paper.
# Elements of Z[w], w = e^{2 pi i/3}, stored as (a,b) = a + b w.
import cmath, math, itertools
W = complex(-0.5, math.sqrt(3)/2)
def mul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c-b*d)
def norm(x):
    a,b=x; return a*a-a*b+b*b
def cx(x): return x[0]+x[1]*W
def hnf(n):
    # lattice n*Z[w] in basis (1,w): generators n*1=(c,d), n*w=(-d,c-d)
    c,d=n
    v1=[c,d]; v2=[-d,c-d]
    # make second coord gcd: integer row reduction on columns
    # want basis {(h11,0),(h12,h22)}
    import math
    a,b=v1,v2
    while b[1]!=0:
        q=a[1]//b[1]
        a=[a[0]-q*b[0],a[1]-q*b[1]]
        a,b=b,a
    # now b[1]==0, a[1]=g
    h22=abs(a[1]); 
    if a[1]<0: a=[-a[0],-a[1]]
    h11=abs(b[0])
    return h11,(a[0],h22)
def red(x,H):
    h11,(h12,h22)=H
    a,b=x
    k=b//h22; a-=k*h12; b-=k*h22
    a%=h11
    return (a,b)
def residues(n):
    H=hnf(n); h11,(h12,h22)=H
    assert h11*h22==norm(n)
    return [(a,b) for a in range(h11) for b in range(h22)],H
def powmod(x,e,H):
    r=(1,0); x=red(x,H)
    while e:
        if e&1: r=red(mul(r,x),H)
        x=red(mul(x,x),H); e>>=1
    return r
UNITS=[(1,0),(0,1),(-1,-1)]  # 1,w,w^2
SIX=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]  # zeta6^k: 1, -w^2=1+w, w, -1, w^2, -w
SIXC=[cmath.exp(2j*math.pi*k/6) for k in range(6)]
def primary(x):
    # unit multiple congruent to 1 mod 3
    for u in [(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1)]:
        y=mul(u,x)
        if y[0]%3==1 and y[1]%3==0: return y
    return None
def is_prime_elt(x):
    N=norm(x)
    if N<2: return False
    def isp(m): return m>1 and all(m%k for k in range(2,int(m**.5)+1))
    if isp(N): return True
    r=int(round(N**.5))
    return r*r==N and isp(r) and r%3==2
def chi6_prime(x,p):
    H=hnf(p); N=norm(p)
    y=powmod(x,(N-1)//6,H)
    if y==(0,0): return 0
    for k,z in enumerate(SIX):
        if red(z,H)==y: return SIXC[k]
    raise ValueError("not a sixth root", x,p,y)
def factor(n):
    # factor primary squarefree n into primary primes by trial division over small primary primes
    fs=[]; rem=n
    for P in PRIMES:
        if norm(P)>norm(rem): break
        # divisibility: rem/P in Z[w]?  rem*conj(P)/N(P)
        while True:
            c=(P[0]-P[1], -P[1])  # conj(a+bw)=a+b w^2 = (a-b) - b w
            q=mul(rem,c); NP=norm(P)
            if q[0]%NP==0 and q[1]%NP==0:
                fs.append(P); rem=(q[0]//NP,q[1]//NP)
            else: break
    if norm(rem)!=1: fs.append(primary(rem))
    return fs
def chi6(x,n,fs):
    v=1
    for p in fs: v*=chi6_prime(x,p)
    return v
def e(z): return cmath.exp(4j*math.pi*z.imag/math.sqrt(3))
def gamma(j,n,fs):
    R,H=residues(n); N=norm(n); nc=cx(n)
    s=0
    for x in R:
        c=chi6(x,n,fs)
        if c==0: continue
        s+=c**j*e(cx(x)/nc)
    return s/math.sqrt(N)
# primary primes up to norm bound, excluding those above 2,3
B=400
PRIMES=[]
for a in range(-40,41):
    for b in range(-40,41):
        x=(a,b)
        if norm(x)<=B and is_prime_elt(x) and x[0]%3==1 and x[1]%3==0 and norm(x)%2 and norm(x)%3:
            if x not in PRIMES: PRIMES.append(x)
PRIMES.sort(key=norm)
print("primary primes (norm<=%d, excl. 2,3):"%B, len(PRIMES))
maxerr={}
def check(n,fs,mu):
    N=norm(n); al=cx(n)/abs(cx(n))
    g1,g2,g3,gm1=(gamma(j,n,fs) for j in (1,2,3,-1))
    four=(4,0); G=chi6(four,n,fs).conjugate()*g3
    chim1=chi6((-1,0),n,fs)
    errs={
     'g2^3 = mu*alpha': abs(g2**3-mu*al),
     'g1*g2 = mu*alpha*G': abs(g1*g2-mu*al*G),
     'g1*g-1 = chi(-1)': abs(g1*gm1-chim1),
     'mu*g-1 = chi(-1) G^-1 conj(alpha) g2': abs(mu*gm1-chim1/G*al.conjugate()*g2),
     '|G|=1': abs(abs(G)-1)}
    for k,v in errs.items(): maxerr[k]=max(maxerr.get(k,0),v)
for p in PRIMES:
    check(p,[p],-1)
cnt=0
for p,q in itertools.combinations(PRIMES[:14],2):
    n=mul(p,q); check(n,[p,q],1); cnt+=1
for p,q,r in itertools.combinations(PRIMES[:7],3):
    n=mul(mul(p,q),r); check(n,[p,q,r],-1); cnt+=1
print("composites checked:",cnt)
for k,v in maxerr.items(): print("%-40s max error %.2e"%(k,v))
