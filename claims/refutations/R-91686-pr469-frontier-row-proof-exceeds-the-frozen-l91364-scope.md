# R-91686 — The universal frontier-row conclusion on PR #469 exceeds the frozen `L-91364` scope

Claim ID: `R-91686`  
Status: **EXACT DEPENDENCY-SCOPE CORRECTION — NO COUNTEREXAMPLE TO THE DESIRED SIGN**  
Created: 2026-08-14  
Reviews: PR #469 at `3cf685181bd367b92cdcfeef9249e0b9b542a09e`  
RH status: **unproved**

## 1. The claim used on PR #469

For a terminal stopped leaf
\[
 p\ge67,\qquad 1\le y<67,
\]
PR #469 defines
\[
 G_{p,y}(j)=D_{P_{61},py}(j)-p^{-1/2}D_{P_{61},y}(j).
\]
For `j>y` the child row vanishes, so
\[
 G_{p,y}(j)=D_{P_{61},py}(j).
\]
`L-91685.7` then cites `L-91364` for strict positivity at every
\[
 2\le j<py.
\]

## 2. Frozen scope of the cited theorem

The frozen theorem `L-91364` at
`e2c97d5902bcc5c94d0b6f2f7de0756b84ce6cad` states and certifies
\[
 D_{P_{61},X}(j)\ge0
 \qquad(2\le j\le66),
\]
with a directed base over those sixty-five rows. It does not state the same theorem for arbitrary `j`.

The replay on PR #469 performs an eighty-digit calculation for the single hostile leaf
\[
(p,y)=(67,13)
\]
and observes positive rows through `j=870`, but it explicitly classifies that calculation as a diagnostic and does not replay a universal all-parameter directed theorem.

Therefore the implication
\[
 j>y\Longrightarrow D_{P_{61},py}(j)>0
\]
for every rough `p`, terminal `y`, and all `j<py` is not established by the cited frozen dependency.

## 3. Correct surviving scope

The following remain intact:

```text
rows 2,...,66 on every terminal leaf          frozen/directed inputs;
inherited rows 2,...,y                        frozen one-prime theorem;
ordinary and radix-four response signs         exact kernel identities;
target, declared-score, and entropy signs      frozen exact/directed inputs;
terminal child D_(P61,y)=c_y                   exact;
frontier rows j>66                             require a new theorem.
```

This is a scope correction, not a negative row witness. A successor may close the frontier by:

1. a directed all-frontier activation-cell theorem;
2. an analytic Green-bulk/boundary estimate uniform in `j`; or
3. avoiding the canonical frontier row in the native producer.

```text
PR469 universal frontier proof as cited       INCOMPLETE
universal frontier sign itself                 OPEN / NO COUNTEREXAMPLE HERE
Riemann Hypothesis                             UNPROVEN
```
