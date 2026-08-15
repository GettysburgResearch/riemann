# M-92940 — Proposal for a joint paired-native physical compiler

Methodology ID: `M-92940`  
Status: **PROPOSED / OPEN PRODUCER**  
Created: 2026-08-16  
Inputs: `R-92940`, `L-92940`, PR #500 abstract coupling infrastructure  
RH status: **unproved**

## Goal

Construct the joint map `Phi_X^joint` required by `L-92940` without producing a positive packet for the cancelling child block.

## Proposed architecture

1. Keep each source occurrence in the paired cone with labels

   ```text
   endpoint cell, small-prime parity, least rough owner, orientation,
   causal history, current/child source owner and physical endpoint target.
   ```

2. Form one coupling problem on the **complete** paired source, allowing transport edges between finite-forcing and oriented-child classes. The Hall flow is not solved separately on each child.

3. Preserve source ownership on the input edges. An input owner may be audited even though no output row is assigned to that owner alone.

4. Prove the total output row is coefficientwise nonnegative and that its ordinary response is exactly `w_X(q)` for every physical column.

5. Evaluate ordinary `q` and `4q` on this same total row before forming detail. Reject any construction whose `q=2` marginal is the rough lift or whose child-only marginal is declared nonnegative.

6. Apply one complete-cell restriction, one label-blind positive quantizer, one common thinning, and one signed finite-comparison ledger to the total row.

7. Export no recursive or terminal-child family. A child may be exported only after a separate positive-completion theorem supplies nonnegative ordinary capacities; the present oriented observation does not.

## Required proof objects

A candidate implementation must publish:

```text
an atomwise joint transport/coupling formula;
exact source marginals and one-use owner audit;
coefficientwise nonnegativity of the total row;
ordinary response identities for every q>=2;
q and 4q response equality before detail;
target and declared-score identities on the same coupling;
complete retained-cell support and one quantizer;
mutation tests for orientation loss, rough-lift substitution,
branchwise child positivity, duplicate ownership and signed-source leakage.
```

## Immediate falsifiers

Reject a candidate if any of the following occurs:

```text
one actual oriented child is assigned a separate nonnegative row with
observation-preserving ordinary capacity;
full Omega(Y) is substituted for an actual child response;
the rough lift is used as the native input;
source labels are erased before the joint coupling;
different couplings are used in target, score and component rows;
q and 4q come from different physical rows;
a signed finite comparison is inserted into positive source;
a nonzero Schur port is claimed without an invoked Schur mechanism.
```

## Boundary

This proposal is a corrected research target, not a completed theorem. It preserves the real local advances of PRs #505/#507 while withdrawing their impossible branchwise physical step.

```text
negative-coordinate obstruction            proved
correct physical architecture               proposed
explicit joint coupling                     open
all-column native row                       open
native deficit and endpoint chain           downstream conditional
Riemann Hypothesis                          unproved
```
