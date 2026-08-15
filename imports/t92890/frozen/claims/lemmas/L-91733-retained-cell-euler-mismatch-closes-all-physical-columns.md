# L-91733 — Retained-cell localization of the Euler mismatch closes every physical column without a cutoff atom

Claim ID: `L-91733`
Status: **PROVED EXACT LOCALIZATION / ALL-COLUMN BOUND ON FROZEN ADJACENT-ERROR AND COLLAR INPUTS**
Created: 2026-08-15
Depends on: `L-91111`, `L-91114`, the factor-67 adjacent bound of `L-91691`, positive radix-four inversion
Compiles: the small-column insight of PR #479 into an actual correction seed
RH status: **unproved**

## 1. The uncovered range

Put

\[
 K=K_X=\left\lfloor\frac X{67}\right\rfloor+1.
\tag{L-91733.1}
\]

The compact theorem at PR #473 proves its relative mismatch estimate for
`q>=K`, and the terminal omission treats `q>X/4`.  It does not cover

\[
 2\le q<K.
\]

A discrepancy supported at seed indices at least `K` still contributes to such
a column through multiples `jq>=K`.

## 2. Localize the discrepancy at the adjacent-cell level

Retain the exact adjacent finite/continuum error

\[
 \varepsilon_X(n)
 =E_X(n)-E_X(n+1)
 =d_X^\star(n)-
  \int_n^{n+1}d_X^\star(t)dt.
\tag{L-91733.2}
\]

Let `I_X` be the finite set of integer endpoint cells actually sent through the
continuum producer and the one global quantizer.  Bottom cells, the fixed top
omission, activation-knot collars and exact inner finite cells are not in
`I_X`.  In particular,

\[
 I_X\subseteq\{n:n\ge K\}.
\tag{L-91733.3}
\]

Define the cumulative retained-cell correction seed

\[
 \boxed{
 E_X^I(n)=
 \sum_{\substack{m\in I_X\\m\ge n}}
 \varepsilon_X(m).
 }
\tag{L-91733.4}
\]

It is exactly the sum of the retained finite cell values minus the integrals of
those same cells.  Complement cells remain literal finite source and are not
continuumized.

Taking one adjacent difference gives

\[
 \boxed{
 E_X^I(n)-E_X^I(n+1)
 =\mathbf1_{I_X}(n)\varepsilon_X(n).
 }
\tag{L-91733.5}
\]

There is no cutoff atom.  By contrast, the naive cumulative-seed truncation
`1_(n>=K)E_X(n)` creates an extra jump at `K-1`.

## 3. Exact all-column carry identity

For every physical ordinary column `q>=2`, the adjacent carry formula gives

\[
\begin{aligned}
 v_q(E_X^I)
 &=\sum_{j\ge1}
   [E_X^I(jq)-E_X^I(jq+1)]\\
 &=\sum_{\substack{j\ge1\\jq\in I_X}}
   \varepsilon_X(jq).
\end{aligned}
\]

Thus

\[
 \boxed{
 v_q(E_X^I)=
 \sum_{jq\in I_X}\varepsilon_X(jq).
 }
\tag{L-91733.6}
\]

This is an actual seed realization of the outer mismatch response, including
when `q<K`.  No discarded cell is assigned to an undeclared recursive owner.

## 4. Uniform ordinary and radix-four bounds

On every retained factor-67 cell, the frozen adjacent estimate is

\[
 |\varepsilon_X(n)|<\frac{19}{2}n^{-3/2}.
\tag{L-91733.7}
\]

Put

\[
 M_q=\left\lceil\frac Kq\right\rceil.
\]

Since

\[
 \sum_{j\ge M}j^{-3/2}<3M^{-1/2},
\]

(L-91733.6) gives, for every `q>=2`,

\[
\begin{aligned}
 |v_q(E_X^I)|
 &<\frac{19}{2}q^{-3/2}
   \sum_{j\ge M_q}j^{-3/2}\\
 &<\frac{57}{2}q^{-3/2}M_q^{-1/2}\\
 &\le\frac{57}{2q\sqrt K}.
\end{aligned}
\]

Hence

\[
 \boxed{
 |v_q(E_X^I)|<\frac{57}{2q\sqrt K}
 \qquad(q\ge2).
 }
\tag{L-91733.8}
\]

Applying this at `q` and `4q` gives

\[
 \boxed{
 |\mathcal D_4v_q(E_X^I)|
 <\frac{171}{4q\sqrt K}.
 }
\tag{L-91733.9}
\]

## 5. Add the positive B-spline collar

The frozen all-column collar estimate is

\[
 |\mathcal D_4v_q(C_X)|
 <\frac{200}{q\sqrt K}
 \qquad(q\ge2).
\tag{L-91733.10}
\]

Therefore

\[
 \boxed{
 |\mathcal D_4v_q(C_X-E_X^I)|
 <\frac{971}{4q\sqrt K}.
 }
\tag{L-91733.11}
\]

For every nonterminal column `2<=q<=X/4`,

\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}
 >\frac4{3\sqrt q}.
\]

The exact integer comparison

\[
 2913^2<2(16\cdot129)^2
\]

gives

\[
 \boxed{
 \frac{|\mathcal D_4v_q(C_X-E_X^I)|}
      {\Omega_X(q)}
 <\frac{129}{\sqrt K}.
 }
\tag{L-91733.12}
\]

This includes the entire missing range `2<=q<K`.

## 6. One source-owned square-root thinning

Use

\[
 \tau_K=\frac{\sqrt K}{\sqrt K+130}
\tag{L-91733.13}
\]

once on the retained positive common-parent measure.  Conditional on the frozen
one-use ideal identity reserving the full child capacities, the ideal current
plus children uses at most `Omega_X`.  Hence

\[
 \Xi_{\rm realized}(q)
 <\tau_K
   \left(1+\frac{129}{\sqrt K}\right)
   \Omega_X(q)
 =\frac{\sqrt K+129}{\sqrt K+130}
  \Omega_X(q).
\]

Thus every nonterminal physical column has strict reserve

\[
 \boxed{
 s_X(q)>
 \frac{\Omega_X(q)}{\sqrt K+130}>0
 \qquad(2\le q\le X/4).
 }
\tag{L-91733.14}
\]

Positive radix-four inversion gives ordinary feasibility from the same one-use
detail inequality.

## 7. Terminal compatibility

For `K>=2`,

\[
 \tau_K\le\frac K{K+178},
\]

because this is equivalent to `178 sqrt(K)<=130K`, whose square follows from
`178^2<=2*130^2`.  The stronger thinning therefore cannot weaken the frozen
top-omission proof.  Its terminal margin remains at least

\[
 581X^{-3/2}.
\]

Above the retained endpoint support, triangularity still gives exactly zero
response.

## 8. Ownership boundary

```text
retained adjacent cell                   one current Euler correction owner
omitted bottom/top/knot cell             literal unused or exact finite source
small physical column q<K                samples only retained cells in (L-91733.6)
naive cumulative cutoff                  forbidden: creates a K-1 atom
full-child/current capacity identity     frozen producer input
all-column analytic constants            exact on frozen adjacent/collar bounds
Riemann Hypothesis                        unproved
```
