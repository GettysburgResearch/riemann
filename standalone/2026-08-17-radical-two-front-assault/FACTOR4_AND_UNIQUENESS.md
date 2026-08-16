# Factor-four complete-gap quadrature and the unique positive two-row scalar

Date: 2026-08-17  
Status: **PROPOSED EXACT IDENTITIES / PRODUCERS REMAIN OPEN**

## 1. The factor-four complete-gap annulus

Take `h=log 2` in the exact annular triangularization. Put

\[
\mathfrak A_2(X)
=F_\Lambda(X)-2F_\Lambda(X/2)+F_\Lambda(X/4).
\]

Its Mellin multiplier is

\[
(1-2^{-s})^2,
\]

which has no zero in `Re(s)>0`. The compact tent weight is

\[
W_2(r)=
\begin{cases}
\log(4r),&1/4\le r<1/2,\\
-\log r,&1/2\le r\le1,\\
0,&\text{otherwise}.
\end{cases}
\]

The exact atom-versus-cell formula is

\[
\boxed{
\begin{aligned}
\mathfrak A_2(X)
={}&\int_{X/4}^{X}
S_\Lambda(\lfloor y\rfloor)y^{-3/2}W_2(y/X)\,dy\\
&-\sum_{X/4<q=p^a\le X}
\frac{\Lambda(q)}{\sqrt q}W_2(q/X).
\end{aligned}}
\]

Both terms are positive. All information outside `[X/4,X]` cancels exactly.
Thus a polylogarithmic bound for this one positive quadrature discrepancy is a
zero-safe RH producer.

## 2. Uniqueness of the `5:3` row

For a general scalar combination

\[
\alpha c_X(2)+\beta c_X(3),
\]

write `a=2^{-z}` and `b=3^{-z}`. The Mellin numerator is

\[
\alpha(2a-1-b)
+\frac\beta3(5b-a-1-3a^2).
\]

The `b` coefficient vanishes exactly when

\[
-\alpha+\frac{5\beta}{3}=0,
\qquad
\beta=\frac{3\alpha}{5}.
\]

Therefore, up to positive scaling, the unique two-row combination eliminating
the independent `3^{-z}` mode is

\[
\boxed{5c_X(2)+3c_X(3).}
\]

At this ratio the unsieved base dictionary is

\[
15,\ 6,\ 3,\ 6,\ 6,\ldots,
\]

and hence strictly positive. The numerator factors completely:

\[
\boxed{
5P_2(z)+3P_3(z)
=-3(2^{-z}-1)(2^{-z}-2).
}
\]

For `0<Re(z)<1`,

\[
\frac12<|2^{-z}|<1,
\]

so neither factor vanishes. This proves exact open-strip noncancellation using
one scalar row rather than an unbounded row family or two independent rows.

## 3. Common dyadic architecture

The two fronts are therefore governed by the same dilation:

```text
complete arithmetic gap:
    factor-four second difference (1-2^{-s})^2;

single reciprocal row:
    numerator -3(1-2^{-z})(2-2^{-z}).
```

Both preserve every open-strip zero. The remaining producers are arithmetic:

```text
ACTQ_2:
|F(X)-2F(X/2)+F(X/4)| <= polylog(X);

SPRP:
5c_X(2)+3c_X(3) >= 0 eventually.
```

Neither producer is proved here, and RH remains unproved.
