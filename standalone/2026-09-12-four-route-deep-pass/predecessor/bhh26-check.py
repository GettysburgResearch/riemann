"""BHH26 exact finite algebra, not a machine proof of the analytic theorem.
Python standard library only. No floating point or special-function oracle.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
FILES = {'README.md','PROOF.md','REVIEW.md','SOURCES.json','VALIDATION.md',
         'check.py','test_check.py','result.json','SHA256SUMS'}

def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def frac(x: F | int) -> str:
    return str(F(x))

def ceilq(x: F) -> int:
    return -((-x.numerator)//x.denominator)

def unif_moment(j: int) -> F:
    # E U^(-2j), including nonpositive integers.
    return (1-F(2)**(1-2*j))/(2*j-1)

def rising(x: F, j: int) -> F:
    v=F(1)
    for k in range(j):
        v*=x+k
    return v

def beta_moment(a: F, b: F, j: int) -> F:
    return rising(a,j)/rising(a+b,j)

def beta_int(a: int,b: int) -> F:
    return F(factorial(a-1)*factorial(b-1),factorial(a+b-1))

def rows(last: int):
    u=[1]
    for n in range(last+1):
        yield n,u
        u=[(u[j]**2 if j<len(u) else 0)-2*(u[j-1]**2 if j else 0)
           for j in range(len(u)+1)]

def threshold_records(last: int=6):
    l=v=F(0);out=[]
    for n,u in rows(last):
        d=2**n-1;m=2*d;b=F(1,4**n);p=F(3,2)*2**n+1
        x=[F(1,4**j) for j in range(n+1)]
        r=[(-1)**d*u[j]*4**(j*d) for j in range(n+1)]
        A=sum(abs(t) for t in r);Q=(A+l)**2
        G=Q-sum(t*t for t in r)
        cross=sum((F(abs(r[i]*r[j]),1)/abs(x[i]-x[j])
                   for i in range(n+1) for j in range(n+1) if i!=j),F())
        W=2*p*cross+(2*p-1)/(p-1)*(2*A+l)*v
        C=W+F(2*m+3,2)*G;E0=2*C;E1=2*n*C+G
        L=F(4)**(d-n)
        B=2*m+1+4*(E1+2*n*E0)/L
        T=ceilq(max(F(2),2*E0/L,B,F(320*16**n)))
        need(T>=2*E0/L and T>=B and T>=320*16**n,'threshold guard')
        # The exact bound which precedes the strict logarithmic inequality.
        need(E0/F(T)<=L/2,'remainder cannot be divided')
        need(B/F(T)<=1,'final phase residual too large')
        need(F(10,3)-1-F(1,12*(5*2**n)**2)>2,'constant in D>2')
        out.append({'depth':n,'derivative_order':d,'pair_order':m,
                    'threshold':str(T),'threshold_decimal_digits':len(str(T)),
                    'error_E0':frac(E0),'error_E1':frac(E1),
                    'polynomial_lower_bound':frac(L)})
        J=4**m*Q;VJ=2*4**(m+1)*Q/b
        lnew=(2*m+3)*4/b*J+(2*4**(m+1)+1)*G/b
        vnew=(2*m+3)*(4/b*VJ+16/b**2*J)+2*4**(m+1)*(4/b*W+4/b**2*G)+W/b+G/b**2
        l,v=lnew,vnew
    need(out[1]['threshold']=='279109','first-stage threshold changed')
    return out

def polynomial_controls():
    out=[]
    for n,u in rows(9):
        need(u[0]==1,'leading endpoint')
        if n:
            need(u[-1]==-2**(2**n-1),'terminal amplitude')
            need(all(t>0 for t in u[:-1]),'interior atom sign')
            need(all(abs(u[j])>=2*abs(u[j-1]) for j in range(1,len(u))),
                 'coefficient growth')
        a=[t*t for t in u]
        b=[F(a[j],4**j) for j in range(len(a))]
        need(all(b[j]>=b[j-1] for j in range(1,len(b))),'EK monotonicity')
        # Independently expand (1-w) sum b_j w^j.
        direct=[F(0)]*(len(b)+1)
        for j,t in enumerate(b):direct[j]+=t;direct[j+1]-=t
        expected=[b[0]]+[b[j]-b[j-1] for j in range(1,len(b))]+[-b[-1]]
        need(direct==expected,'EK telescoping polynomial')
        out.append({'depth':n,'degree':n,'row':u if n<=4 else None,
                    'row_sha256':hashlib.sha256(str(u).encode()).hexdigest(),
                    'terminal_bits':abs(u[-1]).bit_length()})
    return out

def atom_controls():
    # Full (unnormalized) derivative atoms versus the integer-array route.
    old={F(1):F(1)};scale=F(1);panels=[]
    for n,u in rows(5):
        d=2**n-1;a=F(5,2)*2**n;p=a-d
        expected={F(1,4**j):scale*(-1)**d*u[j]*4**(j*d) for j in range(n+1)}
        need(old==expected,'independent atom normalization')
        kap=F(1) if n==0 else beta_int(int(p),int(p))/beta_int(int(a),int(a))
        new={}
        for x,c in old.items():
            q=kap*c*c
            new[x]=new.get(x,F())-q/(2*x)
            new[x/4]=new.get(x/4,F())+4**(2*d+1)*q/x
        panels.append({'depth':n,'atoms':len(old),'derivative_scale':frac(scale),
                       'kappa':frac(kap)})
        old=new;scale=kap*scale*scale/2
    return panels

def beta_derivative_controls():
    # Uniform laws: exact direct beta-pair moments against the full D^2 law.
    panels=0
    for lo,hi in [(F(1,4),F(1)),(F(1,16),F(1,4)),(F(2),F(5))]:
        def um(j):return (hi**(j+1)-lo**(j+1))/((j+1)*(hi-lo))
        for shape in (3,4,5,7):
            kap=beta_int(shape-1,shape-1)/beta_int(shape,shape)
            for power in range(13):
                if power<2:left=F()
                else:
                    j=power-2
                    moment=sum((F(comb(j,l))*rising(F(shape),l)*rising(F(shape),j-l)
                                *um(l)*um(j-l)/rising(F(2*shape),j) for l in range(j+1)),F())
                    left=power*(power-1)*moment
                off=sum((F(comb(power,j))*lo**(power-j)*(hi-lo)**j
                         *beta_moment(F(shape-1),F(shape-1),j)
                         for j in range(power+1)),F())
                right=kap*(lo**power+hi**power-2*off)/(hi-lo)**2
                need(left==right,'full beta diagonal/off-diagonal derivative identity')
                panels+=1
    return panels

def scaling_controls():
    panels=0
    for m in range(7):
        for x in (F(1),F(1,4),F(1,16),F(3,2)):
            for j in range(13):
                # 2D Omega_m delta_x: both endpoint atoms and the full interior.
                exponent=F(2*j-2*m-3,2)
                integral=F(1,2)*x**(j-1)*(1-F(2)**(2*m+3-2*j))/exponent
                endpoints=x**(j-1)*(2*F(4)**(m+1-j)-1)
                direct=endpoints-(2*m+3)*integral
                dual=-2*j*x**(j-1)*unif_moment(j-1-m)
                need(direct==dual,'scale derivative boundary/interior identity')
                panels+=1
    # Literal first law W=U^-2, including its continuous derivative.
    for j in range(18):
        cont=-F(3,4)*(1-F(2)**(3-2*j))/F(2*j-3,2)
        lhs=4*F(1,4)**j-F(1,2)+cont
        rhs=-j*unif_moment(j-1)
        need(lhs==rhs,'literal W derivative measure')
    return {'scaled_atom_moments':panels,'literal_W_moments':18}

def qadd(a,b):return (a[0]+b[0],a[1]+b[1])
def qmul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qnorm(a):return a[0]*a[0]+a[1]*a[1]
def qdiv(a,b):
    d=qnorm(b);need(d!=0,'zero rational denominator')
    c=qmul(a,(b[0],-b[1]));return(c[0]/d,c[1]/d)
def rational_polynomial_controls():
    panels=0
    for n,u in rows(6):
        for z in [(F(1,2),F()),(F(-1,2),F()),(F(),F(1,2)),
                  (F(1,2),F(1,4)),(F(3,4),F(1,4))]:
            value=(F(),F());weighted=(F(),F());power=(F(1),F())
            for j,t in enumerate(u):
                term=(t*t*power[0],t*t*power[1]);value=qadd(value,term)
                weighted=qadd(weighted,(j*term[0],j*term[1]));power=qmul(power,z)
            L=F(4)**(2**n-1-n)
            need(qnorm(value)>=L*L,'polynomial lower bound')
            need(qnorm(qdiv(weighted,value))<=4*n*n,'polynomial logarithmic derivative')
            panels+=1
    return panels

def result():
    return {'schema':'BHH26-v1','source_pr':857,
            'source_head':'3f1984867d23b588d09c88a892882411724b174b',
            'status':'proposed component proofs; independent review required',
            'rh_proved':False,'bounded_window_confinement_proved':False,
            'analytic_theorem_machine_verified':False,
            'thresholds':threshold_records(),'polynomials':polynomial_controls(),
            'independent_atoms':atom_controls(),
            'beta_derivative_moments':beta_derivative_controls(),
            'scaling':scaling_controls(),
            'rational_complex_polynomial_cases':rational_polynomial_controls()}

def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)
def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d:raise ValueError('duplicate JSON key')
        d[k]=v
    return d

def read_json(path):
    def reject(_):raise ValueError('noninteger numeric JSON token')
    return json.loads(Path(path).read_text(encoding='utf8'),object_pairs_hook=unique,
                      parse_float=reject,parse_constant=reject)

def inventory():
    entries=list(HERE.iterdir())
    actual={p.name for p in entries}
    need(actual==FILES,'exact file inventory')
    need(all(p.is_file() and not p.is_symlink() for p in entries),'nonregular packet file')
    lines=(HERE/'SHA256SUMS').read_text().splitlines();seen=set()
    for line in lines:
        digest,name=line.split('  ',1)
        need(name in FILES-{'SHA256SUMS'} and name not in seen,'manifest name')
        need(len(digest)==64 and all(c in '0123456789abcdef' for c in digest),'manifest digest format')
        need(hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,'payload hash')
        seen.add(name)
    need(seen==FILES-{'SHA256SUMS'},'manifest coverage')
    source=read_json(HERE/'SOURCES.json')
    need(source['primary']['head']=='3f1984867d23b588d09c88a892882411724b174b','source head')
    need(source['scope']=='selected-source continuation, not exhaustive repository review','scope')

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write');g.add_argument('--check');args=ap.parse_args()
    if args.check:inventory()
    data=result()
    if args.write:
        Path(args.write).write_text(json.dumps(data,sort_keys=True,indent=2)+'\n',encoding='utf8')
        print('PRODUCED_BHH26; not an accepting command')
    else:
        need(canonical(read_json(args.check))==canonical(data),'primitive reconstruction mismatch')
        print('PASS_BHH26 '+hashlib.sha256(canonical(data).encode()).hexdigest())

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,KeyError,OSError,ZeroDivisionError) as exc:
        print('REJECT_BHH26: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
