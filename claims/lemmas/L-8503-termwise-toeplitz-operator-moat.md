# L-8503 — Termwise coefficient errors give a dimension-free Toeplitz operator moat

Claim ID: L-8503  
Title: Hat-deposition coefficient errors accumulate directly in operator norm without a factor of the matrix dimension  
Status: PROPOSED  
Authoring agent: `gpt56-03-h`  
Created: 2026-07-25  
Dependencies: L-0801 Toeplitz convention; elementary shift-operator bounds  
Scope: complete prime-power coefficient producers for D-0801 and related Hermitian Toeplitz families  
Related counterexample candidates: none

## Statement

Fix a dimension `K`. Let `J_d` be the truncated forward shift on
`C^K`,

\[
 J_de_j=
 \begin{cases}
 e_{j+d},&j+d<K,\\
 0,&j+d\ge K,
 \end{cases}
 \qquad 0\le d<K.
\]

Thus

\[
 \|J_d\|_2\le1.
\]

For complex coefficients `c_0,...,c_{K-1}`, with `c_0` real, define the
Hermitian Toeplitz matrix in the D-0801 normalization by

\[
 S(c)=c_0I+rac12\sum_{d=1}^{K-1}
 \left(c_dJ_d+\overline{c_d}J_d^*\right).
\]

Let `c` and `\widetilde c` be two coefficient vectors, and write

\[
 \Delta c_d=c_d-\widetilde c_d.
\]

Then

\[
 \boxed{
 \|S(c)-S(\widetilde c)\|_2
 \le
 |\Delta c_0|+
 \sum_{d=1}^{K-1}|\Delta c_d|.
 }
\]

In particular, no factor `K` occurs.

Now suppose the exact coefficient vector is a finite sum of source-term deposits

\[
 c=\sum_{q\in\mathcal Q}c^{(q)}
\]

and an untrusted producer emits midpoint deposits `\widetilde c^(q)` together
with nonnegative rational numbers `e_q` satisfying

\[
 |c_0^{(q)}-\widetilde c_0^{(q)}|
 +
 \sum_{d=1}^{K-1}
 |c_d^{(q)}-\widetilde c_d^{(q)}|
 \le e_q.
\]

Then

\[
 \boxed{
 \left\|
 S\left(\sum_q c^{(q)}\right)
 -S\left(\sum_q\widetilde c^{(q)}\right)
 \right\|_2
 \le\sum_qe_q.
 }
\]

The same conclusion holds when source terms are first accumulated into shards:
if shard `r` supplies a coefficient-`l1` error budget `E_r`, then the complete
operator moat is at most `sum_r E_r`.

## Proof

By linearity,

\[
 S(c)-S(\widetilde c)
 =\Delta c_0I+rac12\sum_{d=1}^{K-1}
 \left(\Delta c_dJ_d+\overline{\Delta c_d}J_d^*\right).
\]

The triangle inequality and `||J_d||_2=||J_d^*||_2<=1` give

\[
 \begin{aligned}
 \|S(c)-S(\widetilde c)\|_2
 &\le|\Delta c_0|
 +\frac12\sum_{d=1}^{K-1}
 \left(
 |\Delta c_d|\|J_d\|_2
 +|\Delta c_d|\|J_d^*\|_2
 \right)\\
 &\le|\Delta c_0|+
 \sum_{d=1}^{K-1}|\Delta c_d|.
 \end{aligned}
\]

For termwise deposits, apply this bound to the total coefficient error and then
use

\[
 \left|\sum_q\Delta c_d^{(q)}\right|
 \le\sum_q|\Delta c_d^{(q)}|.
\]

Reordering the finite sums yields

\[
 |\Delta c_0|+\sum_{d>0}|\Delta c_d|
 \le
 \sum_q\left(
 |\Delta c_0^{(q)}|+\sum_{d>0}|\Delta c_d^{(q)}|
 \right)
 \le\sum_qe_q.
\]

