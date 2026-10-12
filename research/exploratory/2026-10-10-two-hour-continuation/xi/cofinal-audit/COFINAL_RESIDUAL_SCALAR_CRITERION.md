# Cofinal residual scalar signs: occurrence exhaustion and the multiplicity trap

Status: complete proposed analytic criterion and fixed-source countermodel.
No actual-Xi all-prefix residual sign theorem or counterexample is asserted.
Scope: a complete even real source with fixed strip, no imaginary-axis roots,
summable inverse-square occurrences, and finite actual real removals. The
criterion requires exhaustion of ALL real occurrences, including multiplicity.
One strict sign interval per distinct real root does not supply that premise.
Exact dependencies: the complete heat/Laplace construction and explicitly
imported Bernstein–Widder theorem in `../COMPLETE_PRIME_HEAT_TRACE.md`, SHA256
`d48987c9143620d6b433163c080a89f3bc4966764d0880a83666a671fda3fb29`;
and PF1–PF4 in [HEAT_POSITIVE_FOURIER_COUNTERMODEL.md](HEAT_POSITIVE_FOURIER_COUNTERMODEL.md),
SHA256 `7ca1093e7b239f3908ae5a4332b4b3432e05c50e3169abaf33424548a1307d24`.
What was actually run: analytic derivation; no new native experiment.
Smallest remaining gap for a native cofinal result: establish the complete
all-prefix residual premise and occurrence exhaustion for the actual source.

## CS1. Exact cofinal criterion when all real occurrences are exhausted

Let a complete even real source have positive-real-part paired representatives
rho=x+iy with `|y|<=A`, positive integer multiplicities and no imaginary-axis
zeros. Assume `sum m_rho |rho|^-2<infinity`. The complete heat trace and its
derivatives converge normally on every compact positive-time interval.

Let E_N be nested finite multisets of ACTUAL real occurrences, each occurrence
removed at most once, such that every real occurrence is eventually in E_N.
Multiplicity is part of this exhaustion condition. Define

\[
 K_N(u)=\sum_{\rho\notin E_N}m_{\rho,N}e^{-\rho^2u},\qquad
 C_{k,N}(t)=\sum_{\rho\notin E_N}m_{\rho,N}(\rho^2+t^2)^{-k},
 \quad u>0,quad k\ge1,quad t>A.
 \tag{CS1}
\]

The notation means subtract the chosen number of real occurrences from
their original integer multiplicity; no nonreal occurrence is removed.
The complete absolute Laplace/Gamma interchange is valid for `t>A`, since
`t^2+Re(rho^2)>0` and the inverse-square sum pays the complete tail.

Under these assumptions the following are equivalent:

1. Every source zero is real.
2. `K_N(u)>=0` for EVERY N and EVERY u>0.
3. `C_(k,N)(t)>=0` for EVERY N, EVERY integer k>=1 and EVERY real t>A.

The inequalities permit a zero residual if the source has finitely many
zeros and all have been removed. No simplicity follows from this criterion.

Real location implies both sign families by positive complete sums. Statement
2 implies statement 3 by the exact Gamma/Laplace integral. For statement 3
implying statement 2, fix N and put

\[
 f_N(X)=C_{1,N}(\sqrt X),\qquad
 (-1)^r f_N^{(r)}(X)=r!C_{r+1,N}(\sqrt X),\qquad X>A^2.
 \tag{CS2}
\]

Complete normal convergence justifies the derivatives. Statement 3 makes
`h_N(z)=f_N(A^2+z)` completely monotone on z>0. Bernstein–Widder supplies
a positive measure nu with `h_N(z)=integral exp(-zu)dnu(u)`. The complete
source Laplace identity also gives

\[
 h_N(z)=\int_0^\infty e^{-zu}e^{-A^2u}K_N(u)\,du.
 \tag{CS3}
\]

For every z>0 the signed density has finite absolute exponential integral.
Multiply both measures by `exp(-z0 u)` for any z0>0 to obtain finite
measures. Uniqueness of their Laplace transforms identifies them, so
`e^(-A^2u)K_N(u)du` is positive. Continuity on u>0 then gives `K_N(u)>=0`
at EVERY positive u. No assertion that scalar signs at a single fixed t
would imply this statement is made; the all-shift quantifier is essential.

## CS2. A purely complex complete trace cannot remain nonnegative

Split the complete source into its real and nonreal occurrences. By the
occurrence-exhaustion premise, for each fixed u>0 the positive real remainder
in K_N tends to zero by dominated convergence. Thus statement 2 would imply

\[
 K_{\rm c}(u)=\sum_{\rho\ {m nonreal}}m_\rho e^{-\rho^2u}\ge0
                                       \qquad(u>0).
 \tag{CS4}
\]

Suppose the nonreal source is nonempty. Set
`sigma_rho=Re(rho^2)=x^2-y^2` and `tau_rho=Im(rho^2)=2xy`.
Since x>0 and y!=0, tau is nonzero. The complete strip and discreteness
make the minimum sigma0 among nonreal occurrences attained on a finite
nonempty block: only finitely many zeros have bounded x, while sigma tends
to infinity with x. Grouping conjugates, that block contributes

