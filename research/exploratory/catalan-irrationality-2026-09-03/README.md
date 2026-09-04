# Catalan's constant irrationality preprint: source lock, audit, and Riemann map

```text
Status: IMPORTED / CLAIMED_BREAKTHROUGH / REVIEW_PENDING
Scope: exact 20-page source receipt; theorem-level proof audit; non-proof numerical replay
Source: Zhi-Wei Sun, arXiv:2609.04176v1, 3 September 2026
Riemann base: main@6dda8b5125457ed936330229f8c9eb6491728e76
Companion code or formalization found: none in the searches recorded here
Riemann Hypothesis: unproved; this preprint does not imply RH
```

The attached preprint claims the first proof that Catalan's constant

\[
G=\beta(2)=L(2,\chi_{-4})
 =\sum_{k\ge 0}\frac{(-1)^k}{(2k+1)^2}
\]

is irrational. If the proof survives specialist review, this is a major
Diophantine result about one of the simplest special values whose irrationality
had remained open.

The repository disposition is deliberately cautious. This packet preserves the
exact supplied PDF receipt, reconstructs the proof architecture, runs several
independent diagnostics, identifies concrete repair items, and maps the method
into Riemann's beta, determinant, alternant, divisor-wavelet, and formal
certificate programs. It does **not** register the headline theorem as verified
or import it into the trusted spine.

## Exact source receipt

```text
File: 2609.04176(1).pdf
SHA256:
1d05b36a5675cb8084935ec6945e004f1af9387c8fae6c48b242b4a94d73bd90

Size:       378564 bytes
Pages:      20
PDF:        1.7
Page size:  612 x 792 points
Title:      Catalan's constant is irrational
Author:     Zhi-Wei Sun
```

All twenty pages were rendered at 1870 by 2420 pixels and visually inspected.
See `PDF_AUDIT.md`.

No public companion repository, formal certificate, exact cell table, or
machine-readable interval certificate was located in the searches performed on
4 September 2026. The paper says that AI produced the numerical data, but the
posted PDF does not contain those artifacts.

## What the proof tries to do

The argument is an adelic determinant contraction.

```text
Catalan tail recurrence
  -> weighted tails u_m
  -> finite-difference residual matrix R
  -> full column rank
  -> one nonzero selected residual minor
  -> Newton completion to a square scalar qhat_B
  -> Pascal-Cauchy Cauchy-Binet expansion
  -> two Vandermonde factors
  -> p-adic lower bounds for every summand
  -> same-scalar upper bound for the minimal denominator H_B^min
  -> archimedean upper bound for |qhat_B|
  -> strict negative B^2 exponent
  -> nonzero integer of absolute value < 1
  -> contradiction.
```

The decisive idea is the choice of weighted tail

\[
u_m=\frac{T_m}{2m+1},
\qquad
T_m+T_{m+1}=\frac1{(2m+1)^2}.
\]

It makes the recurrence compatible with a Cauchy kernel
\(1/(2(i+j)+1)\), while the denominator-clearing product creates the local
prime-power structure used later.

## Current audit verdict

The proof has a coherent, technically interesting core. Several central finite
algebraic steps are independently intelligible, and the published numerical
constants were strongly corroborated by the diagnostic replay in this packet.

It is not yet safe to call the theorem verified. The v1 text has concrete
repair items:

1. Section 3 uses an undefined parameter `D`; dimension count and the formula
   for `F_B` force `D = 2B`.
2. The proof of Theorem 5.1 uses `S <= B/20`, but that hypothesis is absent
   from its statement.
3. Lemma 5.5 says all nonzero layers lie below `5B`. The preceding
   full-row/ideal-row denominator-layer difference can be nonzero above `5B`;
   a safe linear cutoff such as `7B` repairs the subsequent order estimate.
4. The exact 178-cell and 235-cell computational artifacts underlying
   Propositions 6.3 and 7.4 are not supplied.
5. Proposition 9.5, the load-bearing same-scalar asymptotic ledger, is given
   as a compressed synthesis. It still needs a complete uniform derivation,
   including the Pascal alternant factor, all `B^2 log B` cancellations, and
   every prime range.

Items 1–3 appear repairable without changing the final strategy. Item 5 is the
main verification gate. None of these observations proves the claimed theorem
false.

## Independent diagnostics performed

The included script is explicitly labelled `NON_PROOF_DIAGNOSTIC`. It reports:

```text
PDF hash/size receipt: exact match

Published final margin:
  conservative lower bound
  0.0096624265252323507287...
  > 0.00966242652523235

Small-prime constant:
  reconstructed c_odd
  0.006276744728100986
  published
  0.0062767447281009826...

Middle-prime integral:
  reconstructed
  0.17635583794457388
  exact published fraction
  0.17635583792864828...
  absolute difference 1.6e-11
  within the quadrature's reported error budget

Reduced inequality (5.21):
  437661 finite cases checked
  all odd Q, 20 <= B <= 300, 1 <= S <= floor(B/20)
  no failure
```

The floating quadratures are corroboration, not interval proofs. See
`NUMERICAL_REPLAY.md`.

## Strongest relevance to Riemann

The direct L-function connection is a special value, not a zero theorem:
\(G=L(2,\chi_{-4})\). The proof does not use the functional equation, an
explicit formula, zero-free regions, or RH. Its use of the Prime Number Theorem
is far weaker than RH.

The methodological connection is much stronger:

```text
one canonical scalar
+ exact archimedean estimate
+ exact local p-adic saturation
+ no premature absolute-value mismatch
= product-formula contradiction.
```

That is highly relevant to Riemann's current effort to keep arithmetic source,
detector, Gram, Schur, and local-divisor estimates attached to the **same**
object. It also gives a concrete model for turning Pascal/Cauchy alternants and
double Vandermonde divisibility into a global height inequality.

The most promising extraction is an abstract **same-scalar adelic contraction
theorem**, followed by a search for a zeta/xi determinant whose nonzero value is
forced by a hypothetical off-line zero. The latter bridge is wholly open and
would have to avoid finite-exception dilution and retain coefficientwise signed
information.

## Reading order

1. `PDF_AUDIT.md` — exact source and page map.
2. `MATHEMATICAL_DIGEST.md` — end-to-end proof reconstruction.
3. `PROOF_AUDIT.md` — verified pieces, repair items, and the main gap.
4. `NUMERICAL_REPLAY.md` — independent diagnostics and limitations.
5. `CLAIM_MAP.tsv` — compact theorem status table.
6. `RIEMANN_CONNECTION_MAP.md` — links to live repository programs.
7. `IMPROVEMENT_ROADMAP.md` — repair, formalization, optimization, and
   generalization.
8. `RH_LFUNCTION_BRIDGE.md` — what the method does and does not offer for RH.
9. `REPRODUCE.md` and `REVIEW_CHECKLIST.md` — exact replay and promotion gates.

## Nonclaims

This packet does not claim:

- independent verification of Theorem 1.1;
- peer review or community acceptance of the preprint;
- an irrationality measure for `G`;
- a proof for other even Dirichlet beta values;
- a formal Lean proof;
- that PNT-level prime summation supplies RH-level cancellation;
- that irrationality of one L-value constrains zeta zeros;
- that the finite numerical replay is a directed certificate.
