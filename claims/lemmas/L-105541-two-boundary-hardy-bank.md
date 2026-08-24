# L-105541 — Exact two-boundary Hardy realization and zero bank index

Claim ID: `L-105541`  
Status: **PROVED EXACT AT FOLDED SAFE-LINE SCOPE**  
Created: 2026-08-24  
Depends on: `L-105530`, `L-105540`, `L-105341`  
RH status: **not assumed**

Let `X_+` and `X_-` act on the two tensor factors of a folded right/left
safe-line observation.  They commute because they act on different factors.
Put

\[
\mathfrak R(X_+,X_-)
=\frac12\bigl((I-X_+)^{-1}+(I-X_-)^{-1}\bigr).
\tag{L-105541.1}
\]

Apply the bank of `L-105540` separately on the two factors.  The resulting
folded source multiplier is

\[
\Lambda(X_+,X_-)
=
\bigl(W_0(X_+)W_0(X_-)+W_1(X_+)W_1(X_-)\bigr)
\mathfrak R(X_+,X_-).
\tag{L-105541.2}
\]

The independent-variable identity of `L-105530` gives

\[
\boxed{
\Lambda-I
=
\frac{
4X_+^3+4X_-^3-2X_+^3X_--2X_+X_-^3-2X_+^2X_-^2
-X_+^3X_-^2-X_+^2X_-^3
}{32(I-X_+)(I-X_-)}.
}
\tag{L-105541.3}
\]

Thus every total source degree one and two vanishes before any Hermitian
specialization.  If `||X_+||,||X_-||<=r<1`, then

\[
\boxed{
\|\Lambda-I\|
\le
\frac{r^3(4+3r+r^2)}{16(1-r)^2}.
}
\tag{L-105541.4}
\]

For the Xi safe-line normalization, `r=O(1/log T)`, so

\[
\boxed{
\Lambda=I+O(\log(T)^{-3})
}
\tag{L-105541.5}
\]

in operator norm.

The observation map is the literal holomorphic map

\[
f\longmapsto(W_0(X)f,W_1(X)f),
\tag{L-105541.6}
\]

with the left inverse of `L-105540`.  Therefore it realizes the two-boundary
bank without scalar zero-freness, interpolation, or an auxiliary factorization.
The determinant-one completion has an entire inverse, so the bank itself has
zero strip partial index.  Any remaining partial-index or winding term belongs
to the Xi meromorphic quotient and not to the bank.

This theorem does not count the degree-zero carrier on a closed contour; the
firewall `R-105531` remains binding.
