# R-92920 — The `q=2` rough-lift separator is exact, but its unconditional application is withdrawn

Claim ID: `R-92920`  
Status: **PROVED EXACT CONDITIONAL SEPARATOR AND SCOPE CORRECTION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Frozen comparison heads: PR #496 `96f8a6b3cc3d474217633e16d4caa490a0aae518`; PR #500 `d73c1e7a1a482cac31581211a84db43cc34c824e`  
Primary inputs: `L-91377`, `L-91379`, `L-91688`, `L-91733`, `L-91756`  
RH status: **unproved**

## 1. Scope correction

An earlier chat answer asserted that a `109/1200` excess at the physical column
`q=2` refuted the one-shot construction.  That assertion was never deposited in
PR #496.  More importantly, it omitted a load-bearing hypothesis: the physical
coupling must actually have the **full `P_61` rough lift** as its pre-correction
output marginal.

This file supplies the exact conditional theorem and withdraws its use as an
unconditional falsifier of PR #496 or PR #500.

## 2. Native datum and rough lift

Let `N_X` denote the native packet of `L-91377` and let

\[
 \mathfrak D_X
 =\sum_{m\in\mathcal R_{67}}m^{-1/2}N_{X/m}
\]

be its canonical `P_61` rough lift.  At `q=2`, for every `Y>=8`,

\[
 \Omega_Y(2)
 =w_Y(2)-2w_Y(8)
 =\frac{\log4}{\sqrt2}.
\tag{R-92920.1}
\]

Hence, when `X>=536`, the terms `m=1` and `m=67` alone give

\[
 \boxed{
 \frac{\Xi(\mathfrak D_X;2)}{\Omega_X(2)}
 \ge 1+\frac1{\sqrt{67}}.
 }
\tag{R-92920.2}
\]

All further rough terms are nonnegative in this coordinate.

## 3. Exact retained excess at `X=10^16`

Set

\[
 X_0=10^{16},\qquad
 K=\left\lfloor\frac{X_0}{67}\right\rfloor+1
 =149253731343284,
\]

and use the frozen one-shot thinning

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

The exact integer checks

\[
 12216944^2<K,
 \qquad
 67\cdot61^2<500^2
\]

imply

\[
 \sqrt K>12216944,
 \qquad
 \frac1{\sqrt{67}}>\frac{61}{500}.
\]

Therefore

\[
\begin{aligned}
 \tau_K\left(1+\frac1{\sqrt{67}}\right)-1
 &>
 \frac{12216944}{12216944+130}\frac{561}{500}-1\\
 &=\frac{31048691}{254522375}\\
 &>\frac7{75}.
\end{aligned}
\tag{R-92920.3}
\]

Thus a thinned full rough-lift marginal has ideal normalized excess greater
than `7/75` at `q=2`.

## 4. The frozen realization allowances are below `1/400`

The retained-cell mismatch and intrinsic collar satisfy

\[
 \frac{|e^{\rm nonterm}_{X_0}(2)|}{\Omega_{X_0}(2)}
 <\frac{129}{12216944}.
\tag{R-92920.4}
\]

For the literal bottom width two and top width `10002`, the frozen endpoint
score-density bounds give

\[
 H_{\rm omit}
 <\frac{32}{12216944}
  +\frac{160032}{99999999}.
\tag{R-92920.5}
\]

The elementary atanh expansion gives

\[
 \log2
 =2\sum_{n\ge0}\frac1{(2n+1)3^{2n+1}}
 >\frac{56}{81},
\]

while `sqrt(2)>7/5`.  Since

\[
 Y_4(2)=\log2,
 \qquad
 \Omega_{X_0}(2)=\sqrt2\log2,
\]

we have

\[
 Y_4(2)\Omega_{X_0}(2)
 >\frac{21952}{32805}.
\tag{R-92920.6}
\]

The omission is a positive row, so exact `Y_4` duality gives

\[
 \frac{\Xi_{\rm omit}(2)}{\Omega_{X_0}(2)}
 <
 \left(
  \frac{32}{12216944}
  +\frac{160032}{99999999}
 \right)
 \frac{32805}{21952}.
\tag{R-92920.7}
\]

The terminal comparison contributes at most

\[
 \frac{4452X_0^{-3/2}}{\Omega_{X_0}(2)}
 <\frac{4452\cdot405}{10^{24}\cdot392},
\tag{R-92920.8}
\]

because `Omega_(X_0)(2)>392/405`.  Exact rational addition gives

\[
\begin{aligned}
 &\frac{129}{12216944}
 +\left(
  \frac{32}{12216944}
  +\frac{160032}{99999999}
 \right)\frac{32805}{21952}
 +\frac{4452\cdot405}{10^{24}\cdot392}\\
 &\qquad=
 \frac{2800576272675862505353999298560006479}
 {1164003263915522800000000000000000000000}\\
 &\qquad<\frac1{400}.
\end{aligned}
\tag{R-92920.9}
\]

This is an exact audit of every advertised downward allowance relevant at
`q=2` under the rough-lift hypothesis.

## 5. The exact conditional separator

Combining (R-92920.3) and (R-92920.9), any construction whose ideal retained
marginal is the full rough lift satisfies

\[
 \boxed{
 \frac{\Xi(d_{X_0};2)-\Omega_{X_0}(2)}
      {\Omega_{X_0}(2)}
 >\frac7{75}-\frac1{400}
 =\frac{109}{1200}>0.
 }
\tag{R-92920.10}
\]

Thus the `109/1200` separator is mathematically correct for a rough-lift output
marginal.

## 6. Why this is not yet a falsifier of PR #500

PR #500 claims that the internal child colours are **actual paired stopping-line
children**, physically placed with their source orientation retained.  Such a
coupling need not have `mathfrak D_X` as its output marginal.  The paired swap
may contribute the negative signed rough-reservoir observation needed to reduce
`mathfrak D_X` back to `N_X`.

The frozen PR #500 text does not display that native-versus-rough commuting
square explicitly, and its synthetic replay does not encode the paired parity
orientation.  Therefore the correct verdict is:

```text
109/1200 as a theorem about a full rough-lift marginal     PROVED EXACT
109/1200 as an unconditional refutation of PR #496         WITHDRAWN
109/1200 as an unconditional refutation of PR #500         WITHDRAWN
missing discriminator in PR #500                           PAIRED ORIENTATION
rough-lift interpretation of PR #500                       REFUTED BY THIS FILE
native paired interpretation of PR #500                    REPAIRED IN L-92920/L-92921
Riemann Hypothesis                                         UNPROVED
```
