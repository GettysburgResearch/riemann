# Independent review of the complete reunited Dirichlet series

**Verdict:** no load-bearing gap found in the source-conditional
continuation theorem in `DEFORMED_GAUSS_CONTINUATION.md`, Lemma 2.1 and
Theorem 4.1, at the content hashes below. The fixed-index extractions in
`EULER_DOMAIN_EXTENSION.md` also check at their stated scope. The complete
reunited object has the claimed normally convergent divisor
representation on its stated tube. Its proof does not require an angular
zero-free theorem. The separate uncompleted-series consequence does
require the companion angular reciprocal theorem.

**Review independence and method:** this review was performed by a
separate agent that did not write the proof files. The review reconstructed
the local algebra, completion, source functional equation, conductor
bounds, and summability domain. It was iterative: the reviewer sent the
author an equivalent half-space description of the domain, the
small-eta endpoint observation, and two notation clarifications, then
checked the resulting file. This is a substantive AI-agent review, not an
external human review or a formal proof certificate.

**Exact source state:** the repository base was PR #915 at
`9959364671f89b86f3992ec5ed5e19f804eb607b`. The new proof files were
uncommitted during this pass, so this report initially binds their
contents rather than a new head commit. A subsequent frozen-head receipt
must verify these hashes before claiming exact-commit coverage. A
load-bearing change requires a new affected-scope review.

**Source boundary:** the imported October 5 theta automorphy, cusp
Fourier support and coefficient bounds, and finite local transformation
identities are assumed at their physically retained source. Their
application here was checked; the complete upstream paper and its formal
implementation were not reverified. No higher moment, generalized
hierarchy, zero-free improvement, or proof of RH is approved by this
report.

## 1. Files and content identities

All paths in the first table are relative to this packet directory.

| File | SHA-256 |
| --- | --- |
| `DEFORMED_GAUSS_CONTINUATION.md` | `b01b17194884b3e2331d9f668ee71abb33a5e2f1e047d16cb2e906a1c5b32c81` |
| `EULER_DOMAIN_EXTENSION.md` | `56ab7e05b0fde19c82eeea5f274da212bf63f07ac084de1b08c3d8c48aa78a2a` |
| `HIGHER_ANGULAR_SECOND_MOMENT.md` | `82edbaed050710fcdbfa65c20a39cc83338e9f283473462c1756ea717f035959` |
| `OPPOSITE_DERIVATIVE_REFLECTION.md` | `9532f14dc452edf9a50e7ec905e0629c54d510fd9937c5d8c19bcf7dfb4e9ccb` |

The load-bearing inherited files, with paths relative to the repository
root, were also hashed directly from disk.

| File | SHA-256 |
| --- | --- |
| `standalone/2026-10-10-sextic-critical-core/REUNITED_RAMANUJAN_EULER_PRODUCT.md` | `6d1f0e01d8645972de0c38897e37633d8bfc70d193f6e279dcf8f33b0e992433` |
| `standalone/2026-10-10-sextic-critical-core/NEGATIVE_BRANCH_DIRICHLET_SERIES.md` | `025b1f9507f7aff3794d93e80a10337e61732944ec3ba1cb28107c8a7d59326e` |
| `standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex` | `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d` |

