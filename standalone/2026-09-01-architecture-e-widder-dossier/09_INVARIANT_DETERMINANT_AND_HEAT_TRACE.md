# Invariant determinant, matching-scale poles, and the fixed-center heat trace

Status: **PROPOSED EXACT IDENTITIES AND RH-EQUIVALENT REFORMULATIONS; INDEPENDENT REVIEW REQUIRED; RH REMAINS UNPROVED.**

This note extracts the first genuinely height-free leverage from the
functional-equation invariant coordinate.  It does not prove the all-order
E--Widder source inequality.  It replaces the unbounded list of derivative
inequalities by three exact global objects:

1. a normalized determinant which is already a squared characteristic
   function of a positive source distribution;
2. an entire Borel transform whose exponential type detects an off-line zero;
3. one fixed-center invariant zero heat trace whose complete monotonicity is
   equivalent to RH.

The determinant is nonnegative unconditionally.  RH asks only for **strict
nonvanishing** on an open real parameter strip.  A hypothetical off-line zero
creates a noncancellable real pole at one canonical matching scale.  The
published finite-height verification pushes the possible pole into a terminal
subinterval of width less than `2.78e-26`.

The note uses the source and notation of the preceding dossier.  In
particular,

\[
 \mathfrak X(s(s-1))=\xi_{\rm R}(s),
 \qquad
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)}.
\]

The zeros of `mathfrak X` are written as `-a`, where the multiset of `a` is
closed under conjugation and

\[
 q(u)=2\sum_a\frac1{u+a}.
 \tag{0.1}
\]

One `a` is used for each functional-equation orbit, with multiplicity.  The
genus-zero convergence established in the parent packet implies

\[
 \sum_a\frac1{|a|}<\infty.
 \tag{0.2}
\]

## 1. Normalized E--Widder power sums

Retain

\[
 \mathcal W_k(u)
 =(-1)^{k-1}D_u^{2k-1}[u^kq(u)],
 \qquad k\ge1.
\]

Define

\[
 \boxed{
 C_k(u)
 =\frac{(4u)^k}{2(2k-1)!}\mathcal W_k(u).
 }
 \tag{1.1}
\]

The one-atom Widder identity gives

\[
 \boxed{
 C_k(u)=\sum_a\lambda_u(a)^k,
 \qquad
 \lambda_u(a)=\frac{4ua}{(u+a)^2}.
 }
 \tag{1.2}
\]

For

\[
 a=Re^{i\alpha},
 \qquad
 v=\log(u/R),
\]

the transformed atom has the exact hyperbolic form

\[
 \boxed{
 \lambda_u(a)
 =\operatorname{sech}^2\left(\frac{v-i\alpha}{2}\right).
 }
 \tag{1.3}
\]

Indeed,

\[
 u+a
 =2\sqrt{uR}\,
 e^{(v+i\alpha)/2}
 \cosh\left(\frac{v-i\alpha}{2}\right).
\]

For a critical invariant atom, `alpha=0`, and

\[
 0<\lambda_u(a)
 =\operatorname{sech}^2(v/2)\le1.
\]

For an off-line atom, at the canonical matching scale `u=R`,

\[
 \boxed{
 \lambda_R(a)=\sec^2(\alpha/2)>1.
 }
 \tag{1.4}
\]

Thus the new coordinate converts a nonreal invariant zero into a transformed
real eigenvalue strictly outside the interval `[0,1]`.

## 2. The invariant determinant

For fixed `u>0`, define

\[
 \boxed{
 \Delta_u(w)
 =\prod_a\left(1-w\lambda_u(a)\right).
 }
 \tag{2.1}
\]

The product converges locally uniformly in `w` because
`\lambda_u(a)=O_u(1/a)` and (0.2).

Let `eta=eta(w)` satisfy

\[
 \eta+\eta^{-1}=2(1-2w),
 \qquad
 \eta(0)=1.
 \tag{2.2}
\]

Then

\[
 (a+u\eta)(a+u\eta^{-1})
 =(a+u)^2-4uaw.
\]

