# X-15611 — Exact verifier for the compression-to-spectral-tail bridge

Claim ID: `X-15611`  
Title: Fraction-only replay of `L-15626` on a nonreducing rational block  
Status: `EXACT FINITE RATIONAL REGRESSION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15626`

## Purpose

Verify that a strict compression floor controls

\[
 \operatorname{Tr}Q(\Gamma-A)_+Q
\]

even when `Q` is not invariant under `A`.

## Retained matrix

\[
 A=
 \begin{pmatrix}
 89/25&48/25\\
 48/25&61/25
 \end{pmatrix},
 \qquad
 P=\operatorname{span}\{e_1\},
 \qquad
 Q=\operatorname{span}\{e_2\}.
\]

The exact eigenpairs are

\[
 \lambda_1=1,
 \quad
 \phi_1=(3/5,-4/5),
\]

and

\[
 \lambda_2=5,
 \quad
 \phi_2=(4/5,3/5).
\]

Take

\[
 \Gamma=2,
 \qquad
 \gamma=61/25.
\]

The checker reconstructs the complete orthonormal eigenbasis and obtains

\[
 \operatorname{Tr}Q(\Gamma-A)_+Q={16\over25},
\]

\[
 \|QAP\|_{HS}^2={2304\over625},
 \qquad
 \gamma-\Gamma={11\over25},
\]

and therefore

\[
 {\|QAP\|_{HS}^2\over4(\gamma-\Gamma)}
 ={576\over275}.
\]

The strict exact slack is

\[
 {576\over275}-{16\over25}={16\over11}>0.
\]

## Trust boundary

The verifier uses only Python integers, `fractions.Fraction`, JSON, and exact
matrix-vector products. It verifies:

- symmetry and dimensions;
- the exact `P/Q` split;
- the strict compression moat;
- normalization, orthogonality, completeness, and validity of every eigenpair;
- the exact low-spectral trace;
- the Hilbert--Schmidt cross term;
- the final rational inequality.

It trusts no supplied eigenvalue-derived scalar.

## Files

```text
experiments/X-15611-spectral-tail-bridge/verify.py
experiments/X-15611-spectral-tail-bridge/certificates/synthetic.json
experiments/X-15611-spectral-tail-bridge/results/synthetic-verification.json
```

## Scope

This is an exact finite regression for the abstract theorem. It does not
construct the zeta-specific cofinal compression floor of `L-15627`.
