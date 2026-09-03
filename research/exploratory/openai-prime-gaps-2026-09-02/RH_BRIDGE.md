# Prime gaps and the Riemann Hypothesis: exact bridge and firewall

```text
Status: PROPOSED RH-DIRECTED ARCHITECTURE
Established here: implication map and research targets only
Riemann Hypothesis: unproved
```

## 1. Why the imported theorems do not imply RH

Let `p_n` be the nth prime. The bounded-gap import controls one extremal statistic:

\[
\liminf_n(p_{n+1}-p_n)\le 186.
\]

The long-gap import controls another:

\[
\limsup\text{-scale of }(p_{n+1}-p_n)
\quad\text{is at least a specified polylogarithmic function.}
\]

These statements discard almost all arithmetic information:

- the positions of most primes;
- the logarithmic weights `log p` and all prime-power weights `Lambda(n)`;
- signed deviations from the expected main term;
- oscillation across every Mellin/Fourier frequency;
- correlations across scales and residue classes.

RH is equivalent to, or follows from, global statements retaining this signed transform information. Infinitely many very small gaps and infinitely many very large gaps can coexist with RH and do not control zeros off the critical line.

## 2. The correct prime-side source

The natural source objects are

\[
\theta(x)=\sum_{p\le x}\log p,
\qquad
\psi(x)=\sum_{n\le x}\Lambda(n),
\qquad
E_\psi(x)=\psi(x)-x.
\]

Their Mellin transform is tied to `-zeta'(s)/zeta(s)`, and the explicit formula expresses a smoothed prime sum as a main term, archimedean/pole corrections, and a sum over zeros.

A precise formal target is a theorem schema such as

```text
ExplicitFormula(testFunction, normalization):
  primePowerSide = mainTerm + archimedeanTerm + zeroSide.
```

with one fixed convention for:

- `xi` and `zeta` normalization;
- Fourier/Mellin sign and `2*pi` factors;
- zero multiplicity and conjugation;
- admissible test space and contour shift;
- prime powers, pole terms, and endpoint weights.

This matches the Riemann repository's existing requirement for a canonical source contract. Gap theorems should consume consequences of that contract, not substitute for it.

## 3. Honest implication diagram

A useful formal map is

```text
RH
 |
 v
psi(x)=x+O(sqrt(x) log^2 x)   [after a reviewed explicit formula]
 |
 +--> square-root-scale upper bounds for all sufficiently large prime gaps
 |
 +--> weighted short-interval prime estimates
 |
 +--> consistency tests for prime-source numerical packets

Bombieri-Vinogradov / dispersion / trace-function estimates
 |
 v
DHL[k,2] + compact admissible tuple
 |
 v
bounded liminf gaps

short-translates random sieve + Erdos-Rankin cover
 |
 v
large limsup gaps.
```

There are no reverse arrows from either bottom endpoint to RH.

The forward RH-to-gap theorem itself must distinguish `psi` from `theta`: positivity of a `psi` increment may be caused by a prime power. A clean prime-gap consequence should either work with `theta` or explicitly bound the prime-power contribution.

## 4. Relation to the live Riemann proof programs

Two current review-pending PRs sharpen the repository's actual RH bottlenecks:

- PR #785 at `9a965c26fd3e0310736829689db1734bcb5c3ec4` isolates coefficient-resolved theta-lattice Schur extraction (`TLSE`) after proving a broad spectral positivity theorem. The missing coefficient sign is RH-bearing.
- PR #786 at `fc550cb0531e7abbc438a9b6eefa5ca11f90abc7` places `PRIMLS` at exact equivalence with RH and places `PRIMCAR` behind RH plus a short-interval Mobius mean-square input. It also warns that fixed-detector positivity is RH-equivalent, harder than RH, or false.

Those PRs are live sources, not part of this import or the trusted main spine. Their message is nevertheless decisive: a successful prime-gap bridge must eventually pay for uniform signed cancellation or coefficient extraction. Sieve support information alone cannot evade that cost.

## 5. Architecture PG-EF: prime source to RH

The most credible way to use the imports inside a full RH program is the following five-layer architecture.

### Layer 1 — canonical arithmetic source

Construct a reviewed distribution on logarithmic scale from `Lambda(n)` or `theta`, with exact prime-power and endpoint conventions. Prove its Mellin transform identity with `-zeta'/zeta`.

### Layer 2 — exact explicit formula

Prove Guinand-Weil/Weil explicit formulas on a sufficiently rich test-function space. Establish continuity and density statements needed to pass between compactly supported smooth tests, Paley-Wiener tests, and the repository's kernel families.

### Layer 3 — source decomposition informed by gaps

Use the prime-gap libraries to partition the source into local cells:

```text
clusters containing unusually small gaps
ordinary cells
long prime-free cells
prime-power corrections.
```

Derive exact identities, not statistical rhetoric. The aim is to represent the prime-side quadratic form as local positive energies plus a residual signed defect.

