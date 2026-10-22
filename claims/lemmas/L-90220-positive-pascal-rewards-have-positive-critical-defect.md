# L-90220 — Every positive uniform-Pascal reward has strictly positive square-root critical defect

Claim ID: `L-90220`  
Status: **PROPOSED COMPLETE EXACT GLOBAL NO-GO LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: exact uniform-Pascal hitting law `L-33109/L-90208`; elementary square-root sums  
Scope: every eventually constant nonnegative reward, with arbitrary finite or infinite boundary support; no arithmetic sign theorem and no RH conclusion

## 1. Uniform-Pascal boundary rewards

Use the strictly descending uniform-Pascal selected-child kernel

\[
 P_m(k)=\frac{2k}{m(m-1)},
 \qquad 1\le k<m.
 \tag{L-90220.1}
\]

Let `d(j)>=0`, `j>=2`, be a nonzero reward with finite Green mass, and let
`f` be its stopped potential,

\[
 f(m)=\mathbb E_m\sum_{0\le t<\tau_1}d(N_t).
 \tag{L-90220.2}
\]

Assume the affine normalization

\[
 f(m)\longrightarrow1.
 \tag{L-90220.3}
\]

The exact hitting law

\[
 \Pr_m(\tau_j<\infty)=\frac2{j+1}\qquad(m>j)
\]

gives the reward budget

\[
 \boxed{
 1=\sum_{j\ge2}\frac2{j+1}d(j).
 }
 \tag{L-90220.4}
\]

Put

\[
 F(m)=mf(m),
 \qquad
 a(m)=F(m)-F(m-1).
 \tag{L-90220.5}
\]

The increment Dirichlet transfer is the positive reward superposition

\[
 \boxed{
 \mathcal A_d(s)
 :=\sum_{m\ge1}\frac{a(m)}{m^s}
 =\sum_{j\ge2}d(j)\mathcal A_j(s),
 }
 \tag{L-90220.6}
\]

where the fixed-hit factor of `L-90208` is

\[
 \mathcal A_j(s)
 =j^{1-s}+(2-j)(j+1)^{-s}
 +\frac2{j+1}\zeta(s,j+2).
 \tag{L-90220.7}
\]

Because of (L-90220.4), the coefficient of `zeta(s)` in (L-90220.6) is one.
Write

\[
 \boxed{
 \mathcal A_d(s)=\zeta(s)-Q_d(s).
 }
 \tag{L-90220.8}
\]

The finite or absolutely convergent correction is

\[
 \boxed{
 Q_d(s)=\sum_{j\ge2}d(j)B_j(s),
 }
 \tag{L-90220.9}
\]

with

\[
 \boxed{
 B_j(s)
 =\frac2{j+1}\sum_{n=1}^{j+1}n^{-s}
  -j^{1-s}-(2-j)(j+1)^{-s}.
 }
 \tag{L-90220.10}
\]

## 2. Every elementary critical defect is positive

At the square-root exponent,

\[
 B_j\!\left(\frac12\right)
 =\frac2{j+1}\sum_{n=1}^{j+1}\frac1{\sqrt n}
  -\sqrt j+\frac{j-2}{\sqrt{j+1}}.
 \tag{L-90220.11}
\]

Put `N=j+1>=3`.  The integral lower bound for the decreasing function
`t^(-1/2)` is

\[
 \sum_{n=1}^{N}\frac1{\sqrt n}
 \ge\int_1^{N+1}t^{-1/2}\,dt
 =2\sqrt{N+1}-2.
 \tag{L-90220.12}
\]

Therefore

\[
 \boxed{
 B_j(1/2)
 \ge
 L_N:=
 \frac{4\sqrt{N+1}}{N}-\frac4N
 -\sqrt{N-1}+\frac{N-3}{\sqrt N}.
 }
 \tag{L-90220.13}
\]

For `N>=8`, use `sqrt(N+1)>sqrt(N)` and

\[
 \sqrt{N(N-1)}<N-\frac12
\]

to obtain

\[
\begin{aligned}
 L_N
 &>
 \frac{N+1}{\sqrt N}
 -\sqrt{N-1}-\frac4N\\
 &>
 \frac3{2\sqrt N}-\frac4N
 >0,
\end{aligned}
 \tag{L-90220.14}
\]

because `3sqrt(N)>8`.

The five remaining values are elementary radical inequalities:

\[
\begin{array}{c|c}
N&\text{positive lower certificate}\\ \hline
3&
1+\dfrac1{\sqrt3}>\sqrt2,\\[2mm]
4&
\sqrt5-\sqrt3>\dfrac12,\\[2mm]
5&
\dfrac{4\sqrt6}{5}+\dfrac2{\sqrt5}>\dfrac{14}{5},\\[3mm]
6&
\dfrac{2\sqrt7}{3}+\dfrac3{\sqrt6}>
\sqrt5+\dfrac23,\\[3mm]
7&
\dfrac{8\sqrt2}{7}+\dfrac4{\sqrt7}>
\sqrt6+\dfrac47.
\end{array}
 \tag{L-90220.15}
\]

For example, the last four follow respectively from

\[
 \sqrt5>\sqrt3+\frac12,
 \qquad
 \sqrt6>\frac{12}{5},\quad\sqrt5<\frac94,
\]

\[
 \sqrt7>\frac{21}{8},\quad
 \frac3{\sqrt6}>\frac65,\quad
 \sqrt5<\frac94,
\]

and

\[
 \sqrt2>\frac75,\quad
 \frac4{\sqrt7}>\frac32,\quad
 \sqrt6<\frac52.
\]

The `N=3` line follows after squaring the positive quantities, since
`sqrt(3)<3`.

Thus

\[
 \boxed{
 B_j(1/2)>0\qquad(j\ge2).
 }
 \tag{L-90220.16}
\]

No asymptotic estimate or zeta input enters.

## 3. Global critical-defect theorem

Equations (L-90220.9) and (L-90220.16) immediately give

\[
 \boxed{
 Q_d(1/2)>0
 }
 \tag{L-90220.17}
\]

for every nonzero nonnegative uniform-Pascal reward satisfying
(L-90220.3).

Equivalently:

> No positive uniform-Pascal boundary reward—regardless of how many boundary
> states it uses—can make its deterministic Euler correction vanish at the
> square-root critical exponent.

This strictly extends the finite dyadic double-neutral no-go of `L-90218`.
There the contradiction came from a derivative at the neutral root.  Here the
obstruction applies to arbitrary boundary support and directly at the
square-root mode.

## 4. Consequence for proof design

A source filter which removes the square-root critical mode must leave the
positive reward cone.  Therefore every such adapter must use at least one of:

1. signed Pascal reward;
2. more than one separately positive channel whose difference is taken only
   after source pairing;
3. a different Markov policy;
4. a nonlocal state not represented by an eventually constant Pascal
   potential.

The canonical `15:4` reward is positive and globally extremal by `L-90214`, but
its critical defect is necessarily strictly positive.  The factor
`(1-sqrt(2)t)` cannot be added while preserving coordinatewise reward
positivity.

This is a route theorem, not an RH obstruction: signed critical adapters remain
available and may still have a one-sided arithmetic pairing.

## 5. Proof boundary

Proved exactly:

- the positive-reward transfer decomposition;
- the explicit elementary defect `B_j(s)`;
- strict positivity of every `B_j(1/2)`;
- global impossibility of square-root cancellation inside the positive
  uniform-Pascal reward cone.

Not proved:

- sign of any signed critical adapter;
- the low-row or factor-64 payment theorem;
- RH.
