#!/usr/bin/env python3
from fractions import Fraction
from pathlib import Path
import hashlib, json

def transpose(A):
    return [list(row) for row in zip(*A)]

def matmul(A,B):
    Bt=transpose(B)
    return [[sum(a*b for a,b in zip(row,col)) for col in Bt] for row in A]

def matadd(A,B,sign=1):
    return [[A[i][j]+sign*B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def eye(n):
    return [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]

def inverse(A):
    n=len(A)
    I=eye(n)
    M=[A[i][:]+I[i] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[x/q for x in M[c]]
        for r in range(n):
            if r!=c and M[r][c]:
                q=M[r][c]
                M[r]=[M[r][j]-q*M[c][j] for j in range(2*n)]
    return [row[n:] for row in M]

def trace(A):
    return sum(A[i][i] for i in range(len(A)))

def gram(E):
    return matmul(transpose(E),E)

checks=0

# Exact primal identity and completion of the square.
for m in range(1,5):
    for n in range(1,5):
        d=m+n
        for seed in range(1,26):
            A=[[Fraction(((r+1)*(j+2)+seed)%7-3,seed+7)
                for j in range(m)] for r in range(n)]
            B=[[Fraction(((i+2)*(k+1)+2*seed)%9-4,seed+11)
                for k in range(n)] for i in range(m)]
            Em=[eye(m)[r] if r<m else A[r-m] for r in range(d)]
            Ep=[B[r] if r<m else eye(n)[r-m] for r in range(d)]

            Gm=gram(Em); Gp=gram(Ep)
            Gmi=inverse(Gm); Gpi=inverse(Gp)
            C=matmul(transpose(Em),Ep)
            Xs=matmul(Gpi,transpose(C))

            defect=Fraction(m)-trace(
                matmul(matmul(matmul(Gmi,C),Gpi),transpose(C)))

            exact_residual=trace(matmul(
                Gmi,
                gram(matadd(Em,matmul(Ep,Xs),sign=-1))))
            assert defect==exact_residual and defect>=0

            X=[[Fraction(((i+1)*(j+1)+seed)%5-2,seed+13)
                for j in range(m)] for i in range(n)]
            residual=trace(matmul(
                Gmi,
                gram(matadd(Em,matmul(Ep,X),sign=-1))))
            Z=matadd(X,Xs,sign=-1)
            gap=trace(matmul(
                Gmi,
                matmul(matmul(transpose(Z),Gp),Z)))
            assert residual==defect+gap and gap>=0
            checks+=3

# Exact one-pole pseudohyperbolic calibration.
for a in range(-5,6):
    for d in range(-5,6):
        for y in range(1,6):
            for v in range(1,6):
                den=(y+v)**2+(a-d)**2
                corr2=Fraction(4*y*v,den)
                cost=Fraction((y-v)**2+(a-d)**2,den)
                assert 1-corr2==cost
                checks+=1

# Unwhitened pairwise-matching firewall.
for n in range(2,502):
    eps=Fraction(1,n)
    Em=[[Fraction(1),Fraction(1)],[Fraction(0),eps]]
    Ep=[[Fraction(1)],[Fraction(0)]]
    Gm=gram(Em); Gp=gram(Ep); C=matmul(transpose(Em),Ep)
    defect=Fraction(2)-trace(
        matmul(matmul(matmul(inverse(Gm),C),inverse(Gp)),transpose(C)))
    X=[[Fraction(1),Fraction(1)]]
    generalized=trace(matmul(
        inverse(Gm),
        gram(matadd(Em,matmul(Ep,X),sign=-1))))
    raw=eps*eps
    assert defect==1 and generalized==1 and raw<1
    checks+=3

result={
    "verdict":"PASS_T106630_PRIMAL_CAUCHY_TRANSPORT_CERTIFICATE",
    "exact_checks":checks,
    "primal_variational_identity":True,
    "basis_invariant_generalized_residual":True,
    "single_pole_cost":
      "((a-b)^2+(y-v)^2)/((a-b)^2+(y+v)^2)",
    "unwhitened_pairwise_sum_valid":False,
    "mesotransport106630_proved":False,
    "ninety_percent_established":False,
    "rh_established":False,
}
canonical=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
result["proof_object_sha256"]=hashlib.sha256(canonical).hexdigest()
out=Path(__file__).parent/"results"/"verification.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(result["verdict"])
print(json.dumps(result,indent=2,sort_keys=True))
