#!/usr/bin/env python3
"""Independent full-Gram controls for RN minima and DO/BG/BL finite claims.

This imports only the sibling reviewer arithmetic, never an author's producer.
Each pair uses its own period and a complete Euler--Maclaurin tail enclosure.
The proposed coefficients/dual variables come from rational midpoint KKT;
acceptance uses exact feasible parametrization and a rigorous residual floor.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
import argparse
import importlib.util
import json
import hashlib
import math
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reviewer_pass3_checks',HERE/'checks.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
I=m.I;S=m.SCALE;need=m.need;solve=m.solve;logq=m.logq
B=(F(1,6),F(-1,30),F(1,42),F(-1,30),F(5,66),F(-691,2730),F(7,6),F(-3617,510))


def small_log(a):
    z=I.q(F(1,2*a+1));t=z; z2=z.sq(); v=I.q(0)
    for j in range(18):
        v+=t*F(2,2*j+1);t*=z2
    rem=2*t/(37*(1-z2))
    return I(v.lo,v.hi+rem.hi)


@lru_cache(None)
def weight(q,r):
    a=r+32*q
    value=I.q(0)
    for k in range(32):value+=I.q(F(1,(r+k*q)*(r+1+k*q)))
    value+=small_log(a)/q+I.q(F(1,2*a*(a+1)))
    last=I.q(0)
    for j,b in enumerate(B,1):
        # Exact rational term differences avoid severe interval dependency loss.
        term=b/F(2*j)*q**(2*j-1)*(F(1,a**(2*j))-F(1,(a+1)**(2*j)))
        value+=I.q(term)
        if j==8:last=I.q(abs(term))
    return I(value.lo-last.hi,value.hi+last.hi)


@lru_cache(None)
def gram(i,j):
    if i>j:return gram(j,i)
    q=math.lcm(i,j); lo=0;hi=0
    for r in range(1,q):
        c=F((r%i)*(r%j),i*j)
        if not c:continue
        v=weight(q,r)
        lo+=v.lo*c.numerator//c.denominator
        hi+=m.ceildiv(v.hi*c.numerator,c.denominator)
    need(lo>0,'positive actual Gram entry','gram_entries')
    return I(lo,hi)


def dot(a,b):return sum((x*y for x,y in zip(a,b)),I.q(0))
def quadratic(a,G):return sum((a[i]*a[j]*G[i][j] for i in range(len(a)) for j in range(len(a))),I.q(0))


def rn_minima():
    expected={2:('0.072123117281951','0.072123117281952'),
              4:('0.026111243144081','0.026111243144082'),
              8:('0.023695806559291','0.023695806559292'),
              16:('0.022118909935520','0.022118909935521')}
    out=[]
    for Y,N in ((2,4),(4,8),(8,16),(16,32)):
        indices=list(range(2,N+1));tail=list(range(Y,N+1));t=len(tail)
        G=[[gram(i,j) for j in indices] for i in indices]
        C0=[F(1,n) for n in tail];C1=[(logq(n)/n).mid() for n in tail]
        prefix={n:F(m.mu(n)) for n in range(1,Y)}
        s0=sum((a/n for n,a in prefix.items()),F(0))
        s1=sum((a*(logq(n)/n).mid() for n,a in prefix.items()),F(0))
        A=[[G[i-2][j-2].mid() for j in tail]+[C0[k],C1[k]] for k,i in enumerate(tail)]
        A += [C0+[F(0),F(0)],C1+[F(0),F(0)]]
        rhs=[-sum((a*G[i-2][n-2].mid() for n,a in prefix.items() if n>=2),F(0)) for i in tail]
        proposal=solve(A,rhs+[-s0,-1-s1])
        # Free values rational; endpoint formulas make the actual log constraints exact.
        coef={n:I.q(a) for n,a in prefix.items()}
        for n,a in zip(tail,proposal):
            if n not in (Y,N):coef[n]=I.q(a)
        s0i=sum((a/n for n,a in coef.items()),I.q(0))
        s1i=sum((a*logq(n)/n for n,a in coef.items()),I.q(0))
        y=(-1-s1i+s0i*logq(Y))/logq(2);x=-s0i-y
        coef[Y]=Y*x;coef[N]=N*y
        aa=[coef[n] for n in indices]
        value=quadratic(aa,G)-1
        # KKT signs: G a + C^T proposal_dual=0, use lambda=-proposal_dual.
        dual=[-proposal[-2],-proposal[-1]]
        r=[]
        for n in tail:
            r.append(dot(G[n-2],aa)-dual[0]/n-dual[1]*logq(n)/n)
        residual=sum((v.sq() for v in r),I.q(0))
        lam0=F(1,4*(N//Y)**2*N*(N+1))
        bound=I(value.lo-(residual/lam0).hi,value.hi)
        need(bound.within(*expected[Y]),'RN entire affine minimum enclosure','rn')
        need(sum((a/n for n,a in coef.items()),I.q(0)).contains(0),'RN balance control','rn')
        need(sum((a*logq(n)/n for n,a in coef.items()),I.q(0)).contains(-1),'RN derivative control','rn')
        out.append({'Y':Y,'N':N,'minimum':bound.data(),'trial':value.data(),
                    'stationarity_squared_upper':residual.data(),'coercivity':str(lam0),
                    'feasibility':'symbolic endpoint identities, not merely zero-containing intervals',
                    'proposal_sha256':hashlib.sha256(''.join(hex(v.numerator)+'/'+hex(v.denominator)+'\n' for v in proposal).encode()).hexdigest(),
                    'proposal_reproduction':'deterministic rational midpoint KKT above; actual endpoints imposed symbolically'})
    return out


def projection(N):
    ids=list(range(2,N+1)); G=[[gram(i,j) for j in ids] for i in ids]
    b=[logq(k)/k for k in ids]
    c=solve([[a.mid() for a in row] for row in G],[x.mid() for x in b])
    r=[dot(row,c)-bb for row,bb in zip(G,b)]
    # Direct dictionary duals give an independent full Gram floor.
    # finite differences + divisor inversion with at most N summands suffice.
    lam=F(1,4*N*N*N*(N+1))
    residual=sum((v.sq() for v in r),I.q(0))
    val=1-2*dot(c,b)+quadratic(c,G)
    bound=I(val.lo-(residual/lam).hi,val.hi)
    # Enclose the exact optimizer via ||c-c*|| <= ||r||/lam.
    rad=(residual.sqrt()/lam).hi
    exact=[I(I.q(x).lo-rad,I.q(x).hi+rad) for x in c]
    return ids,G,b,bound,exact


def do_bg():
    ids,G,b,delta8,c8=projection(8)
    ids16,G16,b16,delta16,c16=projection(16)
    need(delta8.within('0.024244525306','0.024244525307'),'delta8','do_bg')
    need(delta16.within('0.017936267020','0.017936267021'),'delta16','do_bg')
    # Dilation cross-coupling H_ik = G_i,2k-G_i,2/k.
    H=[[gram(i,2*k)-gram(i,2)/k for k in ids] for i in ids]
    leak=(1-delta8)/2-quadratic(c8,H)
    need(leak.within('-0.001714996317','-0.001714996316'),'actual negative leakage','do_bg')
    # Full coupled odd coefficient is minus coefficient of h_9 in full projection.
    a9=-c16[9-2]
    need(a9.within('-0.105967221800','-0.105967221797'),'full nonsquarefree correction','do_bg')
    # Detail minimizer a*, lifted as sum a_k(2h_2/k-h_k), k odd incl 1.
    odds=list(range(1,17,2)); pi=m.pi_interval()
    astar=[]
    for k in odds:
        v=k*k*sum((F(m.mu(d//k)*m.mu(d),m.j2(d)) for d in odds if d%k==0),F(0))
        astar.append(8*v/pi.sq())
    hcoef=[I.q(0) for _ in ids16]
    for k,a in zip(odds,astar):
        hcoef[0]+=2*a/k
        if k>1:hcoef[k-2]-=a
    # Best old-coarse correction: minimize ||chi-Ha-D_2 v|| over v in B8.
    coarse_rhs=[]
    for j in ids:
        dj=[I.q(0) for _ in ids16];dj[2*j-2]=I.q(1);dj[0]-=F(1,j)
        coarse_rhs.append(dot(dj,b16)-dot(dj,[dot(row,hcoef) for row in G16]))
    coarse_G=[[x/2 for x in row] for row in G]
    v=solve([[x.mid() for x in row] for row in coarse_G],[x.mid() for x in coarse_rhs])
    trial=hcoef[:]
    for j,a in zip(ids,v): trial[2*j-2]+=a;trial[0]-=a/j
    Uval=1-2*dot(trial,b16)+quadratic(trial,G16)
    res=[dot(row,v)-rhs for row,rhs in zip(coarse_G,coarse_rhs)]
    normres=sum((x.sq() for x in res),I.q(0))
    floor=F(1,8*8**3*9)
    U=I(Uval.lo-(normres/floor).hi,Uval.hi)
    need(U.within('0.025491663369','0.025491663370'),'detail lift U8','do_bg')
    need(U.lo>delta8.hi,'actual detail lift is worse than old optimum','do_bg')
    return {'delta8':delta8.data(),'delta16':delta16.data(),'leakage':leak.data(),
            'full_a9_16':a9.data(),'detail_lift_U8':U.data(),
            'assurance':'complete pairwise periodic Gram with directed tails; new rational midpoint solves and residual floors'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--group',choices=('rn','do_bg','all'),default='all')
    args=parser.parse_args();out={}
    if args.group in ('rn','all'):out['rn']=rn_minima()
    if args.group in ('do_bg','all'):out['do_bg']=do_bg()
    print(json.dumps({'schema':'riemann.review.pass3.gram-controls.v1',
       'marker':'PASS_COMPLETE_BOUNDED_GRAM_RECONSTRUCTION','results':out,
       'pairwise_gram_entries':gram.cache_info().currsize,'periodic_weights':weight.cache_info().currsize,
       'bits':m.BITS,'checks':m.COUNTS,'author_producer_executed':False,
       'unbounded_minimum_proved':False,'rh_proved':False},sort_keys=True,indent=2))


if __name__=='__main__':main()
