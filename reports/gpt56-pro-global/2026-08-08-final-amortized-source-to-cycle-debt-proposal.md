# Final proposal: amortized Hausdorff source-to-Cycle-Debt closure

Agent: `gpt56-pro-global`  
Date: 2026-08-08  
Issue: #298  
Status: **FULL PROPOSED PROOF PENDING ADVERSARIAL REVIEW; RH UNVERIFIED**

## Executive result

The live repository contains two complementary exact advances:

```text
PR #286
  analytic/interior shifted cascade contracts by 6/7;
  every finite-cutoff failure is an explicit lower-scale Euler/Peano ledger.

PR #294
  every adjacent parity source dipole has an exact balanced Pascal realization;
  the sibling switch is locally capacity feasible.
```

The missing step was to prove that the actual cutoff coefficients enter those Pascal switches with the correct sign and capacity, and that the resulting flow controls the same negative-capacity debt used by the RH consumer.

The present proposal supplies that bridge.

## 1. Positive finite resolution of the critical target

For every finite endpoint,

\[
q^{-1/2}\log(X/q)
=\sum_{Y=q}^{X-1}\log((Y+1)/Y)q^{-1/2}.
\]

Thus the critical logarithmic target is a positive layer cake of stopped pure powers.  The finite producer never needs a signed Mellin-exponent derivative.

## 2. Hausdorff structure of every cutoff channel

For a pure power sampled on an arithmetic progression,

\[
v_j=(x+jh)^{-s},
\]

there is a positive Hausdorff representation

\[
v_j=\int_0^1y^j\,d\nu(y).
\]

Hence

\[
\Delta^mv_j=\int_0^1y^j(1-y)^m\,d\nu(y)
\]

and the exact Euler remainder

\[
R_K^{(m)}
=\int_0^1{y^K(1-y)^m\over1+y}\,d\nu(y)
\]

are positive and decreasing in the quotient index.

The shifted-even argument in PR #286 is `2kq-1`, while the paired odd argument is `(2k+1)q`; the former is smaller.  Taylor expansion about `2kq` adds only positive even-channel faster powers.  Therefore, after common-destination recombination, the actual paired source coefficients satisfy

\[
A_k\ge B_k\ge0.
\]

The first odd omitted index is either the same as the shifted-even first index or exactly one earlier.  That one unmatched odd term is retained in the explicit collar.

## 3. Exact nonnegative Pascal flow

At parent `4k`, use the central and sibling edges

```text
c_k=[4k,2k],
s_k=[4k,2k-1].
```

Their carry difference is

\[
\chi_{s_k}-\chi_{c_k}
=e_{2k}-e_{2k+1}.
\]

For the actual source pair,

\[
A_ke_{2k}-B_ke_{2k+1}
=(A_k-B_k)e_{2k}+B_k(e_{2k}-e_{2k+1}).
\]

Therefore assign

\[
(A_k-B_k)c_k+B_ks_k.
\]

Both coefficients are nonnegative.  The entire common paired tail contributes **zero negative capacity debt**.

The exact entropy/von-Mangoldt objective loss is

\[
B_k\log((2k+1)/(2k)).
\]

Since the logarithm is less than one,

\[
(A_k-B_k)+B_k\log((2k+1)/(2k))\le A_k.
\]

Thus incoming source pays both residual lower-scale source and the complete objective loss.

## 4. Collar and global budget

All unmatched first terms, endpoint coincidences, zero extensions, and finite analytic threshold rows are retained in PR #286's collar.  Its first-generation capacity is polylogarithmic.

Let `J_a` be residual boundary source, `C_a` paid Pascal cost, and `I_a` new analytic/collar injection. Then

\[
J_{a+1}+C_a\le J_a+I_a.
\]

The analytic state contracts by `6/7`, and there are only `O(log X)` half-scale levels. Hence

\[
J_A+\sum_{a<A}C_a=O(\log^B X).
\]

In the negative-capacity metric:

```text
common paired tail debt =0;
unmatched collar debt   =polylog(X).
```

## 5. Cycle Debt

PR #272's exact doubled-endpoint normal form contains:

```text
factor-1/2 lifted lower flow;
bottom logarithmic tree;
every odd node as an adjacent Pascal commutator.
```

The common odd tail is exactly the nonnegative flow above.  The bottom tree and unmatched terms are the collar.  Therefore the Dyadic Commutator Debt excess is polylogarithmic:

\[
\mathfrak E_\eta(Y;d_Y)=O(\log^B Y).
\]

The exact recurrence gives

\[
N_\eta(2Y)
\le\frac12N_\eta(Y)+O(\log^B Y),
\]

and unit-endpoint interpolation gives polylogarithmic Cycle Debt for every endpoint.

## 6. Prime ramp and RH

The balanced Kummer/entropy consumer yields

\[
\sum_{p^r\le X}{\Lambda(p^r)\over\sqrt{p^r}}
\log(X/p^r)
\ge4\sqrt X-O(\log^{B'}X).
\]

At square endpoints, the reviewed square-screw identity gives the required subpolynomial upper envelope.  The one-sided Laplace/Landau argument excludes every zero to the right of the critical line; the functional equation excludes the reflected half.

The full proposed chain is

```text
positive stopped powers
-> 6/7 analytic contraction
-> ordered Hausdorff cutoff tails
-> nonnegative central/sibling Pascal flow
-> zero paired-tail capacity debt + polylog collar
-> polylog Cycle Debt
-> sharp complete prime-power ramp
-> RH.
```

## 7. Exact review hinge

Reviewers must emit the full source manifest and verify:

1. every common shifted-even coefficient is at least its odd partner;
2. first-omitted index mismatch is at most one and is present in the collar;
3. Taylor and Euler transformations preserve the declared common destination;
4. the source dipole is exactly the carry image of the central/sibling edge pair;
5. all paired edge coefficients are nonnegative;
6. the collar capacity includes every unmatched term;
7. the emitted odd channel is exactly PR #272's commutator channel;
8. the bottom tree and unit-endpoint interpolation are retained.

One finite counterexample rejects the proposal.

## 8. Exact finite regressions

```text
X-29801
  formal stopped-log rows          8,255
  positive finite differences      8,960

X-29802
  ordered shifted jet pairs       24,576

X-29803
  first-omitted index rows        16,511
  unmatched odd collar rows       10,712
  paired jet rows                792,528
  central/sibling carry rows      33,024
```

The checkers authenticate finite algebra only.

## 9. Status boundary

```text
positive target resolution                     proposed exact
shifted analytic 6/7 contraction               inherited/proposed complete
Hausdorff jet and remainder ordering            proposed complete
nonnegative Pascal source flow                 proposed complete
zero paired-tail capacity debt                 proposed complete
polylog unmatched collar                       inherited/proposed complete
DCD/Cycle Debt -> prime ramp -> RH              inherited conditional chain
RH                                              full proposed proof / unverified
```

No merge or public README change is requested before adversarial review.
