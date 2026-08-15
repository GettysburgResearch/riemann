# O-92930 — PR #496 and PR #500 supply complementary halves of the controlling hybrid

Status: **NON-LOAD-BEARING ROUTE DISPOSITION**
Frozen heads: PR #496 `96f8a6b3cc3d474217633e16d4caa490a0aae518`; PR #500 `d73c1e7a1a482cac31581211a84db43cc34c824e`

PR #496 contributes the correct two-ledger distinction and the one-generation terminal-child idea. Its source-to-physical root marginal is abstract at the frozen head.

PR #500 contributes an explicit Hall–causal–physical coupling, source marginals, actual same-index placements, tagged cells, one label-blind quantizer and a discard marginal. Its prose does not sufficiently distinguish the native paired source tree from the row-first `P_61` rough lift.

The controlling hybrid is:

```text
native paired source-tree identity;
PR #500 physical coupling for the root current;
actual source-tree children exported before root realization;
PR #496 two-ledger signed correction;
one canonical row for every actual child;
no recursive tree;
direct native deficit <61744.
```

The earlier unqualified `109/1200` PR falsifier is withdrawn. The exact `q=2` rough-lift separator remains a mandatory normalization regression.


There are two valid closing specializations once the native marginal is fixed:

```text
primary one-shot:
    keep the actual children internal to the one label-blind quantizer;
    native deficit <60989.

fallback terminal-child:
    export the same actual children, insert one canonical row each and stop;
    native deficit <61744.
```

The difference is visibility and modularity, not normalization.  Neither
specialization uses the row-first rough lift.
