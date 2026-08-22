# L-104528 — Exact correlation kernel for the Xi'' Laguerre expression

Claim ID: `L-104528`  
Status: **PROVED EXACT**  
Created: 2026-08-23  
RH status: **not assumed**

Use the classical even positive Fourier kernel `Phi` normalized so that

\[
\Xi(t)=\int_{\mathbb R}\Phi(u)e^{itu}\,du.
\]

Set

\[
\varphi_2(u)=u^2\Phi(u)\ge0,
\qquad
G(t)=\int_{\mathbb R}\varphi_2(u)e^{itu}\,du=-\Xi''(t).
\]

The Laguerre expression is invariant under the sign change `G=-Xi''`:

\[
G'(t)^2-G(t)G''(t)
=\Xi'''(t)^2-\Xi''(t)\Xi''''(t)
=\mathcal L_2(t).
\]

Define the even nonnegative correlation kernel

\[
\boxed{
\mathcal K_2(x)
=\int_{\mathbb R}y^2
\varphi_2(x+y)\varphi_2(x-y)\,dy.
}
\tag{L-104528.1}
\]

A direct symmetrization gives

\[
\begin{aligned}
\mathcal L_2(t)
&=\frac12\iint_{\mathbb R^2}(u-v)^2
\varphi_2(u)\varphi_2(v)e^{it(u+v)}\,du\,dv\\
&=4\int_{\mathbb R}\mathcal K_2(x)e^{2itx}\,dx.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal L_2(t)=4\widehat{\mathcal K_2}(2t).
}
\tag{L-104528.2}
\]

The kernel `mathcal K_2` is even, nonnegative, smooth and rapidly decreasing.
Equation (L-104528.2) has three immediate unconditional consequences.

### Positive-definite Laguerre profile

Since `mathcal K_2>=0`, Bochner's theorem gives

\[
\boxed{
[\mathcal L_2(t_i-t_j)]_{i,j=1}^m\succeq0
\quad\text{for every finite real node set.}
}
\tag{L-104528.3}
\]

In particular,

\[
|\mathcal L_2(t)|\le\mathcal L_2(0).
\]

### Positive Gaussian averages

For every `sigma>0`,

\[
\boxed{
\int_{\mathbb R}\mathcal L_2(t)e^{-\sigma t^2}\,dt
=4\sqrt{\pi/\sigma}
\int_{\mathbb R}\mathcal K_2(x)e^{-x^2/\sigma}\,dx
>0.
}
\tag{L-104528.4}
\]

### Exact remaining kernel theorem

By Fourier duality,

\[
\boxed{
\mathrm{LAG2XI104550}
\iff
\mathcal K_2\text{ is positive definite.}
}
\tag{L-104528.5}
\]

Thus the fixed-order reverse-Rolle problem is reduced to one prescribed
positive-definiteness theorem for the explicit Xi-kernel correlation
`mathcal K_2`.  No derivative-zero percentage or parent zero count occurs in
that kernel statement.