Using the genus-zero product of `mathfrak X` gives the exact determinant
identity

\[
 \boxed{
 \Delta_u(w)
 =
 \frac{\mathfrak X(u\eta)\mathfrak X(u\eta^{-1})}
      {\mathfrak X(u)^2}.
 }
 \tag{2.3}
\]

This identity is independent of RH.

Its logarithmic derivative is the ordinary generating function of the
normalized Widder sequence:

\[
 \boxed{
 \mathcal R_u(w)
 :=-\partial_w\log\Delta_u(w)
 =\sum_{k\ge1}C_k(u)w^{k-1}
 =\sum_a\frac{\lambda_u(a)}{1-w\lambda_u(a)}.
 }
 \tag{2.4}
\]

The first equality is initially valid near `w=0` and then supplies the common
meromorphic continuation.

A partial-fraction calculation gives a second exact form.  Since

\[
 \frac{4ua}{(a+u\eta)(a+u\eta^{-1})}
 =
 \frac{4u}{\eta-\eta^{-1}}
 \left[
  \frac{\eta}{a+u\eta}
  -\frac{\eta^{-1}}{a+u\eta^{-1}}
 \right],
\]

we obtain

\[
 \boxed{
 \mathcal R_u(w)
 =
 \frac{2u}{\eta-\eta^{-1}}
 \left[
  \eta q(u\eta)
  -\eta^{-1}q(u\eta^{-1})
 \right].
 }
 \tag{2.5}
\]

### Real-ray form

For real `0<w<1`, put

\[
 w=\sin^2(\theta/2),
 \qquad
 \eta=e^{i\theta},
 \qquad
 0<\theta<\pi.
\]

Real coefficients give

\[
 \boxed{
 \Delta_u(w)
 =
 \frac{|\mathfrak X(ue^{i\theta})|^2}
      {\mathfrak X(u)^2}.
 }
 \tag{2.6}
\]

Moreover,

\[
 \boxed{
 \mathcal R_u(w)
 =
 \frac{2u}{\sin\theta}
 \Im\left[e^{i\theta}q(ue^{i\theta})\right]
 =
 \frac{4u}{\sin\theta}
 \partial_u\arg\mathfrak X(ue^{i\theta}).
 }
 \tag{2.7}
\]

Thus the complete E--Widder hierarchy has become one radial phase derivative
of the invariant entire function.

## 3. Positive-coefficient probability interpretation

The positive theta representation gives

\[
 \xi_{\rm R}(1/2+x)
 =2\int_0^\infty\Phi(t)\cosh(xt)\,dt.
\]

Consequently its Taylor coefficients in `x^2` are positive.  Substitution
`x^2=u+1/4` shows that

\[
 \boxed{
 \mathfrak X(u)=\sum_{m\ge0}c_mu^m,
 \qquad
 c_m>0.
 }
 \tag{3.1}
\]

For fixed `u>0`, define the power-series distribution

\[
 \boxed{
 p_m(u)=\frac{c_mu^m}{\mathfrak X(u)}.
 }
 \tag{3.2}
\]

Then `p_m(u)>0` and

\[
 \sum_{m\ge0}p_m(u)=1.
\]

Equation (2.6) becomes

\[
 \boxed{
 \Delta_u(w)
 =
 \left|
  \sum_{m\ge0}p_m(u)e^{im\theta}
 \right|^2,
 \qquad
 w=\sin^2(\theta/2).
 }
 \tag{3.3}
\]

Therefore

\[
 \boxed{
 0\le\Delta_u(w)\le1
 \qquad
 (u>0,\ 0\le w\le1)
 }
 \tag{3.4}
\]

unconditionally.

This is the first central leverage of the determinant coordinate:

> The RH-bearing target is no longer a sign theorem.  The determinant is
> already nonnegative from the literal positive source.  The remaining
> theorem is strict nonvanishing of one characteristic function away from
> the parity endpoint.

Under RH the factors in (2.1) satisfy `0<lambda<=1`, so

\[
 \Delta_u(w)>0
 \qquad(0\le w<1).
\]

