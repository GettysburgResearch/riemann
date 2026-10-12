# Exact closed primitive synthesis after completed native acceptance

Status: candidate quantitative sharpening, pending independent review. The
previous completed certificate remains frozen and valid. This calculation
does not replace, integrate again, or alter any continuum source residual.

Let G h(t)=integral_0^t cosh((t-u)/2)h(u)du, and retain the exact real
native Galerkin tests z_i, their complete coefficient balls, U, and weighted
dual matrix B from the completed codimension14 receipt. The reviewed
QUANTITATIVE_PRIMITIVE_COMPLETION.md only needs a synthesis bound

    ||sum_i x_i G z_i||_2^2 <= K sum_i |x_i|^2.              (S1)

Hilbert-space Cauchy--Schwarz gives (S1) with
K=sum_i ||G z_i||_2^2, also for complex x_i. The earlier coarse K=2717696
used the unregularized high-sine coefficient absolute sums. Here the same
exact z_i have closed, smooth primitives, so the complete synthesis trace
can be enclosed directly.

## Complete primitive formulas

Put c=1/2, b=3/2 and a_n=n*pi. Exact convolution gives

    G sin(a_n t) = a_n/(a_n^2+c^2) [cosh(c t)-cos(a_n t)],
    G exp(c t)   = (t/2)exp(c t)+(exp(c t)-exp(-c t))/2,
    G exp(-c t)  = (t/2)exp(-c t)+(exp(c t)-exp(-c t))/2,
    G cosh(b t)  = (3/4)sinh(b t)-(1/4)sinh(c t).            (S2)

These identities can be checked by differentiating the convolution
initial-value equation, or by their exact Laplace transforms. Each vanishes
at zero with derivative equal to its input at zero. They cover all native
basis functions in the exact coefficient inventory: low sines, exp(+-t/2),
cosh(3t/2), and every one of the 100 high sines. No projected coefficient,
frequency tail, or low component is omitted.

Thus every G z_i is a linear combination of six soft functions

    exp(c t), exp(-c t), t exp(c t), t exp(-c t),
    exp(b t), exp(-b t),

and the complete cosines cos(n*pi*t), n=1,...,111. The corresponding exact
coefficient transformations are exactly (S2).

For F(z)=integral_0^1 exp(z*t)dt, the required whole integrals are

    integral soft_j*soft_k = F^(p_j+p_k)(r_j+r_k),
    integral soft_j*cos(n*pi*t) = Re F^(p_j)(r_j+i*n*pi),
    integral cos(n*pi*t)*cos(m*pi*t) = delta_nm/2.           (S3)

All p_j are zero or one, so only powers through two occur. The complete
removable formulas are

    F(z)   =(exp(z)-1)/z,
    F'(z)  =[exp(z)(z-1)+1]/z^2,
    F''(z) =[exp(z)(z^2-2z+2)-2]/z^3,
    F^(p)(0)=1/(p+1), p=0,1,2.                             (S4)

The entire F implementation and F' used in the original reviewed source
are retained; exact zero rates are handled explicitly. Formula (S3) pays
every mixed term and every pair of soft functions. The exact cosine
orthogonality pays all cosine pairs. Directed Arb multiplication encloses
all cancellation without replacing coefficient balls by midpoints.

## Acceptance and constant

The distinct enclose_exact_primitive_synthesis.py first checks the frozen
quantitative extractor hash and invokes its complete fresh weighted replay.
Every frozen residual/source/helper/trial hash, full coverage check, exact
weighted reserve and coefficient identity is therefore preserved. It then
reads that same authenticated coefficient inventory and evaluates (S2)--(S4)
at 256 bits. It requires every computed norm ball to be finite and positive.

The complete synthesis trace is enclosed near 0.51327163928410, strictly
below one. Therefore the simple exact integer K=1 is admissible in (S1).
The original completed scalar quantities remain M=1, epsilon=10^-11,
kappa=6/5, theta=1/200000000001. The same reviewed Young argument now yields

    delta=min[epsilon/(2(1+2K)),theta*kappa/2]
         =1/600000000000.                                  (S5)

At L=1,

    q_1(h,h)>=delta*(||Pi_E h||_2^2+||G h||_2^2).

Native zero extension gives q_L(h,h)>=delta*||G_L h||_2^2 for every complex
h in L2(0,L), every 0<L<=1. The primitive is injective. This improves the
previous completed quantitative constant while preserving precisely its
bounded-window scope. It proves no native L2 spectral gap, no sign at L>1,
and no RH conclusion. Acceptance still requires independent review of this
new finite synthesis computation and its completed outward receipt.
