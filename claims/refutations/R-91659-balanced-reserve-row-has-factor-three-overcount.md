# R-91659 — The balanced/reserve row observation carries a factor-three overcount

Claim ID: `R-91659`  
Status: **EXACT ALGEBRAIC REFUTATION AND NORMALIZATION FIREWALL**  
Created: 2026-08-14  
Refutes on PR #455: `L-91668.10--11` and every conclusion which uses that
identification without a new normalization theorem.  
Replacement: `L-91670`, `L-91671`, `T-91656`  
RH status: **unproved**

## 1. Exact calculation

For a squarefree source atom `n`, put `Y=X/n` and

\[
 w_a(X,n)=\frac1{\sqrt n}(a\sqrt Y-1).
\]

The balanced/reserve split is

\[
w_\Psi=(1+\kappa_*)w_{a_*}+(2-\kappa_*)w_1.
\tag{R-91659.1}
\]

The normalized component profile cited by `L-91330` is

\[
\mathcal Q_{j,a}(Y)=\frac{Q_Y(j)}{a\sqrt Y-1}.
\tag{R-91659.2}
\]

Therefore one labelled channel has physical row observation

\[
w_a(X,n)\mathcal Q_{j,a}(Y)
=\frac1{\sqrt n}Q_Y(j).
\tag{R-91659.3}
\]

After the positive channel coefficients in (R-91659.1) are restored, the sum
is

\[
\begin{aligned}
 &(1+\kappa_*)w_{a_*}\mathcal Q_{j,a_*}
 +(2-\kappa_*)w_1\mathcal Q_{j,1}\\
 &\qquad=
 [(1+\kappa_*)+(2-\kappa_*)]\frac1{\sqrt n}Q_Y(j)\\
 &\qquad=3\frac1{\sqrt n}Q_Y(j).
\end{aligned}
\tag{R-91659.4}
\]

The factor `3` is independent of `\zeta(1/2)` and cannot be removed by a
numerical enclosure.

After the parity observation, the old root row is therefore

\[
3\frac{\mu(n)}{\sqrt n}Q_{X/n}(j),
\]

not one copy. Summing gives `3c_X`, not `c_X`.

## 2. Scope

The atomwise target split (R-91659.1) remains correct. The failure is the
identification of the two separately normalized row channels with one native
component row.

The following are rejected as review targets:

```text
L-91668.10--11
L-91668.17--20 insofar as they identify the row with c_X
L-91669 and T-91655 as conclusion chains depending on that row identity
```

The source-tree and fixed-67 theorems survive at their proper scopes.

## 3. Correct replacement

Use the single SHARP channel

\[
w_\Psi=3w_{4/3}
=\frac1{\sqrt n}(4\sqrt Y-3)
\]

with the single normalized row profile

\[
\mathcal H_{\Psi,j}(Y)
=\frac{Q_Y(j)}{4\sqrt Y-3}
=\frac13\mathcal Q_{j,4/3}(Y).
\]

Then

\[
w_\Psi\mathcal H_{\Psi,j}
=\frac1{\sqrt n}Q_Y(j)
\]

exactly. This is `L-91670`.

```text
balanced/reserve target identity                  RETAINED
balanced/reserve row identity as one c_X           FALSE
single-SHARP target/score/row normalization        REPLACEMENT
Riemann Hypothesis                                 UNPROVED
```
