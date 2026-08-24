# L-105282 — The Wick source has a superfactorial half-derivative budget

Claim ID: `L-105282`  
Status: **PROVED AT THE FROZEN DIRICHLET MODEL SCOPE**  
Created: 2026-08-24  
Depends on: L-105250--L-105253; L-105520  
RH status: not assumed

Let

\[
f_{K,L}(t)=
\sum_{n\le e^{\alpha L}}
\frac{a_{K,L}(n)}{n^{1/2+it}}
\]

be the carrier-free degree-\(K\) Wick source at physical cutoff \(\alpha\).
The normalized source half-derivative energy is

\[
\boxed{
\mathcal E_{1/2}^{\rm src}(K,L,\alpha)
=
\frac1L
\sum_{n\le e^{\alpha L}}
(\log n)\frac{|a_{K,L}(n)|^2}{n}.
}
\tag{1}
\]

Since \(0\le\log n/L\le\alpha\),

\[
\boxed{
\mathcal E_{1/2}^{\rm src}(K,L,\alpha)
\le
\alpha
\sum_{n\le e^{\alpha L}}
\frac{|a_{K,L}(n)|^2}{n}.
}
\tag{2}
\]

The physical prime-simplex theorem therefore gives

\[
\boxed{
\limsup_{L\to\infty}
\mathcal E_{1/2}^{\rm src}(K,L,\alpha)
\le
\alpha\mathcal D_K(\alpha).
}
\tag{3}
\]

Allowing both analytic orientations costs at most the conservative factor two

\[
\mathcal E_{1/2}^{\rm two\text{-}sided}
\le2\alpha\mathcal D_K(\alpha)+o(1).
\tag{4}
\]

For every fixed \(\alpha\le2\), this bound tends to zero superfactorially as
\(K\to\infty\).  At degree four, using the corrected physical estimate

\[
\mathcal D_4(2)
\le
\frac{173344649}{1275293859840},
\]

one obtains

\[
\boxed{
2\alpha\mathcal D_4(\alpha)
\le4\mathcal D_4(2)
<\frac1{1700}.
}
\tag{5}
\]

Thus the frozen source has vastly more than the half-derivative reserve needed
for a ninety-percent theorem.

The unproved step is not the source energy.  It is `AHXFER105280`: transfer the
source half-derivative budget to the boundary all-pass quotient of L-105281
without losing the near-real Blaschke phase slips.  Ordinary \(L^2\), trace,
or Hilbert--Schmidt transfer is insufficient.
