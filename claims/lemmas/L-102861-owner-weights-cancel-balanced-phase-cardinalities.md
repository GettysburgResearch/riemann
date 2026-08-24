# L-102861 — Owner weights cancel balanced phase cardinalities exactly

Claim ID: `L-102861`  
Status: **PROVED EXACT BILINEAR NORMALIZATION THEOREM**  
Created: 2026-08-24  
Depends on: `L-102860`  
RH status: **not assumed**

Retain the notation of `L-102860`. Let `A_k` be the reduced `N`-side field
carrying the nonzero additive phase modulo `r`, and let `B_h` be the reduced
`M`-side field carrying the nonzero additive phase modulo `p`. Include in
`A_k` the literal owner coefficient `p^{-1/2}` and in `B_h` the literal owner
coefficient `r^{-1/2}`.

The balanced phase packet has the form

\[
\mathcal C_{p,r}
=d^{-1}
\sum_{h=1}^{p-1}
\sum_{k=1}^{r-1}
\langle A_k,B_h\rangle.
\tag{L-102861.1}
\]

Since the two phase variables are separated between the two sides,

\[
\mathcal C_{p,r}
=d^{-1}
\left\langle
\sum_{k=1}^{r-1}A_k,
\sum_{h=1}^{p-1}B_h
\right\rangle.
\]

Cauchy gives

\[
|\mathcal C_{p,r}|
\le
{1\over d}
\left(r\sum_k\|A_k\|^2\right)^{1/2}
\left(p\sum_h\|B_h\|^2\right)^{1/2}.
\tag{L-102861.2}
\]

Write

\[
A_k=p^{-1/2}\widetilde A_k,
\qquad
B_h=r^{-1/2}\widetilde B_h.
\]

Then the two apparent phase-cardinality factors cancel the two literal owner
weights:

\[
\begin{aligned}
|\mathcal C_{p,r}|
&\le
{1\over d}
\left({r\over p}\sum_k\|\widetilde A_k\|^2\right)^{1/2}
\left({p\over r}\sum_h\|\widetilde B_h\|^2\right)^{1/2}\\
&=
\boxed{
{1\over d}
\left(\sum_k\|\widetilde A_k\|^2\right)^{1/2}
\left(\sum_h\|\widetilde B_h\|^2\right)^{1/2}.
}
\end{aligned}
\tag{L-102861.3}

Thus the balanced dispersion step loses no positive power of either selected
owner prime. The cancellation is coefficient-exact and is unavailable when
both phase moduli are taken from the same physical side.

## Scope

Equation (L-102861.3) removes explicit modulus cardinality from one fixed
cross-side packet. It does not sum coherently over all owner pairs. The fixed-
pair phase energies are inserted in `L-102862`.