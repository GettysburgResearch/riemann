# Addendum — positive-anchor line-mass budgets and the directed PA-1 launch

Agent: `gpt56-03-i`  
Date: 2026-07-26  
Parent report: `2026-07-26-93-positive-anchor-ladder.md`  
Status: theorem/checker extension and production trigger; no Riemann-data sign

## Concurrent-work correction

During this session, independent PRs #124, #128, and #134 derived the same
one-positive-anchor recurrence and two-sided scalar gate. This is strong
independent confirmation. Accordingly, the durable distinct contributions of
PR #132 are now stated as:

1. the multi-anchor Christoffel/divided-difference ladder `L-12102`;
2. the exact finite ladder checker X-12101;
3. the directed PA-1 implementation X-12102;
4. the multi-anchor certified line-mass budget `L-12103` / X-12103.

PR #134 also improved the one-anchor candidate ranking. Its exact-node scan
reports

```text
x=1/20, w=1/400
relative lower-wall position ~0.0018744703.
```

This is a stronger scale-invariant one-anchor nomination than the original
`w=1` scout. PRs #124/#128 nominate `w=4`, whose new point lies at
`Re(s)=5/2` and is suitable for an independent right-half-plane backend.

The branch retains `w=1` as PA-1 because its full proof-producing workflow was
already implemented and it is the simplest exact two-sided regression. The
wider issue ledger now prioritizes `x=1/20` and `x=2` next.

## Directed PA-1 implementation

X-12102 patches the reviewed PR #103 completed-xi producer to emit only

```text
x=1, u=1, Re(s)=3/2.
```

The trigger PR #135 evaluates the point at 512 and 640 Arb bits and then:

1. checks functional-equation overlap and precision nesting;
2. computes `b0` by the full seventeen-node response contraction;
3. computes it again by the reduced one-new-point formula;
4. requires directed interval overlap;
5. reconstructs all sixteen degree-15 moments;
6. checks lower-square and upper-`y`-square fixed witness intervals;
7. otherwise attempts exact rational LDL plus complete interval-radius positive
   closure.

No workflow run had been published at the latest check, so no PA-1 sign is
claimed.

## L-12103: positive can still be impossible

PR #133's Christoffel-Padé line-mass budget suggested a stronger objective for
multi-anchor tables. If a frozen rational response is

```text
R0(y)=q(y)^2/[D(y) product_r(y+w_r)]
```

or

```text
R1(y)=y q(y)^2/[D(y) product_r(y+w_r)],
```

then every proof-grade surviving line-zero bin supplies a nonnegative lower
contribution under RH. Consequently,

```text
upper(total response)
< sum_bin multiplicity * lower_bin(R)
```

is a contradiction even when the total is positive.

This may be better suited to PA-3/PA-7 than waiting for a negative eigenvalue:
their empirical matrices are positive but near-null.

## Exact X-12103 checker

The standard-library checker reconstructs:

- squared-distance intervals from exact ordinate bins;
- interval Horner images of the frozen polynomial;
- fail-closed square lower bounds;
- positive denominator upper bounds;
- square and `y`-square leverage;
- multiplicity-weighted leverage totals;
- strict final budget comparison.

It enforces the no-double-counting rule through an explicit source-measure
convention and a required `survives_source_measure=true` gate on every bin.
Overlapping bins and removed zeros are rejected.

The exact synthetic contradiction has

```text
total upper          1/10
certified line mass  1/6
```

and verification digest

```text
19a9978824d8bdfb9f6dc6287439e097fe6c7529ab7e39e5ed37cb607d543f60.
```

A consistent `1/4` total control is retained separately.

## New unclaimed computation issue

Issue #137 requests the first Riemann-data budget. The proposed order is:

1. scale-invariant one-anchor finalist `x=1/20`;
2. independent-backend `x=2` control;
3. PA-3 minimum H0/H1 directions;
4. PA-7 only after the source/bin path is validated;
5. cross-height or slab bins only with explicit source-survival proofs.

## Honest boundary

- No directed PA-1 result has landed.
- No PA-3/PA-7 primitive is directed.
- No real line-mass reversal exists.
- No counterexample or `Z-####` identifier is allocated.
- The synthetic negative and budget contradiction validate checker semantics
  only.
