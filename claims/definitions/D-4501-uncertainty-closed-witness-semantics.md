# D-4501 — Uncertainty-closed finite-witness semantics

Claim ID: D-4501  
Title: Exact semantics for a finite witness that survives every declared uncertainty  
Status: PROPOSED  
Authoring agent: `gpt56-06-b`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: none  
Scope: route-independent counterexample certificates  
Related counterexample candidates: every future `Z-####` finite witness

## Statement

A **finite-witness problem** consists of the following data.

1. An exact finite witness object

   \[
   w\in\mathcal W_{\rm exact},
   \]

   encoded by integers, rationals, dyadics, exact finite strings, exact finite
   graphs, or another representation with unambiguous mathematical semantics.

2. A finite family of **logical gates**

   \[
   G_1,\ldots,G_r.
   \]

   These include every theorem, normalization, analytic-domain hypothesis,
   admissibility statement, completeness assertion, and implication needed to
   turn the final finite predicate into falsity of RH.

3. A nonempty set \(\mathcal U\) of admitted **quantitative uncertainty
   realizations**.  Its coordinates may represent input rationalization,
   analytic enclosures, rounding, truncation, tails, omitted blocks,
   discretization, parameter drift, solver residuals, or correlated primitive
   evaluations.

4. An exact concrete evaluation map

   \[
   Y:\mathcal W_{\rm exact}\times\mathcal U\longrightarrow\mathcal Y.
   \]

5. A mathematically specified **disproof region**

   \[
   \mathcal D\subseteq\mathcal Y
   \]

   such that the conjunction of the logical gates and
   \(Y(w,u)\in\mathcal D\) implies that RH is false.

A **quantitative survival certificate** for `w` is a finite, independently
checkable set \(C\subseteq\mathcal Y\) satisfying

\[
 \{Y(w,u):u\in\mathcal U\}\subseteq C\subseteq\mathcal D.
\]

A **full witness-survival certificate** is a quantitative survival certificate
together with proof of every logical gate.

When \(\mathcal Y\) is a metric space, the certificate has a **strict moat** if

\[
 \operatorname{dist}(C,\mathcal Y\setminus\mathcal D)>0.
\]

For the common scalar-negative predicate

\[
 \mathcal Y=\mathbb R,
 \qquad
 \mathcal D=(-\infty,0),
\]

a certified upper bound \(U_C<0\) has moat

\[
 \mu=-U_C>0.
\]

## Definitions

### Logical gates

A logical gate is binary.  It is either proved or it is blocking.  Examples are:

- the exact direction of an RH-equivalent criterion;
- the normalization of `zeta`, `xi`, a transform, or an explicit formula;
- analyticity or meromorphic-domain hypotheses;
- exclusion of poles, branch cuts, trivial zeros, or boundary zeros;
- admissibility of a test function;
- completeness of a finite enumeration before a tail bound begins;
- the theorem that converts a strict finite sign into falsity of RH.

A numerical margin does not weaken or replace a logical gate.

### Quantitative uncertainty channels

Every quantitative channel in an uncertainty-closed certificate has one of the
following states.

```text
ELIMINATED_EXACTLY
ENCLOSED
EXHAUSTIVELY_ENUMERATED
TAIL_BOUNDED
```

The project-level ledger may additionally use

```text
INDEPENDENTLY_RECONSTRUCTED
BLOCKING
```

for assurance and workflow.  `INDEPENDENTLY_RECONSTRUCTED` does not replace a
mathematical enclosure; `BLOCKING` prevents promotion.

### Concrete evaluation DAG

A concrete evaluation DAG is a finite directed acyclic graph whose leaves are
exact inputs or quantitative uncertainty channels and whose internal nodes are
exact mathematical operations.  The root is `Y(w,u)` or a finite object from
which membership in the disproof region is decided.

An enclosure DAG assigns each node a set enclosing every possible concrete
value of that node.  Every internal enclosure transformer must have a proved
local inclusion property.

### Uncertainty closure

A certificate is **quantitatively uncertainty closed** when:

1. every leaf of the concrete evaluation DAG is declared exactly once;
2. every declared quantitative channel is used by the root computation;
3. no quantitative channel is `BLOCKING`;
4. every internal transformer is sound on its declared domain;
5. the root enclosure lies wholly inside the disproof region.

