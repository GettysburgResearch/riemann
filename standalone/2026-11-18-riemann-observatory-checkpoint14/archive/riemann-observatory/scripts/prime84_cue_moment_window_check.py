#!/usr/bin/env python3
"""Exact compression polynomial checks and direct finite rooted-CUE Taylor checks."""

import json
from fractions import Fraction
from math import factorial

import numpy as np
import sympy as sp
from numpy.polynomial import Polynomial


def symbolic_compressions():
    n, p, q = sp.symbols("n p q", integer=True)
    s = sp.symbols("s")
    mean = (n-1)/2

    def integral(poly, lower, upper):
        # Discrete sum by polynomial antiderivatives of 1, s, and s².
        primitives = (s+1, s*(s+1)/2, s*(s+1)*(2*s+1)/6)
        coeff = sp.Poly(poly, s)
        return sum(coeff.nth(j)*(a.subs(s, upper)-a.subs(s, lower-1))
                   for j, a in enumerate(primitives))

    diagonal = (p+q-n)*(1-n*n+2*n*(p+q)+2*p*p+2*q*q-8*p*q)
    cross = (p-q)*(p+q-n)/2
    for high, low in ((p,q), (q,p)):
        end = n-1-high
        assert sp.expand(integral(1,0,end)-integral(1,-low,-1)-(n-p-q)) == 0
        line = (s+p-mean)*(s+q-mean)
        assert sp.expand(12*(integral(line,0,end)-integral(line,-low,-1))-diagonal) == 0
        assert sp.expand(integral(s+q-mean,0,end)+integral(s+p-mean,-low,-1)-cross) == 0
        assert sp.expand(integral(s+p-mean,0,end)+integral(s+q-mean,-low,-1)+cross) == 0

    c, v, d, j2, j3 = sp.symbols("zc zs d J2 J3")
    u, w = c-sp.I*v, c+sp.I*v

    def moments(z):
        m1, b2, b3 = z*d/2, z*j2/2, z*j3/2
        return 1, m1, m1**2+b2, m1**3+3*m1*b2+b3

    left, right = moments(u), moments(w)
    d0 = 1-d*c
    d1 = sum(coef*left[i]*right[j] for (i,j),coef in
             sp.Poly((p+q-1)*(2*p*p-8*p*q+2*p+2*q*q+2*q-1),p,q).terms())
    d01 = sp.sqrt(3)*(left[2]-right[2]-left[1]+right[1])
    joint = d0**4+2*j3*c*d0-3*j2**2*v**2
    assert sp.expand(d0*d1+d01**2-joint) == 0
    # Endpoint with +n (one-sided total exactly the mode dimension) and -1.
    # T(z^n)=0, so the st coefficient of T(exp(sz^n+tz^-1))^-1
    # is exactly -T(z^(n-1)), whose compression is a single outer product.
    d00 = 1-(p+q)/n
    d11 = diagonal/(n*(n*n-1))
    d01 = sp.sqrt(3)*(p-q)*(p+q-n)/(n*sp.sqrt(n*n-1))
    exact = sp.Matrix(((d00,d01),(-d01,d11))).subs({p:n,q:1})
    v_first = sp.Matrix((1/sp.sqrt(n), -sp.sqrt(3)*(n-1)/(sp.sqrt(n)*sp.sqrt(n*n-1))))
    v_last = sp.Matrix((1/sp.sqrt(n), sp.sqrt(3)*(n-1)/(sp.sqrt(n)*sp.sqrt(n*n-1))))
    assert all(sp.simplify(entry) == 0 for entry in exact+v_last*v_first.T)
    assert sp.simplify(d00.subs({p:n,q:0})) == 0
    assert sp.simplify(d11.subs({p:n,q:0})) == 0
    print("Signed discrete compression polynomials and joint determinant verified")
    print("Exact signed-total n endpoint verified, including p=n and q=1")


def exponential_coefficients(log_coefficients):
    coefficients = np.ones(len(log_coefficients), dtype=complex)
    for i in range(1, len(coefficients)):
        coefficients[i] = sum(j*log_coefficients[j]*coefficients[i-j]
                              for j in range(1,i+1))/i
    return coefficients


