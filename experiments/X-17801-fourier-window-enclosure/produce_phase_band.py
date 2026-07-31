#!/usr/bin/env python3
"""Build the proof-grade first-100-zero phase band for the five-notch target."""
from __future__ import annotations
import argparse, json, re
from fractions import Fraction
from pathlib import Path
from typing import Any

DESIGN = tuple(Fraction(x) for x in (
    "14.13472514173469379045725198356247",
    "21.02203963877155499262847959389690",
    "25.01085758014568876321379099256282",
    "30.42487612585951321031189753058409",
    "32.93506158773918969066236896407490",
))
X = Fraction(8578244975439, 549755813888)


def rat(o: dict[str, Any]) -> Fraction:
    return Fraction(int(o["numerator"]), int(o["denominator"]))

def fj(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}

def ij(lo: Fraction, hi: Fraction) -> dict[str, dict[str, int]]:
    return {"lower": fj(lo), "upper": fj(hi)}

def exact_arb(q: Fraction, arb: Any) -> Any:
    return arb(q.numerator) / arb(q.denominator)

def ball_from_interval(lo: Fraction, hi: Fraction, arb: Any) -> Any:
    mid=(lo+hi)/2; rad=(hi-lo)/2
    return arb(exact_arb(mid,arb), exact_arb(rad,arb))

def arf_fraction(v: Any) -> Fraction:
    m,e=v.man_exp(); m=int(m); e=int(e)
    return Fraction(m << e,1) if e>=0 else Fraction(m,1 << (-e))

def arb_bounds(v: Any) -> tuple[Fraction,Fraction]:
    return arf_fraction(v.lower()), arf_fraction(v.upper())


def transform(z: Any, arb: Any, acb: Any, dyadic: int=160) -> Any:
    """Laplace transform of the exact five-notch pole-free window."""
    pi=arb.pi(); one=acb(1); product=acb(1)
    for gamma0 in DESIGN:
        r=2*pi/exact_arb(gamma0,arb)
        rz=r*z
        product *= (one-(-rz).exp())/rz
    for j in range(1,dyadic+1):
        r=arb(1)/(arb(2)**j)
        rz=r*z
        product *= (one-(-rz).exp())/rz
    # The omitted random tail is supported in [0,2^-dyadic].
    eps=arb(1)/(arb(2)**dyadic)
    zabs=z.abs().upper()
    delta=zabs*eps*(zabs*eps).exp()
    product.add_error(delta)
    h=arb(4).log()
    return (-arb(2)*z).exp() * product**2 * (one-arb(2)*(-h*z).exp())


def parse_prime(path: Path) -> tuple[Fraction,Fraction,int]:
    text=path.read_text()
    def grab(name: str) -> Fraction:
        m=re.search(rf"^{name}=([^\n]+)$",text,re.M)
        if not m: raise ValueError(f"missing {name}")
        return Fraction(m.group(1).strip())
    m=re.search(r"terms=(\d+)",text)
    if not m: raise ValueError("missing term count")
    return grab("prime_lower"),grab("prime_upper"),int(m.group(1))


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument("--chain-verification",type=Path,required=True)
    ap.add_argument("--prime-output",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--precision",type=int,default=384)
    ap.add_argument("--trivial-count",type=int,default=100)
    args=ap.parse_args()
    from flint import arb, acb, ctx
    ctx.prec=args.precision
    chain=json.loads(args.chain_verification.read_text())
    bins=chain["bins"]
    if len(bins)!=100 or not all(r["exact_zero_count"]==1 and r["simple"] is True for r in bins):
        raise ValueError("need exactly 100 certified simple zero bins")
    phase=arb(0)
    for row in bins:
        gamma=ball_from_interval(rat(row["lower"]),rat(row["upper"]),arb)
        z=acb(0,gamma)
        phase += -arb(2)*( (z*exact_arb(X,arb)).exp()*transform(z,arb,acb) ).real
    # Retain trivial zeros exactly in the same phase interval.
    xarb=exact_arb(X,arb)
    for j in range(1,args.trivial_count+1):
        lam=arb(2*j)+arb(1)/2
        phase += -( -lam*xarb ).exp()*transform(acb(-lam),arb,acb).real
    phase_lo,phase_hi=arb_bounds(phase)

    # Complete high-zero p=22 tail.
    p=22; pi=arb.pi(); prod_r=arb(1)
    for gamma0 in DESIGN:
        prod_r *= 2*pi/exact_arb(gamma0,arb)
    A=arb(3)*(arb(2)**64)/(prod_r**2)
    T=exact_arb(rat(bins[-1]["upper"]),arb)
    N=arb(100); a0=arb("0.10076"); b0=arb("0.24460"); c0=arb("8.08292")
    logT=T.log(); econst=arb(1).exp()
    Z= -N*T**(-p)
    Z += arb(p)/(2*pi)*T**(1-p)*( (T/(2*pi*econst)).log()/(p-1)+arb(1)/(p-1)**2 )
    Z += a0*T**(-p)*(logT+arb(1)/p)
    Z += b0*T**(-p)*(logT.log()+arb(1)/(p*logT))
    Z += c0*T**(-p)
    _,Ahi=arb_bounds(A); _,Zhi=arb_bounds(Z)

    # Trivial tail: ||G||_1 <= 3 and support upper B=2+2S+log4.
    S=arb(1)
    for gamma0 in DESIGN: S += 2*pi/exact_arb(gamma0,arb)
    B=arb(2)+2*S+arb(4).log(); d=xarb-B
    M=args.trivial_count
    triv_tail=arb(3)*(-(arb(2*M)+arb(5)/2)*d).exp()/(arb(1)-(-2*d).exp())
    _,triv_hi=arb_bounds(triv_tail)

    prime_lo,prime_hi,terms=parse_prime(args.prime_output)
    if terms!=64542: raise ValueError("prime term count")
    Tfrac=rat(bins[-1]["upper"])
    certificate={
      "schema":"riemann.x15605-phase-aware-prime-bound.v1",
      "classification":"RIEMANN_DIRECTED",
      "prime_interval":ij(prime_lo,prime_hi),
      "phase_interval":ij(phase_lo,phase_hi),
      "shells":[{
        "left":fj(Fraction(0)),"right":fj(Tfrac),
        "count_upper":fj(Fraction(100)),"selected_multiplicity":100,
        "transform_envelope_upper":fj(Fraction(0))
      }],
      "high_zero_tail":{
        "transform_constant_upper":fj(Ahi),
        "zero_moment_upper":fj(Zhi)
      },
      "trivial_tail_upper":fj(triv_hi),
      "additional_radius":fj(Fraction(0)),
      "source_bindings":{
        "zero_chain_certificate_sha256":chain.get("certificate_sha256"),
        "zero_count":100,"prime_power_terms":terms,"translation":fj(X),
        "precision_bits":args.precision,"trivial_terms_retained":M,"tail_power":p
      }
    }
    args.output.write_text(json.dumps(certificate,indent=2,sort_keys=True)+"\n")
    print(json.dumps({
      "phase_lower":str(phase_lo),"phase_upper":str(phase_hi),
      "transform_constant_upper":str(Ahi),"zero_moment_upper":str(Zhi),
      "trivial_tail_upper":str(triv_hi),"output":str(args.output)
    },indent=2))
    return 0

if __name__=="__main__": raise SystemExit(main())
