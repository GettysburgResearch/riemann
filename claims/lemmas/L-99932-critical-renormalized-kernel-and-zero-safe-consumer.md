# L-99932 — The last Taylor remainder is one zero-safe critical scalar

Claim ID: `L-99932`  
Status: **PROVED EXACT REDUCTION; SIGN OPEN**  
Created: 2026-08-20  
Depends on: `L-99931` and the specialized Mellin–Landau theorem  
RH status: **unproved**

For an integer `m>=2`, the first Taylor remainder not covered by the strict
prime-mass contraction is

\[
 E_{m,m-1}(X)=
 \sum_{n\ge1}\frac{\beta(n)}{n^{(m+1)/2}}
 r_{m,m-1}\!\left(\sqrt{n/X}\right).
\]

It is absolutely convergent because `r_(m,m-1)(z)=O(z^(m-2))` as
`z->infinity`.  Define

\[
 \mathcal C_m(X)=4^mX^{m/2}E_{m,m-1}(X).
 \tag{L-99932.1}
\]

Then

\[
 \boxed{
 \mathcal C_m(X)=
 \sum_{n\ge1}\frac{\beta(n)}{\sqrt n}K_m(X/n),
 }
 \tag{L-99932.2}
\]

where the kernel is explicitly

\[
 \boxed{
 K_m(y)=4^m
 \begin{cases}
  (1-\sqrt y)^m+m\sqrt y-1,&0<y<1,\\
  m\sqrt y-1,&y\ge1.
 \end{cases}}
 \tag{L-99932.3}
\]

Bernoulli's inequality shows `K_m(y)>=0` for every `y>0`.  Positivity of the
kernel is not positivity of its native Möbius projection.

## Mellin transform

For `1/2<Re(s)<1`, two integrations by parts give

\[
 \boxed{
 \widehat K_m(s)=
 \frac{2\,4^m m!}
 {2s(2s-1)\prod_{j=2}^m(j-2s)}.
 }
 \tag{L-99932.4}
\]

Also

\[
 B(z)=\sum_{n\ge1}\frac{\beta(n)}{n^z}
 =\frac{1-67^{-z}}{\zeta(z)}.
\]

For `0<X<1`, every argument `X/n` lies below one, and therefore

\[
 \mathcal C_m(X)=4^m\sum_{j=2}^m(-1)^j\binom mj
 B\!\left(\frac{j+1}{2}\right)X^{j/2}.
 \tag{L-99932.5}
\]

Subtracting the exact compact interval `(0,1)` from the full multiplicative
convolution yields

\[
 \boxed{
 \begin{aligned}
 \int_1^\infty\mathcal C_m(X)X^{-s-1}\,dX
 ={}&\widehat K_m(s)
 \frac{1-67^{-(s+1/2)}}{\zeta(s+1/2)}\\
 &-4^m\sum_{j=2}^m
 \frac{(-1)^j\binom mj
 B((j+1)/2)}{j/2-s}.
 \end{aligned}}
 \tag{L-99932.6}
\]

Initially (L-99932.6) holds in the fundamental strip.  The second line cancels
all apparent positive-real poles `s=j/2`, `j>=2`.  The pole at `s=1/2` in
`K_hat` is cancelled by the zero of `1/zeta(s+1/2)` at `s=1/2`.
Consequently the continuation is holomorphic at every positive real `s`.

If `rho` is a zeta zero with `Re(rho)>1/2`, then `s=rho-1/2` is a genuine pole:
`K_hat` has no zeros, and `1-67^(-rho)` cannot vanish because
`|67^(-rho)|<1`.

It follows from the nonnegative-density Landau theorem that either condition

\[
 \mathcal C_m(X)\ge0\quad\hbox{eventually}
 \tag{L-99932.7}
\]

or the weaker condition

\[
 \int_1^X(\mathcal C_m(t))_-\frac{dt}{t}=X^{o(1)}
 \tag{L-99932.8}
\]

implies RH.

## The quadratic member

For `m=2`, the identity is especially transparent:

\[
 K_2(y)=16\begin{cases}y,&y<1,\\2\sqrt y-1,&y\ge1,
 \end{cases}
\]

and

\[
 \boxed{
 \mathcal C_2(X)=16B(3/2)X-G_2(X).
 }
 \tag{L-99932.9}
\]

`L-99930` proves `G_2>=0`; proving the opposite envelope
`G_2<=16B(3/2)X` is exactly the critical conclusion-producing direction.  It is
not obtained from supercritical positivity alone.