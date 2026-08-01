#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x18505.real-d0001-direct-block.v1"
RESULT_SCHEMA = "riemann.x18505.real-d0001-direct-block.verification.v1"

class VerificationError(RuntimeError): pass

@dataclass(frozen=True)
class I:
    lo: Fraction
    hi: Fraction
    def __post_init__(self):
        if self.lo > self.hi: raise VerificationError("reversed interval")
    def __add__(self,o:I)->I: return I(self.lo+o.lo,self.hi+o.hi)
    def __sub__(self,o:I)->I: return I(self.lo-o.hi,self.hi-o.lo)
    def __neg__(self)->I: return I(-self.hi,-self.lo)
    def __mul__(self,o:I)->I:
        p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return I(min(p),max(p))
    def recip(self)->I:
        if self.lo <= 0 <= self.hi: raise VerificationError("division by interval containing zero")
        p=(1/self.lo,1/self.hi); return I(min(p),max(p))
    def __truediv__(self,o:I)->I: return self*o.recip()
    def square(self)->I:
        if self.lo >= 0: return I(self.lo*self.lo,self.hi*self.hi)
        if self.hi <= 0: return I(self.hi*self.hi,self.lo*self.lo)
        return I(Fraction(0),max(self.lo*self.lo,self.hi*self.hi))
    def contains(self,o:I)->bool: return self.lo <= o.lo and o.hi <= self.hi
    def overlaps(self,o:I)->bool: return max(self.lo,o.lo) <= min(self.hi,o.hi)

def frac_endpoint(x:Any)->Fraction:
    if not isinstance(x,dict) or set(x)!={"mantissa","exponent"}: raise VerificationError("bad endpoint schema")
    m=x["mantissa"]; e=x["exponent"]
    if isinstance(m,bool) or isinstance(e,bool): raise VerificationError("boolean endpoint")
    m=int(m); e=int(e)
    return Fraction(m)*(Fraction(2)**e)

def interval(x:Any)->I:
    if not isinstance(x,dict) or set(x)!={"lower","upper"}: raise VerificationError("bad interval schema")
    return I(frac_endpoint(x["lower"]),frac_endpoint(x["upper"]))

def rat(x:Any)->Fraction:
    if not isinstance(x,dict) or set(x)!={"numerator","denominator"}: raise VerificationError("bad rational schema")
    n=x["numerator"]; d=x["denominator"]
    if isinstance(n,bool) or isinstance(d,bool): raise VerificationError("boolean rational")
    n=int(n);d=int(d)
    if d<=0: raise VerificationError("nonpositive denominator")
    return Fraction(n,d)

def point(q:Fraction)->I: return I(q,q)

def matrix(x:Any,n:int)->list[list[I]]:
    if not isinstance(x,list) or len(x)!=n: raise VerificationError("matrix row count")
    out=[]
    for row in x:
        if not isinstance(row,list) or len(row)!=n: raise VerificationError("matrix column count")
        out.append([interval(v) for v in row])
    return out

def mat_add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A))] for i in range(len(A))]
def quad(A,v,w):
    s=point(Fraction(0))
    for i in range(len(v)):
        for j in range(len(w)):
            s=s+point(v[i])*A[i][j]*point(w[j])
    return s

def assert_contains(name:str,outer:I,inner:I):
    if not outer.contains(inner): raise VerificationError(f"{name} does not contain exact replay")

def canonical_digest(x:Any)->str:
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()

def fstr(q:Fraction)->str: return f"{q.numerator}/{q.denominator}"
def decimal(q:Fraction,digits:int=24)->str:
    sign='-' if q<0 else ''; q=abs(q); scale=10**digits; n=(q.numerator*scale)//q.denominator
    return f"{sign}{n//scale}.{n%scale:0{digits}d}"

