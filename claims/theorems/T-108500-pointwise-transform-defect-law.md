# T-108500 — Exact defect law for pointwise transforms of degree-2 local data

```text
Claim ID: T-108500
Status:   PROVED (statements 1-4, Theorems 2-3, Lemma 4 of the standalone
          proof; complete proofs) + VERIFIED EXACT (machine, m <= 5
          symbolic, 24 integer instantiations stdlib) + CONJECTURE only in
          the labelled trichotomy target
Created:  2026-08-30
Programme: #764 (Generalized L-Objects), axes A/B, research mode 1
Depends on: L-108001 (uniqueness of minimal rational forms); classical
          inputs cited in the proof (Shimura/Rankin-Selberg m=2 oracle,
          Cauchy identity, Jacobi-Trudi, Kronecker rationality criterion)
Proof:    standalone/2026-08-30-transform-defect-law/PROOF.md
Replay:   experiments/X-108500-transform-defects/  (stdlib, EXACT_RATIONAL)
Discovery layer: research/exploratory/2026-08-30-two-programme-pass/
          matrix/defect_powers_run.py (sympy 1.14.0), matrix/defects.json
RH status: RH and GRH are unproved; this claim does not address them.
```

## Statement (summary; the standalone file is authoritative)

For the generic degree-2 local object with Satake polynomial
`1 - aT + bT^2` and coefficients `h_k`:

1. `sum_k h_k^m T^k = N_m(T) / det(1 - Sym^m(A) T)` with
   `N_m ∈ Z[a,b][T]`, `N_m(0) = 1`, `deg N_m <= m-1`, exact denominator
   generically, and the closed coefficient formula
   `c_r = sum_u (-1)^{r-u} e_{r-u}(Sym^m) h_u^m`;
2. the linear-coefficient law `c_1 = a^m - h_m` (so the defect is
   nontrivial for every `m >= 2`);
3. **the self-duality functional equation of the defect**
   `N_m(T) = b^{m(m-1)/2} T^{m-1} N_m(1/(b^m T))` — the obstruction to
   functoriality is itself self-dual (proved via inversion-closure of the
   weight multiset at `b = 1` plus weighted homogenization);
4. the m=3 defect `1 + 2abT + b^3T^2` is irreducible over `Q(a,b)` AND its
   inverse roots are not rational multiples of weight monomials (the
   second statement needs a splitting-field argument beyond
   irreducibility — supplied after the adversarial wave flagged the gap):
   the m=3 defect EXITS the character ring, while m=2's defect is the
   sign-twisted determinant (classical Rankin-Selberg). For m >= 4 the
   exit is CONJECTURAL, not proved;
5. exact degeneration on the trace-zero (supersingular-type) locus:
   the m=2 defect cancels and the reduced local factor drops degree;
6. (Lemma) every polynomial pointwise transform of every bounded-degree
   local system is rational with a p-uniform degree bound — L3 of the #764
   ladder is never the obstruction; the ladder's discriminating power
   against polynomial transforms begins at L4/L6.

## Novelty position (boundary-audit gated)

PARTIAL_OVERLAP per the audit: defect extraction is classical (Shimura;
Moreno-Shahidi; plethysm); global meromorphy of defect Euler products is
governed by Estermann/Dahlquist/Kurokawa theory, and for GL(2) symmetric
powers the effective direction is Newton-Thorne. Believed new: the uniform
defect tables with exact-denominator minimality, the self-duality law (3),
the character-ring exit theorem (4), and the survival-ladder packaging.
The naive "effective defect iff global survival" criterion is FALSE and is
recorded as such; the corrected three-stratum survival question is stated
as a target in the standalone file, not claimed.

## Failure ledger

- F-108500-1: the initially conjectured effectivity iff was refuted at the
  meromorphy level by the boundary audit (`zeta(s)/zeta(2s)` retains
  continuation); replaced by the S1/S2/S3 trichotomy target.
- F-108500-2: naive coefficientwise instantiation checks fail on the
  trace-zero locus (the reduced form differs from the generic
  instantiation); the honest check is cross-multiplied rational-function
  equality, and the degeneration is now statement 5.
```
