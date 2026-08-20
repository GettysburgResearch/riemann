# The native normalized SHARP box has a half-order, not unweighted, collar window

The conclusion-facing logarithmic box is

\[
\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
=\sum_{n\le X}\frac{\beta(n)}n\Phi(X/n).
\]

This fixes the source exponent. On the collar, translating
`-3u e^-u/2` by a subset product `n` contributes one factor `sqrt(n)`, so the
native coefficient is `beta(n)/sqrt(n)`. The exact variable collar mode is
therefore

\[
-3\sum_{X/67<n\le X}\frac{\beta(n)}{\sqrt n}
=-3\left[
B_{1/2}(X)-(1+67^{-1/2})B_{1/2}(X/67)
+67^{-1/2}B_{1/2}(X/67^2)
\right].
\]

The unweighted window obtained from `p^-1/2` acting on the normalized potential
belongs to a different source normalization.

For the independent compact Poisson route, the exact Cauchy average is

\[
Q_\tau(c)=\sum_{m,n}c_mc_n\min(m,n)^{2\tau}
=2\tau\int_0^\infty t^{2\tau-1}
\left(\sum_{n\ge t}c_n\right)^2dt.
\]

Thus the remaining theorem is one half-order cumulative-tail/cross-core
estimate. It has not been proved here, and RH remains unproved.
