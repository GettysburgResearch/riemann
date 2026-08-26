# L-103004 — The endpoint Wronskian has an exact finite log-ratio budget

Claim ID: `L-103004`  
Status: **PROVED EXACT INTEGRATED KERNEL THEOREM**  
Created: 2026-08-25  
Depends on: `L-103000--L-103001`  
RH status: **not assumed**

Let

\[
a(u)=A(e^u),
\qquad
b(u)=A_-(e^u),
\]

and define the autocorrelation

\[
C(\delta)=\int_{\mathbb R}a(u)a(u-\delta)\,du.
\]

For `delta>0`, the endpoint Wronskian is

\[
W_\delta(u)
=b(u)a(u-\delta)-a(u)b(u-\delta).
\]

Since `b=a'-a/2`, integration by parts gives

\[
\boxed{
\int_{\mathbb R}W_\delta(u)\,du
=2C'(\delta).
}
\tag{L-103004.1}
\]

By `L-103001`, `W_delta<=0`. Therefore

\[
\boxed{
\int_{\mathbb R}|W_\delta(u)|\,du
=-2C'(\delta).
}
\tag{L-103004.2}
\]

The support of `a` has length `2 log 2`, so

\[
C(\delta)=0
\qquad(\delta\ge2\log2).
\tag{L-103004.3}
\]

The exact spline formula of `L-103000` gives

\[
\boxed{
C(0)=\|a\|_2^2=12\log2-8.
}
\tag{L-103004.4}
\]

Integrating (L-103004.2) over every possible positive source separation yields the exact finite budget

\[
\boxed{
\int_0^{2\log2}
\int_{\mathbb R}|W_\delta(u)|\,du\,d\delta
=24\log2-16.
}
\tag{L-103004.5}
\]

## Weighted consequence

Let `nu` be a nonnegative measure on source log-ratios with density bounded by `M` relative to Lebesgue measure. Then

\[
\boxed{
\int_0^{2\log2}
\left[
\int|W_\delta(u)|\,du
\right]d\nu(\delta)
\le
M(24\log2-16).
}
\tag{L-103004.6}
\]

Thus the common-mother endpoint current has a finite total analytic budget across all multiplicative separations. Any power loss in the order-inversion sector must come from concentration of the arithmetic source measure on log-ratio fibres, not from the endpoint kernel.

The theorem also shows that source pairs with ratio at least four do not interact at all in this Wronskian coordinate.