# X-15613 — Exact joint profile-soft direct-short verifier

Claim ID: `X-15613`  
Title: Fraction-only replay of the regularized local-Weyl remainder and main-profile harmonic short  
Status: `EXACT FINITE RATIONAL REGRESSION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15632`

## Retained control

Use a one-dimensional soft packet and one-dimensional harmonic packet.  The
joint main profile Gram is

\[
 \mathcal D=
 \begin{pmatrix}
 1/100&1/10\\
 1/10&1
 \end{pmatrix}\succeq0,
\]

whose main-profile Schur complement is exactly zero.  Put

\[
 L=10,
 \qquad
 \tau=1/20,
 \qquad
 \varepsilon=1/20,
 \qquad
 G=M=1.
\]

The joint remainder is

\[
 \mathcal E=
 \begin{pmatrix}
 -1/100&1/100\\
 1/100&0
 \end{pmatrix}.
\]

The checker proves exactly

\[
 -\varepsilon L\widehat{\mathcal D}
 \preceq\mathcal E\preceq
 \varepsilon L\widehat{\mathcal D},
\]

with

\[
 \widehat{\mathcal D}
 =\mathcal D+\tau\operatorname{diag}(1,1).
\]

The main-profile solve is

\[
 X_0=1/10,
\]

and its actual harmonic residual is

\[
 \mathscr R_0=1/100.
\]

The complete exact matrix is

\[
 \mathcal H=L\mathcal D+\mathcal E.
\]

Its fully shorted soft value is negative:

\[
 \boxed{
 \mathscr S=-\frac{1201}{100000}.
 }
\]

The theorem bound is

\[
 4(\varepsilon+4\varepsilon^2)L\tau
 =\frac3{25},
\]

and therefore

\[
 0<\frac{1201}{100000}<\frac3{25}.
\]

The checker also reconstructs the exact `L-18512` identity

\[
 \mathscr S
 =J_{X_0}^*\mathcal HJ_{X_0}
  -\mathscr R_0^*\mathcal H_{EE}^{-1}\mathscr R_0.
\]

## Validation

```text
6/6 central and adversarial tests pass
certificate SHA-256
febcbd51d850165435b53d5fc7819c16b9b94d2126887e94c11f640e377b8c74
verdict
PASS_EXACT_L15632_DIRECT_SHORT_LMI
```

The mutation suite rejects:

- an indefinite profile Gram;
- failure of the soft threshold;
- failure of either relative remainder LMI;
- an excessive relative error;
- loss of the positive ambient profile block.

## Scope

This artifact verifies the exact finite algebra and the quantitative constant in
`L-15632`.  It does not contain a production Suzuki profile Gram, complete prime
manifest, actual soft spectral projector or cofinal support sequence.
