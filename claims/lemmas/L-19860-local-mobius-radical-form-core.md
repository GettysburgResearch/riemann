# L-19860 — Exact local Möbius inversion places the localized form core in the radical range

Claim ID: `L-19860`  
Status: **PROVED BY FINITE MÖBIUS INVERSION**  
Authoring agent: `gpt56-pro-09-q`  
Created: 2026-08-07  
Dependencies: arithmetic map `E`; compact-BV radical theorem `L-16205`; local construction of `L-20301`  
Scope: closes the source-density gate in the continuous quotient route

## 1. Local target

Fix

\[
 0<a<b<\infty
\]

and let

\[
 h\in C_c^\infty((a,b)).
\]

Put

\[
 g(u)=u^{-1/2}h(u),
\]

extended by zero outside `[a,b]`.

Choose an integer `N` such that

\[
 \boxed{Na>b.}
\tag{L-19860.1}
\]

Let

\[
 P_N(s)=\sum_{n\le N}\frac{\mu(n)}{n^s},
 \qquad
 m_N=P_N(1)=\sum_{n\le N}\frac{\mu(n)}n.
\]

Choose

\[
 \psi\in C_c^\infty((0,a)),
 \qquad
 \int_0^\infty\psi(x)dx=1.
\]

## 2. Exact source

Define on the positive half-line

\[
 \boxed{
 f_h^+(x)
 =\sum_{n\le N}\mu(n)g(nx)
 -m_N\left(\int_0^\infty g(y)dy\right)\psi(x).}
\tag{L-19860.2}
\]

Extend `f_h^+` evenly to the real line and call the result `f_h`.

The source is compactly supported, smooth away from finitely many harmless support endpoints, of bounded variation, and vanishes near zero. Moreover,

\[
 f_h(0)=0,
\]

and

\[
 \int_0^\infty f_h^+(x)dx
 =\left(\sum_{n\le N}\frac{\mu(n)}n-m_N\right)
 \int_0^\infty g(y)dy
 =0.
\]

Thus

\[
 \boxed{f_h(0)=0,\qquad\int_\mathbb R f_h=0.}
\tag{L-19860.3}
\]

`L-16205` therefore places

\[
 J_h=E(f_h)
\]

in the exact weak global Weil radical.

## 3. Truncated divisor identity

Define

\[
 A_N(k)=\sum_{\substack{d\mid k\\d\le N}}\mu(d).
\]

Then

\[
 A_N(1)=1,
 \qquad
 A_N(k)=0\quad(2\le k\le N).
\tag{L-19860.4}
\]

Finite rearrangement gives

\[
 \sum_{m\ge1}\sum_{n\le N}\mu(n)g(nmu)
 =\sum_{k\ge1}A_N(k)g(ku).
\tag{L-19860.5}
\]

## 4. Exact reconstruction on the interval

Take `u in [a,b]`. The correction term involving `psi` vanishes because every `mu>=a`, while `psi` is supported below `a`.

For `k>N`,

\[
 ku\ge(N+1)a>b,
\]

so `g(ku)=0`. Equations (L-19860.4)--(L-19860.5) therefore give

\[
 \sum_{m\ge1}f_h(mu)=g(u).
\]

Multiplying by `u^(1/2)`,

\[
 \boxed{E(f_h)(u)=h(u)\qquad(a\le u\le b).}
\tag{L-19860.6}
\]

Every smooth compactly supported localized vector is the exact interior restriction of a global arithmetic-radical vector.

## 5. Form-core consequence

Take

\[
 a=\lambda^{-1},
 \qquad
 b=\lambda,
\]

with the support of `h` kept strictly inside the open interval. The standard initial domain for the localized convolution form is

\[
 C_c^\infty((\lambda^{-1},\lambda)).
\]

By definition, its closure in the shifted form norm is a form core for the lower-bounded localized Weil form. Equation (L-19860.6) shows that this complete core is contained in the exact interior arithmetic-radical range.

Consequently:

\[
 \boxed{
 \overline{P_\lambda E(\mathcal S_{\rm adm})}^{\,\|.\|_{Q_\lambda+c}}
 =\operatorname{Dom}Q_\lambda,}
\tag{L-19860.7}
\]

where `mathcal S_adm` includes the compact-BV sources (L-19860.2).

This is stronger than ordinary `L2` density and requires no non-zeta-cycle support assumption.

## 6. Closed radical relation

Apply `L-19855/L-19856` to the graph closure of the exact vectors

\[
 J_h=h+t_h.
\]

The resulting minimum-tail quotient form is densely defined on the complete localized form domain, and the exact radical-tail identity extends by graph closure.

Thus the continuous proposal `T-19811` has a concrete source form core; the remaining issue is the quantitative `d_4,d_6` hierarchy and relative zero-side scalarization, not source density.

## 7. Proof boundary

- The reconstruction is finite Möbius algebra and is exact.
- The source class is compact BV rather than Schwartz; `L-16205` is the regularity adapter.
- The theorem proves density and exact extension, not smallness of the constructed lower tail. The minimum-tail quotient may choose better extensions, including the prolate ones.
- No RH conclusion is claimed here.
