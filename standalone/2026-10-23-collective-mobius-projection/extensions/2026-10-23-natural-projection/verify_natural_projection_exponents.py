"""Exact exponent replay only; not an analytic-source certificate."""
from fractions import Fraction as F
import json

checks = []
def check(name, condition):
    if not condition:
        raise RuntimeError(name)
    checks.append(name)

for k in (F(0), F(1,7)):
    check(f"volume_domain_{k}", 4*k <= (1+k)/2)
    check(f"low_mixed_{k}", 5*k <= 1)
    check(f"partial_pole1_{k}", F(5,6)+k/6 <= F(5,6)+k)
    check(f"partial_pole2_{k}", F(31,42)+7*k/6 <= F(5,6)+k)
    check(f"partial_pole3_{k}", F(1,2)+3*k/2 <= F(5,6)+k)
    check(f"progression_head_domain_{k}", F(2,7)+k <= 1)
    for h in (F(0), (1+k)/2):
        base = F(11,12)+k/12
        plateau = F(5,6)+k
        terms = [
            h, k, 5*k/6+h/3, k/3+5*h/6,
            F(5,6)+h/6, F(5,6)+k-5*h/6,
            F(5,6)+5*k/6-h/2, F(5,6)+k/3,
            F(2,3)+h/3,
        ]
        # Each affine term is below one of the two target monomials
        # throughout the box; the fixed assignments avoid an
        # unjustified convex-envelope endpoint inference.
        assignments = [base,plateau,base,base,base,
                       plateau,plateau,plateau,base]
        for i,(x,y) in enumerate(zip(terms, assignments)):
            check(f"small_scale_{k}_{h}_{i}", x<=y)

# Selected squarefree labels, epsilon0/1; old and improved plateau.
for eps in (0,1):
    a=1
    outside = -F(1,2)-F(a,2)+F(a+eps+1,12)-F(11*eps,12)
    inside = -F(1,2)-F(a,2)-F(11*eps,12)
    check(f"new_plateau_outside_{eps}", outside<=-F(5,6))
    check(f"new_plateau_inside_{eps}", inside<=-1)
    low_outside = -F(3,4)-F(a,4)-F(eps,4)
    low_inside = -F(a,2)-F(eps,2)
    check(f"low_mixed_outside_{eps}", low_outside<=-1)
    check(f"low_mixed_inside_{eps}", low_inside<=-F(1,2))
    high_outside = -F(1,4)-F(a,4)-F(eps,4)
    high_inside = F(1,2)-F(a,2)-F(eps,2)
    check(f"high_mixed_outside_{eps}", high_outside<=-F(1,2))
    check(f"high_mixed_inside_{eps}", high_inside<=0)

check("pole_balance",
      F(2,3)+F(1,14) == F(5,6)-F(2,21) == F(31,42))
check("k_head_exponent", -F(5,12)+F(1,6)==-F(1,4))
check("k_tail_exponent", -F(1,4)==F(1,2)*(-F(1,2)))
check("high_nonvolume_D", F(5,12)+F(1,24)==F(11,24))
check("high_nonvolume_K", F(1,24)==F(1,24))
check("high_nonvolume_U", F(1,12)-F(1,12)==0)

for h in (F(6,7), F(7,8), F(1)):
    k=1-h
    old=F(5,6)+h/6
    terms=[h,1-h/12,F(11,6)-h,F(2,3)+h/3]
    for i,t in enumerate(terms):
        check(f"natural_comparison_{h}_{i}",t<=old)
    check(f"natural_label_domain_{h}",k<=F(1,7))
    check(f"natural_gram_domain_{h}",k<h/2)

h=F(7,8)
terms=[h,1-h/12,F(11,6)-h,F(2,3)+h/3]
check("example_new", max(terms)==F(23,24))
check("example_old", F(5,6)+h/6==F(47,48))
check("example_saving", F(47,48)-max(terms)==F(1,48))

# Negative controls: the larger label domain would require a new
# volume-domain argument, and the natural gain is not valid below6/7.
check("reject_automatic_volume_at_one_sixth",
      4*F(1,6) > (1+F(1,6))/2)
h=F(5,6)
check("reject_natural_gain_below_threshold",
      F(11,6)-h > F(5,6)+h/6)

print(json.dumps({"scope":"exact rational exponent algebra only",
                  "checks":len(checks),"status":"pass"},
                 sort_keys=True))