\[
       e^{-\sigma_0u}T(u),\qquad
       T(u)=2\sum_{j=1}^J m_j\cos(\tau_j u),\quad \tau_j>0.
 \tag{CS5}
\]

Combine identical positive frequencies. All coefficients are positive, so
T is nonzero. Its long-interval mean is zero and its mean square is
`q=2 sum_j m_j^2>0`, since distinct nonzero cosine frequencies have vanishing
cross averages. Let `M=2 sum_j m_j`, so `|T(u)|<=M`.

T has values strictly below `-q/(2M)` at arbitrarily large positive times.
Otherwise it would satisfy `-delta<=T(u)<=M` eventually, with
`delta=q/(2M)`. The pointwise inequality
`(T+delta)(M-T)>=0` would give
`T^2<=(M-delta)T+M delta`. Taking long-interval means gives
`q<=M delta=q/2`, a contradiction. This proof requires no commensurability
or unproved generic-frequency cancellation.

All remaining nonreal squared roots have real part separated from sigma0
by a positive gap c, if there are any remaining roots. The complete Gaussian
sum at u=1 is finite. For u>=1,

\[
 \left|e^{\sigma_0u}K_{\rm c}(u)-T(u)\right|
 \le e^{-c(u-1)}
     \sum_{\sigma_\rho>\sigma_0}m_\rho
                               e^{-(\sigma_\rho-\sigma_0)}\longrightarrow0.
 \tag{CS6}
\]

For a finite source with no remaining block this difference is zero.
Along the arbitrarily large negative times of T, CS6 makes K_c strictly
negative eventually. This contradicts CS4. Thus statement 2 forces the
nonreal source to be empty and proves all three equivalences in CS1.

In particular, if an off-real occurrence exists, some finite exhausted
real prefix and some positive heat time must have a negative residual K.
Statement 3 then fails at a finite scalar order and shift as well. Strict
continuity permits rational time or shift witnesses. This is a conditional
criterion, not a uniform algorithm for producing successful census guards.

## CS3. One occurrence per real sign interval can mask off-real zeros forever

Use the normalized Bessel source G_a and late cosine factor from PF1–PF4,
with `X^2>4B^2+A^2`. Form the ONE FIXED original source

\[
 F(z)=\left(\frac{G_a(z)}{G_a(0)}\right)^3
          \frac{\cosh(LA)+\cos(Lz)}{\cosh(LA)+1},
                         \qquad L=\pi/X.
 \tag{CS7}
\]

This source is even real entire of order at most one, with the complete
strip and no imaginary-axis roots. Its real Bessel zeros have multiplicity
THREE; every added lattice root `(2j+1)X+-iA` is off-real and simple.
Each real root still has strict opposite signs at sufficiently close real
endpoints, since the cubic preserves the odd sign crossing and the cosine
factor is positive on the real axis.

The original Fourier kernel remains strictly positive: multiplication of
three positive-kernel Bessel factors convolves their kernels, and the
positive cosh/translation mixture for the cosine factor preserves positivity.
Finite convolution preserves evenness and faster-than-every-exponential
decay. For example every exponential-weighted L1 and L-infinity norm of
the original kernel is finite, and convolution inherits those bounds.
Thus CS7 retains the qualitative positive Fourier property of the parent
countermodel, not merely its zero geometry.

Let J be ANY finite collection of distinct real Bessel roots and remove
ONE occurrence at each. The complete residual trace is

\[
 K_J(u)=3K_G(u)-\sum_{n\in J}e^{-\gamma_n^2u}+K_C(u)
                    \ge2K_G(u)+K_C(u)>0\qquad(u>0).
 \tag{CS8}
\]

The last strict inequality follows from PF3's complete all-time domination
`K_G>|K_C|`. Every squared source root has positive real part, so the
complete Gamma/Fubini formula makes EVERY scalar residual moment strictly
positive for EVERY k>=1 and EVERY t>=0, after EVERY such finite selection.
This includes every finite prefix of the same infinite strict-sign inventory.

Consequently, even one FIXED strictly positive Fourier source with cofinally
many real sign intervals and all-prefix ALL-order/ALL-shift residual scalar
positivity can retain off-real roots. Two real occurrences at every selected
node remain after the one-occurrence removal and violate the exhaustion
premise of CS1. A native simple-census exclusion guard would detect those
extra occurrences and could not be accepted below the first such root.

## CS4. The precise native cofinal boundary

If every real root is known simple and the strict-sign selectors cofinally
cover ALL real roots, one occurrence per interval does exhaust all real
occurrences, and the equivalence of CS1 applies. Without that simplicity or
an actual multiplicity-exhaustion mechanism, CS7–CS8 provide a countermodel.
Local simple-census guards establish simplicity only in their accepted
finite domains; their success cannot be inferred from scalar positivity.

The actual global theorem `K(u)>0` and all whole-source scalar signs uses
N=0 alone and does not supply the complete all-prefix residual premise.
The fixed-head countermodels also show why individual finite prefixes are
insufficient. The all-order mixed/Hankel and complete-monotonicity criteria
retain the missing complex spectral information. No actual universal
residual premise, real-root simplicity theorem or effective cofinal
progress schedule is claimed here.
