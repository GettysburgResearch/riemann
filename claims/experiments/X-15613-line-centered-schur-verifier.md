# X-15613 — Exact line-centered Schur perturbation verifier

Claim ID: `X-15613`  
Title: Fraction-only replay of the full-block perturbation and harmonic residual-short theorem  
Status: `EXACT FINITE RATIONAL REGRESSION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15632`

## Exact control

Use one low coordinate and one harmonic coordinate. The regularized soft metric
and harmonic metric are

\[
 D=\frac1{100},
 \qquad
 G=M=1.
\]

The line-centered block is

\[
 \mathcal H^0
 =
 \begin{pmatrix}
 1/100&1/10\\
 1/10&1
 \end{pmatrix}
 \succeq0,
\]

with zero Schur complement. Take

\[
 h=\ell=1,
 \qquad
 \varepsilon=\frac1{10},
\]

and perturb only the low diagonal by `-1/1000`. The actual Schur value is

\[
 \mathscr S=-\frac1{1000}.
\]

The exact theorem coefficient is

\[
 \eta
 =\frac1{10}(1+1)
 +\frac{(1/10)^2}{1-1/10}(1+1)^2
 =\frac{11}{45}.
\]

Therefore

\[
 \mathscr S\ge-\eta D=-\frac{11}{4500}.
\]

The normalized negative part is `1/1000`, leaving strict slack

\[
 \frac{11}{4500}-\frac1{1000}
 =\frac{13}{9000}>0.
\]

## Verified gates

The checker reconstructs and verifies:

1. positivity of the line-centered block;
2. the ambient floor and low upper bound;
3. both relative perturbation LMIs;
4. the line-centered harmonic minimizer;
5. the exact PR #191 trial-lift and residual short;
6. the actual Schur value;
7. the `L-15632` lower bound and normalized negative-part estimate.

Retained verdict:

```text
PASS_EXACT_L15632_SOFT_SCHUR_BOUND
```

Certificate SHA-256:

```text
58c9aca093b9fe93599249d97a7cddc05c2cf960d6788160dc44ecece72fb81c
```

Six central/adversarial tests are committed.

## Scope

This exact replay verifies finite rational algebra only. It does not verify the
production source-frame graph LMI, the complete Suzuki phase ledger, a growing
soft packet, or RH.
