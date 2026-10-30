#!/usr/bin/env python3
"""Exact rational checks for the reciprocal-density deconvolution countermodel.

The global inequalities are proved in report.md. Fraction comparisons below
check their algebraic constants; float grids are illustrative only.
No Riemann-zero or external proof certificate is produced by this program.
"""
from fractions import Fraction as Q
import json
import math
from pathlib import Path


def coefficients(a):
    den = a**4 + 4
    return (20*a/((1-a*a)*den), -4*a*a/(1-a*a),
            -a*a*(a*a+6)/den, -a*a*(2-3*a*a)/den)


def exact_checks():
    checks = []
    for a in (Q(1, 20), Q(1, 100), Q(1, 10**9)):
        A, B, C, D = coefficients(a)
        assert -a*A-B-C+D == 0
        assert (1-a*a)*B == -4*a*a
        assert -a*a*C-2*D == a*a
        assert 2*C-a*a*D == -3*a*a
        assert C*C+D*D == 10*a**4/(a**4+4)
        assert A >= 5*a
        assert 4*a*a <= -B <= 5*a*a
        assert C*C+D*D <= (Q(8,5)*a*a)**2
        assert (1-a)**2 >= Q(9,10)
        assert -2*a**3+8*a**4 <= -Q(8,5)*a**3 < 0
        checks.append({"a":str(a), "coefficients":[str(v) for v in (A,B,C,D)],
                       "TV_upper_bound":str(Q(11,20)*a),
                       "unnormalized_F_log_curvature_numerator_upper_bound_after_factor":str(-Q(8,5)*a**3)})
    R=1000
    # The h*G_R curvature remains positive at x=3*pi/2; Var(G_R)<=12/R^2.
    h_lower=Q(1,1500)
    eps0,eps1,eps2=(Q(k,5*R*R) for k in (33,39,51))
    curvature_lower=2*h_lower*h_lower-h_lower*(6*eps0+eps2+4*eps1)-eps0*eps2-eps1*eps1
    assert curvature_lower>0
    # After removing the second real factor the density remains negative at pi.
    second_removal_upper=-Q(1,110)+Q(9,R*R)
    assert second_removal_upper<0
    return {"status":"PASS", "exact_parameter_checks":checks,
            "entire_smoothing_scale":R,
            "smoothed_h_curvature_lower_bound":str(curvature_lower),
            "smoothed_second_removal_value_upper_bound":str(second_removal_upper),
            "method":"Exact Fraction arithmetic for algebraic bounds; e^5<150 and e^4<55 used as elementary analytic bounds in report."}


def f_derivatives(x,a):
    A,B,C,D=map(float,coefficients(Q(a)))
    a=float(a)
    z=complex(C,-D)
    return [(A*(-a)**j*math.exp(-a*x)+
             math.exp(-x)*(B*(-1)**j+(z*complex(-1,1)**j*complex(math.cos(x),math.sin(x))).real))/10
            for j in range(3)]


def main():
    out=exact_checks()
    a=Q(1,20)
    max_scaled=-math.inf
    for j in range(20001):
        x=j/100
        f,fp,fpp=f_derivatives(x,a)
        # Scale away the two leading exponential powers before tiny tails.
        if x<=40:
            max_scaled=max(max_scaled,(f*fpp-fp*fp)*math.exp((1+float(a))*x))
    out["illustrative_float_grid"]={"a":str(a),"x_range":[0,40],"step":0.01,
                                    "max_scaled_log_curvature_numerator":max_scaled,
                                    "proof_status":"not a certificate; global proof is algebraic"}
    path=Path(__file__).with_name('countermodel_results.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
