"""Exact rational constants for E_f(sigma)<=-0.31 eta.

The analytic inequalities are in LOGISTIC_NEGATIVE_ARCHIMEDEAN.md.
No global zero-free constant is certified by this finite calculation.
"""
from fractions import Fraction as Q
import json


def check(ok,label):
    if not ok:
        raise RuntimeError(label)


s2=sum((Q(1,(3+2*n)**2) for n in range(100)),Q(0))
s4=sum((Q(1,(3+2*n)**4) for n in range(100)),Q(0))+Q(1,6*201**3)
lower=Q(49,100)*s2-2*Q(49,100)**3*s4
negative=Q(567,200)*lower
b=Q(299,100)
eta=Q(3,400)
positive=175*eta**2*(2/b**3+1/(2*b**2))
net=negative-positive
check(lower>Q(1098466,10**7),'integral lower bound')
check(negative>Q(3114,10000),'negative resource')
check(positive<Q(1288,10**6),'positive correction')
check(net>Q(31,100),'net negative archimedean resource')
check(not net>Q(32,100),'negative control: unjustified 0.32')
print(json.dumps({'status':'pass','scope':'exact constants for E_f(sigma)<=-0.31 eta only',
                  'positive_checks':4,'negative_controls':1,
                  'integral_lower_decimal':float(lower),
                  'negative_resource_decimal':float(negative),
                  'positive_correction_upper_decimal':float(positive),
                  'net_lower_rational':str(net),'net_lower_decimal':float(net)},sort_keys=True))
