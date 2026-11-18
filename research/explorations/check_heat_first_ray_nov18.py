"""Enclose the first zero of the analytically continued Polymath15 Fourier kernel."""
from flint import acb, arb, ctx

ctx.prec = 192
PI = arb.pi()
I = acb(0, 1)
J = 16
ERROR = 200000 * arb(17)**8 * (-arb(4)*17**2/5).exp()


def kernel(y, order=0):
    u = I*y
    z = (4*u).exp()
    first = (9*u).exp()
    second = (5*u).exp()
    total = acb(0)
    for n in range(1, J+1):
        p = PI * n**2
        q = p*z
        def factor(k):
            if order == 0:
                return 1
            if order == 1:
                return I*(k-4*q)
            return 16*q-(k-4*q)**2
        total += (-q).exp()*(2*p**2*first*factor(9)-3*p*second*factor(5))
    result = total + acb(arb(0, ERROR.upper()), arb(0, ERROR.upper()))
    if not result.imag.contains(0):
        raise ArithmeticError("Kernel on the imaginary axis must be real")
    return result.real


def main():
    ceiling = arb(321)/1000
    if not (PI*(4*ceiling).cos() > arb(4)/5 and ERROR < arb("1e-84")):
        raise ArithmeticError("Tail bound invalid")
    # Lower bound on each entire interval: no endpoint-only sampling.
    for j in range(3170):
        interval = (arb(j)/10000).union(arb(j+1)/10000)
        if not kernel(interval) > 0:
            raise ArithmeticError(f"Positivity fails at interval {j}")
    for j in range(3170, 3210):
        interval = (arb(j)/10000).union(arb(j+1)/10000)
        if not kernel(interval, 1) < 0:
            raise ArithmeticError(f"Derivative test fails at interval {j}")
    if not kernel(ceiling) < 0:
        raise ArithmeticError("No negative endpoint")
    lo, hi = arb(317)/1000, ceiling
    for _ in range(130):
        mid = ((lo+hi)/2).mid()
        value = kernel(mid)
        if value > 0:
            lo = mid
        elif value < 0:
            hi = mid
        else:
            raise ArithmeticError("Bisection sign unresolved")
    # After modular inversion at the cusp, the leading term controls the
    # entire remaining open interval. Check the constants at its left edge.
    Y = arb(345)/100
    P = PI/4
    if not ((PI/4+2*ceiling).tan()/2 > Y
            and 4*P**2-12*P/Y+(3+P**2)/Y**2 > arb(1)/50
            and 12*P*Y > 2*(3+P**2)
            and 1000*(9*P)**2*(-8*P*Y).exp() < 1
            and (arb(5)/3)**4*(-4*PI*Y).exp() < arb(1)/2):
        raise ArithmeticError("Modular cusp dominance failed")
    root = lo.union(hi)
    additive = kernel(root, 2)/(2*kernel(root, 1))
    print("first positive kernel root", root)
    print("limiting first-zero speed", 2*root)
    print("additive displacement", additive)
    print("derivative at the root", kernel(root, 1))


if __name__ == "__main__":
    main()
