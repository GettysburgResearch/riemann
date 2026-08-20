# L-100708 — The centered cubic double-owner residual is exactly an inactive-collar layer cake

Claim ID: `L-100708`  
Status: **PROVED EXACT KERNEL/OWNER IDENTITY**  
Created: 2026-08-21  
Depends on: `L-100700`; `L-100702`; cubic kernel of `L-100001`  
RH status: **not assumed**

Let

\[
\Psi(y)=64
\begin{cases}
3y-y^{3/2},&0<y\le1,\\
3\sqrt y-1,&y\ge1,
\end{cases}
\]

be the critical cubic kernel. Put

\[
P(y)=192\sqrt y,
\qquad
C(y)=64(1-\sqrt y)_+^3.
\]

Then, for every `y>0`,

\[
\boxed{
\Psi(y)=P(y)-64+C(y).
}
\tag{L-100708.1}
\]

For `y<=1` this is the binomial identity

\[
192\sqrt y-64+64(1-\sqrt y)^3
=192y-64y^{3/2};
\]

for `y>=1`, `C(y)=0` and the identity is immediate.

## 1. Exact double-owner residual

Let

\[
E_{i+1:j-1}=\prod_{i<h<j}(I-r_hU_h),
\qquad
\Delta_h=I-U_h,
\]

and define

\[
H_{i,j}(X)=\Delta_i\Delta_jE_{i+1:j-1}\Psi(X).
\]

The carrier term of `L-100702` is

\[
M_{i,j}(X)=\Delta_i\Delta_jE_{i+1:j-1}P(X).
\]

Because every dilation fixes constants,

\[
\Delta_i\Delta_jE_{i+1:j-1}1=0.
\]

Consequently the centered residual is exactly

\[
\boxed{
\widetilde H_{i,j}(X)
:=H_{i,j}(X)-M_{i,j}(X)
=
\Delta_i\Delta_jE_{i+1:j-1}C(X).
}
\tag{L-100708.2}
\]

Thus the only signed part left after carrier subtraction is the activation
collar. No deep half-order mode or constant mode remains hidden in
`tilde H_(i,j)`.

## 2. Positive layer-cake representation

For `0<y<=1`,

\[
(1-\sqrt y)^3
=3\int_{\sqrt y}^{1}(1-v)^2\,dv.
\]

With zero contribution for `y>1`, this gives

\[
\boxed{
C(y)=192\int_0^1(1-v)^2
\mathbf1_{\{y\le v^2\}}\,dv.
}
\tag{L-100708.3}
\]

Every finite Euler/difference operator commutes with this ordinary integral.
Therefore

\[
\boxed{
\widetilde H_{i,j}(X)
=192\int_0^1(1-v)^2
\Delta_i\Delta_jE_{i+1:j-1}
\mathbf1_{\{X\le v^2\}}\,dv,
}
\tag{L-100708.4}
\]

where a dilation `U_d` changes the indicator to
`1_(X/d<=v^2)`. Equivalently, after expanding the interval Euler product, each
integrand is the exact signed threshold upper ideal determined by

\[
X\le v^2 n_A.
\]

This is a source-faithful coarea formula: the difficult residual is a positive
mixture of finite multiplicative threshold boundaries, not a generic smooth
kernel.

## 3. Mellin audit

For `Re(s)>0`,

\[
\boxed{
\widehat C(s)
=
\int_0^\infty C(y)y^{s-1}\,dy
=
\frac{192}{s(s+1)(2s+1)(2s+3)}.
}
\tag{L-100708.5}
\]

Indeed, after `t=sqrt(y)`,

\[
\widehat C(s)
=128\int_0^1(1-t)^3t^{2s-1}\,dt.
\]

The transform has no zero in `Re(s)>0`. Hence carrier subtraction has not
manufactured a zero-safe detector by itself; the threshold parity sum remains
the conclusion-producing arithmetic.

## 4. Consequence for the two-ended AND-gate

The row and column energies of `T-100610` can now be written entirely in terms
of the same threshold-upper-ideal family (L-100708.4), with different survival
weights. This removes the last kernel ambiguity from `FOCR100610` and
`LOCR100610`.

It does **not** prove either energy estimate. The finite counterexample on this
branch shows that completion by other rough primes need not preserve the
pointwise sign of a positive distinguished transition. Any valid estimate must
retain cancellation across threshold boundaries, rather than apply a
pointwise invariant cone.