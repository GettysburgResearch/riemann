"""Finite checks for exact signed ideal convolutions and angular ray grouping.
A formal Eisenstein ideal monoid, using split prime pairs and inert prime ideals;
not a verification of analytic estimates, which are proved separately.
"""
from collections import defaultdict
from itertools import product
from math import isqrt, pi, exp
import cmath, json


def primes(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,isqrt(p)+1))]


def split_generator(p):
    # N(a+b omega)=a^2-ab+b^2 for omega=(-1+i sqrt3)/2
    for b in range(1,isqrt(4*p//3)+3):
        for a in range(-isqrt(4*p)-5,isqrt(4*p)+6):
            if a*a-a*b+b*b==p:
                return complex(a-b/2,b*3**.5/2)
    raise AssertionError(('missing split generator',p))


def setup(Nmax):
    data=[]
    for p in primes(Nmax):
        if p in (2,3): continue
        if p%3==1:
            z=split_generator(p)
            phase=(z/abs(z))**6
            data += [(p,p,'+',phase),(p,p,'-',phase.conjugate())]
        elif p*p<=Nmax:
            data += [(p,p*p,'0',1.+0j)]
    return data


def enum_ideals(data,cap):
    out=[]
    def rec(j,n,exps):
        if j==len(data):
            out.append((tuple(exps),n));return
        _,q,_,_=data[j]
        e=0;m=n
        while m<=cap:
            rec(j+1,m,exps+[e]);e+=1;m*=q
    rec(0,1,[])
    return out


def content_primitive(exps, data):
    j=list(exps);a=1
    pairs={}
    for i,(p,norm,side,phase) in enumerate(data):
        if side in ('+','-'):
            pairs.setdefault(p,{})[side]=i
    for p,idx in pairs.items():
        e=min(j[idx['+']],j[idx['-']]); a*=p**e
        j[idx['+']]-=e;j[idx['-']]-=e
    for i,(p,norm,side,phase) in enumerate(data):
        if side=='0':a*=p**j[i]; j[i]=0
    return a,tuple(j)


def lambda_ideal(exps):return (-1)**sum(exps)

def mu_ideal(exps):
    return 0 if max(exps,default=0)>1 else lambda_ideal(exps)

def chi3(a):return 0 if a%3==0 else (1 if a%3==1 else -1)

def phase_ideal(exps,data):
    z=1.+0j
    for e,(_,_,_,v) in zip(exps,data):z*=v**e
    return z



def lambda_integer(n):
    sign=1; d=2
    while d*d<=n:
        while n%d==0: sign=-sign; n//=d
        d+=1
    return -sign if n>1 else sign

def primitive_generator(j,data):
    z=1.+0j
    for e,(p,q,side,phase) in zip(j,data):
        if not e:continue
        assert side!='0'
        alpha=split_generator(p)
        if side=='-':alpha=alpha.conjugate()
        z*=alpha**e
    return z

def convolutions(allowed,k,mu=True):
    z={tuple([0]*len(allowed[0])):(1,1)}
    # Store integer coefficients, and count of signed-free decomposition paths
    for _ in range(k):
        nz=defaultdict(lambda:(0,0))
        for a,(w,c) in z.items():
            for b in allowed:
                s=tuple(x+y for x,y in zip(a,b))
                v=mu_ideal(b) if mu else 1
                pw,pc=nz[s]; nz[s]=(pw+w*v,pc+c)
        z=nz
    return z


def experiment(X,k):
    data=setup(X)
    allideals=enum_ideals(data,X)
    allowed=[e for e,n in allideals if X/2<n<=X and mu_ideal(e)]
    if not allowed:return {'X':X,'k':k,'empty':True}
    coeff=convolutions(allowed,k)
    rays=defaultdict(complex)
    nonzero=0;testedsigns=0; testchi=0; overlaps=0
    for e,(w,c) in coeff.items():
        n=1
        for x,(_,q,_,_) in zip(e,data):n*=q**x
        assert w==lambda_ideal(e)*c,('signed factorization',e,w,c)
        testedsigns+=1
        a,j=content_primitive(e,data)
        assert n==a*a*__import__('functools').reduce(lambda acc,z:acc*z[1][1]**z[0],zip(j,data),1)
        assert lambda_ideal(e)==lambda_ideal(j)*chi3(a),('radial sign',e,a,j)
        testchi+=1
        overlaps+=int(__import__("math").gcd(a, n//(a*a))>1 and c>0)
        rays[j]+=w
        nonzero+=int(w!=0)
    # Quadratic-form Liouville sign for EVERY pair of primitive output rays.
    det_pairs=0
    entries=[]
    for j in rays:
        alpha=primitive_generator(j,data)
        norm=round(alpha.real**2+alpha.imag**2)
        entries.append((j,alpha,norm))
    for j,alpha,n1 in entries:
        for jj,beta,n2 in entries:
            gamma=alpha*beta.conjugate()
            T=round(2*gamma.real);h=round(2*gamma.imag/(3**.5))
            assert T*T+3*h*h==4*n1*n2,(X,k,j,jj,T,h,n1,n2)
            assert lambda_ideal(j)*lambda_ideal(jj)==lambda_integer(T*T+3*h*h)
            det_pairs+=1
    # Equalities A_l(X)^k=sum_J B_J psi_l(J) for integer l, and
    # the Gaussian angular even moment equals its complete ray Gram expansion.
    checked=0;err=0.
    for ell in range(-10,11):
        base=sum(mu_ideal(e)*phase_ideal(e,data)**ell for e in allowed)
        ray=sum(b*phase_ideal(j,data)**ell for j,b in rays.items())
        rel=abs(base**k-ray)/(1+abs(base)**k)
        err=max(err,rel)
        assert rel<1.e-9,('angular grouping',X,k,ell,rel)
        checked+=1
    R=4
    L=30
    ws=[exp(-ell*ell/(2*R*R)) for ell in range(-L,L+1)]; zsum=sum(ws)
    direct=sum(w*abs(sum(mu_ideal(e)*phase_ideal(e,data)**ell for e in allowed))**(2*k) for ell,w in zip(range(-L,L+1),ws))/zsum
    gram=sum(w*abs(sum(b*phase_ideal(j,data)**ell for j,b in rays.items()))**2 for ell,w in zip(range(-L,L+1),ws))/zsum
    assert abs(direct-gram)<1e-7*max(1,direct), (direct,gram)
    return {'X':X,'k':k,'allowed':len(allowed),'output_ideals':len(coeff),'rays':len(rays),'signed_coefficients':testedsigns,'chi_checks':testchi,'overlap_witnesses':overlaps,'determinant_pairs':det_pairs,'angular_indices':checked,'maximum_relative_error':round(err,13),'moment':round(direct,8)}

if __name__=='__main__':
    cases=[(20,1),(20,2),(20,3),(40,1),(40,2),(70,1),(70,2),(100,2)]
    out={'scope':'finite exact monoid and floating angular identity; not the infinite moment bound','checks':[experiment(*x) for x in cases]}
    print(json.dumps(out,sort_keys=True,indent=2))
