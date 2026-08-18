# L-98103 — The rough prefix and active correction collapse to one polylogarithmic Stieltjes transport

Claim ID: `L-98103`  
Status: **PROVED EXACT SUMMATION IDENTITY + ASYMPTOTIC REDUCTION**  
Created: 2026-08-18  
Depends on: `L-98101/L-98102`  
RH status: **unproved**

Let

\[
S_Z(t)=\sum_{v\le t\atop P^-(v)>Z}{\mu(v)\over v}
\tag{L-98103.1}
\]

be the right-continuous rough reciprocal-Mobius prefix, and put

\[
Y=Y_\epsilon(X)=(\log X)^{4+\epsilon}.
\]

The function `U_Z(y)` is continuous and piecewise smooth on every compact
interval: every logarithmic hinge enters with value zero. Hence it has bounded
variation on `[2,Y]` and the following Stieltjes integral is classical.

Apply summation by parts to the active correction of `L-98102`:

\[
\mathcal A_\epsilon(X)
=
\int_{X/Y}^{X/2}\varepsilon_Z(X/t)\,dS_Z(t).
\tag{L-98103.2}
\]

Since

\[
U_Z(2)=0,
\qquad
\varepsilon_Z(2)=-A_Z,
\tag{L-98103.3}
\]

we obtain exactly

\[
\begin{aligned}
A_ZS_Z(X/2)+\mathcal A_\epsilon(X)
={}&
-S_Z(X/Y)\varepsilon_Z(Y)\\
&+
\int_2^Y S_Z(X/y)\,dU_Z(y).
\end{aligned}
\tag{L-98103.4}
\]

The `A_ZS_Z(X/2)` term cancels the lower activation endpoint
`S_Z(X/2)epsilon_Z(2)` exactly. This is the source-faithful recombination of the
nominal Euler main with its inactive boundary; neither may be estimated alone.

The remaining endpoint satisfies

\[
|S_Z(X/Y)\varepsilon_Z(Y)|
\le
{C_bE_Z\over\sqrt Y}
\prod_{Z<p\le X/2}(1+1/p)
=o(1/\log X)
\tag{L-98103.5}
\]

by `L-98101`. Combining with the bulk error gives

\[
\boxed{
U_{\rm full}(X)
=
\int_2^{(\log X)^{4+\epsilon}}
S_Z(X/y)\,dU_Z(y)
+o(1/\log X).
}
\tag{L-98103.6}

More explicitly, the omitted term is bounded in absolute value by
`2 mathcal B_epsilon(X)` with `mathcal B_epsilon` from `T-98100`.

Thus the final source-blind factor-67 obstruction is one Stieltjes correlation
between

1. the rough reciprocal-Mobius profile at long arguments `X/y`; and
2. the complete positive-cube child profile on the polylogarithmic interval
   `2<=y<=(log X)^(4+epsilon)`.

The measure `dU_Z` is signed; replacing it by total variation is not
conclusion-producing. Likewise, separate sign control of `S_Z` is not assumed.
The point of (L-98103.6) is the exact common-source pairing.