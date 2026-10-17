# Research synthesis: what to change after the theta bound reaches its ceiling

**Status: exploration supported by the companion proposed component proofs.**
The aim is a full RH/GRH argument. The outcome of this pass is a set of precise
alternative interfaces, an unconditional logarithmic Fourier consequence, and
two safeguards against false closure. No power-bound improvement is asserted.

## 1. What the latest work supplies, and what it does not

The relevant current objects are not interchangeable.

* OpenAI's September 30 quasi-RH manuscript asserts the `7/8` boundary for
  Dirichlet L-functions and finite-order Hecke L-functions over
  `Q(sqrt(-3))`. Its October 5 companion asserts `11/12` by a shorter route.
* Cureton--Thorner v2 asserts `31/32` for every Dedekind zeta function and
  finite-order Hecke L-function over every number field.
* The repository's latest draft, #959, proposes an all-field `11/12`
  composition using the CT source, higher-order large-sieve inputs and a
  numerator-family second mean. It remains proposed, not accepted or
  independently certified mathematics.
* OpenAI's ordinary two-point correlation manuscript has a quantitative
  theorem for fixed affine forms, with no claimed uniformity for growing
  coefficients. Its general corrected Elliott conclusion is qualitative.

These assertions were checked against pinned primary sources at the scope
recorded in SOURCES.md. None is treated as an available estimate on the
infinite-order angular character `eta=theta^6`. Full theorem reconstruction
and formal dependency audits were not performed.

In #959, the binding positive theta saving is

\[
\frac{1-\alpha}{6}-\frac{M-1}{2}<\frac1{12}
\]

under the admissible linked scales. Its complementary additive regime has the
same ceiling. Another density partition can refine a nonbinding error while
leaving this term intact. That observation is a limitation of those estimates,
not an arithmetic lower bound or a no-go theorem for other approaches.

The existing repository already contains Euler stripping, geometric
coefficient lifts, critical Gaussian energy, full norm-fiber covariance,
long-twist moments and fixed-affine transfers. Rephrasing them alone would
not be a new attack. The present pass focuses on operations before absolute
values, on the still-free Mellin coordinate, and on the literal prime-memory
source.

## 2. First priority: isolate the signed principal residue before freezing z

The Poisson source has more structure than the one-variable detector obtained
after taking two residues. The exact local principal calculation yields

\[
P(\xi,z)=
\frac{\zeta_F^S(6z)}{\zeta_F^S(6z+1)}
\frac{L_F^S(6\xi+6z-4,\eta)}{\zeta_F^S(\xi)}J(\xi,z).
\]

The companion proof identifies the normal-convergence and nonvanishing
domains of `J`, rather than silently deleting an Euler factor. It also keeps
the reciprocal factor `1/zeta_F^S(6z+1)`, whose zeros become poles if one later
pushes the z contour left.

For fixed real `z0>1/3`, write

\[
P(\xi,z_0)=C_{z_0}\frac{G_{z_0}(\xi)}{\zeta_F^S(\xi)}.
\]

Both `G_z0` and its inverse have absolutely summable ideal coefficients with
weight `(N n)^(-1/2)`. They are holomorphic and nonzero on
`Re xi>max(0,5/6-z0)`. Every hypothetical target zero to the right of `1/2`
therefore remains a pole of exactly its own multiplicity. The awkward
angular numerator cannot cancel it at these fixed projections.

This resolves one technical part of a different proof route: one can now
seek a square-root bound for a source with an already safe numerator. The
actual physical normalization is

\[
X^{1/2-z_0}Z^{z_0-1}
\sum_{\mathfrak n}a_{z_0}(\mathfrak n)
W_{z_0}(N\mathfrak n/Z)
\]

times a fixed nonzero scalar. The source paper's admissible profiles permit
nonzero pairings for fixed `z0` in `(1/3,1)`; `z0=1` is an inadmissible shortcut
because the annular Fourier pairing vanishes there.

The most economical choice for an initial attack is `z0=1/2`. The physical
`X` factor disappears, and the desired estimate becomes

\[
\left|\sum_{\mathfrak n}a_{1/2}(\mathfrak n)
W_{1/2}(N\mathfrak n/Z)\right|
\ll_{\varepsilon,F,S,W} Z^{1/2+\varepsilon}
\qquad\text{for every fixed }\varepsilon>0.
\tag{OPEN-PR}
\]

