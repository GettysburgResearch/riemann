"""Exact independent enumeration of a seven-spin instance of the model."""
from fractions import Fraction as F
from itertools import product
from flexible_tree import tree

def controls():
    z=[F(1,10)]*17;z[0]=F(2,7);z[6]=F(3,8);z[7]=F(5,11);z[11]=F(1,10)
    z[12:]=[F(3,5),F(5,8),F(3,5),F(3,5),F(3,5)]
    counts=(2,0,0,0,0,0,1,1,0,0,0)
    _,computed=tree(z,18,counts=counts)
    m0=z[11]*z[0]/100;m6=3*z[11]*z[6];m7=3*z[11]*z[7]
    edges=[(0,1,m0),(0,2,m0),(0,3,m6),(3,4,2*z[12]-1),(0,5,m7),(5,6,2*z[13]-1)]
    direct=[F(0)]*19;wrong_variance=F(0)
    for s in product((-1,1),repeat=7):
        mass=F(1,128)
        for i,j,c in edges:mass*=1+c*s[i]*s[j]
        x=z[0]*(s[1]+s[2])+z[6]*(s[3]+s[4])/2+z[7]*(s[5]+s[6])/2
        bad=z[0]*(s[1]+s[2])+z[6]*(s[3]+s[4])+z[7]*(s[5]+s[6])
        for n in range(19):direct[n]+=mass*x**n
        wrong_variance+=mass*bad**2
    if direct!=computed:raise ValueError('full Gibbs enumeration differs from conditional moment map')
    if direct[0]!=1:raise ValueError('finite Gibbs normalization')
    if wrong_variance==computed[2]:raise ValueError('factor-two negative control failed')
    return {'spins':7,'edges':6,'enumerated_configurations':128,'exact_moment_orders':list(range(19)),
       'normalized_total_mass':'1','conditional_formula_equals_full_enumeration':True,
       'missing_dimer_half_factor_rejected':True}
