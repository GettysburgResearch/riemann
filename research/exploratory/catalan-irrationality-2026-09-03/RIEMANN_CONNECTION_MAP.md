# Connection map into the Riemann repository

```text
Nature of connection:
  strong methodological overlap;
  weak direct RH implication;
  no theorem import into the trusted spine.
```

## 1. PR #757: beta source, primitive pairs, and divisor wavelets

PR #757 studies source-faithful Dirichlet-beta detectors, primitive-pair Gram
forms, Möbius untwisting, and divisor-wavelet reductions.

Sun's proof begins with the same Dirichlet beta function but in a different
regime:

```text
Riemann beta programs:
  beta data varying over height/scale, designed to detect zeta zero geometry

Sun preprint:
  one fixed special value beta(2), tested through its discrete tails.
```

The strongest transferable principle is the weighted-tail choice. The raw
tail recurrence is divided by `2m+1` before finite differences are taken. This
turns a rational recurrence into the Cauchy denominator needed by the
determinant and creates a local divisor structure that survives to the final
height inequality.

That is closely aligned with the repository's rule:

```text
do not take a universal norm or absolute value before the arithmetic
source has been transformed into the exact metric used at the endpoint.
```

Possible extraction:

- treat `u_m` as a canonical discrete beta sensor;
- compute its finite-difference and Mellin symbols;
- compare the Cauchy kernel with the ratio-16 primitive-pair Gram;
- test whether a block of weighted beta tails can supply a source-faithful
  determinant for the wavelet residual.

The irrationality proof does not establish any of PR #757's open RH-equivalent
Möbius estimates.

## 2. PR #758: compact beta detectors and information order

PR #758 classifies fixed compact beta detectors by their first surviving
moment and proves exact Chebyshev extremal statements.

Sun's residual matrix uses a complementary annihilation device:

```text
compact detector moment vanishing
<->
high finite difference annihilates a polynomial defect.
```

The full-rank proof shows that the residual cannot vanish in all selected
directions because that would create an impossible rational first-order
difference equation. This suggests a new detector invariant:

```text
recurrence-defect rank after polynomial annihilation.
```

One concrete project is to place the weighted tails `u_m` in PR #758's
information-order language and identify the exact order at which the rational
tail defect survives.

## 3. PRs #766 and #781: recurrence, alternants, and defect geometry

The overlap here is structural and unusually close.

Sun uses:

```text
finite recurrence
-> Newton completion
-> Pascal alternant
-> Cauchy determinant
-> Cauchy-Binet
-> two Vandermondes
-> local collision valuations.
```

PRs #766/#781 use:

```text
recurrence/Hankel rank
-> alternant or divided-difference formulas
-> defect numerator
-> specialization strata
-> exact determinant and syzygy identities.
```

The common algebraic nucleus is that a recurrence-selected matrix becomes
tractable only after the correct alternant completion. In Sun's proof, the
complement of the selected `S` rows has size three, and the Pascal alternant
quotient has degree at most `3S`. This is a concrete “codimension-three defect”
law analogous in spirit to the repository's alternant defect formulas.

Important firewall:

- `Psi_A(I)` is an alternant quotient, not automatically a Segre
  K-polynomial;
- `qhat_B` is a Diophantine approximant determinant, not an automorphic
  L-function;
- double Vandermonde divisibility does not imply spectral purity or RH.

A useful theorem-sized extraction would be a general
**Pascal-Cauchy completion lemma** parameterized by the number of omitted
Newton rows.

## 4. PR #769: exact relation and certificate discipline

PR #769's explicit resolution work distinguishes:

```text
dimension prediction
actual relation
exact residual check
global promotion theorem.
```

The Catalan preprint currently supplies formulas and claimed cell counts, but
not the actual 178-cell and 235-cell artifacts. The same discipline should be
applied:

```text
producer:
  enumerate cells, derive rational formulas, nominate interval bounds

checker:
  verify complete partition, adjacency, formula identity, exact integral,
  outward rounding, and final inequality

proof packet:
  consume only checker-approved rational data.
```

This is likely the fastest way to turn the numerical part into a durable
object.

## 5. PR #787: interval certificates in prime-gap work

The `PrimeGaps186` audit already separates a floating/FLINT producer from a
kernel-checked certificate. Sun's special-function enclosure is a natural
second test case for a shared exact-certificate library.

Needed primitives include:

- rational interval arithmetic;
- range reduction for logarithms;
- alternating arctangent enclosures;
- recurrence shifts for `psi`, Hurwitz zeta, and `log Gamma`;
- Euler-Maclaurin remainder bounds;
- partition completeness checks.

A common certificate schema could serve both the 152 physical-integral
inequalities and the Catalan small-prime constant.

## 6. Explicit-formula and prime-source programs

Sun uses the Prime Number Theorem only to pass from logarithmically weighted
prime powers to limiting integrals. It does not use zeta zeros.

Still, the local density calculation is a useful model for Riemann's prime-side
programs:

```text
exact prime-power layer
-> scaled local cost
-> singular baseline
-> finite correction integral
-> global weighted summation.
```

This resembles an explicit-formula source decomposition, but with a crucial
difference: the PNT averages unsigned/local height costs. RH requires signed
control at square-root scale.

## 7. Schur, Gram, and same-object discipline

The repository's operator programs repeatedly encounter a mismatch:

```text
a favorable bound is proved for one finite matrix,
while nonvanishing or positivity is needed for another.
```

Sun's key move is to define `H_B^min` from the exact same determinant
`qhat_B` whose real size is bounded. The local positive-part bridge never
switches to a more convenient surrogate scalar.

This is a valuable design rule for:

- cardinal-kernel Schur complements;
- primitive-pair Gram residuals;
- theta-source determinant quotients;
- finite carrier certificates.

## 8. Formal-v0.1 boundary

Nothing in the packet belongs in the current trusted release. A future
experimental Lean project could proceed in this order:

1. tails and recurrence;
2. finite-difference polynomial annihilation;
3. rational-difference no-solution theorem;
4. Newton completion;
5. Cauchy determinant;
6. Pascal alternant and degree bound;
7. local finite occupancy;
8. abstract positive-part height lemma;
9. PNT adapter;
10. exact numerical certificates.

The source theorem should remain an explicit proposition until all analytic
and computational inputs are closed.

## 9. L-function-family atlas

The most natural generalization is not immediately RH. It is to periodic
Dirichlet series

\[
L(2,\chi)=\sum_{n\ge1}\frac{\chi(n)}{n^2}.
\]

Questions suggested by the proof:

- Which periodic coefficient sequences admit a first-order tail recurrence
  after a finite-state lift?
- Which weights turn that recurrence into a Cauchy or confluent-Cauchy kernel?
- How many Newton completion columns are needed?
- Does the alternant quotient remain subquadratic?
- Can local prime-power saturation beat the archimedean baseline?
- Can one prove irrationality or linear independence for a family of
  \(L(2,\chi)\) values?

These are concrete additions to the generalized L-object atlas.

## 10. Summary table

| Riemann program | Imported mechanism | What remains open |
|---|---|---|
| beta detector | weighted tails and finite-difference residual | RH-bearing beta energy |
| primitive pairs | signed local factors retained to endpoint | Möbius cancellation |
| alternant/Segre | Pascal-Cauchy double Vandermonde | canonical geometric source |
| exact certificates | finite cell and interval architecture | released proof objects |
| Schur/cardinal | same-scalar local/global inequality | complete capture |
| prime source | prime-power scaled local densities | signed square-root cancellation |
| formalization | finite exact algebra | PNT, special functions, complete ledger |
