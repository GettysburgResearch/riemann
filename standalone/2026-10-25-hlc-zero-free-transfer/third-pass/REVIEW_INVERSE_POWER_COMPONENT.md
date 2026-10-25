# Independent review of the enlarged native inverse component

**Verdict: PASS within the explicitly imported analytic framework.** I
independently checked the main coherent component theorem, its exact
compatibility with the sufficient tail hypothesis, and the separate
adjustable-floor deduction in Section 6. I found no remaining mathematical
issue in the reviewed bytes. The one precision correction requested during
review—the height factor in the adjustable-floor detector error—has been
applied and checked below.

This review does not independently prove the external Hecke cap, density
theorem, or ordinary product moment. It accepts them only in their stated
finite-order Eisenstein scope. It does not estimate the complementary
native tail or establish RH or a new unconditional zero-free region.

## 1. Exact local file binding

The following hashes were computed from the actual local bytes after the
author's final correction. Git blob hashes include the canonical
`blob <byte count>\0` prefix.

| File | Bytes | SHA256 | Git blob SHA1 |
|---|---:|---|---|
| `INVERSE_POWER_COMPONENT.md` | 29,610 | `46821c4854806910b434c11c7a3560fd2f5a75ef5e52c35414f01e83e86d7437` | `44db72c707a2c64f07e66c890a93c6d3a06e6cb8` |
| `check_inverse_power_component.py` | 13,146 | `08028aa0c0af4f30ddf8743707e3d3eb4d02eea2990b9b0d4a0060e50e6c96c8` | `1a3e98a21d0a0e308e05af8b1bd7e67eea0d9803` |

For the compatibility check only, the separate consumer was read at
`CONDITIONAL_CONSUMER.md`, 21,818 bytes, SHA256
`e8df7950354cc5f977704c148b1030fd7fd7a98edc5853730444bcc8526b65d0`,
Git blob `ad625275f1999853eb9947475496eb1400075b37`.
This reviewer authored that consumer, so this is a cross-file compatibility
check, not an independent review of the consumer's scalar certificate.
The parent reviewer separately reviews that certificate.

No remote commit is authenticated by this local binding. A later remote
authentication must fetch these files at an exact commit and compare
their content hashes and Git blobs.

## 2. Imported scope checked during this review

