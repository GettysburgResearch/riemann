# L-100501 — The critical dyadic inverse has square-root cost

Claim ID: `L-100501`
Status: **PROVED EXACT INTERFACE FIREWALL**
Created: 2026-08-20
Depends on: PR #674's minimal annihilator
RH status: **unproved**

The minimal filter is

\[
\mathscr D
=
(I-\sqrt2S_2)(I-S_2)^2.
\]

The two neutral factors have polynomial inverse coefficients,

\[
(I-S_2)^{-2}
=
\sum_{j\ge0}(j+1)S_{2^j}.
\]

The half-order factor has the exact positive inverse

\[
\boxed{
(I-\sqrt2S_2)^{-1}
=
\sum_{j\ge0}2^{j/2}S_{2^j}.
}
\tag{L-100501.1}
\]

At scale \(X\), the active coefficient mass in (L-100501.1) is comparable to

\[
\sum_{j\le\log_2X}2^{j/2}\asymp\sqrt X.
\]

Thus a source-blind reconstruction of the unfiltered critical state from one
minimal wavelet necessarily pays the full square-root scale. The critical
factor is the homogeneity \(X^{1/2}\), not an artifact of the chosen proof.

A finite-dimensional version is equally sharp. Let \(e_1,\dots,e_N\) be
orthonormal labels and let the physical collapse send every \(e_j\) to one.
Then

\[
\left\|\mathcal C\right\|=\sqrt N.
\]

Choosing equal coefficients on any subinterval on which \(K_0\) has one sign
gives labelled diagonal energy one and physical wavelet magnitude
\(\asymp\sqrt N\).

Therefore none of the following alone proves the wavelet criterion:

```text
the coefficient diagonal;
the free labelled square function;
a source-blind inverse of the dyadic annihilator;
Cauchy--Schwarz after label collapse.
```

The remaining estimate must use the actual Möbius tails in
`L-100500.2` before absolute values.
