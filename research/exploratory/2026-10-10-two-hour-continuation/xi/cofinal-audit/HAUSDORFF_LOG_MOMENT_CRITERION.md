# A constructive Hausdorff criterion for the complete zero spectrum

Status: proposed complete global equivalence and finite negative-witness
mechanism. No all-order criterion is proved to hold for actual Xi here.
Scope: the complete shifted logarithmic moments of an even real entire
source of order below two, optionally after removing finitely many known
real occurrences. Integer multiplicities are retained; simplicity is not
assumed or concluded. For actual Xi the criterion is equivalent to RH.
Exact dependencies: the complete paired source product, classical complete
zero strip, and exclusion of purely imaginary zeros. Positive theta gives
the last input. The compact moment representation is proved below rather
than imported. The separate countermodel note supplies the finite-information
boundary; it does not replace the literal Xi source.
What was actually run: analytic proof. The accompanying exact rational
countermodel checker tests a different finite source, not actual Xi.
Smallest remaining gap: prove every displayed mixed inequality for the
literal actual source, or find a strictly negative authenticated one.

## HC1. Exact source, shifted coefficients and scaling

Let F be even and real entire, F(0)>0, of order less than two. Assume its
zeros lie in `|Im rho|<=A`, A>=0, and that `F(iy)>0` for every real y.
This excludes purely imaginary zeros. Represent every +/- zero pair by
the member with positive real part, retaining its conjugate separately
when distinct, and retain positive integer multiplicities. The complete
paired product is

\[
 F(z)/F(0)=\prod_{\operatorname{Re}\rho>0}
                    (1-z^2/\rho^2)^{m_\rho}.
\tag{HC1}
\]

As usual, order less than two gives absolute inverse-square convergence;
paired genus-one factors and evenness leave no unaccounted exponential
factor. Alternatively HC1 and that absolute convergence can be stated as
explicit source hypotheses.

An optional finite selection removes actual REAL occurrences together
with their negative reflections. If P is its paired polynomial, put
`h=F/(F(0)P)`. It is even entire, `h(0)=1`, and `h(iy)>0`; its remaining
zeros inherit the strip and their integer multiplicities. The whole-source
case is P=1. No uniqueness, simplicity or finite census is needed for this
optional removal; it removes exactly the specified occurrences.

Fix real t>A and put

\[
 c=t^2-A^2>0,\qquad L=1/c,\qquad
 \lambda_\rho=(\rho^2+t^2)^{-1}.
\tag{HC2}
\]

For every remaining source zero, `Re(rho^2+t^2)>=c` and hence
`|lambda_rho|<=L`. Also `sum m|lambda_rho|<infinity`: outside a finite
set, the denominator has absolute value at least `|rho|^2/2`.

Define the real complete moment sequence

\[
 a_n=\sum_{\text{remaining }\operatorname{Re}\rho>0}
                     m_\rho\lambda_\rho^{n+1},\qquad
 b_n=a_n/L^n,\qquad n\ge0.
\tag{HC3}
\]

Reality follows from complete conjugate grouping, and all sums converge
absolutely. These are literal complete logarithmic coefficients:

\[
 a_n=-(n+1)[w^{n+1}]
        \log\frac{h(i\sqrt{t^2-w})}{h(it)}.
\tag{HC4}
\]

Indeed HC1 gives the quotient product
`product(1-w/(rho^2+t^2))^m`. Evenness makes the square-root composition
branch independent as a function of w; its value at zero is one and its
local logarithm is well defined. Formula HC4 therefore has exactly the
normalization and sign displayed. For a finite selection it equals the
whole-source coefficient minus each full selected shifted inverse power.

For actual `F(z)=Xi(z)=xi(1/2+iz)`, one may evaluate the numerator using
`xi(1/2+sqrt(t^2-w))` by the functional equation. Since A=1/2 and t>A,
the expansion center has real part greater than one. Its finite coefficients
can be enclosed using the exact Gamma/zeta source and convergent directed
arithmetic. No root enumeration or finite zero-count theorem is required
in the whole-source version.

## HC2. Global criterion

For integers n,m>=0 define the finite mixed difference

