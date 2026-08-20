# L-99612 — Every individual SHARP source atom has a strict owner half-contraction

Claim ID: `L-99612`  
Status: **PROVED EXACT LOCAL CONTRACTION AND GLOBAL-CARLESON REDUCTION**  
Created: 2026-08-20  
Depends on: `L-99610`  
RH status: **not assumed**

For fixed `x>=n>1`, put `y=x/n` and

\[
Z_x(n)=\frac{\beta_{67}(n)}{\sqrt n}T(y).
\]

Using (L-99610.7), write

\[
\boxed{
Z_x(n)
=
-\sum_{\substack{d\mid n\\d>1}}
a_x(n,d)Z_x(n/d),
}
\tag{L-99612.1}
\]

where

\[
a_x(n,d)=
\frac{\Lambda_{67}(d)}{\log n}
\frac{T(y)}{\sqrt d\,T(yd)}
\ge0.
\tag{L-99612.2}
\]

The target ratio has the exact strict bound

\[
\frac{T(y)}{\sqrt d\,T(yd)}<\frac1d,
\tag{L-99612.3}
\]

because

\[
\sqrt d\,T(yd)-dT(y)=3(d-\sqrt d)>0.
\]

If `q^e || n`, then

\[
\sum_{k=1}^e\frac{1}{q^k}\le\frac e2
\quad(q\ne67),
\]

and

\[
2\sum_{k=1}^e67^{-k}<\frac e2.
\]

Consequently

\[
\boxed{
\sum_{\substack{d\mid n\\d>1}}a_x(n,d)<\frac12.
}
\tag{L-99612.4}
\]

This is a genuine strict contraction at each *outgoing source node*.  It
survives at the critical exponent because the logarithmic owner and the SHARP
target ratio are both retained.

It does not by itself imply positivity after summing all source indices:
many descendants may charge the same smaller owner.  The sole remaining
operator question is therefore an incoming multiplicative Carleson embedding,
not another local sign or source-normalization theorem.
