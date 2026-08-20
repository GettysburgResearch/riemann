#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

# Exact symbolic coefficient verification using monomials in formal r_i.
# A monomial is represented by a frozenset of selected indices and integer sign.

def native(k):
    out={}
    for mask in range(1,1<<k):
        A=frozenset(i for i in range(k) if (mask>>i)&1)
        out[A]=(-1)**len(A)
    return out

def double_owner(k):
    out={}
    for i in range(k):
        A=frozenset([i])
        out[A]=out.get(A,0)-1
        for j in range(i+1,k):
            mids=list(range(i+1,j))
            for mask in range(1<<len(mids)):
                A={i,j}
                sign=1
                for t,h in enumerate(mids):
                    if (mask>>t)&1:
                        A.add(h)
                        sign*=-1
                A=frozenset(A)
                out[A]=out.get(A,0)+sign
    return out

def main():
    for k in range(1,11):
        a=native(k); b=double_owner(k)
        assert a==b, (k,a,b)
    print('PASS_T100600_DOUBLE_OWNER_BI_TRIANGULAR_IDENTITY')

if __name__=='__main__':
    main()
