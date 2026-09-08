#!/usr/bin/env python3
"""Bounded algebra for LT26. This is NOT a zeta zero or RH certificate."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path
import sys

BASE = 'c4fb013692c51d6b26b8a3c33200615af764da82'
PARENT = '2026-09-08-astra-intrinsic-entropy'
PARENT_SHA256 = '84f57cc91a8fb13d0e6892928c9968752f07e70da152d7608abc5af2a4c7d6c9'
PARENT_BLOB = 'afb721d6eddae8eb4fe861091f9747394bd7c708'
FILES = {'PROOF.md','README.md','REVIEW_AND_SOURCES.md','SOURCE_LOCK.json',
         'VALIDATION.md','check.py','test_check.py','verification.json','SHA256SUMS'}
LOCK = {'repository':'GettysburgResearch/riemann','parent_commit':BASE,
        'parent_pr':819,'parent_path':f'standalone/{PARENT}/PROOF.md',
        'parent_sha256':PARENT_SHA256,'parent_blob':PARENT_BLOB,'parent_bytes':14992}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


@dataclass(frozen=True)
class Q:
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        for x in (self.re,self.im):
            require(type(x) in (int,F), 'non-exact complex component')
        object.__setattr__(self,'re',F(self.re))
        object.__setattr__(self,'im',F(self.im))

    @staticmethod
    def lift(x):
        return x if type(x) is Q else Q(x)

    def __add__(self, x):
        x=Q.lift(x); return Q(self.re+x.re,self.im+x.im)
    __radd__=__add__
    def __neg__(self): return Q(-self.re,-self.im)
    def __sub__(self,x): return self+-Q.lift(x)
    def __rsub__(self,x): return Q.lift(x)+-self
    def __mul__(self,x):
        x=Q.lift(x)
        return Q(self.re*x.re-self.im*x.im,self.re*x.im+self.im*x.re)
    __rmul__=__mul__
    def conj(self): return Q(self.re,-self.im)
    def norm2(self): return self.re*self.re+self.im*self.im
    def inv(self):
        a=self.norm2(); require(a>0,'division by zero')
        return Q(self.re/a,-self.im/a)
    def __truediv__(self,x): return self*Q.lift(x).inv()
    def __rtruediv__(self,x): return Q.lift(x)*self.inv()
    def __pow__(self,n):
        require(type(n) is int and n>=0,'invalid exact exponent')
        y=Q(1)
        for _ in range(n): y=y*self
        return y


def frac(x:F) -> str:
    return f'{x.numerator}/{x.denominator}'


def pair(x:Q):
    return [frac(x.re),frac(x.im)]


def invert(m):
    n=len(m)
    a=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(m)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if a[i][j]),None)
        require(pivot is not None,'singular fixture')
        a[j],a[pivot]=a[pivot],a[j]
        p=a[j][j];a[j]=[x/p for x in a[j]]
        for i in range(n):
            if i!=j:
                q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[j])]
    return [row[n:] for row in a]


def reconstruct():
    counts={}
    interpolation=[]
    phases=[Q(1),Q(0,1),Q(F(3,5),F(4,5))]
    for gamma in (F(3,5),F(1),F(2),F(3)):
        for alpha in (F(1,16),F(1,8),F(1,4)):
            for r in range(1,5):
                lam=Q(alpha,gamma); h=((lam-F(1,2))/(lam+F(3,2)))**r
                for E in phases:
                    q=-E*(lam*lam+gamma*gamma)/h
                    U=q.im/gamma; V=q.re-alpha*U
                    require(Q(U)*lam+V==q,'interpolation failed')
                    require(Q(1)+h*(U*lam+V)/(E*(lam*lam+gamma*gamma))==Q(),
                            'delayed zero failed')
                    lc=lam.conj();hc=((lc-F(1,2))/(lc+F(3,2)))**r
                    require(Q(1)+hc*(U*lc+V)/(E.conj()*(lc*lc+gamma*gamma))==Q(),
                            'real conjugation failed')
                    a=(lam-F(1,2))/(lam+F(1,2))
                    require(F(1)-a.norm2()==2*alpha/(lam+F(1,2)).norm2(),'Cayley factor')
                    ratio=(lam+F(1,2)).norm2()/(lam-F(1,2)).norm2()
                    require(ratio>1,'positive zero mass')
                    interpolation.append({'gamma':frac(gamma),'alpha':frac(alpha),
                      'r':r,'formal_delay':pair(E),'U':frac(U),'V':frac(V),
                      'pair_entropy_ratio':frac(ratio)})
    counts['interpolation_panels']=len(interpolation)
    filters=[]
    for r in range(1,13):
        weighted=sum(F(comb(r,k))*2**k for k in range(r+1))
        unweighted=sum(F(comb(r,k))*F(4,3)**k for k in range(r+1))
        require(weighted==3**r and unweighted==F(7,3)**r,'filter majorant')
        for z in (Q(F(1,3)),Q(2,1),Q(F(1,2))):
            direct=((z-F(1,2))/(z+F(3,2)))**r
            partial=sum((Q(comb(r,k)*(-2)**k)/(z+F(3,2))**k
                         for k in range(r+1)),Q())
            require(direct==partial,'stable filter identity')
        # Numerator in local variable x=z-eta is x^r: first r Taylor coefficients vanish.
        poly=[F(0)]*r+[F(1)]
        require(all(x==0 for x in poly[:r]) and poly[r]==1,'jet order')
        filters.append({'r':r,'weighted_majorant':weighted.numerator,
                        'unweighted_majorant':frac(unweighted)})
    counts['filter_panels']=len(filters)
    models=[]
    b=F(1,5);gam=F(3,5);eta=F(1,2)
    def Ds(z): return 5*(z*z+gam*gam)/(z+b)**3
    for alpha in (F(1,100),F(1,50),F(1,20),F(1,10),F(1,5),F(1,3)):
        p=[F(5),-10*(b+alpha),F(5,2)*((b+alpha)**2+gam**2)]
        disc=p[1]**2-4*p[0]*p[2]
        require(disc==50*((b+alpha)**2-gam**2)<0,'all-time positive model')
        lam=Q(alpha,gam)
        def transform(z): return p[0]/(z+b)+p[1]/(z+b)**2+2*p[2]/(z+b)**3
        for z in (Q(eta),Q(1,2),lam,lam.conj()):
            require(transform(z)==5*((z-alpha)**2+gam*gam)/(z+b)**3,
                    'rational Laplace model')
        require(transform(lam)==Q() and transform(lam.conj())==Q(),'model zeros')
        norm=Ds(Q(eta))/transform(Q(eta))
        require(norm.im==0 and norm.re>0,'safe normalization positive')
        require(norm*transform(Q(eta))==Ds(Q(eta)),'exact safe value')
        models.append({'alpha':frac(alpha),'coefficients':[frac(x) for x in p],
                       'discriminant':frac(disc),'normalizer':frac(norm.re)})
    counts['positive_rational_models']=len(models)
    projections=[]
    for c in (F(1,2),F(1,4),F(1,16),F(1,64)):
        q=1+c
        for n in range(1,7):
            G=[[1+q*q if i==j else -q if abs(i-j)==1 else F(0)
                for j in range(n)] for i in range(n)]
            inv=invert(G)
            Dn=(q**(2*(n+1))-1)/(q*q-1)
            Dprev=(q**(2*n)-1)/(q*q-1)
            finite=1-inv[0][0]; limit=1-1/(q*q)
            require(inv[0][0]==Dprev/Dn,'independent inverse/continuant')
            require(finite>limit>0,'nonzero limit')
            rowbound=4*c+c*c
            projections.append({'c':frac(c),'n':n,'finite_error':frac(finite),
                                'limit_error':frac(limit),'gram_row_bound':frac(rowbound)})
    counts['finite_projection_panels']=len(projections)
    constants={'source_L1_upper':frac(F(761,128)),
               'source_L2_squared_upper':frac(F(157,32)),
               'relative_tolerance':frac(F(1,1024))}
    require(F(1025,1024)*F(761,128)<6,'L1 margin')
    require(F(1025,1024)**2*F(157,32)<5,'L2 margin')
    require(F(3,2)-F(2,3)>=F(4,16),'large t envelope endpoint')
    require(F(1,4)>=F(4,16),'small t envelope endpoint')
    counts['envelope_constant_cases']=4
    return {'schema':'LT26-v1','rh_established':False,
       'source_changed':True,'actual_zero_numerically_evaluated':False,
       'scope':'bounded exact algebra; no actual off-line zeta zero or RH result',
       'counts':counts,'total_panels':sum(counts.values()),
       'interpolation':interpolation[:3]+interpolation[-3:],
       'all_interpolation_sha256':hashlib.sha256(json.dumps(interpolation,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
       'filters':filters,'models':models,
       'projections':projections,'constants':constants}


def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        require(k not in d,'duplicate JSON key')
        d[k]=v
    return d


def no_float(_): raise ValueError('non-exact JSON numeric value')


def load(path):
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=no_duplicates,
                      parse_float=no_float,parse_constant=no_float)


def same(x,y):
    if type(x) is not type(y): return False
    if isinstance(x,dict): return x.keys()==y.keys() and all(same(x[k],y[k]) for k in x)
    if isinstance(x,list): return len(x)==len(y) and all(same(a,b) for a,b in zip(x,y))
    return x==y


def authenticate(root):
    require(root.is_dir() and not root.is_symlink(),'invalid packet directory')
    require({p.name for p in root.iterdir()}==FILES,'missing/extra packet paths')
    for name in FILES:
        p=root/name;require(p.is_file() and not p.is_symlink(),'nonregular packet input')
    entries={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        sha,sep,name=line.partition('  ')
        require(sep=='  ' and name not in entries and name in FILES-{'SHA256SUMS'},'manifest syntax')
        require(len(sha)==64 and all(c in '0123456789abcdef' for c in sha),'manifest hash syntax')
        entries[name]=sha
    require(set(entries)==FILES-{'SHA256SUMS'},'manifest coverage')
    for name,sha in entries.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==sha,'checksum '+name)
    require(same(load(root/'SOURCE_LOCK.json'),LOCK),'source-lock mismatch')
    parent=root.parent/PARENT/'PROOF.md'
    require(parent.is_file() and not parent.is_symlink() and not parent.parent.is_symlink(),
            'missing or symlink parent source')
    b=parent.read_bytes()
    require(len(b)==14992 and hashlib.sha256(b).hexdigest()==PARENT_SHA256,'parent source mismatch')
    blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    require(blob==PARENT_BLOB,'parent blob mismatch')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',action='store_true',help='produce finite results, not an acceptance pass')
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    args=ap.parse_args();root=args.root
    if args.write:
        (root/'verification.json').write_text(json.dumps(reconstruct(),indent=2,sort_keys=True)+'\n')
        print('WROTE_BOUNDED_LT26_FIXTURES_NOT_ACCEPTANCE');return
    authenticate(root)
    expected=reconstruct();require(same(load(root/'verification.json'),expected),'primitive replay mismatch')
    print(json.dumps({'status':'PASS_LT26_BOUNDED_ALGEBRA','total_panels':expected['total_panels'],
                      'counts':expected['counts'],'rh_established':False,
                      'actual_zero_numerically_evaluated':False},sort_keys=True))


if __name__=='__main__':
    try: main()
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);sys.exit(1)
