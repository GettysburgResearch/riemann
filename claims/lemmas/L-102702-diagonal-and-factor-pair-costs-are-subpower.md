# L-102702 — Source diagonals and same-product factor-pair collapse are subpower

Claim ID: `L-102702`  
Status: **PROVED UNCONDITIONALLY**  
Created: 2026-08-22  
Depends on: `L-102700--L-102701`  
RH status: **not assumed**

For an ordinary prime, write

\[
(1-z)^{1/2}=\sum_{k\ge0}c_kz^k.
\]

Then

\[
c_0=1,\qquad c_1=-\frac12,
\]

and

\[
|c_k|\ll k^{-3/2}\qquad(k\ge1).
\]

Consequently

\[
\sum_{k\ge0}\frac{|c_k|^2}{p^k}
=
1+\frac1{4p}+O(p^{-2}).
\]

The second labelled \(67\) changes only one fixed local factor. Euler-product
comparison therefore gives

\[
\boxed{
\sum_{n\le Y}\frac{|\lambda(n)|^2}{n}
\ll
(\log(2Y))^{1/4}.
}
\tag{L-102702.1}
\]

The square lift satisfies

\[
\sum_n\frac{|\lambda^\square(n)|^2}{n}
=
\sum_m\frac{|\lambda(m)|^2}{m^2}
<\infty.
\]

Hence

\[
\boxed{
\sum_{n\le Y}\frac{|\lambda_\pm(n)|^2}{n}
\ll
(\log(2Y))^{1/4}.
}
\tag{L-102702.2}
\]

## Same-product factor pairs

Let

\[
\delta=\lambda_-*\lambda_+=\beta-\beta^\square.
\]

For each \(n\),

\[
|\delta(n)|^2
\le
\tau(n)
\sum_{de=n}
|\lambda_-(d)|^2|\lambda_+(e)|^2.
\]

Using the standard uniform divisor bound \(\tau(n)=n^{o(1)}\) and
(L-102702.2),

\[
\boxed{
\sum_{n\le Y}\frac{|\delta(n)|^2}{n}
=
Y^{o(1)}.
}
\tag{L-102702.3}
\]

Thus all of the following costs are subpower:

```text
labelled half-divisor source energy;
diagonal physical Gram terms;
factor-pair multiplicity for one integer product;
the equal-owner multiplicity already controlled in L-102604.
```

No estimate for distinct products is asserted.
