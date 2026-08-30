# L-104537 — Bilateral partition variance and horizontal-modulus curvature

Claim ID: `L-104537`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
Depends on: `L-104528`, `L-104531`  
RH status: **not assumed**

Let

\[
g(u)=u^2\Phi(u)\ge 0
\]

be the complete even Riemann source used in the fixed-order bridge, and define
its bilateral partition function

\[
\boxed{
\mathscr Z(z)=\int_{\mathbb R}g(u)e^{zu}\,du.
}
\tag{L-104537.1}
\]

The double-exponential theta decay makes `Z` entire.  Since `g` is real and
even,

\[
\mathscr Z(-z)=\mathscr Z(z),
\qquad
\overline{\mathscr Z(z)}=\mathscr Z(\overline z).
\tag{L-104537.2}
\]

On the imaginary axis,

\[
\boxed{
\mathscr Z(it)=\widehat g(t)=-\Xi''(t).
}
\tag{L-104537.3}
\]

## 1. The Laguerre profile is one analytic variance determinant

Put

\[
\mathscr D(z)
=\mathscr Z(z)\mathscr Z''(z)-\mathscr Z'(z)^2.
\tag{L-104537.4}
\]

Differentiating (L-104537.3) gives

\[
\boxed{
\mathscr D(it)
=\Xi'''(t)^2-\Xi''(t)\Xi''''(t)
=:\mathcal L_2(t).
}
\tag{L-104537.5}
\]

For real `x`, define the tilted probability

\[
d\mu_x(u)
={e^{xu}g(u)\over \mathscr Z(x)}\,du.
\]

Then

\[
\boxed{
\mathscr D(x)
=\mathscr Z(x)^2\operatorname{Var}_{\mu_x}(u)>0.
}
\tag{L-104537.6}
\]

Equivalently, for all real `x,h`, Cauchy--Schwarz gives the exact midpoint
log-convexity

\[
\boxed{
\mathscr Z(x+h)\mathscr Z(x-h)\ge \mathscr Z(x)^2.
}
\tag{L-104537.7}
\]

Thus the fixed-order problem is not the construction of a positive variance:
the variance is already positive on the complete real exponential family.  It
is the continuation of that variance sign from the real axis to selected
points of the imaginary axis.

## 2. Horizontal modulus identity

For real `t,x`, put

\[
\mathscr Q_t(x)
=\mathscr Z(x+it)\mathscr Z(x-it)
=|\mathscr Z(x+it)|^2.
\tag{L-104537.8}
\]

Evenness of `Z` makes `Q_t` even in `x`, and direct differentiation yields

\[
\boxed{
\mathscr Q_t''(0)=2\mathscr D(it)=2\mathcal L_2(t).
}
\tag{L-104537.9}
\]

Therefore

\[
\boxed{
\mathcal L_2(t)\ge0
\iff
x=0\text{ has nonnegative horizontal curvature for }
|\mathscr Z(x+it)|^2.
}
\tag{L-104537.10}
\]

Using (L-104537.3), this is

\[
\boxed{
\mathcal L_2(t)\ge0
\iff
\left.{d^2\over dh^2}
|\Xi''(t-ih)|^2\right|_{h=0}\ge0.
}
\tag{L-104537.11}
\]

At a real zero `c` of `Xi'''`, the first horizontal derivative already
vanishes.  Hence the Rolle orientation of that critical point is exactly a
local horizontal minimum-versus-maximum question for the off-line modulus of
`Xi''`.

## 3. Finite-shift form

Taylor expansion of the even function `Q_t` gives

\[
\boxed{
|\Xi''(t-ih)|^2-|\Xi''(t)|^2
=h^2\mathcal L_2(t)+O_t(h^4).
}
\tag{L-104537.12}
\]

If `Xi''(t) != 0`, the logarithmic form is

\[
\boxed{
{1\over h^2}
\log { |\Xi''(t-ih)|^2\over |\Xi''(t)|^2 }
\longrightarrow
{\mathcal L_2(t)\over\Xi''(t)^2}.
}
\tag{L-104537.13}
\]

This is the source-locked coordinate naturally compatible with Levinson's
horizontal-shift and mollifier machinery.  It is strictly weaker than proving
`L_2(t)>=0` at every real `t`: the fixed-order descent only needs it at the
real zeros of `Xi'''` counted by Conrey's theorem.
