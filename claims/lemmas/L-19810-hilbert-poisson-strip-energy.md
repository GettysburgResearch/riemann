# L-19810 — Hilbert–Poisson strip energy

Claim ID: `L-19810`  
Title: One vertical-line Hilbert-transform residual is a positive Poisson sum with a universal gap for every zero to the right  
Status: `PROPOSED — COMPLETE CANONICAL-FACTORIZATION PROOF; PRIME-SIDE ENERGY BOUND OPEN`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Dependencies: `T-19805`; boundary Hilbert-transform characterization of outer functions  
Scope: explicit nonnegative quadratic mechanism excluding every fixed off-line mode

## 1. Boundary logarithmic derivative

Retain the notation of `T-19805`. For a sufficiently large harmless damping
exponent `M`, put

\[
G_{\omega,M}(z)=(z+i)^{-M}
\bigl(s_\omega(z)-1\bigr)\zeta(s_\omega(z)),
\qquad
s_\omega(z)=\frac12+\omega-iz.
\tag{L-19810.1}
\]

On the real boundary, away from isolated zeros, define

\[
D_{\omega,M}(t)
={d\over dt}\log G_{\omega,M}(t).
\tag{L-19810.2}
\]

Explicitly,

\[
\boxed{
D_{\omega,M}(t)
=-i\left[
{1\over s_\omega(t)-1}
+{\zeta'\over\zeta}(s_\omega(t))
\right]
-{M\over t+i}.}
\tag{L-19810.3}
\]

Let `mathcal H` denote the real-line Hilbert transform with the convention that
for every outer function `O` in the upper half-plane,

\[
\operatorname{Im}{O'\over O}
=\mathcal H\!\left[
\operatorname{Re}{O'\over O}
\right]
\quad\text{a.e.}
\tag{L-19810.4}
\]

Define the **strip residual**

\[
\boxed{
\mathfrak p_\omega(t)
=\operatorname{Im}D_{\omega,M}(t)
-\mathcal H[\operatorname{Re}D_{\omega,M}](t).}
\tag{L-19810.5}
\]

Changing `M` changes `D_(omega,M)` only by an outer logarithmic derivative, so
`mathfrak p_omega` is independent of `M`.

## 2. Exact positive Poisson sum

Write the canonical factorization

\[
G_{\omega,M}=B_\omega O_{\omega,M}.
\]

The outer part cancels in (L-19810.5). If

\[
p_\rho=x_\rho+iy_\rho
=-\Im\rho+i(\Re\rho-\tfrac12-\omega)
\tag{L-19810.6}
\]

is a zero in the upper half-plane, then

\[
{d\over dt}\log b_{p_\rho}(t)
={2iy_\rho\over(t-x_\rho)^2+y_\rho^2}.
\tag{L-19810.7}
\]

Therefore, with multiplicity and with locally monotone convergence if the sum
is infinite,

\[
\boxed{
\mathfrak p_\omega(t)
=\sum_{\substack{\zeta(\rho)=0\\
\Re\rho>1/2+\omega}}
{2m_\rho(\Re\rho-1/2-\omega)
\over
(t+\Im\rho)^2+(\Re\rho-1/2-\omega)^2}
\ge0.}
\tag{L-19810.8}
\]

Thus one vertical-line Hilbert transform has removed every gamma, pole, outer,
and minimum-phase contribution and retained only a positive sum over zeros to
the right of that line.

For a finite right-zero set,

\[
\boxed{
{1\over2\pi}\int_{\mathbb R}\mathfrak p_\omega(t)\,dt
=N_\omega,}
\tag{L-19810.9}
\]

where `N_omega` is the total multiplicity to the right. For an infinite set the
integral is infinite.

## 3. Universal quadratic gap

For `y>0`, put

\[
P_y(t)={2y\over t^2+y^2}.
\]

A direct integral gives

\[
\boxed{
\int_{\mathbb R}P_y(t)^2\,dt={2\pi\over y}.}
\tag{L-19810.10}
\]

Every nontrivial zeta zero satisfies `Re rho<1`. Hence each ordinate in
(L-19810.8) has

\[
0<y_\rho<\frac12-\omega={1-2\omega\over2}.
\tag{L-19810.11}
\]

Define, allowing the value `+infinity`,

\[
\boxed{
\mathcal E_\omega
={1-2\omega\over4\pi}
\int_{\mathbb R}\mathfrak p_\omega(t)^2\,dt.}
\tag{L-19810.12}
\]

All summands in (L-19810.8) are nonnegative, so cross terms in the square are
nonnegative. If one zero of multiplicity `m` lies to the right, then

\[
\begin{aligned}
\mathcal E_\omega
&\ge {1-2\omega\over4\pi}
 m^2{2\pi\over y_\rho}\\
&={m^2(1-2\omega)\over2y_\rho}>m^2\ge1.
\end{aligned}
\tag{L-19810.13}
\]

Consequently the energy has the exact gap

\[
\boxed{
\mathcal E_\omega
=0
\quad\text{if }\zeta(s)\ne0\ (\Re s>1/2+\omega),}
\tag{L-19810.14}
\]

and

\[
\boxed{
\mathcal E_\omega>1
\quad\text{if even one zero lies to the right}.}
\tag{L-19810.15}
\]

A zero on the boundary is assigned infinite limiting energy. Thus

\[
\boxed{
\mathcal E_\omega<1
\quad\Longrightarrow\quad
\zeta(s)\ne0\quad(\Re s\ge1/2+\omega).}
\tag{L-19810.16}
\]

This is the requested explicit nonnegative quadratic mechanism. It is genuinely
strip-sensitive and cannot miss a fixed off-line mode.

## 4. Pointwise gap

At the center of any Poisson summand,

\[
\mathfrak p_\omega(-\Im\rho)
\ge {2m_\rho\over y_\rho}
>{4\over1-2\omega}.
\tag{L-19810.17}
\]

Hence the still simpler condition

\[
\boxed{
\|\mathfrak p_\omega\|_{L^\infty}
<{4\over1-2\omega}}
\tag{L-19810.18}
\]

also proves the same closed zero-free half-plane.

## 5. Relation to the projection defect

The function `mathfrak p_omega` is the boundary phase derivative of the inner
factor `B_omega`. The outer-normalized symbol of `T-19805` is

\[
\mathfrak a_\omega=\overline{B_\omega}^{\,2}.
\]

Therefore

\[
{d\over dt}\arg\mathfrak a_\omega(t)
=-2\mathfrak p_\omega(t).
\tag{L-19810.19}
\]

The projection-valued Hankel defect and the positive Poisson energy are the
global operator and local differential realizations of the same right-zero
packet.

## 6. Cofinal RH criterion

Let `omega_j downarrow0`. Any one of the cofinal estimates

\[
\boxed{
\mathcal E_{\omega_j}<1,}
\tag{L-19810.20}
\]

or

\[
\boxed{
\|\mathfrak p_{\omega_j}\|_\infty
<{4\over1-2\omega_j}}
\tag{L-19810.21}
\]

proves RH.

Unlike the beta-cell inequality, the target no longer asks a moving local
average to defeat a fixed exponential mode. A fixed off-line zero creates one
fixed Poisson bubble with a universal gap at every line immediately to its
left.

## 7. Proof-producing contour interface

The exact producer is the vertical-line logarithmic derivative
(L-19810.3). A finite certificate for one offset may contain:

1. directed values or cells for `Re D_(omega,M)` and `Im D_(omega,M)`;
2. a directed Hilbert-transform enclosure, including both tails;
3. an `L2` upper interval for the residual in (L-19810.5), or a pointwise upper
   interval;
4. the rational comparison with the universal threshold in
   (L-19810.16) or (L-19810.18).

No zero ordinates enter the definition of the certificate.

## 8. Smallest exact obstruction

The new mathematics converts the final RH sign into one normalized quadratic
line inequality:

\[
\boxed{
{1-2\omega\over4\pi}
\int_{\mathbb R}
\left|
\operatorname{Im}D_{\omega,M}
-\mathcal H\operatorname{Re}D_{\omega,M}
\right|^2dt<1.}
\tag{L-19810.22}
\]

Proving (L-19810.22) along `omega downarrow0` would complete RH. It has not yet
been derived from the prime-side Dirichlet series or the reversible Markov
Dirichlet form of `L-19809`.

This is now the smallest obstruction in this route: a single vertical-line
minimum-phase energy bound, with a universal gap and no compactness, tail,
packet, or phase-cancellation qualifier.

## 9. Proof boundary

- The Poisson representation and energy gap are exact consequences of canonical
  factorization.
- The Hilbert-transform convention is fixed by (L-19810.4), so no sign ambiguity
  remains.
- Boundary zeros are detected by divergent limiting energy rather than silently
  omitted.
- No unconditional upper bound below one has yet been proved; RH is not claimed.