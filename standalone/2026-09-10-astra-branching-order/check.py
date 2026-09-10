#!/usr/bin/env python3
"""Authenticate, then reconstruct exact bounded algebra and one full root disk.
--emit is a producer operation, not an authenticated accepting operation.
No parent executable, numerical scout, zero oracle, or floating arithmetic is used.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb, factorial
import argparse
import hashlib
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'README.md','PROOF.md','VALIDATION.md','SOURCES.json',
         'certificate.py','check.py','test_check.py','result.json','SHA256SUMS'}
PARENT = '5c26d1f7e1075fdea18119a5abb447102ab5850b'

def require(v, message):
    if not v: raise ValueError(message)

def canon(o):
    return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=True)

def pairs(items):
    d={}
    for k,v in items:
        if k in d: raise ValueError('duplicate JSON key')
        d[k]=v
    return d

def badnum(s): raise ValueError('noninteger JSON number')

def load_json(path):
    p=Path(path)
    require(not p.is_symlink() and p.is_file(), 'receipt must be a regular nonsymlink file')
    b=p.read_bytes();require(0<len(b)<=2000000,'receipt size')
    d=json.loads(b,object_pairs_hook=pairs,parse_float=badnum,parse_constant=badnum)
    require(type(d) is dict and d, 'receipt must be a nonempty object')
    return d

def authenticate(root=ROOT):
    names={p.name for p in root.iterdir()}
    require(names==FILES,'exact packet inventory')
    for p in root.iterdir():
        require(p.is_file() and not p.is_symlink(),'regular packet file')
    rows={}
    for line in (root/'SHA256SUMS').read_text('ascii').splitlines():
        digest,sep,name=line.partition('  ')
        require(sep and len(digest)==64 and all(c in '0123456789abcdef' for c in digest), 'manifest syntax')
        require(name in FILES-{'SHA256SUMS'} and name not in rows,'manifest entry')
        rows[name]=digest
    require(set(rows)==FILES-{'SHA256SUMS'},'manifest coverage')
    for name,h in rows.items():
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==h,'hash drift: '+name)
    sources=load_json(root/'SOURCES.json')
    require(sources['parent']['head']==PARENT,'parent drift')
    require(sources['parent']['proposal_sha256']=='bab49ed09fccd832c9a5021049a61e61f41839edb73d59d2df38fb17fcfb9897','parent proof identity')
    require(sources['rh_proved'] is False,'source status')
    return len(rows)

def module():
    spec=importlib.util.spec_from_file_location('bor_certificate',ROOT/'certificate.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m

def rat(q): q=Q(q); return [q.numerator,q.denominator]

def rising(x,n):
    v=Q(1)
    for j in range(n):v*=x+j
    return v

def a(j): return Q(1) if j==0 else (1-Q(2)**(1-2*j))/(2*j-1)

def gamma_mom(k,n):return [rising(k,j)/k**j for j in range(n+1)]

def update(m):
    return [a(j)*sum((comb(j,l)*m[l]*m[j-l] for l in range(j+1)),Q()) for j in range(len(m))]

def value(poly,x):return sum((p*x**j for j,p in enumerate(poly)),Q())

def primitive(poly,x):return sum((p*x**(j+1)/(j+1) for j,p in enumerate(poly)),Q())

def peano(law1,law2):
    # law2-law1; reconstruct the positive-part polynomial on EVERY interval.
    signed={}
    for law,sign in ((law1,-1),(law2,1)):
        for x,p in law.items():signed[x]=signed.get(x,Q())+sign*p
    for j in range(3):require(sum((p*x**j for x,p in signed.items()),Q())==0,'lower moments')
    knots=sorted({Q(0)}|set(signed));total=Q();pieces=0
    for l,r in zip(knots,knots[1:]):
        poly=[Q(),Q(),Q()]
        for x,p in signed.items():
            if x>=r:
                poly[0]+=p*x*x/2;poly[1]-=p*x;poly[2]+=p/2
        checks=[value(poly,l),value(poly,r)]
        if poly[2]>0:
            critical=-poly[1]/(2*poly[2])
            if l<critical<r:checks.append(value(poly,critical))
        require(min(checks)>=0,'Peano positivity')
        total+=primitive(poly,r)-primitive(poly,l);pieces+=1
    gap=sum((p*x**3 for x,p in signed.items()),Q())/6
    require(total==gap,'Peano full integral')
    return {'pieces':pieces,'metric':rat(total)}

def discrete_map(law):
    out={};us={Q(1):Q(1,4),Q(3,2):Q(1,2),Q(2):Q(1,4)}
    for x,px in law.items():
        for y,py in law.items():
            for u,pu in us.items():
                z=(x+y)/u**2;out[z]=out.get(z,Q())+px*py*pu
    return out

def algebra(m):
    beta=[]
    for j in range(13):
        bj=rising(Q(5,2),j)/rising(5,j);wj=a(j)
        if j<=2: require(bj==wj,'beta/uniform first moments')
        else:require(wj>bj,'beta/uniform higher test moment')
        require(bj*rising(5,j)/Q(5,2)**j==rising(Q(5,2),j)/Q(5,2)**j,'beta gamma identity')
        beta.append([j,rat(bj),rat(wj)])
    require(Q(9,256)**2>Q(3,64)**3 and Q(66,1792)**2<Q(4,27)**3,'density crossing range')
    require(a(3)-rising(Q(5,2),3)/rising(5,3)==Q(1,160),'third order scale')
    moments=gamma_mom(Q(5,2),6);stages=[]
    for n in range(33):
        require(moments[1]==1 and moments[2]==Q(7,5),'preserved variance')
        gap=Q(24,175)*Q(31,80)**n
        require(moments[3]==Q(93,35)-gap,'third moment rate')
        require(moments[4]<8,'fourth moment UI bound')
        stages.append([n,rat(moments[3]),rat(gap/6)])
        moments=update(moments)
    inverse=Q(127,7)*Q(5,2)**3/24
    require(inverse==Q(15875,1344) and inverse<12,'inverse moment ceiling')
    require(2*a(3)==Q(31,80),'ideal contraction rate')
    require(24*Q(4,175)/8==Q(12,175),'complete Mellin factor')
    require(Q(127,896)*(16+8*Q(93,35)+6*Q(7,5)**2)<8,'UI induction')
    require(Q(1,3)-Q(1,4)-Q(1,48)==Q(1,16),'gamma input high-strip margin')
    models=[]
    for shift in (Q(1),Q(3,2)):
        for step in (Q(1,3),Q(1),Q(2)):
            lo={shift:Q(1,4),shift+2*step:Q(3,4)}
            hi={shift+step:Q(3,4),shift+3*step:Q(1,4)}
            before=peano(lo,hi);after=peano(discrete_map(lo),discrete_map(hi))
            eu6=(Q(1,4)+Q(1,2)*Q(2,3)**6+Q(1,4)*Q(1,2)**6)
            require(Q(*after['metric'])==2*eu6*Q(*before['metric']),'discrete shared-scale transfer')
            models.append({'shift':rat(shift),'step':rat(step),'before':before,'after':after})
    # Only small mixing moments here; the root proof reconstructs all 601.
    raw,eta=m.mixing_moments(12)
    require(raw[0]==1 and raw[1]==Q(1,2),'mixing law normalization')
    require(raw[2]==Q(11,40),'mixing law second moment')
    # Beta(2,2) integral identity independent of the closed simplification.
    for j in range(13):
        direct=sum((comb(j,l)*6*Q(factorial(l+1)*factorial(j-l+1),factorial(j+3))*a(l)*a(j-l) for l in range(j+1)),Q())
        require(direct==raw[j],'beta mixing coefficient')
    return {'beta_uniform_moments':beta,'ordered_moment_stages':stages,
            'peano_models':models,'inverse_cube_bound':rat(inverse),
            'mixing_raw_through_12':[rat(v) for v in raw]}

def primitive_checks(m):
    def contains(i,x):return i.lo<=Q(x)*m.S<=i.hi
    def zero(z):return contains(z.re,0) and contains(z.im,0)
    pi=m.pi_i();require(pi.lo>3*m.S and pi.hi<Q(22,7)*m.S,'pi bracket')
    require(zero(m.cis(pi)-m.C(-1)),'pi trigonometry')
    require(contains(m.log_i(1),0),'log1')
    for x in (Q(1,8),Q(1,2),Q(2),Q(7),Q(64)):
        require(contains(m.exp_i(m.log_i(x)),x),'exp-log roundtrip')
        sq=m.sqrt_i(x);require(sq.lo**2<=Q(x)*m.S**2<=sq.hi**2,'sqrt bracket')
    gamma=[]
    for k in (1,2,4,7):
        lg,ps=m.loggamma_psi(m.C(k),pi)
        require(contains(m.exp_c(lg).re,factorial(k-1)),'complete integer gamma')
        require(contains(m.exp_c(lg).im,0),'real integer gamma')
        gamma.append(k)
    panels=[]
    for x,y in ((Q(1),Q(1)),(Q(5,2),Q(13,2)),(Q(4),Q(21)),(Q(3),Q(-20))):
        z=m.C(x,y);lg,ps=m.loggamma_psi(z,pi);lg1,ps1=m.loggamma_psi(z+1,pi)
        require(zero(lg1-lg-m.log_c(z)),'complex loggamma recurrence')
        require(zero(ps1-ps-1/z),'complex digamma recurrence')
        panels.append([rat(x),rat(y)])
    return {'integer_gamma_inputs':gamma,'complex_recurrences':panels,'pi':pi.rec()}

def reconstruct(only_algebra=False):
    m=module()
    result={'schema':'BOR26-1','parent':PARENT,
            'status':'proposed component proofs; no independent mathematical acceptance',
            'rh_proved':False,'gamma_5_2_zero_preservation_proved':False,
            'generic_gamma_preservation_refuted':True,
            'algebra':algebra(m),'primitives':primitive_checks(m)}
    if only_algebra:
        result['root_certificate_executed']=False
    else:
        result['root_certificate_executed']=True
        result['root']=m.reconstruct_root()
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    mode=ap.add_mutually_exclusive_group(required=True)
    mode.add_argument('--emit',type=Path);mode.add_argument('--check',type=Path)
    mode.add_argument('--algebra',action='store_true')
    args=ap.parse_args()
    if args.emit:
        out=reconstruct();args.emit.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n',encoding='utf-8')
        print('PRODUCED_BOR26_UNAUTHENTICATED')
        return
    authenticate()
    if args.algebra:
        reconstruct(only_algebra=True);print('PASS_BOR26_BOUNDED_ALGEBRA_ONLY');return
    expect=load_json(args.check);actual=reconstruct()
    require(canon(expect)==canon(actual),'fresh canonical typed result mismatch')
    print('PASS_BOR26_FULL '+hashlib.sha256(canon(actual).encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,KeyError,OSError,ZeroDivisionError) as e:
        print('REJECT_BOR26 '+str(e),file=sys.stderr);sys.exit(2)
