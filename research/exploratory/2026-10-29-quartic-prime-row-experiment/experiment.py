#!/usr/bin/env python3
"""Gaussian quartic prime-row experiment; rationally reproducible, not a proof."""
import argparse, csv, math, cmath
import numpy as np


def prime_sieve(n):
    a=bytearray(b'\1')*(n+1); a[0:2]=b'\0\0'
    for p in range(2,math.isqrt(n)+1):
        if a[p]: a[p*p:n+1:p]=bytes(len(a[p*p:n+1:p]))
    return [i for i in range(2,n+1) if a[i]]


def spf_sieve(n):
    a=list(range(n+1))
    for p in range(2,math.isqrt(n)+1):
        if a[p]==p:
            for j in range(p*p,n+1,p):
                if a[j]==j:a[j]=p
    return a


def primary(a,b):
    for x,y in [(a,b),(-b,a),(-a,-b),(b,-a)]:
        if (x-1)%2==0 and y%2==0 and (((x-1)//2-y//2)%2)==0:
            return x,y
    raise ValueError((a,b))


def gauss_mu(a,b,q,spf):
    sign=1; k=q
    while k>1:
        p=spf[k]; e=0
        while k%p==0:k//=p;e+=1
        if p==2: raise ValueError('only odd ideals are enumerated')
        if p%4==3:
            if e!=2:return 0
            sign=-sign
        elif e==1:
            sign=-sign
        elif e==2:
            if a%p or b%p:return 0
        else:return 0
    return sign


def weight(y, profile):
    if not 1<y<2:return 0.
    if profile=='annular':return 1.
    return math.exp(4.-1./((y-1)*(2-y)))


def columns(scale, beta, profile, mobius):
    cap=math.ceil(2*scale);spf=spf_sieve(cap)
    aa=[];bb=[];cc=[]
    for a in range(1,math.isqrt(cap)+1):
        for b in range(0,math.isqrt(cap-a*a)+1):
            q=a*a+b*b
            if q%2==0 or not scale<q<2*scale:continue
            v=gauss_mu(a,b,q,spf) if mobius else 1
            if not v:continue
            x,y=primary(a,b)
            aa.append(x);bb.append(y);cc.append(v*weight(q/scale,profile)*(q/scale)**(-beta)/math.sqrt(scale))
    return np.array(aa,dtype=np.int64),np.array(bb,dtype=np.int64),np.array(cc,dtype=float)


def sum_squares(p):
    for b in range(1,math.isqrt(p)+1):
        a=math.isqrt(p-b*b)
        if a*a+b*b==p:return a,b
    raise ValueError(p)


def one(X,beta,profile,max_rows):
    D=X**(10/13);N=X**(5/13)
    a,b,c=columns(D,beta,profile,True)
    x,y,z=columns(N,beta,profile,False)
    # At p=1 mod 8, quartic reciprocity has trivial sign between primary
    # generators. This fixes the ray sector for the source orientation.
    rows=[p for p in prime_sieve(2*X) if p>=X and p%8==1]
    if max_rows and len(rows)>max_rows:
        # Deterministic uniform-in-index sample across full annulus.
        rows=[rows[(j*len(rows))//max_rows] for j in range(max_rows)]
    vM=[];vS=[]
    for p in rows:
        ra,rb=primary(*sum_squares(p));root=(-ra*pow(rb,-1,p))%p
        # Table maps exact fourth-power residues to their fixed complex roots.
        root_map={1:1+0j,p-1:-1+0j,root:1j,(-root)%p:-1j,0:0j}
        table=np.fromiter((root_map[pow(k,(p-1)//4,p)] for k in range(p)), dtype=np.complex128,count=p)
        M=np.dot(c,table[(a+b*root)%p]);S=np.dot(z,table[(x+y*root)%p])
        vM.append(abs(M)**2);vS.append(abs(S)**2)
    M=np.asarray(vM);S=np.asarray(vS);q=len(rows)
    if not q:raise ValueError('no rows')
    A=float(M.mean());B=float(S.mean());C=float((M*S).mean())
    M4=float((M*M).mean());S4=float((S*S).mean())
    return dict(X=X,rows=q,D=D,N=N,inverse_cols=len(c),ordinary_cols=len(z),M2=A,S2=B,mixed=C,
        correlation=C/(A*B) if A*B else 0,cauchy_ratio=C/math.sqrt(M4*S4) if M4*S4 else 0,
        M4=M4,S4=S4,max_M2=float(M.max()),max_S2=float(S.max()),
        formal_spike_rows=int(np.sum((M>=D**.6)&(S>=N**.6))))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--scales',nargs='+',type=int,default=[1000,3000,10000,30000]);p.add_argument('--beta',type=float,default=.8);p.add_argument('--profile',choices=['smooth','annular'],default='smooth');p.add_argument('--max-rows',type=int,default=400);args=p.parse_args()
    writer=None
    for X in args.scales:
        row=one(X,args.beta,args.profile,args.max_rows)
        if writer is None:
            writer=csv.DictWriter(__import__('sys').stdout,fieldnames=row.keys());writer.writeheader()
        writer.writerow(row)
