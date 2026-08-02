# Research map and current knowledge

**Status date:** 2026-08-02  
**Global status:** RH remains unsolved.

This page is the current scientific map. It summarizes reviewed mathematics without replacing the exact source commits or review reports.

## One picture

The repository has two broad proof directions and two complementary forms of finite attack:

```text
Arithmetic equivalents                         Explicit-formula / analytic positivity
(Robin, Nicolas, Li, ...)                       (Weil, screw, terminal-prime, xi/Pick)
          |                                                   |
one exact violation disproves RH                one exact RH-necessary negative disproves RH
          |                                                   |
infinite positive proof needs a                 positive proof needs a global or cofinal
complete arithmetic theorem                     positivity / lower-floor theorem
                                                              |
                                                kernel/operator synthesis tries to
                                                organize that cofinal positive proof
```

Finite negative certificates can be decisive. Finite positive certificates are exclusions only.

---

## 1. Robin and Nicolas arithmetic

### Core object

Robin’s inequality is

\[
\frac{\sigma(n)}{n}<e^\gamma\log\log n \qquad (n>5040).
\]

Robin’s classical theorem makes its validity for every \(n>5040\) equivalent to RH. The repository treats that equivalence as an imported, source-qualified theorem; the integrated packet proves finite and structural mathematics around it.

### Reviewed resident results

The packet [`research/integrated/robin/finite-robin-foundations.md`](research/integrated/robin/finite-robin-foundations.md) contains:

- the exact finite maxima of \(\sigma(n)/n\) through \(5582\);
- directed signs locating the adjacent \(403/105\) threshold between \(5582\) and \(5583\);
- the canonical transform that sorts exponents onto the smallest consecutive primes while decreasing \(n\) and increasing abundancy;
- the theorem that every hypothetical Robin counterexample yields a consecutive-prime, nonincreasing-exponent counterexample;
- the exact nested-level encoding and powered shared-budget dynamic-program ceiling for bounded canonical tails.

The finite barrier and canonical reduction were reviewed **VERIFIED** at PR #24’s exact head. The powered envelope was reviewed **VERIFIED** at PR #40’s exact head. The large \(10^{54}\) and \(10^{100}\) production traversals are not imported as first-class results here because their replay and artifact boundaries differ.

### Smallest global burden

One must do at least one of the following:

1. certify a specific Robin violation;
2. prove Robin’s inequality over the entire infinite canonical class;
3. prove a new asymptotic or monotone principle that closes every remaining canonical subtree;
4. replace the route with another arithmetic equivalent whose global tail is more tractable.

A finite range, even an enormous one, is not cofinal.

### Incompatible shortcuts

- The colossally abundant transition spine is useful for discovery but is not automatically a complete search domain.
- “The least counterexample is superabundant” does not mean every counterexample is superabundant.
- Separately maximizing each tail exponent can spend one product budget multiple times; the shared-budget envelope exists precisely to avoid that error.
- A hash of an unavailable terminal stream does not prove gap-free tree coverage.

### Best near-term work

- independently replay one bounded canonical certificate with a distinct arithmetic backend;
- improve exact shared-budget pruning while keeping a tiny checker;
- derive a proved support/exponent tail theorem rather than merely extending the finite endpoint;
- audit primary Robin/Nicolas source statements and exceptional quantifiers.

---

## 2. Weil, screw, and terminal-prime methods

### Core object

Weil-type criteria express RH as nonnegativity of a quadratic form over an admissible test-function class. Screw-function formulations reorganize the same spectral content into conditionally negative or positive kernels. Terminal-prime formulations isolate translated prime-power fluctuations whose Laplace singularities encode off-line zeros.

These routes have two possible successes:

- a strict, exact finite negative witness disproves RH;
- a genuinely global or cofinal positivity theorem proves RH.

### Strong reviewed material in the source record

The review wave accepted substantial finite algebra and several finite computations, including:

- exact carrier and Toeplitz reductions under named explicit-formula conventions;
- exact archimedean and pole corrections;
- a complete finite positive fixed-vector carrier certificate;
- finite screw-range positivity after repairing a missing terminal cell;
- finite criterion and tail algebra for terminal-prime windows;
- countable or finite-element semidecision architectures, subject to precise density and source hypotheses.

The correction packet on `main` includes the terminal-cell coverage theorem and the rule that a local zero census cannot retire a global Weil or screw functional without a locality/complement bound.

### Load-bearing source boundary

The route is unusually sensitive to:

- the exact completed-\(\xi\)/Guinand–Weil normalization;
- Fourier-transform sign and \(2\pi\) conventions;
- admissibility and form-domain hypotheses for each test family;
- complete prime and prime-power coverage;
- exact pole and archimedean terms;
- finite-versus-cutoff-free distinctions;
- authenticated primitive artifacts.

