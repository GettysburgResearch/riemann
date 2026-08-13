# O-91912 — The order-three scalar gate has a positive asymptotic tail

RH status: unproved.

Let
\[
F(x)=\frac{\xi'}{\xi}(1/2+x),
\qquad
Q(x)=x^2FF''-2x^2(F')^2+xFF'+F^2.
\]

On the safe half-line, Stirling asymptotics for the digamma term and the absolutely convergent Euler series give
\[
F(x)=\frac12\log\frac{x}{2\pi}+O(1/x),
\quad
F'(x)=\frac1{2x}+O(1/x^2),
\quad
F''(x)=-\frac1{2x^2}+O(1/x^3).
\]

Therefore
\[
\boxed{Q(x)=\frac14\log^2\frac{x}{2\pi}-\frac12+O(\log x/x).}
\]
In particular `Q(x)>0` for all sufficiently large `x`, unconditionally.

So the order-three reciprocal-concavity problem can in principle be reduced to an explicit safe-axis compact interval plus a directed analytic tail. No explicit threshold is claimed here.
