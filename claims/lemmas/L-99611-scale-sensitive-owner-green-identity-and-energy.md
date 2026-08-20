# L-99611 — The scale-sensitive SHARP owner chain has an exact Green identity and logarithmic augmented energy

Claim ID: `L-99611`  
Status: **PROVED EXACT LIFTED IDENTITY AND ENERGY BOUND**  
Created: 2026-08-20  
Depends on: `L-99610`  
RH status: **not assumed**

Normalize the SHARP target by

\[
q(y)=\frac{T(y)}{\sqrt y}=4-\frac3{\sqrt y},
\qquad y\ge1.
\tag{L-99611.1}
\]

For fixed `x>=n`, run the owner chain of `L-99610` from `N_0=n` to `N_tau=1`
and put

\[
Y_t=\frac{x}{N_t},\qquad M_t=(-1)^tf_{67}(N_t).
\]

Then `M_t` is a bounded martingale and `Y_(t+1)=d_tY_t`.

## 1. Exact stopped Green identity

Discrete integration by parts gives

\[
M_\tau q(Y_\tau)-M_0q(Y_0)
=
\sum_{t<\tau}q(Y_t)(M_{t+1}-M_t)
+
\sum_{t<\tau}M_{t+1}[q(Y_{t+1})-q(Y_t)].
\]

The first sum has expectation zero.  Since `Y_tau=x` and optional stopping
gives `E M_tau=M_0=f_67(n)`, one obtains

\[
\boxed{
f_{67}(n)q(x/n)
=
f_{67}(n)q(x)
-
\mathbb E_n\sum_{t<\tau}
M_{t+1}[q(Y_{t+1})-q(Y_t)].
}
\tag{L-99611.2}
\]

The scale increment is explicit and nonnegative:

\[
\boxed{
q(yd)-q(y)
=
\frac3{\sqrt y}\left(1-\frac1{\sqrt d}\right)\ge0.
}
\tag{L-99611.3}
\]

It is strictly positive for every genuine owner.  Hence the lifted state
detects the squarefree deterministic-parity sector missed by `R-99610`.

## 2. Uniform augmented path energy

Define

\[
\mathcal V_x(n)=
\mathbb E_n\sum_{t<\tau}
\left[
q(Y_t)^2(M_{t+1}-M_t)^2
+
(q(Y_{t+1})-q(Y_t))^2
\right].
\tag{L-99611.4}
\]

Martingale orthogonality and `0<=q<=4` give

\[
\mathbb E\sum q(Y_t)^2(M_{t+1}-M_t)^2
\le16(1-f_{67}(n)^2)\le16.
\]

The scale increments are nonnegative and telescope to at most
`q(x)-q(x/n)<=3`; hence their squared sum is at most nine.  Therefore

\[
\boxed{\mathcal V_x(n)\le25.}
\tag{L-99611.5}
\]

Combining with (L-99610.12),

\[
\boxed{
\sum_{n\le x}\frac{g_{67}(n)}n\mathcal V_x(n)
\le
25(1-67^{-1})^{-2}(1+\log x).
}
\tag{L-99611.6}
\]

Thus the complete lifted owner energy is logarithmic, not power-sized.

## 3. Boundary representation

The normalized SHARP Harnack scalar is exactly

\[
\boxed{
\frac{\mathfrak H_{67}(x)}{\sqrt x}
=
\sum_{n\le x}\frac{g_{67}(n)}n
f_{67}(n)q(x/n).
}
\tag{L-99611.7}
\]

Equations (L-99611.2)--(L-99611.7) give a source-faithful, scale-sensitive
martingale representation of the sole open scalar in PR #653.