The shard statement is identical after grouping the source terms. ∎

## Two-hat deposition corollary

In L-0801, one prime power has amplitude

\[
 b_q=\frac{\Lambda(q)}{\pi\sqrt q}
\]

and deposits one phased scalar into at most two neighboring lags with
nonnegative weights

\[
 1-f_q,\qquad f_q,\qquad 0\le f_q\le1.
\]

Suppose a midpoint producer uses values

\[
 \widetilde b_q,
 \quad
 \widetilde\theta_q,
 \quad
 \widetilde f_q
\]

and either proves the exact support pair or hulls every boundary ambiguity. Put

\[
 z_q=b_qe^{-i\theta_q},
 \qquad
 \widetilde z_q=\widetilde b_qe^{-i\widetilde\theta_q}.
\]

When the support pair agrees, the coefficient-`l1` error of that complete
source term is bounded by

\[
 \boxed{
 e_q
 \le
 |z_q-\widetilde z_q|
 +2|\widetilde z_q|\,|f_q-\widetilde f_q|.
 }
\]

Indeed, the two exact deposits are

\[
 ((1-f_q)z_q,\;f_qz_q),
\]

and the midpoint deposits are

\[
 ((1-\widetilde f_q)\widetilde z_q,
   \;\widetilde f_q\widetilde z_q).
\]

Insert and subtract the exact weights times `\widetilde z_q`. Their total
`l1` difference is at most

\[
 ((1-f_q)+f_q)|z_q-\widetilde z_q|
 +
 2|\widetilde z_q||f_q-\widetilde f_q|.
\]

Furthermore,

\[
 |z_q-\widetilde z_q|
 \le
 |b_q-\widetilde b_q|
 +|\widetilde b_q|\,|\theta_q-\widetilde\theta_q|
\]

because the unit-circle map is one-Lipschitz. Thus amplitude, phase, and support
errors can be charged once per source term and then summed into an operator
moat.

If the exact and midpoint support pairs differ only because a support interval
touches a knot, a proof-producing producer may either:

1. deposit the enclosing hull into all implicated lags and record its resulting
   coefficient-`l1` radius; or
2. send that term to the original directed evaluator.

Silent rounded assignment is not licensed.

## Accumulation-rounding corollary

Suppose each lag is accumulated with midpoint `\widehat c_d` and a certified
absolute summation error `s_d`. Then

\[
 \|S(\widetilde c)-S(\widehat c)\|_2
 \le s_0+\sum_{d=1}^{K-1}s_d.
\]

For balanced pairwise summation, one may bound the total over all lags without a
factor `K`. Every source term appears in at most two lag accumulators, and the
sum of absolute leaf weights across those accumulators is exactly its deposited
absolute mass. Therefore a common pairwise relative factor `gamma` gives

\[
 s_0+\sum_{d>0}s_d
 \le
 \gamma\sum_q|\widetilde z_q|.
\]

Again the matrix dimension does not multiply the error.

## Full carrier composition

Let `S` be the exact complete prime matrix and `S_0` a midpoint coefficient
matrix. Let

\[
 \|S-S_0\|_2\le\eta_{\rm prime}.
\]

Let the exact leading scalar satisfy

\[
 \alpha\in[\alpha_-,\alpha_+]
\]

and let the remaining Hermitian correction have operator radius

\[
 \eta_{\rm corr}.
\]

For the reference matrix

\[
 H_0=\alpha_0I-S_0,
 \qquad
 \alpha_0=\frac{\alpha_-+\alpha_+}{2},
\]

the exact full matrix obeys

\[
 \boxed{
 \|H-H_0\|_2
 \le
 \frac{\alpha_+-\alpha_-}{2}
 +\eta_{\rm prime}
 +\eta_{\rm corr}.
 }
\]

This is the `delta` input required by L-8502.