The old D-0001 source/dictionary layer remains a shared integration bottleneck for several branches. Some later branches provide self-contained or alternative derivations, but the repository still needs one canonical source contract with all conventions and domains reconciled.

### Smallest negative-route burden

Produce one finite object with:

1. a reviewed theorem proving that RH implies its nonnegativity;
2. exact admissible test data;
3. complete and authenticated prime/zero/source primitives;
4. outward arithmetic and a strict negative upper endpoint;
5. independent source or backend reproduction appropriate to a potential disproof.

No such Riemann-data witness is currently integrated.

### Smallest positive-route burden

Prove a global/cofinal sign statement. Examples include:

- eventual nonnegativity or subpolynomial negative part for a reviewed square-screw sequence;
- uniform boundedness of a zero-free terminal-prime statistic;
- a cofinal localized-Weil lower envelope whose \(\liminf\) is nonnegative.

A finite positive ladder cannot supply this.

### Incompatible formulations

- A hard-window surrogate is not interchangeable with a smooth CCM/Suzuki target when its boundary tail controls the coefficients.
- A scalar phase-blind localization may discard the terminal-prime Hankel term that cancels the polar exponential.
- A finite source dictionary is not automatically a density theorem for the chosen finite source spaces.
- A truncated prime sum can have the opposite sign from the complete finite prime-power sum.

### Best near-term work

- produce one canonical explicit-formula/provenance packet;
- repair and independently replay the smallest complete terminal-prime cell;
- extract the reviewed square-screw criterion only after its source and growth theorem are adversarially checked;
- formulate the exact cofinal sign target before running another finite ladder.

---

## 3. Completed-\(\xi\), Pick, Loewner, and Stieltjes methods

### Core object

Let

