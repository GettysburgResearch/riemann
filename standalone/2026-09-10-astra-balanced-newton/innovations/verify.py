#!/usr/bin/env python3
"""Separate primitive reconstruction for NIR26. Imports no producer/repo code."""
import argparse
import copy
import hashlib
import json
import math
import tempfile
from fractions import Fraction as Q
from pathlib import Path

UNIT=2**128
LIMIT=65535
BASE='a1b4625f9775df1fdbd431b5198309a2fce9b038'

def check(c,m):
    if not c: raise ValueError(m)

def serialize(x):
    return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()

def sha(x):return hashlib.sha256(serialize(x)).hexdigest()
def pq(x):x=Q(x);return [x.numerator,x.denominator]
def ceil(a,b):return -((-a)//b)
def units(x):x=Q(x);return [x.numerator*UNIT//x.denominator,ceil(x.numerator*UNIT,x.denominator)]
def sqbounds(a,b):return (0 if a<=0<=b else min(a*a,b*b),max(a*a,b*b))

def mobius(n):
    sign=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p;sign=-sign
            if n%p==0:return 0
        p+=1
    return -sign if n>1 else sign

def pair_norm(c):
    return sum((a*b/Q(max(r,s)) for r,a in c.items() for s,b in c.items()),Q())

def canonical(Y,mu):
    xs=[];current=Q()
    for k in range(1,Y+1):current+=Q(mu[k],k);xs.append(current)
    c={k:Q(mu[k]) for k in range(1,Y+1) if mu[k]};c[Y+1]=-(Y+1)*current
    Esource={k:Q(mu[k]) for k in range(1,Y+1) if mu[k]}
    Esource[Y+1]=-sum(mu[1:Y+1])
    E=pair_norm(Esource);u=sum(xs,Q())/(Y+1);F=sum((x*x for x in xs),Q())
    return c,xs,E,u,F

def coefficient_map(c,N):
    D=1
    for a in c.values():D=math.lcm(D,a.denominator)
    a={r:int(v*D) for r,v in c.items() if v}
    div=[0]*(N+1)
    for r,v in a.items():
        for n in range(r,N+1,r):div[n]+=v
    out=[0]*(N+1)
    for r,v in a.items():
        if r<=N:out[r]+=2*D*v
        for k in range(1,N//r+1):out[r*k]-=v*div[k]
    return out,D*D

def panels(mu,cutoffs):
    M=0;ml=mh=fl=fh=el=eh=ul=uh=0;out=[]
    for k in range(1,max(cutoffs)+1):
        M+=mu[k]
        ml+=UNIT*mu[k]//k;mh+=ceil(UNIT*mu[k],k)
        a,b=sqbounds(ml,mh);fl+=a//UNIT;fh+=ceil(b,UNIT)
        d=k*(k+1);el+=UNIT*M*M//d;eh+=ceil(UNIT*M*M,d)
        ul+=UNIT*M//d;uh+=ceil(UNIT*M,d)
        if k in cutoffs:
            a,b=sqbounds(ul,uh);lo=(k+1)*a//UNIT;hi=ceil((k+1)*b,UNIT)
            transformed=[el+lo,eh+hi]
            check(max(fl,transformed[0])<=min(fh,transformed[1]),'variance enclosure')
            out.append({'Y':k,'F':[fl,fh],'E':[el,eh],'u':[ul,uh],
                        'F_from_variance':transformed,'A':[el+2*lo,eh+2*hi]})
    return out

def boundary_kernel(k,r,s):
    a=r*s;lo=min((r+1)*s,r*(s+1));hi=max((r+1)*s,r*(s+1));last=(r+1)*(s+1)
    return sum((Q(int(j*a<=k<j*lo)-int(j*hi<=k<j*last),j)
                for j in range(1,k//a+1)),Q())

def reconstruct():
    mu=[0]+[mobius(n) for n in range(1,LIMIT+1)]
    isometry=[]
    for N in range(1,13):
        for seed in range(4):
            a={k:Q((-1)**(k+seed)*(1+(k*seed)%3),1+seed%2) for k in range(1,N+1)}
            norm=pair_norm(a)
            tails=[sum((a[n]/n for n in range(k+1,N+1)),Q()) for k in range(N)]
            check(norm==sum((x*x for x in tails),Q()),'tail Cholesky')
            isometry.append([N,seed,pq(norm)])
    proj=[];bounds=[];count=0
    for Y in range(1,25):
        c,x,E,u,F=canonical(Y,mu);b=Y+1
        check(F==E+b*u*u==pair_norm(c),'native norm/variance')
        check(sum(((z-u)**2 for z in [Q(),*x]),Q())==E,'prefix variance')
        for n in range(1,Y+1):
            check(sum((Q(r*(n//r)-(r+1)*(n//(r+1)))*x[r-1] for r in range(1,n+1)),Q())==1,'source equations')
            count+=1
        for j,alpha in ((b,Q(-2,3)),(b+2,Q(3,2))):
            altered=c.copy();altered[j]=altered.get(j,Q())+j*alpha;altered[j+1]=altered.get(j+1,Q())-(j+1)*alpha
            norm=pair_norm(altered);check(norm==F+alpha*alpha,'orthogonal completion')
            proj.append([Y,j,pq(norm)])
        z,d=coefficient_map(c,b*b);e=Q(mu[b])-c[b]
        check(Q(mu[b*b])-Q(z[b*b],d)==e*e,'omitted endpoint')
        bounds.append([Y,pq(e),pq(Q(z[b*b],d)),mu[b*b]])
    ladder=[];source=[0,1]
    for Y in (1,3,15,255):
        check(len(source)==Y+1,'recursive input size')
        # Only the actually generated prefix supplies the next controller.
        m=sum((Q(source[k],k) for k in range(1,Y+1)),Q())
        c={k:Q(source[k]) for k in range(1,Y+1) if source[k]};c[Y+1]=-(Y+1)*m
        B=(Y+1)**2-1;z,d=coefficient_map(c,B)
        check(all(v%d==0 for v in z),'integer arithmetic output')
        source=[v//d for v in z]
        check(source==mu[:B+1],'trial-factor primitive coefficients')
        ladder.append({'input':Y,'output':B,'coefficients':B,'sha256':sha(source[1:])})
    kernel=[];entries=0
    for Y in range(1,11):
        c,x,_,_,F=canonical(Y,mu);b=Y+1;B=b*b-1;q=Q();inc=Q()
        for k in range(1,B+1):
            q+=Q(mu[k],k)
            if k<b:continue
            form=Q()
            for r in range(1,b):
                for s in range(1,b):
                    form+=x[r-1]*x[s-1]*boundary_kernel(k,r,s);entries+=1
            check(q==-form,'signed integer boundary kernel')
            inc+=form*form;kernel.append([Y,k,pq(q)])
        check(F+inc==canonical(B,mu)[-1],'all annular coordinates')
    tails=[]
    H=[Q()]
    for k in range(1,257):H.append(H[-1]+Q(1,k))
    for Y in (1,3,7):
        c,_,_,_,F=canonical(Y,mu);R=257;Jpartial=Q();Qpartial=Q()
        for k in range(1,R):
            V=2*sum((v for n,v in c.items() if n<=k),Q())-sum((v*w*(k//(r*s)) for r,v in c.items() for s,w in c.items()),Q())
            q=2*sum((v/n for n,v in c.items() if n<=k),Q())-sum((v*w/Q(r*s)*H[k//(r*s)] for r,v in c.items() for s,w in c.items()),Q())
            Jpartial+=V*V/Q(k*(k+1));Qpartial+=q*q
        K=2*abs(sum(c.values(),Q()))+sum((abs(x) for x in c.values()),Q())**2
        pr=(Jpartial,Jpartial+K*K/R);ir=(Qpartial,Qpartial+4*K*K/(R-1))
        check(max(pr[0],ir[0])<=min(pr[1],ir[1]),'full physical/innovation tails')
        tails.append({'Y':Y,'first_omitted_cell':R,'K':pq(K),
                      'physical':[units(pr[0])[0],units(pr[1])[1]],
                      'innovation':[units(ir[0])[0],units(ir[1])[1]],
                      'physical_tail':pq(K*K/R),'innovation_tail':pq(4*K*K/(R-1))})
    controls=[]
    for Y in (3,7,15,31,63):
        b=Y+1;hh=[Q()]
        for n in range(1,b*b):hh.append(hh[-1]+Q(1,n))
        ann=Q()
        for k in range(b,b*b):
            q=-hh[k//(Y*Y)]+2*hh[k//(Y*b)]-hh[k//(b*b)]
            expected=-1 if Y*Y<=k<Y*b else (1 if Y*b<=k<b*b else 0)
            check(q==expected,'entire localized annulus')
            ann+=q*q
        check(ann==2*Y+1 and pair_norm({Y:Q(Y),b:Q(-b)})==1,'unit-energy obstruction')
        controls.append([Y,pq(ann)])
    fake=[]
    for b in (16,32,64,128):
        c={1:Q(1),b:Q(-b)};z,d=coefficient_map(c,b*b-1);V=0;lower=0
        check(pair_norm(c)==b-1,'bounded fake input norm')
        for k in range(1,b*b):
            V+=z[k];check(V%d==0,'integer fake cumulative')
            if k>=b*b//2:
                value=V//d;check(2*value>=k,'fake output barrier')
                lower+=UNIT*value*value//(k*(k+1))
        check(lower>=UNIT*b*b//16,'quadratic fake energy')
        fake.append([b,b-1,lower])
    ys=set(range(1,33))|{63,127,255};cuts=ys|{(Y+1)**2-1 for Y in ys}|{1,3,15,255,65535}
    rows=panels(mu,cuts);by={r['Y']:r for r in rows};gains=[]
    for Y in sorted(ys):
        B=(Y+1)**2-1;a=by[Y]['F'][0];b=by[B]['F'][1]
        check((UNIT+b)**2*UNIT<=4*(UNIT+a)**3,'FINITE candidate only')
        gains.append([Y,B])
    body={'schema':'NIR26-v1','parent':BASE,
          'scope':{'RH_proved':False,'all_scale_gain_proved':False,'finite_primitive_replay':True,
                   'whole_raw_tails_bounded':True,'projection_factor':1,'scale_endpoint':'(Y+1)^2-1'},
          'scale':UNIT,'isometry':{'cases':len(isometry),'sha256':sha(isometry)},
          'projection':{'cases':len(proj),'sha256':sha(proj)},'constraints':count,
          'boundary':{'cases':len(bounds),'sha256':sha(bounds),'first':bounds[:3]},'ladder':ladder,
          'kernel':{'panels':len(kernel),'entries':entries,'sha256':sha(kernel)},
          'raw_tails':tails,'localized_controls':controls,'bounded_fake_controls':fake,
          'energy':{'panels':len(rows),'sha256':sha(rows),'ladder_rows':[by[n] for n in (1,3,15,255,65535)]},
          'FINITE_gain_tests':gains}
    return {'body':body,'sha256':sha(body)}

def no_duplicate(pairs):
    result={}
    for k,v in pairs:
        check(k not in result,'duplicate JSON key');result[k]=v
    return result

def read(path):return json.loads(path.read_text(),object_pairs_hook=no_duplicate)

def validate(path,expected):
    r=read(path);check(type(r) is dict and set(r)=={'body','sha256'},'schema keys')
    check(r['sha256']==sha(r['body']),'bad seal')
    check(serialize(r)==serialize(expected),'primitive mathematics, types, or coverage differ')

def selftest(expected):
    changes=[lambda b:b['scope'].update(RH_proved=True),
             lambda b:b['scope'].update(projection_factor=True),
             lambda b:b['scope'].update(all_scale_gain_proved=0),
             lambda b:b.update(scale=float(UNIT)),
             lambda b:b['ladder'][-1].update(output=65534),
             lambda b:b['boundary']['first'][0][1].__setitem__(0,99),
             lambda b:b['kernel'].update(entries=b['kernel']['entries']-1),
             lambda b:b['raw_tails'][0].update(first_omitted_cell=256),
             lambda b:b['raw_tails'][0].update(physical_tail=[0,1]),
             lambda b:b['bounded_fake_controls'][0].__setitem__(2,0),
             lambda b:b['energy']['ladder_rows'][-1]['F'].__setitem__(1,0),
             lambda b:b['FINITE_gain_tests'].pop()]
    with tempfile.TemporaryDirectory(prefix='nir-adverse-') as folder:
        path=Path(folder)/'report.json';path.write_bytes(serialize(expected));validate(path,expected)
        for change in changes:
            bad=copy.deepcopy(expected);change(bad['body']);bad['sha256']=sha(bad['body'])
            check(serialize(bad)!=serialize(expected),'no-op mutation')
            path.write_bytes(serialize(bad))
            try:validate(path,expected)
            except ValueError:pass
            else:raise ValueError('resealed alteration accepted')
        path.write_text('{"body":{},"body":{},"sha256":"x"}')
        try:read(path)
        except ValueError as e:check('duplicate' in str(e),'wrong duplicate refusal')
        else:raise ValueError('duplicate key accepted')
    return len(changes)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('report',type=Path);ap.add_argument('--self-test',action='store_true');ap.add_argument('--output',type=Path)
    a=ap.parse_args();r=reconstruct();validate(a.report,r)
    if a.output:a.output.write_bytes(serialize(r)+b'\n')
    print('NIR SEPARATE RECONSTRUCTION PASS',r['sha256'])
    if a.self_test:print('RESEALED REJECTIONS',selftest(r),'AND DUPLICATE-KEY REFUSAL')
if __name__=='__main__':main()
