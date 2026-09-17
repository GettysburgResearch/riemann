# Exact dependencies and mathematical boundaries

## P7: inherited computer-assisted inequality

The hypothesis called P7 in PROOF.md is a single continuum inequality in six nonnegative gaps for the EXACT kernel K(x)/K(0). It is proved by the public `ainta/zeta-simple-zeros` certificate and independently reconstructed by reviewer A in this repository.

- External freeze: `040c5e899e658aed7b56a2a87f501798fe10761d`.
- External manuscript: `paper/riemann.tex`, blob `fed199bb7e641c718ac1f33d5e885c0b412d5080`.
- Repo freeze: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
- Reviewer manuscript: `reviews/A/supplement/REPORT.md`, blob `e1359f93c399c783e01c86d614fa02e86666671a`, S01–S02.

The reviewer transcript covers 713,315 nodes, with zero unclosed terminal cells. Its elementary source backend is outward 128-bit dyadic arithmetic; accumulation/range layers use explicitly widened binary64 `nextafter`. Those mixed-arithmetic hypotheses remain part of the inherited certificate. The original ainta 707,901-node Arb transcript is a different execution, not another name for the reviewer's transcript.

This pass read the full reported continuum-cover argument and the external TeX statement/proof interface. It did NOT acquire and rerun every source module or execute the seven-point search. Thus the new small checker is not a standalone reimplementation of P7. A referee should use either authenticated source campaign and its analytic cover proof to validate this imported input.

## Stability inequality: inherited and rederived

[A, Section 2] proves

```
||VV*+Q||_F^2 >= 4 tr(VV*+Q)-3r-4b+tr Psi(V*V)
```

for column norms <=1 and n_+(Q)<=b. PROOF.md Section 4 includes a complete rederivation, with zero padding and dependencies allowed. This inequality and the 67.3 percent idea already belong to the external source. The new result is not obtained by claiming their authorship.

## Analytic zeta input: primary manuscript, not an RH-equivalent assumption

Primary source:

`https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf`

35-page manuscript, dated August 10, 2026, author line Claude. The arXiv follow-up is associated with Alpöge–Furman (`2608.13637`), but this proof locks the concrete publisher PDF whose theorem statements were inspected.

Required mathematical outputs:

1. Complete finite-grid Parseval identity and the actual simple-zero columns (Lemma 2.2).
2. The finite outside-zero truncation and the positive index of the nonsimple/off-line part (Propositions 4.1–4.4).
3. The complete outside-zero trace-norm estimate (Proposition 4.2), applied to the optimized smooth taper.
4. The unconditional prime-side trace and squared Frobenius norm, at the optimized cosine taper (Section 5, Section 7.1, Theorem D and its proof).
5. Classical Riemann–von Mangoldt and unit-interval zero counting for collars and dyadic-to-global transfer.

This pass inspected parsed primary text and images of the relevant pages, including printed pp. 8, 12–13 and 21. It did not independently reproduce the entire 35-page analytic proof, run its formalization or certify a PDF byte hash. The PDF URL/version/date and exact sections, rather than an invented local checksum, identify this import.

The source's 67.25 percent scalar bound ALONE is not enough for our conclusion: the actual vectors, index decomposition and normalized trace statements are needed. They are stated explicitly in PROOF.md Section 6.

## New bridge

The previous extraction justified kernel replacement only on fixed-separation blocks. That would not support an unbounded separated block by itself. PROOF.md Section 5 proves a different, global trace-norm estimate:

```
||M_actual-G_exact||_1 <= r [4/(K0 L)+4/L^2].
```

The r factor, the normalized density discrepancy and the full omitted grid trace are all explicit. No entrywise error is summed as though it cost only r when it actually cost r^2.

## No unresolved conjectural premise in the proposed proportional corollary

Once the imported P7 certificate and published analytic estimates are accepted, the new proportional conclusion follows by the complete arguments in PROOF.md. There is no new signed Möbius estimate, global zero-confinement assertion, unproved pair-correlation conjecture or RH hypothesis.

That is a statement about the logical dependency graph, not a claim of independent review of all its inputs. The new composition needs review in its own right. No finiteness of exceptional off-line zeros or implication to RH is established.
