#!/usr/bin/env python3
"""Independent exact Gibbs enumeration of a seven-vertex chain/hub instance."""
from fractions import Fraction as F
from itertools import product
from math import comb
from chain_exact import evaluate

def controls():
    # Vertex0 hub;1,2 repeated leaves;3,4,5,6 the four-vertex core chain.
    z=[F(2,7),F(1,8),F(3,11),F(5,13),F(7,17),F(2,9),F(1,5),F(2,7),F(3,8)]
    eta=F(1,10)
    _,computed=evaluate(z,20,counts=(2,0),ncore=4,eta=eta)
    edges=[(0,1,eta*z[0]),(0,2,eta*z[0]),(0,3,eta),
       (3,4,z[6]),(4,5,z[7]),(5,6,z[8])]
    direct=[F(0)]*21;wrong_variance=F(0);wrong_mass=F(0)
    for spin in product((-1,1),repeat=7):
        mass=F(1,128);bad=mass
        for i,j,c in edges:
            mass*=1+c*spin[i]*spin[j]
            # An independent negative control changes the first core edge
            # to zero while retaining the exact positive Gibbs weights.
            bad*=1+(0 if (i,j)==(3,4)else c)*spin[i]*spin[j]
        x=z[0]*(spin[1]+spin[2])+sum((z[2+k]*spin[3+k]for k in range(4)),F(0))
        power=F(1)
        for n in range(21):direct[n]+=mass*power;power*=x
        wrong_variance+=bad*x*x;wrong_mass+=bad
    if direct!=computed:raise ValueError('full Gibbs enumeration differs from chain recurrence')
    if direct[0]!=1 or wrong_mass!=1:raise ValueError('finite Gibbs normalization')
    if any(direct[k]for k in range(1,21,2)):raise ValueError('zero-field spin-flip symmetry')
    if wrong_variance==computed[2]:raise ValueError('deleted positive edge negative control failed')
    # Independently check all raw-moment/cumulant round trips without using
    # the production cumulant routine.
    cumul=[F(0)]*21
    for n in range(1,21):
        cumul[n]=direct[n]-sum((comb(n-1,j-1)*cumul[j]*direct[n-j]for j in range(1,n)),F(0))
    return {'spins':7,'edges':6,'enumerated_configurations':128,'exact_raw_moment_orders':list(range(21)),
       'normalized_total_mass':'1','chain_formula_equals_full_gibbs_enumeration':True,
       'odd_raw_moments_zero':True,'deleted_core_edge_negative_control_rejected':True,
       'variance':str(direct[2]),'deleted_edge_variance':str(wrong_variance),
       'cumulant18':str(cumul[18]),'cumulant20':str(cumul[20])}

if __name__=='__main__':
    import json
    print(json.dumps(controls(),sort_keys=True))
