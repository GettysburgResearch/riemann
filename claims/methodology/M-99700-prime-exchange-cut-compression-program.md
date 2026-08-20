# M-99700 — Hostile program for the prime-exchange Green--Carleson estimate

## Objective

Prove `PXGC99700` from `T-99700` without replacing the live source by an unsigned rough reservoir or defining a coupling after the desired sign is known.

The exact arithmetic object is now fixed:

```text
vertices       three decorated squarefree fibres;
source masses  |beta(n)| Phi_X^Box(n)/n;
sign           sgn beta(n);
edges          labelled prime-power births and deaths;
capacity       source occurrence used at most once;
observable     factor-67 logarithmic box;
consumer       negative logarithmic mass -> Mellin--Landau -> RH.
```

## 1. Work with the box, not the raw pointwise scalar

The potential `Phi_X^Box` is bounded, continuous at the activation knot, zero at `n=X`, and asymptotically flat in the deep interior. Every electrical estimate must use this potential. Returning to the raw potential `4-3sqrt(n/X)` restores the large activation-boundary energy that the box was designed to remove.

## 2. Cancel the neutral trace first

Use `L-99705` to match the common plus/minus trace at each vertex before any edge flow is created. The remaining source is exactly

\[
\frac{|\beta(n)|}{n}\Phi_X^{\Box}(n).
\]

A proof that spends `g(n)-|beta(n)|` as oriented capacity is invalid.

## 3. Separate downward ownership from cross-source exchange

The owner probabilities of `L-99701` are used only to retain one source occurrence and to control repeated-prime ambiguity. `R-99700` is binding: the squarefree sector has zero owner quadratic variation. Cancellation there must be produced by birth/death edges connecting distinct integers.

## 4. Exact finite dual

At every fixed rational endpoint cell, build the capacitated graph and compute the exact min-cut

\[
\sup_S[m_X^-(S)-m_X^+(N(S))]_+.
\]

The intended analytic theorem is a cut-compression result: every extremal cut should compress, without increasing deficit, to a first-owner product-boundary cut described by

```text
largest active rough prime;
remaining product quotient;
67-adic fibre;
endpoint activation cell.
```

This compression is the first genuinely new theorem. It must be proved, not inferred from scalar positivity or from the existence of some unrestricted transport.

## 5. Proposed cut-compression mechanism

Use four monotone operations:

1. replace a non-owner prime by the first owner while retaining the product;
2. shift source mass toward the activation boundary using monotonicity of `Phi_X^Box`;
3. group equal quotient coordinates before taking any scalar observation;
4. apply submodularity of cut capacity only after source labels are fixed.

The expected output is one quotient-profile cut, not an arbitrary subset of integers.

## 6. Tail and compact parts

After cut compression:

- the compact quotient `1<=X/n<67` is to be checked against the exact factor-67 Hall/profile certificates;
- the moving quotient tail is to be controlled by the prime-reciprocal discrepancy in the Vinogradov--Korobov corridor;
- the critical product-boundary remainder is propagated through the exact child-mass budget below `1/8`.

The three pieces must use the same capacities. A compact Hall packet may not be copied into every child.

## 7. Fail-closed tests

A valid implementation must include:

1. every source atom once;
2. mutation of one `67` coefficient;
3. mutation of one first-owner label;
4. a squarefree negative state with zero divisor-owner energy;
5. a cut whose unrestricted total-mass matching succeeds but graph matching fails;
6. all activation-sided endpoint cells;
7. exact equality of `q` and `4q` observations if a physical-row lift is later added;
8. proof-object hashes generated from the live arithmetic matrix, not random fixtures.

## 8. No-go boundaries

The following do not prove PXGC99700:

```text
local PSD completion;
within-integer Doob energy;
coefficient count below 1/8 before physical typing;
pointwise positivity through a finite endpoint;
source-blind Poincare or large-sieve bounds;
unconstrained max-flow on the complete bipartite graph;
an RH-bearing benchmark bridge.
```

## Scientific status

```text
exact network and capacities        proved
finite max-flow/min-cut dual         proved
cut-compression theorem              open
compressed arithmetic tail          open on the same capacities
PXGC99700                             open / RH-bearing
Riemann Hypothesis                    unproved
```