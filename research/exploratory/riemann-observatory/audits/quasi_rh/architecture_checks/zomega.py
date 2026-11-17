# Minimal Z[omega] arithmetic for auditing paper2.tex Lemma 4.1 / App A identities.
# Elements are tuples (a,b) meaning a + b*omega, omega = e^{2 pi i/3}, omega^2 = -1 - omega.
import cmath, math, itertools
W = complex(-0.5, math.sqrt(3)/2)
def mul(x,y):
    a,b=x; c,d=y
    return (a*c - b*d, a*d + b*c - b*d)
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def sub(x,y): return (x[0]-y[0], x[1]-y[1])
def neg(x): return (-x[0],-x[1])
def conj(x):
    a,b=x  # conj(omega)=omega^2=-1-omega
    return (a-b, -b)
def norm(x):
    a,b=x; return a*a - a*b + b*b
def cval(x): return x[0] + x[1]*W
def divexact(x,y):
    n=norm(y); z=mul(x,conj(y))
    assert z[0]%n==0 and z[1]%n==0, (x,y)
    return (z[0]//n, z[1]//n)
def divides(y,x):
    n=norm(y); z=mul(x,conj(y)); return z[0]%n==0 and z[1]%n==0
def rmod(x,m):
    # Euclidean remainder of x modulo m
    n=norm(m); z=mul(x,conj(m))
    q=(round(z[0]/n), round(z[1]/n))
    # try neighbours to minimise norm
    best=None
    for da in (-1,0,1):
        for db in (-1,0,1):
            qq=(q[0]+da,q[1]+db); r=sub(x,mul(qq,m))
            if best is None or norm(r)<norm(best): best=r
    return best
def powmod(x,e,m):
    r=(1,0); x=rmod(x,m)
    while e:
        if e&1: r=rmod(mul(r,x),m)
        x=rmod(mul(x,x),m); e>>=1
    return r
ONE=(1,0); OM=(0,1); OM2=(-1,-1)
UNITS=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]  # 1,-1,w,-w,w^2,-w^2
SIXTH={ (1,0):0, (1,1):1, (0,1):2, (-1,0):3, (-1,-1):4, (0,-1):5 }  # zeta6^k with zeta6 = -w^2 = 1+w
# zeta6 = e^{2pi i/6} = 1+omega? check: 1+w = 0.5 + i sqrt3/2 = e^{i pi/3}. yes.
def unitpow(k):
    k%=6
    for u,e in SIXTH.items():
        if e==k: return u
def is_primary(x): return (x[0]-1)%3==0 and x[1]%3==0
def make_primary(x):
    for u in UNITS:
        y=mul(u,x)
        if is_primary(y): return y
    raise ValueError(x)
LAM=(1,2)  # 1+2w = sqrt(-3)
def primes_upto(N):
    ps=[]
    sieve=[True]*(N+1)
    for i in range(2,N+1):
        if sieve[i]:
            ps.append(i)
            for j in range(i*i,N+1,i): sieve[j]=False
    return ps
def eisenstein_primes(maxnorm):
    out=[]
    for p in primes_upto(maxnorm):
        if p in (2,3): continue
        if p%3==1:
            found=None
            for a in range(-p,p+1):
                for b in range(-p,p+1):
                    if norm((a,b))==p: found=(a,b); break
                if found: break
            pi=make_primary(found); out.append(pi); out.append(make_primary(conj(pi)))
        elif p*p<=maxnorm:
            out.append(make_primary((p,0)))
    out=sorted(set(out), key=lambda x:(norm(x),x))
    return out
def sextic(x,p):
    """(x/p)_6 for primary prime p not dividing 6, as exponent k in 0..5 (value zeta6^k) or None if p|x."""
    if divides(p,x): return None
    q=norm(p); r=powmod(x,(q-1)//6,p)
    for u,e in SIXTH.items():
        if divides(p,sub(r,u)): return e
    raise ValueError('no sixth root', x,p,r)
Z6=cmath.exp(2j*math.pi/6)
def chi(n_factors, x, j=1):
    """chi_n(x)^j for squarefree n given as list of primary primes; zero extension."""
    tot=0
    for p in n_factors:
        k=sextic(x,p)
        if k is None: return 0
        tot+=k*j
    return Z6**(tot%6)
def prod(fs):
    r=ONE
    for f in fs: r=mul(r,f)
    return r
def residues(m):
    """Complete residue system of O mod m via HNF of lattice mO = span(m, m*w)."""
    v1=m; v2=mul(m,OM)
    # integer matrix columns v1,v2 in basis (1,w); compute HNF lower-triangular: find d2 = gcd of b-coords etc.
    n=norm(m)
    # O/mO: use x = a + b w with 0<=b<g, 0<=a<n/g where g = gcd(m_b, (m w)_b)
    g=math.gcd(v1[1],v2[1])
    d1=n//g
    reps=[(a,b) for b in range(g) for a in range(d1)]
    # sanity: distinct mod m
    return reps
def e_add(z):  # z complex; e(z)=exp(4 pi i Im z / sqrt3)
    return cmath.exp(4j*math.pi*z.imag/math.sqrt(3))
def gauss(n_factors, j, shift=ONE):
    n=prod(n_factors); N=norm(n); s=0
    for x in residues(n):
        c=chi(n_factors,x,j)
        if c==0: continue
        s+=c*e_add(cval(mul(shift,x))/cval(n))
    return s/math.sqrt(N)
def alpha(x):
    z=cval(x); return z/abs(z)
