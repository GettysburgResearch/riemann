#!/usr/bin/env python3
"""Bounded exact controls, not a proof of the analytic theorem or count bound."""
from __future__ import annotations
import argparse, hashlib, json, math
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PARENT='cdbe96a71523c81a7f50c8fe990f0f702ab49c82'
PARENTS={
 'annular-scalar-route/PROOF.md':('0f1b21227d064e61f4f532d9025c78106baa688e','c68840c91308d4a93b85d38e34edc5c5ba9a335b2b25d0b4546a9e86979ffd04'),
 'height-transfer-and-prime-squares/PROOF.md':('2ee61d78b5bcf8e06de973f7e29634112c37e1a9','5208d208fcab211e325dac86c236d085c080a4389fd8933f59e4cac802b9fced'),
 'prime-curvature-and-failure-count/PROOF.md':('d74f2d0fc75ffedd53198f7b12b5bcbbdba8b6c5','74b73d0d2203735de7f989ca12645624911a9bd860bbcb3df861d87c8c24c5da')}
INVENTORY={'README.md','PROOF.md','SOURCES_AND_SYNTHESIS.md','SOURCE_LOCK.json',
 'VALIDATION.md','verify.py','test_rejections.py','result.json','SHA256SUMS'}
PROOF_SHA='036e9d3d7b429e9ac8d850e81910c53addfa1d9654050732cfc3dc8bcc4e47c7'


def require(ok: bool, message: str) -> None:
    if not ok: raise ValueError(message)

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()

def unique(pairs):
    out={}
    for key,val in pairs:
        require(key not in out,'duplicate JSON key')
        out[key]=val
    return out

def load_json(path: Path):
    return json.loads(path.read_text(),object_pairs_hook=unique,
                      parse_float=lambda _: (_ for _ in ()).throw(ValueError('float rejected')))

