"""Prove a strong Lehmer-pair derivative inequality in the new high-zero census."""
import lzma
from pathlib import Path
from flint import acb, arb, ctx
from check_scalar_signs import exact_dyadic, hardy_sign

ANCHOR = 12_363_153_437_138
INDEX = 12_363_153_519_193


def check_pair_heat(h, B, center_height, slope):
    """Bound the Gaussian heat deformation of the pair-removed genus-one product."""
    radius = arb("0.003")
    final = h*h
    low = h*h*arb("0.999")/2
    high = h*h*arb("1.001")/2

    def error_coeff(vmax, size):
        denom = 1-8*B*vmax
        if not denom > 0:
            raise ArithmeticError("Gaussian majorant diverges")
        variance = 2*vmax/denom
        K = B*(arb(1)/2 + 2*B*size**2).exp()/(2*denom.sqrt())
        return K*(3*variance**2+h*h*variance), K*(size**2+6*variance+h*h)

    def error(vmax, size):
        a, b = error_coeff(vmax, size)
        return a+b*size**2

    if not error(final, radius) < radius**2-h*h:
        raise ArithmeticError("Local two-zero disk is not isolated throughout the heat interval")
    curvature_error = 2*error(final, 2*radius)/radius**2
    if not curvature_error < arb("0.1"):
        raise ArithmeticError("Failed uniform heat convexity")
    constant, quadratic = error_coeff(high, radius)
    if not (constant < arb("0.001")*h*h and quadratic < 1):
        raise ArithmeticError("Failed time bracketing at the moving minimum")
    small = arb("0.003")*h
    if not error(final, h+small) < small*(2*h-small):
        raise ArithmeticError("Failed isolation of the nonreal conjugate heat zeros")
    if not (low > arb("1.026e-6") and high < arb("1.030e-6")):
        raise ArithmeticError("Wrong stated time bracket")
    # At the moving minimum the derivative vanishes. Bound G'(0) by Cauchy,
    # then use the lower curvature already proved on the whole diameter.
    shift = error(high, radius)/radius/(2-curvature_error)
    collision_height = center_height-2*low.union(high)*slope + arb(0,shift.upper())
    final_center = center_height-2*final*slope
    stated_final = arb("3000175351972.0825943698701")
    if not abs(final_center-stated_final) < arb("1e-13"):
        raise ArithmeticError("Failed final real center")
    if not abs(collision_height-arb("3000175351972.082590")) < arb("0.000004"):
        raise ArithmeticError("Failed collision ordinate enclosure")
    print(f"pair-removed real logarithmic slope = {slope}")
    print(f"heat double zero ordinate = {collision_height}")
    print(f"final conjugate-disk real center = {final_center}")
    print(f"heat collision backward-time lower endpoint: {low}")
    print(f"heat collision backward-time upper endpoint: {high}")
    print(f"heat curvature error from 2: <= {curvature_error}")
    print(f"heat nonreal conjugate centers offset +/-i*h: {h}, disks radius {small}")


