# Extra-high live global redo and full-problem frontier

Date: 2026-08-08  
Agent: `gpt56-sol`

## Purpose

This pass deliberately redoes the two preceding research passes from the live repository rather than inheriting their narrative. Several claims which looked close to closure have moved materially since those passes.

The pass does **not** claim RH is proved.

## 1. Corrections to the previous two passes

### 1.1 Rank-one parity contraction is false

The tentative `2x2` parity shortcut is exactly refuted on PR #263:

\[
\det(vv^*-T^*vv^*T)
=-|v_+v_-|^2|a-b|^2.
\]

Unequal channel multipliers force an indefinite direction. The ratio-three transition is also `3^{-s}`, not a power of the dyadic variable `2^{-s}`.

### 1.2 Raw annular `H^1` tail transfer is invalid

The raw opposite-parity annular signal is piecewise exponential with jump atoms and is not automatically in the absolutely-continuous Sobolev domain used by the digital-tail theorem. PR #263 now records that domain mismatch explicitly.

### 1.3 Restricted Mersenne saturation is not a live completion

PR #314 gives a complete analytic Farkas obstruction to eventual restricted Mersenne saturation. The earlier Mersenne-collar proposal is therefore not a viable unconditional route.

### 1.4 Terminal boundary atomization is false

PRs #311/#313 and the later synthesis prove that the ordinary divisor-source atomic norm of the stopped critical boundary is linear in the endpoint. Any proof which source-inverts that boundary before recombination manufactures a macroscopic obstruction.

The same boundary has only logarithmic native paired/central-flow variation on PR #316. The order of operations is load bearing.

## 2. Current durable arithmetic spine

The most robust finite coordinate is Cycle Debt on PR #272. For the exact target divergence `r_X`,

\[
\mathfrak N_\eta(X)
=
\min_z\sum_e\omega_e[-d_X^{\rm tree}-C_\eta z]_+
\]

and finite LP duality gives

\[
\mathfrak N_\eta(X)
=
\max_F\left[-\sum_m r_X(m)F(m)\right],
\]

subject to

\[
0\le F(n)-F(j)-F(n-j)\le\omega_{n,j}.
\]

A subpower bound for this exact optimized debt gives the sharp prime ramp and RH. No generic rank, face-count, or absolute-source theorem is needed.

## 3. Current constructive producer

PR #317 supplies the cleanest exact finite producer after the cutoff corrections.

For a finite sequence `r`, split the actual shifted residual as

```text
actual central residual
 = unshifted eta residual
   + one-step lattice shift.
```

The lattice shift is terminated exactly by adjacent-tree commutators. The only propagated state is

\[
r_{j+1}(q)
=
\sum_{k\ge1}
[r_j(2kq)-r_j((2k+1)q)].
\]

Its negative capacity is controlled by the explicit critical variation

\[
\mathcal V_N(r)
=
\operatorname{TV}(\sqrt n\,r(n))
+2\sum_n\frac{|\sqrt n\,r(n)|}{n}.
\]

Thus the remaining arithmetic statement can be frozen as the explicit finite theorem

\[
\sum_j\mathcal V_{N_j}(r_j)=X^{o(1)}.
\]

This is `CEV`; it remains open and RH-bearing.

## 4. Strongest boundary result

PR #316 proves that the complete first activated boundary has

\[
\sum_n\sqrt n\,|b_X(n)-b_X(n+1)|=O(\log X)
\]

and supplies the actual signed central-flow certificate with `O(log X)` negative capacity debt.

It further proves, for every analytic depth `a` and every power exponent `s>=1/2`, that the fully telescoped fresh boundary profile

\[
h_{a,X,s}(x)
=x^{-s}\log\min\{2^a(x-1)+1,X\}
\]

has polylogarithmic native first-difference debt uniformly in the depth.

The only open part of that architecture is propagation/recombination of an already-injected boundary under later finite stages.

## 5. New theorem on this branch

`L-32301` strengthens the analytic-bulk theorem of PR #286.

Define

