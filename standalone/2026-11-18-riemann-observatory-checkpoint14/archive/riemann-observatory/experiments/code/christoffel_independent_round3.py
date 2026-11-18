"""Independent exact Christoffel/one-sided scope checks (Python stdlib only).

This is not a computation of zeta zeros or of the sine-process moments.
The four displayed sine moments are inputs whose polynomial implication is checked.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def solve(A,b):
    A=[list(map(F,row))+[F(v)] for row,v in zip(A,b)]
    n=len(b)
    for j in range(n):
        pivot=next(k for k in range(j,n) if A[k][j])
        A[j],A[pivot]=A[pivot],A[j]
        t=A[j][j];A[j]=[x/t for x in A[j]]
        for k in range(n):
            if k!=j:
                t=A[k][j];A[k]=[x-t*y for x,y in zip(A[k],A[j])]
    return [row[-1] for row in A]


def det(A):
    A=[list(map(F,row)) for row in A];value=F(1)
    for j in range(len(A)):
        pivot=next(k for k in range(j,len(A)) if A[k][j])
        if pivot!=j:A[j],A[pivot]=A[pivot],A[j];value=-value
        t=A[j][j];value*=t
        for k in range(j+1,len(A)):
            ratio=A[k][j]/t
            for ell in range(j,len(A)):A[k][ell]-=ratio*A[j][ell]
    return value


def convolution(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):c[j+k]+=x*y
    return c


def expectation(p,y):return sum((x*t for x,t in zip(p,y)),F(0))


def analyze(y):
    H=[[y[j+k] for k in range(3)] for j in range(3)]
    b=solve([[y[2],y[3]],[y[3],y[4]]],[y[1],y[2]])
    p=[F(1),-b[0],-b[1]]
    assert expectation([0]+p,y)==0
    assert expectation([0,0]+p,y)==0
    lam=expectation(convolution(p,p),y)
    q=[-x for x in convolution(p,p)];q[0]+=1
    return dict(moments=list(map(str,y)),Hankel_leading_minors=[str(det([row[:n] for row in H[:n]])) for n in (1,2,3)],minimizer=list(map(str,p)),lambda_at_zero=str(lam),one_minus_lambda=str(1-lam),candidate_q=list(map(str,q)),q_expectation=str(expectation(q,y)))


# Exact Q(sqrtD) elements are pairs a+b sqrtD.
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y,D):return (x[0]*y[0]+D*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def power(x,n,D):
    z=(F(1),F(0))
    for _ in range(n):z=mul(z,x,D)
    return z

def positive_pair(z,D):
    a,b=z
    if a>=0 and b>=0:return a>0 or b>0
    if a<=0 and b<=0:return False
    if a>0:return a*a>D*b*b
    return D*b*b>a*a


def canonical_checks(D,nodes,weights,target):
    assert all(positive_pair(w,D) for w in weights)
    vals=[]
    for k in range(5):
        v=(F(0),F(0))
        for x,w in zip(nodes,weights):v=add(v,mul(w,power(x,k,D),D))
        assert v==(target[k],F(0)),(D,k,v,target[k])
        vals.append(str(v[0]))
    return {'radicand':D,'nodes':[[str(a),str(b)] for a,b in nodes], 'weights':[[str(a),str(b)] for a,b in weights], 'moments_exact':vals,'weight_positivity_exact':True,'field_encoding':'[a,b] represents a+b sqrt(D)'}


def main():
    eigen=[-1,-1,-1,2,2,2,2,3]
    yw=[sum((F(v)**k for v in eigen),F(0))/8 for k in range(5)]
    ys=list(map(F,[1,1,F(4,3),2,F(13,4)]))
    witness=analyze(yw);sine=analyze(ys)
    assert witness['lambda_at_zero']=='3/14'
    assert sine['lambda_at_zero']=='5/36'
    actual=F(sum(v>0 for v in eigen),len(eigen))
    assert 1-F(witness['lambda_at_zero'])-actual==F(9,56)
    cw=canonical_checks(163,[(F(0),F(0)),(F(4,7),-F(1,7)),(F(4,7),F(1,7))],[(F(3,14),F(0)),(F(11,28),-F(27,2282)),(F(11,28),F(27,2282))],yw)
    cs=canonical_checks(57,[(F(0),F(0)),(F(21,16),-F(1,16)),(F(21,16),F(1,16))],[(F(5,36),F(0)),(F(31,72),F(25,1368)),(F(31,72),-F(25,1368))],ys)
    # Sine minimizer at negative x=-t has nonnegative coefficients and constant1.
    sp=list(map(F,sine['minimizer']))
    assert sp[0]==1 and -sp[1]>0 and sp[2]>0
    result={'arithmetic':'exact Fraction and quadratic-field pair arithmetic; no floating computation','witness_eigenvalues':eigen,'witness_positive_fraction':str(actual),'claimed_minus_actual':str(F(9,56)),'witness':witness,'witness_canonical':cw,'sine_moment_input':sine,'sine_canonical':cs,'sine_positive_index_bound':'31/36','conditional_simple_bound':'13/18','scope':'Checks the stated finite moment algebra, not the source prime-side moment hypothesis or the main AF theorem.'}
    out=Path(__file__).resolve().parents[1]/'results/christoffel_independent_round3.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('Exact8-eigenvalue counterexample,2 Hankel minimizations,10 quadratic-field canonical moments, all positive weights, and sine polynomial certificate passed.')

if __name__=='__main__':main()
