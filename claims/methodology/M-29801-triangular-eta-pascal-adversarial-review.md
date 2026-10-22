# M-29801 — Adversarial review protocol for triangular eta–Pascal closure

Claim ID: `M-29801`  
Title: Freeze, type-check, and mutate the stopped-power bulk and eta–Pascal boundary graph before accepting the RH composition  
Status: **FAIL-CLOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `T-29801`, `L-29801`--`L-29805`, `R-29801`

## 1. Freeze the inputs

Record the reviewed commits before beginning:

```text
PR #272  5cb703bcc1593c4ce8f1f2d8d3840dc61d573dba
PR #286  6bba6161887b6913f4f50c1b90ee46a0fd84c339
PR #294  839900f2738c6a3da67f4754b462e953bc1034ba
this branch head at review start
```

Do not import later fixes retroactively.

## 2. Review order

1. `L-29801-positive-stopped-power-resolution.md`;
2. PR #286 `L-28401/L-28402`;
3. `L-29802-positive-boundary-cone-and-eta-pascal-invariance.md`;
4. PR #294 `L-28301/L-28302`;
5. `L-29803-triangular-two-cone-contraction.md`;
6. PR #272 `L-27207/L-27208/T-27203`;
7. `T-29801-triangular-eta-pascal-full-rh-proposal.md`;
8. `R-29801` and the exact checker;
9. the cross-route lemmas `L-29804/L-29805`;
10. report and integration handoff.

## 3. Required source manifest

For each endpoint, exponent channel, first-omitted quotient, parity, and jet order, emit one row containing:

```text
parent analytic coefficient;
shifted Taylor index;
Euler jet/remainder coefficient;
exact sign-normalized Peano source;
eta even and odd destination;
central residual amount;
Pascal sibling-switch amount;
objective cost;
next endpoint;
common-destination key;
collar/bottom designation.
```

The sum of the emitted rows must reproduce the finite operator before any norm is taken.

## 4. Decisive source-typing test

The proposal stands or falls on the following finite property.

```text
Every boundary output is one of:
  positive Peano/endpoint jet at the next half endpoint;
  balanced Pascal sibling switch at that endpoint;
  declared finite collar.

No boundary output is an unrestricted current-endpoint analytic power channel.
```

A reviewer should search first at:

- endpoint coincidences where the first omitted even and odd terms agree;
- jet orders `M-1` and the exact `M`th remainder;
- the shifted `2kq-1` Taylor correction;
- the smallest rows below the analytic threshold;
- repeated destinations receiving opposite parity contributions.

One undeclared current-scale output rejects the triangular recurrence.

## 5. Exact mutations

Every proof-producing checker must reject:

1. replacing the positive endpoint telescope by Mellin differentiation;
2. reversing the `Delta f(x)=f(x)-f(x+h)` convention;
3. deleting a zero-extension endpoint atom;
4. taking total variation of the eta comb before pairing `2k,2k+1`;
5. increasing the sibling switch from `1/(2k+1)` to `1/(2k)`;
6. routing a boundary jet back to the current analytic bank;
7. adding `6/7+theta_*` as one scalar loss;
8. adding `2^-M` as a separate loss after the Euler partition;
9. taking a norm before common-destination recombination;
10. dropping the bottom logarithmic charge;
11. using an unbalanced Pascal edge;
12. omitting a prime-power carry column;
13. losing the dyadic or `2/3` Mertens mutation;
14. substituting the compact step-window adapter for the full inverse-zeta source;
15. promoting finite computation to the all-endpoint theorem.

## 6. Consumer audit

Independently reconstruct:

```text
triangular recurrence
-> DCD on PR #272
-> factor-one-half Cycle Debt recurrence
-> polylogarithmic debt at every endpoint
-> balanced entropy lower bound
-> complete prime-power ramp
-> square-screw upper envelope
-> Landau pole exclusion
-> functional-equation symmetry.
```

Verify all constants and directions.  In particular, the proof needs a lower bound for the prime ramp and the corresponding upper envelope for the screw function.

## 7. Verdict classes

Use:

```text
VERIFIED
VERIFIED WITH FIXES
GAP/BLOCKED
REJECTED
```

A flaw in the source-typing proof is `GAP/BLOCKED` unless an exact emitted jet contradicts the claimed cone.  An exact counterexample satisfying every declared hypothesis is `REJECTED`.

## 8. Status boundary

Passing the algebraic regression is not enough.  Acceptance requires a complete symbolic source manifest and independent reconstruction of the no-feedback property and the RH consumer.