def main():
    ctx.prec = 160
    block, row = divmod(INDEX-ANCHOR, 10000)
    data = lzma.decompress((Path(__file__).parent/"blocks"/f"{block:04d}.xz").read_bytes()).splitlines()
    brackets = []
    for raw in data[row-12:row+14]:
        m,e,n,f = (int(value,16) for value in raw.split())
        brackets.append((exact_dyadic(m,e),exact_dyadic(n,f)))
    roots = []
    for text, archive in zip(("3000175351972.0811540487070886",
                              "3000175351972.0840218626952641"),brackets[12:14]):
        x = arb(text)
        a, b = x-arb("1e-15"), x+arb("1e-15")
        if not archive[0] < a < b < archive[1] or hardy_sign(a) == hardy_sign(b):
            raise ArithmeticError("Fails scalar refinement of indexed bracket")
        roots.append((a,b))
    left,right=roots[0][0],roots[1][1]
    delta=right-left
    r=arb(3)/2
    # Full-strip Poisson mass and shifted logarithmic derivative, uniformly
    # for every real t in the refined interval.
    t=left.union(right)
    s=acb(2,t)
    elementary=1/s+1/(s-1)-arb.pi().log()/2+(s/2).digamma()/2
    # sum Lambda(n)/n^2 <= sum (log n)/n^2 < 2
    poisson=elementary.real+2
    horizontal=abs(elementary.imag)+2
    local=arb(0)
    for lo,hi in brackets[:12]:
        local+=1/(left-hi)**2
    for lo,hi in brackets[14:]:
        local+=1/(lo-right)**2
    R=min(left-brackets[0][1],brackets[-1][0]-right)
    if not R>0:
        raise ArithmeticError("No verified separation to remaining ordinates")
    square_sum=local+(1+4/R**2)*poisson
    first_derivative=horizontal+delta/r**2+r*(square_sum*poisson).sqrt()
    gbar=2*delta**2*square_sum
    strong=8+delta**2*(8*square_sum+2*first_derivative**2)
    for name,value in (("gap",delta),("Poisson mass",poisson),
                       ("sum of outer inverse squared distances",square_sum),
                       ("absolute all-zero Lehmer statistic",gbar),
                       ("strong Lehmer derivative statistic",strong)):
        print(f"{name} <= {value}")
    if not (poisson<16 and gbar<arb("0.00134") and strong<arb("8.057") and strong<arb(42)/5):
        raise ArithmeticError("Lehmer criteria are not certified")

    # A nearby zero of zeta', without assumptions about the remaining zeros.
    dlow=roots[1][0]-roots[0][1]
    gap=dlow.union(delta)
    half_gap=gap/2
    center_height=((roots[0][0]+roots[1][0])/2).union((roots[0][1]+roots[1][1])/2)
    mid=acb(arb(1)/2,center_height)
    E=1/mid+1/(mid-1)-arb.pi().log()/2+(mid/2).digamma()/2
    radius=arb("0.0001")
    outside_distance=min(left-brackets[11][1],brackets[14][0]-right)
    if not outside_distance>radius:
        raise ArithmeticError("Missing zero-free collar")
    Gprime=square_sum/(1-radius/outside_distance)**2+1
    Gmax=first_derivative + delta*square_sum/2 + abs(E) + radius*Gprime
    root_radius=Gmax*(radius**2+half_gap**2)/2
    if not root_radius<radius:
        raise ArithmeticError("Rouche comparison failed")
    real_error=(Gprime*root_radius*half_gap**2+Gmax*root_radius**2)/2
    leading=half_gap**2*E.real/2
    realpart=arb(1)/2+leading+arb(0,real_error.upper())
    if not (realpart>arb("0.500013") and realpart<arb("0.500015")):
        raise ArithmeticError("Certified derivative zero missed its stated strip")
    print(f"zeta prime unique zero radius around midpoint <= {root_radius}")
    print(f"real part of derivative zero: {realpart}")


    # Refine the derivative zero with scalar zeta only.  G is the logarithmic
    # derivative after removal of the pair, so its integral is a principal log.
    h=arb(2)**-38
    contraction=radius*Gmax+(radius**2+half_gap**2)*Gprime/2
    if not contraction < arb("0.01"):
        raise ArithmeticError("No local fixed-point contraction")
    trial=mid.mid()
    for _ in range(6):
        z=trial-mid
        if not abs(z)+h < radius:
            raise ArithmeticError("Scalar probes leave the proved disk")
        pair_poly=z*z+half_gap**2
        step_ratio=1+(2*z*h+h*h)/pair_poly
        log_ratio=((trial+h).zeta()/trial.zeta()/step_ratio).log()/h
        derivative_error=(h*Gprime/2).upper()
        Gval=log_ratio+acb(arb(0,derivative_error),arb(0,derivative_error))
        if _ == 0:
            # i*(log xi/p)' at the exact pair midpoint is real; the trial
            # differs from that midpoint only by the enclosed root errors.
            slope_error = ((Gprime+1)*abs(z)).upper()
            slope = -(Gval+E).imag + arb(0,slope_error)
            check_pair_heat(half_gap, square_sum, center_height, slope)
        image=-pair_poly*Gval/2
        certified_error=abs(z-image)/(1-contraction)
        stated=acb(arb("0.500013823730388624"), arb("3000175351972.082587159392354416"))
        if certified_error+abs(trial-stated) < arb("2.3e-15"):
            print(f"refined derivative zero center = {trial}; absolute error <= {certified_error}")
            break
        trial=(mid+image).mid()
    else:
        raise ArithmeticError("Insufficient contraction residual")


if __name__=="__main__":
    main()
