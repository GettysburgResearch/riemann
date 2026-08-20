# L-100500 — Exact Abel–Mertens frame for the minimal ratio-eight wavelet

Claim ID: `L-100500`
Status: **PROVED EXACT REAL-VARIABLE THEOREM**
Created: 2026-08-20
Frozen parent: PR #675 at `7b28224ba1b072d4ccd5b93ad37c0a64e7939740`
RH status: **not assumed**

Retain PR #674's ordinary-Möbius wavelet

\[
G_\mu(X)
=
\sum_{X/8\le n\le X}
\frac{\mu(n)}{\sqrt n}K_0(X/n),
\]

where

\[
K_0(y)=
\begin{cases}
8\sqrt y-8-3\log y,&1\le y<2,\\
-8\sqrt2\sqrt y+8(1+\sqrt2)+3(1+\sqrt2)\log y
-3(2+\sqrt2)\log2,&2\le y<4,\\
4\sqrt y-8\sqrt2+9\sqrt2\log2-3\sqrt2\log y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\]

Direct substitution gives

\[
K_0(1)=K_0(8)=0,
\]

and continuity at \(2\) and \(4\).

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\]

Define

\[
V(y)
=
y^{-1/2}\left(\frac12K_0(y)+yK_0'(y)\right).
\]

Then

\[
V(y)=
\begin{cases}
8-\dfrac{7+\frac32\log y}{\sqrt y},&1<y<2,\\[2mm]
-8\sqrt2+
\dfrac{
7(1+\sqrt2)+\frac32(1+\sqrt2)\log y
-\frac32(2+\sqrt2)\log2
}{\sqrt y},
&2<y<4,\\[3mm]
4+
\dfrac{
-7\sqrt2+\frac92\sqrt2\log2
-\frac32\sqrt2\log y
}{\sqrt y},
&4<y<8.
\end{cases}
\tag{L-100500.1}
\]

For

\[
w_X(t)=t^{-1/2}K_0(X/t),
\]

the endpoint terms in Abel summation vanish. Therefore

\[
\begin{aligned}
G_\mu(X)
&=
-\int_{X/8}^{X}M(t)w_X'(t)\,dt\\
&=
\boxed{
X^{-1/2}\int_1^8M(X/y)V(y)\,dy.
}
\tag{L-100500.2}
\end{aligned}
\]

This is an exact compact Mertens frame: no source completion, factor-67
registry, Hall flow, owner label, or positive collapse is present.

## Quantitative Littlewood dictionary

If for some \(\theta\ge0\)

\[
M(x)=O_\varepsilon(x^{1/2+\theta+\varepsilon}),
\]

then (L-100500.2) gives

\[
\boxed{
G_\mu(X)=O_\varepsilon(X^{\theta+\varepsilon}).
}
\tag{L-100500.3}
\]

Conversely, the Mellin transform

\[
\int_1^\infty G_\mu(X)X^{-s-1}\,dX
=
\frac{
(s+\frac32)(1-\sqrt2\,2^{-s})(1-2^{-s})^2
}{
s^2(s-\frac12)\zeta(s+\frac12)
}
\tag{L-100500.4}
\]

has no multiplier zero at \(s=\rho-\frac12\) when
\(\frac12<\Re\rho<1\). Hence

\[
G_\mu(X)=O_\varepsilon(X^{\theta+\varepsilon})
\quad(\forall\varepsilon>0)
\]

implies

\[
\Re\rho\le\frac12+\theta
\]

for every nontrivial zero. In particular,

\[
\boxed{
G_\mu(X)=X^{o(1)}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
\tag{L-100500.5}
\]

The same exponent dictionary holds for PR #675's cumulative Hardy energy.
