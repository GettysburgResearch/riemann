"""Second arithmetic implementation: derive the full output from the short prefix.
Imports no producer. Independent trial factors + Dirichlet Newton; scalar
interval primitives and grid definition are shared and disclosed.
"""
from array import array
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import argparse
from core import *

def trial_mu(n):
    ans=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;ans=-ans
            if n%p==0:return 0
            while n%p==0:n//=p
        p+=1
    return -ans if n>1 else ans

def newton(Y):
    B=(Y+1)**2-1
    base=[trial_mu(k) for k in range(1,Y+1)]
    z=array('i',[0])*(B+1)
    active=[(i+1,a) for i,a in enumerate(base) if a]
    for r,a in active:
        for s,b in active:z[r*s]+=a*b
    out=array('i',[0])*(B+1)
    for k,a in enumerate(base,1):out[k]=2*a
    for d in range(1,Y*Y+1):
        a=z[d]
        if a:
            for k in range(d,B+1,d):out[k]-=a
    need(all(-1<=a<=1 for a in out[1:]),'native coefficient cap')
    return out

def shapes(r):
    need(type(r) is dict and r.get('schema')=='RSC26-v1','schema')
    need(type(r.get('bits')) is int and r['bits']==BITS,'precision')
    for st in r['stages']:
        need(type(st['Y']) is int and st['Y']>=1,'Y')
        need(type(st['B']) is int and st['B']==(st['Y']+1)**2-1,'square endpoint')
        for k,ep in st['endpoints'].items():
            need(k.isdigit() and type(ep['M']) is int,'endpoint type')
            for field in ['m','H']:
                x=ep[field];need(type(x) is list and len(x)==2 and all(type(t) is int for t in x) and x[0]<=x[1],'interval type')
        for p in st['panels']:
            need(type(p['resolution']) is int and type(p['cells']) is int,'grid types')
            need(type(p['certified_gain']) is bool,'gain type')
            for key,value in p.items():
                if key not in ['resolution','cells','certified_gain']:
                    need(type(value) is list and len(value)==2 and all(type(t) is int for t in value) and value[0]<=value[1], 'panel interval')

def fraction_panel(st,mu):
    """Literal weighted and unweighted cell sums, no endpoint mean formulas."""
    Y=st['Y'];B=st['B'];M=[0]*(B+1);m=[F(0)]*(B+1);H=[F(0)]*(B+2)
    for k in range(1,B+2):
        H[k]=H[k-1]+F(1,k)
        if k<=B:M[k]=M[k-1]+mu[k];m[k]=m[k-1]+F(mu[k],k)
    count=0
    for panel in st['panels']:
        ce=cf=ue=uf=F(0)
        for s,t in cells(Y+1,B,panel['resolution']):
            count+=1;w=[F(1,k*(k+1)) for k in range(s,t+1)];W=sum(w)
            v=sum((w0*M[k] for k,w0 in zip(range(s,t+1),w)),F(0))
            ce+=v*v/W
            cf+=sum(m[s:t+1],F(0))**2/(t-s+1)
            a=sum((w0*k for k,w0 in zip(range(s,t+1),w)),F(0))
            ue+=sum((w0*k*k for k,w0 in zip(range(s,t+1),w)),F(0))-a*a/W
            uf+=sum((x*x for x in H[s:t+1]),F(0))-sum(H[s:t+1],F(0))**2/(t-s+1)
        for key,v in [('coarse_E',ce),('coarse_F',cf),('worst_E',ue),('worst_F',uf)]:
            need(contains(panel[key],rat(v.numerator,v.denominator)),'exact direct panel '+key)
    return count

def endpoint_certificate(st):
    """Check upper completed-state bounds from endpoint data only.
    No measured error, full output energy, or future coefficient is read.
    Harmonic numbers certify the universal Lipschitz loss, not a model fit.
    """
    Y=st['Y'];B=st['B'];X=B+1;eps=st['endpoints']
    def H(k):return tuple(st['H_after']) if k==X else tuple(eps[str(k)]['H'])
    def ep(k):return eps[str(k)]['M'],tuple(eps[str(k)]['m'])
    MY,mY=ep(Y);MB,mB=ep(B)
    uB=sub(mB,rat(MB,X));coarse_bounds=[]
    for p in st['panels']:
        ce=cf=ue=uf=integer(0);count=0
        for s,t in cells(Y+1,B,p['resolution']):
            count+=1;Mt,mt=ep(t);Mp,mp=ep(s-1);l=t-s+1
            W=rat(l,s*(t+1));u=add(sub(mt,mp),sub(rat(Mp,s),rat(Mt,t+1)))
            v=sub(sub(scale(mt,t+1),scale(mp,s)),integer(Mt-Mp))
            ce=add(ce,divide(square(u),W));cf=add(cf,divint(square(v),l))
            A=sub(H(t+1),H(s))
            ue=add(ue,nonnegative(sub(sub(integer(l),A),divide(square(A),W))))
            # Closed harmonic first/second moments, independently expanded.
            h1=H(t);h0=H(s-1)
            sh=add(sub(scale(h1,t+1),scale(h0,s)),integer(-l))
            sh2=add(sub(scale(square(h1),t+1),scale(square(h0),s)),
                    add(sub(scale(h0,2*s-1),scale(h1,2*t+1)),integer(2*l)))
            uf=add(uf,nonnegative(sub(sh2,divint(square(sh),l))))
        need(count==p['cells'],'cell count')
        for key,val in [('coarse_E',ce),('coarse_F',cf),('worst_E',ue),('worst_F',uf)]:
            need(list(val)==p[key],'endpoint reconstruction '+key)
        upper=add(add(tuple(st['input']['E']),ce),add(ue,scale(square(uB),2*X)))
        need(list(upper)==p['completed_A_upper'],'completed cost')
        gain=(S+upper[1])**2*S<=4*(S+st['input']['A'][0])**3
        need(gain==p['certified_gain'],'finite gain flag')
        coarse_bounds.append(add(tuple(st['input']['F']),add(cf,uf)))
    return coarse_bounds

