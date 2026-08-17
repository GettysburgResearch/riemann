# L-97202 — The complete P61 reserve is a tensor interface, not a colourwise reserve

Claim ID: `L-97202`  
Status: **PROVED EXACT GROUPING THEOREM**  
Created: 2026-08-17  
Depends on: PR #556; `R-97200`; `L-97201`  
RH status: **not assumed**

Let

\[
P_{61}=\prod_{p\le61}p,
\qquad
T_S=\mathop{*}_{p\mid S}(I-A_p)
\]

be the finite Euler projection on a source sequence. For a disjoint finite rough
set \(R\), convolution commutativity gives

\[
\boxed{T_{P_{61}R}=T_{P_{61}}T_R=T_RT_{P_{61}}.}
\tag{L-97202.1}
\]

This identity is valid only for the full grouped source. It does not say that
any summand indexed by one divisor \(d\mid P_{61}\) is positive.

For the 5:3 quotient packet of `L-97201`, define

\[
\Gamma_X(y)
=\sum_{d\mid P_{61}}\mu(d)
\left[-6h_X(dy)+9h_X(2dy)-3h_X(4dy)\right],
\tag{L-97202.2}
\]

where \(h_X(n)=n^{-1/2}H_X(n)\). The entire nonempty rough contribution is
exactly

\[
\boxed{
\sum_{\substack{r\mid R\\r>1}}\mu(r)\,\Gamma_X(r).
}
\tag{L-97202.3}
\]

The same formula with the pair \((-1,\sqrt2)\) gives the boundary-null grouped
source.

Every `d|P61` occurrence in (L-97202.2) remains inside \(\Gamma_X\). The
terminal reserve certified by PR #556 may be used only at that grouped level.
Equation (L-97202.3) also exposes why grouping does not remove accumulated rough
parity: the factor \(\mu(r)\) multiplies the whole grouped quantity.

## New consumer versus old reserve

`L-97200` takes a different, valid route. It leaves the small-prime coordinates
unsieved and positive. Their Euler factors become \(Z_{<67}(z)\), which is
nonzero in the required half-plane. Therefore no `d|P61` physical colour is
created at all.

The two operations must not be conflated:

```text
grouping P61 colours in the old source      exact but still rough-parity signed
absorbing small Euler factors analytically  exact change of consumer
promoting one finite colour                 invalid
using a grouped reserve as per-colour cash  invalid
```
