"""Test every lattice center of selected Dwars curves at finite negative heat times."""
from flint import arb, ctx

ctx.prec = 128


def check(t, n, dimensionless_radius):
    a = -arb(t)/4
    delta = (arb(n+1)/n).log()
    radius = dimensionless_radius/delta
    bound = arb(0)
    cutoff = 128
    for m in range(1, cutoff+1):
        if m in (n, n+1):
            continue
        x = (arb(m)/n).log()
        y = (arb(m)/(n+1)).log()
        bound += (-a*x*y+radius*abs(x)).exp()
    # Past the cutoff each relative term is bounded by (m/n)^(-q).
    q = a*(arb(cutoff)/(n+1)).log()-radius
    if not q > 1:
        raise ArithmeticError("Tail integral diverges")
    bound += cutoff*(arb(n)/cutoff)**q/(q-1)
    central = 1+2*dimensionless_radius-dimensionless_radius.exp()
    if not bound < central:
        raise ArithmeticError("No strict two-term dominance on the test circles")
    print(f"t={t}, n={n}, inverse-coordinate radius={radius}, "
          f"error={bound}, boundary margin={central-bound}")


if __name__ == "__main__":
    check(-30, 1, arb(1)/20)
    check(-50, 1, arb(1)/100)
    check(-50, 2, arb(7)/50)
