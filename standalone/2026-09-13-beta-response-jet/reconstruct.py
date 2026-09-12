"""BJR26 bounded reconstruction, not a machine proof of the analytic theorems.
No numerical package, zeta evaluator, supplied zero list or floating acceptance.
"""
from fractions import Fraction as Q
from math import comb, isqrt
import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from interval_core import I, C, S, pi_i, log_i, loggamma_psi

N_RESPONSE = 512
ROOT_LEFT = Q('13.7654722174')
ROOT_RIGHT = Q('13.7654722175')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def padd(a, b):
    z = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a): z[i] += v
    for i, v in enumerate(b): z[i] += v
    while len(z) > 1 and not z[-1]: z.pop()
    return z


def pscale(a, c): return [x*c for x in a]


def pmul(a, b):
    z = [Q(0)] * (len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): z[i+j] += v*w
    return z


def ppow(a, n):
    z = [Q(1)]
    for _ in range(n): z = pmul(z, a)
    return z


def evalp(a, x):
    z = Q(0)
    for c in reversed(a): z = z*x+c
    return z


def gamma_weight_certificate():
    # Exact integration of (r^5+4r^4)/(r+x)^8 on [1,4].
    # Common denominator is (x+1)^7 (x+4)^7.
    a, b = [Q(1), Q(1)], [Q(4), Q(1)]
    num = [Q(0)]
    for j in range(6):
        cj = [Q(0)] * (6-j)
        cj[5-j] = Q(comb(5,j)*(-1)**(5-j))
        if j <= 4: cj[4-j] += 4*comb(4,j)*(-1)**(4-j)
        difference = padd(pmul(ppow(a,7), ppow(b,j)),
                          pscale(pmul(ppow(b,7),ppow(a,j)), -1))
        num = padd(num, pscale(pmul(cj,difference), Q(1,j-7)))
    den_reduced = pmul(ppow(a,2),ppow(b,7))
    # 2/3 - B(x), put over 1680*(x+1)^2*(x+4)^7.
    numerator = pscale(padd(pscale(den_reduced,Q(16,3)),
                            pscale(pmul(num,[Q(2),Q(1)]),-1)),210)
    expected = [6092800,28331520,44026752,31552416,10918776,
                1539078,149127,124971,33600,1120]
    require(numerator == [Q(x) for x in expected], 'operator polynomial identity')
    require(all(x > 0 for x in numerator), 'global positive coefficients')
    # Independent finite evaluations of the antiderivative formula.
    for x in [Q(0),Q(1,8),Q(1,2),Q(1),Q(3),Q(16),Q(100)]:
        integral = Q(0)
        for j in range(6):
            cj = comb(5,j)*(-x)**(5-j)
            if j <= 4: cj += 4*comb(4,j)*(-x)**(4-j)
            integral += cj*((x+4)**(j-7)-(x+1)**(j-7))/Q(j-7)
        B = (1+x)**5*(x+2)*integral/8
        exact = evalp(numerator,x)/(1680*(x+1)**2*(x+4)**7)
        require(exact == Q(2,3)-B, 'operator antiderivative cross-check')
    # The beta identity in power-series coordinates (finite controls only).
    beta = Q(1)
    for j in range(21):
        if j: beta *= Q(2*j+9,2*j+14)  # (11/2)_j/(8)_j
        lhs = beta
        rhs = Q(1)
        for r in range(j): rhs *= Q(2*r+11,2*r+16)
        require(lhs == rhs, 'tilted beta moments')
    delta, ball = Q(1,4096), Q(1,64)
    linear = Q(2,3)+Q(25,24)*delta
    quadratic = Q(125,24)+Q(3125,384)*delta
    image = 11*delta+linear*ball+quadratic*ball**2
    lip = linear+2*quadratic*ball
    require(image < ball and lip < Q(5,6), 'analytic parameter ball')
    require(Q(4725,128)*(Q(4,5)**5)*Q(9,10)<11, 'weighted forcing at infinity')
    require(Q(64,70)<1, 'weighted forcing on first interval')
    require(Q(66*16*60,5040)<13, 'complete Mellin tail constant')
    force=Q(275,8)+22*Q(125,8)*33
    require(force==Q(91025,8) and force/Q(2,3)<18000, 'finite-iterate derivative forcing')
    require(33+1089*Q(125,8)<18000, 'finite-iterate product remainder')
    return {'majorant_numerator_ascending':expected,
            'majorant_denominator':'1680*(x+1)^2*(x+4)^7',
            'weighted_operator_cap':'2/3','forcing_cap':'11','response_cap':'33',
            'analytic_radius':str(delta),'analytic_ball_radius':str(ball),
            'ball_image_bound':str(image),'ball_lipschitz_bound':str(lip),
            'complete_mellin_tail_constant':13}


