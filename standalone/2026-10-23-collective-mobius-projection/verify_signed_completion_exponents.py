"""Exact exponent audit only; it does not certify analytic Mertens or kernel inputs."""
from fractions import Fraction as F
import json

checks = 0
def require(condition, message):
    global checks
    checks += 1
    if not condition:
        raise ValueError(message)

for beta in [F(2,3), F(7,8), F(1)]:
    gamma = 1-beta
    require(F(11,24)+gamma/12 == (13-2*beta)/24, 'D core')
    require(F(1,24)+gamma/12 == (3-2*beta)/24, 'H core')
    require(F(7,6)-gamma/2 == F(2,3)+beta/2, 'd0 convergence')
    require(F(13,6)-gamma/2 == F(5,3)+beta/2, 'f convergence')
    require((1-beta)/2+beta > 0, 'positive head exponent')
    require(beta-F(3,2) < 0, 'negative tail exponent')
    for a in range(1,6):
        for presence in [0,1]:
            j=(a+presence)%6
            target=(3-2*beta)*a/12
            unselected=-(25-2*beta)*presence/12+(3-2*beta)*j/12
            require(unselected <= target, 'unselected fixed-prime bound')
            if j<=4:
                selected=-(25-2*beta)*presence/12-1+(3-2*beta)*(j+6)/12
                require(selected <= target, 'selected fixed-prime bound')
            pole_target=(2-beta)*a/12
            pole_unselected=-(12-beta)*presence/12+(2-beta)*j/12
            require(pole_unselected <= pole_target, 'unselected first-pole bound')
            if j<=4:
                pole_selected=-(12-beta)*presence/12-1+(2-beta)*(j+6)/12
                require(pole_selected <= pole_target, 'selected first-pole bound')
    require(1-beta/6-(13-2*beta)/12 == -F(1,12), 'pole D ratio')
    require((2-beta)/6-(3-2*beta)/12 == F(1,12), 'pole H ratio')

beta,h,k=F(7,8),F(6,7),F(1,24)
volume=h+k
nonvolume=(13-2*beta)/12-h*(1-beta)/3+k*(15-2*beta)/12
pole=h/3+F(2,3)
old=F(5,6)+h/6
require(volume==F(151,168), 'benchmark volume')
require(nonvolume==F(7643,8064), 'benchmark nonvolume')
require(pole==F(20,21), 'benchmark pole')
require(max(volume,nonvolume,pole)==pole, 'benchmark maximum')
require(old-pole==F(1,42), 'benchmark saving')
require(k<(3-2*beta)*(2*h-1)/(15-2*beta), 'improved label capacity')
require(k<F(5,6)*(1-h) and k<F(1,7) and k<h/2, 'other capacities')
negative_controls={
    'incorrect_benchmark_rejected': nonvolume != F(1271,1344),
    'missing_inverse_U_gain_rejected': (13-2*beta)/12+k*(15-2*beta)/12 > old,
    'claim_all_projection_mass_below_volume_rejected': pole > volume,
}
for name, passed in negative_controls.items():
    require(passed, name)
print(json.dumps({
    'status':'pass',
    'scope':'Exact affine local exponents and conditional projection benchmark only',
    'total_checks':checks,
    'beta_endpoint_checks':['2/3','7/8','1'],
    'benchmark':{'beta':str(beta),'h':str(h),'k':str(k),'volume':str(volume),
                 'nonvolume':str(nonvolume),'pole':str(pole),'saving':str(old-pole)},
    'negative_controls':negative_controls,
},sort_keys=True))
