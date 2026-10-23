"""Exact exponent audit for C1; the analytic vector estimates are inputs."""
from fractions import Fraction as F
import json

checks=0
def require(ok,label):
    global checks
    if not ok:raise ArithmeticError(label)
    checks+=1

# Every difference below is affine in h,k, so the listed endpoints check
# the full polyhedral parameter ranges. No floating point is used.
for k in (F(0),F(1,7)):
    for h in ((1+k)/2,F(1),F(2)):
        a=h/6-(1+k)/12
        require(a>=0,'balanced cutoff admissible')
        require((1+k-h)/2+3*a==(1+k)/4,'reflected volume')
        require(h/2-3*a==(1+k)/4,'original volume')
        require(F(5,12)+(1+k-h)/12+a/2==F(11,24)+k/24,'reflected nonvolume')
        require(F(5,12)+h/12-a/2==F(11,24)+k/24,'original nonvolume')
        require(h/6+F(1,3)-a==F(5,12)+k/12,'complete pole tail')
        base=F(11,12)+k/12
        plateau=F(5,6)+F(7,6)*k
        require((1+k)/2<=base,'volume dominated')
        require(F(5,6)+k/6<=base,'pole dominated')
        require(2*k<=plateau,'K squared dominated')
        require(h/6>=a,'finite original plateau range')

h=F(6,7);k=F(1,9)
new=[F(11,12)+k/12,F(5,6)+7*k/6]
old=F(5,6)+h/6
require(new==[F(25,27),F(26,27)],'full vector benchmark')
require(old-max(new)==F(5,378),'full vector saving')
require(k<min(2*h-1,h/7,F(1,7)),'strict comparison range')
require(h>=(1+k)/2,'full vector cutoff domain')

# Conditional consumers are explicitly not established by this checker.
with_KU=max(new+[h+k,h/3+F(2,3)])
require(with_KU==F(61,63),'conditional primitive KU consumer')
require(old-with_KU==F(1,126),'conditional primitive saving')
require(F(5,6)+7*F(1,7)/6>old,'overlarge label range rejected')
print(json.dumps({'status':'PASS','checks':checks,
 'scope':'exact finite exponent algebra for the full-series C1 theorem; no primitive extension certified',
 'full_vector_benchmark':{'h':str(h),'k':str(k),'terms':list(map(str,new)),
                          'old':str(old),'saving':str(old-max(new))},
 'hypothetical_primitive_KU_consumer':{'exponent':str(with_KU),'saving':str(old-with_KU),
                                     'analytic_status':'not proved here'}},indent=2))
