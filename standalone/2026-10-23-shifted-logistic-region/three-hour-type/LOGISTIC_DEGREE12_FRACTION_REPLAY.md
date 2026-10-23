# Exact rational replay of the degree-12 sufficient inequality

The independent checker `verify_logistic_degree12_fraction.py`, SHA256
`1e509ab10b892542c398f3e6110236a69ace4aca435c9cacd42a5949be7c3ae6`,
certifies the parent's degree-12 scalar inequality on the entire closed
rectangle

    0 <= A <= 200/963,       28 <= log(t) <= 823/10.

The candidate classical zero-free denominator is R=963/200=4.815.
No fixed-width boundary or RH conclusion is implied.

The scalar definition agrees term by term with
`../three-hour-root/certify_logistic_degree12.py`, SHA256
`350b5dc73787cb6f9925833e19ebaaa9256ed273c44da27e5bb35192be4a83f6`:
the exact degree-12 sum of two squares, K=12 in the height cutoff,
the new exact a1 and sum of cosine coefficients, Carch=-3.00317,
the curvature bound51, and the added margin1.57 eta-90 eta^3.
The latter consists of the separately proved prime gain
1.26 eta-90 eta^3 and the real-axis correction E_f<=-.31 eta.

The arithmetic engine is the SHA-pinned frozen baseline
`verify_logistic_master_fraction.py`, SHA256
`cefd18641114b6fedd8cf3334bcdd2857da7d4694bbbbc951238603e90fc2413`.
It uses only Python integers and Fractions, with outward rounding to
192 binary places after every operation. Trigonometric and exponential
values have explicit rational Taylor tails; logarithms use an atanh
series with its geometric tail. Kernel moments are computed by the
direct exponential power series, independently of the parent's
integration-by-parts recurrence. W is evaluated by a direct polynomial
sum, and J by its positive beta-integral series with an explicit tail.

Alternating rational coordinate bisection accepted70 rectangles after
139 evaluations. Their minimum rational lower margin is

    11048923424355295644315030313501218468228762418794545
    /6277101735386680763835789423207666416102355444464034512896

which exceeds1.76019e-6. Every rectangle is contained in the target
box, their interiors are pairwise disjoint, and their exact total area
is3620/321, the area of the target. Closed boundaries are included.
The deliberately unsupported point A=1/4, log(t)=82.3 is rejected
by a strictly negative upper bound. No floating-point value enters
an acceptance or coverage decision.

The checker also verifies eta<.0075, sigma>.99,
exp(21.233*(200/963))<82.3 and exp(28)<3*10^12.
These are the scalar domain checks required by the global wrapper;
they do not prove that wrapper's analytic premises.

The certificate `LOGISTIC_DEGREE12_FRACTION_CERTIFICATE.json` has SHA256
`56d17fffe63e61bb6724c5b90a4a89146ea31712ed65c73ca6922bff6f4765ad`.
The older R=4.84 and R=4.82 checkers and certificates remain unchanged.

This replay certifies the finite sufficient inequality. The logistic
explicit formula, zero-pair positivity, discarded-zero budget,
archimedean bounds, prime gain, finite RH verification, Littlewood
localization and minimum-zero argument remain separately reviewed
analytic dependencies.
