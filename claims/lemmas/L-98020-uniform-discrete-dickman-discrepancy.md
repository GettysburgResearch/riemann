# L-98020 — Uniform discrete Dickman discrepancy for rough Möbius weights

Claim ID: `L-98020`  
Status: **PROVED UNCONDITIONAL MEASURE-COMPARISON THEOREM**  
Created: 2026-08-18  
RH status: **not assumed**

Let `2 <= z <= Y`, put

\[
u=\frac{\log Y}{\log z},
\]

and define the literal rough Möbius harmonic sum

\[
S(Y,z)=
\sum_{\substack{m\le Y\\m\ \mathrm{squarefree}\\P^-(m)\ge z}}
\frac{\mu(m)}m.
\tag{L-98020.1}
\]

Let `rho` be the Dickman function, normalized by

\[
\rho(u)=1\quad(0\le u\le1),
\qquad
u\rho(u)=\int_{u-1}^{u}\rho(v)\,dv\quad(u>1).
\]

For `1 <= v <= u`, put

\[
\Delta(Y,z)=
\sup_{1\le v\le u}
\left|
\sum_{z\le p\le z^v}\frac1p-\log v
\right|.
\tag{L-98020.2}
\]

Then

\[
\boxed{
|S(Y,z)-\rho(u)|
\le
u e^{\Delta(Y,z)}
\left(
2\Delta(Y,z)+\frac1{2(z-1)}
\right).
}
\tag{L-98020.3}
\]

In particular, the classical prime-reciprocal Mertens theorem gives, uniformly
for `z` sufficiently large,

\[
\boxed{
S(Y,z)=\rho(u)+O\!\left(\frac{u}{\log z}\right).
}
\tag{L-98020.4}
\]

The implied constant is absolute.

## 1. Atomic and continuous prime measures

On `[1,u]`, define

\[
\nu_z=\sum_{z\le p\le Y}\frac1p\,
\delta_{\log p/\log z},
\qquad
\omega(dt)=\frac{dt}{t}.
\tag{L-98020.5}
\]

Their distribution functions differ by at most `Delta(Y,z)`. Their masses obey

\[
\omega([1,u])=\log u,
\qquad
\nu_z([1,u])\le\log u+\Delta(Y,z).
\tag{L-98020.6}
\]

For `k>=0`, define

\[
J_k(\eta;u)=\frac1{k!}
\eta^{*k}(({-\infty},u])
\]

for a positive measure `eta` supported on `[1,u]`, with `J_0=1`.
The continuous Volterra expansion of Dickman is

\[
\rho(u)=\sum_{k\ge0}(-1)^kJ_k(\omega;u).
\tag{L-98020.7}
\]

Only `k<=floor(u)` occur.

## 2. Convolution discrepancy

Let `eta_1,eta_2` be finite positive measures on `[1,u]`, each of mass at most
`M`, and assume the supremum norm of the difference of their distribution
functions is at most `delta`. Then

\[
\left|
\eta_1^{*k}(({-\infty},u])-
\eta_2^{*k}(({-\infty},u])
\right|
\le 2k\delta M^{k-1}.
\tag{L-98020.8}
\]

Indeed, telescope the difference of the two `k`-fold convolutions. Every term
has one signed factor `sigma=eta_1-eta_2` and a positive convolution factor of
mass at most `M^(k-1)`. Its cumulative kernel is monotone, so Stieltjes
integration by parts bounds the term by twice the distribution discrepancy
multiplied by that mass.

Taking

\[
M=\log u+\Delta(Y,z)
\]

and summing (L-98020.8) after division by `k!` gives

\[
\sum_{k\ge1}
|J_k(\nu_z;u)-J_k(\omega;u)|
\le2\Delta(Y,z)e^M.
\tag{L-98020.9}
\]

## 3. Repeated-prime correction

`J_k(nu_z;u)` counts ordered prime tuples and permits repeated primes. The
literal squarefree layer in (L-98020.1) uses distinct primes. A union bound over
a repeated coordinate pair gives

\[
\left|
J_k(\nu_z;u)-
\sum_{z\le p_1<\cdots<p_k\atop p_1\cdots p_k\le Y}
\frac1{p_1\cdots p_k}
\right|
\le
\frac1{2(k-2)!}
\left(\sum_{p\ge z}\frac1{p^2}\right)M^{k-2}.
\tag{L-98020.10}
\]

Summing over `k>=2` yields

\[
\frac12e^M\sum_{p\ge z}\frac1{p^2}
\le\frac{e^M}{2(z-1)}.
\tag{L-98020.11}
\]

Combining (L-98020.7), (L-98020.9), and (L-98020.11), and using
`e^M<=u e^Delta`, proves (L-98020.3).

## 4. Prime-reciprocal input

The prime number theorem implies

\[
\sum_{p\le x}\frac1p
=\log\log x+B_1+O\!\left(\frac1{\log x}\right).
\]

Taking a difference at `x=z^v` and `x=z`, uniformly for `1<=v<=u`, gives

\[
\Delta(Y,z)\ll\frac1{\log z}.
\]

Substitution in (L-98020.3) proves (L-98020.4).

## Scope

This theorem is an absolute comparison between the discrete rough-prime
activation simplex and the continuous Dickman simplex. It does not by itself
control the bounded nonhomogeneous remainder of the `P_61` annular base. That
source term is handled separately in `L-98021`.
