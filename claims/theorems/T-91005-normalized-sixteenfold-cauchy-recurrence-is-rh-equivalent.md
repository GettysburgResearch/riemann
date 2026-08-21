# T-91005 — RH is equivalent to the coefficient-one normalized sixteenfold Cauchy recurrence

Claim ID: `T-91005`  
Status: **PROPOSED COMPLETE RH-EQUIVALENT RECURRENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: the Cauchy soft-count explicit formula and gate criterion; `L-91021`; `L-91022`; the terminal-pair theorem used elsewhere in the Gaussian/Cauchy programme  
RH status: **unproved**

## 1. The completed dyadic gate

Let

\[
 \mathcal N_x(a)
 =\frac12\left[a p_x(a)-a^2p_x'(a)\right],
 \qquad
 p_x(a)=\Re\frac{\xi'}{\xi}\left(\frac12+a+ix\right),
 \tag{T-91005.1}
\]

and define

\[
 \mathcal G_x(a)=\mathcal N_x(2a)-\mathcal N_x(a).
 \tag{T-91005.2}
\]

The resident Cauchy gate theorem identifies

\[
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal G_x(a)\ge0
 \quad(x\in\mathbb R,\ a>0).
 \tag{T-91005.3}
\]

Define the naturally scaled gate

\[
 \boxed{
 \mathcal E_x(a)=a^{-4}\mathcal G_x(a).
 }
 \tag{T-91005.4}
\]

## 2. RH gives a coefficient-one delayed recurrence

Under RH, the zero-side expansion contains only critical-line ordinates.  One
critical-line zero at displacement `u=gamma-x` contributes the dyadic detail
`d_a(u)` of `L-91022`.  Hence (L-91022.9) may be summed over the complete zero
set:

\[
 \boxed{
 \mathcal E_x(a)
 =\mathcal E_x(2a)+\mathcal R_x(a),
 }
 \tag{T-91005.5}
\]

where

\[
 \boxed{
 \mathcal R_x(a)
 =a^{-4}\sum_\gamma m_\gamma
  \sum_{j=1}^3r_{j,a}(\gamma-x)^2
 \ge0.
 }
 \tag{T-91005.6}
\]

The sum converges absolutely because the residual has `u^(-6)` decay and the
standard local zero count is logarithmic.

Thus

\[
 \boxed{
 \mathrm{RH}\Longrightarrow
 \mathcal E_x(a)\ge\mathcal E_x(2a)
 \quad(x\in\mathbb R,\ a>0).
 }
 \tag{T-91005.7}
\]

This is a coefficient-one delayed recurrence; the old factor `1/16` has been
absorbed entirely by the canonical fourth-power scale.

## 3. The recurrence implies the original gate

Assume

\[
 \mathcal E_x(a)\ge\mathcal E_x(2a)
 \tag{T-91005.8}
\]

for every real `x` and positive `a`.  Iterating,

\[
 \mathcal E_x(a)\ge\mathcal E_x(2^Ja).
 \tag{T-91005.9}
\]

By `L-91021`, for every fixed carrier `x` the gate
`G_x(A)` is positive for all sufficiently large `A`.  Therefore the right side
of (T-91005.9) is nonnegative for all sufficiently large `J`.  Consequently

\[
 \mathcal G_x(a)=a^4\mathcal E_x(a)\ge0.
 \]

The Cauchy gate criterion (T-91005.3) then gives RH.

Hence

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal E_x(a)\ge\mathcal E_x(2a)
 \quad\text{for every }x\in\mathbb R,\ a>0.
 }
 \tag{T-91005.10}
\]

## 4. Direct false-RH failure

There is also a local zero-side proof of the reverse implication.  Under false
RH choose a terminal reflected pair

\[
 \rho=\frac12+y+ix,
 \qquad 0<y<\frac12.
\]

At its own ordinate, the contribution to `G_x(a)` tends to `-infinity` as
`a` decreases to `y` from above.  Terminality excludes a nuisance pair at the
same ordinate and doubled depth, which is the only configuration that could
produce the opposite singularity from `G_x(2a)/16`.  Every remaining zero
contribution is bounded or reinforces the negative singularity.  Thus

\[
 \mathcal E_x(a)-\mathcal E_x(2a)<0
\]

for `a>y` sufficiently close to `y`.

So every off-line zero eventually violates one explicit coefficient-one
recurrence row.

## 5. Prime-side normal form

Let

\[
 \mathfrak r_a(t)
 =a\left[
 -\frac14(1+a|t|)e^{-a|t|}
 +\frac{17}{32}(1+2a|t|)e^{-2a|t|}
 -\frac1{16}(1+4a|t|)e^{-4a|t|}
 \right]
 \tag{T-91005.11}
\]

be the physical residual kernel from `L-91022`.  The explicit formula writes

\[
 \mathcal E_x(a)-\mathcal E_x(2a)
 \tag{T-91005.12}
\]

as the completed archimedean/pole contribution of this kernel minus the
absolutely convergent prime-power series

\[
 2a^{-4}\sum_{n\ge2}
 \frac{\Lambda(n)}{\sqrt n}
 \mathfrak r_a(\log n)\cos(x\log n),
 \tag{T-91005.13}
\]

in the resident Guinand--Weil normalization.

The kernel has three decisive structural features:

```text
zero total mass;
three-square Fourier factorization;
high-frequency decay improved from u^-4 to u^-6.
```

Thus the full RH problem on this spine is one source-specific positivity theorem
for a three-port rational wavelet residual, not the original unsplit Cauchy
gate.

## 6. All-generation form

If the recurrence is established prime-side, then

\[
 \boxed{
 \mathcal E_x(a)
 =\mathcal E_x(2^Ja)
  +\sum_{j=0}^{J-1}\mathcal R_x(2^ja).
 }
 \tag{T-91005.14}
\]

The terminal term is eventually nonnegative by `L-91021`; every emitted term
is a positive three-port detail.  This is exactly the coefficient-one,
no-double-spend architecture sought in the earlier Q4 and carry programmes.

## 7. Exact boundary

Closed, subject to review:

```text
sharp normalization a^-4;
RH -> coefficient-one delayed recurrence;
recurrence -> original Cauchy gate -> RH;
direct terminal-pair violation under false RH;
three-port residual prime normal form;
all-generation no-double-spend ledger.
```

Open:

```text
unconditional prime-side positivity of the residual;
source-complete identification of its three ports;
Riemann Hypothesis.
```
