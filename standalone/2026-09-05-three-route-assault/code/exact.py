"""Small exact rational linear algebra; no numerical eigensolvers or assert gates."""
from fractions import Fraction as F
from typing import Sequence

Matrix = list[list[F]]

def matrix(rows: Sequence[Sequence[object]]) -> Matrix:
    out = [[F(x) for x in row] for row in rows]
    if out and any(len(row) != len(out[0]) for row in out):
        raise ValueError('ragged matrix')
    return out

def zeros(n: int, m: int | None = None) -> Matrix:
    if n < 0 or (m is not None and m < 0):
        raise ValueError('negative dimension')
    return [[F(0) for _ in range(n if m is None else m)] for _ in range(n)]

def eye(n: int) -> Matrix:
    a = zeros(n)
    for i in range(n): a[i][i] = F(1)
    return a

def tr(a: Matrix) -> F:
    if any(len(r) != len(a) for r in a): raise ValueError('not square')
    return sum((a[i][i] for i in range(len(a))), F(0))

def transpose(a: Matrix) -> Matrix:
    return [list(c) for c in zip(*a)] if a else []

def scale(a: Matrix, c: object) -> Matrix:
    q = F(c)
    return [[q*x for x in row] for row in a]

def add(a: Matrix, b: Matrix) -> Matrix:
    if len(a)!=len(b) or any(len(x)!=len(y) for x,y in zip(a,b)):
        raise ValueError('shape mismatch')
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]

def sub(a: Matrix, b: Matrix) -> Matrix:
    return add(a,scale(b,-1))

def mul(a: Matrix, b: Matrix) -> Matrix:
    if not a: return []
    if not b:
        if len(a[0]): raise ValueError('shape mismatch')
        return zeros(len(a),0)
    if len(a[0])!=len(b): raise ValueError('shape mismatch')
    bt=transpose(b)
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in bt] for row in a]

def det(a: Matrix) -> F:
    n=len(a)
    if any(len(r)!=n for r in a): raise ValueError('not square')
    b=[r[:] for r in a]; ans=F(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if b[j][i]),None)
        if pivot is None: return F(0)
        if pivot!=i: b[i],b[pivot]=b[pivot],b[i]; ans=-ans
        q=b[i][i]; ans*=q
        for j in range(i+1,n):
            fac=b[j][i]/q
            for k in range(i+1,n): b[j][k]-=fac*b[i][k]
            b[j][i]=F(0)
    return ans

def inverse(a: Matrix) -> Matrix:
    n=len(a)
    if any(len(r)!=n for r in a): raise ValueError('not square')
    b=[r[:]+e for r,e in zip(a,eye(n))]
    for i in range(n):
        p=next((j for j in range(i,n) if b[j][i]),None)
        if p is None: raise ValueError('singular matrix')
        b[i],b[p]=b[p],b[i]
        q=b[i][i]; b[i]=[x/q for x in b[i]]
        for j in range(n):
            if j!=i:
                q=b[j][i]; b[j]=[x-q*y for x,y in zip(b[j],b[i])]
    return [r[n:] for r in b]

def columns(vs: Sequence[Sequence[F]], n: int) -> Matrix:
    if any(len(v)!=n for v in vs): raise ValueError('column dimension')
    return [[v[i] for v in vs] for i in range(n)]

def projection(vs: Sequence[Sequence[F]], n: int) -> Matrix:
    if not vs: return zeros(n)
    b=columns(vs,n)
    return mul(mul(b,inverse(mul(transpose(b),b))),transpose(b))

def outer(v: Sequence[F], w: Sequence[F]) -> Matrix:
    return [[x*y for y in w] for x in v]

def apply(a: Matrix, v: Sequence[F]) -> list[F]:
    if a and len(a[0])!=len(v): raise ValueError('dimension mismatch')
    return [sum((x*y for x,y in zip(row,v)),F(0)) for row in a]

def dot(v: Sequence[F], w: Sequence[F]) -> F:
    if len(v)!=len(w): raise ValueError('dimension mismatch')
    return sum((x*y for x,y in zip(v,w)),F(0))

def hs2(a: Matrix) -> F:
    return sum((x*x for row in a for x in row),F(0))

def principal(a: Matrix, k: int) -> Matrix:
    return [r[:k] for r in a[:k]]

def positive_definite(a: Matrix) -> bool:
    return a==transpose(a) and all(det(principal(a,k))>0 for k in range(1,len(a)+1))
