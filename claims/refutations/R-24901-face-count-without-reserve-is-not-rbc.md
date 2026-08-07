# R-24901 — Face counting without a reflected reserve is not `RBC(K)`

Claim ID: `R-24901`  
Title: A bounded endpoint-charge ledger can coexist with the untouched RH-bearing Möbius energy unless a strict same-source reserve is proved  
Status: **PROPOSED EXACT SCOPE CORRECTION PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #249  
Targets: PR #226 `L-9517/T-9509` and any successor boundary-count argument

## 1. Surviving top source

`L-24901` strengthens the free-lattice analysis but also sharpens the proof
boundary: every row below residual depth `K-1` is Euler-small, while the
`(K-1,K-1)` top-top corner remains.

By the fixed-logarithm decoder of `L-15159` and the exponent-retention theorem in
`R-23005`, this top source retains the complete Möbius/rightmost-zero exponent.
It is not a harmless endpoint correction.

## 2. Exact tautology

The reflected coefficient identity is an equality whose cross term is exactly
`2E`. Therefore a decomposition of the form

\[
2E=(2E)+B
\]

implies only `B=0`.

No bound on `E` follows from proving that `B` has bounded-dimensional endpoint
support. One must first prove that strictly less than the full target energy is
returned on the forcing side, or equivalently produce the Schur reserve of
`L-24904`.

## 3. Finite-dimensional control

Let `v` be any nonzero vector and let the reflected forcing be represented by

\[
F(v)=2\|v\|^2.
\]

Declare an empty boundary ledger, so the number of free endpoint coordinates is
zero. Then the face-count claim holds with `C_*=0`, but `\|v\|` is arbitrary.
This exact control shows that endpoint dimension and energy coercivity are
logically independent.

## 4. Corrected certificate boundary

A valid boundary-charge theorem must provide both:

1. a charge bound `q_K<=C_ref`; and
2. a strict reserve
   \[
   \kappa_0E_K\le\text{charged} + \text{strict lower scale},
   \qquad \kappa_0>0.
   \]

The first without the second is bookkeeping. The second is the arithmetic
content which can prove `BTP(K)`.

## 5. Classification

```text
bounded raw face dimension                     insufficient
bounded paid-coordinate count                  useful only with reserve
reflected identity at equal coefficient         tautological
strict source-bound Schur reserve               required
RBC(K) certificate existence                    open
RH                                               unproved
```
