# L-100721 — Every double-owner cubic derivative is a compensated reciprocal-Möbius prefix coarea

Claim ID: `L-100721`  
Status: **PROVED EXACT ARITHMETIC COAREA IDENTITY**  
Created: 2026-08-21  
Depends on: `L-100720`  
RH status: **not assumed**

Use the notation of `L-100720`.  Let

\[
A_{\mathcal P}(x)
=\sum_{\substack{d\le x\\p\mid d\Rightarrow p\in\mathcal P}}
 {\mu(d)\over d},
\tag{L-100721.1}
\]

with `A_P(x)=0` for `x<1`.  Since `P` is finite, the sum is over the
squarefree divisors of `D_P`.

Define the endpoint-compensated rough prefix

\[
\boxed{
\begin{aligned}
\mathcal B_{p,q;\mathcal P}(x)
={}&A_{\mathcal P}(x)
-p^{-1/2}A_{\mathcal P}(x/p)\\
&-q^{-1/2}A_{\mathcal P}(x/q)
+(pq)^{-1/2}A_{\mathcal P}(x/(pq)).
\end{aligned}}
\tag{L-100721.2}
\]

## Hinge derivative

For `s>0`, expansion of the interior Euler product gives

\[
E_{\mathcal P}h_s(t)
=\sum_{d\mid D_{\mathcal P}}
 {\mu(d)\over\sqrt d}
 \left({t\over\sqrt d}-s\right)_+.
\]

At every nonactivation point,

\[
{d\over dt}E_{\mathcal P}h_s(t)
=A_{\mathcal P}((t/s)^2).
\tag{L-100721.3}
\]

The endpoint shifts contribute the chain-rule factors `p^-1/2` and
`q^-1/2`. Hence

\[
\boxed{
{d\over dt}
\Delta_p\Delta_qE_{\mathcal P}h_s(t)
=\mathcal B_{p,q;\mathcal P}((t/s)^2).
}
\tag{L-100721.4}
\]

Both sides have the same one-sided values at activation points, so the identity
also holds distributionally.

Integrating the hinge representation of `L-100720` yields

\[
\boxed{
H'_{p,q;\mathcal P}(t)
=384\int_0^1(1-s)
 \mathcal B_{p,q;\mathcal P}((t/s)^2)\,ds.
}
\tag{L-100721.5}
\]

After the change of variables `u=t/s`, this becomes the exact multiplicative
coarea formula

\[
\boxed{
H'_{p,q;\mathcal P}(t)
=384t\int_t^\infty
 \left(1-{t\over u}\right)
 \mathcal B_{p,q;\mathcal P}(u^2)
 {du\over u^2}.
}
\tag{L-100721.6}
\]

Thus the derivative of every physical double-owner interval is a positive
quadratic smoothing of one explicit compensated semigroup prefix.  No
component-row, Hall, renewal, or operator-norm object is hidden in this
identity.

## Exact full-activation limit

For `x>=pqD_P`,

\[
A_{\mathcal P}(x)
=A_{\mathcal P}(x/p)
=A_{\mathcal P}(x/q)
=A_{\mathcal P}(x/(pq))
=\prod_{\ell\in\mathcal P}(1-\ell^{-1}).
\]

Therefore

\[
\boxed{
\mathcal B_{p,q;\mathcal P}(x)
=(1-p^{-1/2})(1-q^{-1/2})
 \prod_{\ell\in\mathcal P}(1-\ell^{-1})>0
}
\tag{L-100721.7}
\]

on the complete deep range.  All possible adverse derivative variation is
confined to the finite product-activation collar.

## Conclusion-facing interpretation

The long mixed-collar problem may now be read in two equivalent ways:

```text
physical side:
  sign/variation of H_(p,q;P)(t);

arithmetic side:
  sign/Carleson packing of B_(p,q;P)(x).
```

The equivalence is exact at finite source level.  It does not assert that the
compensated prefix is nonnegative.
