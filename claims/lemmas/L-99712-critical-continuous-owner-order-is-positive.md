# L-99712 — The exponential generating function of all owner orders becomes positive at one sharp continuous order

Claim ID: `L-99712`  
Status: **PROVED EXACT COEFFICIENT THEOREM**  
Created: 2026-08-20  
Depends on: PR #655 `R-99700`  
RH status: **not assumed**

For `u>0`, let

\[
\operatorname{id}^u(n)=n^u,
\qquad
J_u=\mu*\operatorname{id}^u.
\]

Thus

\[
J_u(n)=n^u\prod_{p\mid n}(1-p^{-u})>0
\qquad(n>1),
\tag{L-99712.1}
\]

and `J_u(1)=1`.  The exponential-generating identity

\[
J_u
=
\sum_{k\ge0}{u^k\over k!}
 \bigl(\mu*\ell^{*k}\bigr),
\qquad \ell(n)=\log n,
\tag{L-99712.2}
\]

shows that `J_u` sums every fixed logarithmic owner order refuted in
`R-99700`.

Put

\[
c_u=\beta*\operatorname{id}^u
=(\delta_1-\delta_{67})*J_u.
\tag{L-99712.3}
\]

Write `n=67^e m`, `(m,67)=1`.  Exact multiplicativity gives

\[
\boxed{
 c_u(67^e m)=
 \begin{cases}
 J_u(m),&e=0,\\
 (67^u-2)J_u(m),&e=1,\\
 67^{(e-2)u}(67^u-1)^2J_u(m),&e\ge2.
 \end{cases}}
\tag{L-99712.4}
\]

Consequently, with

\[
u_*={\log2\over\log67},
\tag{L-99712.5}
\]

one has the sharp coefficientwise criterion

\[
\boxed{
 c_u(n)\ge0\text{ for every }n
 \quad\Longleftrightarrow\quad
 u\ge u_*.
}
\tag{L-99712.6}
\]

At the critical order `67^u*=2`, the local 67-adic coefficients are

```text
1, 0, 1, 2, 4, 8, ...
```

and the local Euler factor is

\[
{(1-67^{-z})^2\over1-2\,67^{-z}}
=1+{67^{-2z}\over1-2\,67^{-z}}.
\tag{L-99712.7}
\]

Thus the failure of every fixed owner order is not the end of the positivity
programme: the complete exponential mixture crosses into the positive cone at
one explicit continuous order.

## Endpoint consequence

Define

\[
\mathcal F_u(x)
=
\sum_{n\le x}{c_u(n)\over\sqrt n}T(x/n).
\tag{L-99712.8}
\]

For `u>=u_*`, every summand is nonnegative, so

\[
\boxed{\mathcal F_u(x)\ge0\qquad(x\ge1).}
\tag{L-99712.9}
\]

Equivalently, finite divisor switching gives the positive multiplicative Riesz
completion

\[
\boxed{
\mathcal F_u(x)
=
\sum_{m\le x}m^{u-1/2}H_{67}^{\rm sharp}(x/m)
\ge0.
}
\tag{L-99712.10}
\]

This exact positive completion is a powerful structural check on the adaptive
phase programme.  The next refutation records why it cannot be fed directly to
Landau without removing a genuine positive-real pole.