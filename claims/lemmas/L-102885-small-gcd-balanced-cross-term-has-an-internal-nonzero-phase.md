# L-102885 — Every small-gcd balanced cross term has an internal nonzero phase

Claim ID: `L-102885`  
Status: **PROVED EXACT ADDITIONAL-PHASE REDUCTION**  
Created: 2026-08-24  
Depends on: `L-102834--L-102865`; `L-102884`  
RH status: **not assumed**

Retain a clean four-owner balanced cross term after the exact common-core
extraction of `L-102884`:

\[
N_1=P c_1^2,
\qquad
M_1=Q d_1^2,
\qquad
(c_1,d_1)=1,
\qquad
c_1d_1>1.
\]

Let

\[
\ell_3=P^+(c_1d_1)
\]

be the largest internal core-discrepancy prime.  Orient the pair so that
`ell_3|c_1`.  Then

\[
\ell_3\mid N_1,
\qquad
\ell_3\nmid M_1.
\]

Therefore

\[
N_1-M_1\not\equiv0\pmod{\ell_3}
\]

and the prime Ramanujan identity gives

\[
\boxed{
1=-\sum_{h_3=1}^{\ell_3-1}
 e_{\ell_3}(h_3(N_1-M_1)).
}
\tag{L-102885.1
\]

This identity is independent of, and commutes with, every selected external
owner phase in `L-102865`.

## 1. Three-or-more nonzero phase directions

The direct four-owner packet already has at least two nonzero external owner
phases.  Equation (L-102885.1) supplies a third nonzero coordinate whenever the
reduced cores differ.

Thus every cross term outside the power-saving large-gcd sector has the exact
form

```text
external nonzero owner phases
  x
one nonzero internal core-discrepancy phase.
```

No principal frequency is present in any selected coordinate.

## 2. Fixed-block internal phase energy

Let the phase act on the physical side not divisible by `ell_3`.  On any
dyadic Vaughan variable interval `C<=n<2C`, additive orthogonality gives

\[
\sum_{h_3=0}^{\ell_3-1}
\left\|
\sum_{n\sim C}{b_n\over n}
 e_{\ell_3}(h_3 Q n^2)
 \phi(\,\cdot-2\log n\,)
\right\|_2^2
\ll_\phi
\left(1+{\ell_3\over C}ight)
\sum_{n\sim C}{|b_n|^2\over n^2},
\tag{L-102885.2}

provided the remaining fixed factors are coprime to `ell_3`.  Common factors
are removed first by `L-102884`.  The same estimate holds after deleting the
zero phase.

## 3. New exact frontier

Define

```text
3QBC102885:
  after exact carrier, gauge, owner/core renewals and large-gcd removal, the
  coherent stopped balanced Vaughan sum with its adaptive external phases and
  the internal nonzero core-discrepancy phase has subpower logarithmic negative
  mass in the fixed ratio-eight outer observation.
```

Then

\[
\boxed{
\mathrm{3QBC}_{102885}
\Longrightarrow
\mathrm{SVQDSP}_{102882}
\Longrightarrow
\mathrm{BQSP}_{102870}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-102885.3
\]

The core-identical sector and every large common core have already been removed
by `L-102884`; the remaining theorem contains no zero phase or equal-product
multiplicity.