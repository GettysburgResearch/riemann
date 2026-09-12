#!/usr/bin/env python3
"""Whole-source, outward-rational ten-moment existence certificate. Not RH.
Interval primitives adapted from the FMS26 seed (see SOURCES.json), extended
to 512 bits and 24th-order integrated Taylor control. Standard library only.
"""
from fractions import Fraction as F
from math import factorial, comb, isqrt
import argparse, json, hashlib
from pathlib import Path

BITS=512
S=1<<BITS

def ceildiv(a,b):
    return -((-a)//b)

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def point(x):
        x=F(x)
        return I(x.numerator*S//x.denominator,ceildiv(x.numerator*S,x.denominator))
    @staticmethod
    def bounds(a,b):
        a=F(a);b=F(b)
        return I(a.numerator*S//a.denominator,ceildiv(b.numerator*S,b.denominator))
    def __add__(self,y):
        y=asI(y);return I(self.lo+y.lo,self.hi+y.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,y):return self+-asI(y)
    def __rsub__(self,y):return asI(y)+-self
    def __mul__(self,y):
        y=asI(y);v=[self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return I(min(v)//S,ceildiv(max(v),S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ValueError('division through zero')
        return I(S*S//self.hi,ceildiv(S*S,self.lo))
    def __truediv__(self,y):return self*asI(y).inv()
    def __pow__(self,n):
        if type(n) is not int or n<0:raise ValueError('nonnegative integer power required')
        r=I.point(1);a=self
        while n:
            if n&1:r=r*a
            n//=2
            if n:a=a*a
        return r
    def widened(self,r):
        r=F(r);n=ceildiv(r.numerator*S,r.denominator)
        return I(self.lo-n,self.hi+n)
    def sqrt(self):
        if self.lo<0:raise ValueError("sqrt of negative interval")
        lo=isqrt(self.lo*S);hi=isqrt(self.hi*S)
        if hi*hi<self.hi*S:hi+=1
        return I(lo,hi)
    def contains(self,x):
        x=F(x);return F(self.lo,S)<=x<=F(self.hi,S)
    def decimal(self,digits=15):
        k=10**digits
        def fmt(a):
            return ('-' if a<0 else '')+str(abs(a)//k)+'.'+str(abs(a)%k).zfill(digits)
        return [fmt(self.lo*k//S),fmt(ceildiv(self.hi*k,S))]
    def raw(self):return [str(self.lo),str(self.hi)]

def asI(x):return x if isinstance(x,I) else I.point(x)

def exp_at(x):
    # x is an exact dyadic endpoint, not a float.
    if x==0:return I.point(1)
    # e>2 gives exp(x)<=2^-BITS for x<=-BITS.
    if x<=-BITS*S:return I(0,1)
    r=max(0,(8*abs(x)).bit_length()-BITS)
    while 8*abs(x)>S*(1<<r):r+=1
    y=I(x//(1<<r),ceildiv(x,1<<r))
    if max(abs(y.lo),abs(y.hi))*8>S:raise ValueError('exp reduction failed')
    term=I.point(1);total=term
    for j in range(1,65):
        term=term*y/j;total=total+term
    # For |y|<=1/8 the omitted tail is <=2 |y|^65/65!.
    rem=F(2,8**65*factorial(65));total=total.widened(rem)
    if total.lo<=0:raise ValueError('nonpositive reduced exponential')
    for _ in range(r):total=total*total
    return total

def exp(x):
    x=asI(x)
    if x.hi<=-BITS*S:return I(0,1)
    if x.hi<=0:
        # exp is 1-Lipschitz on the negative half-line.
        a=exp_at(x.lo)
        return I(a.lo,min(S,a.hi+x.hi-x.lo))
    return I(exp_at(x.lo).lo,exp_at(x.hi).hi)

def atan_inv(k):
    x=F(1,k);a=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(110)),F(0))
    rem=x**221/221
    return I.bounds(a,a+rem) # 110 terms: final sign negative; next positive.

def pi_interval():return 16*atan_inv(5)-4*atan_inv(239)


def need(ok, message):
    if not ok:
        raise ValueError(message)

def abs_upper(x):
    x=asI(x)
    return F(max(abs(x.lo),abs(x.hi)),S)

def pow_signed(x,k):
    return x**k if k>=0 else (x**(-k)).inv()

def poly_eval(poly,x):
    out=I.point(0)
    for k in range(max(poly),-1,-1):
        out=out*x+poly.get(k,F(0))
    return out

def derivative_polynomials(n):
    p={1:F(-6),2:F(4)};ans=[]
    for j in range(n+1):
        ans.append(p)
        q={}
        for k,c in p.items():
            q[k]=q.get(k,F(0))+(2*k+F(1,2))*c
            q[k+1]=q.get(k+1,F(0))-2*c
        p={k:c for k,c in q.items() if c}
    return ans

def theta_moments():
    """128 midpoint Taylor cells, degree 23, and all omitted source tails."""
    orders=list(range(0,11,2));cells=128;n=24;terms=8;half=F(1,cells)
    ps=derivative_polynomials(n)
    Bs=[F(3*terms,2)*sum(abs(c)*factorial(k-1) for k,c in p.items()) for p in ps]
    sums={m:I.point(0) for m in orders};pi=pi_interval()
    coeff=[2*half**(k+1)/factorial(k+1) for k in range(0,n,2)]
    for j in range(cells):
        t=F(2*j+1,cells);et=exp(I.point(2*t));fac=exp(I.point(t/2))
        deriv=[I.point(0) for k in range(n)]
        for index in range(1,terms+1):
            q=pi*(index*index)*et;e=fac*exp(-q)
            for k in range(n):
                deriv[k]=deriv[k]+e*poly_eval(ps[k],q)
        for m in orders:
            for ell,k in enumerate(range(0,n,2)):
                df=sum((F(comb(k,v)*factorial(m),factorial(m-v))*t**(m-v)*deriv[k-v]
                         for v in range(min(k,m)+1)),I.point(0))
                sums[m]=sums[m]+coeff[ell]*df
    raw={};errors={}
    for m in orders:
        C=sum(F(comb(n,j)*factorial(m),factorial(m-j))*2**(m-j)*Bs[n-j]
              for j in range(min(n,m)+1))
        error=2*half**n*C/factorial(n)
        # t^m <= m! e^t. Every omitted term is nonnegative on t>=0.
        # n>=9: Q0>243; t>=2: Q0>150 n^2. Both whole sums are paid.
        ti=8*factorial(m)*59537*exp(I.point(-243))
        tp=8*factorial(m)*22802*exp(I.point(-150))
        val=(2*sums[m]).widened(error)
        raw[m]=I(val.lo,val.hi+ti.hi+tp.hi)
        errors[str(m)]={'taylor_L1':str(error),'index_tail_upper':str(F(ti.hi,S)),
                        'physical_tail_upper':str(F(tp.hi,S))}
    need(raw[0].lo>0 and raw[2].lo>0,'positive source mass and variance')
    mu={m:raw[m]/raw[0] for m in orders}
    std={m:(I.point(1) if m==2 else mu[m]/mu[2]**(m//2)) for m in orders[1:]}
    return raw,mu,std,errors

def graph_values(parameters,n1=8,n2=64,r=F(101,100),c=F(1001,1000),max_order=10):
    """All block/hub states with multiplicities, and exact analytic Jacobian."""
    q1,q2,a,b=map(asI,parameters);r=asI(r);c=asI(c)
    need(n1%2==0 and n2%2==0 and min(n1,n2)>=2,'positive even block sizes')
    need(max_order>=4 and max_order%2==0,'even output order')
    ss=list(range(-n1,n1+1,2));ts=list(range(-n2,n2+1,2))
    orders=list(range(0,max_order+1,2))
    q1powers={j:q1**j for j in {s*s//4 for s in ss}}
    q2powers={j:q2**j for j in {t*t//4 for t in ts}}
    rpowers={j:pow_signed(r,j) for j in {s*t//4 for s in ss for t in ts}}
    cpowers={j:pow_signed(c,j) for j in {s*e//2 for s in ss for e in [-1,1]}}
    raw={k:I.point(0) for k in orders};d={k:[I.point(0) for j in range(4)] for k in orders}
    for s in ss:
        for t in ts:
            binomial=comb(n1,(s+n1)//2)*comb(n2,(t+n2)//2)
            for e in [-1,1]:
                w=binomial*q1powers[s*s//4]*q2powers[t*t//4]*rpowers[s*t//4]*cpowers[s*e//2]
                x=s+a*t+b*e;xp=[I.point(1)]
                for k in range(max_order):
                    xp.append(xp[-1]*x)
                for k in orders:
                    term=w*xp[k];raw[k]=raw[k]+term
                    d[k][0]=d[k][0]+term*(s*s//4)/q1
                    d[k][1]=d[k][1]+term*(t*t//4)/q2
                    if k:
                        d[k][2]=d[k][2]+w*k*t*xp[k-1]
                        d[k][3]=d[k][3]+w*k*e*xp[k-1]
    Z=raw[0];need(Z.lo>0,'positive graph normalizer')
    mu={k:raw[k]/Z for k in orders}
    dm={k:[(d[k][j]-mu[k]*d[0][j])/Z for j in range(4)] for k in orders}
    v=mu[2];need(v.lo>0,'positive graph variance')
    out=[];jac=[]
    for k in range(4,max_order+1,2):
        j=k//2;out.append(mu[k]/v**j)
        jac.append([(dm[k][l]-j*mu[k]*dm[2][l]/v)/v**j for l in range(4)])
    return out,jac,v,mu

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),I.point(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def inverse_rational(A):
    n=len(A)
    rows=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        k=next((k for k in range(j,n) if rows[k][j]),None)
        need(k is not None,'singular preconditioner')
        rows[j],rows[k]=rows[k],rows[j];pivot=rows[j][j]
        rows[j]=[x/pivot for x in rows[j]]
        for i in range(n):
            if i!=j:
                p=rows[i][j];rows[i]=[x-p*y for x,y in zip(rows[i],rows[j])]
    return [row[n:] for row in rows]

def strict_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key');out[k]=v
        return out
    def bad(v):
        raise ValueError('noninteger JSON numeric literal')
    return json.loads(Path(path).read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_float=bad,parse_constant=bad)

def validate_certificate(data):
    """Check the claimed predicates, including literal types; no data invention."""
    need(type(data.get('schema')) is int and data['schema']==1,'schema')
    need(data.get('status')=='PROPOSED_TEN_MOMENT_REALIZATION_NOT_RH','status')
    need(data.get('rh_proved') is False,'RH not proved')
    need(data.get('all_order_theta_realization_proved') is False,'all-order not proved')
    need(type(data['graph']['spins']) is int and data['graph']['spins']==73,'73 spins')
    need(data['graph']['matched_even_moments']==[2,4,6,8,10] and
         all(type(x) is int for x in data['graph']['matched_even_moments']),'moment scope')
    d=data['contraction'];beta=F(d['row_bound']);radius=F(d['parameter_radius'])
    displacement=F(d['center_displacement']);ynorm=F(d['preconditioner_infinity_norm'])
    rho=F(d['target_perturbation_radius']);eta=F(d['full_image_radius_bound'])
    need(radius==F(1,10**16) and rho==F(1,10**22),'fixed radii')
    need(0<=beta<F(1,4) and 0<=displacement and ynorm>0,'contraction conditions')
    need(eta==displacement+ynorm*rho+beta*radius and eta<radius/2,'invariant interior')

def reconstruct():
    root=Path(__file__).resolve().parent;data=strict_json(root/'parameters.json')
    center=[F(v) for v in data['center']]
    Y=[[F(v) for v in row] for row in data['preconditioner']]
    need(len(center)==4 and len(Y)==4 and all(len(row)==4 for row in Y),'dimensions')
    inverse_rational(Y)
    radius=F(data['parameter_radius']);rho=F(data['target_perturbation_radius'])
    need(radius==F(1,10**16) and rho==F(1,10**22),'fixed radii')
    box=[I.bounds(x-radius,x+radius) for x in center]
    need(box[0].lo>S and box[1].lo>S and box[2].lo>0 and box[3].lo>0,'strict ferromagnetic guards')
    raw,mu,std,errors=theta_moments();target=[std[k] for k in [4,6,8,10]]
    value,_,_,_=graph_values(center)
    residual=[x-y for x,y in zip(value,target)]
    displacement=matmul(Y,[[x] for x in residual])
    _,J,var,_=graph_values(box);product=matmul(Y,J)
    beta=max(sum((abs_upper(I.point(int(i==j))-product[i][j]) for j in range(4)),F(0)) for i in range(4))
    delta=max(abs_upper(row[0]) for row in displacement)
    ynorm=max(sum(abs(x) for x in row) for row in Y)
    eta=delta+ynorm*rho+beta*radius
    need(beta<F(1,4),'contraction bound')
    need(eta<radius/2,'strict invariant interior with target perturbation')
    out={
      'schema':1,'status':'PROPOSED_TEN_MOMENT_REALIZATION_NOT_RH',
      'rh_proved':False,'all_order_theta_realization_proved':False,
      'source':{'bits':BITS,'theta_terms':8,'cells':128,'taylor_derivative_order':24,'interval':['0','2'],
                'raw_moments':{str(k):v.decimal(38) for k,v in raw.items()},
                'standardized_moments':{str(k):v.decimal(30) for k,v in std.items()},'error_budgets':errors},
      'graph':{'spins':73,'positive_edges':2564,'core':8,'halo':64,'hub':1,
               'magnetization_states':1170,'independent_bath_spins':0,
               'cross_ratio':'101/100','hub_ratio':'1001/1000',
               'parameter_box':[x.decimal(22) for x in box],
               'unnormalized_variance':var.decimal(18),
               'matched_even_moments':[2,4,6,8,10]},
      'contraction':{'row_bound':str(beta),'center_displacement':str(delta),
                     'preconditioner_infinity_norm':str(ynorm),'parameter_radius':str(radius),
                     'target_perturbation_radius':str(rho),'full_image_radius_bound':str(eta),
                     'row_bound_decimal':I.point(beta).decimal(16),
                     'image_fraction_decimal':I.point(eta/radius).decimal(16)},
      'finite_existence':'unique parameters in the stated box for the exact theta moments and every listed-coordinate perturbation of infinity norm at most 1e-22',
      'analytic_theorems_machine_proved':False,'actual_zeros_computed':0}
    validate_certificate(out)
    return out


FILES={'PROOF.md','README.md','REVIEW.md','SOURCES.json','VALIDATION.md',
       'certify.py','parameters.json','certificate.json','test_certify.py','SHA256SUMS'}

def authenticate():
    root=Path(__file__).resolve().parent
    need({p.name for p in root.iterdir()}==FILES,'exact packet inventory')
    need(all((root/n).is_file() and not (root/n).is_symlink() for n in FILES),
         'regular files only')
    records={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        h,n=line.split('  ',1)
        need(n in FILES-{'SHA256SUMS'} and n not in records,'manifest path')
        need(len(h)==64 and all(ch in '0123456789abcdef' for ch in h),'hash syntax')
        records[n]=h
    need(set(records)==FILES-{'SHA256SUMS'},'complete manifest')
    for n,h in records.items():
        need(hashlib.sha256((root/n).read_bytes()).hexdigest()==h,'hash mismatch: '+n)
    source=strict_json(root/'SOURCES.json')
    need(source['parent_commit']=='bc561659684f50a6374bcd8d4afb0caf9fb65027','parent source')
    need(source['rh_proved'] is False and source['all_order_theta_realization_proved'] is False,
         'source status')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--emit',action='store_true');g.add_argument('--check',type=Path)
    args=ap.parse_args()
    if args.check:
        authenticate()
        validate_certificate(strict_json(args.check))
    expected=reconstruct()
    if args.check:
        got=strict_json(args.check);validate_certificate(got)
        need(json.dumps(got,sort_keys=True,separators=(',',':'))==
             json.dumps(expected,sort_keys=True,separators=(',',':')),'result differs')
    print(json.dumps(expected,indent=2,sort_keys=True))

if __name__=='__main__':
    try:
        main()
    except (ValueError,KeyError,TypeError,OSError) as e:
        import sys
        print('REJECT: '+str(e),file=sys.stderr);sys.exit(1)