\[
 D_{n,m}=\sum_{j=0}^{m}(-1)^j{m\choose j}\,b_{n+j}.
\tag{HC5}
\]

Then the following are equivalent:

1. Every remaining source zero is real.
2. `D_(n,m)>=0` for EVERY pair of integers n,m>=0.
3. There is a finite positive measure nu on [0,1] such that
   `b_n=integral x^n dnu(x)` for every n>=0.

For actual Xi, removal of finitely many already real occurrences does not
change this equivalence with RH. Multiplicities are permitted and remain
as positive integer weights. Unlike a cofinal SIMPLE census, this criterion
does not assert that real zeros are simple.

### Real spectrum implies every inequality

If rho is real, `0<lambda_rho<1/t^2<=L`. The positive measure

\[
             \nu=\sum m_\rho\lambda_\rho\,
                          \delta_{\lambda_\rho/L}
\tag{HC6}
\]

has finite mass and moments b_n. Consequently

\[
                 D_{n,m}=\int_0^1 x^n(1-x)^m\,d\nu(x)\ge0.
\tag{HC7}
\]

For a nonempty remaining real source every HC7 is STRICTLY positive:
all its nodes lie strictly between zero and one. The empty finite-source
remainder gives the zero sequence and satisfies the criterion vacuously.

### A constructive measure from the mixed inequalities

Assume all HC5 are nonnegative. Let the linear functional ell on real
polynomials be defined by `ell(x^n)=b_n`. For every N>=1 put

\[
 v_{N,l}={N\choose l}\,D_{l,N-l}\ge0,\qquad
 \nu_N=\sum_{l=0}^{N}v_{N,l}\,\delta_{l/N}.
\tag{HC8}
\]

Equivalently `v_(N,l)=ell(binomial(N,l)x^l(1-x)^(N-l))`.
The binomial partition of unity gives

\[
                        \nu_N([0,1])=b_0.
\tag{HC9}
\]

For fixed n<=N, the binomial falling-factorial identity gives EXACTLY

\[
 \sum_{l=0}^{N}\frac{(l)_n}{(N)_n}v_{N,l}=b_n,
\tag{HC10}
\]

where `(l)_n=l(l-1)...(l-n+1)` and the n=0 ratio is one.
One proof of the polynomial identity is to count ordered n-tuples of
successes in N independent Bernoulli trials. Applying ell then gives HC10.

For every l, the difference between `(l/N)^n` and `(l)_n/(N)_n` is at
most `n(n-1)/(2N)`. These are the probabilities that n samples all belong
to an l-element subset, with and without replacement; coupling the samples
changes an outcome only after a duplicate, whose probability is at most
the displayed union bound. Thus

\[
 \left|\int x^n\,d\nu_N-b_n\right|
                   \le b_0\,\frac{n(n-1)}{2N}.
\tag{HC11}
\]

Finite positive measures of bounded mass on the compact interval have a
weakly convergent subsequence. Let nu be a subsequential limit. Taking N
to infinity in HC11 gives every desired moment b_n. This proves (2)=>(3)
constructively. The measure is unique, since polynomials are uniformly
dense in the continuous functions on [0,1]. No source nodes have been
assumed positive in this construction.

### A positive measure forbids every nonreal source pole

The COMPLETE source meromorphic function is

\[
 G(z)=\sum_{\text{remaining }\operatorname{Re}\rho>0}
                      \frac{m_\rho}{\rho^2+t^2-z}.
\tag{HC12}
\]

It converges locally normally away from its poles. For a compact z set,
all sufficiently distant denominators dominate `|rho|^2/2`, and the
inverse-square source sum converges. Its poles have no finite accumulation.
At the pole `z=rho^2+t^2`, its residue is exactly MINUS the positive integer
source multiplicity. The map rho->rho^2 is injective on the open positive
real half-plane; duplicate occurrences add their positive multiplicities.
There is therefore no cancellation of a pole between distinct source nodes.

For |z|<1/L, absolute convergence and the geometric expansion give

\[
              G(z)=\sum_{n\ge0}a_n z^n
                  =\int_0^1\frac{d\nu(x)}{1-Lzx}.
\tag{HC13}
\]

