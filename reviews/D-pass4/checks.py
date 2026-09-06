#!/usr/bin/env python3
"""Independent exact checks for D-pass4. No source producer is imported.

P61 JSON checks authenticate result semantics, NOT a substitute for the C++
primitive/coverage replay. Pick rectangles remain unverified analytic inputs.
"""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path
from typing import Any
import sympy as s
ROOT=Path(__file__).resolve().parent
class Failure(ValueError): pass
def need(b: bool,msg: str)->None:
    if not b: raise Failure(msg)
def pairs_hook(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise Failure('duplicate JSON key')
        out[k]=v
    return out
def read(p: Path)->Any:
    return json.loads(p.read_text(),object_pairs_hook=pairs_hook,parse_constant=lambda x:(_ for _ in ()).throw(Failure(x)))
def integer(x: Any)->int:
    need(type(x) is str and x and (x.isdecimal() or x[0]=='-' and x[1:].isdecimal()),'integer string')
    return int(x)
def rat(a: int|str,b: int|str=1)->F: return F(int(a),int(b))
def gh(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def gs(a,b):return a[0]-b[0],a[1]-b[1]
def gc(a):return a[0],-a[1]
def gd(a,q):return a[0]/q,a[1]/q
def norm(a):return a[0]*a[0]+a[1]*a[1]
def beta(n: int,q: int)->F:
    a,r=divmod(n,q)
    return F(a*(q-1-r),n+1)
def invert(h:dict[int,F],N:int)->dict[int,F]:
    c={}
    for q in range(N,1,-1):
        c[q]=(h[q]-sum((beta(n,q)*c[n] for n in range(q+1,N+1)),F(0)))/beta(q,q)
    return c
def invsqrt(n:int,bits:int=180)->tuple[F,F]:
    Q=1<<bits;k=math.isqrt(Q*Q//n)
    need(k*k*n<=Q*Q<(k+1)*(k+1)*n,'root enclosure')
    return F(k,Q),F(k+1,Q)
def enclose_linear(coeff:dict[int,F])->tuple[F,F]:
    lo=hi=F(0)
    for n,c in coeff.items():
        a,b=invsqrt(n)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi

def p61_contract(data:dict)->None:
    need(data.get('schema')=='reviewer-D.P61.integer-interval-replay.v1','P61 schema')
    need(data.get('status')=='PASS' and data.get('RH_proved') is False,'status')
    for k,v in {'primitive_precision':256,'finite_endpoint':1000000,'finite_inequalities_checked':1999994,'compact_samples':1401,'compact_Lipschitz_bound':36,'divisor_count':262144}.items():
        need(type(data.get(k)) is int and data[k]==v,k)
    D=integer(data['finite_denominator']);need(D==2**96,'finite denominator')
    ms=data['finite_minima'];need(type(ms) is list and len(ms)==5,'minima count')
    for j,(m,arg,bound) in enumerate(zip(ms,[3,5,184,67,184],[4,3,3,135,-18])):
        need(type(m['test']) is int and m['test']==j and m['N']==arg,'min record')
        l,h=map(integer,m['numerator_interval']);need(l<=h,'ordered minima')
        need(l>bound*D if j<4 else h<bound*D,'strict finite sign')
    c0=list(map(integer,data['compact_C0_numerators']));need(-20*D<c0[0]<=c0[1]<0,'C0 coarse')
    need(4*integer(data['compact_sample_upper_numerator'])<13*D,'compact error')
    need(F(13,4)+F(36,100)<5,'compact extension')
    TD=integer(data['tail_denominator']);need(TD==2**192,'tail denom')
    ts=data['tail_minima'];need(len(ts)==2,'tail count')
    for j,(t,b) in enumerate(zip(ts,[119,40000])):
        need(t['test']==j and type(t['slabs_checked']) is int and t['slabs_checked']==256805,'slab coverage')
        need(integer(t['lower_numerator'])>b*TD,'tail bound')
        need(integer(t['left'])>=1000000 and integer(t['right'])>integer(t['left']),'slab endpoints')

def run()->dict:
    records=[]
    def done(name:str,n:int,detail:Any=True):records.append({'name':name,'fixtures':n,'detail':detail})
    a=read(ROOT/'p61.full.json');b=read(ROOT/'p61.clang.json');p61_contract(a);p61_contract(b)
    need(a==b,'compiler results differ');done('P61_full_replay_result_contract',1,{'finite_inequalities':1999994,'tail_slabs_each':256805})
    high=read(ROOT/'constant.audit.json');need(high['denominator_exponent']==200,'C0 high precision scale')
    l,h=[F(integer(v),2**200) for v in high['numerators']];singleton=F('-13.721771741974681191')
    need(l<=h<singleton,'serialized C0 interval excludes exact constant')
    done('P61_serialized_C0_singleton_is_invalid',1,{'gap_lower':str(singleton-h)})
    # Independently compare the new closed coefficient formula to prime convolution.
    N=2000;ps=list(s.primerange(2,62));p_mu=[0]*(N+1);om=[0]*(N+1)
    for n in range(1,N+1):
        fct=s.factorint(n);om[n]=sum(p in fct for p in ps)
        p_mu[n]=int(s.mobius(n)) if all(p<=61 for p in fct) else 0
    q=[0]+[0 if n==1 else 15 if n==2 else 3 if n==4 else 6 for n in range(1,N+1)]
    f=q[:];m=q[:]
    for p in ps:
        for k in range(N//p,0,-1):f[p*k]-=f[k];m[p*k]+=m[k]
    for n in range(1,N+1):
        c=lambda d:p_mu[n//d] if n%d==0 else 0
        v=lambda d:int(c(d)!=0)
        need(f[n]==6*int(om[n]==0)-6*c(1)+9*c(2)-3*c(4),'signed coeff')
        need(m[n]==6*2**om[n]-6*v(1)+9*v(2)-3*v(4),'unsigned coeff')
    done('P61_closed_coefficients_vs_independent_convolution',2*N)
    # Conditional eight-point Pick box, with fresh Gaussian-rational LDL.
    pk=read(ROOT/'pick68.extract.json');need(len(pk['rectangles'])==8,'Pick count')
    xs=[];v=[];r=[]
    for row in pk['rectangles']:
        e,er,rl,rh,ei,il,ih=row;rl,rh=F(rl)/2**er,F(rh)/2**er;il,ih=F(il)/2**ei,F(ih)/2**ei
        need(rl<=rh and il<=ih,'rectangle order');xs.append(F(1,2**e));v.append(((rl+rh)/2,(il+ih)/2));r.append((rh-rl+ih-il)/2)
    need([row[0] for row in pk['rectangles']]==[17,15,13,11,10,9,7,5],'point freeze')
    M=[[gd((v[i][0]+v[j][0],v[i][1]-v[j][1]),xs[i]+xs[j]) for j in range(8)] for i in range(8)]
    R=max(sum(((r[i]+r[j])/(xs[i]+xs[j]) for j in range(8)),F(0)) for i in range(8))
    need(R==rat(*pk['claimed_radius']),'Pick radius transcription')
    L=[[(F(0),F(0)) for _ in range(8)] for _ in range(8)];ds=[];shift=F(1,2**137)
    for i in range(8):
        d=M[i][i][0]-shift-sum((norm(L[i][k])*ds[k] for k in range(i)),F(0));need(d>0,'Pick LDL pivot');ds.append(d);L[i][i]=(F(1),F(0))
        for j in range(i+1,8):
            z=M[j][i]
            for k in range(i):
                u=gh(L[j][k],gc(L[i][k]));z=gs(z,(u[0]*ds[k],u[1]*ds[k]))
            L[j][i]=gd(z,d)
    need(shift-R>F(1,2**138),'Pick final moat')
    done('Pick68_all_eight_conditional_LDL_pivots_and_radius',9,{'primitive_replay':False,'radius':str(R),'lower_bound':'2^-138'})
    # Exact positive-measure/indefinite-observation separator at a literal prime atom.
    z=s.symbols('z',real=True)
    residual=-s.Rational(1,8)*(1+z)+s.Rational(17,128)*(1+2*z)-s.Rational(1,256)*(1+4*z)
    need(s.expand(residual-(s.Rational(1,256)+z/8))==0,'prime-two residual')
    need(s.expand(-2*residual+s.Rational(1,128)+z/4)==0,'elementary negative kernel')
    done('Actual_prime_two_elementary_kernel_is_negative',2,{'kernel':'-1/128-log(2)/4','scale':1,'carrier':0})
    # Arbitrary rational complex source: bridge and Haar identities at every scale.
    tests=0
    for N in [2,4,8,16,32,64]:
        c=[(F(0),F(0))]+[(F((j*j+3*j)%11-5,7),F(j%5-2,3)) for j in range(1,N+1)]
        C=[(F(0),F(0))]
        for x in c[1:]:C.append((C[-1][0]+x[0],C[-1][1]+x[1]))
        Rv=[gs(gs(C[N],C[j]),C[N-j-1]) for j in range(N)]
        mean=tuple(sum(x[k] for x in Rv)/N for k in [0,1]);energy=norm(mean);coarse=0
        ell=1
        while ell<=N//2:
            if ell*ell>N:coarse+=N//(2*ell)
            need(sum(min(t,2*ell-t)**2 for t in range(1,2*ell))==(2*ell**3+ell)//3,'triangle mass');tests+=1
            for u in range(0,N,2*ell):
                H=tuple(sum(Rv[j][k] for j in range(u,u+ell))-sum(Rv[j][k] for j in range(u+ell,u+2*ell)) for k in [0,1])
                w=lambda x,k:sum(min(t,2*ell-t)*c[x+t][k] for t in range(1,2*ell))
                T=tuple(w(u,k)-w(N-u-2*ell,k) for k in [0,1]);need(H==T,'Haar reflected identity');tests+=1
                energy+=norm(H)/(2*ell*N)
            ell*=2
        need(energy==sum(norm(x) for x in Rv)/N,'Haar Parseval');need(coarse**2<N,'coarse count');tests+=2
    done('Complete_complex_bridge_Haar_reconstruction',tests)
    # Exact average-carry inverses, including full row reconstructions.
    for N,kind in [(60,'linear'),(126,'geometric')]:
        h={q:F(N+1-q) if kind=='linear' else F(99,100)**q-F(99,100)**N for q in range(2,N+1)};cv=invert(h,N)
        for q in h:need(sum((beta(n,q)*cv[n] for n in range(q,N+1)),F(0))==h[q],'carry reconstruction')
        if N==60:need(cv[11]==F(-2,55) and cv[10]==F(53,45) and cv[12]==F(131,33),'linear witness')
        else:need(F(-666,10**6)<cv[9]<F(-665,10**6),'geometric witness')
        done('Carry_inverse_'+kind,N-1,{'negative_coefficient':str(cv[11] if N==60 else cv[9])})
    # Directed backward dual pullback for the T=894 residual, all eliminated rows.
    N=894;start=56;p={}
    for n in range(start,N+1):
        target=beta(n,28)-beta(n,29)
        p[n]=(target-sum((beta(n,q)*p[q] for q in range(start,n)),F(0)))/beta(n,n)
    coeff={28:F(1),29:F(-1)}
    for n,w in p.items():coeff[n]=coeff.get(n,F(0))-w;coeff[N]=coeff.get(N,F(0))+w
    l,h=enclose_linear(coeff);need(F('-0.000004638')<l<=h<F('-0.000004637'),'T894 negative residual')
    done('T894_full_elimination_dual_radical_witness',839,{'lower':str(l),'upper':str(h)})
    # Positive hinge mixture: exact second-difference telescoping (formal values).
    nchecks=0
    for T in range(3,41):
        # arbitrary rational convex powers suffice to test the telescoping identity,
        # while square-root convexity is proved analytically in the manuscript.
        h={q:F(1,q)-F(1,T) for q in range(2,T+1)};h[T+1]=F(0)
        om={k:h[k]-2*h[k+1]+h[k+2] for k in range(2,T)}
        need(all(v>0 for v in om.values()),'hinge weights')
        for q in range(2,T+1):need(sum((om[k]*max(k+1-q,0) for k in om),F(0))==h[q],'hinge telescope');nchecks+=1
    done('Positive_hinge_mixture_telescoping',nchecks)
    # Exact Q(sqrt2) reward from primitive polynomial and direct Pascal action.
    t=s.symbols('t');P=s.Poly((1-t)**2*(1-t/s.sqrt(2))*(1+t)*(1+s.Rational(3,4)*t+t*t),t)
    qs=[s.expand(P.nth(j)) for j in range(7)];S=[s.simplify(sum(qs[:j+1])) for j in range(7)]
    fs=[];prefix=s.S.Zero
    for m in range(1,257):
        j=min(m.bit_length()-1,6);Fv=m-S[j];fs.append(Fv)
        if m<2:continue
        d=s.simplify(((m-1)*Fv-2*sum(fs[:-1]))/(m*(m-1)))
        Aj=2*sum(2**i*S[i] for i in range(j));formula=(Aj+(m+1-2**(j+1))*S[j])/(m*(m-1))
        need(s.simplify(d-formula)==0,'reward primitive identity')
        need(bool(d<0)==(13<=m<=63),'reward sign')
        prefix+=d;need(bool(prefix>s.Rational(9,10)) and bool(prefix<s.Rational(21,10)),'reward prefix')
    need(s.simplify(S[6])==0 and s.simplify(2*sum(2**i*S[i] for i in range(6))-39*(s.sqrt(2)-1))==0,'reward infinite tail')
    done('Primitive_factor64_Pascal_reward_and_prefix',256)
    # Algebraic derivative bridge on each open dyadic cell.
    y=s.symbols('y',positive=True);rt=s.sqrt(2);lg=s.log(2)
    K=[8*s.sqrt(y)-8-3*s.log(y),-8*rt*s.sqrt(y)+8*(1+rt)+3*(1+rt)*s.log(y)-3*(2+rt)*lg,4*s.sqrt(y)-8*rt+9*rt*lg-3*rt*s.log(y)]
    weights=[1,-(2+rt),1+2*rt,-rt]
    for j in range(4):
        derivative=y*s.diff(K[j],y) if j<3 else 0
        shifted=sum(weights[k]*(4*s.sqrt(y/2**k)-3) for k in range(j+1))
        need(s.simplify(derivative-shifted)==0,'SHARP derivative bridge')
    need(s.simplify(K[0].subs(y,1))==0 and s.simplify(K[2].subs(y,8))==0,'wavelet endpoint')
    done('SHARP_wavelet_derivative_bridge_open_cells',6)
    # Fixed-scale endpoint and polarization elementary checks (not an RH sign).
    for u,v in [((F(1),F(2)),(F(-3),F(1))),((F(2,3),F(0)),(F(7),F(-1)))]:
        need(norm(gs(u,v))-norm(u)-norm(v)==-2*gh(u,gc(v))[0],'Wick signed terms')
    done('Wick_Green_signed_not_positive_decomposition',2)
    # Correct causal inverse mass, exact until a dyadic horizon.
    for n in range(21):
        r=sum(s.sqrt(2)**j for j in range(n+1));need(s.simplify((s.sqrt(2)-1)*r-(s.sqrt(2)**(n+1)-1))==0,'critical inverse')
    done('Fixed_critical_dyadic_inverse_mass',21)
    return {'schema':'reviewer-D.pass4.checks.v1','status':'PASS','records':records,'named_checks':len(records),'bounded_fixtures':sum(r['fixtures'] for r in records),'RH_proved':False,'primitive_Pick_values_recomputed':False}

def main()->None:
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--compare',type=Path);a=p.parse_args();out=run()
    if a.compare:need(read(a.compare)==out,'result mismatch')
    text=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if a.output:a.output.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