The primary paper is retained from OpenAI/math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`. The relevant source equations
were read directly: `eq:recip`, `eq:crt-a`,
`eq:theta-local-factors`, `eq:theta-support`,
`eq:theta-coefficient-bound`, `eq:theta-factorized-shifts`,
`eq:ray-local-transform`, `eq:theta-cusp-coordinates`,
`eq:ray-mellin`, `eq:theta-mellin-functional-equation`, and
`eq:dual-cusp-mellin-series`.

The full new joint-series file was reviewed. For the higher-angular
companion, this review reconstructs the plus derivative and its
normalization in Sections 1–2 and checks use of Theorem 6.2 as a named
source-conditional input in the uncompleted corollary. It does not
constitute a second independent verification of the full canonical
second-moment induction in that companion.

## 2. The fixed-index Euler extraction

Write x, y, z as in the proof, with z=qxy. The inherited local factors
are `(1-x+z)/(1-y)` away from n and
`(1+(q-1)x)/(1-y)` at an n-prime. I independently checked both by summing
the squarefree a choice and unrestricted b powers. In particular, the
q factor comes from the unnormalized Ramanujan contribution; inserting
another q to the power -1/2 would change the object.

The new quadratic extraction follows from the polynomial identity

\[
(1-x+z)(1-xz)-(1-x)(1+z)=x^2z-xz^2.
\]

The two error monomials require exactly the strict inequalities
`2 Re(w)+Re(v)>1` and `Re(w)+2 Re(v)>1` for normal convergence of the
prime sum. The remaining denominators 1-x and 1+z are nonzero when
Re(w), Re(v)>0. At primes of n the displayed finite factors cost at most
a fixed constant times `q^max(0,1-Re(w))`; the product of the fixed
constants is absorbed into `(Nn)^epsilon`. The uniformity in k and the
two imaginary parts follows from the same majorants.

The extracted L-functions have the signs and arguments asserted in the
paper: the mixed factor is a numerator of angular type -3 and the
new reciprocal is the finite-order factor at 2v. Its primitive finite
character is fixed; its k-dependent factors are literal Euler deletions.
The latter cannot be restored to one. The fixed-index vanishing at
v=1/2 when kappa squared is principal correctly multiplies first by the
old angular denominator, and does not make a claim about the infinite n
sum.

I also checked the successive extraction of the first J terms linear in
z. Its residual linear coefficient is `x^(J+1)/(1-x)`, while terms of
degree at least two in z have a uniformly bounded coefficient sum on
fixed positive real-part ranges. This proves the stated continuation for
Re(w)>0 and Re(v)>1/2, conditional only on the ordinary Hecke
continuation of its nonzero-angular numerator factors. The two
prospective contour comparisons include both angular numerator costs;
their scalar and conductor exponents are correct. They are not legal
contour shifts for the complete theta object.

## 3. The conditioned series is the actual completed theta series

The coefficient in the joint-series note is

\[
\mathfrak a_k(n)=\gamma_2(n)\rho(n)\vartheta(n)
                  \alpha(n)\chi_k(n)^3.
\]

The source CRT relation gives the phase `chi_m(d)^4` after writing
n=dm. The source reciprocity factor has values in {+1,-1}, so its fourth
power is one. Thus this is precisely the local j=4 twist at a prime of
d. The k primes have j=3. No extra moving finite character is hidden in
that identification.

The completion in equation (1.5) is also exact. The angular factor in
the squarefree coefficient has type +1; the full multiplier has angular
parameter +2 and is realized by one plus horizontal derivative. In the
cube coefficient the cubic d twist appears to the twelfth power. It is
the coprimality mask at d, including its zero value, while the other cube
factors are exactly alpha cubed, rho cubed, and chi_k cubed.

The pure plus derivative changes the angular phase of the cusp scalar
to alpha(c) squared and leaves its norm factor `(Nc)^(1-2s)` unchanged.
The constant Fourier term is annihilated at every cusp, giving the
entire Mellin continuation for each fixed k,d. The raw Fourier
normalization differs from the primary n,b Dirichlet normalization by
the fixed nonzero factor involving `i 3^(5/2) 27^s`. On a fixed real
strip this has no moving-conductor cost or exponential vertical
modulus. This verifies the use of the opposite derivative rather than
an unjustified change of the finite periodic multiplier.

All good k and d primes are forced active. Consequently the reduced
denominator is c_0 k d, with c_0 in the fixed bad-ray family. The source
finite local calculation groups the residue sums before taking absolute
values, so no factor Nk or Nd from the number of individual additive
translates is omitted. There is no growing choice of active subsets in
this conditioned family.

## 4. The left-line saving at d

This is the load-bearing analytic estimate. Let u=1+eta with eta>0.
From the actual cusp support and coefficient majorant, the unweighted
local n,b series is

\[
S_p(u)=\frac{1+q^{-u}}{1-q^{1/2-3u}}.
\]

This expression includes primes shared by n and b: their local
valuation is 3e+epsilon, with epsilon=0 or 1 and e>=0. A coprimality
condition between those indices would be incorrect.

The j=4 local Ramanujan factor has absolute value q to the power -1/2
when p does not divide the Fourier index and `(q-1)q^(-1/2)` otherwise.
Its exact local majorant is therefore

\[
q^{-1/2}\{1+(q-1)[S_p(u)-1]\}.
\]

The bracket is
`1+O_eta(q^(-eta))+O_eta(q^(-3/2-3eta))`. Multiplication over p|d
gives `(Nd)^(-1/2+epsilon)`, by separating the fixed set of small
prime norms. All other good-prime Euler factors have an absolutely
convergent product at u>1. The k factors have modulus at most one, and
the ramified cusp-index sum is a convergent geometric sum. Hence the
whole dual series, not merely an individual coefficient, has the
claimed d saving uniformly in k,d.

The functional equation consequently gives

\[
|\mathcal T_{k,d}(-\eta+it)|
 \ll Q^{1+2\eta}(Nd)^{1/2+2\eta+\epsilon}(2+|t|)^M.
\]

The gamma quotient, up to fixed normalization factors, is

\[
\frac{\Gamma(4/3-s)\Gamma(5/3-s)}
     {\Gamma(s+1/3)\Gamma(s+2/3)}.
\]

On a fixed negative real line Stirling's formula gives polynomial
modulus with exponent `2-4 Re(s)` at large height. The exponential
parts cancel. Neither this quotient nor `(Nc)^(-2it)` introduces a
hidden exponential vertical or conductor factor.

The right line Re(s)=1+eta has a uniform absolute Dirichlet-series
bound. Interpolating the two lines gives exactly the exponents written
in the proof. A holomorphic polynomial weight, chosen with its zeros
outside the strip, can absorb the vertical polynomial before applying
the strip theorem. The Mellin realization supplies the required finite
order. Its fixed-index growth constant does not become a new factor in
the boundary interpolation estimate. Taking eta small in terms of the
requested epsilon proves the piecewise A(sigma), B(sigma) bound,
including neighborhoods of sigma=0 and sigma=1. No absolute dual
convergence at u=1 is asserted or needed.

## 5. The cube factor cancels before continuation

The local n-prime ratio is

\[
1+h(p)=\frac{1+(q-1)x}{1-x+z},\qquad
h(p)=\frac{qx(1-y)}{1-x+z}.
\]

In the common initial region all relevant n,d,m,b sums are absolutely
convergent, so the divisor reindexing is legal. Completing G_(k,d)
introduces the d-deleted cube L-function. The original complete object
already contains the cube L-function without that additional d
deletion. Their ratio is precisely
`product_(p|d)(1-y_p)^(-1)`. It cancels the factor 1-y in h and leaves

\[
j(p)=\frac{qx}{1-x+z}.
\]

The final expression defines j by this right-hand side. It does not
divide by 1-y when that factor vanishes elsewhere. Therefore the
continuation of the complete object acquires no exceptional poles from
the cube reciprocal. This conclusion would be false for the bare
deformed Gauss sum, which lacks the original global cube factor.

The review checked all masks in this reindexing. Divisor sums are
explicitly restricted to squarefree d coprime to kS; `chi_m(d)^4`
enforces the m–d exclusion. The conditioned cube completion retains
the b–d mask, and the restoration quotient accounts exactly for the
cube terms that were present in the original full object. At a deleted
prime x=y=z=0, the old local factors are one and h=j=0. No original
prime intersection is silently discarded.

## 6. Local denominators and the joint holomorphy domain

Division by 1-x+z is safe in this argument because it is used only for
Re(w)>1 and Re(v)>1. For q>=2,

\[
|x|+|z|\le q^{-\Re w}+q^{-\Re v}<1.
\]

On a closed subtube with positive margins this has a uniform gap from
one. This restriction is stronger than the fixed-index Euler domain;
the proof correctly does not use the same division throughout that
larger domain.

The divisor summand is bounded by a constant times

\[
Q^{A(\sigma)+\epsilon}(2+|\Im s|)^M
(Nd)^{1-\omega-\sigma+B(\sigma)+2\epsilon}.
\]

The sum over integral ideals converges when
`omega+sigma>2+B(sigma)`. Expanding the maximum that defines B gives
exactly the three strict inequalities

\[
\omega+\sigma>2,\qquad
\omega+\tfrac32\sigma>\tfrac52,\qquad
\omega+3\sigma>\tfrac52.
\]

Adding omega>1 gives precisely Theorem 4.1's tube. It is convex and
connected, contains the initial region omega>1, sigma>1, and has
positive uniform summability margins on every closed subtube used in
the theorem. Thus the normally convergent holomorphic divisor sum is
the analytic continuation of the original complete object.

The old E_(k,1), L(v,kappa_k), and 1/L(w,chi-_k) are uniformly bounded
there by absolute Euler majorants. The k deletions remain inside those
literal functions. Their bounds and the bounds for j depend only on
the real parts, so the final polynomial factor need only involve
Im(s), while the estimate remains uniform in Im(w). This verifies the
two-variable vertical statement, not just a bounded-height version.

## 7. The uncompleted corollary has different dependencies

For the bare squarefree series, division by
`L_(S,kd)(3s-1/2,chi+_k)` is necessary. The stated angular reciprocal
theorem applies to this literal imprimitive L-function, including its
d mask. Its finite modulus has norm bounded by a fixed multiple of
QNd. It therefore costs only `(QNd(2+|Im s|))^epsilon` on a fixed
interior of the source-conditional zero-free half-plane.

The argument of that L-function satisfies

\[
3\Re s-\tfrac12>\tfrac{11}{12}
\quad\Longleftrightarrow\quad
\Re s>\tfrac{17}{36}.
\]

For 17/36<sigma<1 the same d summability calculation gives
`omega+3 sigma/2>5/2`, hence `Re(v)>1+3 sigma/2`. Its limiting v
boundary is 41/24. A neighborhood of sigma=1 with omega>1 connects
this representation to the initial absolute domain; there is no
disconnected continuation claim. The polynomial vertical estimates
give the asserted smooth individual Gauss bound with finitely many
weight seminorms. This corollary is conditional on the angular
reciprocal theorem, unlike the complete-object result.

## 8. What the reviewed theorem does not provide

For sigma<=0, the tube condition reduces to Re(v)>1. Its ideal-sum
majorant is `(Nd)^(-Re(v)+epsilon)`. At v=1 this is the harmonic
threshold, so this representation does not supply normal convergence
on or across that boundary. Even if kappa is nonprincipal, absence of
a pole in the displayed finite-order numerator would not by itself
repair this summability issue. If kappa is principal, its possible
residue cannot be computed by evaluating the unsummed divisor series
at v=1.

The kernel's first left pole occurs at t=-5/6, with t=s-1/2. Thus the
theorem's Dirichlet-series domain for arbitrary negative sigma is not
automatically a pole-free domain for the smoothed double Mellin
integral. The explicitly mentioned range -1/3<sigma<=0 stays before
that kernel pole, but a full contour application must still handle
the transforms and fixed-ray components.

Finally, combining the literal scalar with the left-line bound cancels
the Q powers exactly:

\[
Q^{2\sigma-1}\,Q^{1-2\sigma}=1.
\]

The remaining balanced-scale cost is `D^(Re(v)-2 sigma)` up to
epsilon losses. In the middle strip there remains `Q^sigma`; at
Q of order D cubed this is adverse. The new continuation therefore
does not establish the conductor saving required for the generalized
moment. Formula (6.4)'s row-phase cancellation is correct, but its
remaining correlated theta factor is not an independent Gauss series.

## 9. Independent checks and remaining review boundary

In addition to direct proof reconstruction, I ran an independent inline
standard-library Python calculation using sparse multivariate
polynomials with exact `Fraction` coefficients. It verified zero
polynomial residuals for the quadratic extraction, the n-prime ratio,
the cube-factor cancellation after z=qxy, and the j=4 local majorant
numerator. Exact rational arithmetic also verified the divisor
exponents, the thresholds 17/36 and 41/24, and the row-scalar powers.
All these checks passed. They are algebra checks, not authentication of
the imported theta theorem or evidence for an infinite moment bound.

I did not run the author's finite diagnostic as a substitute for these
arguments, rebuild Lean, review a new global RH argument, or certify a
new frozen repository head in this pass. The smallest load-bearing
analytic assertion is the uniform d to the power -1/2 saving for the
complete absolute dual series on each strict negative s line. It is
proved here from the imported support and coefficient interfaces by
the displayed positive Euler majorant. The other essential bridge is
the exact matching and cancellation of the original cube factor;
the local identities and zero masks establish that bridge at the
reviewed source.

**Accepted review scope:** the specified fixed-index Euler
continuations, the complete-object normal continuation and conductor
bound on Theorem 4.1's tube, and the separately conditional raw-Gauss
corollary. Any proposed extension through v=1 requires its own new
argument and review. The full fourth moment, the generalized 2k-th
moment hierarchy, and RH remain open.
