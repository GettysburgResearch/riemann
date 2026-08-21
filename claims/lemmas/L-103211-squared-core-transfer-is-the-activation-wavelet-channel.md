# L-103211 — Squared-core source transfer feeds the compact activation-wavelet channel

Claim ID: `L-103211`  
Status: **PROVED EXACT INTERFACE IDENTITY**  
Created: 2026-08-20  
Depends on: `L-103210`; PR #697 `L-101101`  
RH status: **unproved**

Let

\[
\mathcal A_\beta
=
\sum_n\frac{\beta(n)}{\sqrt n}\delta_{\log n}
\]

be the activation measure and let

\[
P_2=(I-\sqrt2S_2)(I-S_2)^2,
\qquad
Jf(X)=\int_1^Xf(t)\frac{dt}{t}.
\]

The compact activation channel in PR #697 is

\[
\mathcal A=-\frac13JP_2\mathcal A_\beta.
\]

A source transition \(p^{-1/2}S_pF\) shifts every activation atom by
\(\log p\) and multiplies it by \(p^{-1/2}\).  Since \(J\), \(P_2\), and
multiplicative shifts commute,

\[
\boxed{
JP_2\mathcal A[p^{-1/2}S_pF]
=
p^{-1/2}S_p\,JP_2\mathcal A[F].
}
\]

Therefore the moving squared-core cutoff does not create a new third type of
error.  It feeds the existing compact activation-wavelet channel, with exact
source provenance.

This supplies the correct two-channel architecture:

```text
continuous quadratic/collar boundary;
atomic moving-completion/activation boundary.
```

PR #697 proves that a uniformly subcritical signed matrix coupling these two
channels would imply RH.  The source identity here does not prove either
arithmetic matrix row.