Conversely, Section 4 shows that any off-line zero creates an interior zero.
Hence

\[
 \boxed{
 {\rm RH}
 \iff
 \Delta_u(w)>0
 \quad\text{for every }u>0,\ 0\le w<1.
 }
 \tag{3.5}
\]

Equivalently, every power-series distribution (3.2) has a nonvanishing
characteristic function on the open upper unit semicircle.

## 4. Matching-scale pole theorem

Let an off-line invariant zero be

\[
 a=Re^{i\alpha},
 \qquad
 \alpha\ne0.
\]

Since every nontrivial zeta zero lies in the open critical strip,

\[
 \Re a>0,
 \qquad
 |\alpha|<\pi/2.
 \tag{4.1}
\]

At `u=R`, equation (1.4) gives

\[
 \lambda_R(a)
 =\lambda_R(\bar a)
 =\sec^2(\alpha/2).
\]

Set

\[
 \boxed{
 w_a=\cos^2(\alpha/2)\in(1/2,1).
 }
 \tag{4.2}
\]

Then

\[
 1-w_a\lambda_R(a)=0.
\]

If the zero orbit has multiplicity `m`, both conjugate invariant atoms give
the same factor.  Therefore

\[
 \boxed{
 \Delta_R(w)
 \text{ has a zero of order }2m\text{ at }w=w_a.
 }
 \tag{4.3}
\]

The generator has principal part

\[
 \boxed{
 \mathcal R_R(w)
 =-\frac{2m}{w-w_a}+O(1).
 }
 \tag{4.4}
\]

No cancellation is possible: every transformed atom producing the same real
pole has residue `-1` times its positive multiplicity.

This gives a canonical individual-zero detector.  The matching scale is not
chosen from the unknown horizontal displacement separately; it is the
invariant modulus `u=|a|`.

## 5. Exact pair-positivity threshold

For one conjugate pair, put

\[
 \lambda=\lambda_u(a).
\]

Its contribution to the real generator is

\[
 \frac{\lambda}{1-w\lambda}
 +\frac{\bar\lambda}{1-w\bar\lambda}
 =
 \boxed{
 \frac{2(\Re\lambda-w|\lambda|^2)}
      {|1-w\lambda|^2}.
 }
 \tag{5.1}
\]

Now

\[
 \frac1\lambda
 =\frac14\left(2+\frac ua+\frac au\right).
\]

Writing `a=Re^{i alpha}` gives

\[
 \boxed{
 \Re\frac1{\lambda_u(a)}
 =
 \frac12
 +\frac{\cos\alpha}{4}
 \left(\frac uR+\frac Ru\right)
 \ge
 \cos^2(\alpha/2).
 }
 \tag{5.2}
\]

Thus every conjugate pair contributes strictly positively whenever

\[
 \boxed{
 0\le w<\cos^2(\alpha/2).
 }
 \tag{5.3}
\]

The lower bound is sharp at the matching scale.

### Unconditional half-ray theorem

Since `Re(a)>0`, every invariant atom has `|alpha|<pi/2`.  Hence

\[
 \boxed{
 \mathcal R_u(w)>0
 \qquad
 (u>0,\ 0\le w\le1/2).
 }
 \tag{5.4}
\]

This is an all-order statement: it sums the entire normalized Widder
hierarchy before taking a sign.

For `0<=w<=1/2`, the radial point `ue^{i theta}` has nonnegative real part.
Therefore

\[
 \Re\sqrt{1/4+ue^{i\theta}}>1/2
\]

for `u>0` (strictly also at `theta=pi/2`).  The corresponding completed-zeta
arguments lie in `Re(s)>1`.  Thus the whole generator on the unconditional
half-ray has a direct absolutely convergent Euler representation.

## 6. Finite height leaves only a terminal interval of quadratic width

Suppose every nontrivial zero through height `H` is critical.  The angular
bound in `08_FINITE_HEIGHT_WIDDER_CONE.md` gives, for every hypothetical
off-line zero above `H`,

