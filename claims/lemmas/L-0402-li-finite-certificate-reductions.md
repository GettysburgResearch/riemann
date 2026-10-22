# L-0402 — Finite certificate reductions for Li coefficients

Claim ID: L-0402  
Title: Exact local interval aggregation and a finite Cauchy–DFT alias bound  
Status: PROPOSED  
Authoring agent: `gpt56-04`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: L-0401; T-0303 only for the final RH implication  
Scope: proof-producing reductions for Issue #14  
Related counterexample candidates: any future negative Li coefficient

## Statement

Let

\[
G(z)=\frac{d}{dz}\log\left(2\xi\left(\frac1{1-z}\right)\right)
=\sum_{m\ge0}\lambda_{m+1}z^m.
\]

### A. Local recurrence

If `a1` and the quantities `B_k` of L-0401 satisfy

\[
a_1\in[\alpha_-,\alpha_+],\qquad
B_k\in[b_{k,-},b_{k,+}]\quad(2\le k\le n),
\]

then

\[
n\alpha_-+\sum_{k=2}^n\binom nk b_{k,-}
\le\lambda_n\le
n\alpha_++\sum_{k=2}^n\binom nk b_{k,+}.
\]

### B. Cauchy–DFT alias bound

Let `0<r<R<1`, `0<=m<M`, and assume `G` is analytic on a neighborhood of
`|z|<=R`.  With `omega=exp(2*pi*i/M)`, define

\[
D_{m,M}(r)=\frac1{Mr^m}\sum_{j=0}^{M-1}
G(r\omega^j)\omega^{-jm}.
\]

Then

\[
D_{m,M}(r)=\lambda_{m+1}+
\sum_{\ell\ge1}\lambda_{m+\ell M+1}r^{\ell M}.
\]

If `|G(z)|<=B` on `|z|=R`, then

\[
\left|D_{m,M}(r)-\lambda_{m+1}\right|
\le E:=\frac{B}{R^m}
\frac{(r/R)^M}{1-(r/R)^M}.
\]

Thus, if a rigorous backend proves
`D_{n-1,M}(r) in [d_-,d_+]`, then

\[
\lambda_n\in[d_- - E,d_+ + E].
\]

A strict negative upper endpoint is a finite sign certificate.  Together with
T-0303, a valid certificate implies RH is false.

## Proof

The local statement follows immediately from Formula A of L-0401 because all
multipliers are nonnegative integers.

For the Cauchy statement, substitute the absolutely convergent power series for
`G(r*omega^j)` into the finite sum.  The roots-of-unity filter

\[
\frac1M\sum_{j=0}^{M-1}\omega^{j(q-m)}
=1\text{ if }q\equiv m\pmod M,\quad 0\text{ otherwise}
\]

leaves exactly the indices `q=m+ell*M`.  Cauchy’s estimate on `|z|=R` gives
`|lambda_{q+1}|<=B/R^q`; summing the resulting geometric tail proves the bound.

## Analytic domain audit

- The outer disk must be zero-free for the transformed `xi`; checking only the
  sample points is insufficient.
- `R<1` keeps `z=1` outside the disk.
- `B` must bound the full outer circle, not a floating sampled maximum.
- The DFT interval must include all function, root-of-unity, summation, and
  rounding errors.
- For `lambda_n`, require `M>=n` so that `m=n-1<M`.

## Exact checker

X-0401’s `verify_dyadic_certificate.py` implements both reductions with Python
integers and `fractions.Fraction`.  It calls no special function or FFT.  It
checks interval propagation only; an independent analytic producer must prove
the supplied enclosures and analyticity premises.

## Gap audit

- Small `r^M` alone is not a tail proof; the factor `B/R^m` is essential.
- Synthetic negative certificates test the checker only and are not Li
  coefficient candidates.
- No actual analytic interval has yet been emitted.

## Adversarial tests

The committed tests accept strict synthetic negatives, reject zero touching and
alias widening through zero, and reject missing inputs, invalid radii, negative
bounds, insufficient sample count, schema drift, and an imaginary DFT interval
that excludes zero.

## Remaining uncertainty

The derivation appears complete but needs independent review.

## Suggested next attack

Build an Arb or separately audited producer for the exact schema.  Certify the
outer-circle supremum by interval subdivision and derivative bounds, then
cross-check one index independently with the local recurrence.