### Layer 4 — the actual RH-bearing estimate

Prove one of the following, with all quantifiers uniform:

- positivity of the complete Weil quadratic form;
- a source-admissible de Branges/canonical-system Hamiltonian;
- the theta-lattice coefficient-extraction theorem left by PR #785;
- the short-interval Mobius square-function estimate identified around PR #786;
- an equivalent square-root prime-discrepancy theorem.

This layer is not supplied by bounded or long gaps. Gap geometry is useful only if it helps dominate the residual signed defect.

### Layer 5 — completeness and conclusion

Prove that the chosen test family is complete for the RH criterion, transfer positivity/cancellation without a finite-to-global leap, and invoke the reviewed equivalence to conclude all nontrivial zeros have real part `1/2`.

## 6. A concrete new gap-based research attack

### 6.1 Log-prime Voronoi decomposition

Let `u_n=log p_n` and assign each `u_n` a cell bounded by midpoints to its neighbors. For a smooth test `f`, compare

\[
\sum_p (\log p) f(\log p)
\]

with the integral main term cell by cell. Seek an exact decomposition

\[
\text{prime source}(f)-\text{main source}(f)
 =\sum_n \bigl(B_n(f)+M_n(f)+R_n(f)\bigr),
\]

where:

- `B_n` is a boundary term determined by adjacent log-gaps;
- `M_n` is the local mass mismatch;
- `R_n` contains prime powers and smoothing corrections.

This identity should be provable unconditionally from definitions.

### 6.2 Local energy bound

On each cell, apply an exact Poincare/Wirtinger inequality to bound the boundary and mass defect by derivatives of `f`, with constants depending explicitly on the local gap. The bounded-gap theorem controls infinitely many favorable cluster cells; the long-gap theorem identifies rare cells where this local constant is large.

### 6.3 Global obstruction

The sum of local upper bounds is not automatically the sign needed by Weil positivity. The project must identify a compensating weighted mean-square or orthogonality theorem for the cell defects. This is the likely RH-equivalent gate. A useful outcome, even without closure, is an exact theorem saying which moment of the full gap/source sequence would suffice.

### 6.4 Candidate sufficient statement

Define a centered cell-defect coefficient `a_n` and a kernel-dependent local vector `v_n(f)`. A possible target is

\[
\left|\sum_n a_n v_n(f)\right|^2
\le \mathcal E_{\mathrm{arch}}(f)
\]

for every admissible test `f`, where the right side is the exact archimedean/main-term energy from the Weil form. If the explicit formula identifies the left side with the zero contribution in the correct normalization, this would imply the required positivity and hence RH.

The key point is that the theorem quantifies over all tests and retains signed coefficients. Merely bounding the largest or smallest gaps cannot prove it.

## 7. Finite-field structural opportunity

The Kloosterman assumptions in `PrimeGaps186` are finite-field RH-type cancellation statements. Their formalization offers a genuine structural laboratory:

```text
geometric object/sheaf
  -> Frobenius eigenvalue bounds
  -> trace-function pointwise/correlation estimates
  -> bilinear sieve cancellation
  -> bounded prime gaps.
```

This does not transfer classical RH by analogy. It may, however, contribute machinery useful for the repository's L-function and Frobenius programs:

- exact character and Fourier-transform normalization;
- self-dual trace kernels;
- conductor and exceptional-locus bookkeeping;
- correlation positivity/orthogonality;
- formal bridges from spectral bounds to arithmetic cancellation.

The right research question is not “does the 186 theorem prove RH?” but “which reusable geometric cancellation mechanism can be transported from the finite-field proof into a source-admissible classical explicit-formula argument?”

## 8. Firewalls

The following inferences are invalid and must never enter the claim graph:

```text
bounded gaps -> RH
large gaps -> RH
bounded gaps + large gaps -> RH
finite verification of gap statistics -> RH
Kloosterman/Deligne bounds over finite fields -> classical zeta RH
external numerical certificate passes -> Lean axiom discharged
spectral or average positivity -> coefficientwise Weil positivity
```

The permissible statements are:

```text
reviewed analytic inputs -> imported gap endpoint
RH -> strong global prime discrepancy -> upper-gap consequences
complete explicit-formula positivity/cancellation -> RH
```

## 9. Best next RH-facing theorem

Before attempting another direct positivity computation, prove a canonical Lean theorem connecting an exact Chebyshev error exponent to prime-gap consequences:

```text
ChebyshevError(alpha, logs) -> EventualPrimeInInterval(H_alpha)
```

and prove the reverse Mellin statement

```text
ChebyshevError(1/2, sufficient logs) -> RH.
```

This installs the missing semantic bridge between the repository's prime-side source and its zero-side criteria. The two imported gap packages can then be registered as independent endpoints on the same distribution interface, without pretending that their present hypotheses close the reverse direction.
