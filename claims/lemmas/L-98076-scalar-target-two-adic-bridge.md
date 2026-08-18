# L-98076 — Exact two-adic bridge between scalar prefix and target root

Claim ID: `L-98076`  
Status: **PROVED EXACT ALGEBRAIC IDENTITY; SIGN USE OPEN**  
RH status: **unproved**

Let
\[
A(t)=\sum_{n\le t}\frac{\mu(n)}n,
\]
let `H(t)` be the native target root, and let
\[
\mathcal D(t)=6B_{1/2}(t)-\frac9{\sqrt2}B_{1/2}(t/2)
+\frac32B_{1/2}(t/4).
\]

Using the exact Abel relation
\[
B_{1/2}(t)=\sqrt t\,A(t)-\frac12\int_1^t A(u)u^{-1/2}du
\]
together with the target identity
\[
H(t)=\sqrt t\,A(t)+\frac32\int_1^t A(u)u^{-1/2}du,
\]
elimination of the Volterra integrals gives
\[
\boxed{
\begin{aligned}
\mathcal D(t)
={}&\sqrt t[8A(t)-6A(t/2)+A(t/4)]\\
&-2H(t)+\frac3{\sqrt2}H(t/2)-\frac12H(t/4).
\end{aligned}}
\]

The reciprocal-Mertens coefficient polynomial is
\[
8-6U+U^2=(2-U)(4-U),\qquad Uf(t)=f(t/2).
\]

No sign consequence is claimed here; this is an exact bridge for future
two-adic/Volterra attacks.
