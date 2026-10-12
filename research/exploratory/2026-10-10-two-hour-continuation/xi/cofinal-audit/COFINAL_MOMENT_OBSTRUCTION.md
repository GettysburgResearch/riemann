# Whole logarithmic moments: exact cofinal scope and a positive-kernel countermodel

Status: proposed complete analytic obstruction and conditional mechanism.
Scope: even real entire sources of order below two, a complete horizontal
zero strip, one-occurrence real-root selections, and complete logarithmic
moments. The countermodel is not the literal Xi or theta source.
Exact dependencies: the complete paired product and one-occurrence semantics
in the frozen four-hour-wave `xi/outer-ray/HIGHER_MOMENT_CENSUS_RECOVERY.md`;
elementary Fourier identities, the displayed Bessel differential equation,
and separated one-dimensional selfadjoint spectral theory.
What was actually run: analytic derivation; no native numerical calculation
or root census is claimed by this note.
Smallest remaining gap for actual Xi: an actual-source theorem guaranteeing
successful exclusion guards at a cofinal sequence of heights. Qualitative
positive theta-kernel facts do not supply that theorem.

## CA1. Source and sharp angular horizon

Let F be even and real entire, F(0)>0, of order less than two. Its zeros
have integer multiplicities, lie in `|Im rho|<=A`, and have no purely imaginary
members. Represent every +/- pair by its member with `Re rho>0`, retaining
the conjugate member separately when it is distinct. Assume the complete
paired product

\[
 F(z)/F(0)=\prod_{\operatorname{Re}\rho>0}
                   (1-z^2/\rho^2)^{m_\rho}.
\tag{CA1}
\]

The inverse-square sum converges absolutely. The product follows from the
order bound: pairing genus-one factors cancels their linear exponentials,
and evenness removes the remaining degree-at-most-one exponential factor.

A selection removes one actual real occurrence from each of finitely many
disjoint positive real strict-sign intervals, together with its reflection.
Every other occurrence, including extra selected multiplicity, remains.
If an earlier complete SIMPLE census through R is explicitly imported,
and every low selected root is identified with its unique earlier root,
the entire unselected source has `|Re rho|>R`. Its complete moment is

\[
 T_k=-k[z^{2k}]\log(F(z)/F(0))
                 -\sum_{\text{selected }\gamma}\gamma^{-2k}
     =\sum_{\text{unselected }\operatorname{Re}\rho>0}
                  m_\rho\rho^{-2k}.
\tag{CA2}
\]

For R>0 and A>0, write `theta_R=atan(A/R)`. Every individual projection
in CA2 is strictly positive if

\[
                2k\theta_R<\pi/2.
\tag{CA3}
\]

This angular horizon is sharp for a theorem using only that support strip.
If `2k theta_R>pi/2`, choose an angle strictly between `pi/(4k)` and the
smaller of `theta_R` and `3pi/(4k)`. A point `x+iy` with x>R and
`0<y<=A` can have that angle, and its inverse-2k projection is negative.
Its conjugate gives the same negative real projection. At equality there
is no uniform strictly positive lower projection margin: admissible points
approaching the corner make that margin tend to zero. Thus the robust
allowable orders grow only as `pi R/(4A)` for large R/A.

The distinction is between positivity of EACH source projection and
positivity of their sum. All scalar complete T_k can be positive even in
the presence of off-real zeros; CA2 below gives an explicit example.

## CA2. A strictly positive Fourier kernel with late off-real zeros

Fix a>0 and define

\[
 G_a(z)=K_{iz}(a)=\int_0^\infty e^{-a\cosh u}\cos(zu)\,du.
\tag{CA4}
\]

The integral is entire, even and real. Its full Fourier kernel is
`e^{-a cosh u}/2`, strictly positive on the whole real line. On `|z|<=r`,
the absolute integral is bounded by
`integral_0^infty exp(-(a/2)e^u+r u) du`, which is at most a constant times
`(2/a)^r Gamma(r)` for r>=1. Therefore its logarithmic maximum growth is
`O(r log(r+2))`, so its order is at most one and in particular below two.

Every zero of G_a is real and simple, and its absolute value exceeds a.
Here is the spectral argument, including the point that excludes complex
order zeros. For any fixed z, the decaying function

\[
                   y(u)=K_{iz}(a e^u)
\]

satisfies

\[
 (-d^2/du^2+a^2e^{2u})y=z^2y,\qquad u\ge0.
\tag{CA5}
\]

The usual decaying K solution is nonzero and square integrable, together
with the required derivative and potential terms. If G_a(z)=0, it satisfies
the Dirichlet condition y(0)=0. Multiplying CA5 by its conjugate and
integrating gives

