# L-99000 — Primitive prefix and exact logarithmic window

**Status:** proved exactly.  **RH is not assumed.**

Let \(\mu\) be the Möbius function and define
\[
q(1)=0,\quad q(2)=15,\quad q(4)=3,\quad q(n)=6\quad(n\notin\{1,2,4\}).
\]
Let \(a=q*\mu\). Then
\[
a(n)=6\mathbf 1_{n=1}-6\mu(n)
 +9\mathbf 1_{2\mid n}\mu(n/2)
 -3\mathbf 1_{4\mid n}\mu(n/4).
\]
For real \(X>0\), put
\[
R_X=\sum_{n\ge1}\frac{a(n)}{\sqrt n}\log(X/n)_+,
\qquad
\mathcal A_X=R_X-R_{X/4}.
\]
Define the primitive prefix
\[
C(t)=\sum_{n\le t}\frac{a(n)}{\sqrt n},
\qquad C(t)=0\quad(0<t<1).
\]
Then finite Fubini gives
\[
R_X=\int_1^X C(t)\,\frac{dt}{t},
\qquad
\boxed{\mathcal A_X=\int_{X/4}^{X}C(t)\,\frac{dt}{t}}.
\]
If
\[
B_{1/2}(t)=\sum_{n\le t}\frac{\mu(n)}{\sqrt n},
\qquad B_{1/2}(t)=0\quad(t<1),
\]
then
\[
\boxed{C(t)=6-\mathcal D(t)},
\qquad
\mathcal D(t)=6B_{1/2}(t)-\frac9{\sqrt2}B_{1/2}(t/2)
 +\frac32B_{1/2}(t/4).
\]
Consequently the stronger pointwise inequality \(C(t)\ge0\) implies
\(\mathcal A_X\ge0\) for every \(X\).

Every displayed identity is finite at each endpoint and uses no limiting
interchange.