The integral on the right is analytic on
`Omega=C\[1/L,infinity)`. That slit plane remains connected after deleting
the locally finite isolated source poles. Identity continuation therefore
makes the two sides equal there, starting with their common germ at zero.
If a remaining rho=x+iy had x>0 and y nonzero, its pole would have
imaginary part `2xy`, hence would be a NONREAL point of Omega. The integral
would be analytic across that point, whereas HC12 has residue `-m!=0`.
This is impossible. All remaining rho are therefore real, proving (3)=>(1).

The imaginary-axis exclusion is necessary. If it is dropped, extend the
pair convention to represent a purely imaginary +/- pair by its positive
imaginary member. Then `F(z)=1+z^2/d^2`, with `0<d<=A<t`, has purely
imaginary zeros and all HC5 nonnegative: its node `(t^2-d^2)^(-1)` is
positive and at most L.
Positive theta excludes exactly this otherwise undetectable possibility.

## HC3. Finite negative witnesses and the native boundary

If the remaining source contains an off-real zero, the equivalence proves
that SOME finite HC5 is strictly negative. This is stronger than a claim
of singularity at an infinite limit: failure of the universal nonnegative
criterion means failure at an actual pair of finite integer indices.
Every such witness uses only the finite coefficients
`a_n,...,a_(n+m)` and the known scale L.

When these coefficients admit convergent directed evaluation, a strictly
negative witness has a nonzero margin and can eventually be enclosed with
a negative upper endpoint. Enumerating pairs and precisions in a dovetailed
way is thus, IN PRINCIPLE, a finite refutation search for an off-real actual
source zero. This does not assert that one exists or that any existing
finite checker already performs the unbounded search.

Conversely, finitely many positive HC5 never prove the universal condition.
For the strictly positive Fourier countermodel `F_X` in the companion
`COFINAL_MOMENT_OBSTRUCTION.md`, fixed shifted logarithmic coefficients
tend to those of the all-real `G_a` as X tends to infinity. Every fixed
mixed HC5 for G_a is strictly positive by HC7. Therefore any prescribed
FINITE collection of these tests passes for sufficiently large X, even
though F_X has off-real zeros. The same applies to finitely many positive
definite moment matrices: the all-real base has infinitely many distinct
nodes, so a nonzero finite polynomial has a strictly positive square norm.

## HC4. An exact rational scalar-positive countermodel

For a small independently checkable illustration, take the finite source
with positive-half-plane zeros

\[
                    1,\quad 2+i/2,\quad2-i/2
\tag{HC14}
\]

and their negative reflections, all simple. Its even real polynomial
product has order zero, lies in the strip A=1/2, and is strictly positive
on the imaginary axis. This polynomial is not a positive Fourier theta
source; the infinite positive-kernel example above supplies that stronger
qualitative countermodel separately.

Every unshifted scalar moment is positive. The real node contributes one;
the complex inverse-square node is `(60-32i)/289` with modulus `4/17`.
Hence its kth moment is at least `1-2(4/17)^k>0` for every k>=1.

Set t=1 and L=4/3. The shifted nodes are

\[
 \lambda_0=1/2,\qquad \lambda_\pm=(76\mp32i)/425.
\tag{HC15}
\]

Their complex modulus is less than 1/5, since `16/425<1/25`.
Thus EVERY shifted scalar `a_n` is positive as well:
`a_n>2^(-n-1)[1-2(2/5)^(n+1)]>=2^(-n-1)/5`.
Yet the mixed criterion detects the off-real nodes at a finite order:

\[
 D_{0,31}=\tfrac12(5/8)^{31}
       +2\Re\left[\frac{76-32i}{425}
                      \left(\frac{368+24i}{425}\right)^{31}\right]<0.
\tag{HC16}
\]

Its value is approximately `-0.00023616985386171267`; the strict sign is
an EXACT rational predicate, not a floating-point calculation. The
accompanying checker compares the direct complex-node formula with the
binomial combination of the exact shifted moments and records the full
rational result. It also checks the structural norm bounds used for the
all-order scalar statements. No numerical actual-Xi or RH claim follows.

The remaining actual-source problem is precisely the infinite mixed
positivity theorem. Positive theta, positive complete scalar moments, and
a long finite set of positive mixed tests do not silently prove it.
