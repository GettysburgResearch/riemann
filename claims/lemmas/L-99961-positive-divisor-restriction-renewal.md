# L-99961 — Every divisor restriction of the duplicate-67 source is a positive dilation renewal of the base packet

Claim ID: `L-99961`  
Status: **PROVED EXACT DIRICHLET/PHYSICAL FACTORIZATION**  
Created: 2026-08-20  
RH status: **not assumed**

Let

\[
\beta=(\varepsilon-\delta_{67})*\mu,
\qquad
B(z)=\sum_{n\ge1}\frac{\beta(n)}{n^z}
=\frac{1-67^{-z}}{\zeta(z)}.
\]

For a positive integer `d`, define

\[
B_d(z)=\sum_{m\ge1}\frac{\beta(dm)}{m^z}.
\tag{L-99961.1}
\]

If `beta(d)=0`, then `B_d=0`. Otherwise write

\[
d=67^e d_0,
\qquad e\in\{0,1,2\},
\qquad d_0\text{ squarefree},
\qquad(67,d_0)=1.
\]

Then

\[
\boxed{B_d(z)=\beta(d)B(z)G_d(z),}
\tag{L-99961.2}
\]

where

\[
G_d(z)=
\prod_{p\mid d_0}(1-p^{-z})^{-1}
\,G_e(67^{-z}),
\tag{L-99961.3}
\]

and

\[
G_0(x)=1,
\qquad
G_1(x)=\frac{1-x/2}{(1-x)^2}
       =\sum_{k\ge0}\left(1+\frac k2\right)x^k,
\]

\[
G_2(x)=\frac1{(1-x)^2}
       =\sum_{k\ge0}(k+1)x^k.
\tag{L-99961.4}
\]

In particular every Dirichlet coefficient `g_d(r)` of `G_d` is nonnegative.

## Proof of the local factors

For `p!=67`, the local beta polynomial is `1-x`. If `p|d`, the sequence
`beta(p^(1+k))` is `-1,0,0,...`; dividing by `beta(p)=-1` leaves `1`, so the
relative factor is `(1-x)^(-1)`.

At `67`, the beta polynomial is `(1-x)^2`, with local coefficients
`1,-2,1`. For `e=1`, the shifted local sequence is `-2,1,0,...`, hence after
division by `beta(67)=-2` the polynomial is `1-x/2`; for `e=2` it is `1`.
This gives (L-99961.4).

## Physical packet identity

Let `psi` be any compactly supported measurable kernel and put

\[
f_\psi(y)=\sum_n\frac{\beta(n)}{\sqrt n}\psi(y/n).
\]

Then finite support and (L-99961.2) give

\[
\boxed{
\sum_{d\mid n}
\frac{\beta(n)}{\sqrt n}\psi(y/n)
=
\frac{\beta(d)}{\sqrt d}
\sum_{r\ge1}\frac{g_d(r)}{\sqrt r}
 f_\psi\!\left(\frac{y}{dr}\right).
}
\tag{L-99961.5}
\]

Thus every divisor tail in `DGOC99810` is a signed scalar `beta(d)` times a
**positive** dilation renewal of the same base packet. Squaring removes the
outer sign but not the scalar obstruction inside `f_psi`.

## Uniform Euler-factor bound

For every fixed `sigma>1/2` and every `epsilon>0`,

\[
\boxed{G_d(\sigma)\ll_{\sigma,\epsilon}d^\epsilon.}
\tag{L-99961.6}
\]

Indeed

\[
\log G_d(\sigma)
\ll_\sigma1+\sum_{p\mid d}p^{-\sigma},
\]

and the latter is `o(log d)` uniformly in `d`; the extremal set uses the
smallest primes. This is the exact estimate used in the RH converse of
`L-99960`.
