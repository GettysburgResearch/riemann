#!/usr/bin/env python3
"""Exact countermodels verifying why the local gate needs both interior tests."""
from fractions import Fraction as F
from pathlib import Path
import runpy,json

g=runpy.run_path(str(Path(__file__).with_name('certify_bessel_window.py')))
I=g['I']
def intervals(p):return [I(x) for x in p]

# r=-z^3/(z^2+1/4) has strictly negative imaginary part on the upper
# unit semicircle, but two nonreal interior poles. Boundary positivity alone
# is insufficient. Its exact boundary numerator is x^2+3/4.
A=intervals([0,0,0,1]);B=intervals([F(1,4),0,1])
boundary=g['bernstein_positive'](g['circle_polynomial'](A,B))
count=g['graeffe_count'](B)
if count['zero_count']!=2:raise ArithmeticError('complex-pole control count')
try:g['real_poles'](A,B,F(1),2)
except ArithmeticError as e:
    if not isinstance(e.args[0],tuple) or e.args[0][0]!='Incomplete real root coverage':raise
else:raise ArithmeticError('nonreal interior poles were accepted')

# r=-z-(1/100)/(z-1/3) passes the outer semicircle sign and has exactly
# one interior real pole, but its residue is negative.
A2=intervals([F(1,100),-F(1,3),1]);B2=intervals([-F(1,3),1])
boundary2=g['bernstein_positive'](g['circle_polynomial'](A2,B2))
count2=g['graeffe_count'](B2)
if count2['zero_count']!=1:raise ArithmeticError('negative-residue control count')
try:g['real_poles'](A2,B2,F(1),1)
except ArithmeticError as e:
    if e.args[0]!='Certified negative residue':raise
else:raise ArithmeticError('negative interior residue was accepted')

print(json.dumps({'status':'PASS','arithmetic':'exact rational intervals',
 'complex_pole_control':{'boundary_passes':True,'interior_zero_count':2,'missing_real_coverage_rejected':True},
 'negative_residue_control':{'boundary_passes':True,'interior_real_poles':1,'negative_residue_rejected':True},
 'scope':'Verifies rejection of two mathematically distinct false local-sign shortcuts; no RH assertion.'},indent=2))
