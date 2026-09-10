# PDF audit: arXiv:2609.04176v1

```text
Status: EXACT SOURCE RECEIPT + VISUAL AUDIT
Scope: the 20-page PDF attached by the user
Mathematical status: source verification, not proof verification
```

## File receipt

```text
Title:      Catalan's constant is irrational
Author:     Zhi-Wei Sun
arXiv:      2609.04176v1 [math.NT]
Source footer date: 3 September 2026
SHA256:
1d05b36a5675cb8084935ec6945e004f1af9387c8fae6c48b242b4a94d73bd90

Size:             378564 bytes
Pages:            20
PDF version:      1.7
Page size:        612 x 792 points
Rotation:         0
Encrypted:        no
JavaScript:       no
Form fields:      none
Renderer output:  1870 x 2420 pixels per page
```

The PDF was not copied into the repository. The checksum is the durable source
lock.

## Visual inspection

All twenty pages were rendered and inspected. No blank page, missing page,
unexpected rotation, clipped body text, corrupt equation block, or obvious
pagination mismatch was observed.

The render process emitted a font-substitution warning, but the resulting pages
were legible and no visible missing-glyph blocks were found. This is an importer
inspection, not an independent typesetting or mathematical review.

## Page map

| PDF page | Main content |
|---:|---|
| 1 | Abstract; definition `G = beta(2)`; L-function context |
| 2 | Prior `L(2, chi_-3)` result; Theorem 1.1; tails `T_m`, weighted tails `u_m` |
| 3 | Five-stage architecture; notation; Theorem 2.1 |
| 4–6 | Full-column-rank proof; polynomial defect; impossible rational difference equation |
| 6–7 | Newton completion; fixed scalar `qhat_B`; minimal integerizer |
| 8 | Pascal alternant and Cauchy determinant; double Vandermonde |
| 9–12 | Prime-power layers; local valuation lower bound; saturation theorem; 2-adic layer |
| 12–13 | Full-row stability and ideal model |
| 13–15 | Odd small-prime limiting model; Hurwitz-zeta integral; interval claim |
| 16–17 | Middle-prime marginal ladder; exact rational integral |
| 17–18 | Large-prime piecewise density and gain |
| 18–19 | PNT summation; same-scalar quadratic ledger; strict margin |
| 19 | Final nonzero-integer contradiction |
| 19–20 | Acknowledgments and references |

## Exact editorial findings visible in the PDF

### Undefined `D`

On page 6, Section 3 defines the square matrix using:

```text
i^r, 0 <= r < D
binom(i, D + c_t), 1 <= t <= 3.
```

Page 7 then refers to the “first `D` columns,” while

```text
F_B = product_{r=0}^{2B-1} r!.
```

No definition of `D` appears. Since the matrix has

```text
D + S + 3 = N = 2B + S + 3
```

columns, `D = 2B` is forced. A revised source should state it explicitly.

### Missing regime in Theorem 5.1

Theorem 5.1 is stated for every odd prime power and `B >= 20`, but its proof
uses

```text
S <= B/20.
```

The final theorem later sets `S = floor(B/20)`, so the application lies in the
needed regime. The intermediate theorem still requires a corrected statement.

### Reused equation numbers

Section 5.1 restarts labels `(5.1)`, `(5.2)`, `(5.3)`, duplicating labels
already used earlier in Section 5. This is editorial but makes exact citation
ambiguous.

### `5B` support sentence

Lemma 5.5 states that all nonzero layers satisfy `p^nu < 5B` for large `B`.
For the full-row versus ideal-row denominator layer, the diagnostic example

```text
B = 100, S = 5, Q = 503
ideal layer  = 108
actual layer = 114
difference   = 6
Q > 5B
```

shows that `5B` is not a safe literal support cutoff for the quantity just
discussed. The source definitions give a uniform cutoff below
`6B + 2S + 5`, hence below `7B` in the final regime. Substituting such a safe
linear cutoff leaves the claimed `o(B^2)` estimate unchanged.

## Source completeness boundary

The PDF describes, but does not include:

- the 178 merged odd-small-prime cells;
- their rational quadratic formulas;
- the endpoint interval table;
- the 235 middle-prime affine cells;
- the exact integration program;
- a complete line-by-line expansion of Proposition 9.5.

No companion code repository was found in the searches recorded in
`SOURCE_LOCK.json`.
