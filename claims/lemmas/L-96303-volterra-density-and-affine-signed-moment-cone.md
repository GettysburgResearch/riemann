# L-96303 — The universal Volterra density and the exact signed affine-cell moment cone

Claim ID: `L-96303`  
Status: **PROVED EXACT TRANSFORM AND CONE CHARACTERIZATION**  
Created: 2026-08-17  
Depends on: the Volterra source identity retained from PR #495; `L-96302`  
RH status: **not assumed**

## 1. Universal Volterra density

Define

\[
\boxed{
\mathscr L(x)
=
\sum_{d\le x}\frac{\mu(d)}{\sqrt d}
\left(2\sqrt{\frac xd}-1\right).
}
\tag{L-96303.1}
\]

Direct integration gives

\[
\boxed{
\int_1^\infty \mathscr L(x)x^{-s-1}\,dx
=
\frac{s+1/2}
{s(s-1/2)\zeta(s+1/2)}.
}
\tag{L-96303.2}
\]

This is exactly the scalar density multiplying the positive derivative fibre in the native Volterra disintegration.

Let `v(t)=mathcal V(e^t)` and `ell(t)=mathscr L(e^t)`. Comparing (L-96302.2) and (L-96303.2) yields the distributional identity

\[
\boxed{
(D-\tfrac12)\ell
=D(D+\tfrac12)v,
\qquad D=\frac d{dt}.
}
\tag{L-96303.3}
\]

Thus the reciprocal-row and affine–Volterra fronts are two differential coordinates of the same reciprocal-zeta state.

## 2. Signed affine-cell cone

On one endpoint cell `I=[a,b]` contained in `[n,n+1]`, the positive derivative row has the exact form

\[
p_s=A_n-s^{-1/2}B_n.
\]

Let `w` now be any integrable signed scalar weight and define

\[
M_I=\int_Iw(s)\,ds,
\qquad
U_I=\int_Iw(s)s^{-1/2}\,ds.
\]

Then

\[
\boxed{
\int_Iw(s)p_s\,ds=M_IA_n-U_IB_n.
}
\tag{L-96303.4}
\]

There exist `alpha,beta>=0` such that

\[
\int_Iw(s)p_s\,ds=\alpha p_a+\beta p_{b-}
\]

if and only if

\[
\boxed{
M_I\ge0,
\qquad
\frac{M_I}{\sqrt b}\le U_I\le\frac{M_I}{\sqrt a}.
}
\tag{L-96303.5}
\]

Indeed, `alpha+beta=M_I` and

\[
\alpha a^{-1/2}+\beta b^{-1/2}=U_I
\]

have a nonnegative solution exactly under (L-96303.5).

For the native Volterra source,

\[
w_X(s)=\frac{2\mathscr L(X/s)}s.
\]

Therefore pointwise positivity of `mathscr L` is sufficient but not necessary. The weaker cell-moment inequalities (L-96303.5) are the exact positivity target for the complete affine source.
