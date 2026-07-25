#!/usr/bin/env python3
"""Exact fixed-vector checker for a full complex xi Pick grid.

Consumes the primitive Arb feature-table certificate from X-3902 and an X-6602
result containing one Gaussian-dyadic vector. Reconstructs the full shifted
Pick Rayleigh interval using only integers, Fraction, JSON, base64 and SHA-256.
"""
from __future__ import annotations
import argparse, base64, hashlib, json, struct, sys
if hasattr(sys, "set_int_max_str_digits"): sys.set_int_max_str_digits(1000000)
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.xi-full-pick-audit.v1"
class CertificateError(ValueError): pass

def exact_int(x: Any, name: str) -> int:
    if isinstance(x, bool) or not isinstance(x, int):
        raise CertificateError(f"{name} must be an integer")
    return x

def canonical_sha(value: Any) -> str:
    raw=json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
    return hashlib.sha256(raw).hexdigest()

def arb_endpoint(raw: Any, name: str) -> Fraction:
    if not isinstance(raw,dict): raise CertificateError(f"{name} must be an object")
    m=int(raw["mantissa"]);e=int(raw["exponent"])
    return Fraction(m<<e,1) if e>=0 else Fraction(m,1<<(-e))

def intersect_component(point: dict[str,Any], component: str) -> tuple[Fraction,Fraction]:
    pairs=[]
    for assembly in ("f_via_xi","f_via_parts"):
        raw=point[assembly][component]
        pairs.append((arb_endpoint(raw["lower"],f"{assembly}.{component}.lower"),
                      arb_endpoint(raw["upper"],f"{assembly}.{component}.upper")))
    lo=max(a for a,b in pairs);hi=min(b for a,b in pairs)
    if lo>hi: raise CertificateError(f"the two {component} assemblies do not overlap")
    return lo,hi

def rat(raw: Any,name: str) -> Fraction:
    if not isinstance(raw,dict): raise CertificateError(f"{name} must be an object")
    n=int(raw["numerator"]);d=int(raw["denominator"])
    if d<=0: raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n,d)

def load(path: Path) -> dict[str,Any]:
    value=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value,dict): raise CertificateError(f"{path} must contain an object")
    return value

def decode_vector(raw: Any, point_count: int) -> tuple[int,list[int],list[int]]:
    if not isinstance(raw,dict): raise CertificateError("vector missing")
    bits=exact_int(raw.get("scale_bits"),"scale_bits")
    if raw.get("encoding")!="int64-le-base64": raise CertificateError("unsupported vector encoding")
    length=exact_int(raw.get("length"),"length")
    if length!=point_count: raise CertificateError("vector dimension mismatch")
    try:
        rb=base64.b64decode(raw["real_numerators_base64"],validate=True)
        ib=base64.b64decode(raw["imag_numerators_base64"],validate=True)
    except Exception as exc:
        raise CertificateError(f"invalid vector base64: {exc}") from exc
    if len(rb)!=8*length or len(ib)!=8*length: raise CertificateError("vector byte length mismatch")
    real=list(struct.unpack("<"+"q"*length,rb));imag=list(struct.unpack("<"+"q"*length,ib))
    return bits,real,imag

def interval_digest(lo: Fraction,hi: Fraction) -> str:
    value={"lower":{"numerator":str(lo.numerator),"denominator":str(lo.denominator)},
           "upper":{"numerator":str(hi.numerator),"denominator":str(hi.denominator)}}
    return canonical_sha(value)

def verify(primitive: dict[str,Any], result: dict[str,Any]) -> dict[str,Any]:
    if result.get("schema")!=SCHEMA: raise CertificateError("wrong result schema")
    points=primitive.get("points")
    if not isinstance(points,list) or not points: raise CertificateError("primitive points missing")
    target=result.get("exact_strongest_frozen_vector")
    if not isinstance(target,dict): raise CertificateError("exact vector target missing")
    bits,real,imag=decode_vector(target.get("vector"),len(points))
    canonical={"scale_bits":bits,"real_numerators":real,"imag_numerators":imag}
    digest=canonical_sha(canonical)
    if target.get("vector_sha256")!=digest: raise CertificateError("vector SHA mismatch")
    scale=1<<bits;vr=[Fraction(a,scale) for a in real];vi=[Fraction(a,scale) for a in imag]
    parsed=[]
    for index,p in enumerate(points):
        x=rat(p.get("x"),f"points[{index}].x");t=rat(p.get("t"),f"points[{index}].t")
        rlo,rhi=intersect_component(p,"real");ilo,ihi=intersect_component(p,"imag")
        parsed.append((x,t,rlo,rhi,ilo,ihi))
    qlo=Fraction(0);qhi=Fraction(0)
    for i,(xi,ti,rlo,rhi,ilo,ihi) in enumerate(parsed):
        hr=Fraction(0);him=Fraction(0)
        for j,(xj,tj,*_) in enumerate(parsed):
            u=xi+xj;w=ti-tj;den=u*u+w*w
            invr=u/den;invi=-w/den
            hr += vr[j]*invr-vi[j]*invi
            him += vr[j]*invi+vi[j]*invr
        cr=2*(vr[i]*hr+vi[i]*him);ci=2*(vr[i]*him-vi[i]*hr)
        if cr>=0:a,b=cr*rlo,cr*rhi
        else:a,b=cr*rhi,cr*rlo
        d=-ci
        if d>=0:c,e=d*ilo,d*ihi
        else:c,e=d*ihi,d*ilo
        qlo+=a+c;qhi+=b+e
    if target.get("rayleigh_interval_sha256")!=interval_digest(qlo,qhi):
        raise CertificateError("rayleigh interval SHA mismatch")
    verdict="CERTIFIED_POSITIVE_FIXED_VECTOR" if qlo>0 else "CERTIFIED_NEGATIVE_FIXED_VECTOR" if qhi<0 else "UNRESOLVED"
    if target.get("verdict")!=verdict: raise CertificateError("claimed verdict mismatch")
    return {"verified":True,"point_count":len(points),"vector_sha256":digest,
            "rayleigh_interval_sha256":interval_digest(qlo,qhi),
            "lower_decimal":format(float(qlo),".17e"),"upper_decimal":format(float(qhi),".17e"),
            "verdict":verdict,
            "proof_boundary":"finite exact contraction of supplied primitive Arb rectangles only"}

def main() -> int:
    ap=argparse.ArgumentParser();ap.add_argument("primitive",type=Path);ap.add_argument("result",type=Path);args=ap.parse_args()
    try: out=verify(load(args.primitive),load(args.result))
    except (OSError,json.JSONDecodeError,CertificateError,ZeroDivisionError) as exc:
        print(json.dumps({"verified":False,"error":str(exc)},indent=2),file=sys.stderr);return 2
    print(json.dumps(out,indent=2,sort_keys=True));return 0 if out["verdict"]!="UNRESOLVED" else 1
if __name__=="__main__": raise SystemExit(main())
