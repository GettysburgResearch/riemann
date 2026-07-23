# L-5501 — Exact endpoint susceptibility ranking for piecewise-carrier thresholds

Claim ID: L-5501  
Title: The first-cell effect of a new prime power is ranked exactly by a phase-adjusted endpoint product  
Status: PROPOSED  
Authoring agent: `gpt56-05-f`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; L-0801; L-4204  
Scope: fixed-carrier logarithmic-cutoff events in the piecewise autocorrelation family  
Related counterexample candidates: none

## Statement

Fix a carrier `T`, a cell count `K>=2`, and a unit vector

\[
 v=(v_0,\ldots,v_{K-1})\in\mathbb C^K.
\]

Let `q=p^a` be a prime power, put `L_0=log q`, and write

\[
 \theta_q=T\log q,
 \qquad
 E_{0,K-1}(\theta_q)
 =e^{-i\theta_q}e_0e_{K-1}^*
  +e^{i\theta_q}e_{K-1}e_0^*.
\]

For the normalized complete-prime Toeplitz operator `S_K(L)` of L-0801, the
right-minus-left derivative jump at `L=L_0` is

\[
 S_K'(L_0+)-S_K'(L_0-)
 =\frac{K}{2\pi a\sqrt q}E_{0,K-1}(\theta_q).
\]

Consequently the derivative jump of the frozen-vector leading margin

\[
 M_v(L)=\alpha_T\|v\|^2-v^*S_K(L)v,
 \qquad
 \alpha_T=\frac{\log(T/(2\pi))}{2\pi},
\]

is

\[
 M_v'(L_0+)-M_v'(L_0-)
 =-\chi_q(v),
\]

where the **signed endpoint susceptibility** is

\[
 \boxed{
 \chi_q(v)=
 \frac{K}{\pi a\sqrt q}
 \operatorname{Re}
 \left(e^{-iT\log q}\overline{v_0}v_{K-1}\right).
 }
\]

Thus among a finite threshold set, sorting by decreasing `chi_q(v)` is exactly
sorting by the instantaneous downward derivative impulse on the frozen-vector
leading margin. A negative susceptibility is initially favorable to positivity,
not to a counterexample search.

The operator-norm susceptibility, independent of `v`, is

\[
 \boxed{
 \frac{K}{2\pi a\sqrt q}.
 }
\]

Throughout the first deposition cell

\[
 L_0<L<\frac{K}{K-1}L_0,
\]

the exact event contribution is

\[
 v^*S_q(L)v
 =\frac{K\log p}{\pi\sqrt q}
   \frac{L-L_0}{L}
   \operatorname{Re}
   \left(e^{-iT\log q}\overline{v_0}v_{K-1}\right).
\]

Its limiting full-cell drop in the leading margin is therefore

\[
 \boxed{
 D_q(v)=
 \frac{\log p}{\pi\sqrt q}
 \operatorname{Re}
 \left(e^{-iT\log q}\overline{v_0}v_{K-1}\right).
 }
\]

## Proof

L-4204 gives the exact first-cell matrix

\[
 S_q(L)=\frac{K\log p}{2\pi\sqrt q}
 \frac{L-L_0}{L}
 E_{0,K-1}(\theta_q).
\]

Differentiating `(L-L_0)/L` at `L_0+` gives `1/L_0`. Since
`L_0=a log p`, the coefficient becomes `K/(2 pi a sqrt(q))`. The term is absent
on the left, which proves the matrix derivative jump.

The quadratic form of the Hermitian corner matrix is

\[
 v^*E_{0,K-1}(\theta_q)v
 =2\operatorname{Re}
  \left(e^{-i\theta_q}\overline{v_0}v_{K-1}\right).
\]

The leading margin contains `-v^*S_Kv`, so its derivative jump is the negative
of the displayed susceptibility. The nonzero eigenvalues of the corner matrix
are `+1` and `-1`, proving the operator norm. Finally, as
`L` tends to `K L_0/(K-1)` from below,

\[
 K\frac{L-L_0}{L}\longrightarrow1,
\]

which gives the full-cell formula. ∎

## Motivation

A threshold scan that ranks only by `1/sqrt(q)` ignores the carrier phase and
the leading mode. L-5501 provides the exact, inexpensive ranking statistic. It
also distinguishes three quantities that must not be conflated:

1. instantaneous frozen-vector susceptibility `chi_q(v)`;
2. worst-case operator susceptibility `K/(2 pi a sqrt(q))`;
3. integrated full-first-cell drop `D_q(v)`.

## Analytic domain audit

All logarithms are real logarithms of positive integers. The phase is used only
through a unit complex exponential. The threshold matrix is finite and
Hermitian. No zeta-function evaluation or analytic continuation occurs in this
lemma.

## Dependency audit

D-0801 fixes the carrier family. L-0801 fixes the normalized prime Toeplitz
coefficient. L-4204 proves the corner-entry formula. This lemma extracts and
organizes its ranking consequences without promoting the Guinand--Weil
normalization.

## Gap audit

- A large positive `chi_q(v)` does not imply an eigenvalue crossing; the old
  prime background and eigenvector rotation continue to move.
- The vector used for ranking may cease to be the leading vector.
- Floating phases or floating endpoint coordinates make the ranking empirical.
- A threshold may rank highly instantaneously but have a tiny cell before the
  next prime power.
- The full-cell formula concerns only that one event; later thresholds entering
  before the full deposition knot must be included separately.

## Adversarial tests

1. Set `v_0=0` or `v_{K-1}=0`; the frozen-vector susceptibility must vanish.
2. Rotate `v` by a global phase; the score must remain unchanged.
3. Replace `T` by `T+pi/log(q)`; the signed score reverses.
4. Compare the derivative formula with exact finite differences of the isolated
   corner event.
5. Verify that the matrix derivative eigenvalues are equal and opposite.

## Remaining uncertainty

No algebraic gap is known. Its discovery effectiveness depends on the endpoint
mass of actual leading modes and on rigorous control of the background.

## Suggested next attack

Use exact dyadic endpoint coordinates and directed phase balls to rank large
threshold shards. Retain only events whose maximum integrated drop plus a
background/eigenvector-rotation bound can approach the current margin.
