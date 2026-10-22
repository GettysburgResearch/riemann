# PFR-T5 — Actual-Xi Gamma-resolvent abscissa

Status: **AUTHOR-PROVED EXACT ANALYTIC THEOREM; REVIEW PENDING; EXTERNAL NOVELTY UNESTABLISHED**
Scope: global actual `xi`; no height localization
Dependencies: PFR-T4, `N(T)=O(T log T)`, elementary Laplace theory
RH status: **unproved**

For `a>1/2`, integer `m>=2`, and centered zeros `lambda_rho=rho-1/2`, define

\[
R_{a,m}(t)=\sum_\rho\frac{e^{\lambda_\rho t}}{(a-\lambda_\rho)^m}.
\]

The sum is absolutely convergent.  It also has the zero-free source formula

\[
\begin{aligned}
R_{a,m}(t)
={}&\frac{e^{t/2}}{(a-1/2)^m}
+\frac{e^{-t/2}}{(a+1/2)^m}
-\sum_{k\ge0}\frac{e^{-(2k+1/2)t}}{(a+2k+1/2)^m}\\
&-\frac{e^{at}}{(m-1)!}
\sum_{n\ge2}\frac{\Lambda(n)}{n^{a+1/2}}(\log n-t)_+^{m-1}.
\end{aligned}
\]

Writing

\[
F(w)=\frac{\xi'}{\xi}\!\left(\frac12+w\right),
\]

the Laplace transform of `R_(a,m)` is also the safe Taylor remainder

\[
\frac{(-1)^m}{(z-a)^m}
\left[F(z)-\sum_{k<m}\frac{F^{(k)}(a)}{k!}(z-a)^k\right].
\]

If

\[
B_\xi=\sup_\rho|\Re(\rho-1/2)|,
\]

then

\[
B_\xi=
\inf\left\{\sigma:
\int_0^\infty e^{-2\sigma t}|R_{a,m}(t)|^2dt<\infty
\right\}
=
\limsup_{t\to\infty}\frac1t\log|R_{a,m}(t)|.
\]

Hence RH is equivalent to boundedness of this one entirely real prime-defined
function, and also to finiteness of its weighted energy for every
`sigma>0`.

The proof uses the nonremovable poles of

\[
\sum_\rho\frac{(a-\lambda_\rho)^{-m}}{z-\lambda_\rho}
\]

and the analyticity of the Laplace transform supplied by any stronger growth
or `L^2` bound.

Full proof: `XI_GAMMA_RESOLVENT_108260.md`.