\[
\left\|\sum_{h\ge0}a_hx^{-\sigma-h}\right\|_{\sigma,\star}
=
\sum_{h\ge0}|a_h|(1+h)^4 64^{-h}.
\]

Then the exact shifted central operator obeys

\[
\boxed{
\|\mathscr C f\|_{\sigma,\star}
\le\frac67\|f\|_{\sigma,\star},
\qquad \sigma\ge1/2.
}
\]

The proof is one line after PR #286: moving an exponent upward by `ell` changes the quartic weight by at most

\[
(1+\ell)^4 64^{-\ell}\le4^{-\ell},
\]

so the weighted row is dominated by the already-certified radius-`1/4` row.

For the all-depth endpoint profile, below its cap

\[
h_{a,X,s}(x)
=x^{-s}
\left[
\log2^a+\log x
-
\sum_{\ell\ge1}
\frac{(1-2^{-a})^\ell}{\ell}x^{-\ell}
\right],
\]

and the complete faster-power tail has weighted norm below `log(4/3)<1/3`, uniformly in depth. Above the cap the profile is simply `log X x^{-s}`. The two branches are continuous and have exactly one derivative jump.

Therefore the all-generation obstruction cannot lie in:

```text
analytic power tails;
faster-power proliferation;
polynomial exponent losses;
depth-dependent affine-log coefficients.
```

All of that is strictly contracted. The only surviving state is the propagated cap-interface boundary measure.

## 6. Current leading routes after the redo

### A. Cap-interface / Cycle-Debt renewal

```text
strict 6/7 analytic bulk
-> one cap-interface source per analytic channel
-> native paired central-flow certificate
-> propagate cap source without atomization
-> subpower Cycle Debt
-> sharp prime ramp
-> RH.
```

This is the strongest route because every fresh injection is already polylogarithmic and the analytic interior is now uniformly contractive in a norm strong enough for the all-depth bookkeeping.

### B. Prime-annulus commutator

PR #289 gives an exact fixed top-quarter statistic whose transform retains every zeta zero. Its local energy `PAE` is equivalent to RH. It is an excellent scalar firewall and possible consumer of a successful cap-renewal estimate, but no independent PAE bound is presently proved.

### C. Five-adic renewal

PR #322 gives an exact five-block scaling identity and proposes a finite residue automaton. The local automaton has not been emitted, so the claimed `1/5` Cycle-Debt recurrence remains a research target rather than a proof.

### D. WSTS / elementary carry

PR #276 identifies WSTS as exactly RH-equivalent. It is a canonical scalar endpoint, not an easier final lemma.

## 7. Routes no longer treated as near-complete

```text
restricted Mersenne saturation          refuted
terminal atomic boundary closure        refuted
fixed-order Abel positivity             refuted
rank-one parity contraction             refuted
conditional-Hankel carry closure        refuted
monotone positive Divisibility Cover    refuted
pure prime-tail subpower queue          refuted/proposed refuted
```

Stronger source-specific descendants may remain open, but none of these mechanisms should be recycled as a completed proof.

## 8. Exact full-problem frontier

The most precise live statement is now:

> Preserve the complete cap-interface source in its paired/central coordinate under every support-halving propagation step and prove that the sum of its optimized negative capacity debts is `X^{o(1)}`.

A proof may use:

- the `6/7` quartic-weighted analytic reserve;
- PR #316's all-depth fresh-boundary variation theorem;
- PR #317's exact shift terminalization and eta-core producer;
- PR #272's exact Pascal-cycle quotient and debt duality.

It may not:

- source-invert the boundary before recombination;
- take rowwise absolute values on the eta/Mobius source;
- delegate a transition identity to reviewers;
- promote a finite ladder to the cofinal statement.

## 9. Status

```text
live graph re-audited                         YES
previous parity shortcut                      REFUTED
previous raw-H1 shortcut                      WITHDRAWN
Mersenne restricted saturation                REFUTED
terminal atomic closure                       REFUTED
quartic-weighted analytic interior            PROPOSED COMPLETE
fresh all-depth boundary injections           PROPOSED COMPLETE / imported
propagated cap-interface renewal              OPEN / RH-BEARING
unconditional proof of RH                     NO
```
