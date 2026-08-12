# R-91324 — The normalized Fisher–Hankel feature has trivial natural boundary-L2 core

Claim ID: `R-91324`  
Status: **EXACT DOMAIN REFUTATION OF `L-91316.11`--`L-91316.17` AS A BOCHNER-L2 CONSTRUCTION**  
Created: 2026-08-13  
Refutes: the declared dense-core Hilbert operator in `L-91316`  
Preserves: the finite-carrier covariance identity `L-91312.10` and the model-space identity `L-91316.7`  
Repaired by: `L-91325`  
RH status: **unproved**

## 1. The issue

Fix `a>1/2`, put

\[
 \sigma=\frac12+a>1,
 \qquad
 \varphi_a(t)=\frac{\xi(\sigma-it)}{\xi(\sigma)},
 \tag{R-91324.1}
\]

and retain

\[
 h_{a,t}(Y)
 =\frac{e^{-itY}}{\varphi_a(-t)}
  -\frac{e^{itY}}{\varphi_a(t)}.
 \tag{R-91324.2}
\]

`L-91316.11` proposes, on a common dense core in `K_(Theta_a)`,

\[
 (\mathcal A_ag)(Y)
 =P_+\!\bigl[h_{a,\cdot}(Y)\mathcal U_{\Theta_a}g\bigr]
 \in H^2,
 \tag{R-91324.3}
\]

as a Bochner `L2(P_a;H2)` feature map. The standard Riesz projection in
(R-91324.3) can be applied by that construction only after the boundary
multiplier belongs to `L2(P_a;L2(R))`.

The maximal natural domain for that pre-projected multiplier is in fact
trivial.

## 2. The completed characteristic amplitude decays exponentially

For fixed `sigma>1`, the completed zeta formula is

\[
 \xi(s)
 =\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
 \tag{R-91324.4}
\]

On the line `Re(s)=sigma`, absolute convergence gives

\[
 |\zeta(\sigma-it)|\le\zeta(\sigma).
\]

Uniform Stirling estimates therefore give constants `C_a,M_a>0` such that

\[
 \boxed{
 |\varphi_a(t)|
 \le C_a(1+|t|)^{M_a}e^{-\pi|t|/4}
 \qquad(t\in\mathbb R).
 }
 \tag{R-91324.5}
\]

For example, one may take any `M_a` larger than
`(1/2+a)/2+3/2`. In particular,

\[
 \varphi_a(t)\longrightarrow0
 \qquad(|t|\to\infty).
 \tag{R-91324.6}
\]

No lower bound for `zeta` is needed here. The safe-line nonvanishing is used
only to make the reciprocal well defined.

## 3. The normalized phase variance grows exponentially

The exact diagonal covariance formula of `L-91312.15` is

\[
 \mathcal H_a(t,t)
 =2\left[
  \frac1{|\varphi_a(t)|^2}
  -\operatorname{Re}
   \frac{\varphi_a(2t)}{\varphi_a(t)^2}
 \right].
 \tag{R-91324.7}
\]

Hence

\[
 \mathcal H_a(t,t)
 \ge
 \frac{2(1-|\varphi_a(2t)|)}{|\varphi_a(t)|^2}.
 \tag{R-91324.8}
\]

By (R-91324.6), there is `T_a` such that
`|varphi_a(2t)|<=1/2` for `|t|>=T_a`. Thus

\[
 \mathcal H_a(t,t)
 \ge\frac1{|\varphi_a(t)|^2}
 \qquad(|t|\ge T_a).
 \tag{R-91324.9}
\]

Combining this with (R-91324.5), for every `0<gamma<pi/2` there are constants
`c_(a,gamma)>0` and `T_(a,gamma)` such that

\[
 \boxed{
 \mathcal H_a(t,t)
 \ge c_{a,\gamma}e^{\gamma|t|}
 \qquad(|t|\ge T_{a,\gamma}).
 }
 \tag{R-91324.10}
\]

The finite-carrier covariance remains perfectly meaningful. The obstruction
appears only when the normalized features are integrated over the whole Hardy
boundary.

## 4. A Hardy boundary function cannot have two-sided exponential decay

### Lemma

