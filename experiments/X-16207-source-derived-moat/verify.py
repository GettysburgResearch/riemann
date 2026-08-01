#!/usr/bin/env python3
"""Fail-closed checker for source-derived CCM radial/derivative moat data.

Version 2 corrects a relative-normalization error in the original endpoint
ledger: the p=4 integration-by-parts remainder for a unit tail profile contains
||f^(4)||_1/sqrt(delta), where delta is the first-alias energy. An absolute
source Sobolev bound cannot be inserted without this divisor.
"""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any
SCHEMA="riemann.x16207-source-derived-moat.v2"
RESULT_SCHEMA="riemann.x16207-source-derived-moat-result.v2"
class CertificateError(ValueError): pass
def integer(v:Any,name:str)->int:
 if isinstance(v,bool) or not isinstance(v,int): raise CertificateError(f"{name} must be an integer")
 return v
def frac(v:Any,name:str)->Fraction:
 if isinstance(v,bool): raise CertificateError(f"{name} must not be Boolean")
 if isinstance(v,int): return Fraction(v)
 if isinstance(v,str):
  try: return Fraction(v)
  except (ValueError,ZeroDivisionError) as exc: raise CertificateError(f"{name} is not rational") from exc
 raise CertificateError(f"{name} must be an integer or rational string")
def fstr(x:Fraction)->str: return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def check_sha(v:Any,name:str)->str:
 if not isinstance(v,str) or len(v)!=64: raise CertificateError(f"{name} must be a SHA-256 digest")
 try: int(v,16)
 except ValueError as exc: raise CertificateError(f"{name} is not hexadecimal") from exc
 return v.lower()
