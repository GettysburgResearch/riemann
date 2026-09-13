"""Exact/interval finite moment algebra; no numerical eigensolver."""
from fractions import Fraction as Q
from math import factorial
from exact_interval import I,SCALE
from native_sources import power_sums

ZERO=I.q(0)

def interval(pair):
    if type(pair) is not list or len(pair)!=2 or any(type(x) is not str for x in pair):
        raise TypeError('two exact rational strings required')
    a,b=map(Q,pair)
    if a>b:raise ValueError('reversed receipt interval')
    return I(I.q(a).lo,I.q(b).hi)

def pivots(s,d,shift):
    if type(d) is not int or d<1 or shift not in (0,1):raise ValueError('matrix protocol')
    a=[[s[i+j+shift] for j in range(d)] for i in range(d)];out=[]
    for k in range(d):
        p=a[k][k];out.append(p)
        if p.lo<=0:break
        for i in range(k+1,d):
            for j in range(i,d):
                a[j][i]=a[i][j]=a[i][j]-a[i][k]*a[j][k]/p
    return out

def positive(s,d,shift):
    out=pivots(s,d,shift)
    if len(out)!=d or any(x.lo<=0 for x in out):raise ArithmeticError('positive definiteness not certified')
    return [x.bounds() for x in out]

def solve(a,b):
    a=[list(row)+[bb] for row,bb in zip(a,b)];n=len(b)
    for k in range(n):
        pivot=next((i for i in range(k,n) if a[i][k]),None)
        if pivot is None:raise ArithmeticError('singular moment matrix')
        a[k],a[pivot]=a[pivot],a[k];v=a[k][k];a[k]=[x/v for x in a[k]]
        for i in range(n):
            if i!=k:
                v=a[i][k]
                if v:a[i]=[x-v*y for x,y in zip(a[i],a[k])]
    return [row[-1] for row in a]

def pade(f,d=8):
    s=power_sums(f)
    # These rational moments define the comparator, not the native source.
    u=[Q(((x.lo+x.hi)*10**60)//(2*SCALE),10**60) for x in s[:2*d]]
    h0=[[u[i+j] for j in range(d)] for i in range(d)]
    c=solve(h0,[-u[d+i] for i in range(d)])+[Q(1)]
    D=[(-1)**j*c[d-j] for j in range(d+1)]
    P=[sum((D[j]*(-1)**(k-j)*u[k-j] for j in range(min(k,d)+1)),Q(0)) for k in range(d)]
    for k in range(d,2*d):
        if sum((D[j]*(-1)**(k-j)*u[k-j] for j in range(d+1)),Q(0))!=0:
            raise ArithmeticError('exact Pade order failed')
    if min(D)<=0 or min(P)<=0:raise ArithmeticError('positive polynomial coefficients')
    ps=[positive([I.q(x) for x in u],d,shift) for shift in (0,1)]
    return {'variable':'t=w/200; approximates d/dt log Phi(i sqrt(200t))',
            'nodes':d,'rational_moments':list(map(str,u)),
            'D':list(map(str,D)),'P':list(map(str,P)),
            'positive_matrix_pivots':ps,
            'entire_lift_or_native_zero_exclusion_claimed':False}

def quadratic(s,x):
    return sum((x[i]*x[j]*s[i+j+1] for i in range(len(x)) for j in range(len(x))),ZERO)

def derive(gamma,theta,parameters):
    if set(parameters)!= {'scale','d','shift','vector'} or type(parameters.get('d')) is not int or parameters['d']!=7 or type(parameters.get('shift')) is not int or parameters['shift']!=1:raise ValueError('witness protocol')
    if type(parameters.get('scale')) is not int or parameters['scale']!=200:raise ValueError('scale')
    xs=parameters.get('vector')
    if type(xs) is not list or len(xs)!=7 or any(type(v) is not str for v in xs):raise TypeError('rational witness')
    x=list(map(Q,xs))
    f=[interval(v) for v in gamma['f']];g=[interval(v) for v in theta['f']]
    if len(f)!=15 or len(g)!=17:raise ValueError('complete coefficient scopes')
    s=power_sums(f);ts=power_sums(g)
    form=quadratic(s,x)
    if not form.inside('-0.000000000010843','-0.000000000010842'):
        raise ArithmeticError('native negative form not reconstructed')
    ps=pivots(s,7,1)
    if len(ps)!=7 or any(v.lo<=0 for v in ps[:6]) or ps[-1].hi>=0:
        raise ArithmeticError('F5 inertia (6,1) not certified')
    eps=Q(1,2**72);pert=[f[0]]
    for k,v in enumerate(f[1:],1):
        error=I.q(eps/Q(32)**(2*k)).hi
        pert.append(I(v.lo-error,v.hi+error))
    robust=quadratic(power_sums(pert),x)
    if robust.hi>=I.q('-0.00000000001').lo:raise ArithmeticError('robust finite-jet obstruction failed')
    theta_pivots=[positive(ts,8,sh) for sh in (0,1)]
    exponent=192
    errors=[Q(16,2**(3*exponent//4))*Q(3)**(2*k+1)/Q(2*k+1)+Q(factorial(2*k),2**590) for k in range(17)]
    tube=[g[0]]
    for k,v in enumerate(g[1:],1):
        er=1600*(I.q(errors[k]/factorial(2*k))+v*errors[0])
        tube.append(I(v.lo-er.hi,v.hi+er.hi))
    permanent=[positive(power_sums(tube),8,sh) for sh in (0,1)]
    return {'status':'PROPOSED_COMPONENTS_REVIEW_REQUIRED','rh_proved':False,
            'arithmetic_upper_bound_proved':False,'cofinal_dimension_growth_proved':False,
            'F5':{'raw_moment_degree':28,'scaled_hankel_dimension':7,
                  'scaled_hankel_shift':2,'negative_form':form.bounds(),
                  'shift_two_pivots': [v.bounds() for v in ps],
                  'shift_one_positive_pivots':positive(s,7,0),
                  'weighted_fit_radius':32,'weighted_fit_tolerance':str(eps),
                  'perturbed_form':robust.bounds(),
                  'native_zero_certificate_imported':False},
            'theta':{'raw_moment_degree':32,'matrix_dimension':8,
                     'shift_one_and_two_pivots':theta_pivots},
            'permanent_gamma':{'dimension':8,'every_N_at_least':str(2**exponent),
                     'stage_threshold_power_of_two':exponent,
                     'source_coefficient_tube':[v.bounds() for v in tube],
                     'shift_one_and_two_pivots':permanent,
                     'direct_gamma_evaluation_at_threshold':False},
            'native_theta_rational_comparator':pade(g)}
