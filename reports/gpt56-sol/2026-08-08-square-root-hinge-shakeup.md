# Shake-up pass: square-root hinges, dual coefficients, and the shortest elementary frontier

Date: 2026-08-08  
Agent: `gpt56-sol`  
Branch: `agent/gpt56-sol/323-halfpower-dual-superposition`  
Status: **NEW EXACT REDUCTIONS + DIRECTED FINITE THEOREM NOMINATION; RH UNPROVED**

## Executive conclusion

The previous quick response proposed a universal weighted-BV contraction for the activated central boundary.  That was too optimistic.  `R-32301` now gives an exact endpoint-nine counterexample.  The source-specific first-boundary variation theorem on PR #316 survives; the generic operator principle does not.

A fresh repo-wide comparison of the live arithmetic, five-adic, Cycle-Debt, Brownian/Nörlund, and carry routes suggests a cleaner first-principles pivot:

```text
DO NOT propagate q^(-1/2) log(X/q) through a boundary cascade.
FIRST resolve it positively into endpoint-vanishing square-root hinges.
THEN solve one static finite carry problem for each hinge.
```

PR #295 already proves the exact positive hinge decomposition.  The new observation is that each hinge has a canonical **upper-triangular average-row realization**, reducing the whole elementary route to one explicit coefficient sign theorem, SHARP.

## 1. The two static reductions

### 1.1 Half-power Prefix Debt

`L-32302` proves exactly

\[
w_X=\sum_{Q=2}^{X-1}\log((Q+1)/Q)\,p_Q,
\qquad
p_Q(q)=q^{-1/2}\mathbf1_{q\le Q}.
\]

Cycle Debt is positively homogeneous and subadditive, so polylogarithmic debt for `p_Q` implies polylogarithmic debt for the full critical target.

This is already preferable to propagating the logarithmic target because the static family has no Jordan logarithm.

### 1.2 Square-root hinges

The stronger existing identity is

\[
w_X=\sum_{T=3}^{X}\lambda_{X,T}h_T,
\qquad
h_T(q)=q^{-1/2}-T^{-1/2},
\qquad
\lambda_{X,T}\ge0.
\]

Unlike `p_Q`, every hinge vanishes at its cutoff.  This removes the endpoint jump which produces immediate higher-stage monotonicity defects in the raw half-power prefix.

The hinge route is therefore preferred.

## 2. SHARP

For

\[
\beta_{nq}
=\frac{\lfloor n/q\rfloor[q-1-(n\bmod q)]}{n+1},
\]

let `c_T` be the unique triangular solution

\[
h_T(q)=\sum_{n=q}^{T}c_T(n)\beta_{nq}.
\]

The theorem to prove is

\[
\boxed{c_T(n)\ge0\quad(2\le n\le T).}
\]

If this holds, put mass `c_T(n)/(n+1)` on every split in row `n`.  That is an explicit nonnegative carry flow for the hinge.  Positive hinge superposition then produces an exact nonnegative flow for the complete critical target.

This completely bypasses:

```text
BTP;
physical-to-carry transference;
Cycle-Debt optimization;
atomic boundary inversion;
Pascal-cycle repair;
five-adic boundary automata;
Brownian total positivity.
```

Those routes remain useful mutations and alternative proof languages, but they are not dependencies of the SHARP proposal.

## 3. Directed finite result

The exact adjoint formula is

\[
c(j)=
\frac{(j+1)[j u_j-(j-2)u_{j+1}]
      +2\sum_{m=j+2}^{T}u_m}
     {j(j-1)},
\]

where

\[
u_m=\sum_{k\le T/m}\mu(k)h_T(mk).
\]

`X-32301` encloses every inverse square root with exact integer intervals at denominator `10^30`, propagates Möbius signs outward, and certifies every nonendpoint coefficient strictly positive at

```text
T=100,
T=1,000,
T=10,000,
T=100,000,
T=1,000,000.
```

The endpoint coefficient is exactly zero.

