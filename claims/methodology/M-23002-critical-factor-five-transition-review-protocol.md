# M-23002 — Review protocol for the critical factor-five transition certificate

Claim ID: `M-23002`  
Title: Fail-closed review protocol for `CF5TC(R)`  
Status: **METHODOLOGY / PRODUCTION CONTRACT**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-08  
Target theorem: `T-23005`

## 1. Freeze discipline

A certificate must bind exact commits for:

```text
PR #236  all-ratio shell, digital recurrence, and R-23008;
PR #241  independent-frequency physical block;
PR #263  parity-paired source and finite Bezout reconstruction;
PR #269  factor-five localization and carry-space Schur reserve;
PR #234  fixed-ratio shell/rightmost-zero transfer.
```

Mutable branch heads are not acceptable proof dependencies.

## 2. Required source manifest

For every retained prefix and physical block, emit:

- the complete `b_2` and `omega_2` source coefficients;
- every dyadic translate and parity sibling;
- the finite Bezout synthesis coefficients;
- the complete quotient-cell labels `2`, `3`, and `4`;
- every finite boundary row;
- every noncoprime and endpoint correction;
- a duplicate-free hash of the complete source list.

The same-sign Möbius hypercube mutation from PR #239 must remain present in the
manifest.  It may disappear only through an explicit opposite-parity source
identity, never through a rank declaration.

## 3. Physical block requirements

The producer must use independent frequencies `(t,s)` and the exact block
kernel

\[
\Phi_{J,\alpha}(t-s).
\]

It must retain all source cross terms.  Automatic rejection follows from:

```text
one-frequency diagonalization;
H(z)^2 in place of a Hermitian mixed product;
entrywise absolute values before source recombination;
loss of a translated sibling;
using the global vertical norm as one physical block.
```

## 4. Carry-image map

The central proof object is a pair of exact finite maps

\[
\mathcal S_R:\mathcal H_{\rm physical}\to\mathcal H_{\rm carry},
\qquad
\mathcal S_R^*.
\]

The certificate must verify:

1. coefficientwise agreement on the complete source manifest;
2. every quotient cell in `2m<=n<5m`;
3. the positive generalized-prime synthesis of `L-26903`;
4. an operator or quadratic-form bound with total loss at most
   `R^(1+eta_R)`, `eta_R->0`;
5. preservation of the explicit carry Schur reserve after all source maps;
6. a complete kernel/cokernel ledger.

A carry-space reserve quoted without this source map does not verify `CF5TC`.

## 5. Tempered channel

Every term assigned to `D_R(J)` must have a separate proof of

\[
\limsup_{J\to\infty}{\log(1+D_R(J))\over J}=0.
\]

The certificate must classify each term as one of:

```text
finite endpoint;
archimedean boundary;
certified critical-line packet;
polynomial multiplicity term;
strict lower-scale output;
finite production boundary.
```

An unidentified source, the target transition block, or an off-line pole may
not be placed in the tempered channel.

## 6. Critical scaling mutation

The checker must test the digital prefix on a synthetic pole mode.  At a mode
with real part `beta`, the required inverse loss is

\[
R^{2\beta}/(\log R)^{O(1)}.
\]

It must reject:

- any claimed polylogarithmic inverse on a critical-line mode;
- any `R^(1-c)` loss at `beta=1/2`;
- any `R^(1+eta_R)` theorem that silently omits a positive-exponent mode.

## 7. Factor-five mutations

Mandatory exact mutations are:

1. a row in `m<=n<2m` must retain the positive pointwise wavelet;
2. rows in `2m<=n<4m` must retain the negative pointwise band;
3. the transition cell `4m<=n<5m` may not be declared positive without the
   production matrix;
4. every row `n>=5m` must reproduce the exact nonnegative Kummer tail;
5. the finite rows below the uniform-reserve threshold must be enumerated;
6. the generalized-prime digital correction must be retained.

## 8. Consumer mutations

A successful certificate must export at least one of:

```text
subexponential dyadic shell energy;
the exact 2/3 first-cell Mertens bound;
eventual bottom-charge one-sign;
a localized pole-exclusion inequality of T-23005.
```

The all-ratio causal filter must reproduce the first-cell source exactly.  A
packet-level claim of an automatic high-order Mertens difference is forbidden.

## 9. Verdicts

The production checker may emit only:

```text
CERTIFIED_CF5TC_CRITICAL_ORDER_OBSERVABILITY
UNRESOLVED_CF5TC_TRANSFERENCE
REJECTED_INCOMPLETE_SOURCE_MANIFEST
REJECTED_PHYSICAL_BLOCK_MISMATCH
REJECTED_RESERVE_LOST
REJECTED_NONTEMPERED_DEFECT
REJECTED_SUPERCRITICAL_CONDITION_NUMBER
```

No finite sample, floating reconnaissance, or synthetic matrix may emit an RH
verdict.
