# Physical-scale Wick normalization and a signed strip cut

This note records the strongest conclusion that survived an attempted
unconditional ninety-percent proof.

## Corrected model

The Hermitian frozen symbol is

\[
1+2\Re\sum a(n)n^{-1/2-it},
\]

not the same display without \(n^{-1/2}\).  At cutoff \(e^{\alpha L}\), its
energy is

\[
\mathcal D_K(\alpha)
=
\sum_{m\ge K+1}q_{K,m}^2\frac{m!}{(2m)!}\alpha^{2m}.
\]

For the degree-four square-root polynomial and \(\alpha=2\),

\[
\mathcal D_4(2)
\le
\frac{173344649}{1275293859840}
<
\frac1{7000}.
\]

So the physically scaled model has ample reserve.

## Compression versus congruence

If \(C=V^*HV\), every source-fixed map \(A\) gives
\(A^*CA=(VA)^*H(VA)\), and its positive index cannot exceed that of \(H\).
A holomorphic multiplier need not be zero-free merely to define a compression.

But off the real line the Hermitian factor is \(p p^\#\), not \(p^2\).  This is
why the positive formal source identity does not by itself pass through the Xi
contour.

## Accretive anchor

For a contraction \(X\),

\[
(I-X)^{-1}+(I-X^*)^{-1}-I
=
(I-X^*)^{-1}(I-X^*X)(I-X)^{-1}\succeq0.
\]

Thus the safe-line source has a positive anchor.  If the complete Xi
compression is \(C=B+E\) with \(B\ge G\), then

\[
\nu_{\le0}(C)
\le
\operatorname{tr}\!\left[
(G^{-1/2}EG^{-1/2})_-
\right].
\]

A normalized negative trace below \(1/20\) leaves more than \(19/20\) positive
directions.  The full confluent signature then gives more than \(90\%\) of
zeta zeros on the line.

The required negative-trace estimate is `STRIPNEG105520`.  It contains the
Hardy polarization, vertical/endpoint, archimedean, taper and companion-flux
terms.  It is not proved here.  Ninety percent and RH remain unproved.
