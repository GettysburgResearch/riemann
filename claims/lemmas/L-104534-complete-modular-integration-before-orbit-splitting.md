# L-104534 — Complete modular integration before theta-orbit splitting

Claim ID: `L-104534`  
Status: **PROVED EXACT SCALAR REDUCTION**  
Created: 2026-08-23  
Depends on: `L-104531`  
RH status: **not assumed**

This theorem executes the modular attack in the order required by the mixed-
frequency firewalls: assemble the complete Jacobi source first, remove its
neutral carrier exactly, and only then integrate by parts.

## 1. Carrier-subtracted Jacobi mother

Put

\[
\mathcal A(u)=e^{u/2}\vartheta(e^{2u}),
\qquad
\mathcal B(u)=\mathcal A(u)-2\cosh(u/2),
\qquad
L=D^2-\frac14.
\]

Jacobi inversion makes `A` and `B` even.  Moreover `B` and all of its
derivatives decay exponentially, while

\[
L\mathcal B=L\mathcal A=4\Phi.
\]

Thus, with

\[
g(u)=u^2\Phi(u),
\]

one has the exact neutral-free source identity

\[
\boxed{
g(u)=\frac{u^2}{4}L\mathcal B(u).
}
\tag{L-104534.1}
\]

No nondecaying theta carrier enters an integration by parts.

## 2. Complete two-variable modular form

Use the coordinates

\[
u=x+y,
\qquad
v=x-y,
\]

and put

\[
\mathscr C(x,y)=\mathcal B(x+y)\mathcal B(x-y),
\qquad
P_x(y)=y^2(x^2-y^2)^2.
\]

The conclusion-facing associated kernel is

\[
\mathcal K_2(x)=\int_{\mathbb R}y^2g(x+y)g(x-y)\,dy.
\]

Since

\[
L_uL_v
=\frac1{16}
\left[
(\partial_x^2-\partial_y^2)^2
-2(\partial_x^2+\partial_y^2)+1
\right],
\]

one obtains

\[
\mathcal K_2(x)
=\frac1{256}\int_{\mathbb R}
P_x(y)
\left[
(\partial_x^2-\partial_y^2)^2
-2(\partial_x^2+\partial_y^2)+1
\right]
\mathscr C(x,y)\,dy.
\tag{L-104534.2}
\]

All `y`-boundary terms vanish.  Moving every `y` derivative onto the explicit
polynomial gives the coefficient-one scalar identity

\[
\boxed{
\begin{aligned}
256\mathcal K_2(x)=\int_{\mathbb R}\Big[&
P_x\,\partial_x^4\mathscr C
-2(P_x+P_x'')\,\partial_x^2\mathscr C\\
&+(P_x-2P_x''+P_x'''')\,\mathscr C
\Big](x,y)\,dy,
\end{aligned}
}
\tag{L-104534.3}
\]

where primes on `P_x` mean `y` derivatives and the `x` derivatives act only
on `C`. Explicitly,

\[
P_x=y^2(x^2-y^2)^2,
\]

\[
P_x''=2x^4-24x^2y^2+30y^4,
\qquad
P_x''''=-48x^2+360y^2.
\tag{L-104534.4}
\]

Equation (L-104534.3) is the complete modular scalar quartic. It contains no
orbitwise square roots, local PSD ports or omitted cross frequencies.

## 3. Exact variance representation

Let

\[
C_g(x)=\int_{\mathbb R}g(x+y)g(x-y)\,dy.
\]

When `C_g(x)>0`, define the probability measure

\[
d\mu_x(y)=C_g(x)^{-1}g(x+y)g(x-y)\,dy.
\]

It is even in `y`, so its mean is zero, and

\[
\boxed{
\mathcal K_2(x)=C_g(x)\operatorname{Var}_{\mu_x}(y).
}
\tag{L-104534.5}
\]

This proves pointwise positivity of the fully assembled source kernel in one
line.  The remaining problem is its positive definiteness as a function of
`x`, not positivity of its values.

## 4. An unconditional central positivity interval

Put

\[
\mu_{2j}=\int_{\mathbb R}u^{2j}g(u)\,du
\qquad(j=0,1,2).
\]

Strict Cauchy--Schwarz gives

\[
D:=\mu_0\mu_4-\mu_2^2>0.
\]

The Laguerre profile

\[
\mathcal L_2(t)
=\Xi'''(t)^2-\Xi''(t)\Xi''''(t)
=4\int_{\mathbb R}\mathcal K_2(x)\cos(2tx)\,dx
\]

satisfies, using `cos z >= 1-z^2/2`,

\[
\boxed{
\mathcal L_2(t)
\ge
\mu_0\mu_2
-\frac{t^2}{2}(\mu_0\mu_4-\mu_2^2).
}
\tag{L-104534.6}
\]

Indeed

\[
\mathcal L_2(0)=\mu_0\mu_2,
\qquad
16\int x^2\mathcal K_2(x)\,dx=D.
\]

Consequently

\[
\boxed{
\mathcal L_2(t)>0
\quad\text{whenever}\quad
|t|<
\tau_*:=\sqrt{\frac{2\mu_0\mu_2}{\mu_0\mu_4-\mu_2^2}}.
}
\tag{L-104534.7}
\]

The radius is expressed entirely in three positive source moments and is
therefore independently certifiable by the theta series. A high-precision
diagnostic gives `tau_* approximately 5.22375`; that decimal is discovery data,
not part of the analytic proof.

## 5. Scope

The modular integration route has now reached one exact scalar quartic and a
nontrivial central positivity interval.  The coefficients in (L-104534.3) are
not all nonnegative, so the identity is not itself a global Gram proof.  The
remaining scalar theorem is positive definiteness of `K_2`, equivalently
pointwise nonnegativity of its Fourier transform.