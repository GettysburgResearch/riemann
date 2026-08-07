# L-15402 — Exact signed-jump representation of the odd localized Weil sector

Claim ID: `L-15402`  
Title: Odd parity turns the complete localized Weil form into a positive signed-edge jump form with explicit potential  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-07-31  
Dependencies: L-15401; Yoshida's odd-function sufficiency as summarized and rederived in Suzuki, arXiv:2606.09096  
Scope: ambient lower bounds for odd functions in the scaled localized form  
Related counterexample candidates: none

## Motivation

L-15401 leaves one negative odd polar channel. T-15401 controls it through one
Birman--Schwinger scalar. On the odd sector there is a stronger exact
reorganization: pass to the half interval and rewrite the polar rank one, every
cross-origin continuous jump, and every cross-origin prime jump as positive
**signed-edge** squares.

The result is one complete nonlocal Schrödinger form. A positive supersolution
gives an ambient lower floor directly, with no resolvent scalar, omitted-mode
packet, or discarded positive term.

## Half-interval notation

Let

\[
 I_+=(0,1),
 \qquad
 s_a(x)=\sinh(ax/2),
 \qquad
 S_a=\int_0^1s_a(y)\,dy
     =\frac2a\bigl(\cosh(a/2)-1\bigr).
\tag{L-15402.1}
\]

For `f` on `I_+`, let `w` be its odd extension:

\[
 w(x)=f(x),\quad x>0,
 \qquad
 w(-x)=-f(x).
\tag{L-15402.2}
\]

Then

\[
 \|w\|_{L^2(-1,1)}^2=2\|f\|_{L^2(0,1)}^2.
\tag{L-15402.3}
\]

Use `K_a`, `V_a`, `c_n`, and `\delta_n` from L-15401. For
`0<\delta\le2`, define

\[
 C_\delta=\bigl(\max(0,\delta-1),\min(1,\delta)\bigr).
\tag{L-15402.4}
\]

## Exact odd half-form

Define

\[
\boxed{
 W_a^{\rm odd}(x)=2V_a(x)-8aS_as_a(x).}
\tag{L-15402.5}
\]

For a half-interval function `f`, put

\[
\begin{aligned}
 \mathfrak h_a^{\rm odd}(f)={}&
 \int_0^1\int_0^1
 K_a(|x-y|)|f(x)-f(y)|^2\,dx\,dy\\
 &+\int_0^1\int_0^1
 K_a(x+y)|f(x)+f(y)|^2\,dx\,dy\\
 &+\sum_{n\le e^{2a}}c_n\Bigg[
 2\mathbf1_{\{\delta_n<1\}}
 \int_0^{1-\delta_n}|f(x+\delta_n)-f(x)|^2\,dx\\
 &\hspace{39mm}
 +\int_{C_{\delta_n}}|f(t)+f(\delta_n-t)|^2\,dt
 \Bigg]\\
 &+4a\int_0^1\int_0^1
 s_a(x)s_a(y)|f(x)-f(y)|^2\,dx\,dy\\
 &+\int_0^1W_a^{\rm odd}(x)|f(x)|^2\,dx.
\end{aligned}}
\tag{L-15402.6}
\]

Every double or translated term is a squared modulus with a nonnegative
coefficient. The sign `+` inside a cross-origin square records odd reflection;
it does not make the energy negative.

## Exact odd-sector identity

For every odd core function `w` and its half-interval representative `f`,

\[
\boxed{q_a(w)=\mathfrak h_a^{\rm odd}(f).}
\tag{L-15402.7}
\]

No polar resolvent and no discarded complement remain.

## Proof

### 1. Continuous jump quadrants

For odd `w`, split the continuous jump form from L-15401 into four sign
quadrants. The two same-sign quadrants together give

\[
 \int_0^1\int_0^1K_a(|x-y|)|f(x)-f(y)|^2\,dx\,dy.
\tag{L-15402.8}
\]

The two opposite-sign quadrants together give

\[
 \int_0^1\int_0^1K_a(x+y)|f(x)+f(y)|^2\,dx\,dy.
\tag{L-15402.9}
\]

These are exactly the first two lines of (L-15402.6).

### 2. Prime-shift jumps

Fix `\delta=\delta_n`. If `\delta<1`, the positive-positive and
negative-negative pieces of

\[
 c_n\int_{-1}^{1-\delta}|w(x+\delta)-w(x)|^2\,dx
\]

are equal and sum to

\[
 2c_n\int_0^{1-\delta}|f(x+\delta)-f(x)|^2\,dx.
\tag{L-15402.10}
\]

The cross-origin piece is

\[
 c_n\int_0^\delta|f(t)+f(\delta-t)|^2\,dt.
\tag{L-15402.11}
\]

If `1\le\delta\le2`, the complete translated interval crosses the origin and,
after `t=x+\delta`, equals

\[
 c_n\int_{\delta-1}^{1}|f(t)+f(\delta-t)|^2\,dt.
\tag{L-15402.12}
\]

Equations (L-15402.11)--(L-15402.12) are unified by the interval
`C_\delta` in (L-15402.4). This proves the prime part of (L-15402.6).

### 3. Polar channel

For odd `w`,

\[
 C_a(w)=0,
 \qquad
 S_a(w)=2\int_0^1s_a(x)f(x)\,dx.
\]

Therefore the polar contribution is

\[
 -2a|S_a(w)|^2
 =-8a\left|\int_0^1s_a(x)f(x)\,dx\right|^2.
\tag{L-15402.13}
\]

The exact rank-one ground-state identity

