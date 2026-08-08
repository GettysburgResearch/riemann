# L-23012 — The parity comb is the minimal positive digital kernel

Claim ID: `L-23012`  
Title: The binary-digit kernel is a geometric causal smoothing of one positive alternating-interval comb whose Laplace transform is `eta(s)/s`  
Status: **PROPOSED EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-o`  
Created: 2026-08-07  
Dependencies: `L-23011`; elementary binary expansion; the Dirichlet eta identity  
Scope: the dyadic Euler-aligned shell

## 1. Positive parity comb

Define

\[
\boxed{
 P_2(t)=
 e^{-t/2}
 \mathbf1_{\{\lfloor e^t\rfloor\text{ is odd}\}}.}
\tag{L-23012.1}

Equivalently,

\[
P_2(t)=e^{-t/2}
\sum_{m\ge0}
\mathbf1_{[\log(2m+1),\,\log(2m+2))}(t).
\tag{L-23012.2}

Then

\[
P_2(t)\ge0,
\qquad
P_2\in L^1(\mathbb R)\cap L^2(\mathbb R).
\tag{L-23012.3}

At every integer boundary, the comb alternately turns on and off.  Therefore, in
distributions,

\[
\boxed{
\left(\partial_t+\frac12\right)P_2
=
\lambda_2,}
\tag{L-23012.4}

where

\[
\boxed{
\lambda_2
=
\sum_{n\ge1}{(-1)^{n+1}\over\sqrt n}
\delta_{\log n}.}
\tag{L-23012.5}

## 2. Eta transform

For `s=z+1/2` in the initial convergence half-plane,

\[
\begin{aligned}
\widehat P_2(z)
&=
\sum_{m\ge0}
\int_{\log(2m+1)}^{\log(2m+2)}e^{-st}\,dt\\
&={1\over s}
\sum_{m\ge0}
\left[(2m+1)^{-s}-(2m+2)^{-s}\right].
\end{aligned}
\]

Hence

\[
\boxed{
\widehat P_2(z)
={\eta(z+1/2)\over z+1/2},}
\tag{L-23012.6}

where

\[
\eta(s)=(1-2^{1-s})\zeta(s).
\]

The factor `1-2^(1-s)` has zeros only on `Re s=1`.  Therefore the zeros of the
positive comb transform in

\[
0<\operatorname{Re}z<\frac12
\]

are exactly the hypothetical off-line zeta zeros after the usual shift.

## 3. Exact bit-layer decomposition

Let `epsilon_j(n)` be the `j`-th binary digit of `n`.  Then

\[
s_2(n)=\sum_{j\ge0}\epsilon_j(n).
\tag{L-23012.7}

Moreover,

\[
\epsilon_j(\lfloor e^t\rfloor)
=
\mathbf1_{\{\lfloor e^{t-j\log2}\rfloor\text{ is odd}\}}.
\]

Using the definition of `S_2` in `L-23011`, one obtains pointwise

\[
\boxed{
S_2(t)
=
\sum_{j\ge0}2^{-j/2}
P_2(t-j\log2).}
\tag{L-23012.8}

The series is nonnegative and converges in both `L1` and `L2`.  In operator form,

\[
\boxed{
S_2
=
\left(I-2^{-1/2}\tau_{\log2}\right)^{-1}P_2.}
\tag{L-23012.9}

Conversely,

\[
\boxed{
P_2
=
S_2-2^{-1/2}\tau_{\log2}S_2.}
\tag{L-23012.10}

Thus the passage between the binary-digit kernel and the parity comb uses
mutually inverse causal `L1` filters.  It creates no new exponential growth
obstruction.

At transform level, (L-23012.9) is exactly

\[
{C_2(s)\over s}
={1\over1-2^{-s}}{\eta(s)\over s}.
\tag{L-23012.11}

## 4. Three-tap inversion of the dyadic shell source

Let `beta_2` be the Euler-aligned atomic source of `L-23010/L-23011`.
Combining (L-23012.10) with the two-tap equation `L-23011.17` gives

\[
\boxed{
P_2*\beta_2
=
 w_\infty
-{3\over\sqrt2}\tau_{\log2}w_\infty
+\tau_{2\log2}w_\infty.}
\tag{L-23012.12}

Indeed, if

\[
r_2=w_\infty-\sqrt2\tau_{\log2}w_\infty,
\]

then

\[
P_2*\beta_2
=
\left(I-2^{-1/2}\tau_{\log2}\right)r_2.
\]

The right-hand side of (L-23012.12) is elementary, causal, and exponentially
decaying.

## 5. Minimal positive-kernel formulation

After a fixed compact smoothing and the Sobolev factorization of `L-23010`, the
remaining dyadic shell theorem is equivalent to stable inversion of convolution
by the single positive kernel `P_2` on the actual source `beta_2`.

The kernel has no Möbius coefficient, no prime coefficient, no endpoint tail,
and no growing packet dictionary.  It is simply an exponentially weighted union
of the alternating unit intervals

\[
[1,2),[3,4),[5,6),\ldots
\]

in the original multiplicative variable.

A full proof may therefore be sought as a total-positivity, Wiener--Hopf,
canonical-system, or source-specific coercivity theorem for this parity comb.
The zero geometry of its transform shows that any generic zero-free theorem for
`P_2` is already RH-bearing.

## 6. Connection to the completed Xi kernel

Multiplication of `eta(s)` by the zero-free gamma and exponential factors in the
completed functional equation corresponds to convolution of `P_2` with an
explicit positive log-gamma kernel.  The remaining polynomial boundary operator
produces the classical Riemann Fourier kernel.

Thus the parity-comb inversion and the canonical Xi Mellin/total-positivity route
on PR #219 are two regularizations of the same minimal positive source.  The
known log-concavity theorem supplies only the first total-positivity shadow; the
all-order step remains open in either coordinate.

## 7. Proof boundary

Closed exactly:

- positivity and integrability of the parity comb;
- its alternating atomic derivative;
- the eta transform;
- the complete binary bit-layer factorization;
- the mutually inverse causal filters between `P_2` and `S_2`;
- the elementary three-tap convolution output.

Open:

- a critical coercivity or total-positivity theorem for `P_2` on the actual shell
  source;
- zero-free continuation of its transform in the open counterexample strip;
- RH.
