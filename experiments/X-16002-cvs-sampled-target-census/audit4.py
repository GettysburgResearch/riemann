"""AUDIT POINT 4: does p=(-1,3,-1) refute L-16003(iv)'s outer-ray clause?"""
from fractions import Fraction as F
import sympy as sp
s = sp.symbols('s')
lams=[-1,0,1]; p=[F(-1),F(3),F(-1)]
P = sum(sp.Rational(p[i].numerator,p[i].denominator)*sp.prod([(sp.Integer(lams[k])-s) for k in range(3) if k!=i]) for i in range(3))
P = sp.Poly(sp.expand(P), s)
print("p =", [str(x) for x in p], "  eta^T p =", sum(p))
print("P(s) =", P.as_expr(), "  roots:", sp.solve(P.as_expr(), s))
rts = sorted(sp.nsimplify(r) for r in sp.solve(P.as_expr(), s))
print()
print("Region occupancy:")
for j in range(2):
    a,b = lams[j], lams[j+1]
    c = sum(1 for r in rts if a < r < b)
    print(f"  interior gap ({a},{b}): {c} root(s)   xi_j*xi_(j+1) = {p[j]*p[j+1]} -> parity must be {'ODD' if p[j]*p[j+1]>0 else 'EVEN'}")
lo = sum(1 for r in rts if r < lams[0]); hi = sum(1 for r in rts if r > lams[-1])
print(f"  outer ray (-inf,{lams[0]}): {lo} root(s)")
print(f"  outer ray ({lams[-1]},inf):  {hi} root(s)")
print()
print("L-16003(iv) as written says: '...and the two outer rays carry none.'")
print(f"  --> REFUTED: the outer rays carry {lo+hi} of the {int(P.degree())} roots, the interior gaps carry 0.")
print()
print("CORRECTED outer-ray parity rule (derive: as s->lam_N^+, R -> -inf*sign(xi_N);")
print("as s->+inf, R ~ -(eta^T xi)/s -> 0^- * sign(eta^T xi)).  Odd iff xi_N*(eta^T xi) < 0:")
for (nm, xN) in [("upper", p[-1]), ("lower", p[0])]:
    prod = xN*sum(p)
    print(f"  {nm} ray: xi_(+-N)*(eta^T xi) = {prod} -> parity {'ODD' if prod<0 else 'EVEN'}")
print(f"  observed: lower {lo}, upper {hi}  -> rule {'HOLDS' if (lo%2==(1 if p[0]*sum(p)<0 else 0) and hi%2==(1 if p[-1]*sum(p)<0 else 0)) else 'FAILS'}")
print()
print("Cross-check the corrected rule on a battery:")
import itertools
tests=[[F(1),F(8),F(1)],[F(1,10),F(8,10),F(1,10)],[F(-1),F(3),F(-1)],[F(2),F(-3),F(2)],[F(3),F(-3),F(1)],[F(-1),F(4),F(-2)]]
for pp in tests:
    tot=sum(pp)
    if tot==0: continue
    pp=[x/tot for x in pp]
    Pq = sum(sp.Rational(pp[i].numerator,pp[i].denominator)*sp.prod([(sp.Integer(lams[k])-s) for k in range(3) if k!=i]) for i in range(3))
    Pq = sp.Poly(sp.expand(Pq), s)
    rr = sp.Poly(Pq,s).real_roots()
    rr = [sp.nsimplify(r) for r in rr]
    lo = sum(1 for r in rr if r < -1); hi = sum(1 for r in rr if r > 1)
    g0 = sum(1 for r in rr if -1 < r < 0); g1 = sum(1 for r in rr if 0 < r < 1)
    pred = lambda x: 1 if x*sum(pp) < 0 else 0
    ok = (lo%2==pred(pp[0])) and (hi%2==pred(pp[-1])) and (g0%2==(1 if pp[0]*pp[1]>0 else 0)) and (g1%2==(1 if pp[1]*pp[2]>0 else 0))
    print(f"  p={str([str(x) for x in pp]):<44} occupancy lo={lo} g0={g0} g1={g1} hi={hi}  parity rule {'OK' if ok else 'FAIL'}")