\[
 z^2\int|y|^2=\int(|y'|^2+a^2e^{2u}|y|^2)>a^2\int|y|^2.
\tag{CA6}
\]

Thus z^2 is real and strictly positive, and z is real with |z|>a.
The confining separated operator has discrete unbounded spectrum. At a
real zero, differentiating CA5 in z and applying Green's identity gives
`-y_z(0)y'(0)=2z integral y^2`, which is nonzero. The Dirichlet eigenfunction
has y'(0) nonzero; hence G_a'(z) is nonzero. This also proves simplicity
of the entire-function zeros rather than only simplicity of eigenvalues.

For a prescribed finite height B and any A>0, choose X>B, put L=pi/X,
and form

\[
 F_X(z)=G_a(z)\,
       \frac{\cosh(LA)+\cos(Lz)}{\cosh(LA)+1}.
\tag{CA7}
\]

Its Fourier kernel is

\[
 \frac{\cosh(LA)g(u)+[g(u-L)+g(u+L)]/2}{\cosh(LA)+1},
 \qquad g(u)=e^{-a\cosh u}/2.
\tag{CA8}
\]

This kernel remains strictly positive, even, and superexponentially
decaying. The source is even and real entire of order at most one.
The cosine factor is strictly positive on the real axis; its zeros are
exactly

\[
                     (2j+1)X\ \pm iA,\qquad j\in\mathbb Z.
\tag{CA9}
\]

They are simple because A>0. Hence every real zero of F_X is the same
simple real zero of G_a, while all off-real zeros occur after height X.
All source zeros lie in the strip `|Im rho|<=A`. Taking a larger than any
desired fixed seed radius also supplies a zero-free disk of that radius.
For every finite B one therefore has a complete SIMPLE real census through
B, a strictly positive entire Fourier source, and later off-real zeros.
No sound real-root exclusion guard can pass a height at or above X.

There is an even stronger scalar-moment statement. Let gamma_1 be the first
positive zero of G_a and take X>=2 gamma_1. The complete inverse-2k moment
of G_a is at least `gamma_1^(-2k)`. The absolute contribution of all
positive-half-plane cosine zeros is at most

\[
 2 X^{-2k}\sum_{j\ge0}(2j+1)^{-2k}
       \le (\pi^2/4)X^{-2k}.
\tag{CA10}
\]

Consequently EVERY scalar complete logarithmic moment of F_X is positive:

\[
 C_k(F_X)\ge\gamma_1^{-2k}(1-\pi^2/16)>0,
                         \qquad k\ge1.
\tag{CA11}
\]

Full scalar moment positivity, even at all orders, does not imply a real
zero spectrum. After removing any prescribed finite prefix of real roots,
the same argument works with the first remaining real root and X chosen
at least twice as large. Distant off-real nodes can remain hidden behind
closer real nodes in every scalar moment.

Finally, the normalized cosine factor in CA7 tends to one locally uniformly
as X tends to infinity. Thus F_X tends locally uniformly to G_a, with all
derivatives, while their real zeros are exactly identical. Any specified
finite collection of strict logarithmic-moment or finite-matrix inequalities
that passes for G_a also passes for sufficiently large X. This is a finite
information obstruction. The functions do not share the literal actual
theta identity, Euler product, or Dirichlet coefficients of Xi.

## CA3. Shifted moments bypass the angular cap but do not force progress

For fixed t>A define

\[
 M_k(t)=\sum_{\text{unselected }\operatorname{Re}\rho>0}
                     m_\rho(\rho^2+t^2)^{-k}.
\tag{CA12}
\]

It is an absolutely convergent complete source sum. The paired product gives
the exact branch-independent identity

\[
 M_k(t)=-k[w^k]\log\frac{F(i\sqrt{t^2-w})}{F(it)}
           -\sum_{\text{selected }\gamma}(\gamma^2+t^2)^{-k}.
\tag{CA13}
\]

Evenness makes the square-root composition single valued as a function of
w, and its value at zero is nonzero. The normalization and the factor -k
come directly from `log(1-w/(rho^2+t^2))` in the complete product.

For rho=x+iy, x>0 and |y|<=A, put D=rho^2+t^2. Its real part is positive,
and maximizing `2x|y|/(x^2+t^2-y^2)` in x and y gives the SHARP global bound

\[
                      |\arg D|\le\arcsin(A/t).
\tag{CA14}
\]

The maximizing point is `x=sqrt(t^2-A^2), |y|=A`. Thus every individual
projection in CA12 is positive if `k arcsin(A/t)<pi/2`, with no prior finite
census needed. Taking `t=2kA` supplies a strict uniform angular margin for
every k>=1. Any hypothetical remaining source root with `|Re rho|<=H`
contributes at least

\[
 \frac{\cos(k\arcsin(A/t))}{(H^2+t^2+A^2)^k}>0.
\tag{CA15}
\]

A strict directed upper endpoint for the COMPLETE M_k below CA15 therefore
proves the usual complete SIMPLE census, if the selection removes one
occurrence from every corresponding low real root. This is a valid positive
test family, not an unconditional source bound small enough for acceptance.

Increasing k with a fixed finite selection cannot make this family cofinal.
Here assume A>0; the zero-width case already has an entirely real spectrum
and does not admit this particular t-scaling. Assume the source has infinitely
many zeros, as Xi does. For `t=alpha k A`
with fixed `alpha>2/pi`, all projections are positive for sufficiently large
k, while every fixed unselected root satisfies

\[
 t^{2k}(\rho^2+t^2)^{-k}
                  =(1+\rho^2/t^2)^{-k}\longrightarrow1.
\tag{CA16}
\]

For any integer N, choose N remaining occurrences. Their real projections
in CA16 exceed 1/2 for all sufficiently large k, and every other projection
is nonnegative. Therefore

\[
                         t^{2k} M_k(t)\longrightarrow+\infty.
\tag{CA17}
\]

For fixed H, the CA15 threshold after the same normalization tends to
`cos(1/alpha)`, a finite positive number. Any genuine upper endpoint is at
least the exact real moment, so the exclusion guard eventually fails.
For real gamma, the normalized weight is approximately
`exp(-k gamma^2/t^2)` in the small-ratio region. Its resolution scale
`t/sqrt(k)` is therefore `alpha A sqrt(k)`, which GROWS with k.

There is also a necessary caution concerning a sharper corner formula.
Writing phi=arg D, differentiation gives

\[
 \partial_x\Re D^{-k}=-2k|D|^{-k-1}
          [x\cos((k+1)\phi)+y\sin((k+1)\phi)],
\]
\[
 \partial_y\Re D^{-k}=2k|D|^{-k-1}
          [y\cos((k+1)\phi)-x\sin((k+1)\phi)].
\tag{CA18}
\]

The stronger acute condition `(k+1)|phi|<pi/2` makes the x derivative
negative, but does NOT alone make the y derivative nonpositive. Near y=0
its sign is the sign of `t^2-(2k+1)x^2`. In particular, a sufficiently large
shift makes the function INCREASE with |y| near zero. A safe global lower
contribution is CA15; an exact corner improvement needs its own monotonicity
or minimization proof.

## CA4. Cofinal success has an exact conditional meaning

Consider real strict-sign selections that remove ONE occurrence per interval,
and successful complete-source exclusion guards at heights tending to
infinity. Such cofinal success implies that every source zero is real AND
simple. Indeed, any fixed off-real zero, omitted real occurrence, or extra
selected multiplicity is below one of those heights and contradicts that
guard. For actual Xi this is stronger than RH because RH does not assert
simplicity.

Conversely, assume that every source zero is real and simple and that its
analytic values admit convergent directed evaluation. Fix any t>A and use
k=1 in CA12. Select the first N positive real roots. Every simple root
admits arbitrarily narrow rational strict-sign intervals. As N grows,

\[
                       M_1(t)=\sum_{j>N}(\gamma_j^2+t^2)^{-1}\to0.
\tag{CA19}
\]

For any prescribed finite H avoiding selected root endpoints, the CA15 cost
is fixed and strictly positive. First choose N so that the exact tail is
less than half that cost, then refine the finite selected intervals and
the native coefficient sufficiently to obtain a strict upper endpoint
below the cost. Repeating at a cofinal choice of admissible rational heights
produces successful guards. Thus, with arbitrarily growing real selections
and precision, existence of a cofinal successful hierarchy is equivalent
to an entirely real SIMPLE spectrum. This is a conditional completeness
statement for the mechanism, not a proof of its successful continuation.

A classical density bound `N(u)<=C u log(e+u)` gives, under this entirely
real/simple hypothesis and a selection of ALL roots through B,

\[
 \sum_{\gamma>B}(\gamma^2+t^2)^{-1}
 \le 2C\,\frac{\log(e+B)+1}{B}.
\tag{CA20}
\]

This follows by Stieltjes integration by parts and
`integral_B^infty log(e+u)/u^2 du <= (log(e+B)+1)/B`.
It gives finite sufficient selections, roughly B of order `H^2 log H`
for the fixed first-moment kernel. The hypothesis that the selection has
removed ALL those occurrences is not available from sign existence alone.
An off-real root in CA7 prevents success above its own real part regardless
of arithmetic precision, real-root search extent, or choice of a sound
positive complete-source kernel.

## CA5. Boundary of the actual-theta conclusion

The actual positive theta kernel supplies `Xi(it)>0` and excludes purely
imaginary zeros. It does not, by its positivity alone, make logarithmic
cumulants into a positive moment measure of inverse squared zeros. CA7 has
the same qualitative positive Fourier property, strip, complete paired
product, arbitrarily long exact simple real prefix, and even positive
scalar moments at ALL orders, while retaining off-real zeros.

An additional theorem about the literal actual theta/arithmetic source may
distinguish Xi from these functions. A full mixed-moment positivity theorem
is one precise candidate; its infinite scope must be proved rather than
inferred from finitely many strict positive matrices. Alternatively, a
quantified actual-source tail bound guaranteeing a new complete exclusion
above every established census would be sufficient. Both are substantive
new source statements. The positive-kernel observation and finite moment
calculations do not already contain them.