If `g in H2(C_+)` and, for some `gamma>0`,

\[
 \int_{\mathbb R}e^{\gamma|t|}|g(t)|^2dt<\infty,
 \tag{R-91324.11}
\]

then `g=0`.

### Proof

By the Paley--Wiener theorem, the inverse Fourier transform of the boundary
value of `g` is supported on one closed half-line. Choose `0<delta<gamma/2`.
Cauchy--Schwarz gives

\[
 \int_{\mathbb R}|g(t)|e^{\delta|t|}dt<\infty.
 \tag{R-91324.12}
\]

Therefore the inverse Fourier integral extends holomorphically to the strip
`|Im z|<delta`. On the real axis it agrees almost everywhere with the
one-sided Paley--Wiener representative, hence vanishes almost everywhere on an
open half-line. Continuity makes that vanishing pointwise there, and the
identity theorem makes the strip function identically zero. Therefore `g=0`.

## 5. The natural multiplier core is exactly zero

Before applying `P_+`, define

\[
 (\widetilde{\mathcal A}_ag)(Y,t)
 =h_{a,t}(Y)(\mathcal U_{\Theta_a}g)(t).
 \tag{R-91324.13}
\]

Since `|U_(Theta_a)g|=|g|` on the boundary and
`E_a|h_(a,t)|^2=H_a(t,t)`, Tonelli gives

\[
 \boxed{
 \|\widetilde{\mathcal A}_ag\|_{L^2(P_a\times dt)}^2
 =\int_{\mathbb R}\mathcal H_a(t,t)|g(t)|^2dt.
 }
 \tag{R-91324.14}
\]

If the right side is finite, (R-91324.10) implies (R-91324.11) for some
`gamma>0`. The lemma then gives `g=0`. Conversely the zero vector is in the
domain. Hence

\[
 \boxed{
 \operatorname{Dom}(\widetilde{\mathcal A}_a)
 =\{0\}.
 }
 \tag{R-91324.15}
\]

There is therefore no nonzero, let alone dense, core on which
`L-91316.11` is obtained by applying the bounded Riesz projection to an
`L2(P_a;L2)` boundary multiplier.

## 6. Consequences for `L-91316`

The following claims in `L-91316` are not established as Hilbert-space
statements by the declared construction:

```text
A_a: K_Theta -> L2(P_a;H2) on a common dense core;
J_a = a sqrt(2 V_a) C_a A_a as a bounded-source factorization;
J_a*J_a <= 2 a^2 V_a A_a*A_a;
the positive score-orthogonal reserve built from A_a;
the delayed direct-integral Fisher-Hankel Gram.
```

A distributional or analytically regularized `P_+` could conceivably assign a
finite value after cancellation. This theorem does not rule out such a new
operator. It proves that it is not the Bochner-`L2` operator asserted in
`L-91316`, and that the contraction argument cannot use the infinite raw
feature norm.

The pointwise finite-carrier identity

\[
 \partial_a\log\Theta_a(t)
 =-\mathbb E_a[\sigma_a h_{a,t}]
\]

remains exact. So does the separate model-space Hankel identity
`L-91316.7`. What fails is their proposed merger through one normalized
`L2(P_a;H2)` feature map.

## 7. Repair direction

The blow-up is caused entirely by the reciprocal completed amplitude in
`h_(a,t)`. Multiplying the feature by `varphi_a(t)` produces a uniformly
bounded centered feature. `L-91325` carries out that renormalization and shows
that the exact phase tangent then factors through an explicit unbounded
reciprocal-amplitude Toeplitz leg. The amplification cannot be discarded by
data processing; it is the new load-bearing analytic object.

## 8. Exact boundary

```text
finite-carrier Fisher covariance identity               RETAINED
safe-line exponential decay of varphi_a                  EXACT
exponential growth of H_a(t,t)                           EXACT
nonzero H2 function with two-sided exponential decay     IMPOSSIBLE
natural pre-projected normalized-feature L2 core         {0}
L-91316 dense-core Bochner operator                      REFUTED AS WRITTEN
possible distributional regularization                   NOT RULED OUT
bounded renormalized replacement                         L-91325
Riemann Hypothesis                                       UNPROVED
```
