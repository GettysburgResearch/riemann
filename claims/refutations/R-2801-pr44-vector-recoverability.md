# R-2801 — The historical PR #44 eigenvector is not recoverable from the committed scalar summary

Claim ID: R-2801  
Title: A retained leading eigenvalue and residual cannot reconstruct the missing carrier eigenvector  
Status: PROPOSED  
Authoring agent: `gpt56-04-c`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: draft PR #44 and its inherited X-0801 merger  
Scope: provenance of the `c=10^11`, `K=1024` carrier finalist  
Related counterexample candidates: none

## Statement

The actual floating eigenvector used to report the PR #44 cell

```text
c=10^11, K=1024, T=4709203636353.65
```

cannot be reconstructed from the files committed to that pull request.

This is not merely a missing convenience function. The committed information is
mathematically insufficient to identify the historical vector. Recovery requires
at least one external artifact that was not committed:

1. the original eigenvector;
2. the merged 1,024 complex Toeplitz lag coefficients;
3. all complete prime shard files; or
4. another complete deterministic regeneration input that fixes the same matrix
   arithmetic and accumulation order.

## Repository evidence

The retained PR #44 summary records:

- the largest prime Toeplitz eigenvalue;
- the leading margin;
- a residual norm;
- dimensions and finite term counts.

It does not contain the 1,024 vector components or the merged Toeplitz
coefficients. The inherited X-0801 merger constructs the Hermitian Toeplitz
matrix and calls

```python
numpy.linalg.eigvalsh(matrix)
```

which returns eigenvalues only. It does not calculate an eigenvector that could
have been preserved implicitly.

The changed-file ledger contains no target shard file, coefficient array, or
vector artifact. A blocking request for the original shards/vector was posted on
PR #44.

## Proof of non-identifiability

Fix any dimension `K>=2` and any real number `lambda`. For every unit vector
`u in C^K`, the rank-one Hermitian matrix

\[
 H_u=\lambda uu^*
\]

has largest eigenvalue `lambda` with eigenvector `u`. If desired, add an
arbitrary Hermitian operator of norm below `|lambda|` on `u^perp`; the leading
eigenpair remains unchanged while the rest of the matrix varies.

Thus the scalar leading eigenvalue does not determine the eigenvector. A scalar
residual norm does not repair this: for the exact pair above it is zero for
every `u`, and a prescribed positive residual can be produced by an arbitrarily
small perturbation in infinitely many directions.

Prime counts, cutoff, carrier, and dimension constrain how the missing matrix was
computed, but without its lag coefficients or a deterministic replay they do
not supply the missing `K^2` or Toeplitz `K` degrees of freedom. Therefore no
algorithm can infer the historical vector uniquely from the committed scalar
summary.

## Resolution adopted by X-2804

X-2804 makes the provenance failure impossible in future runs:

- regenerate or recover the complete lag coefficients;
- compute the leading vector explicitly with `eigh`;
- fix its arbitrary global phase canonically;
- export exact dyadic coordinates;
- bind the vector and full artifact with separate SHA-256 digests;
- record the residual, norm, Rayleigh value, backend, and coverage counts.

When the original shards are unavailable, a complete regeneration at the same
`T,c,K` produces a **replacement vector**, not the historical bit pattern. The
proof pass evaluates that replacement exact dyadic vector from scratch, so no
perturbation assumption or identity with the lost object is needed.

## Gap audit

1. This refutation concerns recovery from committed repository data; an agent may
   still possess the missing original files externally.
2. A regenerated replacement can reproduce the reported eigenvalue closely but
   is not thereby the historical vector.
3. SHA-256 preserves an artifact after creation; it cannot reconstruct an
   artifact that was never hashed.
4. The result says nothing about the mathematical sign of the carrier form.

## Suggested next attack

Complete the in-progress coverage-checked coefficient regeneration, freeze the
replacement vector immediately, and use only that exact object in the directed
prime certificate. If the original files later appear, preserve them separately
and compare the two vectors after canonical phase alignment.
