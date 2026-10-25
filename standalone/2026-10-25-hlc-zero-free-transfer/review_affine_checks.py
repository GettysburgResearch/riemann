"""Finite orientation check over actual Eisenstein primary ideals.
No asymptotic estimate or analytic zero-free claim is tested here.
"""
import cmath, json, math
import numpy as np


def mul(z,w):
    a,b=z;c,d=w
    return (a*c-b*d,a*d+b*c-b*d)
def sub(z,w): return (z[0]-w[0],z[1]-w[1])
def norm(z): a,b=z;return a*a-a*b+b*b
def div(z,w):
    c,d=w;num=mul(z,(c-d,-d));q=norm(w)
    return None if num[0]%q or num[1]%q else (num[0]//q,num[1]//q)
def powe(z,e):
    r=(1,0)
    while e:
        if e&1:r=mul(r,z)
        z=mul(z,z);e//=2
    return r
def emb(z): return z[0]+z[1]*complex(-.5,math.sqrt(3)/2)
Nmax=140
bound=int(2*math.sqrt(Nmax))+1
ideals=sorted([(a,b) for a in range(-bound,bound+1) for b in range(-bound,bound+1)
                if a%3==1 and b%3==0 and 1<=norm((a,b))<=Nmax and math.gcd(norm((a,b)),6)==1],
               key=lambda z:(norm(z),z))
primes=[];fac={};mu={}
for n in ideals:
    if n==(1,0):fac[n]={};mu[n]=1;continue
    rem=n;ff={}
    for p in primes:
        if norm(p)>norm(rem):break
        while (q:=div(rem,p)) is not None:
            ff[p]=ff.get(p,0)+1;rem=q
    if rem!=(1,0):
        assert rem==n
        primes.append(n);ff[n]=1
    fac[n]=ff
    mu[n]=0 if any(e>1 for e in ff.values()) else (-1)**len(ff)
units=[(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]
def symbol_prime(u,p):
    if div(u,p) is not None:return 0j
    v=powe(u,(norm(p)-1)//6)
    found=[r for r in units if div(sub(v,r),p) is not None]
    assert len(found)==1,(u,p,found)
    return emb(found[0])
def psi(u,n):
    z=(emb(n)/abs(emb(n)))**(-1)*norm(n)**(.37j)
    for p,e in fac[n].items():z*=symbol_prime(u,p)**e
    return z
D=55
cols=[n for n in ideals if D<norm(n)<2*D]
rows=[n for n in ideals if 7<=norm(n)<=49 and mu[n]!=0][:7]
w=np.array([.7+.19*j for j in range(len(rows))])
A=np.array([[math.sqrt(wj)*psi(u,n) for n in cols] for wj,u in zip(w,rows)],dtype=complex)
def profile(n):
    y=norm(n)/D
    return math.exp(4-1/((y-1)*(2-y)))*(1+.3j*y)
c=np.array([mu[n]*profile(n) for n in cols])
# Complex, noncoordinate frame makes conjugation errors observable.
frame=np.array([[1+.13j*r,(-1)**r+.21j*(r+1)] for r in range(len(rows))],dtype=complex)
P=frame@np.linalg.inv(frame.conj().T@frame)@frame.conj().T
Pi=np.eye(len(rows))-P
assert np.linalg.norm(Pi@Pi-Pi)<1e-12
results={}
for label,Z in [('full',A),('projected',Pi@A)]:
    K=Z.T@Z.conj() # linear in its first column argument
    I=float(np.vdot(Z@c,Z@c).real/D)
    diagonal=float(sum(abs(c[j])**2*K[j,j].real for j in range(len(cols)))/D)
    T=0j;terms=0
    for ni,n in enumerate(cols):
        for p in fac[n]:
            a=div(n,p)
            if div(a,p) is not None:continue
            VD=math.log(D)/math.log(norm(n))*profile(n)
            for mi,m in enumerate(cols):
                if m==n:continue
                h=sub(m,n)
                assert h[0]%3==0 and h[1]%3==0
                T+=mu[a]*mu[m]*math.log(norm(p))*K[ni,mi]*VD*profile(m).conjugate()
                terms+=1
    rhs=diagonal-T/(D*math.log(D))
    assert abs(rhs-I)<1e-12,(label,I,rhs)
    assert abs(T.imag)<1e-11
    wrong=float((c@K.T@c.conj()).real/D)
    results[label]={'I':I,'diagonal':diagonal,'T_real':T.real,'T_imag':T.imag,
                    'identity_error':abs(rhs-I),'reversed_kernel_error':abs(wrong-I),'summands':terms}
assert np.all(np.real(np.diag((Pi@A).T@(Pi@A).conj()))<=np.real(np.diag(A.T@A.conj()))+1e-12)
assert results['projected']['reversed_kernel_error']>1e-6
print(json.dumps({'primary_ideals':len(ideals),'rows':len(rows),'columns':len(cols),'checks':results},indent=2))
