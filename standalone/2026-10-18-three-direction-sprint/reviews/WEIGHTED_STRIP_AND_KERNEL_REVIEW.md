# Review of the weighted-strip gate and the literal arithmetic kernel

Status: **internal analytic component review. Neither missing all-order
positivity nor a new zero-free region is approved.**

The coordinator read `theta/WEIGHTED_STRIP_GATE.md` at raw SHA256
`cb4ed852b031f6899d1d7717f491317fdde80b5938a511141ec6f0fe4d2b6ee5`.
The physical zero band and the common modulus gap give the stated
semialgebraic node region. The second node power controls the entire
positive-weight modulus mass through cos(4 arg z)>=1-8B^2/R0^2.
The disk united with the upper exterior half-plane is simply connected,
contains zero, and has no branch point of any admitted factor. The same
logarithm normalization and canonical bound therefore identify the limit
on the WHOLE domain. Hurwitz applies there.

The circle-node counterexample is also exact: discrete Fourier
orthogonality matches every specified jet with strictly positive weights,
while a single constant pays their full modulus mass. Its branch points
can obstruct a common domain from the Taylor disk to the exterior. Thus
moment matching plus a band and a modulus bound is insufficient without
the stated analytic identification condition. This is not a failure of
#1003's real-node theorem, where the imaginary-axis argument stays inside
one open half-plane.

The coordinator also reconstructed `theta/ARITHMETIC_STIELTJES_KERNEL.md`,
raw SHA256
`7258644891d1a1bf93ccf0551aae616c239e964587ff8ef71ebe627f63b5d8e2`.
The rational term of F'/F is 1/(x-1/4); both xi polynomial factors are
included. Gaussian subordination of the absolute Euler and digamma series
gives the displayed literal prime-power kernel, with all normalizations
and all prime powers retained. The digamma identity was read directly in
DLMF5.9.16. The u=0 subtraction justifies the delicate joint exchange.

For the far-prime bounds, on |z-y|=y/2 one has Re(1/z)>=2/(3y).
Cauchy and (i+j)!<=2^(i+j)i!j! give exactly C_y(P)^2. Integrating the
decreasing majorant after completing the square at log n=3y/2 gives
the stated full n>N tail and constant. The archimedean tail follows
from the same Cauchy estimate and the increasing derivative of
u/4+u^2/(24y). These bounds pay complete tails at the actual polynomial
coefficient resource; they do not determine the sign of the retained core.

Bernstein--Widder plus Stieltjes continuation makes complete monotonicity
of this literal kernel sufficient for RH; under RH the paired product
and Laplace uniqueness give its converse. This is classical spectral-zeta
and explicit-formula territory, credited in the note. The coefficient
moment formula now states its weighted-integrability hypotheses. The
negative factorial-kernel determinant correctly prevents inferring the
cumulant Hankel positivity from k>=0 alone.

The Rodgers--Tao deformation test was checked directly against their
primary paper, equations1--4 and Theorem1.1. Quadratic damping is negative
heat time, up to the positive variable rescaling. Their threshold theorem
therefore supplies a nonreal zero for every positive damping. Evenness,
positivity and the stated potential convexity survive that deformation.
Hence those generic theta properties do not furnish the missing arithmetic
positivity. No new proof of Rodgers--Tao or of that positivity is claimed.
