# R-100200 — Jump reserve alone cannot prove the quadratic envelope

Claim ID: `R-100200`  
Status: **PROVED SCOPE FIREWALL**

The adverse activation jumps of the normalized envelope have total mass below the initial Euler reserve. This fact is useful but insufficient.

`L-100200` shows that on every integer cell the envelope evolves continuously as

\[
16r+24aX^{-1/2}-9bX^{-1}.
\]

When \(a<0\) and \(b<0\), this function can have a genuine interior minimum, whose sign is the Schur complement

\[
(-b)r-a^2.
\]

A positive jump-only reserve contains no information about this determinant. Therefore no proof may pass from “all adverse jumps are paid” directly to `FEAG99980`.