I freshly opened Xu--Sang's
[arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), especially
Theorem 2.2, equation (6.3), Lemma 6.2 and Proposition 6.3. I also fetched
the actual pinned
[September 30 source](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)
at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`; its reported Git
blob is `268c4e3206d460c617d3d2129742a72b831b3def`. In that content I read
the logarithmic-control and deleted-Euler-factor lemmas, buffered bins,
dyadic pointwise estimates, simultaneous detector proof, and the empty
prime-slot case of the plain product moment.

The ordinary fourth moment permits bounded nonnegative log-lengths with
no conductor lower bound. The density count is for the actual
sixth-power-free physical rows and polynomial-height buffered bins.
Common profiles, fixed finite presentation families, original zero
extensions and fixed polynomial height costs remain necessary. The
reviewed component keeps these conditions. It does not use a theorem
for all angular characters or transfer Liu's larger-field consumer to
the Eisenstein field.

## 3. Main theorem: exact identities and analytic estimates

### Smooth convolution and the outer selector

I verified the ordinary convolution identity directly. Since `m_y=mu_E`
through norm `y`, the support of `delta_1-m_y*1` starts strictly above
`y`. Its convolution square vanishes through `y^2`. Multiplication by
`mu_E` gives

\[
             \mu_E=2m_y-m_y*m_y*1\qquad(Nn\le y^2).
\]

For `y=sqrt(2D)` and `D>8`, the linear term is absent on the annulus
`(D,2D)`. Bounded `D` means bounded `U` in the claimed length range and
is harmless. The argument does not require squarefree products or
coprime factors; the repeated-prime terms are essential.

Both notes use the same fixed smooth `w_0` in the short factors and the
same smooth `chi_0(Nr/U^(13/20))` in the low term. Their high term is
exactly its coherent complement. The low support extends through
`2U^(13/20)`. Neither the pointwise argument nor the sufficient tail
hypothesis silently replaces this selector with a sharp outer cutoff.

### Buffered inverse products and the printed floor

On a bin with `delta=2a-1`, the reciprocal contour gives each actual
normalized inverse factor of length `A` the exponent
`delta log_U(A)/2`, with the prescribed small losses. Smooth separation
of the coupled `a,b` profile therefore gives the squared outer
polynomial exponent `delta rho` at product scale `R=U^rho`.
The dyadic factors satisfy `AB` comparable to `R`; no condition
`R<=y` is needed. Their cutoff derivatives remain bounded even when
the two-factor product exceeds either factor cutoff.

The above-floor count is

\[
 \mathcal R(\delta)=\frac{15-16\delta}{15-6\delta},
 \qquad 0<\delta\le\frac34.
\]

I independently differentiated this rational function and optimized
`mathcal R(delta)+s delta`. Its derivative is
`-150/(15-6delta)^2`; its second derivative is negative. The interior
critical point is `5/2-5/sqrt(6s)`, with contacts at `s=2/3` and
`s=200/147`. These facts give all three branches of the stated envelope.
The cap is load-bearing for its general form.

For the main theorem, the printed `.51` floor contributes
`1+13/500` to the fourth moment at `2rho=13/10`. The legal competitor
`delta=1/2` already gives `37/30`, which is larger. Thus the main result
does not depend on the adjustable-floor assertion. Its fourth-moment
endpoint and final exponent are exactly

\[
 E_* = \frac{71}{12}-\frac{\sqrt{195}}3,
 \qquad \frac{1+E_*}{2}
       =\frac{83}{24}-\frac{\sqrt{195}}6.
\]

### Primitive reflection and restoration

The zero-deletion coefficient is the primitive value `psi_u^*(e)`.
Using the original zero-extended value there would erase required
terms; the reviewed expression does not do so. Every good prime of a
sixth-power-free row has a nontrivial local character and conductor
exponent one. Consequently only fixed bad primes require restoration
after primitive reflection. The restoration over `S_0` has bounded
mass `sum_h (Nh)^(-1/2)`.

I independently checked both normalizations. In the normalized formula,
the external scalar is `(Ne Nh)^(-1/2)` and the actual dual scale is

\[
 L_u=\frac{\mathcal C_u\,Nr\,Ne}{D\,Nh}.
\]

After including `Nr^(-1/2)` and `L_u^(-1/2)`, the unnormalized
coefficient is exactly `sqrt(D/C_u)/(Nr Ne)`; the `Nh` powers cancel.
All characters at the primitive conductor still vanish there. The
puncture changes the dual scale without being inserted into the
primitive conductor.

For the common nominal scale `L_0=C_* R Ne/(D Nh)`, separation on
`z=C_u/C_*`, `x=Nr/R`, and `y'=Nn/N` leaves precisely

