# L-102744 — A subcritical removal budget makes the carrier-quotiented Wick tail positive

Claim ID: `L-102744`  
Status: **PROVED EXACT POSITIVE-OPERATOR THEOREM**  
Created: 2026-08-23  
Depends on: `L-102729`; `L-102742`  
RH status: **not assumed**

Let `T` be a positive linear operator on a cone of nonnegative carriers, and
suppose

\[
 TK\le\rho K
 \qquad(0\le\rho<1).
 \tag{L-102744.1}
\]

Then, for every integer `j>=1`, positivity of `T` gives

\[
 T^{2j+1}K
 =T^{2j}(TK)
 \le\rho T^{2j}K.
 \tag{L-102744.2}
\]

Pair consecutive terms in the exponential Taylor remainder:

\[
\begin{aligned}
 (e^{-T}-I+T)K
 &=\sum_{j\ge1}
 \left[
 \frac{T^{2j}K}{(2j)!}
 -\frac{T^{2j+1}K}{(2j+1)!}
 \right]\\
 &\ge
 \sum_{j\ge1}
 \left(1-\frac\rho{2j+1}\right)
 \frac{T^{2j}K}{(2j)!}
 \ge0.
\end{aligned}
\tag{L-102744.3}
\]

The first pair yields the quantitative reserve

\[
 \boxed{
 (e^{-T}-I+T)K
 \ge
 \frac{3-\rho}{6}\,T^2K.
 }
 \tag{L-102744.4}
\]

## Application to the full filtered SHARP disk

For the labelled prime-removal operator

\[
 (Tf)(y)
 =\sum_{p\le y}p^{-1/2}f(y/p)
 +\mathbf1_{67\le y}67^{-1/2}f(y/67),
\]

`L-102729` proves, uniformly for

\[
 K_w=P_2|S_-+w|^2,
 \qquad |w|\le1/2,
\]

that

\[
 TK_w\le0.983K_w.
\]

Therefore

\[
 \boxed{
 (e^{-T}-I+T)K_w\ge0
 \qquad(|w|\le1/2),
 }
 \tag{L-102744.5}
\]

and more sharply

\[
 \boxed{
 (e^{-T}-I+T)K_w
 \ge0.336\,T^2K_w.
 }
 \tag{L-102744.6}
\]

Since logarithmic integration `J` is positive, the same statements hold for
the integrated filtered rays.

## Meaning

After exact removal of root and first chaos, the hard Wick source retains the
**entire filtered Hermitian disk** and carries a strict second-chaos reserve.
This conclusion uses the factorial exponential coefficients and is stronger
than generic disk positivity.

It does not orient the fixed outer ray `w=-8`: the latter lies outside the
proved disk, and a disk-positive quadratic can still have a negative outer
increment. The new reserve must be transported through the carrier-recombined
outer functional; that is the sharpened source-specific frontier in
`T-102810`.