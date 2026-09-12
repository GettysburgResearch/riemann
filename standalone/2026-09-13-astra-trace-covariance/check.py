#!/usr/bin/env python3
"""Bounded exact/interval checks for TC26. No test proves the open RH bound."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

BITS = 512
SCALE = 1 << BITS
CUTOFF = 8192
MAX_N = 16

class CheckError(Exception):
    pass

def require(ok, msg):
    if not ok:
        raise CheckError(msg)

def enc(x):
    x = F(x)
    return [str(x.numerator), str(x.denominator)]

def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def integ(p, lo=F(0), hi=F(1)):
    return sum((x*(hi**(i+1)-lo**(i+1))/F(i+1) for i,x in enumerate(p)), F(0))

def at(p, x):
    return sum((a*x**i for i,a in enumerate(p)), F(0))

def legendre(l):
    p = [F(0)]*(l+1)
    for k in range(l//2+1):
        p[l-2*k] = F((-1)**k*math.factorial(2*l-2*k),
            2**l*math.factorial(k)*math.factorial(l-k)*math.factorial(l-2*k))
    return p

def recurrence(L):
    out = [[F(1)], [F(0),F(1)]]
    for l in range(1,L):
        p=[F(0)]*(l+2)
        for k,a in enumerate(out[-1]): p[k+1] += F(2*l+1,l+1)*a
        for k,a in enumerate(out[-2]): p[k] -= F(l,l+1)*a
        out.append(p)
    return out

def psi(p):
    out=[F(0)]*len(p)
    for r in range(1,len(p),2):
        out[r] = -p[r]/r
        out[0] += p[r]/r
    return out

def mobius_sieve(N):
    mu=[1]*(N+1); mu[0]=0
    prime=[True]*(N+1)
    for p in range(2,N+1):
        if not prime[p]: continue
        for n in range(p,N+1,p):
            prime[n]=False
            mu[n] = -mu[n]
        for n in range(p*p,N+1,p*p): mu[n]=0
    return mu

def trial(n):
    if n==1: return 1
    ans=1; p=2
    while p*p<=n:
        if n%p==0:
            n//=p; ans=-ans
            if n%p==0: return 0
        p+=1
    if n>1: ans=-ans
    return ans

# Every operation rounds outwards to a fixed dyadic mesh.
def iv(x):
    if isinstance(x, tuple): return x
    f=F(x)*SCALE
    return (f.numerator//f.denominator, -((-f.numerator)//f.denominator))

def add(x,y):
    x,y=iv(x),iv(y); return x[0]+y[0],x[1]+y[1]

def neg(x):
    x=iv(x); return -x[1],-x[0]

def sub(x,y): return add(x,neg(y))

def times(x,y):
    x,y=iv(x),iv(y)
    z=[a*b for a in x for b in y]
    return min(z)//SCALE, -((-max(z))//SCALE)

def reciprocal(x):
    x=iv(x); require(x[0]>0,'reciprocal domain')
    return SCALE*SCALE//x[1], -((-SCALE*SCALE)//x[0])

def power(x,n):
    out=iv(1)
    for _ in range(n): out=times(out,x)
    return out

def total(xs):
    z=iv(0)
    for x in xs: z=add(z,x)
    return z

def overlap(a,b): return max(a[0],b[0])<=min(a[1],b[1])

def arctan_inv(q):
    z=iv(0); k=0
    while True:
        term=F((-1)**k,(2*k+1)*q**(2*k+1))
        z=add(z,term)
        k+=1
        rem=F(1,(2*k+1)*q**(2*k+1))
        if rem < F(1,1 << (BITS+16)):
            # Alternating-series remainder lies between zero and next term.
            return (add(z,(-iv(rem)[1],0)) if k%2
                    else add(z,(0,iv(rem)[1])))

def pi_interval():
    return sub(times(16,arctan_inv(5)), times(4,arctan_inv(239)))

def bernoulli(N):
    B=[F(1)]
    for n in range(1,N+1):
        B.append(-sum((F(math.comb(n+1,k))*B[k] for k in range(n)),F(0))/F(n+1))
    return B

def even_zeta_odd(s,pi,B):
    k=s//2
    z=times(F((-1)**(k+1))*B[s]/(2*math.factorial(s)), power(times(2,pi),s))
    return times(1-F(1,2**s),z)

def receipt_iv(x):
    # Less unwieldy, still outward, 100-bit presentation mesh.
    sh=BITS-100
    return [str(x[0]//(1<<sh)), str(-((-x[1])//(1<<sh))), '100']

def poly_norm_iv(p):
    return total(times(times(a,b), F(3**(i+j+1)-1,i+j+1))
                 for i,a in enumerate(p) for j,b in enumerate(p))

def digest(payload):
    return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def reconstruct():
    mu=mobius_sieve(CUTOFF)
    require(all(mu[n]==trial(n) for n in range(1,CUTOFF+1)), 'Mobius paths')
    rec=recurrence(63)
    primitives=[]
    for j in range(32):
        l=2*j+1; p=legendre(l); require(p==rec[l],'Rodrigues/recurrence')
        ps=psi(p)
        v=(2*l+1)*integ(mul(ps,ps))
        require(v==F(1,j+1),'primitive energy')
        c=ps[0]
        expected=F((-1)**j*4**j*math.factorial(j)**2,math.factorial(2*j+1))
        require(c==expected,'primitive boundary')
        primitive=[F(0)]*(l+2)
        for r,a in enumerate(p): primitive[r+1] = -a/F(r+1)
        primitive[0] = integ(p)
        fenergy=(2*l+1)*integ(mul(primitive,primitive))
        require(fenergy==F(2,(2*l-1)*(2*l+3)),'primitive-of-Legendre energy')
        primitives.append([j,enc(v),enc(fenergy),enc((2*l+1)*c*c)])

    parseval_controls=[]
    for N in (1,2,4,8,16,32):
        for x in (F(1,64),F(1,16),F(1,4),F(1,2),F(3,4),F(1)):
            value=sum((F(4*j+3)*at(psi(legendre(2*j+1)),x)**2
                       for j in range(N)),F(0))
            require(value <= 1/x-1, 'finite Parseval upper bound')
            parseval_controls.append([N,enc(x),enc(value)])

    # Two finite decompositions: direct divisor interval integration versus
    # compensated polynomial formula; no limiting sum is used in these checks.
    cutoff_checks=[]; pair_checks=[]
    for j in range(4):
        l=2*j+1;p=legendre(l);ps=psi(p)
        Fp=[F(0)]+[p[r]/r if r else F(0) for r in range(1,l+1)]
        for R in (3,7,15,31):
            acc=[F(0)]*(l+1)
            mR=sum((F(mu[n],n) for n in range(1,R+1,2)),F(0))
            atoms=[]
            for n in range(3,R+1,2):
                a=[F(mu[n],n)*ps[r]/n**r for r in range(l+1)]
                atoms.append(a)
                for r in range(l+1): acc[r]+=a[r]
            corrected=[-a for a in acc];corrected[0]+=ps[0]*mR
            for t in (F(1),F(4,3),F(2),F(8,3),F(3)):
                direct=sum((F(mu[n],n)*at(Fp,min(F(1),t/n))
                            for n in range(1,R+1,2)),F(0))
                require(direct==at(corrected,t),'finite source identity')
            diag=sum((integ(mul(a,a),F(1),F(3)) for a in atoms),F(0))*(2*l+1)
            signed=integ(mul(acc,acc),F(1),F(3))*(2*l+1)
            cross=sum((integ(mul(a,b),F(1),F(3)) for i,a in enumerate(atoms)
                       for k,b in enumerate(atoms) if i!=k),F(0))*(2*l+1)
            require(signed==diag+cross,'complete ordered covariance')
            weight=F(0)
            # Independently integrate the complete finite step density in x.
            for n in range(3,R+1,2):
                weight+=F(mu[n]**2,n)*integ(mul(ps,ps),F(1,n),F(3,n))*(2*l+1)
            require(diag==weight,'finite squarefree density')
            cutoff_checks.append([j,R,enc(diag),enc(signed),enc(cross)])
            if j==0: pair_checks.append([R,enc(cross)])

    # Euler-Walsh orthogonality: enumerate all prime signs, no random sampling.
    primes=(3,5,7); ns=[math.prod(primes[i] for i in range(3) if mask>>i&1)
                       for mask in range(1,8)]
    random_checks=[]
    for j in range(3):
        l=2*j+1;ps=psi(legendre(l)); expected=F(0); observed=F(0)
        for n in ns:
            a=[ps[r]/(n**(r+1)) for r in range(l+1)]
            expected+=integ(mul(a,a),F(1),F(3))*(2*l+1)
        for signs in range(8):
            acc=[F(0)]*(l+1)
            for mask,n in enumerate(ns,1):
                sign=(-1)**((mask&signs).bit_count())
                for r in range(l+1): acc[r]+=sign*ps[r]/n**(r+1)
            observed+=integ(mul(acc,acc),F(1),F(3))*(2*l+1)/8
        require(expected==observed,'Walsh all-configuration identity')
        random_checks.append([j,enc(expected)])

    pi=pi_interval(); require(pi[0]>3*SCALE and pi[1]<F(22,7)*SCALE,'pi bracket')
    alpha=times(4,reciprocal(power(pi,2)))
    count=0
    for X in range(1,CUTOFF+1):
        if X%2: count+=mu[X]**2
        err=sub(count,times(alpha,X))
        require(max(abs(err[0]),abs(err[1]))**2 <= 4*X*SCALE*SCALE,
                'squarefree counting error control')
    B=bernoulli(4*MAX_N)
    # A_s=sum_{odd n>=3} mu(n)^2/n^s. A_2 is exact in pi;
    # all higher tails are paid by the integral bound, not discarded.
    moments={2:sub(times(12,reciprocal(power(pi,2))),1)}
    for s in range(3,4*MAX_N+1):
        low=sum(SCALE//(n**s) for n in range(3,CUTOFF+1,2) if mu[n])
        count=sum(bool(mu[n]) for n in range(3,CUTOFF+1,2))
        moments[s]=add((low,low+count), (0,iv(F(1,(s-1)*CUTOFF**(s-1)))[1]))
    # Check A2 independently against its literal complete-tail enclosure.
    low=sum(SCALE//(n*n) for n in range(3,CUTOFF+1,2) if mu[n])
    count=sum(bool(mu[n]) for n in range(3,CUTOFF+1,2))
    require(overlap(moments[2],add((low,low+count),(0,iv(F(1,CUTOFF))[1]))),'A2 Euler/direct')
    S=iv(0);D=iv(0); rows=[];columns=[]
    for j in range(MAX_N):
        l=2*j+1;p=legendre(l);ps=psi(p)
        qq=mul(ps,ps)
        dj=times(2*l+1,total(times(a*F(3**(k+1)-1,k+1),moments[k+2])
                              for k,a in enumerate(qq)))
        out=[iv(0)]*(l+1);out[0]=iv(ps[0])
        for r in range(1,l+1,2):
            out[r]=times(p[r]/r,sub(reciprocal(even_zeta_odd(r+1,pi,B)),1))
        sj=times(2*l+1,poly_norm_iv(out))
        require(dj[0]>0 and sj[0]>0,'positive column intervals')
        S=add(S,sj);D=add(D,dj)
        columns.append([j,receipt_iv(sj),receipt_iv(dj)])
        if j+1 in(1,2,4,8,16): rows.append([j+1,receipt_iv(S),receipt_iv(D),receipt_iv(sub(S,D))])
    # Strict native controls: total covariance is NOT nonpositive at all N.
    require(F(int(rows[0][3][0]),1<<100)>1,'native positive covariance')
    require(F(int(rows[1][3][0]),1<<100)>F(int(rows[0][3][1]),1<<100),'covariance initially increases')
    # Exact basis constants for separate positive/negative divergence.
    divergence_constants=[enc(sum((F(4*j+3)*psi(legendre(2*j+1))[0]**2
                                  for j in range(N)),F(0))) for N in(1,2,4,8)]
    payload={'schema':'TC26-v1','status':'PROPOSED; native covariance upper bound OPEN; RH not proved',
             'bits':BITS,'squarefree_cutoff':CUTOFF,'max_trace_degree_count':MAX_N,
             'primitive_checks':primitives,'parseval_controls':parseval_controls,'finite_source_covariances':cutoff_checks,
             'walsh_controls':random_checks,'native_columns':columns,'native_traces':rows,
             'positive_divergence_basis_constants':divergence_constants,
             'scope':{'mobius_comparisons':CUTOFF,'primitive_degrees':32,'parseval_panels':36,'squarefree_count_panels':CUTOFF,
                      'finite_source_panels':16,'finite_source_point_checks':80,
                      'walsh_models':3,'walsh_sign_assignments_per_model':8,
                      'native_trace_cutoffs':5,'analytic_proofs_machine_verified':False,
                      'independent_mathematical_review':False}}
    return payload

def reject_duplicates(pairs):
    d={}
    for k,v in pairs:
        if k in d: raise CheckError('duplicate JSON key')
        d[k]=v
    return d

def strict_types(x):
    if type(x) is float: raise CheckError('float receipt forbidden')
    if type(x) is dict:
        for v in x.values(): strict_types(v)
    elif type(x) is list:
        for v in x: strict_types(v)

def accept(record, expected):
    strict_types(record)
    require(type(record) is dict and set(record)=={'payload','sha256'},'receipt fields')
    require(record['sha256']==digest(record['payload']),'payload hash')
    # Compare canonical encodings, so True cannot alias 1.
    require(json.dumps(record['payload'],sort_keys=True,separators=(',',':'))==
            json.dumps(expected,sort_keys=True,separators=(',',':')),'primitive reconstruction')

def self_test(expected):
    pristine={'payload':expected,'sha256':digest(expected)};accept(pristine,expected)
    changes=[('status','RH proved'),('bits',True),('squarefree_cutoff',4),
             ('max_trace_degree_count',100000),('primitive_checks',[]),
             ('finite_source_covariances',[]),('walsh_controls',[]),
             ('native_traces',[]),('scope',{}),('positive_divergence_basis_constants',[])]
    for key,val in changes:
        bad=copy.deepcopy(pristine);bad['payload'][key]=val;bad['sha256']=digest(bad['payload'])
        try: accept(bad,expected)
        except CheckError: pass
        else: raise CheckError('accepted resealed change '+key)
    try: json.loads('{"x":1,"x":2}',object_pairs_hook=reject_duplicates)
    except CheckError: pass
    else: raise CheckError('accepted duplicate')
    return len(changes)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path);parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args();expected=reconstruct()
    if args.check:
        record=json.loads(args.check.read_text(),object_pairs_hook=reject_duplicates,
                          parse_float=lambda _: (_ for _ in ()).throw(CheckError('float JSON')))
        accept(record,expected)
    if args.write:
        args.write.write_text(json.dumps({'payload':expected,'sha256':digest(expected)},sort_keys=True,separators=(',',':'))+'\n')
    rejected=self_test(expected) if args.self_test else 0
    print('PASS TC26',digest(expected),'resealed_refusals',rejected)
    print(json.dumps(expected['native_traces']))

if __name__=='__main__':
    try: main()
    except (CheckError,OSError,ValueError,ZeroDivisionError) as e:
        raise SystemExit('FAIL: '+str(e))
