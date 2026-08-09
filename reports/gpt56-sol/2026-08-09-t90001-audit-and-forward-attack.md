# T-90001 audit and forward attack — 2026-08-09

Branch: `agent/gpt56-sol/90005-zcollapse-proof`  
Base inspected: `claude/riemann-proof-review-8nz34i` at `777a5b9f20a96a01fabd0c7e9daec5d208e2d778`  
Earlier source commit: `617d6c2c701aed4c0861d827193f81991ea78f34`  
Authoring/review agent: `gpt56-sol`  
RH status: **UNPROVED**

## 1. Executive result

The source session's mathematical centerpiece survives targeted re-derivation:
the finite theta bridge and the Moat mechanism are coherent, and WSTS is indeed
an RH-equivalent scalar criterion once a complete Landau consumer is supplied.
The most serious residency issue in the source note was not a discovered false
identity; it was that the full converse consumers lived only in session journals.
This branch removes that gap.

The branch also proves a new deterministic theorem that was only numerical in
the source session: the exact dyadic shell has one continuum sign crossing and,
for every even endpoint, only a uniformly bounded finite transition window.
Consequently the tail maximum is the endpoint scalar up to
`O(X^(-3/2) log X)`.

No unconditional estimate of that endpoint scalar is obtained.  RH remains
open.

## 2. Audit of the post-verification T-90001 repairs

The requested source-side post-verification edits were inspected in the actual
branch rather than inferred from the session summary.  The important repairs
are mathematically appropriate.

### 2.1 Symbol collision

The Chebyshev error is consistently typed as
\[
R(t)=\vartheta(t)-t,
\]
while the prime Riesz/ramp sum is given a separate symbol.  This removes a real
ambiguity in the original converse prose.

### 2.2 Top-cell extension

The identity expressing `b(kq)-b(kq+1)` as an integral of `g` needs the analytic
formula on the top interval when `kq<=X<kq+1`.  The repaired proof extends the
formula through `[X,X+1]`.  Because
\[
b_X(X)=b_X'(X)=0,
\]
the disagreement with the declared zero extension is quadratic and is smaller
than the already retained floor-error slack.  This is the correct repair.

### 2.3 The `g'` monotonicity bug

The raw quantity
\[
|g'(u)|={u^{-3/2}\over2}|\log u+2|
\]
is not monotone on `(0,1]`.  The repaired argument uses
\[
M(u)={u^{-3/2}\over2}(2-\log u),
\]
which is decreasing there and majorizes `|g'|`.  The resulting per-modulus
`q^(-3/2)` floor estimate is preserved.  This was a genuine proof-writing bug,
not a failure of the bridge.

### 2.4 Moat antiderivative and constants

The global cell antiderivative
\[
H(\theta)
=-2\sqrt\theta[A_N+(S_N+1)\log\theta+2S_N-2]
+4N\theta-4
\]
was independently differentiated.  It satisfies `H'=-E`, `H(1)=0`, and exact
continuity at reciprocal knots.  With
\[
J=H/\sqrt\theta,
\]
\[
J'(\theta)
=2\theta^{-3/2}[N\theta+1-(S_N+1)\sqrt\theta]
\ge2\theta^{-3/2}(\sqrt{N\theta}-1)^2,
\]
using only
\[
S_N\le2\sqrt N-1.
\]
Thus `H<=0`, and scale monotonicity gives `H_c<=0` for every `c in (0,1)`.
This is the strongest and cleanest part of the source packet.

## 3. T-90001 is now resident in both directions

### 3.1 Forward direction

`L-90007` reconstructs the elementary cell estimates
\[
|E(\theta)|\ll\theta^{-1/2}(1+\log(1/\theta)),
\]
\[
|E'(\theta)|\ll\theta^{-3/2}(1+\log(1/\theta)),
\]
uniformly for the actual finite shell ratio.  Under RH, the classical
`vartheta(t)-t=O(sqrt(t) log^2 t)` estimate and Stieltjes integration by parts
give
\[
B_X\ll\log^4(2X).
\]
This is enough for WSTS.

The source session claimed an additional one-log sharpening to `log^3`.  That
sharpening is not needed for the equivalence and its full bookkeeping was not
resident.  This branch deliberately does **not** make it load bearing.

### 3.2 Converse direction

`L-90006` supplies a shorter consumer than the source-session `hat E` route.
At `z=2`,
\[
T_X^s(2)=A_X-A_{\lfloor X/2\rfloor},
\]
so WSTS telescopes directly to `A_X=O_epsilon(X^epsilon)` one-sidedly.

The complete prime-power seed satisfies
\[
\sum_{q\le X}\Lambda(q)v_q(b_X)
=\sum_{n=2}^Xb_X(n)\log\frac n{n-1}
=4\sqrt X+O(\log X).
\]
Higher prime powers cost only `O(log^3 X)`, hence the ordinary prime seed is
`4 sqrt(X)+O(log^3 X)`.  Therefore WSTS implies
\[
4\sqrt X-
\sum_{p\le X}{\log p\over\sqrt p}\log{X\over p}
\ll_\varepsilon X^\varepsilon.
\]

