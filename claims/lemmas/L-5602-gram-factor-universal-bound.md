# L-5602 — Universal (all-vector) positivity certificate for a D-0801 cell

Claim ID: L-5602
Title: A Gram factor certifies `lambda_max(S_K)` and therefore the sign of the
exact D-0801 form for *every* vector at once
Status: PROPOSED
Authoring agent: `opus5-01`
Reviewing agents: none
Created: 2026-07-25
Last updated: 2026-07-25
Dependencies: D-0801; L-0801; L-4202; L-4203; L-5601
Scope: one frozen triple `(T, c, K)`
Related counterexample candidates: none

## Motivation

Every certified D-0801 computation in the repository so far has been a
*fixed-vector* statement: it certifies the sign on one nominated vector and is
silent about the remaining `2K-1` real dimensions.  That is the right object
when a specific negative nomination must be checked, but it is the wrong object
when the question is *"does this parameter cell contain a counterexample at
all?"*.  This lemma upgrades the fixed-vector certificate to a statement about
the whole family, at the cost of one extra `K x K` factorization.

## Statement

Fix `T`, a cutoff `c` and a cell count `K`.  Let `S_K = S_K(T,c)` be the exact
complete prime Toeplitz matrix of L-0801, let `A_K` and `R_K` be the exact
archimedean and pole blocks of L-4201 and L-4203, and let

\[
 Q_K^{\rm exact}=A_K+R_K-S_K,
 \qquad
 \ell_T=\frac{1}{2\pi}\log\frac{T}{2\pi}.
\]

Let `\hat S_K` be any Hermitian matrix with

\[
 \|\hat S_K-S_K\|_2\le\eta,
\]

let `t` be a real number, and suppose a matrix `L \in C^{K\times K}` is exhibited
together with a bound

\[
 \| (tI-\hat S_K)-LL^{*} \|_2\le\varrho .
\]

Then

\[
 \boxed{\;\lambda_{\max}(S_K)\;\le\;t+\varrho+\eta\;}
\]

and consequently, with `B = B_A + \|R_K\|_2` the nonprime correction gate of
L-4202/L-4203,

\[
 \boxed{\;
 \lambda_{\min}\!\left(Q_K^{\rm exact}\right)
 \;\ge\;\ell_T-B-t-\varrho-\eta .}
\]

If the right-hand side is positive then **no** vector `v \in C^K` gives a
negative exact D-0801 explicit-formula value at these parameters: the whole
`K`-cell family is excluded as a counterexample source, not merely the
nominated mode.

## Proof

For any complex matrix `L`, `LL^{*}` is positive semidefinite, so
`\lambda_{\min}(LL^{*}) \ge 0`.  By Weyl's inequality applied to
`M = tI-\hat S_K = LL^{*} + (M-LL^{*})`,

\[
 \lambda_{\min}(M)\ \ge\ \lambda_{\min}(LL^{*})-\|M-LL^{*}\|_2\ \ge\ -\varrho .
\]

Since `\lambda_{\min}(tI-\hat S_K) = t-\lambda_{\max}(\hat S_K)`, this gives
`\lambda_{\max}(\hat S_K) \le t+\varrho`, and one more application of Weyl's
inequality with `\|\hat S_K-S_K\|_2 \le \eta` gives the first display.

For the second, L-4202 states `\|A_K-\ell_T I\|_2 \le B_A`, so for every unit
vector `v`,

\[
 v^{*}Q_K^{\rm exact}v
 = \ell_T + v^{*}(A_K-\ell_TI)v + v^{*}R_Kv - v^{*}S_Kv
 \ \ge\ \ell_T-B_A-\|R_K\|_2-\lambda_{\max}(S_K). \qquad\blacksquare
\]

Note what is *not* used: no property of the algorithm that produced `L` is
required.  A wrong or badly conditioned factor only inflates `\varrho` and
weakens the conclusion; it can never make a false conclusion true.  In
particular the correctness of the LAPACK Cholesky routine is not a dependency.

## Making `\varrho` rigorous in binary64

Let `\tilde M = fl(tI-\hat S_K)` be the matrix actually factored and let
`fl(LL^{*})` be the computed product.  For every summation order, and also when
fused multiply-adds are used, the inner-product rounding bound gives

\[
 \left|fl\!\left(\textstyle\sum_k a_kb_k\right)-\sum_ka_kb_k\right|
 \le\gamma_K\sum_k|a_kb_k|,
 \qquad \gamma_K=\frac{Ku}{1-Ku},\quad u=2^{-53}.
\]

Hence, entrywise, `|LL^{*}-fl(LL^{*})| \le \gamma_K |L||L^{*}|`, and since both
`\tilde M-fl(LL^{*})` and the error matrix are Hermitian, `\|\cdot\|_2 \le
\|\cdot\|_\infty` gives

\[
 \boxed{\;
 \varrho\;\le\;
 \big\|\tilde M-fl(LL^{*})\big\|_\infty
 +\gamma_K\big\||L||L^{*}|\big\|_\infty
 +u\,|t|\;}
\]

the last term covering the rounding incurred when `tI-\hat S_K` is formed (only
the diagonal is affected; the off-diagonal entries are negated exactly).  The
two computed `\infty`-norms are themselves sums of `K` nonnegative binary64
numbers and are inflated by a factor `1+10^{-9}` in the implementation.

Finally the passage from the double-double stream output to the binary64 matrix
`\hat S_K` costs

\[
 \|\hat S_K - S_K^{dd}\|_2\le u\left(|z_0|+\sum_{d\ge1}|z_d|\right),
\]

which is added to `\eta` alongside the L-5601 bound `\sum_d\eta_d`.

## An auxiliary bound that is *not* sufficient, and why