\[
 |\alpha|<\arctan(1/H).
\]

Define

\[
 \boxed{
 w_H
 =
 \cos^2\left(\frac12\arctan\frac1H\right)
 =
 \frac12\left(1+\frac{H}{\sqrt{H^2+1}}\right).
 }
 \tag{6.1}
\]

The pair theorem yields

\[
 \boxed{
 \mathcal R_u(w)>0
 \qquad
 (u>0,\ 0\le w<w_H).
 }
 \tag{6.2}
\]

The unproved real-ray interval is therefore only

\[
 [w_H,1).
\]

Its width satisfies

\[
 \boxed{
 1-w_H
 =
 \frac1{
  2\sqrt{H^2+1}
  \bigl(\sqrt{H^2+1}+H\bigr)
 }
 <\frac1{4H^2}.
 }
 \tag{6.3}
\]

With the imported Platt--Trudgian height

\[
 H=3\cdot10^{12},
\]

we obtain

\[
 \boxed{
 1-w_H<2.78\cdot10^{-26}.
 }
 \tag{6.4}
\]

This result is complementary to the finite-order cone.  It does not imply
coefficientwise positivity for unbounded Widder order.  It proves that the
**all-order generator**, as one object, is already positive on all but a
quadratically thin terminal interval.

In angular coordinates the unresolved region is

\[
 \pi-\arctan(1/H)<\theta<\pi.
\]

It is exactly the near-parity or near-critical-line boundary.

## 7. Entire Borel transform and exponential-type criterion

Define the factorially summed Widder transform

\[
 \boxed{
 \mathcal E_u(\tau)
 =
 \sum_{k\ge1}\frac{C_k(u)}{k!}\tau^k.
 }
 \tag{7.1}
\]

Since `sum |lambda_u(a)|<infinity`, the zero-side expression

\[
 \boxed{
 \mathcal E_u(\tau)
 =
 \sum_a\left(e^{\tau\lambda_u(a)}-1\right)
 }
 \tag{7.2}
\]

converges locally uniformly and defines an entire function of `tau`.

Under RH, every transformed atom lies in `(0,1]`; consequently

\[
 \operatorname{type}(\mathcal E_u)\le1
 \qquad(u>0).
\]

Conversely, an off-line atom at its matching scale has the positive real
value

\[
 \lambda_R(a)=\sec^2(\alpha/2)>1.
\]

Equivalently, the ordinary generator has the noncancellable pole (4.4), so
Cauchy--Hadamard gives

\[
 \limsup_{k\to\infty}|C_k(R)|^{1/k}
 \ge\sec^2(\alpha/2)>1.
\]

For an exponential generating function,

\[
 \operatorname{type}(\mathcal E_u)
 =
 \limsup_{k\to\infty}|C_k(u)|^{1/k}.
\]

Therefore

\[
 \boxed{
 {\rm RH}
 \iff
 \operatorname{type}(\mathcal E_u)\le1
 \quad\text{for every }u>0.
 }
 \tag{7.3}
\]

This trades coefficient-by-coefficient positivity for an entire-growth
theorem.  Unlike the ordinary generator, the Borel series has no finite
radius barrier.  A source-side construction of (7.1) with type at most one
would prove RH without proving every Widder inequality separately.

No such source-side type bound is proved here.

## 8. The fixed-center invariant zero heat trace

For every nontrivial zero, define the centered zero coordinate

\[
 \gamma_\rho=\frac{\rho-1/2}{i}.
\]

Then

\[
 \boxed{
 a_\rho
 =-\rho(\rho-1)
 =\frac14+\gamma_\rho^2.
 }
 \tag{8.1}
\]

Use the full zero multiset, including multiplicity, and define

\[
 \boxed{
 K(t)
 =\sum_\rho m_\rho e^{-a_\rho t}
 =e^{-t/4}\sum_\rho m_\rho e^{-t\gamma_\rho^2},
 \qquad t>0.
 }
 \tag{8.2}
\]

The Riemann--von Mangoldt bound gives absolute and locally uniform
convergence.  The full-zero convention exactly matches the factor two in
`q`, and

