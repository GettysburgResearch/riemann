# L-91329 — The Green primitive commutes exactly with multiplicative Dirichlet convolution

Claim ID: `L-91329`  
Status: **EXACT OPERATOR IDENTITY AND ORIENTATION THEOREM**  
Created: 2026-08-12  
Depends on: `L-91311/L-91312`  
RH status: **unproved**

## 1. Arithmetic convolution and Green primitive

For an arithmetic function \(a\) and a function \(F\) on \([1,\infty)\), put

\[
 (\mathcal T_aF)(x)
 =\sum_{n\le x}a(n)F(x/n),
 \tag{L-91329.1}
\]

and

\[
 (\mathcal JF)(x)
 =\int_1^xF(y)\frac{dy}{y}.
 \tag{L-91329.2}
\]

Every sum below is finite at fixed \(x\). Interchanging the finite sum and integral, then substituting \(y=nu\), gives

\[
 \begin{aligned}
 (\mathcal J\mathcal T_aF)(x)
 &=\sum_{n\le x}a(n)
   \int_n^xF(y/n)\frac{dy}{y}\\
 &=\sum_{n\le x}a(n)
   \int_1^{x/n}F(u)\frac{du}{u}\\
 &=(\mathcal T_a\mathcal JF)(x).
 \end{aligned}
 \tag{L-91329.3}
\]

Therefore

\[
 \boxed{
 \mathcal J\mathcal T_a
 =\mathcal T_a\mathcal J
 }
 \tag{L-91329.4}
\]

as an exact pointwise identity, with no convergence issue.

## 2. Application to Suzuki's kernel

Retain

\[
 c_\omega(n)=\frac{J_{2\omega}(n)}{n^\omega}>0,
 \qquad
 c_\omega*d_\omega=\varepsilon,
 \tag{L-91329.5}
\]

and define the free endpoint function

\[
 F_\omega(x)=g_\omega(1/x)
 \qquad(x\ge1).
 \tag{L-91329.6}
\]

`L-91311` gives

\[
 H_\omega(x):=xh_\omega(x)
 =\mathcal T_{c_\omega}F_\omega(x).
 \tag{L-91329.7}
\]

The Green primitive used in `L-91312` is

\[
 A_\omega(x)
 =\int_1^xh_\omega(y)dy
 =\mathcal JH_\omega(x).
 \tag{L-91329.8}
\]

Hence

\[
 \boxed{
 A_\omega
 =\mathcal T_{c_\omega}\mathcal JF_\omega,
 }
 \tag{L-91329.9}
\]

and exact deconvolution gives

\[
 \boxed{
 \mathcal T_{d_\omega}A_\omega
 =\mathcal JF_\omega.
 }
 \tag{L-91329.10}
\]

## 3. Mellin-domain form

Let

\[
 \gamma(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2),
 \tag{L-91329.11}
\]

\[
 C_\omega(s)=\frac{\zeta(s-\omega)}{\zeta(s+\omega)},
 \qquad
 G_\omega(s)=\frac{\gamma(s-\omega)}{\gamma(s+\omega)}.
 \tag{L-91329.12}
\]

In the initial common half-plane,

\[
 \mathcal M F_\omega=G_\omega,
 \qquad
 \mathcal M H_\omega=C_\omega G_\omega
 =\frac{\xi(s-\omega)}{\xi(s+\omega)},
 \tag{L-91329.13}
\]

and

\[
 \boxed{
 \mathcal M A_\omega(s)
 =\frac{C_\omega(s)G_\omega(s)}{s}.
 }
 \tag{L-91329.14}
\]

Equation (L-91329.10) is the physical-space form of multiplication by \(C_\omega^{-1}\).

## 4. Orientation consequence

The all-detail Julia corner is the **inverse** arithmetic channel. Applied to the interacting Green output, it returns the free archimedean endpoint primitive:

```text
interacting Suzuki Green vector
  -- all-detail Jordan inverse -->
free endpoint Green vector.
```

It does not, by itself, generate the interacting Hardy vector from the positive source. Any proposal assigning the all-detail inverse directly to the interacting output must also include the complete forward Jordan channel and its pole-zero cancellation. Without that extra entanglement the transfer orientation is wrong.