def endpoint_coefficients(N):
    # w(z)=(1-z)^(5/2) E[1-(1-W)z]^-5.
    a=[Q(1)]; v=[Q(1)]; w=[Q(1)]; beta=Q(1); derivative=[Q(0)]
    for j in range(1,N+1):
        a.append(a[-1]*Q(2*j-7,2*j))
        v.append((Q(7*j-2,4)*v[-1] -
                  (Q(6*j+3,8)*v[-2] if j>1 else 0))/j)
        w.append(((2*j+3)*w[-1]-2*v[-1]+a[-1])/(2*j-1))
        beta*=Q(2*j+3,2*(j+4))
        derivative.append(Q(0) if j==1 else 2*w[-1]/(1-2*beta))
    require(w[:4]==[Q(1),Q(0),Q(0),Q(-7,32)], 'actual W low coefficients')
    require(derivative[:4]==[Q(0),Q(0),Q(0),Q(-7,10)], 'native endpoint response jet')
    return derivative,a,w


def raw_endpoint_derivatives(N):
    # Independent fixed-moment differentiation, followed by finite Laguerre transform.
    k=Q(5,2); beta=Q(1); e=[Q(1),Q(1)]; de=[Q(0),Q(0)]
    for j in range(1,N+1):
        beta*=Q(2*j+3,2*(j+4))
        if j==1: continue
        W=Q(1-Q(1,2**(2*j-1)),2*j-1)
        conv=sum((e[i]*e[j-i] for i in range(1,j)),Q(0))
        dconv=sum((de[i]*e[j-i]+e[i]*de[j-i] for i in range(1,j)),Q(0))
        e.append(beta*conv/(1-2*beta))
        de.append((W-beta)*conv/(1-2*beta)**2+beta*dconv/(1-2*beta))
    ds=[2*sum((de[i]*e[j-i] for i in range(j+1)),Q(0)) for j in range(N+1)]
    return [sum(((-k)**i*comb(j+4,j-i)*ds[i] for i in range(j+1)),Q(0))
            for j in range(N+1)]


def coefficient_controls():
    n=40; direct,a,w=endpoint_coefficients(n)
    raw=raw_endpoint_derivatives(n)
    require(direct==raw,'independent raw-moment response')
    e=[Q(1)]; rr=[Q(1)]
    for j in range(1,n+1):
        e.append((2*j*e[-1]-2*Q(3,4)**j)/(2*j-1))
        rr.append(comb(j+4,4)*e[-1])
    for j in range(n+1):
        require(w[j]==sum((a[i]*rr[j-i] for i in range(j+1)),Q(0)),
                'independent original scale integral coefficients')
    # Check the finite fixed-point third moment and its derivative independently.
    for theta in [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]:
        a3=(30+theta)/160
        moment=6*a3*Q(7,5)/(1-2*a3)
        require(moment==21*(30+theta)/(5*(50-theta)), 'third fixed moment')
        deriv=Q(6,160)*Q(7,5)/(1-2*a3)**2
        require(deriv==336/(50-theta)**2, 'third response moment')
    return {'raw_moment_comparisons':n+1,'scale_integral_comparisons':n+1,
            'third_moment_parameter_cases':5,
            'first_response_coefficients':[str(x) for x in direct[:8]]}


def response_coefficient_l1_tail(N):
    # Tail j>N, split convolution at m=floor((N+1)/2).
    m=(N+1)//2
    require(m>=3,'tail starts after exceptional binomial signs')
    binomtail=Q(1)
    for j in range(1,m): binomtail*=Q(5-2*j,2*j)
    binomtail=abs(binomtail)
    return Q(16,5)*(Q(2047,11)*binomtail+
                    Q(23,4)*1024*comb(m+4,4)*Q(3,4)**m)


