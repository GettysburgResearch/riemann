# Fixed Hankel dimension can hide off-real zeros at every row shift

Status: complete proposed analytic countermodel; independent review pending.
Scope: for EVERY prescribed finite dimension d, construct ONE positive Fourier
source whose complete shifted Hankel matrices of that dimension are positive
definite at EVERY nonnegative integer row shift, at one prescribed spectral
shift t0>A. The same source has off-real zeros, positive heat at every positive
time, and all scalar moments positive at every order and nonnegative spectral
shift. The source depends on d. No actual-Xi theorem or counterexample.
What was actually run: analytic derivation; no native numerical jobs.
Smallest remaining actual-source gap: control every matrix dimension, or another
literal theta/Euler statement that excludes this qualitative source.

Exact frozen dependencies:

- CA1–CA2 in ../COFINAL_MOMENT_OBSTRUCTION.md, SHA256
  7588200870a048a52a9da84cb884e3062808d0e36f9b25a978d449340b3e8d35:
  complete paired product, Bessel spectrum, simplicity, positive Fourier kernel.
- PF1–PF4 in ../HEAT_POSITIVE_FOURIER_COUNTERMODEL.md, SHA256
  7ca1093e7b239f3908ae5a4332b4b3432e05c50e3169abaf33424548a1307d24:
  complete spectral majorant, heat domination and scalar Gamma/Fubini transport.
- HC1–HC2 in ../HAUSDORFF_LOG_MOMENT_CRITERION.md, SHA256
  4f72ef0b7685bd0346f9c0d61b54819a2c7462de78d9620473cf07383ec9c54f:
  normalization of the complete shifted moment sequence.
- CS3 in ../COFINAL_RESIDUAL_SCALAR_CRITERION.md, SHA256
  a9471f13d2284d30a7456197fcb2292dd11defc4339729664ea011552df49550:
  positive Fourier convolution and one-occurrence multiplicity semantics.

The following matrix estimates and quantifier strengthening are supplied here.

## FD1. Exact quantifiers, source and moments

Fix a>0, A>0, t0>A, an integer d>=1, and a finite census height H0>=0.
Let

\[
 G_a(z)=K_{iz}(a)=\int_0^\infty e^{-a\cosh u}\cos(zu)\,du.
 \tag{FD1}
\]

Its complete positive zeros are distinct and simple,
0<gamma1<gamma2<..., and are all its positive-half-plane representatives.
They are the square roots of the positive Dirichlet eigenvalues of
-d²/du²+a²e^(2u) on the half-line. The dependencies prove the complete
spectral correspondence, simplicity, order at most one, and
sum gamma_r^(-2)<infinity. For any fixed ell>0 they also give

\[
 \gamma_r^2\le B^2r^2,\qquad
 B^2=(\pi/\ell)^2+a^2e^{2\ell}.
 \tag{FD2}
\]

For a sufficiently large real X, put L=pi/X and define

\[
 F_X(z)=\frac{G_a(z)}{G_a(0)}
             \frac{\cosh(LA)+\cos(Lz)}{\cosh(LA)+1}.
 \tag{FD3}
\]

Its real zeros are precisely the simple Bessel zeros. The additional complete
positive-half-plane representatives are

\[
 \rho_{j,\pm}=(2j+1)X\pm iA,\qquad j\ge0,
 \tag{FD4}
\]

all simple. There are no imaginary-axis roots; every zero lies in the strip
|Im rho|<=A. The Fourier kernel is a strictly positive cosh-weighted mixture
of the original Bessel kernel and its translates. Thus F_X is even real
entire of order at most one, with a strictly positive even Fourier kernel.
It has the complete paired product and retains all multiplicities.
Choosing X>H0 preserves the complete SIMPLE real census through H0.
This is not the literal theta kernel or Euler product of actual Xi.

Set c=t0²-A²>0. For every positive-half-plane source representative define
z_rho=c/(rho²+t0²). Define the complete REAL moments and d-by-d matrices

\[
 b_n=c^n\sum_{\operatorname{Re}\rho>0}
                 m_\rho(\rho^2+t_0^2)^{-n-1}
     =\frac1c\sum_{\operatorname{Re}\rho>0}m_\rho z_\rho^{n+1},
 \qquad
 H_n^{(d)}=(b_{n+i+j})_{0\le i,j<d},\qquad n\ge0.
 \tag{FD5}
\]

These are the normalized HC shifted logarithmic coefficients, not truncated
root sums. The complete sums converge absolutely: all nodes have modulus
less than one, and their absolute first-power sum is finite by the complete
inverse-square product. Conjugate grouping makes b_n and H_n^(d) real.
Entrywise and quadratic-form summation therefore retain every source node.

