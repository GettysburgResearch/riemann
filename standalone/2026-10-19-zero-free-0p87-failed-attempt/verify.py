#!/usr/bin/env python3
"""Exact arithmetic audit of a FAILED 87/100 zero-free comparison.

This certifies substitutions in a declared sufficient-estimate model.
It does not compute zeta zeros, prove any new zero-free region, or certify
an imported analytic theorem. No numerical optimization is used.
"""
from fractions import Fraction as F
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


def text(q: F) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def row_envelope(delta: F, x: F, kappa: F) -> dict:
    alpha = F(5, 6)
    c = F(2, 3) / kappa
    D = 3 - (1 + c) * x
    P = (2 - c * x) * (1 - x)
    J = (alpha - delta) * D + delta * P
    t = 1 + delta * P / (2 * J)
    r = ((2 - c * x) * t - x * (1 - c / 2)) / D
    m = t - r
    zm, zs = (1 - r) / 2, (1 - 2 * m) / (6 * kappa)
    R = 1 - delta + (alpha - delta) * delta * P / (2 * J)
    require(F(1) <= t <= F(3, 2), "detector range")
    require(t-F(1, 2) <= r <= 1 and 0 <= m <= F(1, 2), "witness ranges")
    require(r + 2*zm == 1 and 2*r + 8*zm < 3, "inverse capacities")
    require(2*m + 6*kappa*zs == 1, "plain capacity")
    require(1-delta*r-2*x*delta*zm == R, "inverse witness count")
    require(1-2*delta*m-2*x*delta*zs == R, "plain witness count")
    require(1-alpha+(alpha-delta)*t == R, "long witness count")
    return dict(kappa=kappa, R=R, t=t, r=r, m=m, zM=zm, zS=zs)


def raw_error(B: F, ell: F, b: F, delta: F, x: F, R: F) -> F:
    """E0(h)-B, not the error normalized to B(ell) at a different ell."""
    a = (1+delta)/2
    ly = (1+b-ell)/2
    h = (1+b+3*ell)/2
    return a-a*ly-ell/2+x*delta*ell+h*(R+delta/2-F(1,6))-B


def main() -> None:
    B, delta, x = F(87,100), F(7,18), F(1,2)
    ell = 4*(F(11,12)-B)
    require(ell == F(14,75), "minimum prime length")
    cases = []
    for kappa in (F(3,4), F(37,50)):
        row = row_envelope(delta, x, kappa)
        R = row["R"]
        e0 = raw_error(B, ell, F(0), delta, x, R)
        eb = F(1,6) - (1-R)/2
        ee = -F(1,2)+F(3,2)*(delta+R)
        emin = raw_error(B, ell, 1-ell, delta, x, R)
        require(emin == e0+eb*(1-ell), "endpoint affine identity")
        require(eb < 0 and ee-eb > 0, "full triangle minimum")
        # For ell'=ell+v and 0<=b'<=1-ell', the error equals
        # emin + (ee-eb)*v + (-eb)*(1-ell'-b'). Both increments >=0.
        require(emin > F(1,40), "strict positive power obstruction")
        require(raw_error(B, ell+F(1,200), F(1,8),delta,x,R)
                == e0+ee*F(1,200)+eb*F(1,8), "raw exponent slope")
        h=(1+F(1,8)+3*ell)/2
        e=raw_error(B,ell,F(1,8),delta,x,R)
        required_R=R-e/h
        require(required_R == F(214,337), "count needed at b=1/8")
        row.update(error_at_b_zero=e0, error_b_slope=eb,
                   error_ell_slope=ee, minimum_error=emin,
                   error_at_b_one_eighth=e, required_count_at_b_one_eighth=required_R,
                   missing_count_saving_at_b_one_eighth=R-required_R)
        cases.append({k:text(v) for k,v in row.items()})
    require(cases[0]["R"] == "2363/3546", "old-count identity")
    require(cases[0]["minimum_error"] == "7003/265950", "old-error identity")
    require(cases[1]["R"] == "2075/3114", "optimistic-count identity")
    require(cases[1]["minimum_error"] == "6139/233550", "optimistic-error identity")

    # A separate diagnostic of the raw sextic large-sieve weighted kernel.
    # On [0,1/2], [1/2,1], [1,2], [2,infinity), k(v) has slopes 0,1/3,5/6,1.
    points=(F(0),F(1,2),F(1),F(2))
    def K(v): return max(F(1),v,F(5,6)+v/3,F(1,3)+5*v/6)
    vals=[K(v)-delta*v for v in points]
    slopes=[-delta,F(1,3)-delta,F(5,6)-delta,1-delta]
    require(slopes[0] < 0 and slopes[1] < 0 and slopes[2] > 0 and slopes[3] > 0,
            "piecewise envelope slopes")
    require(min(vals) == F(7,9) and vals[2] == F(7,9), "raw kernel minimum")

    # Reproduce, not discover, the reported Liu-v2 benchmark from its cubic.
    def p(q): return 1188*q**3-2160*q*q+171*q+190
    lo,hi=F(38858,100000),F(38859,100000)
    require(p(lo)>0 and p(hi)<0, "reported root bracket")
    # p' <0 on this interval follows from 3564*(.389)^2-4320*(.388)+171<0.
    require(3564*F(389,1000)**2-4320*F(388,1000)+171<0, "root uniqueness")
    for _ in range(90):
        mid=(lo+hi)/2
        if p(mid)>0: lo=mid
        else: hi=mid
    blo,bhi=(18*lo+7)/(18*lo+9),(18*hi+7)/(18*hi+9)
    require(blo > F(874957019420098945,10**18)
            and bhi < F(874957019420098947,10**18), "reported benchmark enclosure")
    report={
      "status":"FAILED_NEW_REGION_ATTEMPT",
      "candidate_boundary":text(B),
      "new_zero_free_region_proved":False,
      "rh_proved":False,
      "scope":"Exact sufficient-estimate arithmetic, not an arithmetic lower bound or analytic certification",
      "row_zero_real_part":text((1+delta)/2),
      "delta":text(delta),"prime_amplitude_ratio":text(x),
      "minimum_prime_length":text(ell),"cases":cases,
      "raw_sieve_diagnostic":{
        "minimum":text(min(vals)),"at_v":"1",
        "warning":"A diagnostic of this raw kernel only; it does not rule out signed improvements or other estimates"
      },
      "reported_external_benchmark_interval":[text(blo),text(bhi)],
      "remote_publication":"No new remote commit or PR created in this pass"
    }
    print(json.dumps(report,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
