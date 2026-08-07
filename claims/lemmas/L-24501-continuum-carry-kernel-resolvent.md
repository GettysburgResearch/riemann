# L-24501 — Exact continuum carry kernel and inverse-zeta resolvent

Claim ID: `L-24501`  
Title: The scaling limit of the carry matrix has an explicit Mellin–Laplace symbol, and its causal inverse is a concrete Möbius Riesz state with Abel mass eight  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-07  
Frozen review base: PR #241 at `3a227e7595e1fe9e38956048297aa97531c80e4e`  
Dependencies: elementary cell integration; the Euler product in `Re(s)>1`; no RH input  
Scope: exact scalar continuum algebra; no positivity or discrete-stability theorem

## 1. Continuum carry kernel

For real `t>=1`, define

\[
 b(t)
 =\frac{\lfloor t\rfloor\bigl(\lfloor t\rfloor+1-t\bigr)}{t}.
 \tag{L-24501.1}
\]

Thus, on the cell `n<=t<n+1`,

\[
 b(t)=\frac{n(n+1-t)}{t}.
 \tag{L-24501.2}
\]

The function is nonnegative, decreases from `1` to `0` on each open cell, and
has a unit-height reset at every integer. Put

\[
 \boxed{
 k(u)=e^{-u/2}b(e^u),\qquad u\ge0.}
 \tag{L-24501.3}
\]

This is the exact scale kernel obtained from the finite carry coefficient after
`n=Xe^{-v}`, `q=Xe^{-u}` and fixed `u-v`.

## 2. Exact Laplace transform

For `Re(s)>1/2`, put `p=s+5/2`. Then

\[
\begin{aligned}
 K(s)
 &: =\int_0^\infty e^{-su}k(u)\,du\\
 &=\int_1^\infty b(t)t^{-s-3/2}\,dt\\
 &=\sum_{n\ge1}n\int_n^{n+1}(n+1-t)t^{-p}\,dt.
 \tag{L-24501.4}
\end{aligned}
\]

The two elementary telescoping sums are

\[
 \sum_{n\ge1}n(n+1)
 \bigl[n^{1-p}-(n+1)^{1-p}\bigr]
 =2\zeta(p-2),
 \tag{L-24501.5}
\]

and

\[
 \sum_{n\ge1}n
 \bigl[n^{2-p}-(n+1)^{2-p}\bigr]
 =\zeta(p-2).
 \tag{L-24501.6}
\]

Consequently

\[
\boxed{
 K(s)
 =\zeta\!\left(s+\frac12\right)
  \frac{s-\frac12}
  {(s+\frac12)(s+\frac32)}.}
 \tag{L-24501.7}
\]

The equality is initially an absolutely convergent identity for
`Re(s)>1/2`. The integral on the left converges farther left, and equation
(L-24501.7) supplies its meromorphic continuation.

Two useful removable values are

\[
 \boxed{K(1/2)=1/2}
 \tag{L-24501.8}
\]

and

\[
 K(0)=-\frac23\zeta(1/2)>0.
 \tag{L-24501.9}
\]

The first follows from
`(s-1/2)zeta(s+1/2)->1`; the second is continuation of the convergent integral.

## 3. Causal inverse

Let `g` be the causal distribution whose Laplace transform is

\[
\boxed{
 G(s)
 =\frac1{s^2K(s)}
 =\frac{(s+\frac12)(s+\frac32)}
 {s^2(s-\frac12)\zeta(s+\frac12)}
 }
 \tag{L-24501.10}
\]

in `Re(s)>1/2`. Then

\[
\boxed{(k*g)(u)=u}
 \tag{L-24501.11}
\]

in causal distributions, because the Laplace transform of `u` is `1/s^2`.

The rational factor has the exact partial fraction expansion

\[
 \frac{(s+\frac12)(s+\frac32)}{s^2(s-\frac12)}
 =\frac8{s-\frac12}-\frac7s-\frac3{2s^2}.
 \tag{L-24501.12}
\]

Using

\[
 \frac1{\zeta(s+1/2)}
 =\sum_{n\ge1}\frac{\mu(n)}{n^{s+1/2}}
 \qquad(\operatorname{Re}s>1/2),
 \tag{L-24501.13}
\]

inverse Laplace transformation gives the explicit right-continuous function

\[
\boxed{
\begin{aligned}
 g(u)=\sum_{n\le e^u}\frac{\mu(n)}{\sqrt n}
 \bigg[
 8e^{(u-\log n)/2}
 -7
 -\frac32(u-\log n)
 \bigg].
\end{aligned}}
 \tag{L-24501.14}
\]

The sum is finite at every `u`. Formula (L-24501.14), rather than a formal
inverse operator, is the proof-facing continuum carry state.

## 4. Critical Abel mass

Equation (L-24501.10) has a removable value at `s=1/2`:

\[
\boxed{G(1/2)=8.}
 \tag{L-24501.15}
\]

Equivalently, the critical weighted mass is eight in the Abel sense:

\[
\boxed{
 \lim_{\sigma\downarrow1/2}
 \int_0^\infty e^{-\sigma u}g(u)\,du=8.}
 \tag{L-24501.16}
\]

No claim of unconditional absolute convergence at the boundary is made. Turning
the Abel value into a finite positive carry mass with a polylogarithmic boundary
error is the separate discrete-stability theorem `L-24503`.

## 5. Exact zero exposure

Every nontrivial zero `rho` of `zeta` produces a pole of `G` at

\[
 s=\rho-\frac12.
 \tag{L-24501.17}
\]

The rational numerator in (L-24501.10) is nonzero there, and no nontrivial zero
coincides with `s=0` or `s=1/2`. Multiplicity is preserved.

Thus the continuum carry resolvent carries the complete rightmost-zero
obstruction. Positivity, subexponential growth, or boundary-stable positive
discretization of `g` is not a routine renewal estimate: any such theorem must
exclude the off-line poles in (L-24501.17).

## 6. Review firewall

A review should separately verify:

1. the cell definition (L-24501.1);
2. both telescoping sums (L-24501.5)--(L-24501.6);
3. every half-shift in (L-24501.7);
4. the removable value `K(1/2)=1/2`;
5. the partial fractions (L-24501.12);
6. the finite Möbius formula (L-24501.14);
7. that no zeta-zero pole is canceled.

The exact regression `X-24501` checks items 1--6 at finite rational test points.
It does not certify any asymptotic carry theorem.

## 7. Proof boundary

Closed exactly in this lemma:

- the continuum carry kernel;
- its Laplace symbol;
- the causal inverse symbol;
- the explicit finite Möbius state;
- the critical Abel mass;
- the shifted-zero pole locations.

Open:

- positivity of the inverse state;
- finite greedy-to-continuum stability;
- a polylogarithmic boundary remainder;
- RH.

No priority claim is made for the kernel transform until a dedicated literature
search and independent review are complete.
