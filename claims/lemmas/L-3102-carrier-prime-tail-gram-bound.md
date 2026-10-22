# L-3102 — Gram-relative bound for omitted carrier prime powers

Claim ID: L-3102  
Title: Every omitted carrier prime-power block is dominated by its scalar weight times the exact Gram matrix  
Status: PROPOSED  
Authoring agent: `gpt56-05`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0701 and the convolution notation of L-0702  
Scope: complete-tail control for carrier-shifted compact-support Weil searches  
Related counterexample candidates: carrier-Weil finite witnesses

## Statement

Use the real carrier family from D-0701/L-0702,

\[
 f_a(x)=\mathbf 1_{[-\Delta/2,\Delta/2]}(x)\cos(2\pi ax),
\]

with Gram matrix

\[
 G_{a,b}=\int_{\mathbb R}f_a(x)f_b(x)\,dx
\]

and convolution matrix

\[
 C_{a,b}(\xi)=\int_{\mathbb R}f_a(x)f_b(\xi-x)\,dx.
\]

For every real coefficient vector `v` and every real `xi`,

\[
 |v^{\mathsf T}C(\xi)v|\le v^{\mathsf T}Gv.
\]

Equivalently, in quadratic-form order,

\[
 -G\preceq C(\xi)\preceq G.
\]

Let `E` be any finite set of prime powers among those with `q<=c`, and define
its exact omitted prime block by

\[
 P_E=-\frac1\pi\sum_{q\in E}
 \frac{\Lambda(q)}{\sqrt q}
 C\!\left(\frac{\log q}{2\pi}\right).
\]

Set

\[
 W_E=\frac1\pi\sum_{q\in E}\frac{\Lambda(q)}{\sqrt q}.
\]

Then

\[
 -W_EG\preceq P_E\preceq W_EG,
\]

and hence, for every real `v`,

\[
 |v^{\mathsf T}P_Ev|\le W_E\,v^{\mathsf T}Gv.
\]

If `H_partial` contains every nonprime block and a selected partial prime sum,
while `H_full=H_partial+P_E`, then a fixed vector satisfies

\[
 v^{\mathsf T}H_fullv
 \le v^{\mathsf T}H_partialv+W_Ev^{\mathsf T}Gv,
\]

and

\[
 v^{\mathsf T}H_fullv
 \ge v^{\mathsf T}H_partialv-W_Ev^{\mathsf T}Gv.
\]

Therefore a partial negative may be promoted without complete reevaluation only
when a rigorous upper enclosure of the first right-hand side is still negative.
Likewise, a rigorous positive lower enclosure excludes that fixed vector.

If `G` is positive definite, the generalized Rayleigh minima obey

\[
 \lambda_{\min}(H_partial,G)-W_E
 \le \lambda_{\min}(H_full,G)
 \le \lambda_{\min}(H_partial,G)+W_E.
\]

## Motivation

PR #27 found that top-prime truncation can reverse the apparent sign by a large
amount, and Issue #29 asks for deterministic complete-tail control. The bound
above is phase-independent, dimension-independent, and exact once the omitted
prime-power list is fixed. It turns every partial carrier sum into a safe
ranking interval and gives an immediate fixed-vector promotion test.

## Proof

For a real vector `v`, put

\[
 f_v=\sum_a v_af_a.
\]

Each `f_a`, and hence `f_v`, is real and even. Therefore

\[
 v^{\mathsf T}C(\xi)v
 =\int_{\mathbb R}f_v(x)f_v(\xi-x)\,dx
 =\int_{\mathbb R}f_v(x)f_v(x-\xi)\,dx.
\]

Translation preserves the `L^2` norm. Cauchy--Schwarz gives

\[
 |v^{\mathsf T}C(\xi)v|
 \le ||f_v||_2\,||f_v(\cdot-\xi)||_2
 =||f_v||_2^2
 =v^{\mathsf T}Gv.
\]

This is exactly the pair of quadratic-form inequalities
`-G preceq C(xi) preceq G`.

Every coefficient `Lambda(q)/sqrt(q)` in `W_E` is nonnegative. Applying the
single-frequency bound term by term and using the triangle inequality yields

\[
 |v^{\mathsf T}P_Ev|
 \le\frac1\pi\sum_{q\in E}\frac{\Lambda(q)}{\sqrt q}
 |v^{\mathsf T}C(\xi_q)v|
 \le W_Ev^{\mathsf T}Gv.
\]

The fixed-vector inequalities follow by adding `v^T H_partial v`.

When `G` is positive definite, divide by `v^TGv` and take the infimum over all
nonzero `v`. The quotient of the omitted block lies in `[-W_E,W_E]` for every
`v`, so the generalized minimum can move by at most `W_E`. ∎

## Analytic domain audit

The proof uses only real `L^2` functions of compact support and finite sums.
The logarithms in the prime locations are real because `q>0`. No statement is
made here about the Guinand--Weil normalization itself.

## Dependency audit

D-0701/L-0702 supply the real even carrier functions and identify their
convolution matrix with the prime block. Conditional on those definitions, the
bound is elementary and independent of the explicit-formula sign audit.

## Gap audit

- `E` must contain every actually omitted prime power, with multiplicity encoded
  exactly once through `Lambda(p^m)=log p`.
- The scalar sum `W_E` must be outwardly enclosed; a floating underestimate is
  unsafe.
- The bound can be loose because it ignores phase cancellation. It is a safety
  envelope, not a prediction of the true tail.
- The generalized-eigenvalue corollary requires `G` positive definite. The
  fixed-vector inequalities do not.
- This does not bound omitted pole, archimedean, negative-frequency, or Gram
  corrections; those remain separate exact terms.

## Adversarial tests

1. At `xi=0`, `C(0)=G`, so equality is attained and the constant `1` cannot be
   improved uniformly.
2. Use a one-dimensional carrier family and verify the omitted-block bound
   directly for several prime powers.
3. Deliberately omit a higher power `p^m` while retaining `p`; the certificate
   must still include the missing `log p/sqrt(p^m)` weight.
4. Compare a top-prime partial screen that is empirically negative but whose
   `+W_E v^TGv` upper bound is positive; it must not be promoted.

## Remaining uncertainty

No mathematical gap is known. Its practical strength at very large cutoffs
will depend on block design; narrow omitted blocks should be much more useful
than one global tail from a small cutoff.

## Suggested next attack

Implement cumulative exact or directed-ball values of `W_E` for segmented prime
blocks. During Issue #29 searches, retain a candidate only when its fixed-vector
upper bound stays negative after adding every omitted block envelope.