The weighted Gaussian Mellin transform has no zeros. Combined with the proved
noncancellation, this estimate would exclude all target zeros with real part
greater than `1/2`. A common-row signed energy estimate strong enough to imply
OPEN-PR would work as well, provided its measure and all nonunit masks are
retained.

**Why the argument stops here.** The existing theta bound controls the full
automorphic integral at linked physical scales. It does not control a chosen
principal residue of that integral. Large residues can cancel against other
parts. Extracting this term by absolute values or by an unjustified Mellin
projection would assume the needed bound. The invertible critical convolution
comparison also proves that mere selection of these completion coefficients
does not create square-root cancellation for free.

A useful next theorem would construct and bound that signed projection
directly on the automorphic side, with the actual source profiles and
horizontal tails. A calculation which only reoptimizes the old scalar
exponents does not address OPEN-PR.

## 3. Second priority: use the functional equation as a scattering operator

The inherited one-variable Euler stripping ratio is not arbitrary:

\[
R(s)=\frac{L(6s-2,\eta)}{L(6s-3,\eta)}.
\]

Completing the angular Hecke L-function gives the exact representation

\[
R(r+\tfrac12)=A(r)/\Theta(r),\quad
A(r)=C_\eta(3+6r)^{-g},\quad
\Theta(r)=\frac{\Lambda_\eta(6r)}{\Lambda_\eta(1+6r)}.
\]

The functional equation and paired Hadamard product prove that `Theta` is
inner in the right half-plane without putting its zeros on a line. This is
useful precisely because it avoids applying an unproved GRH statement to the
angular character.

On the critical boundary, the absolute value of `R` is known exactly. It is
a bounded smoothing multiplier on L2. For a causal Hardy input `F`, the
decomposition

\[
F=\Theta H+D,\qquad D\in H^2\ominus\Theta H^2
\]

separates the causal part from the anticausal defect after stripping.
Evaluation at any finite set of angular zeros gives an exact Gram lower bound
on that defect. This furnishes a checkable way to reject localizations that
have destroyed the angular nulls.

There are two viable research objectives here:

1. Construct a localization of the genuine source that preserves `Theta`
   divisibility and yields a controlled causal norm.
2. Retain the full model-space defect and prove an arithmetic bound for it,
   together with all residues of target-zeta poles and all localization tails.

Neither objective is proved. The source's two-sided Gaussian tail must be
decomposed honestly before using a causal Hardy theorem. Even exact angular
zero cancellation in an untruncated meromorphic formula does not prove Hardy
membership of the arithmetic source.

The elementary control in SCATTERING_CONTROL.md shows why this matters. With
`R_a(r)=(r+a)/(r-a)`, boundary multiplication is unitary, but the causal
solution for the input `1/(r+b)` includes a nonzero `exp(a u)` mode. Moving
the inverse line replaces that growing mode by an anticausal tail and leaves
the corresponding residue. Omitting it would manufacture a false stability
theorem. This control rules out that inference, not the scattering approach.

## 4. A third coordinate: exact prime-memory evolution

For the unchanged width-one native source `G(u)`, unique ideal factorization
and Gaussian differentiation give

\[
2G'(u)+uG(u)+
\sum_{\mathfrak b}\Lambda_F^S(\mathfrak b)
(N\mathfrak b)^{-1/2-it_0}G(u-\log N\mathfrak b)=0.
\]

Only prime powers appear in the outer sum; every composite Möbius cofactor
remains inside `G`. There is no averaging over the fixed height `t0` and no
replacement of distinct ideals by one norm representative.

The energy identity converts the target to a one-sided signed correlation:

\[
|G(U)|^2+\int_0^Uu|G(u)|^2du+\mathcal C(U)=|G(0)|^2.
\]

Thus the missing inequality

\[
\mathcal C(U)\geq-C_\varepsilon e^{\varepsilon U}
\quad\text{for every fixed }\varepsilon>0\text{ and all }U\geq0
\tag{OPEN-PM}
\]

would imply RH for the fixed field. A rigorous Gaussian bound controls the
entire omitted prime-memory tail for a cutoff
`P=ceil(exp(U+R))`, uniformly even for arbitrarily negative past times.

This is a genuine source identity with a finite approximation rule, but the
negative part of the correlation is not bounded by it. The positive memory
measure has infinite total mass. A termwise completion into squared
differences separates divergent sums and is invalid. At a finite cutoff,
using only total mass incurs an exponentially large cost on the logarithmic
horizon. An effective argument must retain signed arithmetic information.

