"""Complete-theta moment enclosures, not a truncated-source definition.

See ISING.md for the complete 1/128 trapezoidal alias bound, both omitted
spatial lattices, every n>=21 term, and dyadic rounding. All three analytic
remainders together are less than (2r)! 2^-237 for r<=10.
"""
from fractions import Fraction as Q
from math import factorial, comb
from exact_interval import I, exp, pi, SCALE

def theta_moments(order=10, step_den=128):
    if type(order) is not int or not 1<=order<=10:raise ValueError('order must be 1..10')
    if step_den not in (128,160):raise ValueError('certified meshes are 128 and 160')
    p=pi();mom=[I.q(0) for _ in range(order+1)]
    for j in range(3*step_den+1):
        t=Q(j,step_den);e2=exp(2*t);e9=exp(Q(9,2)*t);e5=exp(Q(5,2)*t)
        ph=I.q(0)
        for n in range(1,21):
            nn=n*n
            ph=ph+(4*(p**2)*nn**2*e9-6*p*nn*e5)*exp(-p*nn*e2)
        wt=Q(1 if j==0 else 2,step_den)
        for r in range(order+1):mom[r]=mom[r]+wt*t**(2*r)*ph
    for r in range(order+1):
        error=I.q(Q(factorial(2*r),1<<237)).hi
        mom[r]=I(mom[r].lo-error,mom[r].hi+error)
    return mom

def cumulants(even):
    m=[I.q(0)]*(2*len(even)-1)
    for r,v in enumerate(even):m[2*r]=I.q(v)
    k=[I.q(0)]*len(m)
    for n in range(1,len(m)):
        k[n]=m[n]-sum((comb(n-1,j-1)*k[j]*m[n-j] for j in range(1,n)),I.q(0))
    return k[2::2]

def report(mesh=128):
    raw=theta_moments(10,mesh)
    normal=[v/raw[0] for v in raw];normal[0]=I.q(1)
    cum=cumulants(normal);v=normal[1];k4=cum[1]
    if not v.inside('0.0462','0.0463'):raise ArithmeticError('variance boundary failed')
    if not k4.inside('-0.000448','-0.000444'):raise ArithmeticError('fourth cumulant boundary failed')
    return {'mesh_denominator':mesh,'theta_terms':20,'cells_each_positive_side':3*mesh,
            'max_even_moment':20,'bits':512,'source':'complete native theta with all analytic remainders',
            'normalization':raw[0].bounds(),'variance':v.bounds(),'fourth_cumulant':k4.bounds(),
            'normalized_even_moments':[x.bounds() for x in normal],
            'rh_proved':False,'all_order_realization_proved':False}

if __name__=='__main__':
    import argparse,json
    a=argparse.ArgumentParser();a.add_argument('--mesh',type=int,default=128);ns=a.parse_args()
    print(json.dumps(report(ns.mesh),indent=2,sort_keys=True))