This is a closed-world mathematical statement relative to the specified
concrete semantics.  An incorrect semantics, missed theorem hypothesis, or
unsound primitive enclosure is a logical or trusted-base failure, not an
unpriced quantitative perturbation.

### Trusted computing base

The trusted computing base is the collection of components whose correctness
has not itself been reduced to a checked proof object.  It may include:

- the mathematical proof of each logical gate;
- a primitive ball-arithmetic library;
- the certificate parser and exact checker;
- the compiler, runtime, or proof-assistant kernel.

Independent implementations reduce epistemic risk but do not logically prove
one another sound.  Formal verification or a sufficiently small audited kernel
can reduce the trusted base further.

## Motivation

The repository already has route-specific ingredients:

- dyadic-vector perturbation bounds;
- omitted-prime envelopes;
- exact rational final checkers;
- contour-image tubes;
- branch-and-bound coverage certificates;
- directed transcendental signs.

What is missing is a common statement of what it means for these ingredients to
be complete.  D-4501 makes the decisive object the image of the **entire admitted
uncertainty set**, not a midpoint, a preferred implementation, or a list of
individual error bars considered separately.

The definition also prevents a dangerous category error.  Quantitative error
can be defeated by a strict moat.  A wrong theorem, a missing source term, or an
invalid analytic domain cannot.

## Construction template

A route should instantiate D-4501 in this order.

1. Freeze an exact witness `w`.
2. State the exact scalar, matrix contraction, winding invariant, contraction
   test, or arithmetic predicate that decides the witness.
3. List every logical gate.
4. Expose every quantitative primitive as a leaf.
5. Preserve correlation among leaves when it is mathematically known.
6. Build a sound root enclosure or invariant-preserving tube.
7. Compute the moat to the failure boundary.
8. Reject the certificate if any gate or leaf remains blocking.
9. Reconstruct the decisive object with an independent checker.

## Analytic domain audit

D-4501 is an abstract definition.  It introduces no analytic function and no
contour.  Every concrete instantiation must supply its own domain, pole, branch,
and boundary audit as logical gates or sound quantitative leaves.

## Dependency audit

No earlier mathematical claim is used.  The terminology is designed to absorb,
without duplicating, route-specific claims such as `L-3101`, `L-3102`,
`L-3104`, and the gate structure in `M-0901`.

## Gap audit

- “All uncertainty” means all uncertainty represented by the exact concrete
  semantics and its complete leaf ledger.  The definition does not magically
  prove that a human selected the correct semantics.
- An interval produced by an unverified library is not sound merely because it
  is called an interval.
- Independent agreement is evidence against implementation error, not a proof
  that two implementations do not share a defect.
- A large numerical margin cannot discharge an equivalence theorem,
  normalization, or domain hypothesis.
- Declaring independent boxes can destroy known correlations and make a true
  witness uncertifiable; it remains sound but may be unnecessarily weak.
- Omitting an uncertainty channel from the DAG is a logical completeness error,
  not a small zero-width interval.

## Adversarial tests

1. Remove one declared tail channel while leaving the root score unchanged; the
   closure checker must reject the unused/missing leaf mismatch.
2. Insert an undeclared primitive into one internal node; the checker must reject
   the new dependency.
3. Change a proved gate to `BLOCKING`; the certificate must lose full-witness
   status regardless of its numerical moat.
4. Enlarge one quantitative leaf until the root enclosure touches the boundary;
   strict survival must be rejected.
5. Replace a joint correlated uncertainty set by independent boxes and compare
   the loss of margin without changing soundness.
6. Mutate the exact witness bytes while reusing old enclosures; digest and
   dependency checks must fail.

## Remaining uncertainty

The definition cleanly separates mathematical robustness from epistemic trust,
but a future formalization should choose one canonical machine-readable DAG and
one proof-kernel boundary.  Different routes may initially need different
abstract domains: intervals, disks, affine forms, polytopes, Taylor models, or
topological tubes.

## Suggested next attack

Prove the compositional enclosure theorem `L-4501`, add support-function and
dual certificates for correlated uncertainty in `L-4502`, and instantiate the
framework for fixed-vector Pick witnesses in `L-4503`.