def verify(r):
    shapes(r);Y=max(st['Y'] for st in r['stages']);out=newton(Y);B=len(out)-1
    need(B==r['max_endpoint'],'max endpoint')
    digest=sha256(bytes(a+1 for a in out[1:])).hexdigest()
    need(digest==r['coefficient_digest'],'complete coefficient reconstruction')
    # Tighter 176-bit recomputation validates ALL supplied endpoint intervals.
    W=1<<176;shift=176-BITS
    wanted=set(int(k) for st in r['stages'] for k in st['endpoints'])|{B+1}
    EP={};M=ml=me=hl=he=0
    checks={st['Y'] for st in r['stages']}|{st['B'] for st in r['stages']}
    states={};elo=ee=flo=fhi=0
    conv=lambda a,e:(a//(1<<shift),-((-(a+e))//(1<<shift)))
    for k in range(1,B+2):
        hl+=W//k;he+=int(W%k!=0)
        if k<=B:
            M+=out[k];ml+=out[k]*W//k;me+=int(out[k]!=0 and W%k!=0)
            elo+=M*M*W//(k*(k+1));ee+=int(M*M*W%(k*(k+1))!=0)
            lo=0 if ml<=0<=ml+me else min(ml*ml,(ml+me)**2)
            hi=max(ml*ml,(ml+me)**2)
            flo+=lo//W;fhi+=-((-hi)//W)
            if k in checks:
                u0=ml-(-((-M*W)//(k+1)));u1=ml+me-M*W//(k+1)
                usq0=0 if u0<=0<=u1 else min(u0*u0,u1*u1)
                usq1=max(u0*u0,u1*u1)
                a0=elo+2*(k+1)*usq0//W
                a1=elo+ee-((-2*(k+1)*usq1)//W)
                states[k]={'E':conv(elo,ee),'F':conv(flo,fhi-flo),
                           'u':conv(u0,u1-u0),'A':conv(a0,a1-a0)}
        if k in wanted:
            conv=lambda a,e:(a//(1<<shift),-((-(a+e))//(1<<shift)))
            EP[k]=(M,conv(ml,me),conv(hl,he))
    endpoint_checks=0;direct_cells=0;allbounds=[]
    for st in r['stages']:
        for kind,k in [('input',st['Y']),('output',st['B'])]:
            for key,val in states[k].items():
                need(contains(st[kind][key],val),'complete state '+kind+' '+key)
        for key,ep in st['endpoints'].items():
            k=int(key);M,m,H=EP[k];endpoint_checks+=1
            need(ep['M']==M and contains(ep['m'],m) and contains(ep['H'],H),'endpoint arithmetic')
        need(contains(st['H_after'],EP[st['B']+1][2]),'last harmonic endpoint')
        bounds=endpoint_certificate(st);allbounds.append(bounds)
        if st['Y']<=15:direct_cells+=fraction_panel(st,out)
    # ONE max-range bound proves every cutoff Y<=max Y in the inherited gain.
    last=max(range(len(r['stages'])),key=lambda i:r['stages'][i]['Y'])
    upperF=min(z[1] for z in allbounds[last])
    uniform_gate=(S+2*upperF)**2<=32*S*S
    need(uniform_gate,'finite all-cutoff gain not certified')
    return {'output_coefficients':B,'endpoint_checks_counting_overlap':endpoint_checks,
            'direct_fraction_cells':direct_cells,'uniform_gain_cutoffs':[1,Y],
            'uniform_gain_source':'A_n <= 2 F_n; F_n monotone; A_Y >= F_1 = 1',
            'F_max_upper_numerator':upperF,'denominator_bits':BITS}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('report',nargs='?',default='reports/native.json');a=p.parse_args()
    result=verify(strict_read(a.report));print(canonical(result))
    Path('reports/verification.json').write_text(canonical(result)+'\n')