def verify(doc:dict[str,Any])->dict[str,Any]:
    if doc.get("schema")!=SCHEMA: raise VerificationError("unexpected schema")
    sup=doc.get("support")
    if not isinstance(sup,dict) or sup.get("c")!=5 or sup.get("N")!=1 or sup.get("sector")!="even": raise VerificationError("wrong production support")
    dm=doc.get("declared_metric")
    if not isinstance(dm,dict): raise VerificationError("missing declared metric")
    qw=dm.get("Q_W"); qe=dm.get("Q_E")
    if not isinstance(qw,dict) or not isinstance(qe,dict): raise VerificationError("missing inclusion columns")
    w_raw=qw.get("integer_column"); r_raw=qe.get("integer_column")
    if not isinstance(w_raw,list) or not isinstance(r_raw,list) or len(w_raw)!=2 or len(r_raw)!=2: raise VerificationError("basis dimension")
    if any(isinstance(v,bool) for v in w_raw+r_raw): raise VerificationError("boolean basis")
    w=[int(v) for v in w_raw]; r=[int(v) for v in r_raw]
    if w != [-r[1],r[0]]: raise VerificationError("declared orthogonal rotation mismatch")
    if sum(w[i]*r[i] for i in range(2))!=0: raise VerificationError("basis not orthogonal")
    gw_exact=Fraction(sum(x*x for x in w)); ge_exact=Fraction(sum(x*x for x in r))
    GW=interval(dm["G_W"]); GE=interval(dm["G_E"]); M=interval(dm["M"])
    assert_contains("G_W",GW,point(gw_exact)); assert_contains("G_E",GE,point(ge_exact)); assert_contains("M",M,point(ge_exact))
    h=rat(dm["h"])

    pm=doc.get("primitive_matrices")
    if not isinstance(pm,dict): raise VerificationError("missing primitive matrices")
    P=matrix(pm["P_even"],2); E=matrix(pm["E_even"],2); Q=matrix(pm["Q_even"],2)
    for name,A in (("P",P),("E",E),("Q",Q)):
        if not A[0][1].overlaps(A[1][0]): raise VerificationError(f"{name} symmetry intervals disjoint")
    PE=mat_add(P,E)
    for i in range(2):
        for j in range(2): assert_contains(f"Q[{i},{j}]",Q[i][j],PE[i][j])

    c=doc.get("compressed")
    if not isinstance(c,dict): raise VerificationError("missing compressed objects")
    PW=quad(P,w,w); EW=quad(E,w,w); BW=PW+EW; Z=quad(Q,r,w); C=quad(Q,r,r)
    assert_contains("P_W",interval(c["P_W"]),PW)
    assert_contains("E_W",interval(c["E_W"]),EW)
    assert_contains("B_W",interval(c["B_W"]),BW)
    assert_contains("Z_W",interval(c["Z_W"]),Z)
    assert_contains("C",interval(c["C"]),C)
    X=interval(c["X_N"])
    if X.lo!=0 or X.hi!=0: raise VerificationError("pilot requires exact trial solve X_N=0")
    R=Z
    assert_contains("R_N",interval(c["R_N"]),R)
    coerc=C-point(h*ge_exact)
    if coerc.lo<=0: raise VerificationError("coercivity pivot is not strictly positive")
    assert_contains("coercivity pivot",interval(c["coercivity_pivot_C_minus_hM"]),coerc)
    penalty=R.square()/point(h*ge_exact)
    assert_contains("residual penalty",interval(c["residual_penalty"]),penalty)
    D=BW-penalty
    assert_contains("D_N",interval(c["D_N"]),D)
    m=rat(c["m"])
    pivot=D-point(m*gw_exact)
    if pivot.lo<=0: raise VerificationError("direct LDL pivot does not exclude zero")
    assert_contains("LDL pivot",interval(c["LDL_pivot_D_minus_mG"]),pivot)
    Dn=D/point(gw_exact); pn=pivot/point(gw_exact); Cn=C/point(ge_exact); Zn=Z/point(gw_exact)
    assert_contains("D normalized",interval(c["D_N_normalized"]),Dn)
    assert_contains("pivot normalized",interval(c["LDL_pivot_normalized"]),pn)
    assert_contains("C normalized",interval(c["C_normalized"]),Cn)
    assert_contains("Z normalized",interval(c["Z_normalized"]),Zn)
    exact_schur=BW/point(gw_exact)-Z.square()/(C*point(gw_exact))
    assert_contains("exact Schur normalized",interval(c["exact_schur_normalized"]),exact_schur)
    if doc.get("verdict")!="CERTIFIED_POSITIVE_REAL_D0001_DIRECT_BLOCK": raise VerificationError("false verdict field")
    delta=doc.get("delta_operator_norm_upper")
    if frac_endpoint(delta)!=0: raise VerificationError("delta must be exact zero after strict positive pivot")
    result={
      "schema":RESULT_SCHEMA,
      "input_certificate_sha256":hashlib.sha256((json.dumps(doc,sort_keys=True,indent=2)+"\n").encode()).hexdigest(),
      "support":{"c":5,"N":1,"sector":"even"},
      "basis_dimension_W":1,
      "basis_dimension_E":1,
      "h":fstr(h),"m":fstr(m),
      "coercivity_pivot_lower_exact":fstr(coerc.lo),
      "coercivity_pivot_lower_decimal":decimal(coerc.lo),
      "direct_ldl_pivot_lower_exact":fstr(pivot.lo),
      "direct_ldl_pivot_lower_normalized_exact":fstr(pn.lo),
      "direct_ldl_pivot_lower_normalized_decimal":decimal(pn.lo),
      "direct_floor_lower_normalized_exact":fstr(Dn.lo),
      "direct_floor_lower_normalized_decimal":decimal(Dn.lo),
      "exact_schur_lower_normalized_exact":fstr(exact_schur.lo),
      "exact_schur_lower_normalized_decimal":decimal(exact_schur.lo),
      "delta_operator_norm_upper_exact":"0",
      "verdict":"CERTIFIED_POSITIVE_REAL_D0001_DIRECT_BLOCK",
      "scope":"Actual cutoff-free D-0001 c=5,N=1 even finite block; not a complete augmented Suzuki low hierarchy."
    }
    result["verification_sha256"]=canonical_digest(result)
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument("certificate",type=Path);ap.add_argument("--output",type=Path,required=True);args=ap.parse_args()
    doc=json.loads(args.certificate.read_text())
    if not isinstance(doc,dict): raise VerificationError("root must be object")
    result=verify(doc);args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True));return 0
if __name__=="__main__": raise SystemExit(main())
