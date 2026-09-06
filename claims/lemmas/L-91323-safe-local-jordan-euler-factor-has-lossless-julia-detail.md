# L-91323 — Every safe local Jordan Euler factor has an explicit lossless Julia detail

Claim ID: `L-91323`  
Status: **EXACT LOCAL LOSSLESS FACTORIZATION**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Universal two-parameter factor

Let

\[
0<\alpha<\beta<1,
\qquad
c_{\alpha,\beta}=\frac{1-\beta}{1-\alpha},
\]

and put

\[
\delta_{\alpha,\beta}^2
=
\frac{(\beta-\alpha)(1-\alpha\beta)}
     {(1-\alpha)^2}.
\tag{L-91323.1}
\]

Define on the unit disk

\[
m_{\alpha,\beta}(z)
=
c_{\alpha,\beta}\frac{1-\alpha z}{1-\beta z},
\tag{L-91323.2}
\]

\[
d_{\alpha,\beta}(z)
=
\delta_{\alpha,\beta}\frac{1-z}{1-\beta z}.
\tag{L-91323.3}
\]

Both functions are analytic in the closed disk except beyond the stable pole
\(z=\beta^{-1}>1\).

## 2. Exact Julia identity

For \(|z|=1\),

\[
\begin{aligned}
|1-\beta z|^2
-c_{\alpha,\beta}^2|1-\alpha z|^2
&=
\left(\beta-c_{\alpha,\beta}^2\alpha\right)|1-z|^2\\
&=
\delta_{\alpha,\beta}^2|1-z|^2.
\end{aligned}
\tag{L-91323.4}
\]

Therefore

\[
\boxed{
|m_{\alpha,\beta}(z)|^2
+
|d_{\alpha,\beta}(z)|^2
=1
\qquad(|z|=1).
}
\tag{L-91323.5}
\]

The column multiplier

\[
\boxed{
\mathcal J_{\alpha,\beta}(z)
=
\begin{pmatrix}
m_{\alpha,\beta}(z)\\
d_{\alpha,\beta}(z)
\end{pmatrix}
}
\tag{L-91323.6}
\]

is inner. Multiplication by this column is an isometry

\[
H^2(\mathbb D)
\longrightarrow
H^2(\mathbb D)\oplus H^2(\mathbb D).
\tag{L-91323.7}
\]

This is an explicit lossless Julia analysis node, not an abstract defect
square.

## 3. Prime specialization

For a prime \(p\), scale \(a>0\), and safe vertical line \(\sigma>0\), put

\[
\alpha_{p,a,\sigma}=p^{-(\sigma+2a)},
\qquad
\beta_{p,\sigma}=p^{-\sigma}.
\tag{L-91323.8}
\]

For \(z=e^{-it\log p}\),

\[
Q_{p,a}(\sigma+it)
=
\frac{1-\alpha_{p,a,\sigma}z}
     {1-\beta_{p,\sigma}z}
\tag{L-91323.9}
\]

is the local Euler factor of

\[
Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}.
\]

Its anchor-normalized form is exactly

\[
\boxed{
m_{p,a,\sigma}(z)
=
\frac{Q_{p,a}(\sigma+it)}
     {Q_{p,a}(\sigma)}
=
m_{\alpha_{p,a,\sigma},\beta_{p,\sigma}}(z).
}
\tag{L-91323.10}
\]

Hence each individual prime factor has a completely explicit positive-metric
lossless completion.

## 4. Exact geometric impulse

The detail has the convergent expansion

\[
\frac{1-z}{1-\beta z}
=
1-(1-\beta)\sum_{k\ge1}\beta^{k-1}z^k.
\tag{L-91323.11}
\]

Thus the auxiliary channel is one vacuum contact followed by one geometric
prime-power tail. It is the transfer-level counterpart of the compound-Poisson
first-chaos innovation.

## 5. Exact scale cocycle at one prime

The Euler cocycle gives

\[
Q_{p,2a}(s)
=
Q_{p,a}(s)Q_{p,a}(s+2a).
\tag{L-91323.12}
\]

The anchor normalizations multiply with coefficient one, so

\[
\boxed{
m_{p,2a,\sigma}(z)
=
m_{p,a,\sigma}(z)
m_{p,a,\sigma+2a}(z).
}
\tag{L-91323.13}
\]

Consequently

\[
\boxed{
\begin{pmatrix}
m_{p,2a,\sigma}\\
d_{p,a,\sigma}\\
m_{p,a,\sigma}d_{p,a,\sigma+2a}
\end{pmatrix}
}
\tag{L-91323.14}
\]

is an inner three-output column. This is the exact local two-section detail
ledger needed by the dyadic descent proposal.

## 6. Scope

Closed exactly:

```text
one prime, one safe line -> explicit lossless Julia node;
prime-power geometric detail;
coefficient-one two-section scale cascade.
```

Not closed:

```text
infinite-prime critical-boundary limit;
completed gamma/theta wave operator;
hard-range innerness;
RH.
```
