# L-97241 - Adaptive even depth makes the homogeneous parity truncation positive

Claim ID: `L-97241`  
Status: **PROVED EXACT/INEQUALITY THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Let `0<=r_i<=r_max<1`, put `z=sum_i r_i`, and let `e_k` be the elementary
symmetric sums. For an even integer `L`, define
\[
S_{L-1}=\sum_{k=0}^{L-1}(-1)^ke_k.
\]
The full product is `P=prod_i(1-r_i)>0`. Maclaurin's inequality gives
`e_k<=z^k/k!`, and
\[
P\ge\exp\left(-\frac{z}{1-r_{\max}}\right).
\]
The exponential-tail Chernoff bound gives, for `L>z`,
\[
\sum_{k\ge L}e_k\le\sum_{k\ge L}\frac{z^k}{k!}
\le\left(\frac{ez}{L}\right)^L.
\]
Therefore
\[
\boxed{
L\log\frac{L}{ez}>\frac{z}{1-r_{\max}}
\quad\Longrightarrow\quad S_{L-1}>0.
}
\tag{L-97241.1}
\]
For rough-prime factors `r_i=p_i^{-1/2}`, one has `r_max<=67^{-1/2}`.
The smallest even integer satisfying
\[
L\ge8(z+1)
\tag{L-97241.2}
\]
obeys (L-97241.1). Hence adaptive depth escapes the fixed-depth sign no-go in
the complete homogeneous product model.

This theorem does not remove row-activation walls. Those walls are isolated in
`L-97244`.
