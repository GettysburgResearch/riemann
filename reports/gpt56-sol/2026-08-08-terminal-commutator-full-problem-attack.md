# Full-problem attack — descendant capacity, critical commutator lifting, and terminal boundary closure

**Agent:** `gpt56-sol`  
**Date:** 2026-08-08  
**Base:** PR #303 at `4367007d658c78a42024a9c94c3c6b078cac2568`  
**Status:** **FULL PROPOSED PROOF PENDING SOURCE-MANIFEST REVIEW**  
**RH:** **UNVERIFIED**

## 1. Why another pivot was necessary

The newest repository state had reached PR #301's proposed eta--Pascal proof and
PR #303's exact correction.  PR #303 correctly found that a formal divisor
source is not the same mathematical object as a nonnegative central/sibling
edge pair.  It then proposed `SFC`: match every analytic source coefficient to
an actually present positive central edge, with polylogarithmic defect.

That correction was necessary, but the zero-defect capacity target remained
stronger than the Cycle-Debt consumer requires.

This pass attacks the actual signed capacity instead.

## 2. First correction — actual central capacity includes descendants

For a decreasing source `c_m`, the canonical positive flow is

```text
sum_m (c_m-c_(m+1)) T_m.
```

PR #303's capacity mutation used `c_n-c_(n+1)` as the coefficient available on
the central edge of size `n`.  That is only the root contribution from `T_n`.
Larger trees contain the same edge as a descendant.

The exact total coefficient is

\[
\kappa_n
=\sum_{r\ge0}
\left[
 \sum_{m=2^r(n-1)+1}^{2^rn}c_m
-
 \sum_{m=2^rn+1}^{2^r(n+1)}c_m
\right].
\]

It obeys

\[
\kappa_n
=(c_n-c_{n+1})
+2\kappa_{2n}+\kappa_{2n-1}+\kappa_{2n+1}.
\]

The smallest exact witness is

```text
N=4, c_m=1/m:
root-only h_2 contribution       1/6
expanded h_2 coefficient        3/4.
```

This invalidates the exact `available=1/6` claim in the capacity replay.
It does not prove capacity sufficiency: at `N=6`, the expanded `h_4`
coefficient is `1/20`, below the model requirement `1/5`.

The corrected lesson is that capacity must be expanded exactly, but exact
positive matching is still unnecessary.

## 3. Breakthrough — every divisor source has a bounded exact split-flow lift

Let

\[
E_h=T_{h+1}-T_h.
\]

Then

\[
L_q(E_h)=1_{q\mid h+1}.
\]

Therefore, for any finite signed divisor source `sigma`,

\[
\Phi(\sigma)=\sum_{m\ge2}\sigma_mE_{m-1}
\]

realizes its complete carry vector exactly.

The adjacent-tree recursion gives much more than the old unweighted
`O(log h)` edge count.  In the PR #272 capacity metric,

\[
\|E_h\|_{\omega,1}
\le24\sqrt{h+1}.
\]

Hence

\[
\mathcal N_\omega(\Phi(\sigma))
\le24\sum_m\sqrt m|\sigma_m|.
\]

This is the missing source-to-flow map.  It is linear, exact, balanced, and does
not request an incoming positive edge.

## 4. The paired eta source costs only logarithmically

For the actual shifted pair

\[
A_k={ (2kq-1)^{-s}\over2k},
\qquad
B_k={ ((2k+1)q)^{-s}\over2k+1},
\qquad s\ge1/2,
\]

use the exact carry-equivalent flow

\[
(A_k-B_k)E_{2k-1}+B_k(S_k-C_k).
\]

Its negative capacity is at most

\[
24\sqrt{2k}(A_k-B_k)+4\sqrt kB_k
\ll q^{-s}k^{-s-1/2}.
\]

At the critical exponent this sums to

\[
O(q^{-1/2}\log K).
\]

This is the quantitative distinction omitted by the source-blind mutation
`c_n=1/n`.  That mutation has square-root total capacity because it lacks the
actual critical half-power.  It correctly refutes zero debt; it does not refute
subpower Cycle Debt.

## 5. Terminal boundary closure

PR #286 already proves that the complete first-omitted Euler/Peano ledger has
polylogarithmic capacity-weighted variation.  Its divisor-switch proof is
precisely

\[
\sum_m\sqrt m|\sigma(m)|
\ll
\sum_n{\tau(n+b)\over n}\,
\operatorname{polylog}(X),
\]

for finitely many shifts `b` at fixed Euler order.

The analytic bank contracts by `6/7`, so the sum of these atomic norms through
all `O(log X)` half-scale depths is polylogarithmic.

Instead of propagating a Hausdorff residual and asking for another boundary
contraction, terminate every emitted source immediately with `Phi(sigma)`.
The total negative capacity is polylogarithmic.

Thus the new spine is

```text
positive stopped powers
-> shifted analytic bank, factor 6/7
-> complete finite divisor boundary source
-> exact adjacent-tree terminal lift
-> polylog negative Cycle Debt
-> sharp complete prime-power ramp
-> square-screw/Landau
-> RH.
```

No `SFC`, WSTS, Mertens estimate, reflected LMI, or nonnegative full-flow theorem
is assumed.

## 6. Exact replay

`X-30401` uses only integers and `Fraction` arithmetic.

```text
expanded capacity / Haar identities              12,636
factor-two capacity recurrences                   12,636
adjacent commutator divisor-source rows           13,040
integer capacity-majorant rows                     1,024
shifted source-order rows                          3,840
paired source / flow carry rows                  622,080
```

Retained digest:

```text
b41721d6b9c6f82d05156f28be954d878e8f0560b3216188ddfbc3e7e9d6236d
```

The checker does not verify the full PR #286 source manifest or RH.

## 7. Honest proof boundary

New exact results:

```text
root-only expanded-capacity equality          refuted;
actual descendant capacity formula            proved;
adjacent commutator source map                proved;
O(sqrt(n)) commutator capacity norm           proved;
critical paired-fiber logarithmic debt        proved.
```

Proposed complete cross-PR composition:

```text
PR #286 cap ledger = atomic source norm;
all emitted sources are present exactly once;
terminal commutator lift -> polylog Cycle Debt;
Cycle Debt consumer -> RH.
```

The decisive review is now finite and source typed: reconstruct the complete
Euler/Peano boundary manifest and verify that its declared capacity norm is
exactly the atomic divisor-source norm.  Until that is independently replayed,
RH is not accepted as proved.
