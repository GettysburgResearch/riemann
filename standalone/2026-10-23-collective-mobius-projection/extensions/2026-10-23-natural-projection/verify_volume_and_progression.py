"""Exact finite consequences; arithmetic identities remain analytic inputs."""
from fractions import Fraction as F
import json
n=0
def require(ok,why):
    global n
    if not ok:raise ArithmeticError(why)
    n+=1
for k in (F(0),F(1,7)):
    for h in ((1+k)/2,F(1),F(2)):
        require(4*k<=h,'empty-head mixed volume')
        require(-F(1,6)+5*k/6+5*h/6<=h,'head mixed volume')
require(-F(29,12)+F(1,4)==-F(13,6),'remaining f exponent')
require(-F(3,2)+F(5,6)==-F(2,3),'k head sum')
require(-F(5,12)+F(1,6)==-F(1,4),'balanced k tail')
for k in (F(0),F(1,6)):
    require(F(2,7)+k<=1,'progression head legality')
    require(F(31,42)+7*k/6<=F(5,6)+k,'middle pole cost')
    require(F(1,2)+3*k/2<=F(5,6)+k,'scalar second pole cost')
    require(F(5,6)+k/6<=F(5,6)+k,'first pole cost')
require(F(2,3)+F(1,14)==F(31,42),'pole head exponent')
require(F(5,6)-F(2,21)==F(31,42),'pole tail exponent')
h=F(6,7);k=F(1,10)
terms=[h,F(11,12)+k/12,F(5,6)+7*k/6,F(2,3)+h/3]
require(terms==[F(6,7),F(37,40),F(19,20),F(20,21)],'squarefree projection example')
require(F(5,6)+h/6-max(terms)==F(1,42),'squarefree projection saving')
for k in (F(0),F(1,7)):
    for h in (F(0),(1+k)/2):
        bound=max(F(11,12)+k/12,F(5,6)+k)
        small=[h,k,5*k/6+h/3,k/3+5*h/6,
               F(5,6)+h/6,F(5,6)+k-5*h/6,
               F(5,6)+5*k/6-h/2,F(5,6)+k/3,F(2,3)+h/3]
        for term in small:require(term<=bound,'small-scale natural projection cost')
for eps in (0,1):
    require(-F(11,12)*eps-F(1,2)+F(2+eps,12)-F(1,2)<=-F(5,6),'selected outside plateau')
    require(-F(11,12)*eps-1<=-1,'selected inside plateau')
h=F(7,8);k=1-h
natural=[h,1-h/12,F(11,6)-h,F(2,3)+h/3]
require(natural==[F(7,8),F(89,96),F(23,24),F(23,24)],'natural projection terms')
require(F(5,6)+h/6-max(natural)==F(1,48),'natural projection saving')
for h in (F(6,7),F(1)):
    k=1-h
    require(k<=F(1,7) and k<h/2,'natural range and Gram')
    for term in [h,1-h/12,F(11,6)-h,F(2,3)+h/3]:
        require(term<=F(5,6)+h/6,'closed natural comparison; strict inside')
print(json.dumps({'status':'PASS','checks':n,'scope':'finite exponent algebra only; analytic identities require the separate proofs and reviews','squarefree_projection_terms':list(map(str,terms)),'natural_projection_terms':list(map(str,natural))},indent=2))
