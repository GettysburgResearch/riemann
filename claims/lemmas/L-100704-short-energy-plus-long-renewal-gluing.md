# L-100704 — A short-interval energy estimate and a long-interval one-sided estimate jointly close RH

Claim ID: `L-100704`  
Status: **PROVED EXACT IMPLICATION-MATRIX GLUING THEOREM**  
Created: 2026-08-20  
Depends on: PR #691 `L-100605`; `L-100702`; `L-100703`  
RH status: **not assumed**

Apply the exact double-owner coefficient decomposition to the minimal ordinary-
Mobius wavelet `G_mu`. For `X>8` its empty-source term vanishes. Split

\[
G_\mu(X)=G_{\rm sh}(X)+G_{\rm lo}(X),
\tag{L-100704.1}
\]

where

```text
G_sh:
  diagonal blocks i=j and off-diagonal blocks p_j/p_i<=8;

G_lo:
  off-diagonal blocks p_j/p_i>8.
```

This is an exact source partition. No cutoff remainder is introduced.

Define the two terminal statements:

\[
\boxed{
\int_{2^L}^{2^{L+1}}|G_{\rm sh}(X)|^2{dX\over X}
=2^{o(L)}
}
\tag{SCME100704}
\]

and

\[
\boxed{
\int_{2^L}^{2^{L+1}}(G_{\rm lo}(X))_-{dX\over X}
=2^{o(L)}.
}
\tag{LRNM100704}
\]

Then

\[
(G_\mu)_-
\le |G_{\rm sh}|+(G_{\rm lo})_-.
\tag{L-100704.2}
\]

By Cauchy--Schwarz on a logarithmic block,

\[
\int_{2^L}^{2^{L+1}}|G_{\rm sh}(X)|{dX\over X}
\le(\log2)^{1/2}
\left(
\int_{2^L}^{2^{L+1}}|G_{\rm sh}(X)|^2{dX\over X}
\right)^{1/2}.
\tag{L-100704.3}
\]

Therefore `SCME100704 + LRNM100704` imply subpower logarithmic negative mass
for `G_mu`. The minimal-wavelet Mellin--Landau theorem yields

\[
\boxed{
\mathrm{SCME100704}+\mathrm{LRNM100704}
\Longrightarrow RH.
}
\tag{L-100704.4}

## Why the two statements are complementary

- `SCME100704` is the natural output of the centered-moment/phase route. The
  endpoint ratio is bounded, the physical shell is fixed, and a Hilbert-space
  estimate can retain cancellation.
- `LRNM100704` is the natural output of interior squaring plus positive divisor
  renewal. Long intervals have room for source-side completion while the two
  endpoint owners remain fixed.

Neither statement alone covers the full native source. Together they cover it
exactly and only once.

This is the first conclusion theorem in the matrix whose hypotheses are
assigned to two different existing mechanisms rather than asking one estimate
to solve every geometric regime.
