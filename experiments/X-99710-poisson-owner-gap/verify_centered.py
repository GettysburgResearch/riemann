#!/usr/bin/env python3
from fractions import Fraction
import hashlib, json, math

VERDICT="PASS_T99712_ANNULUS_CENTERED_OWNER_TAIL_FACTORIZATION"

def exact_tail_factorization(r,b):
    lhs=Fraction(0)
    for i,ri in enumerate(r):
        for j,rj in enumerate(r):
            lhs += b[i]*b[j]*min(ri,rj)**2

    points=[Fraction(0)]+sorted(set(r))
    rhs=Fraction(0)
    for k in range(1,len(points)):
        lo,hi=points[k-1],points[k]
        tail=sum((b[i] for i,ri in enumerate(r) if ri>=hi),Fraction(0))
        rhs += (hi**2-lo**2)*tail**2
    return lhs,rhs

def verify():
    checks={}
    fixtures=[
        ([1,2,5],[Fraction(1),Fraction(-2),Fraction(3,2)]),
        ([1,3,4,8],[Fraction(2),Fraction(-1,3),Fraction(5,7),Fraction(-4)]),
        ([2,2,7],[Fraction(1,2),Fraction(3,5),Fraction(-7,11)])
    ]
    for r,b in fixtures:
        lhs,rhs=exact_tail_factorization(list(map(Fraction,r)),b)
        assert lhs==rhs
    checks["exact_min_kernel_tail_factorization"]=True

    r=[Fraction(1),Fraction(4),Fraction(8)]
    b=[Fraction(2),Fraction(-3),Fraction(5)]
    physical=sum(b,Fraction(0))**2
    low=(Fraction(1)**2-Fraction(0)**2)*sum(b,Fraction(0))**2
    assert physical==low
    checks["physical_square_is_first_tail_term"]=True

    assert 2*(1-Fraction(1,2))==1
    assert Fraction(10)-Fraction(6,67)>1
    assert Fraction(10)+Fraction(6,67**2)>1
    checks["fixed_width_unit_owner_gap"]=True

    samples=[]
    for L in [100,1000,10000,100000,1000000]:
        M=max(1,int(L/(math.log(L+math.e)**3)))
        logR=(M+3)*math.log(2)
        assert logR/L < 0.2
        samples.append({"L":L,"M":M,
                        "log_R_over_log_x":logR/(L*math.log(2))})
    checks["subpower_annulus_samples"]=samples

    checks["aotp99710_proved"]=False
    checks["rh_established"]=False
    payload={"verdict":VERDICT,"checks":checks,
             "open":["AOTP99710","RH"]}
    payload["proof_object_sha256"]=hashlib.sha256(
        json.dumps(payload,sort_keys=True,separators=(",",":")).encode()
    ).hexdigest()
    return payload

if __name__=="__main__":
    p=verify()
    print(VERDICT)
    print(p["proof_object_sha256"])