For a Hermitian Toeplitz `S_K` with symbol

\[
 \sigma(\omega)=\operatorname{Re}z_0+\sum_{d=1}^{K-1}\operatorname{Re}
 \left(z_de^{id\omega}\right),
\]

Parseval gives, for every `u \in C^K` with `\hat u(\omega)=\sum_ju_je^{-ij\omega}`,

\[
 u^{*}S_Ku=\frac1{2\pi}\int_{-\pi}^{\pi}\sigma(\omega)|\hat u(\omega)|^2d\omega,
 \qquad
 \|u\|^2=\frac1{2\pi}\int_{-\pi}^{\pi}|\hat u(\omega)|^2d\omega ,
\]

so `\lambda_{\max}(S_K) \le \sup_\omega\sigma(\omega)`, and `\sigma` is a
trigonometric polynomial of degree `K-1` whose supremum can be enclosed by an
FFT on `2^m` points plus the Bernstein closure
`\sup\sigma \le \max_{\rm grid}\sigma + (K-1)^2\|\sigma\|_\infty(2\pi/2^m)^2/8`
(the second-order form is legitimate because `\sigma'` vanishes at an interior
maximum), bootstrapped from the trivial bound `\|\sigma\|_\infty \le
|z_0|+\sum_{d\ge1}|z_d|`.

This route is elementary, cheap and completely self-contained, and it is
implemented as a first gate.  **At the target parameters it is far too weak**:
at `c=10^{11}`, `K=1024` the executed value is

\[
 \sup_\omega\sigma(\omega)\le10.3371 ,
 \qquad\text{while}\qquad \ell_T=4.35172 .
\]

That is not a contradiction and it is worth recording as a structural fact:
the infinite Toeplitz operator `T[\sigma]` has `\lambda_{\max}` more than twice
`\ell_T`, so it is precisely the *finite-section* constraint — the requirement
that the envelope live in exactly `K` cells matched to the support
`\Delta=\log c/2\pi` — that keeps the D-0801 form positive.  Any attempt to
relax the family towards the infinite Toeplitz limit changes `\Delta` and hence
`\ell_T` simultaneously and does not produce a free lunch.

## Analytic domain audit

- Only finite-dimensional Hermitian linear algebra is used; no contour, branch
  or analytic continuation appears.
- Weyl's inequality is applied to Hermitian matrices of equal dimension in the
  same normalized cell basis, as L-4202's gap audit requires.
- `\ell_T`, `B_A` and `\|R_K\|_2` are evaluated by outward-rounded arithmetic at
  60 decimal digits; only the outward endpoints enter the claim.

## Dependency audit

- L-0801 for `S_K` and its Toeplitz orientation (used at the point where the
  first row is assembled from `z_d/2`).
- L-4202 for `\|A_K-\ell_TI\|_2 \le B_A`, used in the final display; its
  hypothesis `b = 2L/K \le 1/20` is checked numerically by the implementation
  and holds at the target (`b = 0.0494696`).
- L-4203 for `\|R_K\|_2`, used in the same display.
- L-5601 for `\eta = \sum_d\eta_d`, used in both displays.
- Everything remains conditional on the D-0801/T-2801 explicit-formula
  normalization, which this lemma does not re-derive.

## Gap audit

1. The conclusion is a statement about one parameter triple `(T,c,K)`.  It is
   not a positivity theorem for the D-0801 family, still less for RH.
2. `\lambda_{\min}(Q_K^{\rm exact}) > 0` excludes a counterexample *in this
   cell*.  A counterexample could still exist at another carrier or cutoff.
3. The Gram residual `\varrho` must be computed, not assumed; a factorization
   that "succeeded" is not by itself evidence.
4. `\|\cdot\|_2 \le \|\cdot\|_\infty` is used for Hermitian matrices only.
5. The symbol bound is an upper bound for `\lambda_{\max}(S_K)`, never a lower
   one; failing that gate proves nothing.
6. If `\ell_T-B-t-\varrho-\eta \le 0` the lemma yields **no** conclusion in
   either direction; in particular it never certifies a negative value.  A
   negative direction requires the fixed-vector route of L-2806/L-5504.

## Adversarial tests

1. Feed a synthetic `S_K` with a known spectrum (e.g. a scalar multiple of the
   identity, or a rank-one perturbation of it) and check that the certified
   upper bound brackets the true `\lambda_{\max}` from above and is not
   absurdly loose.
2. Shift `t` below the true `\lambda_{\max}`; the factorization must fail or the
   residual must blow up, and the checker must report "unresolved", never
   "positive".
3. Perturb one off-diagonal of the assembled matrix by `10^{-3}` and require the
   certified bound to move by no more than the Weyl allowance.
4. Compare the certified `\lambda_{\max}` upper bound against the floating
   `eigh` value; the difference must be positive and of the predicted size
   (`~7\times10^{-11}` at `K=1024`).
5. Run the whole pipeline at a cutoff where the symbol gate *does* succeed
   (small `c`) and require the two routes to agree.

## Remaining uncertainty

The linear algebra is elementary and I am confident in it.  The inputs it
consumes are not: `B_A` and `\|R_K\|_2` inherit L-4202 and L-4203, which are
still `PROPOSED` and have not been independently reconstructed, and the entire
statement inherits the D-0801 normalization.  The lemma is therefore a
conditional exclusion, and the certificate labels it as such.

## Suggested next attack

Replace `B_A` by the exact archimedean Toeplitz matrix of L-4201 evaluated with
directed balls.  At the target parameters `B_A \approx 1.66\times10^{-10}` is
already `1.6\times10^{6}` times smaller than the certified margin, so this is
not urgent for the sign; it becomes urgent as soon as a cell is found where the
margin drops below `10^{-8}`.
