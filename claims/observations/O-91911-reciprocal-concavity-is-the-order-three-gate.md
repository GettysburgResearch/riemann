# O-91911 — Reciprocal concavity is the order-three gate

RH status: unproved.

Let
\[
F(x)=\Xi'(x)/\Xi(x),\qquad
k(t)=\frac{\sqrt t}{F(\sqrt t)},\quad t>1/4.
\]

Using `O-91910` and the first-factor sign in `L-91911`, the remaining three-node determinant condition is
\[
\boxed{k[t_1,t_2,t_3]\le0}
\]
for every `1/4<t1<t2<t3`. Equivalently, the order-three gate is concavity of `k`.

With `x=sqrt(t)`, direct differentiation gives
\[
k''(t)=-\frac{x^2FF''-2x^2(F')^2+xFF'+F^2}{4x^3F^3}.
\]
Thus the scalar target is
\[
\boxed{x^2FF''-2x^2(F')^2+xFF'+F^2\ge0\qquad(x>1/2).}
\]

This inequality is open. It does not prove all finite-order positivity and does not prove RH.