\[
 \sqrt{N/L_0}\,z^{-1/2}x^{-1}
       \Phi_t\!\left(\frac{(N/L_0)y'}{zx}\right).
\]

The conductor Fourier mode is a bounded row scalar. The separated
column profiles are common within the mean. Root numbers and local
primitive values are also bounded row scalars; discarding their
absolute values only after the appropriate norm inequality creates no
row-selected column coefficients.

### Small dual scales, infinite tails, and coherence

The dyadic factor `sqrt(N/L_0)` is retained. For `B>1/2`,

\[
 \sum_{N\ge1\ {\rm dyadic}}
       (N/L_0)^{1/2}(1+N/L_0)^{-B}\ll_B1
\]

uniformly for all `L_0>0`. When `L_0<1`, the sum is
`O(L_0^(B-1/2))`. This is the necessary small-scale check; a fictitious
unit contribution per empty dual scale would not be valid.

I checked the finite-range use of the ordinary moment as well. The
nominal dual scale is bounded by a prescribed power of `U`, uniformly
in `h`. Beyond a larger fixed power, the elementary plain-sum bound
and a sufficiently large fixed transform decay order control the
infinite dual tail. No ordinary moment is applied at an unbounded
log-length.

Hölder combines the actual outer fourth moment with the actual ordinary
fourth moment. Minkowski then sums the common Fourier modes, dual
annuli, conductor sectors, and outer windows. The moving puncture costs
only `U^epsilon`: for every positive fixed loss, large prime factors of
`prod_{p|Q_s}(1+(Np)^(-1/2))` are bounded by the corresponding small
power of `NQ_s`, and the finitely many small primes cost a constant.
The `h` mass is a fixed convergent product.

The resulting bound is for the norm of the coherent low sum. The proof
does not equate it with a sum of separate squared norms or replace its
signed coefficients by a different arithmetic sequence.

### Heights and allowed varying parameters

The pointwise reciprocal input is first established inside a finite
buffered height rectangle. Larger separated frequencies are covered
by a fixed polynomial height factor, or equivalently by late Fourier
truncation and trivial tail estimates. Internal detector and moment
orders are fixed before the buffer height; external Mellin and Fourier
decay orders are chosen afterwards. Differentiating the external
common profile only changes the final finite profile and height orders.

This order of choices gives the asserted common-profile estimate. The
source's finite-dimensional detector parameters can then be handled by
their parameter derivatives and Sobolev bound. It does not permit
arbitrary independent tests on different rows. All actual frequencies
entering one `L`-argument share one cumulative height allowance.

## 4. Separate review of Section 6

I also accept Section 6 as a deduction from the pinned proof, rather
than as a claim that its adjustable-floor theorem was already printed.
This acceptance is separate from that of the main component theorem.

The source logarithmic-control lemma explicitly allows its real
parameter down to `1/2`. In the detector proof, replacing the floor
`.51` by a fixed `1/2+nu` preserves the buffered-maxima construction.
The Gamma-integral contour stays at real part at least `1/4+nu` in
its `L`-argument. Saturation divides a preliminary loss by `delta`, so
using `delta>=2nu` requires reducing that loss first. All of these
operations are valid for fixed positive `nu`; no constant is asserted
uniform as `nu` tends to zero.

The originally omitted source height factor was corrected before this
binding. The error is now written as

\[
 U^{-3+t(5/4-\operatorname{Re}\rho)+o(1)}T_1^2.
\]

Its pre-height exponent is at most `-15/8`. With
`T_1<=U^(1/100)`, the full bound is
`U^(-371/200+o(1))=o(1)`. I checked these exact fractions against the
pinned detector proof.

For fixed integer `j`, the Dirichlet series of `mu_E^{*j}(n)psi_u(n)`
is exactly `L_orig(s,psi_u)^(-j)`, including the natural zeros.
Raising the local reciprocal bound to a fixed power and shifting the
same finite contour is legitimate. Its coefficients have a fixed
divisor bound on the absolute line. The floor contribution is
`U^(1+p rho nu+epsilon_1)`, which fits the desired loss after choosing
the fixed `nu` from the bounded ranges and requested epsilon.

The general envelope in (32) still uses the `7/8` cap. The narrower
row-volume consequence does not need that cap: the two uncapped density
branches satisfy the displayed line `1-2delta/3`, so slopes at most
`2/3` give exponent at most one. This reasoning permits neither a
growing inverse power `j` nor a floor varying with `U`.

## 5. Consumer compatibility and reproducible checks

The complete low term in the conditional consumer is the same as (9),
with the same masks, phases, finite-order row family, smooth factor
cutoffs and smooth outer selector. Its required length interval
`[29/25,117/100]` lies inside the component theorem's bounded range.
The strict radical comparison is exact:

\[
 \frac{17}{15}-\left(\frac{83}{24}-\frac{\sqrt{195}}6\right)
       >\frac1{1000},
 \qquad
 195-\left(\frac{3489}{250}\right)^2=\frac{14379}{62500}>0.
\]

Thus the component really supplies the complementary low term needed
by that consumer. It supplies no estimate for its coherent high term.
The conditional region remains conditional on the full high-term
second moment, not on a diagonal or unsigned replacement.

I read the checker and independently replayed it with `python -O`.
All acceptance predicates use explicit `require` calls. Its output
reported 1,820 convolution checks, 5,694 phase/mask checks, 648
reflection-normalizer checks, 6,868 envelope comparisons and 101
contact identities, all passing. It also passed the printed-floor
test, exact radical margin, critical-length interval, and negative
controls for omitted repeated primes, a lost puncture factor, and an
excessive claimed saving.

The rational enclosure

\[
 \frac{29}{25}<\frac{174882826}{150272989}
       <r_c<\frac{6994}{6007}<\frac{117}{100}
\]

uses sign brackets and derivative bounds, not decimal acceptance.
I checked its monotonicity directions and the interior contact identity
`rho_*(r)=(1+sqrt(r-1))^2/3`, including its endpoint range
`1<=r<=58/49`.

The checker's finite envelope comparisons are corroborating algebra,
not a proof of inequalities on a continuum. The derivative/concavity
argument above supplies that proof. Likewise the finite multiplicative
examples do not prove a character moment or an analytic continuation.
The review accepts the new deductions subject to the exact imported
premises and records the full native tail as the remaining open estimate.
