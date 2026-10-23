"""Finite exact consequences; imported analytic estimates are not certified."""
from fractions import Fraction as F
import json

n=0
def require(value, label):
    global n
    if not value: raise ArithmeticError(label)
    n+=1

for k in (F(0),F(1,6)):
    require(F(1,2)+k<=F(2,3),'residue head')
    require(-F(1,6)+F(11,6)*k<=F(2,3),'residue tail')
    require(F(1,4)+F(5,4)*k<=F(11,12)+k/12,'mixed volume')
    require((1+k)/2<=F(11,12)+k/12,'volume')
    require(F(5,6)+k/6<=F(11,12)+k/12,'pole')
    require(2*k<=F(5,6)+k,'finite support')
    require(F(1,3)+k/2-F(5,12)*(1-k)==-F(1,12)+F(11,12)*k,'first density tail')
    require(F(1,6)+F(2,3)*k-F(1,4)*(1-k)==-F(1,12)+F(11,12)*k,'second density tail')
h=F(7,8);k=F(1,8)
full=[F(11,12)+k/12,F(5,6)+k]
require(max(full)==F(23,24),'full raw example')
require(F(5,6)+h/6-max(full)==F(1,48),'full raw saving')
h=F(6,7);k=F(1,12)
primitive=[h+k,F(11,12)+k/12,F(5,6)+F(7,6)*k,F(2,3)+h/3]
require(primitive==[F(79,84),F(133,144),F(67,72),F(20,21)],'CP terms')
require(max(primitive)==F(20,21),'CP maximum')
require(F(5,6)+h/6-max(primitive)==F(1,42),'CP saving')
require(k<F(1,7) and k<h/2,'CP range')
require(8**30>3**31*10**12,'finite heat example logarithm')
print(json.dumps({'status':'PASS','checks':n,'scope':'exact exponent and integer arithmetic only; analytic inputs assumed','primitive_projection_terms':list(map(str,primitive))},indent=2))
