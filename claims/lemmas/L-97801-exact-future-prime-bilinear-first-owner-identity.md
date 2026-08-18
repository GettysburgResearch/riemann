# L-97801 — Exact future-prime bilinear identity with sharp two-row normalization

Claim ID: `L-97801`  
Status: **PROVED EXACT SOURCE/ACTIVATION IDENTITY AND EQUIVALENCE**  
Created: 2026-08-18  
Depends on: `L-97800`; the literal dictionaries of PR #579  
RH status: **unproved**

## 1. Factor the full large-prime Möbius source at a moving cutoff

Let

\[
 \mu_{>3}(n)=
 \begin{cases}
 \mu(n),&(n,6)=1,\\
 0,&(n,6)>1,
 \end{cases}
\]

and let `mu_>z` be `mu` on squarefree integers all of whose prime factors exceed `z`, and zero otherwise. Let `mu_(3,z]` be the corresponding finite Euler factor on primes `3<p<=z`. Unique prime factorization gives

\[
 \mu_{>3}=\mu_{>z}*\mu_{(3,z]}.
\tag{L-97801.1}
\]

Since `a_(j,z)=mu_(3,z]*q_j`, the full coefficient dictionary is

\[
 \boxed{a_{j,\infty}=\mu_{>z}*a_{j,z}.}
\tag{L-97801.2}
\]

Applying the literal Riesz observation and reindexing the finite active sum gives, for every real `X`,

\[
 \boxed{
 C_{j,\infty}(X)
 =\sum_m{\mu_{>z}(m)\over\sqrt m}
 C_{j,z}(X/m).
 }
\tag{L-97801.3}
\]

Every activation remains exactly `mk<=X`; no continuum approximation occurs.

## 2. Unique least-prime ownership

For every `m>1` in (L-97801.3), let `p=P^-(m)` and write `m=pr`. Then `P^-(r)>p` and `mu(m)=-mu(r)`. Hence

\[
 \boxed{
 C_{j,\infty}(X)=C_{j,z}(X)-\mathcal G_j(X;z),
 }
\tag{L-97801.4}
\]

where

\[
 \boxed{
 \mathcal G_j(X;z)=
 \sum_{p>z}{1\over\sqrt p}
 \sum_{\substack{r\ \mathrm{squarefree}\\P^-(r)>p}}
 {\mu(r)\over\sqrt r}
 C_{j,z}\!\left({X\over pr}\right).
 }
\tag{L-97801.5}
\]

The convention is that the inner term is zero when inactive and `P^-(1)=+infinity`. The outer prime is the unique least owner, so no source occurrence is duplicated. The same coefficient and activation are visible in both rows.

## 3. Sharp normalization

Take `z=z_*(X)` from `L-97800`. Both denominators below are strictly positive. Define

\[
 \boxed{
 \Gamma_{23}(X)=
 \max\left\{
 {\mathcal G_2(X;z_*)\over C_{2,z_*}(X)},
 {\mathcal G_3^\sharp(X;z_*)\over C_{3,z_*}^\sharp(X)}
 \right\}.
 }
\tag{L-97801.6}
\]

Then

\[
 \boxed{
 C_{2,\infty}(X)\ge0\ \text{and}\
 C_{3,\infty}^\sharp(X)\ge0
 \iff
 \Gamma_{23}(X)\le1.
 }
\tag{L-97801.7}
\]

The denominator is the actual positive truncated physical row, not unsigned mass, rough density, a Hall reserve, or a source-blind norm. The constant one is sharp: equality is precisely a zero of one full row.

## 4. Exact two-row dual

For `u=(u_2,u_3)>=0`, `u!=0`, put

\[
 \Gamma_u(X)=
 {u_2\mathcal G_2+u_3\mathcal G_3^\sharp
  \over
  u_2 C_{2,z_*}+u_3C_{3,z_*}^\sharp}.
\]

This is a weighted average of the component ratios. Therefore

\[
 \boxed{
 \sup_{u\in\mathbb R_+^2\setminus\{0\}}\Gamma_u(X)
 =\Gamma_{23}(X).
 }
\tag{L-97801.8}
\]

Thus the extremal duals are the literal row-two or row-three rays. No fixed positive scalar combination, including the `5:3` scalar, can replace both component inequalities.

## 5. The single remaining theorem

Define `FPCB23` by

\[
 \boxed{
 \Gamma_{23}(X)\le1
 \quad\text{for every sufficiently large real }X.
 }
\tag{L-97801.9}
\]

By (L-97801.7), `FPCB23` is equivalent to eventual `LPTRP_23` once the uniform truncated-row theorem is installed. It is one explicit growing-prime correlation, with one-use ownership, exact activations and sharp normalization. It remains open.