The claim is

\[
 \forall d\ge1\ \forall a,A,t_0,H_0\text{ as above}\quad
 \exists X:\quad H_n^{(d)}(F_X,t_0)\succ0
                       \quad\text{for EVERY integer }n\ge0,
 \tag{FD6}
\]

while F_X has the off-real lattice FD4. The choice of X may depend on ALL
fixed parameters, including d; t0 is fixed before X is chosen.

## FD2. A real Vandermonde head pays every polynomial of fixed degree

For r=1,...,d put

\[
 z_r=\frac{c}{\gamma_r^2+t_0^2},\qquad
 1>z_1>\cdots>z_d>0,\qquad
 v(z)=(1,z,\ldots,z^{d-1})^T.
 \tag{FD7}
\]

Let V be the real matrix whose r-th row is v(z_r)^T. Its determinant is
the nonzero Vandermonde product. Hence

\[
 \beta=\lambda_{\min}(V^TV)>0.
 \tag{FD8}
\]

This is a fixed mathematical constant independent of X. No numerical
approximation or certified value of beta is needed for the existence theorem.
If an explicit positive expression is desired, the eigenvalue product gives
the valid lower bound

\[
 \beta\ge
 \frac{\prod_{1\le r<s\le d}(z_r-z_s)^2}
      {\left(\sum_{r=1}^d\sum_{i=0}^{d-1}z_r^{2i}\right)^{d-1}}>0,
 \tag{FD9}
\]

with empty product and denominator power zero interpreted as one at d=1.

For every real q in R^d, the first d Bessel nodes alone contribute

\[
 \frac1c\sum_{r=1}^d z_r^{n+1}(q^Tv(z_r))^2
 \ge \frac{\beta}{c}z_d^{n+1}\|q\|_2^2.
 \tag{FD10}
\]

Every other real Bessel node contributes a nonnegative square. Therefore
FD10 is a lower bound for the COMPLETE real-node part, at every n>=0.
It is a relative bound that decays with n; no n-independent absolute
positive eigenvalue margin is asserted.

## FD3. The complete complex lattice is uniformly smaller

For a lattice node with x=(2j+1)X,

\[
 |\rho^2+t_0^2|\ge\operatorname{Re}(\rho^2+t_0^2)
                      =x^2+c.
 \tag{FD11}
\]

Consequently, setting alpha=c/(X²+c), one has

\[
 |z_{\rho_{j,\pm}}|\le\alpha<1,\qquad
 \sum_{j\ge0,\ \pm}|z_{\rho_{j,\pm}}|
 \le\frac{2c}{X^2}\sum_{j\ge0}(2j+1)^{-2}
 =\frac{c\pi^2}{4X^2}.
 \tag{FD12}
\]

The lattice matrix contribution is the complete conjugate-grouped real
symmetric matrix

\[
 E_n=\frac1c\sum_{j\ge0,\ \pm}
              z_{\rho_{j,\pm}}^{n+1}
                  v(z_{\rho_{j,\pm}})v(z_{\rho_{j,\pm}})^T.
 \tag{FD13}
\]

The transpose in FD13 is ordinary transpose. A complex node does NOT give
a Hermitian positive square. Instead, for real q, complex Cauchy–Schwarz
on the polynomial coefficients gives

\[
 |(q^Tv(z))^2|=|q^Tv(z)|^2
       \le\|q\|_2^2\sum_{i=0}^{d-1}|z|^{2i}
       \le\frac{\|q\|_2^2}{1-\alpha^2}.
 \tag{FD14}
\]

Thus absolute convergence, FD12 and FD14 pay the complete complex quadratic
form without assuming positivity of any individual complex contribution:

\[
 |q^TE_nq|
 \le \frac{\pi^2}{4X^2(1-\alpha^2)}
                       \alpha^n\|q\|_2^2.
 \tag{FD15}
\]

Choose X so large that all FOUR strict conditions hold:

\[
 X>H_0,\qquad X^2>4B^2+A^2,\qquad
 \alpha<z_d,\qquad
 \frac{c\pi^2}{4\beta z_dX^2(1-\alpha^2)}<\frac12.
 \tag{FD16}
\]

Such an X exists: the fixed beta and z_d are positive, alpha tends to zero,
and the last expression tends to zero as X tends to infinity. For every
integer n>=0, the ratio of FD15 to FD10 is bounded by

