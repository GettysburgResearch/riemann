# L-102006 — Rankin control of the centered large-product collar tail

Claim ID: `L-102006`
Status: **PROVED EXACT WEIGHT BOUND; UNSIGNED CLOSURE REFUTED**
Created: 2026-08-21
Audited: 2026-08-21
Depends on: `L-102004--L-102005`; PR #691 `L-100615--L-100616`
RH status: **not assumed**

Retain the centered collar expansion

\[
\widetilde H_{ij}(X)
=
\sum_{\substack{S\subseteq(i,j)\\m_S>X/(p_ip_j)}}
(-1)^{|S|}m_S^{-1/2}\widetilde K_{ij}(X/m_S),
\]

with `|widetilde K_(ij)|<=256` from `L-102004`.

For `0<theta<1/2`, Rankin's inequality gives

\[
\mathbf1_{m_S>X/(p_ip_j)}
\le
\left(\frac{m_Sp_ip_j}{X}\right)^\theta.
\]

Hence

\[
\boxed{
\sum_{\substack{S\subseteq(i,j)\\m_S>X/(p_ip_j)}}m_S^{-1/2}
\le
\left(\frac{p_ip_j}{X}\right)^\theta
\prod_{p_i<p<p_j}(1+p^{-1/2+\theta}).
}
\tag{L-102006.1}
\]

This is an exact finite Euler-product majorant. It cannot be conclusion-facing:
`1/2-theta<1`, so the logarithm of the product contains the power-sized sum

\[
\sum_{p_i<p<p_j}p^{-1/2+\theta}.
\]

The explicit threshold of `L-102005` therefore does not become small after
source-blind absolute values.

## Source-side squared version

Suppose every interior prime `p<=Z` is completed before physical collapse, so
its native factor is replaced by

\[
I-p^{-1}U_{p^2}.
\]

Applying Rankin to the resulting product labels gives

\[
\boxed{
\left(\frac{p_ip_j}{X}\right)^\theta
\prod_{\substack{p_i<p<p_j\\p\le Z}}(1+p^{-1+2\theta})
\prod_{\substack{p_i<p<p_j\\p>Z}}(1+p^{-1/2+\theta}).
}
\tag{L-102006.2}
\]

For positive `theta`, even the squared product need not be subcritical over a
long interval; the threshold gain and the Euler masses must be balanced before
absolute values.

Let

\[
T=\frac{X}{p_ip_j}.
\]

If `Z>=sqrt(T)`, then every product of **two** unsquared primes above `Z`
strictly exceeds `T`:

\[
q_1,q_2>Z\quad\Longrightarrow\quad q_1q_2>Z^2\ge T.
\tag{L-102006.3}
\]

Thus the correct unsquared-depth boundary is two, not three. A one-label
unsquared product crosses the threshold only when that label itself exceeds
`T`; squared-core factors can also push depth-zero or depth-one terms across
the threshold.

```text
large-product localization            PROVED
unsigned Rankin closure               REFUTED
finite squaring improves small labels PROVED EXACT
unsquared depth >=2 at Z=sqrt(T)       AUTOMATICALLY ABOVE THRESHOLD
final signed recombination             OPEN
```
