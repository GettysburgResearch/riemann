# M-32401 — Review protocol for the critical-neutral cap route

Claim ID: `M-32401`  
Status: **FAIL-CLOSED REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-08

## 1. Frozen review order

1. PR #316 `L-30901/L-30902/T-30901`.
2. PR #323 `R-32201` zero-mode firewall.
3. `L-32401` affine-log analytic-core factorization.
4. `L-32402` critical-neutral scale theorem.
5. `T-32401` conditional CNCR chain.
6. A future production CNCR object.
7. PR #272 Cycle-Debt consumer and the atomized PR #297 pole criterion as independent downstream checks.

## 2. Mandatory algebra checks

Reconstruct exactly

\[
2^a(x-1)+1=2^a x\left(1-{1-2^{-a}\over x}\right)
\]

and therefore

\[
\log(2^a(x-1)+1)
=a\log2+\log x-
\sum_{\ell\ge1}{(1-2^{-a})^\ell\over\ell x^\ell}.
\]

Verify the coefficient-tail bound

\[
\sum_{\ell\ge1}{(1-2^{-a})^\ell\over\ell 4^\ell}
\le\log(4/3).
\]

Reject any proof which places the capped and uncapped functions on the wrong side of the cap point.

## 3. Zero-mode firewall

A reviewer must explicitly verify

\[
\widehat\beta(\rho-1/2)=1-\eta(\rho)=1
\]

at every zeta zero.

Reject any CNCR proof which uses a source-blind strict eta contraction on the complete critical state. The coefficient-one recurrence is intentional.

## 4. CNCR production requirements

A valid production certificate must emit:

1. every current cap state, with exact endpoint and exponent;
2. all same-destination recombinations before any absolute value;
3. the exact extracted affine-log analytic component;
4. the complete residual capped component;
5. every Pascal/fundamental-cycle correction;
6. the exact lower-scale destination of each residual;
7. every unit-endpoint interpolation term;
8. the total coefficient of all lower-scale cap states;
9. a proof that this total is at most one;
10. the polynomial fresh-injection ledger.

## 5. Mandatory mutations

Reject upon any of:

```text
PR #304's terminal atomic-norm estimate;
strict complete eta contraction;
five-adic residue contraction with character channels omitted;
absolute values before cap recombination;
uncapped affine-log terms left inside the unknown state;
dyadic coefficient >1;
dropped cap kink;
dropped bottom charge;
dropped 2/3 Mertens mutation;
finite numerical trend used as the cofinal theorem.
```

## 6. Status firewall

```text
L-32401 exact factorization                  proposed complete
L-32402 spectral threshold                  proposed complete
T-32401 CNCR -> RH                           conditional
CNCR                                         open
RH                                           unproved
```
