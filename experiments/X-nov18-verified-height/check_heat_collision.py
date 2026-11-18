"""Enclose the new pair's double zero in heat time and ordinate by scalar xi samples."""
from math import factorial
from flint import acb, arb, ctx

# All decimals below denote exact inputs enclosed by Arb.
CENTER = "3000175351972.08258795570117635"
SCALE = "0.001434"
DEGREE = 48


def xi_coefficients():
    center, scale = arb(CENTER), arb(SCALE)
    s0 = acb(arb(1)/2, center)
    log_gamma = (s0/2).lgamma()
    zeta0 = s0.zeta()
    log_pi = arb.pi().log()
    values = []
    for j in range(DEGREE//2+1):
        node = (acb(0, 2*arb.pi()*j/DEGREE)).exp()
        if j == 0 or 2*j == DEGREE:
            node = acb(1 if j == 0 else -1)
        s = s0 + acb(0,8*scale)*node
        completed = ((s/2).lgamma()-log_gamma-(s-s0)*log_pi/2).exp()
        values.append(-s*(s-1)*completed*s.zeta()/(s0*(s0-1)*zeta0))
    values.extend(v.conjugate() for v in values[1:DEGREE//2][::-1])
    ratio = arb(1)/16
    alias = 10000*(arb("0.001")*128**2).exp()*ratio**DEGREE/(1-ratio**DEGREE)
    coeffs = []
    for n in range(DEGREE):
        phase = acb(0, -2*arb.pi()*n/DEGREE).exp()
        total = sum((values[j]*phase**j for j in range(DEGREE)), acb(0))/DEGREE
        if 0 not in total.imag:
            raise ArithmeticError("Conjugate scalar samples lost reality")
        coeffs.append((total.real+arb(0,alias.upper()))/8**n)
    return coeffs


def jet(coeffs, nu, z):
    if not (nu > 0 and nu < arb(".51") and abs(z) < arb(".1")):
        raise ValueError("Outside the certified heat tail domain")
    moments = [arb(1), z]
    while len(moments) < DEGREE:
        n = len(moments)-1
        moments.append(z*moments[n]+2*nu*n*moments[n-1])
    tail = 10000*arb(".097")**DEGREE/(1-arb(".097"))
    return [sum((coeffs[n]*moments[n-j]*(factorial(n)//factorial(n-j))
                 for n in range(j, DEGREE)), arb(0))+arb(0,(factorial(j)*tail).upper())
            for j in range(4)]


def main():
    ctx.prec = 224
    coeffs = xi_coefficients()
    nu, z = arb(".5"), arb(".0023")
    for _ in range(6):
        value, first, second, third = jet(coeffs, nu, z)
        det = second**2-first*third
        nu = (nu-(second*value-first**2)/det).mid()
        z = (z-(second*first-third*value)/det).mid()
    radius = arb("1e-23")
    error = arb(0,radius.upper())
    value, first, _, _ = jet(coeffs, nu, z)
    _, d1, d2, d3 = jet(coeffs, nu+error, z+error)
    # Residual map (nu,z) -> (nu,z) - (C,C_z)/2.
    lip = max(abs(1-d2/2)+abs(d1)/2, abs(d3)/2+abs(1-d2/2))
    if not (lip < arb(".1") and max(abs(value),abs(first))/2+lip*radius < radius):
        raise ArithmeticError("The heat double root has not been enclosed")
    backward_time = (nu+error)*arb(SCALE)**2
    ordinate = arb(CENTER)+(z+error)*arb(SCALE)
    print(f"backward time in Xi units: {backward_time}")
    print(f"double zero ordinate in Xi units: {ordinate}")
    print(f"rescaled contraction constant at most {lip}")


if __name__ == "__main__":
    main()
