# X-12102 — Directed positive-anchor PA-1 decision

## Objective

Evaluate the cheapest L-12101 positive-anchor extension of the PR #103 table:

```text
anchor w       1
horizontal x   1
Re(s)          3/2
new primitives 1
final degree   15
```

Unlike the critical-line zero anchor, `w=1` creates two scalar boundaries. A
strict directed failure below the lower boundary gives a polynomial-square
response witness; a strict failure above the upper boundary gives a
`y`-times-square witness.

Ordinary reconnaissance predicts positivity, with approximate distances

```text
lower  4.0503336772e-6
upper  1.4585952792e-5.
```

These are scheduling values only.

## Producer

`build_positive_anchor_source.py` patches the reviewed PR #103 completed-xi C
producer to emit only

```text
x = 1 = 2^0.
```

No special sentinel arithmetic is needed: the inherited source already
represents `x=2^-xbits`, and `xbits=0` gives exact numerator and denominator one.
The patch changes only the x-grid declaration and records source and patched
SHA-256 values.

The production workflow evaluates the same exact point at 512 and 640 Arb bits,
checks functional-equation overlap and coordinatewise rectangle nesting, and
retains both source hashes and timing records.

## Verifier

`verify_pa1.py` reuses the reviewed X-9309 interval, logarithm, source-binding,
and rational linear-algebra primitives. It adds:

1. exact `x=1` point and normalization checks;
2. full seventeen-node response-1 contraction;
3. the reduced L-12101 one-new-point contraction;
4. mandatory interval overlap;
5. recurrence
   
   ```text
   b_(k+1) = a_k - b_k;
   ```
6. exact lower and upper rank-one reference directions;
7. interval square and `y`-times-square witness contractions;
8. exact rational LDL plus interval row-radius positive closure.

The reduced polynomial is reconstructed without SymPy. If

```text
D(y)=product_i(y+u_i),
beta=-1/D(-1),
```

then

```text
P_r(y) = [1-D(y)/D(-1)]/(y+1)
       + D(y)/[D(-1)(y+u_r)].
```

The checker verifies the polynomial divisions and response identity exactly.

## Verdicts

```text
CERTIFIED_NEGATIVE_PA1_H0_SQUARE
CERTIFIED_NEGATIVE_PA1_H1_Y_SQUARE
CERTIFIED_POSITIVE_FULL_DEGREE15_PA1_CONE
UNRESOLVED_PA1_CONE
```

The negative process exit code is one, allowing CI to preserve a strict result
without treating it as a software failure. Malformed inputs exit two.

## Workflow

```text
.github/workflows/x12102-directed-pa1.yml
```

The workflow:

1. installs FLINT;
2. runs exact helper tests;
3. generates and compiles the exact x=1 producer;
4. evaluates 512 and 640 bit rectangles;
5. performs full and reduced contractions;
6. decides both degree-15 moment matrices;
7. records SHA-256 and timing ledgers;
8. commits immutable results on trigger-branch pushes.

## Trust boundary

Exact in the Python verifier:

- rational parsing and arithmetic;
- logarithm series and tails inherited from X-9309;
- total-count shell subtraction;
- full and reduced response coefficients;
- moment recurrence;
- witness quadratics;
- LDL pivots and row-radius comparison;
- source and artifact hashes.

External trusted components:

- FLINT/Arb completed-xi rectangles;
- compiler, runtime, and hardware;
- inherited total-zero-count and canonical-product implications.

A strict negative remains a nomination until a second directed completed-xi
implementation reproduces the primitive and the analytic dependencies are
reviewed.

## Current status

The producer patch, exact verifier, helper tests, and production workflow are
committed. No PA-1 directed result is claimed in this branch before a retained
workflow artifact appears.
