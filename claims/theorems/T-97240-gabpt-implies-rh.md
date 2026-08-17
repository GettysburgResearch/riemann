# T-97240 - GABPT implies the Riemann Hypothesis through one scalar Mellin transform

Claim ID: `T-97240`  
Status: **PROVED CONDITIONAL IMPLICATION; GABPT OPEN**  
Created: 2026-08-17  
Depends on: `L-97240--L-97244`, `R-97240`, Landau's theorem  
RH status: **unproved**

Assume `GABPT`, equivalently
\[
\mathcal R_X=5c_X(2)+3c_X(3)\ge0
\]
for every sufficiently large `X`. By `L-97240`, with `z=s+1/2`,
\[
\int_1^\infty\mathcal R_X X^{-s-1}\,dX
=\frac6{s^2}-\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
\tag{T-97240.1}
\]
Removing a finite initial interval changes the transform by an entire function.
Landau's abscissa theorem for a nonnegative Mellin density forces the tail
transform to be holomorphic throughout `Re s>0`, because the expression is
analytic on the positive real axis.

If `zeta(rho)=0` with `Re rho>1/2`, then `s=rho-1/2` lies in `Re s>0`. The finite
numerator in (T-97240.1) cannot vanish there: its zeros require `2^{-rho}=1` or
`2`, hence `Re rho=0` or `-1`. Thus (T-97240.1) would have a nonremovable pole,
a contradiction. The functional equation gives
\[
\boxed{\mathrm{GABPT}\Longrightarrow\mathrm{RH}.}
\]

`GABPT` is not proved by this packet. The Riemann Hypothesis remains unproved.