\[
 \boxed{
 q(u)=\int_0^\infty e^{-ut}K(t)\,dt.
 }
 \tag{8.3}
\]

### Fixed-center heat theorem

\[
 \boxed{
 {\rm RH}
 \iff
 K\text{ is completely monotone on }(0,\infty).
 }
 \tag{8.4}
\]

#### Proof

Under RH, every `a_rho` is the positive real number
`\gamma^2+1/4`.  Therefore

\[
 (-1)^mK^{(m)}(t)
 =\sum_\rho m_\rho a_\rho^m e^{-a_\rho t}
 \ge0.
\]

Conversely, if `K` is completely monotone, Bernstein's theorem gives a
positive measure `mu` on `[0,infinity)` with

\[
 K(t)=\int_0^\infty e^{-rt}\,d\mu(r).
\]

Substitution in (8.3) and Tonelli's theorem yield

\[
 q(u)=\int_0^\infty\frac{d\mu(r)}{u+r}.
\]

Thus `q` is Stieltjes, and the invariant Stieltjes converse in the parent
packet gives RH. `square`

This is the second central leverage:

> The all-center first-Hermite reality criterion can be replaced by complete
> monotonicity of one fixed-center invariant heat trace.

The price is the full derivative hierarchy in heat time.  The gain is that
the source is one Gaussian prime sum with no horizontal phase.

## 9. Exact gamma-plus-prime heat source

Apply the centered Guinand--Weil formula to

\[
 h_t(z)=e^{-tz^2}.
\]

In the normalization already used by the integrated First-Hermite packet,

\[
 \boxed{
 \begin{aligned}
 H(t):=\sum_\rho m_\rho e^{-t\gamma_\rho^2}
 ={}&
 2e^{t/4}\\
 &+\frac1{2\pi}\int_{\mathbb R}
 e^{-tx^2}
 \left[
  \Re\psi\left(\frac14+\frac{ix}{2}\right)
  -\log\pi
 \right]dx\\
 &-\frac1{\sqrt{\pi t}}
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.
 \end{aligned}
 }
 \tag{9.1}
\]

Every term is absolutely convergent for fixed `t>0`.  Multiplication by
`e^{-t/4}` gives

\[
 \boxed{
 \begin{aligned}
 K(t)
 ={}&2\\
 &+\frac{e^{-t/4}}{2\pi}\int_{\mathbb R}
 e^{-tx^2}
 \left[
  \Re\psi\left(\frac14+\frac{ix}{2}\right)
  -\log\pi
 \right]dx\\
 &-\frac{e^{-t/4}}{\sqrt{\pi t}}
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 e^{-(\log n)^2/(4t)}.
 \end{aligned}
 }
 \tag{9.2}
\]

Differentiating (9.1) with `-partial_t` recovers exactly the
First-Hermite prime weight

\[
 \frac1{2\sqrt\pi t^{3/2}}
 \left(1-\frac{(\log n)^2}{2t}\right)
 e^{-(\log n)^2/(4t)}
\]

and the imported first-Hermite explicit formula.  This is an internal
normalization check on (9.1).

Combining (8.4) and (9.2), RH is equivalent to the fixed-center source
inequalities

\[
 \boxed{
 (-1)^mD_t^m K(t)\ge0
 \qquad(t>0,\ m\ge0).
 }
 \tag{9.3}
\]

This is not a generic heat positivity statement.  It is the exact
gamma-plus-prime all-Hermite hierarchy in the invariant coordinate.

## 10. Relation to total positivity of the invariant coefficients

Equation (3.1) gives a positive coefficient sequence `c=(c_m)`.  Since
`mathfrak X` has genus zero, the classical
Aissen--Schoenberg--Whitney--Edrei theorem gives

\[
 \boxed{
 {\rm RH}
 \iff
 (c_m)_{m\ge0}\text{ is a Pólya-frequency sequence of infinite order}.
 }
 \tag{10.1}
\]

Under RH,

