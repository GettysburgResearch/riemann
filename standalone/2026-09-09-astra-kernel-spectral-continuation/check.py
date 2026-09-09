#!/usr/bin/env python3
"""Exact finite regressions, NOT a proof of RH or of analytic continuation.
No zeta-zero oracle, numerical contour integration, source-code import, or floats.
Polynomial-root controls are synthetic F, never declared to be zeta zeros.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, math
from fractions import Fraction as Q
from pathlib import Path
BASE='f99d9e3908dde4865377c75d9ca051c1f545bf4f'
SCHEMA='astra-kernel-spectral-continuation/v1'
class CheckError(RuntimeError): pass
def req(b,m):
    if not b: raise CheckError(m)
def canon(v): return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(v): return hashlib.sha256(canon(v)).hexdigest()
def rat(v): v=Q(v); return [v.numerator,v.denominator]
def trim(a):
    a=list(a)
    while len(a)>1 and not a[-1]:a.pop()
    return a or [Q(0)]
def add(a,b):
    c=[Q(0)]*max(len(a),len(b))
    for i,v in enumerate(a):c[i]+=v
    for i,v in enumerate(b):c[i]+=v
    return trim(c)
def scale(a,c):return trim([v*c for v in a])
def mul(a,b):
    c=[Q(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):c[i+j]+=u*v
    return trim(c)
def ev(a,x):
    r=Q(0)
    for v in reversed(a):r=r*x+v
    return r
def shifted(a,r):
    out=[Q(0)]*len(a)
    for k,v in enumerate(a):
        for j in range(k+1):out[j]+=v*math.comb(k,j)*r**(k-j)
    return trim(out)
def divide_root(a,r):
    b=[Q(0)]*(len(a)-1);b[-1]=a[-1]
    for j in range(len(b)-2,-1,-1):b[j]=a[j+1]+r*b[j+1]
    req(a[0]+r*b[0]==0,'inexact root division')
    return trim(b)
def inv_series(a,n):
    req(a[0]!=0,'zero analytic denominator'); out=[]
    for k in range(n):
        v=(Q(1) if not k else Q(0))-sum((a[j]*out[k-j] for j in range(1,min(k,len(a)-1)+1)),Q(0))
        out.append(v/a[0])
    return out
def ipower_series(r,e,n):
    req(r!=0,'series center zero'); out=[];bc=Q(1)
    for k in range(n):
        if k:bc=bc*Q(e-k+1,k)
        out.append(bc*r**(e-k))
    return out

def mellin_piece(s,t,r):
    """Direct integration of (1/(ruv)-1)+, split at u=1/r."""
    c=Q(1,r)
    D=c**s/Q((t-1)*(s-1))-c**s/Q(t*s)
    D+=c**t/Q(t*(t-1))*((1-c**(s-t))/Q(s-t))
    Is=c**s/Q(s*(s-1));It=c**t/Q(t*(t-1))
    return s*(1-s)*t*(1-t)*D+s*(1-s)*t*Is+s*t*(1-t)*It

def divisor_kernel_checks():
    rows=[];pieces=diagonals=0
    for r in range(1,32,2):
        c=Q(1,r)
        for s in range(2,9):
            # Diagonal represented exactly as a + b log(c), not a floating log.
            D0=c**s*(Q(1,(s-1)**2)-Q(1,s*s));Dlog=-c**s/Q(s*(s-1))
            a=s*s*(1-s)**2*D0+2*s*s*(1-s)*c**s/Q(s*(s-1))
            b=s*s*(1-s)**2*Dlog
            req((a,b)==(-c**s,-s*(s-1)*c**s),'confluent diagonal sign')
            diagonals+=1
            for t in range(2,9):
                if s==t:continue
                direct=mellin_piece(s,t,r)
                Fs=Q(s-1,s)*c**s;Ft=Q(t-1,t)*c**t
                expect=s*t*(Ft-Fs)/Q(s-t)
                req(direct==expect,'density/atom bilinear mismatch');pieces+=1
                rows.append([r,s,t,*rat(direct)])
    for R in [1,3,7,15,31]:
        for s,t in [(2,3),(2,7),(3,5),(5,8)]:
            lhs=sum((mellin_piece(s,t,r) for r in range(1,R+1,2)),Q(0))
            zs=sum((Q(1,r**s) for r in range(1,R+1,2)),Q(0));zt=sum((Q(1,r**t) for r in range(1,R+1,2)),Q(0))
            req(lhs==s*t*(Q(t-1,t)*zt-Q(s-1,s)*zs)/Q(s-t),'finite divisor sum')
    return {'density_atom_pairs':pieces,'confluent_log_pairs':diagonals,'finite_divisor_sums':20,'transcript_sha256':digest(rows),'first_pair':rows[0]}

def make_F(spec):
    a=[Q(1)]
    for r,m in spec:
        for _ in range(m):a=mul(a,[Q(1),-1/r])
    return a

def ell(F,spec,chosen,p,base,power,origin=True):
    """Residue sum of -Y^s s^p/(s^2 F(s)); polynomial in formal log(Y).
    Y=base^4, so Y^r is rational for the selected rational roots.
    """
    a=F[0];b=F[1] if len(F)>1 else Q(0)
    out=([b/a**2,-Q(power)/a] if p==0 else ([-1/a] if p==1 else [Q(0)])) if origin else [Q(0)]
    for idx in chosen:
        r,m=spec[idx]; G=list(F)
        for _ in range(m):G=divide_root(G,r)
        h=scale(mul(ipower_series(r,p-2,m),inv_series(shifted(G,r),m)),-1)[:m]
        h=h+[Q(0)]*(m-len(h))
        e=4*r*power;req(e.denominator==1,'nonrational exponential control')
        yp=Q(base)**int(e)
        term=[yp*h[m-1-j]*Q(power**j,math.factorial(j)) for j in range(m)]
        out=add(out,term)
    return trim(out)

def jet(F,r,t,j,k):
    ans=Q(0)
    for d in range(1,len(F)):
        for z in range(d):
            p=z+1;q=d-z
            if p>=j and q>=k:ans-=F[d]*math.comb(p,j)*r**(p-j)*math.comb(q,k)*t**(q-k)
    return ans

def det(a):
    a=[list(row) for row in a];v=Q(1)
    for k in range(len(a)):
        z=next((i for i in range(k,len(a)) if a[i][k]),None)
        if z is None:return Q(0)
        if z!=k:a[k],a[z]=a[z],a[k];v=-v
        pivot=a[k][k];v*=pivot
        for i in range(k+1,len(a)):
            q=a[i][k]/pivot
            for j in range(k+1,len(a)):a[i][j]-=q*a[k][j]
    return v

def spectral_checks():
    specs=[[(Q(3,4),1)],[(Q(1,2),1),(Q(3,4),1)],[(Q(1,2),2),(Q(5,4),1)],[(Q(3,4),3)],[(Q(1,2),2),(Q(3,4),2),(Q(5,4),1)]]
    rows=[];models=jets=cross=0;missing_origin_witness=None
    for si,spec in enumerate(specs):
        F=make_F(spec);D=len(F)-1
        for ri,(r,m) in enumerate(spec):
            G=[ [jet(F,r,r,j,k) for k in range(m)] for j in range(m)]
            anti=-r*r*shifted(F,r)[m]
            req(det(G)==(-1)**(m*(m-1)//2)*anti**m,'root-jet determinant')
            for j in range(m):
                for k in range(m):
                    if j+k<m-1:req(G[j][k]==0,'low jet must vanish')
                    if j+k==m-1:req(G[j][k]==anti,'jet antidiagonal')
                    jets+=1
            for ti,(t,n) in enumerate(spec):
                if ti==ri:continue
                for j in range(m):
                    for k in range(n):req(jet(F,r,t,j,k)==0,'cross-root jet');cross+=1
        for mask in range(1<<len(spec)):
            chosen=[i for i in range(len(spec)) if mask>>i&1]
            for base in (2,3,5):
                for origin in (True,False):
                    ls=[ell(F,spec,chosen,p,base,1,origin) for p in range(D+1)]
                    B=[Q(0)]
                    for d in range(1,D+1):
                        for j in range(d):B=add(B,scale(mul(ls[j+1],ls[d-j]),-F[d]))
                    q2=ell(F,spec,chosen,0,base,2,origin)
                    expect=add(q2,scale(ls[0],-2)) if origin else q2
                    req(trim(B)==trim(expect),'full square-scale residue identity')
                    if not origin and chosen and missing_origin_witness is None:
                        delta=add(B,scale(add(q2,scale(ls[0],-2)),-1))
                        req(delta!=[Q(0)],'background failure witness')
                        missing_origin_witness=[rat(x) for x in delta]
                    rows.append([si,mask,base,origin,[rat(x) for x in B]])
                    models+=1
    return {'models':models,'jet_entries':jets,'distinct_root_jet_entries':cross,'all_roots_synthetic_not_zeta':True,'missing_origin_discrepancy':missing_origin_witness,'transcript_sha256':digest(rows)}

def gaussian_checks():
    # Simple conjugate pair of the SYNTHETIC polynomial (z-r)(z-conj(r)).
    rows=[]
    for beta in (Q(1,4),Q(1,2),Q(3,4)):
        for gamma in (Q(1),Q(3,2),Q(4)):
            # k=-r^2 F'(r), F'(r)=2i gamma. Exact real and imaginary parts.
            kr=4*beta*gamma**2;ki=-2*gamma*(beta**2-gamma**2)
            gram=[[kr/2,ki/2],[ki/2,-kr/2]]
            req(det(gram)==-(kr*kr+ki*ki)/4<0,'real indefinite root plane')
            rows.append([rat(beta),rat(gamma),rat(det(gram))])
    return {'synthetic_conjugate_planes':len(rows),'actual_zero_locations_tested':0,'transcript_sha256':digest(rows)}

def cutoff_checks():
    rows=[];balance=0
    for s in (Q(-1,2),Q(0),Q(1,2),Q(3,4),Q(1),Q(2),Q(3)):
        for base in (2,3,5,8):
            eps=Q(1,base**4)
            def epow(t):
                n=4*t;req(n.denominator==1,'exact rational cutoff power');return Q(base)**(-int(n))
            if s==1:bal=Q(0)
            else:bal=s*(1-s)/(s-1)*(1-epow(s-1))+s-s*epow(s-1)
            req(bal==0,'literal finite-cutoff harmonic balance');balance+=1
            for k in range(1,7):
                full=s*(k+1)/(s+k)
                direct=s*(1-s)/(s+k)*(1-epow(s+k))+s-s*epow(s+k)
                req(direct==full*(1-epow(s+k)),'compact cutoff moment')
                bound=(abs(s*(1-s))/(s+1)+abs(s))*epow(s+1)
                req(abs(full-direct)<=bound,'complete small-coordinate bound')
                rows.append([rat(s),base,k,rat(direct),rat(bound)])
    for base in (2,3,5,8):
        eps=Q(1,base**4)
        req((1/eps-1)+1-1/eps==0,'log-background cutoff balance')
        for k in range(1,7):
            truncated=(1-eps**k)/k+1-eps**k;full=Q(1,k)+1
            req(full-truncated==(1+Q(1,k))*eps**k,'background boundary remainder')
    return {'harmonic_balances':balance+4,'power_moments':len(rows),'background_moments':24,'transcript_sha256':digest(rows)}

def log_interval(x,terms=24):
    x=Q(x);req(x>0,'log domain');k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def unit(y):
        t=(y-1)/(y+1);s=sum((2*t**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
        e=2*t**(2*terms+1)/Q(2*terms+1)/(1-t*t)
        return s,s+e
    a,b=unit(x);c,d=unit(Q(2))
    return (a+k*c,b+k*d) if k>=0 else (a+k*d,b+k*c)

def kernel_bound_checks():
    rows=[]; M=128;hM=sum((Q(1,2*k-1) for k in range(1,M+1)),Q(0))
    for j in range(1,65):
        lo,hi=log_interval(Q(j+1,j));l=lo/2-Q(1,2*j+1);h=hi/2-Q(1,2*j+1)
        req(0<l<=h<=Q(3,8*(2*j+1)**3),'midpoint harmonic difference')
    for j in range(1,25):
        hj=sum((Q(1,2*k-1) for k in range(1,j+1)),Q(0))
        for z in (Q(2*j-1),Q(4*j-1,2),Q(2*j),Q(4*j+1,2),Q(6*j+2,3)):
            lo,hi=log_interval(Q(2*M)/z)
            base=z*(hj-hM)+z/2-j
            rlo=base+z*lo/2;rhi=base+z*hi/2+3*z/Q(128*M*M)
            req(-Q(3,8)/z<rlo<=rhi<Q(3,8)/z,'complete R interval')
            rows.append([rat(z),rat(rlo),rat(rhi)])
    return {'midpoint_differences':64,'directed_R_samples':len(rows),'transcript_sha256':digest(rows),'arithmetic':'rational atanh intervals plus full harmonic remainder'}

def mu_trial(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign

def native_checks():
    N=33**2;div=[0]*(N+1);div[1]=1
    for n in range(1,N+1):
        for k in range(2*n,N+1,n):div[k]-=div[n]
    req(all(div[n]==mu_trial(n) for n in range(1,N+1)),'primitive Mobius divisor inversion')
    def q(x):return sum((Q(div[n])*(1-Q(x,n)) for n in range(1,x+1,2)),Q(0))
    rows=[]
    for Y in range(3,34,2):
        lam={n:Q(div[n]) for n in range(1,Y,2)}
        lam[Y]=-Y*sum((a/n for n,a in lam.items()),Q(0))
        req(sum((a/n for n,a in lam.items()),Q(0))==0,'native harmonic balance')
        B=Q(0)
        for a,va in lam.items():
            for b,vb in lam.items():
                z=Q(Y*Y,a*b)
                B+=va*vb*sum((z/r-1 for r in range(1,int(z)+1,2)),Q(0))
        req(sum(lam.values())==q(Y),'native source total')
        req(q(Y*Y)==2*q(Y)+B,'complete native square-scale scalar')
        rows.append([Y,rat(q(Y)),rat(q(Y*Y)),rat(B)])
    return {'primitive_mu_checks':N,'actual_cutoffs':len(rows),'transcript_sha256':digest(rows),'first_row':rows[0]}

def reconstruct():
    return {'schema':SCHEMA,'main':BASE,'RH_proved':False,'analytic_theorems_machine_proved':False,
            'scope':'bounded exact arithmetic, rational interval samples, and synthetic spectral algebra; no actual zeta-zero input',
            'divisor_kernel':divisor_kernel_checks(),'spectral':spectral_checks(),'conjugate':gaussian_checks(),
            'cutoffs':cutoff_checks(),'kernel_bound':kernel_bound_checks(),'native':native_checks()}

def load(path):
    def unique(pairs):
        out={}
        for k,v in pairs:req(k not in out,'duplicate JSON key');out[k]=v
        return out
    def nofloat(s):raise CheckError('floating JSON forbidden')
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=unique,parse_float=nofloat,parse_constant=nofloat)
def validate(doc,expected):
    req(type(doc) is dict and set(doc)=={'payload','sha256'},'outer schema')
    req(doc['sha256']==digest(doc['payload']),'resealed digest mismatch')
    req(canon(doc['payload'])==canon(expected),'primitive reconstruction disagreement')
def selftest(expected):
    base={'payload':expected,'sha256':digest(expected)};validate(base,expected)
    changes=[lambda p:p.__setitem__('RH_proved',True),lambda p:p.__setitem__('analytic_theorems_machine_proved',True),
      lambda p:p.__setitem__('main','0'*40),lambda p:p.__setitem__('scope','unconditional full RH proof'),
      lambda p:p['spectral'].__setitem__('all_roots_synthetic_not_zeta',False),
      lambda p:p['conjugate'].__setitem__('actual_zero_locations_tested',9),
      lambda p:p['divisor_kernel']['first_pair'].__setitem__(-1,p['divisor_kernel']['first_pair'][-1]+1),
      lambda p:p['spectral']['missing_origin_discrepancy'][0].__setitem__(0,0),
      lambda p:p['spectral'].__setitem__('jet_entries',0),lambda p:p['cutoffs'].__setitem__('harmonic_balances',0),
      lambda p:p['kernel_bound'].__setitem__('directed_R_samples',0),lambda p:p['native']['first_row'][3].__setitem__(0,0)]
    rejected=0
    for change in changes:
        d=copy.deepcopy(base);old=canon(d['payload']);change(d['payload']);req(canon(d['payload'])!=old,'no-op mutation')
        d['sha256']=digest(d['payload'])
        try:validate(d,expected)
        except CheckError:rejected+=1
        else:raise CheckError('resealed corruption accepted')
    req(rejected==12,'tamper coverage');return rejected

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path);ap.add_argument('--self-test',action='store_true');args=ap.parse_args()
    try:
        p=reconstruct();doc={'payload':p,'sha256':digest(p)}
        if args.write:args.write.write_bytes(canon(doc)+b'\n')
        if args.check:validate(load(args.check),p)
        n=selftest(p) if args.self_test else 0
        print(json.dumps({'PASS':True,'RH_proved':False,'sha256':doc['sha256'],'resealed_rejections':n,'native_cutoffs':p['native']['actual_cutoffs'],'spectral_models':p['spectral']['models']},sort_keys=True));return 0
    except (CheckError,OSError,ValueError,KeyError,TypeError,ZeroDivisionError) as e:print('ERROR:',e);return 1
if __name__=='__main__':raise SystemExit(main())
