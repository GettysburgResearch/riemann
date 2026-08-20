# L-101101 — Exact quadratic–wavelet distributional bridge

## Definitions

Let

\[
 T(x)=(4\sqrt x-3)\mathbf 1_{x\ge1},\qquad
 \beta(n)=\mu(n)-\mathbf 1_{67\mid n}\mu(n/67).
\]

Use logarithmic distributions, write `D=X d/dX`, and define

\[
 h_\beta(X)=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}T(X/n),
\]

\[
 H_2(X)=\sum_{n\ge1}\frac{\beta(n)}{\sqrt n}T(X/n)^2.
\]

Let

\[
 C_2=16\frac{1-67^{-3/2}}{\zeta(3/2)},\qquad
 E_2(X)=C_2X\mathbf 1_{X\ge1}-H_2(X).
\]

The activation measure is

\[
 \mathcal A_\beta=
 \sum_{n\ge1}\frac{\beta(n)}{\sqrt n}\,\delta_{\log n}.
\]

For zero-extended functions put

\[
 (S_af)(X)=f(X/a),\quad
 P_2=(I-\sqrt2S_2)(I-S_2)^2,
\]

and

\[
 (Jf)(X)=\int_1^X f(t)\frac{dt}{t}.
\]

Finally define the compact beta-wavelet

\[
 G_\beta=JP_2h_\beta.
\]

## Exact bridge

As logarithmic distributions,

\[
 \boxed{(D-1)E_2=C_2\delta_0-\mathcal A_\beta-3h_\beta.}
\]

Consequently

\[
 \boxed{
 3G_\beta
 =C_2JP_2\delta_0
  -JP_2\mathcal A_\beta
  -JP_2(D-1)E_2.
 }
\]

The first term is a fixed calibration supported in `1<=X<=8`.  Thus the
continuous quadratic boundary and the discrete activation boundary are the
two exact inputs of one conclusion-bearing compact wavelet.

## Proof

Write `u=log X` and `t(u)=T(e^u)`.  The function `t^2` jumps from zero to one
at `u=0`.  For `u>0`,

\[
 \frac{d}{du}t(u)^2
 =4e^{u/2}t(u)=t(u)^2+3t(u).
\]

Therefore

\[
 (D-1)T^2=\delta_0+3T.
\]

Dilation by every `n`, multiplication by `beta(n)/sqrt(n)`, and finite
summation on compact `X`-ranges give

\[
 (D-1)H_2=\mathcal A_\beta+3h_\beta.
\]

Because `(D-1)(C_2e^u 1_{u>=0})=C_2delta_0`, subtraction proves the first
identity.  Applying the commuting linear operator `JP_2` proves the second.

## Mellin check and detector preservation

For `z=s+1/2`,

\[
 \widehat T(s)=\frac{s+3/2}{s(s-1/2)},
\]

and

\[
 \sum_{n\ge1}\frac{\beta(n)}{n^z}
 =\frac{1-67^{-z}}{\zeta(z)}.
\]

Hence

\[
 \boxed{
 \widehat G_\beta(s)=
 \frac{(1-67^{-(s+1/2)})(s+3/2)
 (1-\sqrt2\,2^{-s})(1-2^{-s})^2}
 {s^2(s-1/2)\zeta(s+1/2)}.
 }
\]

The finite factors have no zero at a translated zeta zero with
`0<Re(s)<1/2`.  Thus subpower logarithmic negative mass for `G_beta` feeds the
frozen Mellin–Landau consumer and implies RH.  The bridge itself does not
supply that estimate.
