# O-19855 — Three-front continuation: balanced rough ray, Fisher–Hankel compression, and Stein-variability defect

Claim ID: `O-19855`  
Status: **LIVE CROSS-BRANCH SYNTHESIS — ALL CONCLUSION-BEARING STEPS REMAIN SUBJECT TO REVIEW**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Purpose

This record freezes the continuation after the three-front portfolio of
`O-19854`.  The live branches have moved materially:

1. the factor-54 programme has closed all finite analytic/discrete collars;
2. the Suzuki programme has an exact completed Fisher factorization through the
   model-space tangent;
3. the Brownian programme has large unconditional positive cones and one exact
   Stein-kernel obstruction.

No branch proves RH.

## 2. Arithmetic front — only the rough allocation survives

On PR #399, `L-91114/L-91115` now pay:

```text
finite target/continuum mismatch;
positive B-spline quantization collar;
complete tapering terminal annulus;
```

with nonnegative endpoint weights and bounded score debt.  `R-91102` remains
the mandatory correction refuting the false exact finite/Volterra row peel.

The only remaining reset operation is the delayed rough-prime state allocation.

### 2.1 Exact diagonal basis

`L-91311` proves

\[
 X=L-R=\sqrt x B(x),
 \qquad
 Y=L-2R=A(x),
\]

and diagonal rough renewals

\[
 \sum_{m\in\mathcal M_{59}}m^{-1/2}X(x/m)
 =\delta_{53}\sqrt x,
\]

\[
 \sum_{m\in\mathcal M_{59}}m^{-1/2}Y(x/m)
 =\beta_{53}.
\]

Thus the rough operator has exactly one square-root mode and one constant mode.

### 2.2 Unique balanced interior ray

Put `z0=zeta(1/2)` and

\[
 \kappa_*
 =-\frac{2(1+z_0)}{2+z_0},
 \qquad
 c_*=\frac1{2+z_0}.
\]

Then

\[
 H_*=L+\kappa_*R,
 \qquad
 E_*=H_*-c_*
\]

is the unique affine state cancelling both rough neutral modes.  `L-91315`
identifies these modes as:

```text
constant-mode residue at s=0;
endpoint entropy score 2 fhat(1/2).
```

Moreover

\[
 0<\kappa_*<2,
 \qquad
 \Psi=L+2R=H_*+(2-\kappa_*)R.
\]

So the balanced ray lies strictly inside the available positive output wedge.
Its complete rough discrepancy is one finite small-prime boundary port of size
`O(x^-1/2)`, whose scalar accumulation across factor-54 generations is bounded.

The open theorem is now a full-column realization of this balanced branching,
not a search for the correct scalar normalization.

## 3. Suzuki front — model-space projection is now explicit

On PR #400, `L-91312` writes the boundary phase tangent as a completed Fisher
covariance.  If

\[
 \varphi_a(t)=\mathbb E_a e^{itY},
 \qquad
 \Theta_a(t)=\varphi_a(-t)/\varphi_a(t),
\]

and

\[
 h_{a,t}(Y)
 =\frac{e^{-itY}}{\varphi_a(-t)}
  -\frac{e^{itY}}{\varphi_a(t)},
\]

then

\[
 \partial_a\log\Theta_a(t)
 =-\mathbb E_a[(Y-\mathbb E_aY)h_{a,t}(Y)].
\]

`L-91316` passes this identity through the Suzuki model-space projection.  For
`g in K_(Theta_a)`, define

\[
 (\mathcal A_ag)(Y)
 =P_+[h_{a,\cdot}(Y)\overline{\Theta_a}g].
\]

Then

\[
 \boxed{
 \mathcal J_a
 =a\sqrt{2\operatorname{Var}_a(Y)}\,
  \mathcal C_a\mathcal A_a,
 \qquad
 \|\mathcal C_a\|\le1,
 }
\]

and hence

\[
 \mathcal J_a^*\mathcal J_a
 \preceq
 2a^2\operatorname{Var}_a(Y)\mathcal A_a^*\mathcal A_a.
\]

The source-minus-output defect is explicit and positive.

`R-91011` is the mandatory scope correction: arbitrary raw delay modulation
need not preserve `K_(Theta_a)`.  Full polarization among resident model-space
vectors is exact, but the physical delay/orientation-to-model-space intertwiner
and finite bridge remain open.

The remaining source theorem is the concrete comparison

```text
Jordan + gamma + pole first-chaos norm
    >= completed Fisher-Hankel norm.
```

## 4. Brownian front — large positive sectors and one exact defect

On PR #401:

- `L-91314` proves Brownian reflection positivity for every real test satisfying
  `F>=0` and `F'>=0`;
- `L-91318` proves the mixed cross term is nonnegative between any two tests in
  that cone;
- `L-91317` proves a signed SOS sector obtained from
  \[
  F_P(x)=\int_{-\infty}^xe^{r_0t}|P(e^{dt})|^2dt,
  \]
  allowing arbitrary polynomial phases and signed exponential coefficients of
  unbounded support.

Thus the obstruction is not simply one negative coefficient.

### 4.1 Canonical Stein normal form

`L-91319` introduces the canonical Stein kernel `tau_u` of the completed tilt.
For the reflection observable `A_F`,

\[
\begin{aligned}
 \operatorname{Re}\operatorname{Cov}_u^{(2)}(\mathcal A_F,S)
 ={}&V_u\big(
  |\mathbb E_uF(Z)|^2+|\mathbb E_uF(-Z)|^2
 \big)\\
 &+\operatorname{Re}\mathcal D_u(F),
\end{aligned}
\]

where `V_u=Var_u(Z)` and

\[
 \mathcal D_u(F)
 =\mathbb E[
  (\tau_u(Z_1)-V_u)\partial_1\mathcal A_F
 +(\tau_u(Z_2)-V_u)\partial_2\mathcal A_F].
\]

The first line is a universal positive Gaussian rank-two bulk.  Every arbitrary
complex interference obstruction lies in the fluctuation of the Stein kernel
away from its constant mean.  A quantitative defect bound is explicit.

The next Brownian theorem is therefore:

```text
theta/Gamma-Beta curvature dominates the Stein-variability defect,
pointwise in the tilt or after integration.
```

## 5. Shared architecture after the continuation

The three frontiers now align more sharply:

| Front | Positive bulk | Exact residual obstruction |
|---|---|---|
| factor-54 | balanced `H_*` rough ray | finite column realization of the complementary boundary state |
| Suzuki | completed Fisher-Hankel Gram | Jordan/gamma/pole source-norm comparison plus delay/bridge intertwining |
| Brownian | Gaussian rank-two Fisher bulk and monotone/SOS cones | variable Stein-kernel interference defect |

Each route has removed the scalar normalization ambiguity.  Each survivor is a
structured cross-channel norm comparison.

## 6. Exact status

```text
factor-54 finite collars                         CLOSED / PROPOSED COMPLETE
unique rough mass-and-score neutral ray          EXACT
rough balanced full-column allocation            OPEN / RH-BEARING
Suzuki model-space Fisher factorization           EXACT
arbitrary-delay invariance                        REFUTED / CORRECTED
Jordan/gamma/pole vs Fisher-Hankel norm            OPEN / RH-BEARING
Brownian monotone and signed SOS sectors           EXACT POSITIVE
Brownian Stein-variability normal form             EXACT
Stein-defect domination                            OPEN / RH-BEARING
Riemann Hypothesis                                UNPROVED
```
