# L-99820 — Native normalization of the factor-67 logarithmic box

Claim ID: `L-99820`  
Status: **PROVED EXACT SOURCE/OPERATOR IDENTITY**  
Created: 2026-08-20  
Depends on: PR #653 scalar; PR #658 `L-99703`  
RH status: **not assumed**

Put

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

and

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\]

Let

\[
(\mathcal S_{67}h)(X)=\int_{X/67}^{X}h(t)\frac{dt}{t}
\]

with zero extension below one. Define

\[
W(y)=\int_{\max(1,y/67)}^yT(v)\frac{dv}{v},
\qquad
\phi(y)=\frac{W(y)}{\sqrt y}.
\tag{L-99820.1}
\]

Finite Fubini gives

\[
(\mathcal S_{67}h)(X)
 =\sum_{n\le X}\frac{\beta(n)}{\sqrt n}W(X/n).
\]

Since `sqrt(X/n)=sqrt(X)/sqrt(n)`, division by `sqrt(X)` yields

\[
\boxed{
\frac{(\mathcal S_{67}h)(X)}{\sqrt X}
 =\sum_{n\le X}\frac{\beta(n)}{n}\phi(X/n).
}
\tag{L-99820.2}
\]

This fixes the native prime coefficient on the normalized potential.

## One-prime dictionary

Let `(U_pF)(y)=F(y/p)`. The unnormalized and normalized steps obey

\[
\boxed{
W(y)-p^{-1/2}W(y/p)
 =\sqrt y\,[\phi(y)-p^{-1}\phi(y/p)].
}
\tag{L-99820.3}
\]

Thus

```text
unnormalized kernel W:       I-p^(-1/2) U_p;
normalized kernel phi:       I-p^(-1)   U_p.
```

Using `p^(-1/2)` on `phi` changes the native coefficient.

## Logarithmic conjugation

Put `u=log y` and

\[
G(u)=e^u\phi(e^u),
\qquad G(u)=0\quad(u<0).
\]

For

\[
\mathcal E_p=I-p^{-1}U_p
\]

one has

\[
\boxed{
e^u(\mathcal E_p\phi)(e^u)
 =G(u)-G(u-\log p).
}
\tag{L-99820.4}
\]

Hence the complete normalized Euler source is conjugate to ordinary backward
finite differences of `G`:

\[
\boxed{
e^u\frac{(\mathcal S_{67}h)(e^u)}{e^{u/2}}
 =\sum_n\beta(n)G(u-\log n).
}
\tag{L-99820.5}
\]

Equation (L-99820.5) is a change of normalization, not a positivity theorem.
It is the required statement-to-use dictionary for every box/collar argument.
