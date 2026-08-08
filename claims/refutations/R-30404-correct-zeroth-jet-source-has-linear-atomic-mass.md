# R-30404 — The correctly inverted zeroth Euler jet has linear atomic mass

Claim ID: `R-30404`  
Title: Even after repairing the source type by exact multiples-Möbius inversion, one stopped endpoint contributes `Omega(N)` critical atomic norm in the zeroth common-tail jet  
Status: **EXACT STRONG REFUTATION OF THE POLYLOGARITHMIC BOUNDARY-NORM CLAIM**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`  
Primary targets: `L-30403.3--.8`, `T-30401.4`  
Dependencies: `R-30403`; PR #286 exact zeroth Euler coefficient; PR #301 common-tail positivity; elementary Möbius inversion  
Scope: one stopped pure-power endpoint and the legitimate divisor-source coordinate; no assertion about every coupled non-atomic flow representation

## 1. The zeroth common-tail boundary vector

Fix a stopped endpoint `N` and the critical pure power `s=1/2`. On the interval

\[
 I_N=
 \left\{
 q\in\mathbb Z:
 \left\lfloor\frac{N+1}{4}\right\rfloor+1
 \le q\le
 \left\lfloor\frac N3\right\rfloor
 \right\},
\tag{R-30404.1}
\]

the shifted-even and unshifted-odd omitted tails start together at `k=2`.

The zeroth Euler jet of the recombined common tail is therefore

\[
 \boxed{
 h_N(q)=\frac12\left[
 \frac{(4q-1)^{-1/2}}4
 -\frac{(5q)^{-1/2}}5
 \right]
 \qquad(q\in I_N).
 }
\tag{R-30404.2}
\]

Every term is positive. This is an actual boundary vector indexed by the output carry column `q`; unlike the ill-typed source in `L-30402`, it is not yet a divisor source.

## 2. Correct divisor-source inversion

Let

\[
 Q_N=\left\lfloor\frac N2\right\rfloor
\]

be the output endpoint. The unique divisor source whose floor transform equals `h_N` on `2<=q<=Q_N` is

\[
 \boxed{
 \sigma_N(m)
 =\sum_{d\le Q_N/m}\mu(d)h_N(md).
 }
\tag{R-30404.3}
\]

For every `m in I_N`, one has `m>N/4`, hence

\[
 2m>Q_N.
\]

Only the term `d=1` occurs in (R-30404.3). Therefore

\[
 \boxed{
 \sigma_N(m)=h_N(m)>0
 \qquad(m\in I_N).
 }
\tag{R-30404.4}

This is a source identity, not an estimate.

## 3. A uniform positive atomic contribution per source node

For `m in I_N`, multiply (R-30404.2) by `sqrt(m)`:

\[
 \sqrt m\,\sigma_N(m)
 =\frac12\left[
 \frac1{4\sqrt{4-1/m}}
 -\frac1{5\sqrt5}
 \right].
\tag{R-30404.5}
\]

Since

\[
 \frac1{4\sqrt{4-1/m}}\ge\frac18
\]

and

\[
 \frac1{5\sqrt5}<\frac9{100},
\]

one obtains the explicit lower bound

\[
 \boxed{
 \sqrt m\,|\sigma_N(m)|
 >\frac7{400}.
 }
\tag{R-30404.6
}

The second inequality is exact after squaring:

\[
 \frac1{125}<\frac{81}{10000}.
\]

## 4. Linear lower bound

For `N>=48`,

\[
 |I_N|
 =\left\lfloor\frac N3\right\rfloor
 -\left\lfloor\frac{N+1}{4}\right\rfloor
 \ge\frac N{24}.
\tag{R-30404.7}
\]

Consequently the correct critical atomic norm satisfies

\[
 \begin{aligned}
 \|\sigma_N\|_{\rm at}
 &=\sum_{m\le Q_N}\sqrt m\,|\sigma_N(m)|\\
 &\ge\sum_{m\in I_N}\sqrt m\,|\sigma_N(m)|\\
 &>\frac7{400}|I_N|\\
 &\ge\frac{7N}{9600}.
 \end{aligned}
\tag{R-30404.8}

In particular,

\[
 \boxed{
 \|\sigma_N\|_{\rm at}>\frac N{2000}
 \qquad(N\ge48).
 }
\tag{R-30404.9}

This is incompatible with every fixed polylogarithmic upper bound.

## 5. Why other Euler channels do not remove the witness

The interval `I_N` is a common-tail sector, so there is no unmatched odd collar there. PR #301 `L-29808` proves that all common-tail finite differences and the exact Euler remainder have nonnegative source coefficients after even/odd recombination. The positive stopped-endpoint resolution also has positive weights.

Thus the zeroth-jet source in (R-30404.4) is not canceled by another common-tail jet before the atomic norm is taken. Adding the remaining positive common-tail channels can only increase the source coefficient on this sector.

## 6. Consequence for the proposed proof

The frozen proof asserted that the complete first-generation source obeys

\[
 \|\sigma_0\|_{\rm at}=\operatorname{polylog}(N).
\]

The correctly typed source instead satisfies the linear lower bound (R-30404.9). Therefore:

```text
finite boundary vector
-> exact Möbius divisor source
-> absolute adjacent-tree termination
```

cannot produce polylogarithmic Cycle Debt.

This conclusion does not depend on the q-dependent source error of `R-30403`; it survives after that error is repaired.

## 7. Correct remaining problem

A viable completion must avoid the absolute atomic norm of the zeroth common tail. It must retain a coupled cancellation or an actual relative capacity at the complete source level before Möbius inversion and absolute values. The required result is a substantive source-bound flow theorem, not a finite manifest audit.

## 8. Corrected status

```text
correct Möbius-inverted zeroth source       PROPOSED COMPLETE EXACT
its atomic norm                             Omega(N)
polylog complete boundary norm              FALSE
absolute terminal adjacent-tree completion  FALSE
coupled zeroth-tail flow theorem             OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```