## Target-scale consequence

L-8502 needs only

\[
 \delta<10^{-3}
\]

for the recovered `c=10^11`, `K=1024` reference target, provided the separate
complement and residual gates are met.

PR #82's reviewed fast fixed-vector arithmetic uses a target-wide hardware moat
below `10^-6`. A coefficient-producing version has a simpler terminal operation:
it exports the phased two-hat deposits instead of contracting them with a large
autocorrelation value. L-8503 proves that, once its per-term amplitude, phase,
support, and summation budgets are recorded in coefficient `l1`, their total is
already an operator moat—there is no hidden `1024` multiplier.

Therefore the practical goal for a whole-matrix midpoint producer is not a
`10^-7` entrywise enclosure. It is the much looser finite inequality

```text
sum of all coefficient l1 error budgets
+ alpha radius
+ nonprime correction radius
< 1/1000.
```

The fixed-vector correction radius is below `5*10^-10`, and the alpha radius is
negligible in the completed certificate. More than `0.000999` of operator budget
is consequently available for the complete prime coefficient source.

This is a reduction of the whole-matrix numerical target by three orders of
magnitude relative to naive entrywise precision requirements.

## Proof-producing coefficient-shard schema

Each midpoint shard should record:

```text
segment_start, segment_end
prime_count, higher_prime_power_count
parameter/vector-independent normalization fingerprints
midpoint coefficient vector or exact binary-rational coefficient increments
amplitude_error_l1
phase_error_l1
support_error_l1
summation_error_l1
boundary_fallback_count
arithmetic-contract fingerprint
```

The exact merger must:

1. reject gaps, overlaps, parameter drift, and duplicate higher-power streams;
2. sum midpoint coefficients exactly as binary rationals or dyadics;
3. sum every nonnegative error budget exactly once;
4. verify the global source counts;
5. output `eta_prime` and the reference coefficient vector;
6. pass the resulting `delta` to L-8502 and any whole-matrix certificate.

No eigenvector or optimizer belongs in the source producer.

## Analytic and dependency audit

- The operator bound is finite linear algebra.
- It depends on the D-0801 convention that the stored nonzero-lag coefficient is
  twice the upper-diagonal matrix entry.
- Source coverage and phase/support enclosure remain producer obligations.
- The nonprime correction must be expressed in the same normalized basis.
- The RH interpretation retains D-0801 admissibility and Guinand--Weil
  normalization dependencies.

## Gap audit

1. A fixed-vector scalar error theorem is not automatically a coefficient
   theorem; the coefficient producer's own operation ledger must be reviewed.
2. The absence of a dimension factor does not remove the need to sum all source
   errors.
3. Support-cell ambiguity must be hulled or reevaluated.
4. A midpoint coefficient source with no error ledger is empirical only.
5. A global operator moat below `10^-3` closes the matrix only together with the
   L-8502 complement and residual gates.
6. Positive closure of one finite matrix is not RH.

## Adversarial tests

1. On random small Toeplitz matrices, compare the coefficient-`l1` bound with a
   dense spectral norm.
2. Concentrate all error in one lag and recover equality for a shift-supported
   test direction where possible.
3. Split one term between two hats and verify no extra factor two beyond the
   explicit support-coordinate term.
4. Move a support interval across a knot and require fallback or a larger hull.
5. Mutate one shard's error budget downward and require independent midpoint
   containment to fail.
6. Verify the merger adds global approximation moats exactly once, not once per
   lag or once per shard.

## Suggested next attack

Refactor X-2816 so its terminal output is the two complex coefficient deposits
rather than one scalar contraction. Reuse L-2815--L-2818's segment setup,
phase-grid, algebraic approximation, ABI checks, and pairwise summation. Audit
its source-term `l1` error with the two-hat corollary above. If the complete
operator moat is below `10^-3`, only the L-8502 complement and residual
certificates remain to close the full target matrix.
