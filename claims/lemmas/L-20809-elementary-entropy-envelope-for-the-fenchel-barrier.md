# L-20809 — Elementary entropy envelope for the Fenchel barrier

Claim ID: `L-20809`  
Title: The archimedean Fenchel barrier is an explicit entropy function plus a positive `O(P^-5)` correction  
Status: `PROPOSED — COMPLETE ANALYTIC ENCLOSURE`  
Authoring agent: `gpt56-03-u`  
Created: 2026-08-07  
Dependencies: `L-9503`; `T-20802`  
Scope: remove the implicit convex conjugate from the cofinal prime-prefix test  
Related counterexample candidates: none

## 1. Exact smooth series

Use

\[
 B={1\over2}\left(\psi(1/4)-\log\pi\right),
 \qquad
 C=\pi^2+8G,
 \tag{L-20809.1}
\]

where `G` is Catalan's constant.  For

\[
 y=e^{t/2}\ge\sqrt2,
 \tag{L-20809.2}
\]

the smooth term of `L-9503` is

\[
 \boxed{
 A(t)=4(y-2)+2B\log y+{C\over4}-R_0(y),
 }
 \tag{L-20809.3}
\]

with

\[
 R_0(y)=4\sum_{m\ge1}{y^{-(4m+1)}\over(4m+1)^2}>0.
 \tag{L-20809.4}
\]

Its derivative is

\[
 \boxed{
 p(y):=A'(t)=2y+B+R_1(y),
 }
 \tag{L-20809.5}
\]

where

\[
 R_1(y)=2\sum_{m\ge1}{y^{-(4m+1)}\over4m+1}>0.
 \tag{L-20809.6}
\]

The map `y -> p(y)` is strictly increasing on `[sqrt2,infinity)`.

## 2. Exact parametric conjugate

At `p=p(y)`, the constrained Fenchel optimizer is `t=2log y`, and

\[
 \boxed{
 A_+^*(p(y))
 =2(p(y)-B)\log y-4y+8-{C\over4}+R_0(y).
 }
 \tag{L-20809.7}
\]

This formula already gives a proof-producing evaluator requiring only positive
rapidly convergent series and no numerical Legendre transform.

## 3. Elementary entropy barrier

Define

\[
 \boxed{
 \mathcal H(p)
 =2(p-B)\left[
 \log\left({p-B\over2}\right)-1
 \right]
 +8-{C\over4}.
 }
 \tag{L-20809.8}
\]

Then, for every `y>=sqrt2`,

\[
 \boxed{
 0\le
 A_+^*(p(y))-\mathcal H(p(y))
 \le
 {4y^{-5}\over25(1-y^{-4})}.
 }
 \tag{L-20809.9}
\]

Thus the exact prime-prefix criterion of `T-20802` lies inside an elementary
interval of width `O(P^-5)`.

### Proof

Put

\[
 R=R_1(y),
 \qquad
 u={R\over2y},
 \qquad
 {p-B\over2}=y(1+u).
 \tag{L-20809.10}
\]

Subtracting (L-20809.8) from (L-20809.7) gives the exact identity

\[
 \boxed{
 A_+^*(p)-\mathcal H(p)
 =R_0(y)-4y\bigl[(1+u)\log(1+u)-u\bigr].
 }
 \tag{L-20809.11}
\]

For `u>=0`,

\[
 0\le(1+u)\log(1+u)-u\le{u^2\over2}.
 \tag{L-20809.12}
\]

The upper inequality follows by differentiating and using
`log(1+u)<=u`.  Hence

\[
 A_+^*(p)-\mathcal H(p)
 \ge R_0(y)-{R_1(y)^2\over2y}.
 \tag{L-20809.13}
\]

The positive series satisfy

\[
 R_0(y)\ge{4y^{-5}\over25},
 \tag{L-20809.14}
\]

and

\[
 R_1(y)
 \le {2y^{-5}\over5(1-y^{-4})}.
 \tag{L-20809.15}
\]

Therefore

\[
 {R_1(y)^2\over2y}
 \le {2y^{-11}\over25(1-y^{-4})^2}
 \le {4y^{-5}\over25}
 \tag{L-20809.16}
\]

for `y>=sqrt2`; the last inequality is equivalent to

\[
 2y^6(1-y^{-4})^2\ge1,
\]

whose left side is already `9` at `y=sqrt2` and increases thereafter.
This proves the lower bound in (L-20809.9).

The second term in (L-20809.11) is nonnegative, so

\[
 A_+^*(p)-\mathcal H(p)\le R_0(y).
\]

Finally

\[
 R_0(y)
 \le {4y^{-5}\over25(1-y^{-4})},
 \tag{L-20809.17}
\]

which proves the upper bound. QED.

## 4. Prime-moment criterion with a thin ambiguity band

For a prime-power prefix, let `P=P_j`, `Q=Q_j`, and let `y(P)` be the unique
solution of (L-20809.5).  Put

\[
 E(P)={4y(P)^{-5}\over25(1-y(P)^{-4})}.
 \tag{L-20809.18}
\]

Then:

\[
 \boxed{
 Q<\mathcal H(P)
 \quad\Longrightarrow\quad
 M_j<0
 \quad\Longrightarrow\quad
 \mathrm{RH\ is\ false},
 }
 \tag{L-20809.19}
\]

while

\[
 \boxed{
 Q\ge\mathcal H(P)+E(P)
 \quad\Longrightarrow\quad
 M_j\ge0.
 }
 \tag{L-20809.20}
\]

Only the interval

\[
 \mathcal H(P)\le Q<\mathcal H(P)+E(P)
 \tag{L-20809.21}
\]

requires evaluation of the exact positive series correction.  Since
`P-B=2y+O(y^-5)`, its width is `O(P^-5)`.

Hence, after the fixed initial gate, RH is equivalent to the cofinal
**prime-power entropy inequality**

\[
 \boxed{
 Q_j
 \ge
 2(P_j-B)\left[
 \log\left({P_j-B\over2}\right)-1
 \right]
 +8-{C\over4}
 +\Delta_j,
 }
 \tag{L-20809.22}
\]

where the exact correction satisfies

\[
 0\le\Delta_j\le E(P_j)=O(P_j^{-5}).
 \tag{L-20809.23}
\]

The leading two prime moments are

\[
 P_j=\sum_{q\le q_j}{\Lambda(q)\over\sqrt q},
 \qquad
 Q_j=\sum_{q\le q_j}{\Lambda(q)\log q\over\sqrt q}.
 \tag{L-20809.24}
\]

This removes all matrices, zero data, and implicit variational optimization
from the arithmetic target.

## 5. Asymptotic interpretation

The main term of `P_j` is `2sqrt(q_j)` and the main term of `Q_j` is
`2sqrt(q_j)(log q_j-2)`.  Equation (L-20809.22) matches both leading orders and
retains the complete constant-scale remainder on which RH depends.

A phase-blind prime-number-theorem error is still far too large: the theorem
has exposed the exact entropy-scale sign but has not proved it.  A genuine
completion must derive (L-20809.22) from arithmetic structure—such as an exact
positive convolution, a block transport theorem, or a strip-sensitive
factorization—not from a coarse estimate for `psi(x)-x`.

## 6. Proof boundary

- The series identities, conjugate formula, and envelope are exact.
- The envelope is uniform over the entire post-`log2` range.
- No cofinal lower bound for `Q_j-mathcal H(P_j)` is claimed.
- A successful proof of (L-20809.22) for every prefix would prove RH by
  `T-20802`.