\[
 \frac{c\pi^2}{4\beta z_dX^2(1-\alpha^2)}
                    \left(\frac{\alpha}{z_d}\right)^n<\frac12.
 \tag{FD17}
\]

Combining the complete real and complex parts gives the simultaneous bound

\[
 q^TH_n^{(d)}q>
        \frac{\beta}{2c}z_d^{n+1}\|q\|_2^2
                   \qquad(q\ne0,\ n\ge0).
 \tag{FD18}
\]

This proves FD6 for infinitely many row shifts, using a single finite
dimension and one fixed source. Every smaller leading dimension is also
positive definite, as a principal submatrix.

## FD4. Simultaneous all-time heat and all-order scalar positivity

The second condition in FD16 is the complete PF heat-domination condition.
For every j>=0, the two distinct real nodes gamma_(2j+1), gamma_(2j+2)
have squares smaller than (2j+1)²X²-A² by FD2. Their heat contributions
strictly dominate the absolute heat contribution of the j-th complex pair.
Grouping the complete normally convergent series yields

\[
 K_{F_X}(u)>0\qquad\text{for EVERY }u>0.
 \tag{FD19}
\]

All source squared roots have strictly positive real part, because X²>A².
Complete absolute Gamma/Fubini transport then gives

\[
 C_k(F_X,t)=
 \sum_{\operatorname{Re}\rho>0}m_\rho(\rho^2+t^2)^{-k}
 =\frac1{(k-1)!}\int_0^\infty
                 u^{k-1}e^{-t^2u}K_{F_X}(u)\,du>0
 \quad(k\ge1,\ t\ge0).
 \tag{FD20}
\]

Thus the SAME X chosen in FD16 supplies every scalar order and every
nonnegative spectral shift, as well as the entire row-shift family at
dimension d and the fixed matrix spectral shift t0. No claim of all
matrix dimensions or all matrix spectral shifts is made.

## FD5. One fixed triple-root source masks every one-occurrence prefix too

For the same X in FD16, form the separate source

\[
 \widetilde F_X(z)=
       \left(\frac{G_a(z)}{G_a(0)}\right)^3
                  \frac{\cosh(LA)+\cos(Lz)}{\cosh(LA)+1}.
 \tag{FD21}
\]

It retains order at most one, the complete strip, absence of imaginary-axis
zeros, and a strictly positive even Fourier kernel: three Bessel kernels
are convolved, and the cosine multiplier is the same positive translation
mixture. The inherited CS3 convolution argument pays decay and convergence.
Every real Bessel root now has multiplicity THREE and still admits a strict
real sign crossing; the lattice roots remain simple and off-real.
This variant does not have a SIMPLE real census.

Let J be ANY finite set of distinct positive real Bessel roots and remove
ONE actual occurrence at each. Every real node then has remaining
multiplicity at least two. Its residual real matrix part therefore dominates
twice FD10. The unchanged lattice obeys FD15–FD17. Hence the COMPLETE
residual matrices obey, simultaneously for every such J,

\[
 q^TH_{n,J}^{(d)}q>
           \frac{3\beta}{2c}z_d^{n+1}\|q\|_2^2
           \qquad(q\ne0,\ n\ge0).
 \tag{FD22}
\]

Similarly the complete residual heat is
3K_G-sum_(r in J) exp(-gamma_r²u)+K_C >=2K_G+K_C>0.
Its every scalar moment at every nonnegative shift is strictly positive
by the same complete Gamma/Fubini argument. ONE fixed source therefore
masks the complex lattice after EVERY finite one-occurrence sign selection,
including all prefixes of a cofinal inventory of distinct real roots.
The unremoved real multiplicities violate occurrence exhaustion; they are
not silently identified with the empty real remainder.

## FD6. Exact boundary of the obstruction

The primary result has the order of quantifiers EVERY finite d, THEN SOME
source F_X(d), THEN EVERY integer row shift n. It does not provide one
off-real source passing every d. For each fixed off-real source, the complete
all-dimension Hankel criterion or its constructive finite negative-witness
version requires a negative finite matrix form at some larger dimension.
There is no contradiction: FD18 only fixes an initial finite dimension.

The triple-root variant adds EVERY finite one-occurrence sign prefix at
that same prescribed d. It does not exhaust every real occurrence and
does not pass complete SIMPLE-census exclusion guards through its triple
roots. Neither construction asserts a failure or success of a literal
actual-theta/Euler inequality. These qualitative hypotheses, together with
all scalar signs and all row shifts at one fixed matrix dimension, cannot
by themselves establish real location or cofinal SIMPLE census progress.
