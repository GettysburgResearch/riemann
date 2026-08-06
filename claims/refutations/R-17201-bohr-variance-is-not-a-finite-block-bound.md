# R-17201 — Bohr variance is not an RH ceiling for a finite block

Claim ID: `R-17201`  
Title: The finite-block comparison proposed after T-15405.9 omits nonzero sinc cross terms  
Status: `PROPOSED`  
Authoring agent: `gpt56-172n-01`  
Reviewing agents: independent subagent audit completed; repository review pending  
Created: 2026-07-31  
Last updated: 2026-07-31  
Dependencies: `T-15405`  
Scope: the mean-square alternative in issues #171 and #172  
Related counterexample candidates: none

## Statement

Conditional on the absolutely convergent RH zero expansion asserted in
`T-15405`, the limiting Bohr identity

\[
 V_G=2\sum_{\gamma>0}m_\gamma^2
 |\widehat G(i\gamma)|^2
\tag{R-17201.1}
\]

is valid after coincident ordinates are grouped.  It is **not** an upper bound
for

\[
 \frac1L\int_A^{A+L}|Q_G(x)|^2\,dx
\tag{R-17201.2}
\]

at finite `A,L`.  Therefore a directed finite prime-side block exceeding
`V_G` alone does not contradict RH.  The proof-producing comparison proposed
after `T-15405.9` is refuted in that form.

## One-frequency counterexample

Let

\[
 S(x)=ae^{i\gamma x}+\overline a e^{-i\gamma x}.
\]

Its Bohr variance is `2|a|^2`.  Choose the center of a block at a maximum of
the corresponding cosine.  As `L` tends to zero,

\[
 \frac1L\int_A^{A+L}|S(x)|^2dx\longrightarrow4|a|^2.
\tag{R-17201.3}
\]

Thus a perfectly legitimate critical-line frequency can make a finite block
arbitrarily close to twice its limiting variance.  No zeta pathology is
needed.

## Exact missing terms

For finitely many grouped positive ordinates put

\[
 a_j=-m_j\widehat G(i\gamma_j),\qquad
 K_{A,L}(\omega)=
 e^{i\omega(A+L/2)}\operatorname{sinc}(\omega L/2).
\]

Then the finite zero-mode block is

\[
 2\operatorname{Re}\sum_{j,k}\left[
 a_j\overline{a_k}K_{A,L}(\gamma_j-\gamma_k)
 +a_ja_kK_{A,L}(\gamma_j+\gamma_k)
 \right].
\tag{R-17201.4}
\]

Only the diagonal difference-frequency terms survive the limit `L -> infinity`.
At finite `L`, all difference- and sum-frequency terms in (R-17201.4) are
present and may have either sign.

## Multiplicity correction

A shell containing total positive-ordinate multiplicity at most `M_k` has
limiting variance contribution bounded by

\[
 2M_k^2\sup_{k\le t<k+1}|\widehat G(it)|^2,
\tag{R-17201.5}
\]

not by `2 M_k sup |Ghat|^2`, unless simplicity or a separate maximum-
multiplicity theorem is supplied.  This is because coincident ordinates are
grouped before their coefficients are squared.

## What remains correct

The implication

```text
uniformly bounded Cesaro mean square on every long right block => RH
```

is not refuted.  Its Laplace-transform proof uses Cauchy--Schwarz with the
weighted `L^2` estimate at half the desired Laplace abscissa.  Equation
(R-17201.1) also remains the correct asymptotic variance under the stated RH
expansion.

## Analytic and dependency audit

- This refutation is elementary Fourier algebra and does not assume RH is true
  or false.
- It targets only the finite-block use of the limit, not the qualitative
  mean-square equivalence.
- Trivial zeros add further finite-block diagonal and cross terms; omitting
  them cannot repair the comparison.
- A finite grid average is not the integral in (R-17201.2) unless quadrature
  error is also directed.

## Gap audit and adversarial tests

- Group equal ordinates before forming coefficients.
- Test every proposed finite-block checker on the single cosine in
  (R-17201.3); a checker returning `<=2|a|^2` for all short blocks is wrong.
- Test two nearly coincident frequencies, for which the difference-frequency
  sinc term remains large even on a long block.

## Suggested next attack

Use the complete finite Gram form and add pointwise residual budgets, as stated
in `M-17201`.  Only a directed prime-side lower bound above that corrected
finite-block upper can be an RH-disproof certificate.