## 5. Choose a boundary target that tolerates multiplicity

There is a stronger reason to reject a simple contraction argument for the
native reciprocal source. A zero of order `m` produces a pole of order `m`
in `e^(a z^2)/zeta_F^S(1/2+z+it)`. The finite Gram proof gives sharp limsup
energy growth of order

\[
U^{2m-1}\quad(\Re\rho=1/2),\qquad
e^{2\delta U}U^{2m-2}\quad(\Re\rho=1/2+\delta>1/2).
\]

Known unconditional multiple-zero theorems make `O(U)` native energy false
for many actual Dedekind sources. The distinction is exponential versus
subexponential growth, not boundedness versus growth. This conclusion
retains the literal coefficients and every separately fixed twist.

For a cleaner target use the prime discrepancy

\[
P_{a,t}(x)=\sum_{\mathfrak n}\Lambda_F^S(\mathfrak n)
(N\mathfrak n)^{-1/2-it}g_a(x-\log N\mathfrak n)
-\int_0^\infty e^{(1/2-it)v}g_a(x-v)\,dv.
\]

Its transform uses the logarithmic derivative, so every zero is a simple
pole whose residue is proportional to multiplicity. The explicit formula
retains all missing-Euler zeros and a left-line remainder; its Gaussian zero
sum converges absolutely. Under RH, its mean energy is exactly

\[
\lim_{U\to\infty}\frac1U\int_0^U|P_{a,t}(x)|^2dx
=\sum_{\rho=1/2+i\gamma\ \mathrm{distinct}}
m_\rho^2e^{-2a(\gamma-t)^2}.
\]

This gives a multiplicity-compatible target `P=O(1)`, equivalent to RH at
every separately fixed width and height. The criterion is a classical
explicit-formula reformulation, with exact Gaussian and finite-S bookkeeping
provided here. It is not an arithmetic proof of boundedness. It also does not
automatically bound the prime discrepancy convolved against the native
inverse source in OPEN-PM.

Gaussian damping explains why a small finite experiment is a poor global
test: a zero at ordinate far from the chosen height has an exponentially
suppressed coefficient. Changing width or a separately fixed height improves
local sensitivity but does not establish an all-height or all-scale bound.

## 6. What the Dirichlet correlation work can actually contribute

The exact completion identity is `F=a*b`, with native
`a(n)=mu(n)xi(n)1_((n,S)=1)`. For all four allowed coefficient families, `b`
and its convolution inverse have uniformly finite weighted mass at every
fixed exponent greater than `1/2`.

Additive phases therefore transfer exactly through

\[
\sum_{n\leq X}F(n)e(\alpha n)
=\sum_{d\leq X}b(d)
\sum_{r\leq X/d}a(r)e(d\alpha r).
\]

The dilation of the phase is essential. Applying established uniform
Davenport and Green--Tao estimates yields arbitrary logarithmic savings,
uniformly over all permitted powerful-prime profiles and degrees. Parseval
then gives a logarithmic saving in the full sum of squared correlations over
all shifts and in smooth signed filters of arbitrary growing width. This is
a quantitative consequence; it does not need an illicit fixed-form to
growing-form extension of the new correlation manuscript.

It does not close RH. The same invertibility transfers any hypothetical
power saving in the reverse direction to the native Möbius source. Nor do
generic nonpretentiousness and small individual correlations force a
square-root mean. The exact family `f_theta(n)=n^(theta-1)`, with
`1/2<theta<1`, is uniformly nonpretentious and has uniformly power-saving
shifted correlations, while its sum grows as `X^theta/theta`. Its complete
covariance stays coherent. This is a counterexample to that generic
bootstrap, not to a Möbius-specific theorem or to the cited papers.

## 7. Decision and stopping point

The free-`z` signed principal projection is the most direct new place to seek
an improved automorphic bound: it preserves the actual source and resolves
numerator noncancellation without a singular critical inverse. The scattering
description is a complementary operator route, with the exact lost component
identified. Prime-memory evolution and the logarithmic-derivative detector
provide calibrated arithmetic targets on which a proposed stability estimate
can be tested.

The missing work is an estimate such as OPEN-PR, OPEN-PM, or boundedness of
the prime detector. Each is explicitly at RH strength. No established input
in this pass supplies that estimate, and none of the finite checks substitutes
for it. The contribution is the proved interfaces and the elimination of
specific false shortcuts, together with an unconditional logarithmic
cancellation consequence. A full proof remains open.
