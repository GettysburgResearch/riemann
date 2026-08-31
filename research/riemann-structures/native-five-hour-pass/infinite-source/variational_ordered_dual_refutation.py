"""Directed root enclosure and exact witnesses refuting K=1,2,3 duals."""
from fractions import Fraction as F
from hashlib import sha256
import argparse
import importlib.util
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
BASE=HERE/'variational_certificate.py'
BASE_SHA='aa25f2aec339ca0502f1591d6219bfe9a0b883a7ec19528383ac9c2230db04db'
CENTER=tuple(map(F,('-0.08233305700654603','1.1226168381295267',
                    '-0.5082335933099136','0.5775184399712018','0.9383761444256082')))
RADIUS=F(1,100000000)
WITNESSES=((1,F(15,16),F(31,32),F(1,32)),
           (2,F(15,16),F(501,512),F(21,1024)),
           (3,F(15,16),F(503,512),F(5,256)))


def require(ok,why):
    if not ok:raise ValueError(why)


require(sha256(BASE.read_bytes()).hexdigest()==BASE_SHA,'pinned variational base before import')
spec=importlib.util.spec_from_file_location('pinned_variational_base',BASE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)


class Jet:
    def __init__(self,value,gradient):self.value=value;self.gradient=gradient
    def __add__(self,other):
        if not isinstance(other,Jet):other=Jet(other,[0]*len(self.gradient))
        return Jet(self.value+other.value,[a+b for a,b in zip(self.gradient,other.gradient)])
    __radd__=__add__
    def __neg__(self):return Jet(-self.value,[-x for x in self.gradient])
    def __sub__(self,other):return self+(-other)
    def __rsub__(self,other):return other+(-self)
    def __mul__(self,other):
        if not isinstance(other,Jet):other=Jet(other,[0]*len(self.gradient))
        return Jet(self.value*other.value,[a*other.value+self.value*b
                   for a,b in zip(self.gradient,other.gradient)])
    __rmul__=__mul__
    def reciprocal(self):
        return Jet(1/self.value,[-x/(self.value*self.value) for x in self.gradient])
    def __truediv__(self,other):
        if not isinstance(other,Jet):other=Jet(other,[0]*len(self.gradient))
        return self*other.reciprocal()
    def __rtruediv__(self,other):return Jet(other,[0]*len(self.gradient))/self
    def __pow__(self,power):
        require(type(power)is int and power>=0,'small integer Jet power')
        out=Jet(1,[0]*len(self.gradient))
        for _ in range(power):out=out*self
        return out


def profile(y):
    a,b,c,d,t=y;z=-a/b;f=a+b*t
    Av=1-t+f*f/(2*b)
    Bv=(1-t*t)/2+a*(t*t-z*z)/2+b*(t**3-z**3)/3
    Cv=1-t+f**3/(3*b)
    Aw=c*(1-t)+d*(1-t*t)/2
    Bw=c*(1-t*t)/2+d*(1-t**3)/3
    Cw=c*c*(1-t)+c*d*(1-t*t)+d*d*(1-t**3)/3
    return [1,Av,Bv,Cv/2,Aw,Bw,Cw/2]


def equations(y,small):
    x=profile(y);linear=[sum(row[j]*x[j] for j in range(7)) for row in small]
    a,b,c,d,t=y
    return [linear[3]*a+linear[1],linear[3]*b+linear[2],
            linear[6]*c+linear[4],linear[6]*d+linear[5],
            linear[3]*(1-a-b*t)**2-linear[6]*(c+d*t)**2]


def rational_inverse(matrix):
    n=len(matrix);aug=[row[:]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(matrix)]
    for p in range(n):
        pivot=next(i for i in range(p,n) if aug[i][p])
        aug[p],aug[pivot]=aug[pivot],aug[p]
        q=aug[p][p];aug[p]=[x/q for x in aug[p]]
        for i in range(n):
            if i!=p:
                q=aug[i][p];aug[i]=[x-q*y for x,y in zip(aug[i],aug[p])]
    return [row[n:] for row in aug]


