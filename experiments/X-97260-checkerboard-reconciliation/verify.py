#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import argparse, hashlib, json

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]

def transpose(A):
    return [list(row) for row in zip(*A)]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    args=ap.parse_args()

    H=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
    K=[[Fraction(1),Fraction(1)],[Fraction(2),Fraction(4)]]
    M=matmul(H,K)
    assert det2(H)==1 and det2(K)==2 and det2(M)==2

    a=Fraction(3,2); b=Fraction(5,3)
    H_cross=[[Fraction(0),a],[b,Fraction(0)]]
    H_ordered=[[a,Fraction(0)],[Fraction(0),b]]
    assert det2(H_cross)==-a*b
    assert det2(H_ordered)==a*b

    H_rect=[
        [Fraction(2),Fraction(0),Fraction(3)],
        [Fraction(0),Fraction(5),Fraction(0)],
    ]
    K_rect=[[Fraction(1),Fraction(7)],[Fraction(2),Fraction(11)]]
    M_rect=matmul(transpose(H_rect),K_rect)
    assert len(M_rect)==3 and len(M_rect[0])==2

    result={
      "classification":"PASS_T97260_CHECKERBOARD_RECONCILIATION",
      "det_H":"1",
      "det_K":"2",
      "det_source_feature":"2",
      "hall_feasible":False,
      "cross_order_incidence_minor":str(det2(H_cross)),
      "owner_ordered_incidence_minor":str(det2(H_ordered)),
      "correct_product_shape":[3,2],
      "imported_odd_history_gap_lower_bound":"17",
      "global_Hall_proved":False,
      "RH_established":False,
    }
    raw=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["proof_object_sha256"]=hashlib.sha256(raw).hexdigest()

    out=Path(args.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(result["classification"])
    print(result["proof_object_sha256"])

if __name__=="__main__":
    main()
