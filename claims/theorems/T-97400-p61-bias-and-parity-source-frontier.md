# T-97400 — Exact disposition of the parity-contractive factor-67 proposals after the repaired `P_61` bias theorem

Claim ID: `T-97400`  
Status: **UNCONDITIONAL HARDENING THEOREM; FULL RH PRODUCER OPEN**  
Created: 2026-08-18  
RH status: **unproved**

The following chain is now exact:

```text
complete P61 scalar bias 1/42 <= F/M <= 1/8      PROVED DIRECTED/ANALYTIC
old PR #565 constant 1/40                         FALSE at x=184
one-prime high-scale scalar difference            PROVED STRICTLY POSITIVE
<1/8 contraction arithmetic with lower 1/42       PROVED EXACT
PR #565 swapped-current positive-source claim      FALSE AS AN INTERFACE
PR #565 root marginal identification               UNPROVEN / MISMATCH
PR #566 reserve injection                          RETAINED CONDITIONALLY
PR #566 reserve -> Hall-current domination         NOT DERIVED / COUNTERMODEL
PR #566 finite M-matrix lemma                       PROVED EXACT ABSTRACTLY
CPSL67 / GPHT* / GABPT / TFPE / ACBI               OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVEN
```

In particular, neither PR #565 nor PR #566 is presently a complete proof
proposal after exact statement-to-use reconstruction.

A valid successor may use `L-97400` and `L-97401`, but it must commit one
source object satisfying all of the following simultaneously:

1. its root signed marginal is the actual annular Möbius scalar;
2. every rough child has its exact coefficient `p^{-1/2}` and cumulative parity;
3. every positive current is a true submeasure of that root source;
4. current and recursive children are source-disjoint and spent once;
5. its total recursive unsigned mass is `<M/sqrt(67)`;
6. its current scalar has the repaired lower bias `>= (M-H)/42`;
7. every child scalar has the hereditary upper bound `<=m/6`.

With those seven clauses, `L-97401` yields strict positivity and the exact
annular Mellin--Landau consumer of PR #547 yields RH.  At the reviewed heads,
clauses 1--4 are the first missing arrow; they may not be replaced by a scalar
identity that cancels the rough child or by a reserve used once in `g` and a
second time recursively.