def direct_moments(N, k, order, cosine, sine):
    """Use only the full compressed free-particle determinant, not the minor."""
    n, width = N+1, int(k[-1])
    harmonic = np.sum(1/k)
    coefficients = np.zeros(2*width+1, dtype=complex)
    coefficients[width+k] = -(cosine-1j*sine)/(2*k)
    coefficients[width-k] = -(cosine+1j*sine)/(2*k)
    mode = np.arange(n)
    offset = mode[:,None]-mode
    remove = np.column_stack((np.ones(n), mode-N/2))
    remove /= np.linalg.norm(remove, axis=0)
    projection = np.eye(n)-remove@remove.T
    operators = [np.eye(n)]
    power = np.ones(1)
    for j in range(1,order+1):
        power = np.convolve(power, coefficients)
        matrix = np.zeros((n,n),dtype=complex)
        inside = abs(offset) <= j*width
        matrix[inside] = power[offset[inside]+j*width]
        operators.append(projection@matrix@projection/factorial(j))
    inverse = [np.eye(n)]
    log_coefficients = np.zeros(order+1,dtype=complex)
    for j in range(1,order+1):
        log_coefficients[j] = sum(l*np.trace(inverse[j-l]@operators[l])
                                  for l in range(1,j+1))/j
        inverse.append(-sum(operators[l]@inverse[j-l] for l in range(1,j+1)))
    log_coefficients[1] -= cosine*harmonic
    values = exponential_coefficients(log_coefficients)
    assert max(abs(values.imag)) < 1e-12
    return [v*factorial(j) for j,v in enumerate(values.real)]


def surrogate(N, k, order, cosine, sine):
    n = N+1
    harmonic = np.sum(1/k)
    d, j2, j3 = len(k)/n, np.sum(k)/n**2, np.sum(k*k)/n**3
    linear = Polynomial((1,-d*cosine))
    t = Polynomial((0,1))
    prefactor = (linear**4+2*j3*cosine*t*linear
                 -3*j2*j2*(sine*t)**2-linear**2/n**2)/(1-1/n**2)
    exponent = np.zeros(order+1)
    exponent[1:3] = (harmonic*cosine,harmonic*(cosine*cosine+sine*sine)/4)
    values = np.convolve(prefactor.coef, exponential_coefficients(exponent)).real
    return [values[j]*factorial(j) for j in range(order+1)]


def crossing_correction(N, k, order, cosine, sine):
    n = N+1
    if order*k[-1] <= n:
        return 0.0
    assert (order-1)*k[-1] <= n
    one_step = np.zeros(int(k[-1])+1)
    one_step[k] = 1/k
    weights = np.ones(1)
    for _ in range(order):
        weights = np.convolve(weights, one_step)
    p = np.arange(n+1,len(weights))
    a = 2*(p-n)*(p*p+n*p-n*n+1)/(n*(n*n-1))
    multiplier = -2*((cosine+1j*sine)**order).real/2**order
    return float(multiplier*np.dot(weights[n+1:], a))


def case(N, a, b, order, cosine, sine):
    k = np.arange(int(a*N)+1, int(b*N)+1)
    direct = direct_moments(N,k,order,cosine,sine)
    formal = surrogate(N,k,order,cosine,sine)
    correction = crossing_correction(N,k,order,cosine,sine)
    expected = formal.copy()
    expected[-1] += correction
    error = max(abs(u-v) for u,v in zip(direct,expected))
    assert error < 5e-11
    return {"N":N,"band":[str(a),str(b)],"order":order,
            "cosine_weight":cosine,"sine_weight":sine,
            "direct_last_moment":direct[-1],"finite_surrogate_last_moment":formal[-1],
            "predicted_crossing_correction":correction,
            "maximum_discrepancy_through_order":error}


if __name__ == "__main__":
    symbolic_compressions()
    checks = []
    for order,a,b in ((4,Fraction(1,20),Fraction(1,10)),(5,Fraction(1,20),Fraction(1,10)),
                      (4,Fraction(13,50),Fraction(8,25)),(5,Fraction(41,200),Fraction(49,200))):
        for cosine,sine in ((1.0,0.0),(0.8,0.6)):
            checks.append(case(100,a,b,order,cosine,sine))
    for cosine,sine in ((1.0,0.0),(0.8,0.6)):
        checks.append(case(99,Fraction(4,25),Fraction(21,100),5,cosine,sine))
    print(json.dumps(checks,indent=2))
