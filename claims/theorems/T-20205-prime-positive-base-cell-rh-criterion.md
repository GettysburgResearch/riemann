# T-20205 — Prime-positive compact base-cell criterion

Claim ID: `T-20205`  
Title: Uniform integer-dilation control on one interval below the first prime knot is equivalent to RH  
Status: `PROPOSED — COMPLETE LANDAU/COVERING ARGUMENT; COFINAL INEQUALITY OPEN`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20203`; the upper-envelope version of Landau's one-sign theorem  
Scope: a global scalar criterion with nonnegative prime coefficients  
Related counterexample candidates: none

## 1. Fixed base cell

Fix real numbers

\[
 0<a<b<\log2
\]

and put

\[
 I=[a,b].
\]

For every integer `r>=2`, use the dilation defect

\[
 \mathcal D_r(t)=r^2\Psi(t)-\Psi(rt).
\]

Under RH, `T-20203` gives

\[
 \mathcal D_r(t)\ge0
 \qquad(r\ge2,\ t\in I).
\tag{1}
\]

## 2. A symmetric Landau envelope

The lower-envelope argument in `T-20203` has the following upper-envelope
counterpart.

Suppose that for every `epsilon>0`,

\[
 \Psi(T)\le C_\epsilon(1+T)^{B_\epsilon}e^{\epsilon T}
\tag{2}
\]

eventually. Choose a positive polynomial `P_epsilon` and a compactly supported
continuous correction so that

\[
 H_\epsilon(T)=P_\epsilon(T)e^{\epsilon T}-\Psi(T)
\]

is nonnegative on the complete half-line. Its Laplace transform is the negative
of the screw transform plus a function holomorphic to the right of `epsilon`.
Landau's theorem forces the convergence abscissa to be at most `epsilon`, because
the meromorphic continuation has no singularity on the positive real Laplace
axis: `xi` has no positive real zero.

Letting `epsilon` tend to zero makes `xi'/xi` holomorphic in the complete right
half-plane after the standard coordinate change. Functional-equation symmetry
then gives RH. Therefore

\[
\boxed{
 \Psi(T)\le e^{o(T)}
 \quad\Longrightarrow\quad RH.}
\tag{3}
\]

Here `e^(o(T))` has the usual quantified meaning in (2); it is a one-sided upper
bound, not an absolute-value estimate.

## 3. Compact-cell covering

Assume that, for every `epsilon>0`,

\[
\boxed{
 \inf_{t\in I}\mathcal D_r(t)
 \ge-C_\epsilon e^{\epsilon r}}
\tag{4}
\]

for all sufficiently large integers `r`. Polynomial factors in `r` may be
included without changing the argument.

For every sufficiently large `T`, the interval

\[
 [T/b,T/a]
\]

contains an integer `r`. Put `t=T/r`; then `t in I`. Equation (4) gives

\[
 \Psi(T)
 \le r^2\Psi(t)+C_\epsilon e^{\epsilon r}.
\tag{5}
\]

Since `Psi` is continuous on the fixed compact interval `I`, its upper norm
there is finite. Moreover `r` is comparable to `T`. Thus, after replacing
`epsilon` by a smaller number in (4), equation (5) yields

\[
 \Psi(T)\le C'_\epsilon(1+T)^2e^{\epsilon T}.
\]

Equation (3) proves RH.

Combining this converse with (1), one obtains

\[
\boxed{
 RH
 \iff
 \mathcal D_r(t)\ge0
 \text{ for every }t\in I
 \text{ and every sufficiently large integer }r.}
\tag{6}
\]

The weaker exact growth criterion is

\[
\boxed{
 RH
 \iff
 \sup_{t\in I}\bigl(-\mathcal D_r(t)\bigr)_+
 =e^{o(r)}.}
\tag{7}
\]

## 4. Why the prime side is one-signed

Because `b<log2`, there is no prime power `q>=2` with `log q<=t` for any
`t in I`. Hence the small-scale ramp in `r^2 Psi(t)` is empty.

The entire prime contribution to `D_r(t)` is therefore

\[
\boxed{
 \sum_{q\le e^{rt}}{\Lambda(q)\over\sqrt q}
 (rt-\log q),}
\tag{8}
\]

and every coefficient is nonnegative.

Thus the criterion removes the negative-prime prefix completely—not by an
estimate, but by placing the fixed base cell before the first prime knot.
The complete arithmetic difficulty is the order-one cancellation between this
positive prime ramp and the explicit negative polar/gamma channels.

## 5. Exact remaining target

A full proof now follows from the compact-cell statement

\[
\boxed{
 \inf_{a\le t\le b}
 \left[r^2\Psi(t)-\Psi(rt)\right]
 \ge-e^{\epsilon r}}
\tag{9}
\]

for every `epsilon>0` and all sufficiently large integer `r`.

Unlike the square-cutoff formulation, every prime in (9) has a favorable sign.
This makes three tools natural:

1. an explicit lower bound for the positive prime ramp with the continuous main
   term canceled before estimation;
2. a Selberg/prime-pair positive square controlling the centered remainder;
3. a uniform interval argument in `t`, rather than phase selection at isolated
   translations.

## 6. Proof boundary

- The compact covering and one-sided Landau implication are exact.
- The absence of negative prime coefficients is exact for `b<log2`.
- No uniform lower bound (9) is proved.
- A finite range of `r` or a finite grid in `t` does not establish (6).
- The interval must have positive length; one fixed base point does not cover the
  complete half-line under integer dilation without an additional recurrence
  or phase theorem.
