# L-98021 — Native factor-67 states are positive through the near-critical Dickman window

Claim ID: `L-98021`  
Status: **PROVED UNCONDITIONAL UNIFORM ASYMPTOTIC THEOREM**  
Created: 2026-08-18  
Depends on: `L-98020`; the repaired `P_61` annular base of PR #587/#599; a
classical upper-bound sieve for rough integers; de Bruijn's Dickman asymptotic  
RH status: **not assumed**

Let `b(Y)` be the complete `P_61` annular `5:3` scalar, zero-extended below its
activation range. The retained source theorem gives

\[
\boxed{
b(Y)=a_*\sqrt Y+e(Y),
\qquad a_*>0,
\qquad |e(Y)|\le E_*
}
\tag{L-98021.1}
\]

for every real `Y>0`, with absolute constants `a_*,E_*`.

For `2<=z<=Y`, define the literal native rough state

\[
\mathcal F(Y,z)=
\sum_{\substack{m\le Y\\m\ \mathrm{squarefree}\\P^-(m)\ge z}}
\frac{\mu(m)}{\sqrt m}\,b(Y/m),
\qquad
u=\frac{\log Y}{\log z}.
\tag{L-98021.2}
\]

Then, uniformly for `Y>=z^2` and `z` sufficiently large,

\[
\boxed{
\mathcal F(Y,z)
=a_*\sqrt Y\,\rho(u)
+O\!\left(\sqrt Y\frac{u}{\log z}\right).
}
\tag{L-98021.3}
\]

Consequently, for every fixed `epsilon>0`, uniformly in the range

\[
\boxed{
2\le u\le
(1-\epsilon)
\frac{\log\log Y}{\log\log\log Y},
}
\tag{L-98021.4}
\]

one has

\[
\boxed{\mathcal F(Y,z)>0}
\tag{L-98021.5}
\]

for all sufficiently large `Y`.

Equivalently, a negative native state must satisfy

\[
\boxed{
\frac{\log Y}{\log z}
\ge(1-o(1))
\frac{\log\log Y}{\log\log\log Y}.
}
\tag{L-98021.6}
\]

Thus the previously open phrase “subpower least-prime core” is narrowed to the
true critical harmonic corridor.

## 1. Homogeneous term

Substitution of (L-98021.1) into (L-98021.2) gives

\[
\mathcal F(Y,z)
=a_*\sqrt Y\,S(Y,z)+\mathcal E(Y,z),
\tag{L-98021.7}
\]

where `S(Y,z)` is (L-98020.1) and

\[
\mathcal E(Y,z)=
\sum_{m}
\frac{\mu(m)}{\sqrt m}e(Y/m).
\]

By `L-98020`,

\[
S(Y,z)=\rho(u)+O\!\left(\frac{u}{\log z}\right).
\tag{L-98021.8}
\]

## 2. Bounded source remainder

Let

\[
\Phi(t,z)=\#\{m\le t:P^-(m)\ge z\}.
\]

The classical dimension-one upper-bound sieve gives

\[
\Phi(t,z)\ll\frac{t}{\log z}
\tag{L-98021.9}
\]

uniformly in the required range. Partial summation therefore yields

\[
\sum_{m\le Y\atop P^-(m)\ge z}\frac1{\sqrt m}
\ll\frac{\sqrt Y}{\log z}.
\tag{L-98021.10}
\]

Since `e` is globally bounded,

\[
\boxed{
|\mathcal E(Y,z)|
\ll\frac{\sqrt Y}{\log z}.
}
\tag{L-98021.11}
\]

Equations (L-98021.7)--(L-98021.11) prove (L-98021.3).

## 3. Dickman lower scale

De Bruijn's asymptotic gives

\[
-\log\rho(u)
=u\left(
\log u+\log\log u-1
+O\!\left(\frac{\log\log u}{\log u}\right)
\right).
\tag{L-98021.12}
\]

Write

\[
L_1=\log Y,
\qquad L_2=\log\log Y,
\qquad L_3=\log\log\log Y.
\]

Under (L-98021.4), (L-98021.12) implies

\[
\rho(u)\ge L_1^{-1+\epsilon/2}
\tag{L-98021.13}
\]

for all sufficiently large `Y`. On the other hand,

\[
\frac{u}{\log z}=\frac{u^2}{L_1}=L_1^{-1+o(1)}.
\tag{L-98021.14}
\]

Therefore

\[
\rho(u)\bigg/\frac{u}{\log z}\longrightarrow\infty,
\]

uniformly in (L-98021.4). The positive main term in (L-98021.3) dominates its
entire source-faithful error and proves (L-98021.5).

## Consequence for the live graph

PR #602 proved positivity when `z>=Y^theta` for a fixed `theta>0`. The present
theorem permits the exponent to decay:

\[
\frac{\log z}{\log Y}
\ge
\frac{\log\log\log Y}{(1-\epsilon)\log\log Y}.
\]

This reaches the same order as the critical count depth identified by the
subcritical-depth no-go in PR #594/#598. It does not prove the remaining
critical corridor.
