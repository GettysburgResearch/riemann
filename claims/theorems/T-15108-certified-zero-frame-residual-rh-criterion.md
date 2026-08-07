# T-15108 — Cofinal certified-zero frame and complete residual control imply RH

Claim ID: `T-15108`  
Status: **PROVED CONDITIONAL COMPOSITION THEOREM; COFINAL FRAME/RESIDUAL RATIO OPEN**  
Authoring agent: `gpt56-04-f`  
Created: 2026-07-31  
Dependencies: `L-15117`, `L-15119`, `L-15122`, `L-15125`, `T-15104`, and the finite Connes--van Suijlekom real-zero theorem  
Scope: corrected noncircular final theorem for the fixed arithmetic target-pinned route  
Related counterexample candidates: none

## 1. Actual smooth target sequence

Let

\[
 L_j\to\infty,
 \qquad
 N_j\to\infty.
\]

Let `p_j` be the exact CCM coefficient vector of the actual smooth-window
Hermite-radical target, normalized by

\[
 \eta_j^{\mathsf T}p_j=1,
\]

with every used coordinate nonzero.  Let `F_j` be the corresponding compact
finite transform before boundary normalization.

Assume the directed localization and finite Fourier-tail budgets prove

\[
 \boxed{
 F_j\longrightarrow\Xi}
 \tag{T-15108.1}
\]

locally uniformly on `|Im z|<1/2`.

Let `Q_j^W` be the complete actual finite Weil special matrix, represented by
the exact polar, archimedean, and all-prime-power source of `L-15119`.

## 2. Selected certified-zero frame

For every sufficiently large `j`, choose a finite proof-grade multiset `Z_j` of
nonresonant critical-line zeros and construct the positive Cauchy Gram

\[
 Q_j^Z
 =\sum_{\gamma\in Z_j}
  A_{\gamma,L_j}
  \ell_{\gamma,j}\ell_{\gamma,j}^{\mathsf T}
 \tag{T-15108.2}
\]

from `L-15122`.

Let

\[
 z_j=Q_j^Zp_j.
 \tag{T-15108.3}
\]

Subtract the selected source from the complete arithmetic source and put

\[
 Q_j^{\rm rem}=Q_j^W-Q_j^Z.
 \tag{T-15108.4}
\]

For one rational boundary scalar `c_j`, define the complete residual

target-pinned matrix

\[
 R_j
 =\mathcal T_{p_j}(Q_j^{\rm rem},c_j).
 \tag{T-15108.5}
\]

The full arithmetic target-pinned matrix is

\[
 \mathcal T_{p_j}(Q_j^W,c_j)
 =\mathcal T_{p_j}(Q_j^Z,0)+R_j.
 \tag{T-15108.6}
\]

## 3. Directed finite inequalities

Let

\[
 M_j=\operatorname{diag}(m_{j,1},\ldots,m_{j,n_j}),
 \qquad m_{j,i}>0.
\]

Assume directed proof objects establish numbers

\[
 g_j>0,
 \qquad
 \rho_j\ge0,
 \qquad
 \omega_j\ge0
\]

such that:

### A. Positive frame floor

\[
 \boxed{
 x^{\mathsf T}Q_j^Zx
 \ge g_jx^{\mathsf T}M_jx
 \qquad(x\perp p_j).}
 \tag{T-15108.7}
\]

### B. Selected-zero evaluation residual

\[
 \boxed{
 |(z_j)_i|
 \le\rho_j|(p_j)_i|(M_j)_{ii}
 \qquad\text{for every }i.}
 \tag{T-15108.8}
\]

The exact evaluation identity of `L-15125` permits `rho_j` to be produced from
directed values of `F_j(gamma)` at the selected zeta zeros.

### C. Complete arithmetic residual form

\[
 \boxed{
 |x^{\mathsf T}R_jx|
 \le\omega_jx^{\mathsf T}M_jx
 \qquad(x\perp p_j).}
 \tag{T-15108.9}
\]

The residual includes the complete prime-side arithmetic source after the
selected source is removed.  No sign or RH location is assigned to the
unselected part.

Assume

\[
 \boxed{
 \rho_j+\omega_j<g_j.}
 \tag{T-15108.10}
\]

## 4. Finite conclusion

By `L-15125`,

\[
 \boxed{
 \mathcal T_{p_j}(Q_j^W,c_j)\succeq0,
 \qquad
 \ker\mathcal T_{p_j}(Q_j^W,c_j)
 =\mathbb Rp_j.}
 \tag{T-15108.11}
\]

This conclusion is obtained without a target-root calculation and without a
canonical Loewner positivity assumption.

The scalar update preserves the exact special commutator/divided-difference
form and parity.  The finite Connes--van Suijlekom theorem therefore implies
that every zero of `F_j` is real.

## 5. Global conclusion

The real-rooted finite transforms converge locally uniformly to `Xi` in the
open centered critical strip.  Hurwitz's theorem excludes every nonreal zero of
`Xi` there.  Thus every nontrivial zeta zero lies on the critical line and

\[
 \boxed{\mathrm{RH}.}
\]

## 6. Compact cofinal statement

It is sufficient to prove

\[
 \boxed{
 \limsup_{j\to\infty}
 \frac{\rho_j+\omega_j}{g_j}<1.}
 \tag{T-15108.12}
\]

The stronger condition

\[
 \boxed{
 \frac{\rho_j+\omega_j}{g_j}
 \longrightarrow0}
 \tag{T-15108.13}
\]

is more than sufficient.

This is the corrected final full cofinal statement:

```text
actual smooth target
+
positive certified-zero Cauchy frame floor g_j
+
selected target-evaluation residual rho_j
+
complete prime-side target-pinned residual omega_j
+
(rho_j+omega_j)/g_j < 1 cofinally

=> fixed arithmetic scalar completion
=> finite real-rooted transforms
=> RH.
```

## 7. Why this criterion is noncircular

No hypothesis in (T-15108.7)--(T-15108.10) asserts that the target polynomial is
real-rooted.  The positive selected frame uses only already certified
critical-line zeros.  The unknown arithmetic content is retained in `R_j`,
which is produced from the complete explicit formula.

Real-rootedness is a conclusion of the positive arithmetic matrix, not an input.
This distinguishes (T-15108.12) from:

- canonical-Loewner positivity;
- complete Rouché exhaustion of all target roots;
- arbitrary special completion;

all of which are already sufficient for RH when combined with target
convergence.

## 8. Proof-producing interface

A finite certificate must contain:

1. directed actual smooth target coefficients and boundary normalization;
2. proof-grade selected zero balls and multiplicities;
3. the complete selected Cauchy Gram and source;
4. a rational complement basis and directed lower frame LMI;
5. directed finite-transform evaluations at the selected zeros;
6. the complete polar/archimedean/all-prime-power source;
7. the residual target-pinned matrix for one rational `c_j`;
8. directed LMIs for `omega_j M_j+/-R_j` on `p_j^perp`;
9. the strict rational comparison `rho_j+omega_j<g_j`.

No target root finder is needed.

## 9. Proof boundary

The theorem does not establish:

- a cofinal selected-zero frame with controlled `g_j`;
- coordinate-relative decay of the selected evaluation residual `rho_j`;
- a complete residual-form bound `omega_j=o(g_j)`;
- a passing Riemann sequence.

Those are now the exact three zeta-specific asymptotic estimates.  No proof of
RH is claimed.