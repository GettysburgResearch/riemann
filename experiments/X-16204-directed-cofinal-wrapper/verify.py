#!/usr/bin/env python3
"""Exact checker for one directed cofinal CCM support block."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x16204-directed-cofinal-wrapper.v1"

class CertificateError(ValueError):
    pass

def integer(v: Any, name: str) -> int:
    if isinstance(v, bool) or not isinstance(v, int):
        raise CertificateError(f"{name} must be an integer")
    return v

def frac(v: Any, name: str) -> Fraction:
    if isinstance(v, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(v, int):
        return Fraction(v)
    if isinstance(v, str):
        try:
            return Fraction(v)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    if isinstance(v, list) and len(v) == 2:
        p=integer(v[0],name+"[0]"); q=integer(v[1],name+"[1]")
        if q == 0:
            raise CertificateError(f"{name} denominator is zero")
        return Fraction(p,q)
    raise CertificateError(f"{name} must be integer, fraction string, or [p,q]")

def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def digest(payload: dict[str, Any]) -> str:
    obj=dict(payload); obj.pop("proof_object_sha256",None)
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def check_hex(v: Any, name: str) -> str:
    if not isinstance(v,str) or len(v)!=64:
        raise CertificateError(f"{name} must be a SHA-256 hex digest")
    try: int(v,16)
    except ValueError as exc: raise CertificateError(f"{name} is not hexadecimal") from exc
    return v.lower()

class Iv:
    """Closed rational interval with exact natural arithmetic."""
    def __init__(self, lo: Fraction, hi: Fraction | None = None):
        self.lo=Fraction(lo); self.hi=Fraction(lo if hi is None else hi)
        if self.lo > self.hi: raise CertificateError("invalid interval")
    def __add__(self, other):
        other=other if isinstance(other,Iv) else Iv(Fraction(other))
        return Iv(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return Iv(-self.hi,-self.lo)
    def __sub__(self, other):
        return self + -(other if isinstance(other,Iv) else Iv(Fraction(other)))
    def __rsub__(self, other): return Iv(Fraction(other))-self
    def __mul__(self, other):
        other=other if isinstance(other,Iv) else Iv(Fraction(other))
        vals=(self.lo*other.lo,self.lo*other.hi,self.hi*other.lo,self.hi*other.hi)
        return Iv(min(vals),max(vals))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo <= 0 <= self.hi: raise CertificateError("interval division by zero")
        return Iv(1/self.hi,1/self.lo)
    def __truediv__(self, other):
        return self*(other if isinstance(other,Iv) else Iv(Fraction(other))).reciprocal()
    def __pow__(self, n: int):
        if n < 0: return (self**(-n)).reciprocal()
        out=Iv(Fraction(1)); base=self
        while n:
            if n&1: out=out*base
            base=base*base; n//=2
        return out

def phase_airy_grid_certificate() -> tuple[Fraction,Fraction]:
    """Prove 5 <= d_t^2 omega_sigma <= 18 on the Airy rectangle."""
    yl,yu=Fraction(105,64),Fraction(16,7)
    sl,su=Fraction(0),Fraction(1,8)
    worst_lo=None; worst_hi=None
    for i in range(64):
        a=yl+(yu-yl)*i/64; b=yl+(yu-yl)*(i+1)/64
        for j in range(32):
            c=sl+(su-sl)*j/32; d=sl+(su-sl)*(j+1)/32
            y=Iv(a,b); s=Iv(c,d)
            poly=(2*s**2*y+s**2-2*s*y**3+2*s*y**2-6*s*y
                  +y**4-2*y**3+4*y**2)
            den=(y-s)**2*(y-1)**2
            omega_sq=y*(y-s)/(y-1)
            ratio=poly/den
            if ratio.lo <= 0:
                raise CertificateError("Airy phase grid lost positivity")
            lo_sq=omega_sq.lo*ratio.lo**2
            hi_sq=omega_sq.hi*ratio.hi**2
            if lo_sq < 25 or hi_sq > 324:
                raise CertificateError("Airy phase grid failed [5,18] enclosure")
            worst_lo=lo_sq if worst_lo is None else min(worst_lo,lo_sq)
            worst_hi=hi_sq if worst_hi is None else max(worst_hi,hi_sq)
    assert worst_lo is not None and worst_hi is not None
    return worst_lo,worst_hi

def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload,dict) or payload.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")

    phase=payload.get("phase_partition")
    if not isinstance(phase,dict): raise CertificateError("phase_partition missing")
    sigma=frac(phase.get("sigma_sq_upper"),"sigma_sq_upper")
    wl=frac(phase.get("omega_left"),"omega_left")
    wr=frac(phase.get("omega_right"),"omega_right")
    alias_gap=frac(phase.get("higher_alias_gap"),"higher_alias_gap")
    sec=frac(phase.get("stationary_second_derivative_lower"),"stationary_second_derivative_lower")
    fold_lo=frac(phase.get("fold_third_lower"),"fold_third_lower")
    fold_hi=frac(phase.get("fold_third_upper"),"fold_third_upper")
    if not (0 <= sigma <= Fraction(1,8)): raise CertificateError("sigma^2 gate exceeds 1/8")
    if wl < Fraction(17,8) or wr > Fraction(9,4) or wl >= wr:
        raise CertificateError("stationary frequency window is outside the safe rational window")
    if alias_gap <= 0: raise CertificateError("alias gap must be positive")
    if 4*(4-sigma)/3 < (wr+alias_gap)**2:
        raise CertificateError("higher-alias derivative gap is not proved")
    ratio=Fraction(11,16)
    if wl*wl-4 < ratio*ratio:
        raise CertificateError("stationary discriminant ratio gate failed")
    if sec > Fraction(4,3)*ratio:
        raise CertificateError("stationary second-derivative lower bound overstated")
    if fold_lo > 8 or fold_hi < Fraction(60,7):
        raise CertificateError("fold cubic bounds are not outward")
    R=integer(phase.get("radial_scale_R"),"radial_scale_R")
    q=integer(phase.get("cube_root_q"),"cube_root_q")
    if q <= 0 or not (q**3 <= R < (q+1)**3):
        raise CertificateError("cube-root scale certificate failed")
    airy_t=frac(phase.get("airy_t_radius_upper"),"airy_t_radius_upper")
    airy_w=frac(phase.get("airy_frequency_radius_upper"),"airy_frequency_radius_upper")
    if airy_t < Fraction(1,q) or airy_w < Fraction(9,q*q):
        raise CertificateError("Airy transition radius understated")
    check_hex(phase.get("interval_phase_ledger_sha256"),"interval_phase_ledger_sha256")
    airy_sq_lo,airy_sq_hi=phase_airy_grid_certificate()
    if q < 16:
        raise CertificateError("Airy rational rectangle requires q>=16")

    radial=payload.get("radial_replay")
    if not isinstance(radial,dict): raise CertificateError("radial_replay missing")
    if radial.get("classification") != "DIRECTED_INTERVAL_ODE":
        raise CertificateError("radial replay is not directed interval ODE evidence")
    length=frac(radial.get("finite_interval_length"),"finite_interval_length")
    K=frac(radial.get("transition_bound"),"transition_bound")
    e0=frac(radial.get("initial_error_upper"),"initial_error_upper")
    res=frac(radial.get("residual_sup_upper"),"residual_sup_upper")
    tail2=frac(radial.get("tail_l2_sq_upper"),"tail_l2_sq_upper")
    dK=frac(radial.get("derivative_transition_bound"),"derivative_transition_bound")
    de0=frac(radial.get("derivative_initial_error_upper"),"derivative_initial_error_upper")
    dres=frac(radial.get("derivative_residual_sup_upper"),"derivative_residual_sup_upper")
    dtail2=frac(radial.get("derivative_tail_l2_sq_upper"),"derivative_tail_l2_sq_upper")
    if min(length,K,dK) <= 0 or min(e0,res,tail2,de0,dres,dtail2) < 0:
        raise CertificateError("radial replay contains invalid bounds")
    l2sq=length*K*K*(e0+length*res)**2+tail2
    dl2sq=length*dK*dK*(de0+length*dres)**2+dtail2
    claimed_l2=frac(radial.get("claimed_l2_sq_upper"),"claimed_l2_sq_upper")
    claimed_dl2=frac(radial.get("claimed_derivative_l2_sq_upper"),"claimed_derivative_l2_sq_upper")
    if claimed_l2 < l2sq or claimed_dl2 < dl2sq:
        raise CertificateError("radial replay claim understates the a-posteriori bound")
    check_hex(radial.get("producer_sha256"),"radial producer_sha256")
    check_hex(radial.get("primitive_sha256"),"radial primitive_sha256")

    endpoint=payload.get("poisson_endpoint")
    if not isinstance(endpoint,dict): raise CertificateError("poisson_endpoint missing")
    p=integer(endpoint.get("p"),"poisson p")
    if p != 4: raise CertificateError("this production schema fixes p=4")
    pi_lo=frac(endpoint.get("pi_lower"),"pi_lower")
    zeta4=frac(endpoint.get("zeta4_minus_one_upper"),"zeta4_minus_one_upper")
    if pi_lo > 3 or zeta4 < Fraction(9083,108045):
        raise CertificateError("outward pi/zeta constants are not safe")
    deriv=frac(endpoint.get("derivative_l1_upper"),"derivative_l1_upper")
    vmin=frac(endpoint.get("v_lower"),"v_lower")
    lam=frac(endpoint.get("lambda_lower"),"lambda_lower")
    cutoff=integer(endpoint.get("alias_cutoff_K"),"alias_cutoff_K")
    tail=frac(endpoint.get("post_cutoff_zeta_tail_upper"),"post_cutoff_zeta_tail_upper")
    if min(deriv,vmin,lam) <= 0 or cutoff < 2:
        raise CertificateError("invalid endpoint data")
    if tail < Fraction(1,3*cutoff**3):
        raise CertificateError("post-cutoff p-series tail understated")
    point=zeta4*deriv/(2*pi_lo*vmin)**4
    l2point=(zeta4*deriv)**2/((2*pi_lo)**8*7*lam**7)
    if frac(endpoint.get("claimed_point_upper"),"claimed_point_upper") < point:
        raise CertificateError("endpoint point bound understated")
    if frac(endpoint.get("claimed_l2_sq_upper"),"endpoint claimed_l2_sq_upper") < l2point:
        raise CertificateError("endpoint L2 bound understated")
    check_hex(endpoint.get("polylog_channel_sha256"),"polylog_channel_sha256")

    gram=payload.get("profile_gram")
    if not isinstance(gram,dict): raise CertificateError("profile_gram missing")
    gram_lo=frac(gram.get("lower"),"profile_gram.lower")
    gram_hi=frac(gram.get("upper"),"profile_gram.upper")
    if not (0 < gram_lo <= gram_hi):
        raise CertificateError("profile Gram bounds invalid")
    check_hex(gram.get("directed_gram_sha256"),"directed_gram_sha256")

    co=payload.get("cofinal_block")
    if not isinstance(co,dict): raise CertificateError("cofinal_block missing")
    measure=frac(co.get("measure_lower"),"measure_lower")
    exceptional=frac(co.get("exceptional_measure_upper"),"exceptional_measure_upper")
    families=co.get("mean_square_families")
    if measure <= 0 or exceptional < 0 or not isinstance(families,list) or not families:
        raise CertificateError("invalid cofinal block")
    bad=exceptional; thresholds=Fraction(0); family_out=[]
    for i,item in enumerate(families):
        if not isinstance(item,dict): raise CertificateError("mean-square family must be object")
        ms=frac(item.get("mean_square_upper"),f"family[{i}].mean_square_upper")
        th=frac(item.get("threshold"),f"family[{i}].threshold")
        if ms < 0 or th <= 0: raise CertificateError("invalid mean-square family")
        b=ms/(th*th); bad += b; thresholds += th
        family_out.append({"bad_measure_upper":fstr(b),"threshold":fstr(th)})
    if bad >= measure:
        raise CertificateError("cofinal good-set measure is not positive")
    check_hex(co.get("support_average_ledger_sha256"),"support_average_ledger_sha256")

    scal=payload.get("scalarization")
    if not isinstance(scal,dict): raise CertificateError("scalarization missing")
    logR=frac(scal.get("log_R_lower"),"log_R_lower")
    bounded=frac(scal.get("bounded_main_correction_upper"),"bounded_main_correction_upper")
    deterministic=frac(scal.get("deterministic_error_upper"),"deterministic_error_upper")
    if logR <= 0 or min(bounded,deterministic) < 0:
        raise CertificateError("invalid scalarization budget")
    total_abs=bounded+deterministic+thresholds
    eps=total_abs/(gram_lo*logR)
    claimed_eps=frac(scal.get("claimed_relative_epsilon_upper"),"claimed_relative_epsilon_upper")
    if claimed_eps < eps or claimed_eps >= 1:
        raise CertificateError("relative scalarization epsilon invalid")

    hier=payload.get("tail_hierarchy")
    if not isinstance(hier,dict): raise CertificateError("tail_hierarchy missing")
    a=frac(hier.get("a_lower"),"a_lower")
    d4=frac(hier.get("d4_upper"),"d4_upper")
    d8=frac(hier.get("d8_lower"),"d8_lower")
    C4=frac(hier.get("target_constant_upper"),"target_constant_upper")
    c8=frac(hier.get("gap_constant_lower"),"gap_constant_lower")
    if min(a,d4,d8,C4,c8) <= 0:
        raise CertificateError("tail hierarchy constants must be positive")
    muD=C4*d4
    target=(1+claimed_eps)*a*muD
    gap=a*((1-claimed_eps)*c8*d8-2*claimed_eps*muD)
    if gap <= 0:
        raise CertificateError("complete target-complement gap is not positive")
    ratio=target/gap
    claimed_ratio=frac(hier.get("claimed_ground_correction_ratio_upper"),"claimed_ground_correction_ratio_upper")
    if claimed_ratio < ratio:
        raise CertificateError("ground correction ratio understated")

    result={
      "schema":SCHEMA,
      "classification":"EXACT_COFINAL_CCM_WRAPPER_BLOCK",
      "phase_partition":{
        "safe_window":[fstr(wl),fstr(wr)],
        "higher_alias_gap":fstr(alias_gap),
        "stationary_second_derivative_lower":fstr(sec),
        "fold_third_interval":[fstr(fold_lo),fstr(fold_hi)],
        "airy_t_radius_upper":fstr(airy_t),
        "airy_frequency_radius_upper":fstr(airy_w),
        "airy_phase_second_derivative_squared_enclosure":[fstr(airy_sq_lo),fstr(airy_sq_hi)],
      },
      "radial_replay":{"l2_sq_upper":fstr(l2sq),"derivative_l2_sq_upper":fstr(dl2sq)},
      "poisson_endpoint":{"point_upper":fstr(point),"l2_sq_upper":fstr(l2point),"post_cutoff_tail_upper":fstr(tail)},
      "cofinal_block":{"bad_measure_upper":fstr(bad),"good_measure_lower":fstr(measure-bad),"families":family_out},
      "scalarization":{"total_absolute_error_upper":fstr(total_abs),"relative_epsilon_upper":fstr(eps)},
      "positive_route":{"target_rayleigh_upper":fstr(target),"complete_gap_lower":fstr(gap),"ground_correction_ratio_upper":fstr(ratio)},
      "proof_boundary":("The checker composes directed primitive bounds. It does not create the interval-ODE Dunster primitive or identify an explicit good support; the support certificate proves positive good-set measure in a dyadic block.")
    }
    result["proof_object_sha256"]=digest(result)
    claimed=payload.get("claimed_result_sha256")
    if claimed is not None and claimed != result["proof_object_sha256"]:
        raise CertificateError("claimed result digest mismatch")
    return result

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("certificate",type=Path); ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    try:
        obj=json.loads(a.certificate.read_text()); out=verify(obj); code=0
    except (OSError,json.JSONDecodeError,CertificateError) as exc:
        out={"schema":SCHEMA,"classification":"REJECTED","reason":str(exc)}; code=2
    text=json.dumps(out,indent=2,sort_keys=True)+"\n"
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(text)
    else: print(text,end="")
    return code
if __name__=="__main__": raise SystemExit(main())