This is substantially stronger evidence than a binary64 scan, but it is still only a finite theorem nomination.

## 4. Two scope corrections discovered during the pass

### 4.1 Generic BV is false

For `X=9` and `h=delta_9`, the weighted adjacent variation satisfies

\[
V(h)=2\sqrt2+3,
\]

while

\[
V(\mathcal T_9h)=\sqrt2+\sqrt3+2+\sqrt5>V(h).
\]

So the prior speculative ambient variation contraction is withdrawn.

### 4.2 Fixed third Abel is false even for the average-carry inverse

For the quadratic-prefix target

\[
W_T(q)=\binom{T-q+2}{2},
\]

the unique average-carry inverse at

```text
T=1000, n=11
```

is exactly

\[
-156358/55.
\]

Thus the square-root phenomenon is not explained by generic convexity or a fixed finite cumulative order.  The exponent `1/2` and its source-specific arithmetic are load bearing.

## 5. Exact dual normal form

`L-32301` removes another layer of notation from Cycle Debt.  Every normalized finite dual has unique coefficients

\[
b_q=\sum_{d\mid q}\mu(d)[F(q/d)-F(q/d-1)]
\]

such that

\[
F(n)=\sum_{q\le n}b_q\lfloor n/q\rfloor.
\]

Every dual split constraint is

\[
0\le\sum_qb_q\chi_e(q)
\le\sum_qq^{-1/2}\chi_e(q),
\]

and the target objective is simply

\[
-\sum_qb_qt(q).
\]

For a hinge this becomes

\[
-\sum_{q\le T}b_q(q^{-1/2}-T^{-1/2}).
\]

Therefore SHARP has an exact dual equivalent:

> every feasible carry-row coefficient vector has nonnegative pairing with the square-root hinge.

A proof may attack either the primal triangular coefficients or this finite coefficient cone.

## 6. Comparison with the newest five-adic route

PR #322 has an exact and useful factor-five identity.  However its five residue coefficients still contain the full critical multiples-Möbius state, and the source-specific five-state contraction remains open.  It is therefore a coordinate change for the same arithmetic obstruction, not yet a finite automaton proof.

SHARP is more radical: it avoids propagating a residue state entirely.  If true, every finite hinge is solved in one triangular pass.

## 7. Comparison with Brownian/Nörlund

The Brownian/Nörlund branch has a compelling finite one-sided stability target and useful positive cardinal kernels.  A targeted total-positivity literature check did not reveal a theorem which turns the available additive Hirschman-Widder/PF structure into the required Mellin half-plane stability.  The raw producer also has a known right-half-plane mutation, so a generic probability closure would be unsafe.

The route remains genuinely independent, but SHARP is currently the shorter finite theorem.

## 8. What a true completion must now do

A reviewer should not be asked to prove SHARP.  A future authoring pass must supply one symbolic all-endpoint theorem, preferably in one of these forms:

1. prove the adjoint numerator is nonnegative for the square-root hinge;
2. prove the exact hinge pairing is nonnegative for every feasible dual coefficient vector;
3. construct the hinge row weights directly by a positive source-specific representation;
4. prove an equivalent fractional/Stieltjes positivity theorem which survives the exact third-Abel mutation.

Finite directed positivity is not enough.

## 9. Current hierarchy after the shake-up

```text
strongest short elementary target:
  SHARP square-root hinge triangular positivity;

weaker static fallback:
  polylog stopped half-power Cycle Debt;

strongest dynamic carry route:
  PR #316 coupled activated-boundary variation;

strongest exact radix compression:
  PR #322 five-adic residue renewal;

strongest independent non-arithmetic route:
  PR #296 Brownian/Norlund half-plane stability.
```

## 10. Honest conclusion

This pass does not produce an unconditional proof of RH.  It does overturn the previous quick BV direction and replaces it with a much smaller, cleaner, exact finite theorem whose directed signs survive six orders of magnitude in endpoint size.

If SHARP can be proved symbolically, the elementary carry route closes without any of the boundary machinery that has generated the recent chain of refutations.
