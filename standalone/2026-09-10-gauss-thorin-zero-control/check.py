#!/usr/bin/env python3
"""Source-reconstructed directed GTP complex-zero certificates.

Standard library only. Zero counts follow from the analytic lemmas in PROOF.md,
not a numerical root-finder. No zeta evaluation or zero table is imported.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from functools import lru_cache
import argparse, hashlib, json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from intervals import I,C,S,BITS,need,hull,sqrt_i,exp_i,exp_c,log_i,pi_i_cached,gamma_prefactor

# Rational brackets, not trusted roots: signs, disjointness and completeness
# are checked against source-reconstructed polynomials before bisection.
BRACKETS = {'3': [['1839639/100000000', '919821/50000000'], ['7146379/50000000', '14292761/100000000'], ['15197669/25000000', '60790679/100000000']], '10': [['5529/20000000', '108/390625'], ['241799/100000000', '120901/50000000'], ['7909/1250000', '632723/100000000'], ['1128301/100000000', '70519/6250000'], ['418947/25000000', '1675791/100000000'], ['9498/390625', '2431491/100000000'], ['3799543/100000000', '1899773/50000000'], ['844343/12500000', '6754747/100000000'], ['474943/3125000', '15198179/100000000'], ['60792709/100000000', '7599089/12500000']]}

def solve(a,b):
    a=[list(r)+[v] for r,v in zip(a,b)];n=len(b)
    for k in range(n):
        j=next(j for j in range(k,n) if a[j][k])
        a[k],a[j]=a[j],a[k]
        p=a[k][k];a[k]=[v/p for v in a[k]]
        for j in range(n):
            if j!=k:
                p=a[j][k];a[j]=[u-p*v for u,v in zip(a[j],a[k])]
    return [r[-1] for r in a]

def moments(N):
    # g=S'/S, S=sinh(sqrt(6t))/sqrt(6t).
    ss=[F(6**j,factorial(2*j+1)) for j in range(N+2)]
    gg=[]
    for n in range(N+1):
        gg.append((n+1)*ss[n+1]-sum(ss[j]*gg[n-j] for j in range(1,n+1)))
    return [(-1)**j*v for j,v in enumerate(gg)]

def ev(p,x):
    ans=p[-1]
    for v in reversed(p[:-1]):ans=ans*x+v
    return ans

@lru_cache(None)
def seed(m):
    mu=moments(2*m)
    p=solve([[mu[i+j] for j in range(m)] for i in range(m)],[-mu[m+i] for i in range(m)])+[F(1)]
    h=mu[2*m]+sum(p[j]*mu[m+j] for j in range(m));d=h/(2*m+1)
    need(h>0,'nonpositive source error norm')
    for j in range(m):need(sum(p[k]*mu[k+j] for k in range(m+1))==0,'orthogonality')
    brackets=BRACKETS[str(m)]
    need(len(brackets)==m,'incomplete root coverage')
    xx=[];last=F(0)
    for lo,hi in brackets:
        lo,hi=F(lo),F(hi)
        need(last<lo<hi<1,'root brackets not ordered inside (0,1)')
        fl,fh=ev(p,lo),ev(p,hi)
        need(fl*fh<0,'root bracket lacks a sign change')
        last=hi
        for _ in range(310):
            mid=(lo+hi)/2;fm=ev(p,mid)
            if fl*fm<0:hi=mid;fh=fm
            elif fm==0:lo=hi=mid;break
            else:lo=mid;fl=fm
        xx.append(hull(lo,hi))
    ww=[]
    for root in xx:
        quotient=[I.point(0)]*m;quotient[-1]=I.point(1)
        for j in range(m-1,0,-1):quotient[j-1]=I.point(p[j])+root*quotient[j]
        numerator=sum((mu[j]*quotient[j] for j in range(m)),I.point(0))
        derivative=ev(quotient,root)
        ww.append(numerator/derivative)
    need(all(w.lo>0 for w in ww),'nonpositive Gaussian weight')
    need(sum(ww,I.point(0)).contains(1),'weights not normalized')
    for j in range(2*m):
        need(sum((w*(r**j) for w,r in zip(ww,xx)),I.point(0)).contains(mu[j]),'quadrature moment mismatch')
    beta=[w/r for w,r in zip(ww,xx)]
    A=2*sum(beta,I.point(0))
    need(A.hi < (m*(2*m+3)+1)*S,'shape upper bound failed')
    return xx,ww,beta,A,p,d

@lru_cache(None)
def grid(m,den,left,right):
    xx,ww,beta,A,_,_=seed(m)
    rows=[]
    for j in range(left*den,right*den+1):
        u=F(j,den);t=exp_i(I.point(u))
        exponent=-2*sum((b*log_i(1+r*t) for r,b in zip(xx,beta)),I.point(0))
        L2=exp_i(exponent)
        g=sum((w/(1+r*t) for w,r in zip(ww,xx)),I.point(0))
        rows.append((u,t,L2,g))
    return rows

def integral_error(m,qre,qim,den=16,left=-100,right=40):
    # Uniform on the q-disk of radius 1/16: Cauchy then bounds its derivative.
    R=F(1,16);amin=qre-R;amax=qre+R;tmax=abs(qim)+R
    need(0<amin<=amax<1,'invalid Mellin Cauchy disk')
    h=F(1,den);Aub=F(m*(2*m+3)+1)
    # eta=1; cos(1/2)>7/8, hence sec(1/2)<8/7.
    common=F(4)/(1-amax)*F(8,7)**(int(Aub)+1)*exp_i(I.point(tmax))
    alias=common/(exp_i(2*pi_i_cached()/h)-1)
    ltail=2*h*exp_i(I.point((1-amax)*(left-h)))/(1-exp_i(I.point(-(1-amax)*h)))
    rtail=Aub*h*exp_i(I.point(-(amin+2)*(right+h)))/(1-exp_i(I.point(-(amin+2)*h)))
    e=alias+ltail+rtail
    return F(e.hi,S)

def evaluate(m,sre,sim,den=16,left=-100,right=40):
    qre,qim=sre/2,sim/2;q=C.point(qre,qim)
    raw=C.point();draw=C.point()
    for u,t,L2,g in grid(m,den,left,right):
        osc=exp_c(C.point((1-qre)*u,-qim*u))
        term=osc.scale(2*L2*g/F(den))
        raw=raw+term;draw=draw+term.scale(-u)
    er=integral_error(m,qre,qim,den,left,right)
    raw=raw.widen(er);draw=draw.widen(16*er)
    pre,ps=gamma_prefactor(q)
    value=(pre*raw).scale(F(1,2))
    deriv=(pre*(draw+ps*raw)).scale(F(1,4))
    return value,deriv,er

def lower_modulus(z:C)->F:
    def low(x):
        return F(x.lo,S) if x.lo>0 else F(-x.hi,S) if x.hi<0 else F(0)
    a,b=low(z.re),low(z.im)
    return F(sqrt_i(I.point(a*a+b*b)).lo,S)

def error_bound(m,den=32,left=-10,right=30):
    k=2*m+1;_,_,_,_,_,d=seed(m)
    anchors=[F(3,16),F(5,16)]
    totals=[I.point(0),I.point(0)]
    rows=grid(m,den,left,right)
    h=F(1,den)
    growth=exp_i(I.point(k*h))
    for u,t,L2,g in rows[:-1]:
        cap=2*d*(t**k)*growth
        cap=I(min(cap.lo,S),min(cap.hi,S))
        for i,a in enumerate(anchors):
            totals[i]=totals[i]+h*exp_i(I.point(-a*u))*cap*L2
    out=[]
    for a,total in zip(anchors,totals):
        total=total+2*d*exp_i(I.point((k-a)*left))/(k-a)
        total=total+exp_i(I.point(-(a+2)*right))/(a+2)
        prod=F(1)
        for j in range(1,k):prod*=j-a
        out.append((a,total,prod))
    pp=I.point(1)
    for j in range(k):
        b=max(abs(j-anchors[0]),abs(j-anchors[1]))
        pp=pp*sqrt_i(I.point(b*b+F(707,100)**2))
    e=F(3,2)*pp*max(F(total.hi,S)/p for a,total,p in out)
    return F(e.hi,S),{'anchors':[{'a':str(a),'J_upper':str(F(t.hi,S)),'gamma_product_lower':str(p)} for a,t,p in out], 'epsilon':str(F(e.hi,S))}

def certificate(m,sre,sim,radius,reflected=False,source=False):
    v,d,raw_error=evaluate(m,sre,sim)
    if reflected:
        need(sre==F(1,2),'reflection center must be on critical line')
        v=C(v.re,I.point(0));d=C(I.point(0),d.im)
    vup=v.norm_upper();dlow=lower_modulus(d)
    curvature=F(17)*radius*radius/2
    # The whole radius disk has q real part between 3/16 and 5/16.
    need(sre/2-radius/2>F(3,16) and sre/2+radius/2<F(5,16),'curvature strip')
    eps=F(0);envelope=None
    if source:
        need(reflected,'native-xi transfer requires reflection in this certificate')
        need(abs(sim)/2+radius/2<F(707,100),'height outside source envelope')
        eps,envelope=error_bound(m)
    margin=radius*dlow-vup-curvature-eps
    need(margin>0,'Rouche certificate has no strict margin')
    return {'order':m,'center':[str(sre),str(sim)],'radius':str(radius),'reflected':reflected,'native_xi_transfer':source,
       'value':v.record(),'derivative':d.record(),'raw_quadrature_error':str(raw_error),
       'value_upper':str(vup),'derivative_lower':str(dlow),'curvature_cost':str(curvature),'source_error':str(eps),
       'strict_margin':str(margin),'source_envelope':envelope,'zero_count_in_open_disk':1,
       'critical_line_forced':reflected, 'simple':True}

def run():
    ans={}
    cases=[('raw_m3',3,F('0.471003433'),F('14.138525882'),F(1,10**6),False,False),
           ('reflected_m3',3,F(1,2),F('14.138974966'),F(1,10**6),True,False),
           ('native_xi_via_m10',10,F(1,2),F('14.134725'),F(1,10**5),True,True)]
    for name,m,re,im,r,ref,src in cases:
        print('checking '+name,file=sys.stderr,flush=True)
        ans[name]=certificate(m,re,im,r,ref,src)
        print(name+' strict margin '+str(F(ans[name]['strict_margin'])),file=sys.stderr,flush=True)
    return {'schema':'GZC26-v1','arithmetic':'outward 288-bit dyadic; standard library','RH_proved':False,
            'scope':'three disks only; no complementary region or all-height claim',
            'primitive':{'S':'sinh(sqrt(6t))/sqrt(6t)','c':'pi/6','mean_X':1,
               'root_polynomials':{str(m):[str(x) for x in seed(m)[4]] for m in (3,10)},
               'defect_constants':{str(m):str(seed(m)[5]) for m in (3,10)}},
            'certificates':ans}

def canonical(result):
    return json.dumps(result,indent=2,sort_keys=True)+'\n'

def verify_receipt(expected, path):
    need(path.read_text(encoding='utf-8')==expected,
         'receipt not identical to source-reconstructed canonical result')

def authenticate():
    base=Path(__file__).resolve().parent
    manifest=base/'MANIFEST.sha256'
    entries={}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest,name=line.split('  ')
        need(name not in entries and Path(name).name==name,'invalid manifest entry')
        entries[name]=digest
    expected=set(entries)|{'MANIFEST.sha256'}
    actual={p.name for p in base.iterdir()}
    need(actual==expected,'unlisted or missing packet file')
    for name,digest in entries.items():
        p=base/name
        need(p.is_file() and not p.is_symlink(),'nonregular packet file')
        need(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'packet hash mismatch: '+name)
    need(manifest.is_file() and not manifest.is_symlink(),'nonregular manifest')

def self_test(result):
    import copy, tempfile
    expected=canonical(result)
    changes=[('false-rh',lambda r:r.__setitem__('RH_proved',True)),
      ('count',lambda r:r['certificates']['raw_m3'].__setitem__('zero_count_in_open_disk',2)),
      ('source-error',lambda r:r['certificates']['native_xi_via_m10'].__setitem__('source_error','0')),
      ('boolean-alias',lambda r:r['certificates']['raw_m3'].__setitem__('zero_count_in_open_disk',True)),
      ('height',lambda r:r['certificates']['raw_m3']['center'].__setitem__(1,'14')),
      ('polynomial',lambda r:r['primitive']['root_polynomials']['3'].__setitem__(0,'0')),
      ('removed-scope',lambda r:r.pop('scope'))]
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'candidate.json';p.write_text(expected,encoding='utf-8')
        verify_receipt(expected,p)
        for name,change in changes:
            candidate=copy.deepcopy(result);change(candidate)
            p.write_text(canonical(candidate),encoding='utf-8')
            try:verify_receipt(expected,p)
            except ArithmeticError:pass
            else:raise ArithmeticError('altered record accepted: '+name)
        p.write_text(expected.replace('{','{\n  "RH_proved": true,',1),encoding='utf-8')
        try:verify_receipt(expected,p)
        except ArithmeticError:pass
        else:raise ArithmeticError('duplicate-key record accepted')
    print('PASS: pristine receipt plus eight altered-record refusals (same acceptance function)')

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--emit',type=Path,help='producer mode; not an acceptance receipt')
    ap.add_argument('--check',type=Path)
    ap.add_argument('--self-test',action='store_true')
    ap.add_argument('--authenticate-only',action='store_true')
    args=ap.parse_args()
    if args.authenticate_only:
        authenticate();print('PASS: packet inventory and hashes');sys.exit(0)
    if args.check:authenticate()
    result=run();text=canonical(result)
    if args.emit:args.emit.write_text(text,encoding='utf-8')
    if args.check:
        verify_receipt(text,args.check)
        print('PASS: three full analytic-disk predicates reconstructed')
    if args.self_test:self_test(result)
    if not args.emit and not args.check:print(text,end='')
