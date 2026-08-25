# R-106450 — A positive artanh source bank does not make the physical companion inner

Claim ID: `R-106450`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-25  
Depends on: `L-106452`  
RH status: **not assumed**

The operator-monotone source theorem `L-106452` is a source-space Gram
statement.  It cannot be promoted directly to innerness of the ratio of two
physical observations.

Consider the positive atomic Fourier source

\[
F(z)=2+\cos z
 =2+{e^{iz}+e^{-iz}\over2}.
\]

Its Fourier measure is positive and even.  For every real `x`,

\[
F(x)\ge1,
\]

so `F` has no real zero.  It has nonreal zeros because `cos z=-2`.

Fix `0<lambda<1` and form the derivative companion denominator

\[
E_+(z)=F(z)+i\lambda F'(z)
 =2+\cos z-i\lambda\sin z.
\]

Put `w=e^{iz}`.  Multiplication by `2w` gives

\[
\boxed{
2wE_+(z)
 =(1-\lambda)w^2+4w+(1+\lambda).
}
\tag{R-106450.1}

The discriminant is

\[
16-4(1-\lambda^2)=12+4\lambda^2>0,
\]

so both roots are negative real. Their product is

\[
{1+\lambda\over1-\lambda}>1,
\]

while

\[
(1-\lambda)(-1)^2+4(-1)+(1+\lambda)=-2<0
\]

and the leading coefficient is positive. Therefore one root lies in
`(-1,0)` and the other lies in `(-infinity,-1)`. Since `|e^{iz}|=e^{-Im z}`,
`E_+` has one zero in each open half-plane in every periodic divisor cell.

Consequently

\[
\Theta_{\lambda,F}
 ={F-i\lambda F'\over F+i\lambda F'}
\]

is a genuine quotient of an inner and an anti-inner factor; it is not inner.
This remains true even though:

```text
the Fourier source is positive and even;
the common-carrier artanh factorization is exact;
the complete artanh Loewner kernel is positive;
F has no real zero.
```

The missing operation is the physical observation map.  A ratio of observed
positive source transforms is not the observation of the positive spectral
ratio.  Any use of `L-106452` in the Xi programme must therefore retain a
sampling, Pontryagin-space, signed-index, or source-to-companion realization
theorem.