For the deficit `F(X)`, the Mellin transform is
\[
\widehat F(z)
={4\over z-1/2}
+{1\over z^2}{\zeta'\over\zeta}(z+1/2)
+{1\over z^2}Q(z+1/2),
\]
where
\[
Q(s)=\sum_p\sum_{k\ge2}{\log p\over p^{ks}}
\]
is holomorphic for `Re s>1/2`.  The pole at `s=1` cancels exactly.  A zero
`rho` with `Re rho>1/2` survives with residue
\[
m_\rho/(\rho-1/2)^2.
\]
A standard Landau one-sign argument applied to
`C X^epsilon-F(X)>=0` excludes such a pole.  No reciprocal-zeta numerator and
no dyadic blind spot appear in this consumer.

This closes the largest source-session Flag 0 residency gap.  The old auxiliary
real-`X` interpolation flag is also unnecessary: the ramp itself interpolates
between consecutive integers with error `O(log X/sqrt X)`.

## 4. New result: exact dyadic one-crossing and finite z-collapse

`L-90005` starts from the exact `c=1/2` shell profile.  On quotient cell `N`,
with `M=floor(N/2)` and `x=sqrt(theta)`, it reduces to
\[
P_N(x)=C_N+2D_N\log x-K_Nx,
\qquad
P_N''(x)<0.
\]
The reciprocal-knot values satisfy an explicit scalar increment and are proved
to be strictly increasing.  The only crossing is on the `N=7` cell.  Its root
is
\[
\boxed{c_*=0.1408520350138399254409579889\ldots}.
\]
This corrects the source note's coarse `0.1408512...` value.

For every even integer `X`, exact secant-curvature comparison transfers the
continuum sign to the finite shell:
\[
q\le c_*X-1\Longrightarrow s_X(q)>0,
\]
\[
q\ge c_*X+158\Longrightarrow s_X(q)<0.
\]
The width `158` is intentionally crude and analytic; the retained regression
through `X=20000` sees a much smaller transition.

Therefore
\[
\boxed{
B_X=[T_X^s(2)]_+ +O(X^{-3/2}\log(2X))
}
\]
for every even `X`.  This proves the deterministic part of the old numerical
Lemma S at a stronger finite level.  It does not estimate the endpoint scalar.

## 5. New alternate route: critical-Haar annularization of the low-row scalar

The low-row SHARP criterion uses
\[
\omega=(\varepsilon-\delta_2)*(2\varepsilon-\delta_2)*\mu
\]
and the complete hinge
\[
W(T)=\sum_{n\le T}\omega(n)(n^{-1/2}-T^{-1/2}).
\]
`L-90008` inserts the critical Haar factor
\[
\varepsilon-\sqrt2\,\delta_2.
\]
The resulting scalar is exactly
\[
U(T)=W(T)-W(T/2).
\]
Its local two-adic polynomial is
\[
(1-x)^2(2-x)(1-\sqrt2 x),
\]
which vanishes at both `x=1` and `x=1/sqrt(2)`.  Hence every complete two-adic
fiber cancels in both the constant and half-power moments, leaving the exact
annular formula
\[
U(T)
=\sum_{T/16<m\le T,\ m\ odd}{\mu(m)\over\sqrt m}w(T/m)
\]
with an explicit four-band kernel `w`.

The Mellin multiplier added by the Haar difference is `1-2^(-z)`, whose zeros
are on `Re z=0`.  Therefore every hypothetical zeta zero with `Re rho>1/2`
still creates a pole.  This is a zero-safe compact annularization, not a
smoothing that hides the obstruction.

The annular kernel is not one-signed, so the low-row sign theorem remains open.

## 6. Route selection after this pass

### First choice: Q4 reflected/Jordan recurrence

The live Q4 graph has the most ingredients whose combination could still
produce an inequality rather than another RH criterion:

- a deterministic reserve increment `Delta_4 R = Theta(n log n)` on the same
  radix step as the RH-sensitive innovation;
- a compact main-pole-killing current source;
- exact physical/carry typing;
- a critical-line parity jet frame for the compact current;
- one source-matched augmented curvature which absorbs that entire jet without
  double spending;
- adaptive critical-Haar diagonalization whose inverse-source curvature reduces
  to only two dynamic states.

The remaining theorem is genuinely reflected/dynamical: orient the positive
source-complete curvature dissipatively through a coefficient-one delayed
recurrence.  A scalar positive reserve by itself is not enough; `L-34006`
already states this firewall correctly.  I did not find a legitimate generic
PSD/Cauchy shortcut that bypasses the source-convolved two-frequency ledger.

This is still the route I would attack first in a continuation.

### Second choice: low-row critical-Haar annuli

`L-90008` makes the low-row route much more local: every dyadic innovation has
fixed multiplicative support and finite overlap across scales while preserving
every off-line pole.  The next productive question is whether this annular bank
admits a coercive square/energy inequality stronger than pointwise sign.

### Deprioritized as a producer: WSTS itself

After `L-90005` and `L-90006`, attacking WSTS directly means attacking the
surviving prime-ramp endpoint scalar.  The geometry, max over tails, and
consumer are no longer the difficulty.  This is a clean front door and an
excellent review criterion, but not presently the best producer of new RH
information.

## 7. Exact boundary after this pass

Proposed complete, pending independent review:

```text
T-90001 finite theta bridge and Moat
L-90007 RH => WSTS, conservative O(log^4 X)
L-90006 WSTS => prime ramp => RH
L-90005 dyadic continuum one-crossing
L-90005 even-endpoint finite bounded transition and z-collapse
L-90008 critical-Haar factor-16 annularization of the low-row scalar
```

Explicitly unproved:

```text
WSTS
prime-ramp subpower bound unconditionally
odd-endpoint sharp z-collapse
coercive estimate for the low-row annular bank
Q4 reflected dissipative coefficient-one recurrence
Riemann Hypothesis
```

The branch should be reviewed as a proof-spine repair plus two new structural
theorems, not as an RH proof claim.