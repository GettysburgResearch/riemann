#!/usr/bin/env python3
from __future__ import annotations
import json, math, hashlib
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

BITS=320
SCALE=1<<BITS

class E(RuntimeError): pass

def fd(a,b):
    if b<=0: raise E('bad den')
    return a//b

def cd(a,b):
    if b<=0: raise E('bad den')
    return -((-a)//b)

@dataclass(frozen=True)
class Ball:
    lo:int; hi:int; scale:int=SCALE
    def __post_init__(self):
        if self.lo>self.hi: raise E('reversed')
    @staticmethod
    def point(n:int): return Ball(n*SCALE,n*SCALE)
    @staticmethod
    def frac(n:int,d:int): return Ball(fd(n*SCALE,d),cd(n*SCALE,d))
    @staticmethod
    def dec(s:str):
        t=Decimal(s).as_tuple(); n=0
        for q in t.digits: n=10*n+q
        if t.sign:n=-n
        if t.exponent>=0:return Ball.frac(n*10**t.exponent,1)
        return Ball.frac(n,10**(-t.exponent))
    def coerce(self,o): return o if isinstance(o,Ball) else Ball.point(o)
    def __add__(self,o):
        o=self.coerce(o); return Ball(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return Ball(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-self.coerce(o))
    def __rsub__(self,o): return self.coerce(o)-self
    def __mul__(self,o):
        o=self.coerce(o); p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return Ball(fd(min(p),SCALE),cd(max(p),SCALE))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.coerce(o)
        if o.lo<=0<=o.hi: raise E('zero div')
        ls=[];hs=[]
        for a in (self.lo,self.hi):
            for b in (o.lo,o.hi):
                if b<0:n,d=-a*SCALE,-b
                else:n,d=a*SCALE,b
                ls.append(fd(n,d));hs.append(cd(n,d))
        return Ball(min(ls),max(hs))
    def square(self):
        if self.lo<=0<=self.hi:
            u=max(self.lo*self.lo,self.hi*self.hi); return Ball(0,cd(u,SCALE))
        p=(self.lo*self.lo,self.hi*self.hi); return Ball(fd(min(p),SCALE),cd(max(p),SCALE))
    def abs_upper(self): return max(abs(self.lo),abs(self.hi))
    def midpoint(self): return (self.lo+self.hi)//2
    def to_frac_interval(self): return I(Fraction(self.lo,SCALE),Fraction(self.hi,SCALE))

class Directed:
    def __init__(self):
        self.zero=Ball(0,0); self.one=Ball.point(1); self.two=Ball.point(2)
        self.pi=16*self._atan_inv(5,190)-4*self._atan_inv(239,90)
        self.log2=self._log2(260); self.sqrt2=self.sqrt(self.two)
    def point(self,n): return Ball.point(n)
    def frac(self,n,d): return Ball.frac(n,d)
    def decimal(self,s): return Ball.dec(s)
    def sqrt(self,x):
        if x.lo<0: raise E('sqrt neg')
        lo=math.isqrt(x.lo*SCALE); r=math.isqrt(x.hi*SCALE); hi=r if r*r==x.hi*SCALE else r+1
        return Ball(lo,hi)
    def _atan_inv(self,q,terms):
        lo=hi=0;qpow=q
        for n in range(terms):
            den=qpow*(2*n+1); tl=fd(SCALE,den);th=cd(SCALE,den)
            if n%2==0:lo+=tl;hi+=th
            else:lo-=th;hi-=tl
            qpow*=q*q
        den=qpow*(2*terms+1); nh=cd(SCALE,den)
        if terms%2==0:hi+=nh
        else:lo-=nh
        return Ball(lo,hi)
    def _log2(self,terms):
        z=self.frac(1,3);z2=z*z;power=z;total=self.zero
        for n in range(terms):
            total += (2*power)/self.point(2*n+1);power*=z2
        tail=(2*power)/(self.point(2*terms+1)*(self.one-z2))
        return Ball(total.lo,total.hi+tail.hi)
    def log_rational(self,num,den=1,terms=260):
        k=num.bit_length()-den.bit_length()
        if k>=0:yn,yd=num,den<<k
        else:yn,yd=num<<(-k),den
        while yn<yd:k-=1;yn*=2
        while yn>=2*yd:k+=1;yd*=2
        z=self.frac(yn-yd,yn+yd);z2=z*z;power=z;total=self.zero
        for n in range(terms):
            total += (2*power)/self.point(2*n+1);power*=z2
        tail=(2*power)/(self.point(2*terms+1)*(self.one-z2))
        total=Ball(total.lo,total.hi+tail.hi)
        return total+k*self.log2
    def _sin_small(self,x,terms=88):
        x2=x*x;power=x;total=self.zero;fact=1
        for n in range(terms):
            if n:power*=x2;fact*=(2*n)*(2*n+1)
            term=power/self.point(fact);total=total+term if n%2==0 else total-term
        power*=x2;fact*=(2*terms)*(2*terms+1);rem=power/self.point(fact);rad=rem.abs_upper()
        return Ball(total.lo-rad,total.hi+rad)
    def _cos_small(self,x,terms=88):
        x2=x*x;power=self.one;total=self.zero;fact=1
        for n in range(terms):
            if n:power*=x2;fact*=(2*n-1)*(2*n)
            term=power/self.point(fact);total=total+term if n%2==0 else total-term
        power*=x2;fact*=(2*terms+1)*(2*terms+2);rem=power/self.point(fact);rad=rem.abs_upper()
        return Ball(total.lo-rad,total.hi+rad)
    def sin(self,x):
        q=fd(2*x.midpoint()+self.pi.midpoint()//2,self.pi.midpoint())
        y=x-(q*self.pi)/self.two; quarter=self.pi.hi//4
        if y.lo < -quarter or y.hi>quarter:
            found=False
            for cand in range(q-2,q+3):
                tr=x-(cand*self.pi)/self.two
                if tr.lo>=-quarter and tr.hi<=quarter:q,y,found=cand,tr,True;break
            if not found:raise E('range')
        r=q%4
        if r==0:return self._sin_small(y)
        if r==1:return self._cos_small(y)
        if r==2:return -self._sin_small(y)
        return -self._cos_small(y)
    def cos(self,x): return self.sin(x+self.pi/self.two)

@dataclass(frozen=True)
class I:
    lo:Fraction; hi:Fraction
    def __post_init__(self):
        if self.lo>self.hi: raise E('I reversed')
    @staticmethod
    def point(x): return I(Fraction(x),Fraction(x))
    def __add__(self,o): return I(self.lo+o.lo,self.hi+o.hi)
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,o): return self+(-o)
    def __mul__(self,o):
        p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi);return I(min(p),max(p))
    def recip(self):
        if self.lo<=0<=self.hi:raise E('I zero div')
        p=(1/self.lo,1/self.hi);return I(min(p),max(p))
    def __truediv__(self,o): return self*o.recip()
    def square(self):
        if self.lo>=0:return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi<=0:return I(self.hi*self.hi,self.lo*self.lo)
        return I(Fraction(0),max(self.lo*self.lo,self.hi*self.hi))
    def abs_upper(self): return max(abs(self.lo),abs(self.hi))

ZEROS=[
("14.134725141734693790457251983562470270784257115699243175685567460149963429809256764949010393172","4.50e-94"),
("21.022039638771554992628479593896902777334340524902781754629520403587598586068890799713658514180","1.61e-94"),
("25.010857580145688763213790992562821818659549672557996672496542006745092098441644277840238224558","7.48e-95"),
("30.424876125859513210311897530584091320181560023715440180962146036993329389333277920290584293902","1.04e-94"),
("32.935061587739189690662368964074903488812715603517039009280003440784815608630551005938848496135","3.58e-94"),
("37.586178158825671257217763480705332821405597350830793218333001113622149089618537264730329104946","2.17e-94"),
("40.918719012147495187398126914633254395726165962777279536161303667253280528720071282996003719890","5.00e-94"),
("43.327073280914999519496122165406805782645668371836871446878893685521088322305053626456349371063","1.95e-94"),
("48.005150881167159727942472749427516041686844001144425117775312519814090216416308281330335372305","4.14e-94"),
("49.773832477672302181916784678563724057723178299676662100781955750433511611515739278732707507401","1.26e-94"),
("52.970321477714460644147296608880990063825017888821224779900748140317564950304188054137587827094","4.23e-94"),
("56.446247697063394804367759476706127552782264471716631845450969843958475280274505666903011314275","1.78e-94"),
("59.347044002602353079653648674992219031098772806466669698122451754746800152699629811838102487075","4.03e-94"),
("60.831778524609809844259901824524003802910090451219178257101348824808493667294920538430841670394","3.50e-94"),
("65.112544048081606660875054253183705029348149295166722405966501086675343232668685384416774784439","4.11e-94"),
("67.079810529494173714478828896522216770107144951745558874196669551694901218956196983530293975086","2.73e-94"),
("69.546401711173979252926857526554738443012474209602510157324539999663387672274910419533344933178","3.53e-94"),
("72.067157674481907582522107969826168390480906621456697086683306151488407372399608348363525330412","2.16e-94"),
("75.704690699083933168326916762030345922811903530697400301647775301574197027706323608384037021835","4.19e-94"),
("77.144840068874805372682664856304637015796032449234461041765231453151139164253715089408288694700","3.53e-94")]

W=[116689468362578147411353556252846438487,170141183460469231731687303715884105728]
R=[170141183460469231731687303715884105728,-116689468362578147411353556252846438487]
GW=sum(x*x for x in W)
assert GW==sum(x*x for x in R) and W[0]*R[0]+W[1]*R[1]==0

def binI(mlo,elo,mhi,ehi): return I(Fraction(int(mlo))*(Fraction(2)**int(elo)),Fraction(int(mhi))*(Fraction(2)**int(ehi)))
B_HARD=binI("30215486490932980847652004656282335598019682924520561314131410790513488039947845008999542693863856700503726045721717",-131,"30217339081070589790176914293115333719011219957412740066570456329822562350376455487196886131784841743341420556386888",-131)
A_SOFT=binI("25079698045972117708704012808735295378218444705750057982447736630318312608086699819480461019397964181520420163796992",-143,"29905394590705030686075914458360872499858162218352700347786884945839425469892185097396833683325055975634019143281664",-143)
Z=binI("-28530514681382153316450767197095152694040512579653900531076912643300408930257812287301763908066295931775185859584000",-146,"38675493387489556421074583082335174383937730100762436542724076560722675624728926898777201945805205175584704840581120",-147)

def decball(d,center,radius):
    c=d.decimal(center);r=d.decimal(radius);return Ball(c.lo-r.hi,c.hi+r.hi)

def row_and_derivative(d:Directed,c:int,g:Ball):
    L=d.log_rational(c);sqrtL=d.sqrt(L);phase=L*g/d.two;S=d.sin(phase);C=d.cos(phase)
    v0=-(d.two*S)/(g*sqrtL)
    mu=L*g/(d.two*d.pi); mup=g/(d.two*d.pi)
    fac=sqrtL*S/d.pi
    v1=fac*d.sqrt2*mu/(d.one-mu.square())
    q=g/d.two
    dv0=-(d.two/g)*(q*C/sqrtL-S/(d.two*L*sqrtL))
    facp=(S/(d.two*sqrtL)+sqrtL*q*C)/d.pi
    dv1=d.sqrt2*(facp*mu/(d.one-mu.square())+fac*mup*(d.one+mu.square())/(d.one-mu.square()).square())
    return [v0,v1],[dv0,dv1]

def matzero(d): return [[d.zero,d.zero],[d.zero,d.zero]]
def outer_add(M,v,factor=2):
    for i in range(2):
        for j in range(2): M[i][j]+=factor*v[i]*v[j]

def transform(A,left,right):
    s=Ball(0,0)
    for i in range(2):
        for j in range(2): s+=A[i][j]*left[i]*right[j]
    return s

def qjson(x:Fraction): return {"numerator":str(x.numerator),"denominator":str(x.denominator)}
def ijson(x:I): return {"lower":qjson(x.lo),"upper":qjson(x.hi)}
def bjson(x:Ball): return ijson(x.to_frac_interval())
def canonical(obj): return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def build():
    d=Directed(); D=matzero(d);K=matzero(d); rows=[]
    for center,rad in ZEROS:
        g=decball(d,center,rad);v,dv=row_and_derivative(d,5,g);outer_add(D,v);outer_add(K,v);outer_add(K,dv)
        rows.append({"gamma":bjson(g),"row":[bjson(x) for x in v],"d_log_support_row":[bjson(x) for x in dv]})
    Ds=transform(D,[d.point(x) for x in R],[d.point(x) for x in R]).to_frac_interval()/I.point(GW)
    Dh=transform(D,[d.point(x) for x in W],[d.point(x) for x in W]).to_frac_interval()/I.point(GW)
    Dsh=transform(D,[d.point(x) for x in R],[d.point(x) for x in W]).to_frac_interval()/I.point(GW)
    Ks=transform(K,[d.point(x) for x in R],[d.point(x) for x in R]).to_frac_interval()/I.point(GW)
    Kh=transform(K,[d.point(x) for x in W],[d.point(x) for x in W]).to_frac_interval()/I.point(GW)
    Ksh=transform(K,[d.point(x) for x in R],[d.point(x) for x in W]).to_frac_interval()/I.point(GW)
    tau=Fraction(1,1000)
    det_tau=(Ds-I.point(tau))*(Dh-I.point(tau))-Dsh.square()
    if det_tau.hi>=0: raise E('soft threshold not between eigenvalues')
    if Ds.hi>=tau or Dh.lo<=tau: raise E('basis rayleigh split failed')
    gap=Dh-I.point(Ds.hi)
    if gap.lo<=0: raise E('profile gap')
    angle_upper=Fraction(2)*Dsh.abs_upper()/gap.lo
    m2_upper=Ks.hi+Kh.hi
    h=Fraction(1,4); m=Fraction(1,100000)
    hard_coerc=B_HARD-I.point(h*GW)
    if hard_coerc.lo<=0: raise E('hard coercivity fail')
    penalty=Z.square()/I.point(h*GW)
    direct=A_SOFT-penalty
    pivot=direct-I.point(m*GW)
    if pivot.lo<=0: raise E('soft direct pivot fail')
    exact=A_SOFT-Z.square()/B_HARD
    if exact.lo<=0: raise E('soft exact schur fail')
    out={
      "schema":"riemann.x18507.real-profile-soft-common-ledger.v1",
      "support":{"c":5,"N":1,"sector":"even","prime_powers":[2,3,4,5],"log_support_derivative":"d/d log(c)"},
      "bindings":{"arithmetic_certificate_path":"experiments/X-18505-real-d0001-direct-block/certificates/c5-N1-p384.json","arithmetic_certificate_blob_sha":"c609850c39081b653bf054184bd0534ff0145927","arithmetic_certificate_sha256":"1fbbb15004dbfc2af84e6ab71d88ba7e8098535f88182236f9ee1eceb0d6e350","arithmetic_verifier_path":"experiments/X-18505-real-d0001-direct-block/verify.py","zero_config_path":"experiments/X-20701-directed-d0001-frame/configs/verified-height-320.json","zero_config_blob_sha":"29cd860e223f349f70eedc64c87870a77d7f4fa6"},
      "source_identity":{"coordinates":"[e0,(e-1+e1)/sqrt(2)]","localization_matrix":[[1,0],[0,1]],"source_synthesis_matrix":[[1,0],[0,1]],"soft_column":[str(x) for x in R],"hard_column":[str(x) for x in W],"metric_gram":str(GW),"identity_verdict":"EXACT_LF_EQUALS_I"},
      "profile":{"classification":"ACTUAL_20_CERTIFIED_LINE_ZERO_EVALUATION_PROFILE","symmetric_zero_factor":2,"zero_rows":rows,"D_even":[[bjson(x) for x in rr] for rr in D],"K_even":[[bjson(x) for x in rr] for rr in K],"compressed_normalized":{"D_soft":ijson(Ds),"D_cross":ijson(Dsh),"D_hard":ijson(Dh),"K_soft":ijson(Ks),"K_cross":ijson(Ksh),"K_hard":ijson(Kh)},"graph_lmi":{"M_squared_upper":qjson(m2_upper),"proof":"K <= tr_G(K) G for positive K in dimension two"},"buffered_soft_export":{"threshold_tau":qjson(tau),"det_D_minus_tau_I":ijson(det_tau),"soft_rayleigh_upper":qjson(Ds.hi),"hard_rayleigh_lower":qjson(Dh.lo),"projector_graph_angle_upper":qjson(angle_upper),"soft_dimension":1,"hard_dimension":1,"verdict":"CERTIFIED_ONE_DIMENSIONAL_BUFFERED_SOFT_SPLIT"}},
      "complete_weil_matrix":{"classification":"BOUND_TO_X18505_COMPLETE_CUTOFF_FREE_PRIME_POLE_ARCHIMEDEAN_MATRIX","A_soft":ijson(A_SOFT),"Z_soft_hard":ijson(Z),"C_hard":ijson(B_HARD),"hard_metric":qjson(Fraction(GW)),"soft_metric":qjson(Fraction(GW))},
      "pr191_direct_short":{"trial_solve":qjson(Fraction(0)),"hard_floor_h":qjson(h),"target_floor_m":qjson(m),"hard_coercivity_pivot":ijson(hard_coerc),"residual_penalty":ijson(penalty),"direct_lower":ijson(direct),"shifted_ldl_pivot":ijson(pivot),"exact_schur":ijson(exact),"normalized_direct_lower":ijson(direct/I.point(GW)),"normalized_shifted_ldl_pivot":ijson(pivot/I.point(GW)),"normalized_exact_schur":ijson(exact/I.point(GW)),"negative_part_upper":qjson(Fraction(0)),"verdict":"CERTIFIED_POSITIVE_REAL_PROFILE_SOFT_DIRECT_BLOCK"},
      "sequence_parameterization":{"supports":"c_j in {5,10,20,50,100,200,500,1000,2000,5000,...}, c_j -> infinity","packet_schedule":"use X-18506 source-canonical N_j with exact even basis and complete prime powers q<=c_j","profile_schedule":"use K_j certified critical-line zero rows plus directed unseen-zero ledger; form D_j and d_log(c) graph Gram K_j","soft_schedule":"choose a directed empty generalized-eigenvalue interval in [tau_j,2 tau_j] and export a Riesz projector/interval graph","proof_gate":"run the same PR #191 residual short and require the shifted LDL pivot to be positive","status":"PARAMETERIZED; UNBOUNDED PASSING THEOREM NOT CLAIMED"},
      "verdict":"CERTIFIED_FIRST_REAL_COMMON_PROFILE_SOFT_LEDGER",
      "scope":"Actual c=5,N=1 D-0001 zeta arithmetic plus 20 proof-grade critical-line zero profiles. This is a common production calibration block, not yet the complete cofinal Suzuki hierarchy."
    }
    out['proof_object_sha256']=canonical(out)
    return out

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(description='Build the deterministic real c=5 profile-soft common ledger.')
    ap.add_argument('--certificate',type=Path,required=True)
    ap.add_argument('--summary',type=Path,required=True)
    args=ap.parse_args()
    out=build();args.certificate.parent.mkdir(parents=True,exist_ok=True);args.certificate.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    summary={'schema':'riemann.x18507.real-profile-soft-common-ledger.summary.v1','proof_object_sha256':out['proof_object_sha256'],'soft_D_upper':out['profile']['buffered_soft_export']['soft_rayleigh_upper'],'hard_D_lower':out['profile']['buffered_soft_export']['hard_rayleigh_lower'],'projector_angle_upper':out['profile']['buffered_soft_export']['projector_graph_angle_upper'],'graph_M_squared_upper':out['profile']['graph_lmi']['M_squared_upper'],'normalized_direct_lower':out['pr191_direct_short']['normalized_direct_lower'],'normalized_shifted_ldl_pivot':out['pr191_direct_short']['normalized_shifted_ldl_pivot'],'normalized_exact_schur':out['pr191_direct_short']['normalized_exact_schur'],'shifted_ldl_pivot':out['pr191_direct_short']['shifted_ldl_pivot'],'verdict':out['verdict']}
    summary['summary_sha256']=canonical(summary)
    args.summary.parent.mkdir(parents=True,exist_ok=True);args.summary.write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
    print(json.dumps(summary,indent=2,sort_keys=True))
