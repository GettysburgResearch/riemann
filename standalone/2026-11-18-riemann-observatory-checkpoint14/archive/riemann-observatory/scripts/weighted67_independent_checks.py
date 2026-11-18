from fractions import Fraction
from math import factorial

from flint import arb, ctx

ctx.prec = 128
pi = arb.pi()
ratio = arb(3) / 2
d = arb(2).log()
qs = [1 + arb(2).sqrt(), arb(2).sqrt() * d, arb(2).sqrt() * d**2]


def antiderivative(x, u, p):
    return x * sum(
        (-1)**k * (factorial(p) // factorial(p-k)) * u**(p-k)
        for k in range(p+1)
    )


def weighted_polynomial(T, U, M, center, j):
    p = 2*j
    left = -center
    middle = M.log() - center
    right = (2*M).log() - center

    dense_diag = (middle**(p+1) - left**(p+1)) / (p+1) + center**p
    if p:
        dense_diag += (-center).exp() * (p * arb(-1).exp())**p
    tail_diag = 2 * (right**(p+1) - middle**(p+1)) / (p+1)
    tail_diag += 8 * right**p / M
    diag = dense_diag + tail_diag

    correction = diag + antiderivative(2*M, right, p) - antiderivative(arb(1), left, p)
    correction += center**p + middle**p + 4 * right**p
    return (diag * (1/T-1/U) + 3*pi*correction/T**2).sqrt()


def norms(T, U, M):
    center = ((T*U).sqrt()/(2*pi)).log()/2
    beta = (U/T).log()/4 + 2/T
    theta2 = 1/T
    polynomial = [weighted_polynomial(T, U, M, center, j) for j in range(3)]
    # Retain both signed mode denominators, with a separate n=1 term.
    truncation = arb(7)/25
    velocity = arb('5.36')
    scale = truncation + 2/T + arb(1)/2 + velocity/pi*(
        1/(2*pi-velocity)+1/(2*pi)
        +(pi**2/6-1)*(1/(2*pi-velocity/2)+1/(2*pi))
    )
    errors = []
    for j, radius in enumerate([arb(0), arb(1)/6, arb(1)/3]):
        errors.append(
            scale * (arb('1.85')*radius/2).exp()
            * truncation**(radius-arb(1)/2)
            * T**((radius-1)/2) * (1/T-1/U).sqrt()
            * (factorial(j)/radius**j if j else 1)
        )
    p0, p1, p2 = polynomial
    e0, e1, e2 = errors
    g0 = p0 + qs[0]*e0
    g1 = p1 + beta*p0 + qs[0]*e1 + qs[1]*e0
    g2 = p2 + 2*beta*p1 + (beta**2+theta2)*p0 + qs[0]*e2 + 2*qs[1]*e1 + qs[2]*e0
    return g0, g1, g2


def residual_coefficients(V):
    # ||t^-1 G^(j)|| <= a[j] (log T)^(j+1/2) / sqrt(T).
    h = V.log()
    bnorm = (1+1/h)/2
    cnorm = ((1+5/h)/3 + (3*pi/h)*((h+5)/V + arb('0.56')+8/V)).sqrt()
    p0, p1, p2 = [bnorm**j*cnorm for j in range(3)]
    beta = ratio.log()/4 + 2/V
    e0, e1, e2 = [
        12*factorial(j)*3**j / (arb(3).sqrt()*V**(arb(1)/3)*h**(j+arb(1)/2))
        for j in range(3)
    ]
    g0 = p0+qs[0]*e0
    g1 = p1+beta*p0/h+qs[0]*e1+qs[1]*e0/h
    g2 = p2+2*beta*p1/h+(beta**2+1/V)*p0/h**2+qs[0]*e2+2*qs[1]*e1/h+qs[2]*e0/h**2
    return g0, g1, g2


def main():
    cutoff = 100
    initial = 10000-cutoff
    J = 32
    base = arb(initial)
    truncation = arb(7)/25
    rad = arb(1)/3
    assert (ratio+(rad+arb(5)/6)/base)/truncation < arb('5.36')
    assert (2*pi/(1-rad/base)).log()+pi/(base-rad)+1/base**2 < arb('1.85')
    assert (2*(truncation+1/base)*(2*pi/ratio.sqrt()).sqrt()).log() < arb(1)/2
    assert truncation**2*base > 1
    assert 1/base+pi/4 < 1
    squares = [arb(0)]*3
    for k in range(J):
        exact_T = Fraction(initial)*Fraction(3, 2)**k
        exact_M = Fraction(7, 25)*exact_T
        M = arb(-((-exact_M.numerator)//exact_M.denominator))
        T = arb(exact_T.numerator)/exact_T.denominator
        g = norms(T, T*ratio, M)
        squares = [total+gj**2 for total, gj in zip(squares, g)]
    V = arb(initial)*ratio**J
    h = V.log()
    a = residual_coefficients(V)
    for j in range(3):
        power = 2*j+1
        q = (1+ratio.log()/h)**power/ratio
        assert q < 1
        squares[j] += a[j]**2*h**power/V/(1-q)
    first = arb(initial)
    M = arb((7*initial+24)//25)
    b0, b1, _ = norms(first, arb(10000), M)
    g0, g1, g2 = (x.sqrt() for x in squares)
    f1 = g1+g0/first+arb(3)/(2*cutoff)*b0
    f2 = g2+2*g1/first+2*g0/first**2+arb(3)/cutoff*(b1+b0/first)+arb(6)/cutoff**2*b0
    tail = 2*f1*f2
    assert tail < arb('0.491'), tail
    assert arb('0.61649875288731141830')+tail < arb('1.10722')
    print(f'total analytic tail: {tail}')



if __name__ == '__main__':
    main()