\[
F(s)=\frac{\xi'(s)}{\xi(s)},\qquad
J_T(u)=\sqrt u\,\Re F\!\left(\frac12+\sqrt u+iT\right).
\]

Under RH, the horizontal response has a positive zero-resolvent representation. Consequences include:

- positive-real scalar inequalities;
- nonnegative secants;
- alternating divided differences;
- Stieltjes moment and localizing matrices;
- Pick-matrix positive semidefiniteness;
- total nonnegativity of cross-Loewner matrices;
- barycentric and matched-pole fixed-vector inequalities.

A strict directed violation of any correctly normalized RH-necessary finite predicate would disprove RH.

### Reviewed resident results

[`research/integrated/xi/derivative-free-pick-loewner.md`](research/integrated/xi/derivative-free-pick-loewner.md) contains reviewed finite theorems from PRs #48 and #52:

- the exact two-point secant formula;
- the complete alternating divided-difference hierarchy;
- total nonnegativity of every cross-Loewner minor;
- barycentric product localizers;
- two sign-complete channels;
- exact matched-pole annihilators and mismatch polynomials.

[`research/integrated/xi/finite-pick-controls.md`](research/integrated/xi/finite-pick-controls.md) contains two reviewed finite positive controls from PRs #68 and #71. Each proves an entire complex \(8\times8\) Pick matrix box positive definite at one exact point set. They eliminate those exact finite candidates and nothing else.

### Why the finite criteria are sharp

An off-line zero creates a pole in the right half-plane. Immediately to one side of that pole:

- scalar \(\Re F\) may remain positive;
- the derivative-free secant can become negative;
- a higher Loewner minor can fail even when every sampled entry is positive;
- a modeled barycentric vector can algebraically cancel the positive rank-one part of the reflected pair.

Thus the route is not merely sampling a weak necessary condition. Its finite witness families are existentially complete in principle. The unknown problem is locating and certifying a witness, not proving that some finite witness would exist under false RH.

### Exact remaining burden

For a disproof:

1. choose exact points and a fixed exact predicate before final evaluation;
2. compute proof-grade \(\xi\) or \(F\) balls excluding denominators from zero;
3. preserve all shared correlations in the contraction;
4. authenticate the completion normalization and producer source;
5. obtain a strict negative endpoint;
6. independently reproduce any survivor.

For a proof, finite positivity is insufficient. One would need a theorem covering every point or a complete positivity class.

### Incompatible shortcuts

- A negative midpoint eigenvalue is not a negative matrix interval.
- A fitted rational or Loewner model may nominate points but cannot be the certificate.
- Real same-height value constraints are not the full complex Pick cone.
- Selected critical-line zero deflation cannot reuse one physical zero mass twice.
- A local zero slab cannot retire a global direct-\(\xi\) or Pick functional without a locality theorem.
- Complex-center Taylor coefficients cannot simply be replaced by their real parts and called a generalized Li criterion.

### Proposed connection

> **PROPOSED — complete-Bernstein unification.**  
> The reviewed secant/divided-difference and Stieltjes formulas strongly suggest organizing the horizontal response \(J_T\) as a complete Bernstein function under RH. This would unify the scalar, divided-difference, Loewner, and Stieltjes views and connect them to screw-kernel positivity. The finite formulas are reviewed; the repository-wide equivalence and exact normalization of this unifying statement still require a separate exact-SHA proof and review.

This proposal does not alter the status of any integrated theorem.

### Best near-term work

- build one small two-backend value-only producer for orders one through three;
- certify primitive normalization before expanding the grid;
- select points by condition-aware moat rather than raw midpoint;
- use the existing positive boxes as regression controls;
- independently audit the complete-Bernstein connection.

---

## 4. Kernel and operator synthesis

### Core object

Localized Weil and CCM/Suzuki programs replace an infinite positivity problem by:

1. a finite low packet;
2. an infinite or large positive complement;
3. cross maps;
4. a Schur-corrected low block;
5. a cofinal lower envelope.

A typical target has the form

\[
B_j-Z_j^*C_j^{-1}Z_j\ge -\varepsilon_jG_j,
\qquad \varepsilon_j\to0,
\]

on a hierarchy that captures every dangerous direction.

### What the review wave established

The archive indexes reviewed finite components including:

- block Temple/Schur floor inequalities;
- cardinal and radical finite-section repairs;
- exact right-inverse and selected-zero count gaps;
- canonical deficit augmentation of the complement;
- three-block triangular Schur factorization;
- explicit Möbius local extension;
- two-frame conditional evaluation algebra;
- the classification of the final off-line cardinal kernel defect.

These finite statements are valuable. They do not by themselves prove the required cofinal estimate.

### The decisive conceptual boundary

Once the complement and visible quotient are controlled, the remaining selected-real-zero kernel is not a harmless bookkeeping block. Under false RH, an off-line \(\Xi\)-cardinal difference gives a genuine negative direction invisible at all selected real zeros. Positive-complement Schur elimination subtracts another nonnegative term and cannot rescue that direction.

Therefore the final \(-o(1)\) corrected-kernel floor is essentially the RH-bearing statement itself unless a noncircular synthesis theorem proves it.

### Smallest load-bearing missing steps

A successful positive proof needs all of:

1. a hierarchy proven complete in the relevant form/metric topology;
2. exact source and domain compatibility;
3. a finite positive complement at each level;
4. a complete selected-zero-invisible kernel;
5. a uniform synthesis or corrected-residual estimate on that kernel;
6. a cofinal rate \(\varepsilon_j\to0\);
7. a theorem transferring the cofinal lower envelope to global Weil positivity.

Finite packet existence, fixed-rank diagonal extraction, or finite positive ladders do not substitute for item 5 or 6.

### Why this stack is not yet a resident packet

The reviewed branches use colliding claim IDs, alternate source theorems, stacked repairs, and mixed finite/cofinal statements. A clean extraction must choose one canonical normalization and dependency graph without silently extending any frozen verdict. That is a high-priority Round 2 review target.

### Best near-term work

- produce one readable dependency-minimal operator packet;
- separate exact finite block algebra from every cofinal assumption;
- choose one canonical source/form-domain interface;
- state the complete-kernel synthesis estimate in a falsifiable norm;
- test proposed shortcuts against the off-line cardinal obstruction before computing.

---

## Connections among programs

### Shared finite-witness principle

Robin violations, negative Weil values, negative Pick minors, and negative corrected-kernel directions are all finite separating predicates. The common proof discipline is:

```text
reviewed necessity theorem
+ exact witness
+ complete authenticated primitives
+ strict exact/directed sign
= decisive finite contradiction
```

This is a methodological connection, not a mathematical equivalence among the objects.

### Shared cofinal obstacle

Positive approaches repeatedly reduce to an unbounded one-sided estimate:

- every canonical Robin tail;
- every required support in localized Weil positivity;
- every scale in a screw or terminal-prime criterion;
- every level in a complete corrected-kernel hierarchy.

Large finite verification is useful but cannot cross this quantifier boundary.

### Zero information appears in different coordinates

- Pick/Loewner packets see zero resolvents and poles.
- Screw/terminal-prime packets see translated oscillatory modes.
- Kernel synthesis sees off-line cardinal signature blocks.
- Robin sees the same global question through multiplicative arithmetic rather than explicit zeros.

Connections between these coordinates are valuable proposal engines. They must be labeled **PROPOSED** until exact normalization and quantifiers are proved.

## Current conclusion

The repository contains strong finite proof infrastructure and several sharp RH-equivalent finite witness architectures. It does not contain a strict negative Riemann-data witness or a completed cofinal positive theorem. The highest-value work is now less about adding another isolated finite calculation and more about closing one exact source interface or one explicit unbounded quantifier.