@dataclass(frozen=True)
class I:
    lo: Q
    hi: Q
    def __post_init__(self):
        require(type(self.lo) is Q and type(self.hi) is Q and self.lo<=self.hi,'bad interval')
    @staticmethod
    def point(x):
        x=Q(x); return I(x,x)
    def __add__(self, other):
        o=other if isinstance(other,I) else I.point(other)
        return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-as_i(other)
    def __rsub__(self,other): return as_i(other)+-self
    def __mul__(self,other):
        o=as_i(other); v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(min(v),max(v))
    __rmul__=__mul__
    def enclose(self,bits=112):
        d=1<<bits
        l=(self.lo.numerator*d)//self.lo.denominator
        h=-((-self.hi.numerator*d)//self.hi.denominator)
        return {'lower_numerator':l,'upper_numerator':h,'denominator_power_two':bits}

def as_i(x): return x if isinstance(x,I) else I.point(x)

def atan_inv(n: int, terms=64) -> I:
    x=Q(1,n)
    s=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    nxt=(-1)**terms*x**(2*terms+1)/Q(2*terms+1)
    return I(min(s,s+nxt),max(s,s+nxt))

def log_small(x:Q, terms=64) -> I:
    require(Q(1)<=x<=Q(2),'log range')
    t=(x-1)/(x+1)
    val=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    rem=2*t**(2*terms+1)/(Q(2*terms+1)*(1-t*t))
    return I(val,val+rem)

LOG2=log_small(Q(2))
def logq(x:Q) -> I:
    require(x>0,'log domain'); k=0
    while x>2: x/=2; k+=1
    while x<1: x*=2; k-=1
    return log_small(x)+k*LOG2

def logi(x:I)->I:
    return I(logq(x.lo).lo,logq(x.hi).hi)

def power2(e:Q)->Q:
    require(e.denominator==1,'noninteger power in exact helper')
    k=e.numerator
    return Q(2**k) if k>=0 else Q(1,2**(-k))

# Pairs encode rational + rational*log(2).
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(a,x): return (a*x[0],a*x[1])
def monomial_integral(exponent:Q,left:int,right:int):
    # endpoints are 4^left and 4^right.
    t=exponent+1
    if not t: return (Q(0),Q(2*(right-left)))
    return ((power2(2*right*t)-power2(2*left*t))/t,Q(0))
def J_integral(s:Q):
    out=(Q(0),Q(0))
    for l,r,a,b in [(-1,0,Q(1,3),-Q(1,192)),(0,1,-Q(1,192),Q(1,3))]:
        out=add(out,mul(a,monomial_integral(s,l,r)))
        out=add(out,mul(b,monomial_integral(s-3,l,r)))
    return out

def w(x:Q)->Q:
    if x<=Q(1,4) or x>=4: return Q(0)
    return x/3-1/(192*x*x) if x<=1 else 1/(3*x*x)-x/192

def prime_power_sieve(n:int):
    out=[0]*(n+1); primes=[]
    mark=[True]*(n+1)
    if n>=0: mark[0]=False
    if n>=1: mark[1]=False
    for p in range(2,n+1):
        if mark[p]:
            primes.append(p)
            for j in range(p*p,n+1,p): mark[j]=False
            q=p
            while q<=n:
                out[q]=p; q*=p
    return out

def trial_base(n:int):
    if n<2: return 0
    p=next((d for d in range(2,math.isqrt(n)+1) if n%d==0),n)
    q=n
    while q%p==0: q//=p
    return p if q==1 else 0

def authenticate(check_manifest:bool):
    require(sha((ROOT/'PROOF.md').read_bytes())==PROOF_SHA,'proof mismatch')
    lock=load_json(ROOT/'SOURCE_LOCK.json')
    require(lock['publication_parent']==PARENT,'wrong parent')
    require({x['path'] for x in lock['parents']}==set(PARENTS),'parent scope mismatch')
    for entry in lock['parents']:
        p=ROOT.parent/entry['path']; require(not p.is_symlink(),'parent symlink')
        data=p.read_bytes(); blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        gb,sh=PARENTS[entry['path']]
        require(blob==gb==entry['git_blob'] and sha(data)==sh==entry['sha256'],'parent bytes mismatch')
        require(type(entry['bytes']) is int and entry['bytes']==len(data),'parent length mismatch')
    if not check_manifest: return
    require(all(not p.is_symlink() for p in ROOT.rglob('*')),'symlink rejected')
    require({p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}==INVENTORY,'inventory mismatch')
    rows={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,name=line.split('  ',1)
        require(name not in rows,'duplicate checksum')
        rows[name]=h
    require(set(rows)==INVENTORY-{'SHA256SUMS'},'manifest coverage')
    for name,h in rows.items(): require(sha((ROOT/name).read_bytes())==h,'checksum mismatch: '+name)

def reconstruct():
    counts={}; fixtures=0
    def check(group,ok):
        nonlocal fixtures
        require(ok,group); counts[group]=counts.get(group,0)+1; fixtures+=1
    for n in range(1,513): check('prime_power_sieve',prime_power_sieve(512)[n]==trial_base(n))
    for k in range(-6,10):
        s=Q(k,2); r=s-Q(1,2)
        j=J_integral(s)
        if s in (Q(-1),Q(2)): target=(Q(0),Q(21,32))
        else: target=((Q(65,64)-(power2(2*r)+power2(-2*r))/8)/(Q(9,4)-r*r),Q(0))
        check('mellin_weight',j==target)
        check('mellin_reflection',j==J_integral(1-s))
    check('mellin_normalization',J_integral(Q(1))==(Q(45,128),Q(0)))
    check('mellin_normalization',J_integral(Q(1,2))==(Q(49,144),Q(0)))
    for m in range(1,13): check('affine_pole_residue',-Q(1,2)*2*m==-m)
    pi=16*atan_inv(5)-4*atan_inv(239)
    hn=sum((Q(1,j) for j in range(1,1025)),Q(0))
    gn=I(hn-logq(Q(1024)).hi-Q(1,1024),hn-logq(Q(1024)).lo)
    c0=Q(47,64)-Q(21,64)*(gn+logi(pi))+Q(115,96)*LOG2-Q(641,1728)*logq(Q(3))-Q(65,192)*logq(Q(5))
    check('source_constant',c0.lo>Q(1,25) and c0.hi<Q(1,20))
    check('source_constant',Q(1,4)-c0.hi-Q(1,10)>Q(1,10))
    check('source_constant',(Q(1,6)+Q(1,3)*LOG2).hi<Q(2,5))
    panels=[]; pp=prime_power_sieve(576); logs={p:logq(Q(p)) for p in set(pp) if p}
    for m in range(2,13):
        p=sum((Q(1,m)*w(Q(n,m*m))*logs[pp[n]] for n in range(2,4*m*m+1) if pp[n]),I.point(0))
        dd=p-Q(45,128)*m+Q(1,4)
        check('bounded_native_values',dd.lo>0)
        panels.append({'m':m,'D_interval':dd.enclose()})
    for h in (0,1,5):
        for d0 in (-30,-15,-5,-1,0,3,15):
            for inc in (-13,-1,0,1,13):
                for k in range(9):
                    value=Q(d0)+Q(inc*k,8)
                    if d0>=-h: check('unit_cell_background',value+h+13>=0)
    for T in (16,32,64,128):
        nodes=list(range(2,math.isqrt(2*T)+2))
        # Deterministic bounded subset fixtures, not an exhaustive all-length run.
        for mask in range(64):
            bad={n for i,n in enumerate(nodes) if (mask>>(i%6))&1}
            cells={j for n in bad for j in (n-1,n) if j>=3}
            length=sum((max(0,min(2*T,(j+1)**2)-max(T,j*j)) for j in cells),0)
            f=sum(1 for n in bad if n<=math.isqrt(4*T))
            check('square_cell_geometry',length*length<=144*T*f*f)
    rec=[]
    for r in (1,2):
        for delta in (Q(1),Q(1,2),Q(1,3),Q(1,7),Q(1,10),Q(1,100),Q(1,1000)):
            u=Q(1); step=delta/r; steps=(step.denominator+step.numerator-1)//step.numerator
            for j in range(1,steps+1):
                u=max(Q(0),u-step)
                check('feedback_iteration',u==max(Q(0),1-j*step))
            check('feedback_termination',u==0 and 1-(steps-1)*step>0)
            rec.append({'r':r,'delta':str(delta),'steps':steps})
        for alpha in (Q(1,100),Q(1,10),Q(1,2),Q(1)):
            for delta in (Q(1,1000),Q(1,10),Q(1)):
                check('strict_supremum_gap',max(Q(0),alpha-delta/r)<alpha)
    # Synthetic control: without real-axis regularity a positive function has a real pole.
    for a in (Q(1,10),Q(1,2),Q(1)):
        for s in (Q(2),Q(3)):
            check('real_pole_control',(s-a)*Q(1,s-a)==1)
    # Resonant Fourier coefficient and means; no zeta-zero data.
    modes={-2:Q(1,6),-1:Q(1,2),1:Q(1,2),2:Q(1,6)}
    v={0:Q(1)}
    for degree in range(1,9):
        nxt={}
        for i,a in v.items():
            for j,b in modes.items(): nxt[i+j]=nxt.get(i+j,Q(0))+a*b
        v=nxt
        if degree%2==0: check('resonant_fourier_means',v.get(0,Q(0))>0)
    return {'schema':'sparse-sign-bootstrap-v1','status':'PROPOSED_COMPONENT_PROOFS',
        'RH_proved':False,'native_power_saving_proved':False,'new_positive_range':False,
        'global_theorems_machine_proved':False,'parent':PARENT,
        'finite_groups':counts,'finite_fixture_total':fixtures,
        'C0_interval':c0.enclose(),'native_fixture_scope':{'m_min':2,'m_max':12,'all_source_integers_through':576},
        'native_fixtures':panels,'conditional_feedback_arithmetic':rec,
        'analytical_boundary':'Landau, spectral expansion, all-K count, and almost-periodic recurrence are paper arguments; no count saving is established.'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--check',type=Path); ap.add_argument('--write',type=Path)
    args=ap.parse_args(); require(not(args.check and args.write),'choose write or check')
    authenticate(check_manifest=not bool(args.write))
    result=reconstruct(); encoded=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.write: args.write.write_text(encoded)
    elif args.check:
        expected=load_json(args.check)
        require(json.dumps(expected,sort_keys=True,separators=(',',':'))==json.dumps(result,sort_keys=True,separators=(',',':')),'result mismatch')
    print(encoded,end='')

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,KeyError,TypeError) as e:
        raise SystemExit('REJECT: '+str(e))
