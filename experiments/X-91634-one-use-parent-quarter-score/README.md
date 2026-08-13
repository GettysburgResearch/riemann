# X-91634 — corrected one-use parent quarter-score certificate

This replay certifies the scalar inequality compatible with one parent-capacity row. Put

\[
\Sigma(y)=\sum_{m\le y}\frac{\mu(m)}{\sqrt m}\left(5\sqrt{\frac ym}-3\right),
\qquad
\mathcal P(y)=\sum_{q\le y}\frac{\Lambda(q)}{\sqrt q}\log\frac yq.
\]

For every `1<=x<=67`, it proves

\[
\sum_{j=0}^{4}2^{j-4}\Sigma(4^jx)-\mathcal P(256x)
<-40.905782490079282354.
\]

The five coefficients are declared-score coefficients. The literal finite row is counted once: any exact parent row with ordinary response `w_(256x)` has entropy exactly `P(256x)` by the carry–entropy duality of `R-91633`. Charging a weighted sum of five literal entropies is impossible under one parent capacity.

The verifier uses exact Möbius and prime-power prefixes, integer-isqrt square-root enclosures, an atanh logarithm series with explicit positive tail, outward fixed-point interval arithmetic, and both one-sided endpoints of all `16,896` common cells plus every activated knot.

Run:

```bash
python3 verify.py
sha256sum -c SHA256SUMS
```

The positive one-use row identity is supplied separately by `L-91621` and the nested identity embedding `L-91559`. Those inputs remain subject to frozen-SHA replay and independent reconstruction. RH is not asserted here.