def build():
    data=base.read_authenticated(base.GRAM_FILE,base.GRAM_SHA)
    sys.path.insert(0,str(Path.home()/'.cache/riemann-five-hour-deps'))
    from flint import arb,ctx
    ctx.prec=192
    G=[[base.from_pair(x,arb) for x in row] for row in data['gram21_intervals']]
    P=[[arb(0) for _ in range(7)] for _ in range(21)]
    for j in (0,10,12,13,14,18,20):P[j][0]=arb(1)
    P[1][1]=1;P[10][2]=-2;P[7][3]=2
    for j in (2,4,17):P[j][4]=1
    P[18][4]=-1
    for j in (13,14,20):P[j][5]=-2
    for j in (6,8,15):P[j][6]=2
    small=base.small_gram(G,P,arb)
    center=[base.arb_fraction(x,arb) for x in CENTER]
    box=[base.ball(x-RADIUS,x+RADIUS,arb) for x in CENTER]
    def jet(values):
        return [Jet(value,[arb(int(i==j)) for j in range(5)]) for i,value in enumerate(values)]
    ec=equations(jet(center),small);eb=equations(jet(box),small)
    Jc=[[sum(base.bounds(x)[0:2],F(0))/2 for x in row.gradient] for row in ec]
    pre=rational_inverse(Jc);prea=[[base.arb_fraction(x,arb) for x in row] for row in pre]
    J=[[x for x in row.gradient] for row in eb]
    residual=[x.value for x in ec]
    error=[[arb(int(i==j))-sum(prea[i][k]*J[k][j] for k in range(5))
            for j in range(5)] for i in range(5)]
    displacement=[]
    for interval,origin in zip(box,CENTER):
        lo,hi=base.bounds(interval);displacement.append(base.ball(lo-origin,hi-origin,arb))
    image=[center[i]-sum(prea[i][k]*residual[k] for k in range(5))
           +sum(error[i][j]*displacement[j] for j in range(5)) for i in range(5)]
    contraction=max(sum(base.bounds(abs(x))[1] for x in row) for row in error)
    require(contraction<1,'strict five-dimensional contraction')
    for old,new in zip(box,image):
        lo,hi=base.bounds(old);a,b=base.bounds(new);require(lo<a and b<hi,'strict Krawczyk image')
    a,b,c,d,t=box
    require(b>0 and d>0 and 0<-a/b<t<1 and 0<a+b*t<1 and 0<c+d*t<c+d<1,
            'strict declared ordered regimes')
    x=profile(box);mom=[sum(P[i][j]*x[j] for j in range(7)) for i in range(21)]
    theta=base.matvec(G,mom,arb)
    cv=theta[7];cw=theta[6]+theta[8]+theta[15]
    require(cv>0 and cw>0,'strict positive profile coefficients')
    records=[]
    for K,u0,v0,w0 in WITNESSES:
        u=base.arb_fraction(u0,arb);v=base.arb_fraction(v0,arb);w=base.arb_fraction(w0,arb)
        require(u<t,'registered witness before true switch')
        Lv=theta[1]-2*theta[10]*u
        p=theta[2]-2*u*theta[13]+(theta[4]-2*u*theta[20])*v \
          +(theta[17]-theta[18]-2*u*theta[14])*v*v+K*(1-v)
        q=theta[6]+theta[15]*v+theta[8]*v*v
        gap=cv*(v+Lv/(2*cv))**2+w*p+w*w*q
        require(gap<0,'strict registered dual refutation')
        records.append({'K':K,'u_v_w':list(map(str,(u0,v0,w0))),
                        'early_branch_gap_interval':base.encoded(gap)})
    return {'schema':'native-ordered-linear-dual-refutation/v1',
            'status':'CERTIFIED_REGISTERED_K1_K2_K3_DUALS_ALL_FAIL',
            'inputs':{base.GRAM_FILE:base.GRAM_SHA,'variational_base_sha256':BASE_SHA},
            'ordered_dual_theorem_sha256':sha256(
                (HERE/'variational_ORDERED_DUAL_THEOREM.md').read_bytes()).hexdigest(),
            'scientific_conclusion_note_sha256':sha256(
                (HERE/'ORDERED_DUAL_LINEAR_MENU_REFUTATION.md').read_bytes()).hexdigest(),
            'root_box':list(map(base.encoded,box)),'krawczyk_image':list(map(base.encoded,image)),
            'contraction_upper':str(contraction),'witnesses':records,
            'full_three_coordinate_optimizer_certified':False}


def main():
    parser=argparse.ArgumentParser();modes=parser.add_mutually_exclusive_group(required=True)
    modes.add_argument('--write',action='store_true');modes.add_argument('--check',action='store_true')
    args=parser.parse_args()
    result=build();result['producer_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    result['preregistration_sha256']=sha256(
        (HERE/'variational_ORDERED_DUAL_REFUTATION_PREREGISTRATION.md').read_bytes()).hexdigest()
    path=HERE/'variational_ordered_dual_refutation.verification.json'
    if args.write:path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf8')
    else:require(base.typed_equal(json.loads(path.read_text(encoding='utf8'),
                                             object_pairs_hook=base.unique_object),result),
                 'complete exact typed replay')
    print(json.dumps({'status':result['status'],'contraction_upper':result['contraction_upper'],
                      'witnesses':result['witnesses']},indent=2))


if __name__=='__main__':main()