\[
 \frac{\mathfrak X(uz)}{\mathfrak X(u)}
 =
 \prod_a
 \frac{1+uz/a}{1+u/a}
\]

is the probability-generating function of an infinite sum of independent
Bernoulli variables.  The determinant (3.3) is the squared modulus of its
characteristic function.

This is a static version of the same target:

```text
all Widder inequalities
<=> all invariant Toeplitz minors
<=> nonvanishing of every power-series characteristic function
<=> negative-real invariant zero divisor
<=> RH.
```

The positive-sum `PF_infinity` firewall from the parent packet remains in
force.  The theorem must act on the completed coefficient sequence, not on
individual theta modes.

## 11. Exact log-coordinate recurrence

Let

\[
 y=\log u.
\]

The differential recurrence for `mathcal W_k`, together with the
normalization (1.1), gives

\[
 \boxed{
 C_{k+1}
 =
 \frac{2}{k(2k+1)}
 \left(k^2-\partial_y^2\right)C_k.
 }
 \tag{11.1}
\]

For one atom this is the Pöschl--Teller recurrence for the shifted profile
(1.3).  It makes the invariant hierarchy a sequence of one-dimensional
hyperbolic filters rather than an unstructured family of derivatives.

A generic positivity-preserving claim for the operator in (11.1) is false.
The useful point is that all transformed atoms and all source terms obey the
same exact recurrence.

## 12. The new completion fronts

The current height-free targets are now:

### Determinant front

Prove

\[
 \Delta_u(w)>0
 \qquad(u>0,\ 0\le w<1)
\]

directly from the positive coefficient/source distribution.  By Section 6,
with the imported verified height, only a terminal interval of width below
`2.78e-26` remains.

### Borel front

Construct the factorially summed source transform (7.1) directly from the
gamma and prime labels and prove

\[
 \operatorname{type}(\mathcal E_u)\le1.
\]

This avoids the finite radius of the ordinary generating function.

### Fixed-center heat front

Use (9.2) to prove complete monotonicity of `K`.  This is one center, no
cosine phase, and one Gaussian prime source.  It is the invariant form of the
First-Hermite constant-four frontier.

### Coefficient total-positivity front

Prove the complete invariant coefficient sequence `(c_m)` is `PF_infinity`.
Recent tail Toeplitz-minor theorems are relevant only as partial input; they do
not by themselves cover all ranks and shifts.

Any one of these four fronts closes `(EW)` and RH.

## 13. Exact boundary

```text
normalized sech-squared atom formula                 PROPOSED COMPLETE / REVIEW
determinant ratio and radial generator               PROPOSED COMPLETE / REVIEW
positive source characteristic-function identity    PROPOSED COMPLETE / REVIEW
matching-scale noncancellable pole                   PROPOSED COMPLETE / REVIEW
unconditional generator positivity on 0<=w<=1/2     PROPOSED COMPLETE / REVIEW
verified-height generator interval, gap <2.78e-26    PROPOSED COMPLETE / REVIEW
Borel exponential-type criterion                     PROPOSED COMPLETE / REVIEW
fixed-center heat complete-monotonicity criterion    PROPOSED COMPLETE / REVIEW
gamma-plus-prime invariant heat formula              PROPOSED COMPLETE / REVIEW
log-coordinate recurrence                            PROPOSED COMPLETE / REVIEW
terminal determinant / Borel / heat source theorem   OPEN / RH-EQUIVALENT
E--Widder source inequality for all orders            OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```

## 14. Priority review points

1. the orbit convention and factor two in (0.1);
2. local convergence of the determinant product;
3. the `eta` factorization and logarithmic derivative;
4. positivity of the invariant coefficients after the `1/4` translation;
5. the matching-scale zero order and generator residue;
6. the pair threshold (5.2);
7. use of the finite-height angular bound in (6.2);
8. the exponential-type converse;
9. the full-zero convention in the heat trace;
10. constants in the Guinand--Weil formula (9.1);
11. the PF-infinity equivalence for the translated invariant sequence;
12. the recurrence (11.1).
