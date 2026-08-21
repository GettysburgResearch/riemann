# L-100712 — The critical cubic Green kernel has a positive compact exponential B-spline

Claim ID: `L-100712`  
Status: **PROVED EXACT ANALYTIC / DISTRIBUTIONAL THEOREM**  
Created: 2026-08-21  
Depends on: cubic kernel of `L-100001`  
RH status: **not assumed**

Let

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1.
\end{cases}
\tag{L-100712.1}
\]

Put `u=log y`, `h=log 2`, and

\[
\psi(u)=\Psi(e^u).
\]

Let `tau_h f(u)=f(u-h)`, corresponding to the scale shift
`S_2F(y)=F(y/2)`, and define

\[
\boxed{
\mathscr D_4
=(I-S_2)(I-\sqrt2S_2)(I-2S_2)(I-2\sqrt2S_2).
}
\tag{L-100712.2}
\]

Set

\[
K_{16}(y)=(\mathscr D_4\Psi)(y).
\tag{L-100712.3}
\]

## 1. The cubic kernel is a fourth-order Green function

On `u<0`,

\[
\psi(u)=192e^u-64e^{3u/2};
\]

on `u>0`,

\[
\psi(u)=192e^{u/2}-64.
\]

Thus, away from zero,

\[
D(D-\tfrac12)(D-1)(D-\tfrac32)\psi=0,
\qquad D={d\over du}.
\tag{L-100712.4}
\]

At `u=0`, the function and its first two derivatives are continuous:

\[
\psi(0)=128,
\qquad
\psi'(0)=96,
\qquad
\psi''(0)=48.
\]

The third derivative jumps from `-24` to `24`. Hence, as distributions,

\[
\boxed{
D(D-\tfrac12)(D-1)(D-\tfrac32)\psi
=48\delta_0.
}
\tag{L-100712.5}
\]

## 2. Positive Peano representation

For real `lambda` define

\[
A_\lambda=I-e^{\lambda h}\tau_h.
\]

The fundamental theorem of calculus gives the exact identity

\[
\boxed{
(A_\lambda f)(u)
=\int_0^h e^{\lambda t}(D-\lambda)f(u-t)\,dt.
}
\tag{L-100712.6}
\]

The four operators commute. Applying (L-100712.6) successively with

\[
\lambda\in\{0,\tfrac12,1,\tfrac32\}
\]

and using (L-100712.5) yields

\[
\boxed{
\begin{aligned}
K_{16}(e^u)
=48\int_{[0,h]^4}
&\exp\!\left(\tfrac12t_2+t_3+\tfrac32t_4\right)\\
&\times\delta\!\left(u-t_1-t_2-t_3-t_4\right)
\,dt_1dt_2dt_3dt_4.
\end{aligned}
}
\tag{L-100712.7}
\]

Every weight in this integral is positive. Therefore

\[
\boxed{
K_{16}(y)\ge0\quad(y>0),
\qquad
K_{16}(y)>0\quad(1<y<16).
}
\tag{L-100712.8}
\]

Moreover

\[
\boxed{
\operatorname{supp}K_{16}=[1,16].
}
\tag{L-100712.9}
\]

Thus the four real cubic carriers produce a literal positive compact
exponential B-spline, not merely a signed annihilator.

## 3. Mellin transform and zero-safe strip

For the bilateral Mellin transform

\[
\widehat F(s)=\int_0^\infty F(y)y^{-s-1}\,dy,
\]

(L-100712.5) gives

\[
\widehat\Psi(s)
=\frac{48}{s(s-\tfrac12)(s-1)(s-\tfrac32)}
\tag{L-100712.10}
\]

by meromorphic continuation. Hence

\[
\boxed{
\widehat K_{16}(s)
=48\prod_{\lambda\in\{0,1/2,1,3/2\}}
\frac{1-2^{\lambda-s}}{s-\lambda}.
}
\tag{L-100712.11}
\]

The apparent singularities at `s=lambda` are removable, with positive limiting
values. The nonremovable zeros lie on the four vertical lines

\[
\Re s\in\{0,\tfrac12,1,\tfrac32\}.
\]

In particular

\[
\boxed{
\widehat K_{16}(s)\ne0
\qquad(0<\Re s<\tfrac12).
}
\tag{L-100712.12}
\]

## 4. A new compact conclusion-complete scalar

Let

\[
\beta=(\varepsilon-\delta_{67})*\mu
\]

and define

\[
\boxed{
\mathcal B_{16}(X)
=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}
K_{16}(X/n).
}
\tag{L-100712.13}
\]

The support restricts the sum exactly to

\[
X/16\le n\le X.
\]

For `Re s>1/2`, finite/absolute Fubini gives

\[
\boxed{
\int_1^\infty\mathcal B_{16}(X)X^{-s-1}\,dX
=
\frac{1-67^{-(s+1/2)}}{\zeta(s+1/2)}
\widehat K_{16}(s).
}
\tag{L-100712.14}
\]

By (L-100712.12), no zeta zero with
`1/2<Re rho<1` is cancelled at `s=rho-1/2`. The positive-real carrier points
have already been removed by the four exact scale factors.

Therefore the frozen one-sided Mellin--Landau theorem gives

\[
\boxed{
\int_1^Y(\mathcal B_{16}(X))_-\frac{dX}{X}=Y^{o(1)}
\Longrightarrow RH.
}
\tag{L-100712.15}
\]

## 5. Scope

The kernel `K_16` is positive, compact, and zero-safe, but the source `beta` is
still signed. Pointwise positivity of `mathcal B_16` is **not** asserted.

The theorem nevertheless removes simultaneously:

```text
the deep critical half-order carrier;
the constant carrier;
the active linear carrier;
the active three-half carrier;
all noncompact kernel tails.
```

The remaining arithmetic is a fixed ratio-sixteen signed shell. It is an
alternative conclusion-facing target for the audited double-owner and balanced
homotopy coordinates.