def endpoint_response(p,N=N_RESPONSE):
    coeff,_,_=endpoint_coefficients(N)
    term=C(1);total=C()
    for j in range(1,N+1):
        term=term*(j-1-p)/(j+4)
        total+=coeff[j]*term
    # |(j-p)/(j+5)| <=1 throughout p's rectangle once j>=N.
    min_a=Q(p.re.lo,S);abs_p_sq=p.re.abs_upper()**2+p.im.abs_upper()**2
    require(2*min_a+10>0 and (2*min_a+10)*N+25>=abs_p_sq,
            'Pochhammer tail ratio')
    error=response_coefficient_l1_tail(N)*term.abs_upper()
    return total.inflate(error),error


def qinterval(lo,hi):
    a=I.of(lo);b=I.of(hi)
    return I(a.lo,b.hi)


def decimal_enclosure(interval,digits=12):
    d=10**digits
    lo=(interval.lo*d)//S
    hi=-((-interval.hi*d)//S)
    return [str(Q(lo,d)),str(Q(hi,d))]


def native_response_and_drift():
    # Complete normalized raw-source response at two nonzero complex arguments.
    panels=[]
    for t in [4,8]:
        z,error=endpoint_response(C(Q(1,4),Q(t,2)))
        if t==4:
            require(z.re.lo>0,'positive actual logarithmic response at height 4')
        else:
            require(z.re.hi<0,'negative actual logarithmic response at height 8')
        panels.append({'s_real':'1/2','s_imag':t,'logarithmic_response':z.rec(),
                       'real_decimal_enclosure':decimal_enclosure(z.re),
                       'imag_decimal_enclosure':decimal_enclosure(z.im),
                       'complete_series_tail_upper':str(error)})
    pi=pi_i();lc=log_i(pi/15)
    endpoint_values=[]
    for t in [ROOT_LEFT,ROOT_RIGHT]:
        lg,_=loggamma_psi(C(Q(21,4),t/2),pi)
        phase=lc*t/2+lg.im-pi/2
        endpoint_values.append(phase)
    require(endpoint_values[0].hi<0 and endpoint_values[1].lo>0,
            'whole gamma phase root bracket')
    tbox=qinterval(ROOT_LEFT,ROOT_RIGHT)
    _,psi=loggamma_psi(C(Q(21,4),tbox/2),pi)
    slope=(lc+psi.re)/2
    require(slope.lo>I.of(Q(28,100)).hi,'whole interval phase slope')
    response,error=endpoint_response(C(Q(1,4),tbox/2))
    velocity=-response.im/slope
    require(velocity.lo>I.of(Q('2.08931')).hi and
            velocity.hi<I.of(Q('2.08932')).lo,'native zero velocity')
    return {'series_degree':N_RESPONSE,'complex_response_panels':panels,
            'gamma_anchor_zero_bracket':[str(ROOT_LEFT),str(ROOT_RIGHT)],
            'phase_minus_pi_over_2_at_endpoints':[x.rec() for x in endpoint_values],
            'whole_bracket_phase_slope':slope.rec(),
            'zero_initial_velocity':velocity.rec(),
            'velocity_decimal_enclosure':decimal_enclosure(velocity),
            'velocity_witness':['2.08931','2.08932'],
            'root_is_xi_zero':False,
            'critical_line_local_analytic_branch':True,
            'positive_parameter_interval_numerically_instantiated':False,
            'collision_sign_proved':False}


def reconstruct():
    result={'version':'BJR26-1',
            'status':'proposed components; analytic review required; RH not proved',
            'source_parent_pr':878,
            'source_parent_sha':'e28fd6c04d315c5f31f37b2240a263cd2e0cfeaf',
            'weighted_operator':gamma_weight_certificate(),
            'coefficient_checks':coefficient_controls(),
            'native_initial_response':native_response_and_drift(),
            'rh_proved':False,'unbounded_zero_confinement_proved':False,
            'native_double_collision_computed':False,
            'arithmetic':'exact Fraction + 512-bit outward integer intervals'}
    return result

if __name__=='__main__':
    print(json.dumps(reconstruct(),sort_keys=True,indent=2))