\[
\begin{aligned}
 -8a\left|\int s_af\right|^2
 ={}&4a\int_0^1\int_0^1
 s_a(x)s_a(y)|f(x)-f(y)|^2\,dx\,dy\\
 &-8aS_a\int_0^1s_a(x)|f(x)|^2\,dx
\end{aligned}
\tag{L-15402.14}
\]

follows by expansion. This gives the fourth line of (L-15402.6) and the second
term of (L-15402.5).

### 4. Local potential

Because `V_a` is even,

\[
 \int_{-1}^1V_a(x)|w(x)|^2\,dx
 =2\int_0^1V_a(x)|f(x)|^2\,dx.
\]

Combining this with (L-15402.8)--(L-15402.14) proves (L-15402.7). QED.

## Signed-edge ground-state identity

Let `J` be a symmetric nonnegative edge measure on a space `X`, and let
`\sigma(x,y)=\sigma(y,x)\in\{+1,-1\}`. Define

\[
 \mathfrak e_\sigma(f)=\frac12\int
 |f(x)-\sigma(x,y)f(y)|^2\,J(dx,dy)+\int W|f|^2.
\tag{L-15402.15}
\]

For every positive `\psi`, the elementary identity

\[
\begin{aligned}
 |u-\sigma v|^2={}&pq
 \left|\frac up-\sigma\frac vq\right|^2\\
 &+(p-q)\left(\frac{|u|^2}{p}-\frac{|v|^2}{q}\right)
\end{aligned}
\tag{L-15402.16}
\]

with `p=\psi(x)`, `q=\psi(y)` gives

\[
\boxed{
\begin{aligned}
 \mathfrak e_\sigma(f)={}&\frac12\int
 \psi(x)\psi(y)
 \left|\frac{f(x)}{\psi(x)}
 -\sigma(x,y)\frac{f(y)}{\psi(y)}\right|^2J(dx,dy)\\
 &+\int\left[W(x)+\frac1{\psi(x)}
 \int(\psi(x)-\psi(y))J_x(dy)
 \right]|f(x)|^2d\mu(x).
\end{aligned}}
\tag{L-15402.17}
\]

The local Barta residual is independent of the edge sign. The sign appears only
inside the nonnegative remainder.

## Signed-edge measure for the odd Weil form

Equation (L-15402.6) has the standard normalization

\[
 \frac12\int|f(x)-\sigma f(y)|^2J_a^{\rm odd}(dx,dy)
 +\int W_a^{\rm odd}|f|^2,
\tag{L-15402.18}
\]

where:

1. same-side continuous edges have density `2K_a(|x-y|)` and `\sigma=+1`;
2. cross-origin continuous edges have density `2K_a(x+y)` and `\sigma=-1`;
3. same-side prime atoms have ordered weight `2c_n` and `\sigma=+1`;
4. cross-origin prime atoms have ordered weight `2c_n` and `\sigma=-1`;
5. polar edges have density `8a s_a(x)s_a(y)` and `\sigma=+1`.

The ordered atomic conventions count each undirected prime edge twice; the
factor `1/2` in (L-15402.18) recovers exactly (L-15402.6).

## Exact odd Barta floor

For `\psi>0` on `(0,1)`, define

\[
 b_{a,\psi}^{\rm odd}(x)=
 W_a^{\rm odd}(x)+\frac1{\psi(x)}
 \int\bigl(\psi(x)-\psi(y)\bigr)
 J_{a,x}^{\rm odd}(dy).
\tag{L-15402.19}
\]

Then

\[
 m_a^{\rm odd}
 =\operatorname*{ess\,inf}_{x\in(0,1)}b_{a,\psi}^{\rm odd}(x)
\tag{L-15402.20}
\]

satisfies

\[
 \mathfrak h_a^{\rm odd}(f)\ge
 m_a^{\rm odd}\|f\|_{L^2(0,1)}^2.
\tag{L-15402.21}
\]

Consequently,

\[
\boxed{
 \frac{q_a(w)}{\|w\|_{L^2(-1,1)}^2}
 \ge\frac{m_a^{\rm odd}}2
 \quad\text{for every nonzero odd }w.}
\tag{L-15402.22}
\]

This is a complete ambient bound for the odd localized form.

## RH consequence

Yoshida proved that strict Weil positivity on all nonzero odd compactly
supported test functions implies RH. Thus either of the following would close
the positive programme:

1. `m_a^{\rm odd}\ge0` for every positive rational `a`, with support continuity
   filling all real supports;
2. an unbounded support sequence with cofinal lower bounds
   `m_{a_j}^{\rm odd}/2\ge-\varepsilon_j`, `\varepsilon_j\to0`, together with
   the odd localized support monotonicity argument analogous to T-14302.

The present lemma does not construct that cofinal supersolution family.

## Proof-producing schema

A certificate binds:

1. exact support and complete prime-power manifest;
2. a strictly positive rational spline `\psi`;
3. every continuous and atomic signed-edge channel in (L-15402.18);
4. a partition containing every spline knot and translated knot image;
5. directed cellwise lower enclosures of (L-15402.19);
6. one strict or approximate lower floor.

No finite eigensystem or ambient resolvent is part of the proof object.

## Gap audit

- Factors of two depend on the full-to-half norm and ordered-edge conventions;
  they require independent audit.
- A `+` square is represented by `\sigma=-1`; the local Barta term remains
  sign-independent only because (L-15402.16) is exact.
- The polar rank one must be rewritten exactly as in (L-15402.14); dropping it
  is invalid.
- The supersolution must be strictly positive on the complete open interval.
- A finite-node residual check does not prove the cellwise essential infimum.
- A finite set of positive supports is not RH.