def canonical_sha(obj:dict[str,Any])->str:
 x=dict(obj); x.pop("proof_object_sha256",None)
 return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def verify(payload:dict[str,Any])->dict[str,Any]:
 if not isinstance(payload,dict) or payload.get("schema")!=SCHEMA: raise CertificateError("schema mismatch")
 source=payload.get("source")
 if not isinstance(source,dict): raise CertificateError("source manifest missing")
 gamma=integer(source.get("gamma"),"source.gamma")
 if gamma<=0 or source.get("modes")!=[0,4,8,12]: raise CertificateError("unexpected source packet")
 for key in ("actual_primitive_sha256","full_exact_result_sha256","full_exact_proof_object_sha256","producer_sha256"):
  check_sha(source.get(key),f"source.{key}")
 columns=payload.get("repaired_columns")
 if not isinstance(columns,list) or len(columns)!=2: raise CertificateError("exactly two repaired columns are required")
 radial=Fraction(0); derivative=Fraction(0); horizontal=Fraction(0); abs_f4_sq=Fraction(0)
 for i,col in enumerate(columns):
  if not isinstance(col,dict): raise CertificateError(f"column[{i}] must be an object")
  r=frac(col.get("radial_l2_error_upper"),f"column[{i}].radial")
  d=frac(col.get("frequency_derivative_l2_error_upper"),f"column[{i}].derivative")
  h=frac(col.get("horizontal_strip_l2_error_upper"),f"column[{i}].horizontal")
  f4=frac(col.get("source_fourth_derivative_l1_upper_unscaled"),f"column[{i}].f4_unscaled")
  if min(r,d,h,f4)<0: raise CertificateError("source bounds must be nonnegative")
  radial+=r; derivative+=d; horizontal+=h; abs_f4_sq+=f4*f4
 repl=payload.get("source_derived_replacements")
 if not isinstance(repl,dict): raise CertificateError("source_derived_replacements missing")
 tail_sq=frac(repl.get("tail_l2_sq_upper"),"tail_l2_sq_upper")
 derivative_sq=frac(repl.get("derivative_tail_l2_sq_upper"),"derivative_tail_l2_sq_upper")
 horizontal_sq=frac(repl.get("horizontal_tail_l2_sq_upper"),"horizontal_tail_l2_sq_upper")
 if tail_sq<radial*radial: raise CertificateError("global radial tail is understated")
 if derivative_sq<derivative*derivative: raise CertificateError("global derivative tail is understated")
 if horizontal_sq<horizontal*horizontal: raise CertificateError("global horizontal tail is understated")
 endpoint=payload.get("endpoint_relative_ledger")
 if not isinstance(endpoint,dict): raise CertificateError("endpoint_relative_ledger missing")
 norm_f4_raw=endpoint.get("normalized_fourth_derivative_l1_upper")
 if norm_f4_raw is None:
  endpoint_closed=False; endpoint_data=None
 else:
  norm_f4=frac(norm_f4_raw,"normalized_fourth_derivative_l1_upper")
  point=frac(endpoint.get("poisson_endpoint_point_upper"),"poisson_endpoint_point_upper")
  l2sq=frac(endpoint.get("poisson_endpoint_l2_sq_upper"),"poisson_endpoint_l2_sq_upper")
  l2norm=frac(endpoint.get("poisson_endpoint_l2_norm_upper"),"poisson_endpoint_l2_norm_upper")
  if min(norm_f4,point,l2sq,l2norm)<0 or l2norm*l2norm<l2sq: raise CertificateError("normalized endpoint ledger invalid")
  endpoint_closed=True; endpoint_data={"normalized_f4_upper":fstr(norm_f4),"point_upper":fstr(point),"l2_sq_upper":fstr(l2sq),"l2_norm_upper":fstr(l2norm)}
 first=payload.get("first_alias_profile_gram")
 if not isinstance(first,dict): raise CertificateError("first_alias_profile_gram missing")
 corr=frac(first.get("normalized_cross_abs_upper"),"normalized_cross_abs_upper")
 first_lo=frac(first.get("lower"),"first_alias.lower"); first_hi=frac(first.get("upper"),"first_alias.upper")
 if corr<0 or first_lo>1-corr or first_hi<1+corr: raise CertificateError("first-alias Gram bounds are not outward")
 complete=payload.get("complete_arithmetic_alias")
 if not isinstance(complete,dict): raise CertificateError("complete arithmetic alias block missing")
 cross_raw=complete.get("cross_error_upper"); full_up_raw=complete.get("full_upper")
 alias_closed=False; complete_lo=None; complete_hi=None
 if cross_raw is not None or full_up_raw is not None:
  if cross_raw is None or full_up_raw is None: raise CertificateError("complete alias lower and upper fields must be supplied together")
  cross=frac(cross_raw,"complete_alias.cross_error_upper"); complete_hi=frac(full_up_raw,"complete_alias.full_upper")
  complete_lo=first_lo-cross
  if cross<0 or complete_lo<=0 or complete_hi<first_hi: raise CertificateError("complete arithmetic profile-Gram moat invalid")
  alias_closed=True
 if radial>Fraction(1,gamma*gamma): raise CertificateError("radial diagonal target gamma^-2 failed")
 if derivative>Fraction(1,gamma): raise CertificateError("frequency diagonal target gamma^-1 failed")
 if not endpoint_closed: classification="RADIAL_DERIVATIVE_CLOSED_NORMALIZED_ENDPOINT_OPEN"
 elif not alias_closed: classification="SOURCE_FIELDS_CLOSED_COMPLETE_ALIAS_GRAM_OPEN"
 else: classification="PRODUCTION_PROFILE_GRAM_CLOSED"
 result={
  "schema":RESULT_SCHEMA,"classification":classification,"gamma":gamma,
  "source_bindings":{k:source[k] for k in source if k.endswith("sha256")},
  "source_derived":{"radial_l2_sum_upper":fstr(radial),"frequency_derivative_l2_sum_upper":fstr(derivative),"horizontal_l2_sum_upper":fstr(horizontal),"tail_l2_sq_upper":fstr(tail_sq),"derivative_tail_l2_sq_upper":fstr(derivative_sq),"horizontal_tail_l2_sq_upper":fstr(horizontal_sq),"absolute_source_f4_packet_upper":"not-used-relatively"},
  "endpoint_relative":endpoint_data,
  "profile_gram":{"first_alias_lower":fstr(first_lo),"first_alias_upper":fstr(first_hi),"complete_lower":None if complete_lo is None else fstr(complete_lo),"complete_upper":None if complete_hi is None else fstr(complete_hi)},
  "cofinal_decay":{"radial_gate":"sum eps_rad <= gamma^-2","derivative_gate":"sum eps_drad <= gamma^-1","endpoint_gate":"requires normalized radial endpoint/ODE asymptotic, not absolute source H4","complete_alias_gate":"cross_error_upper must tend to zero before promotion"},
  "proof_boundary":"The coefficient-tail radial and derivative placeholders are source-derived. The earlier absolute H4 endpoint substitution was not relative to the first-alias energy and is rejected. Promotion requires a normalized radial endpoint remainder and the complete Poisson cross-alias Gram."
 }
 result["proof_object_sha256"]=canonical_sha(result); return result
def main()->int:
 ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("certificate",type=Path); ap.add_argument("--output",type=Path); args=ap.parse_args()
 try: out=verify(json.loads(args.certificate.read_text())); code=0
 except (OSError,json.JSONDecodeError,CertificateError) as exc: out={"schema":RESULT_SCHEMA,"classification":"REJECTED","reason":str(exc)}; code=2
 text=json.dumps(out,indent=2,sort_keys=True)+"\n"
 if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(text)
 else: print(text,end="")
 return code
if __name__=="__main__": raise SystemExit(main())
