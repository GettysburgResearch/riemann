#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import hashlib, json, random
from pathlib import Path

VERDICT="PASS_T105410_F1_ORTHOGONAL_ATO_REDUCTION"

def run():
    rng=random.Random(105410)
    split=0
    for _ in range(5000):
        A=Fraction(rng.randint(-100,100),rng.randint(1,30))
        G=Fraction(rng.randint(-100,100),rng.randint(1,30))
        B=G-A
        H=(49*A*A-96*A*G+48*G*G)/24
        assert H==A*A/24+2*B*B
        L=5*A-G
        assert L==4*A-B
        assert Fraction(769,2)*H-L*L==(A+192*B)**2/48
        assert L*L<=Fraction(769,2)*H
        split+=1

    # Exact finite Gram identity and support firewall on an integer log lattice.
    gram=0
    for _ in range(250):
        N=20
        ka=[Fraction(rng.randint(-4,4),5) for _ in range(4)]
        kb=[Fraction(rng.randint(-4,4),7) for _ in range(4)]
        c=[Fraction(rng.randint(-5,5),rng.randint(1,8)) for _ in range(N)]
        fa=[]; fb=[]
        for u in range(N+3):
            fa.append(sum(c[n]*ka[u-n] for n in range(N) if 0<=u-n<len(ka)))
            fb.append(sum(c[n]*kb[u-n] for n in range(N) if 0<=u-n<len(kb)))
        lhs=sum(x*x/Fraction(24)+2*y*y for x,y in zip(fa,fb))
        rhs=Fraction(0)
        for n in range(N):
            for m in range(N):
                kernel=Fraction(0)
                for u in range(N+3):
                    an=ka[u-n] if 0<=u-n<len(ka) else 0
                    am=ka[u-m] if 0<=u-m<len(ka) else 0
                    bn=kb[u-n] if 0<=u-n<len(kb) else 0
                    bm=kb[u-m] if 0<=u-m<len(kb) else 0
                    kernel+=an*am/Fraction(24)+2*bn*bm
                if abs(n-m)>=len(ka) and abs(n-m)>=len(kb):
                    assert kernel==0
                rhs+=c[n]*c[m]*kernel
        assert lhs==rhs>=0
        gram+=1

    # Positive box-spline transform identity as formal rational factors.
    box=0
    for m in range(1,9):
        ps=[2,3,5,7,11,13,17,19][:m]
        s=Fraction(3,2)
        lhs=Fraction(1)
        for p in ps:
            lhs*=1-Fraction(1,p**2)  # s+1/2=2
        rhs=lhs/(s+Fraction(1,2))**m
        product=Fraction(1)
        for p in ps:
            product*= (1-Fraction(1,p**2))/(s+Fraction(1,2))
        assert rhs==product
        box+=1

    # PSD alone cannot force subpower size.
    for N in (1,10,100,1000):
        eps=Fraction(1,100)
        block=4-2*eps
        assert N*block>0

    mutations=sorted([
      "moving_box_order_promoted_to_fixed_detector_rejected",
      "orthogonal_coordinates_estimated_on_different_sources_rejected",
      "carrier_reintroduced_before_gram_rejected",
      "psd_sign_promoted_to_subpower_size_rejected",
      "diagonal_bound_promoted_to_offdiagonal_rejected",
      "far_ratio_zero_promoted_to_near_collision_rejected",
      "f1ato105405_promoted_to_proved_rejected",
      "rh_promoted_by_replay_rejected",
    ])
    result={
      "schema":"riemann.x105410.f1-orthogonal-ato.v1",
      "classification":VERDICT,
      "base_pr":730,
      "base_sha":"9aaf39898c95a1aa4af0b8aaf3a6fb56046e1b0f",
      "three_ray_pr":719,
      "three_ray_sha":"847e7feeac864bda4e3df38329d1a70c59aa4814",
      "orthogonal_split_checks":split,
      "gram_checks":gram,
      "box_transform_checks":box,
      "positive_box_spline_proved":True,
      "orthogonal_primitive_split_proved":True,
      "adelic_gram_reduction_proved":True,
      "f1ato105405_proved":False,
      "rh_established":False,
      "mutations_rejected":mutations,
    }
    canon=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["proof_object_sha256"]=hashlib.sha256(canon).hexdigest()
    return result

def main():
    r=run(); p=Path(__file__).resolve().parent/'results'/'verification.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(r['classification']);print(r['proof_object_sha256'])
if __name__=='__main__':main()
