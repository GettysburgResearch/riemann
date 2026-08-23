# L-104531 — Modular theta source and strong associated-kernel exhaustion

Claim ID: `L-104531`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
RH status: **not assumed**

Let

\[
\vartheta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},
\qquad
\mathcal A(u)=e^{u/2}\vartheta(e^{2u}),
\qquad D={d\over du}.
\]

Jacobi inversion gives

\[
\boxed{\mathcal A(-u)=\mathcal A(u).}
\tag{L-104531.1}
\]

The classical Riemann Fourier kernel satisfies the exact differential identity

\[
\boxed{
\Phi(u)={1\over4}\left(D^2-{1\over4}\right)\mathcal A(u).
}
\tag{L-104531.2}
\]

Indeed the `n=0` theta term is annihilated, while for

\[
f_n(u)=e^{u/2}e^{-\pi n^2e^{2u}}
\]

one has

\[
\left(D^2-{1\over4}\right)f_n
=
2\left(2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2}\right)
 e^{-\pi n^2e^{2u}}.
\]

## Positive theta-orbit decomposition

For `v>=0` put

\[
\phi(v)=
\left(2\pi^2e^{9v/2}-3\pi e^{5v/2}\right)e^{-\pi e^{2v}}.
\]

Since `2 pi e^(2v)-3>0`, one has `phi(v)>0`.  For every real `u`,

\[
\boxed{
\Phi(u)=\sum_{n\ge1}n^{-1/2}\phi(|u|+\log n).
}
\tag{L-104531.3}
\]

Define

\[
g(u)=u^2\Phi(u),
\qquad
g_n(u)=u^2n^{-1/2}\phi(|u|+\log n).
\]

Then every `g_n` is even and nonnegative and

\[
\boxed{g=\sum_{n\ge1}g_n.}
\tag{L-104531.4}
\]

For every fixed integer `J>=0`, the series converges absolutely in

\[
L^1\big((1+|u|)^Jdu\big).
\tag{L-104531.5}
\]

This follows directly from the factor

\[
\exp[-\pi n^2e^{2|u|}]
\]

and permits termwise Fourier differentiation to every fixed order.

## Associated kernel and strong cutoff exhaustion

Put

\[
\mathcal K_2(x)=
\int_{\mathbb R}y^2g(x+y)g(x-y)\,dy
\tag{L-104531.6}
\]

and let `g^(N)=sum_(n<=N) g_n`, with associated kernel `K_2^(N)`.  Then for every fixed `J`,

\[
\boxed{
\|(1+|x|)^J(\mathcal K_2^{(N)}-\mathcal K_2)\|_{L^1(dx)}\to0.
}
\tag{L-104531.7}
\]

Consequently their Fourier transforms and every fixed number of derivatives converge uniformly on the real axis.

With the Fourier convention

\[
\widehat f(t)=\int_{\mathbb R}f(u)e^{itu}\,du,
\]

one has `widehat g(t)=-Xi''(t)` and the exact identity

\[
\boxed{
\Xi'''(t)^2-\Xi''(t)\Xi''''(t)
=4\widehat{\mathcal K_2}(2t).
}
\tag{L-104531.8}
\]

Thus the fixed-order reverse-Rolle sign is a single positive-definiteness question for the fully assembled modular source.  Equation (L-104531.7) supplies a strong finite-cutoff exhaustion; it does not permit taking signs before the complete theta-orbit sum.