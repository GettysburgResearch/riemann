# L-15438 — Pointwise small-shift local limit on the natural scale

Claim ID: `L-15438`  
Title: The rescaled Jordan measure converges to `delta_0 + Lebesgue`, the rescaled beta kernel converges to the exponential density, and their convolution gives `Y_s(lambda/s) -> e^{-lambda}` locally uniformly for `lambda>0`  
Status: `PROPOSED — COMPLETE POSITIVE-MEASURE LOCAL-LIMIT ARGUMENT`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15434`, `L-15435`, `L-15437`; continuity of Laplace transforms for positive locally finite measures  
Scope: `s downarrow0` with `lambda=st` in compact subsets of `(0,infinity)`  
Related counterexample candidates: none

## 1. The rescaled arithmetic measure

Define the positive locally finite measure

\[
\boxed{
\mu_s
=\sum_{n\ge1}{F_s(n)\over n}
 \delta_{s\log n}.}
\tag{L-15438.1}
\]

For `r>0`,

\[
\begin{aligned}
\int_0^\infty e^{-r\lambda}d\mu_s(\lambda)
&=\sum_{n\ge1}{F_s(n)\over n^{1+sr}}\\
&={\zeta(1+sr)\over\zeta(1+s(1+r))}.
\end{aligned}
\tag{L-15438.2}
\]

The Laurent expansion of zeta at one gives

\[
\boxed{
{\zeta(1+sr)\over\zeta(1+s(1+r))}
\longrightarrow {1+r\over r}
=1+{1\over r}.}
\tag{L-15438.3}
\]

The right side is the Laplace transform of

\[
\boxed{
\mu_0=\delta_0+d\lambda.}
\tag{L-15438.4}
\]

After one fixed exponential tilt, the measures are finite.  The continuity
theorem therefore gives

\[
\boxed{
\mu_s\Longrightarrow_{\rm vague}\delta_0+d\lambda.}
\tag{L-15438.5}
\]

Since all distribution functions are monotone and the limiting distribution
function

\[
\mu_0([0,\lambda])=1+\lambda
\tag{L-15438.6}
\]

is continuous for `lambda>0`, the convergence of cumulative masses is locally
uniform away from zero:

\[
\boxed{
\sup_{\delta\le\lambda\le L}
\left|
 \sum_{s\log n\le\lambda}{F_s(n)\over n}
 -(1+\lambda)
\right|
\longrightarrow0.}
\tag{L-15438.7}
\]

## 2. The rescaled beta kernel

Put

\[
\boxed{k_s(\lambda)=n_s(\lambda/s),\qquad\lambda\ge0.}
\tag{L-15438.8}
\]

The incomplete-beta formula reads

\[
k_s(\lambda)
={\pi^{s/2}\over\Gamma(s/2)}e^{-\lambda}
B_{1-e^{-2\lambda/s}}
 \left({s\over2},{3\over2}-{s\over2}\right).
\tag{L-15438.9}
\]

For every `0<delta<L`, the omitted beta tail is exponentially small uniformly
on `[delta,L]`, while

\[
{\pi^{s/2}\over\Gamma(s/2)}
B\left({s\over2},{3\over2}-{s\over2}\right)
=\pi^{s/2}{\Gamma((3-s)/2)\over\Gamma(3/2)}
\longrightarrow1.
\tag{L-15438.10}
\]

Hence

\[
\boxed{
\sup_{\delta\le\lambda\le L}
|k_s(\lambda)-e^{-\lambda}|
\longrightarrow0.}
\tag{L-15438.11}
\]

Moreover, for all sufficiently small `s`,

\[
\boxed{0\le k_s(\lambda)\le C e^{-\lambda}}
\tag{L-15438.12}
\]

with one absolute `C` on `lambda>=0`.  The functions `k_s` are unimodal, so
their total variations are uniformly bounded as well.

## 3. Exact scaled convolution

At `t=lambda/s`, the positive discrete component of `Y_s` is exactly

\[
\boxed{
M_s(\lambda/s)
=\int_{[0,\lambda]}
 k_s(\lambda-u)d\mu_s(u).}
\tag{L-15438.13}
\]

Fix `0<delta<L`.  For `lambda in [delta,L]`, split the integral at
`u=lambda-epsilon`.

On the first part, (L-15438.5) and (L-15438.11) give convergence to the
corresponding convolution with `mu_0`.  On the final interval, (L-15438.12) and
the locally uniform cumulative convergence (L-15438.7) bound the contribution
by `O(epsilon)+o_s(1)`, uniformly in `lambda`.  Letting `epsilon downarrow0`
yields

\[
\begin{aligned}
M_s(\lambda/s)
&\longrightarrow
\int_{[0,\lambda]}
 e^{-(\lambda-u)}(\delta_0+du)\\
&=e^{-\lambda}+1-e^{-\lambda}=1.
\end{aligned}
\tag{L-15438.14}
\]

Thus

\[
\boxed{
\sup_{\delta\le\lambda\le L}
|M_s(\lambda/s)-1|
\longrightarrow0.}
\tag{L-15438.15}
\]

## 4. Continuous comparator

The comparator has the exact scaled form

\[
\begin{aligned}
c_s I_s(\lambda/s)
&={c_s\over s}\int_0^\lambda k_s(v)dv.
\end{aligned}
\tag{L-15438.16}
\]

Since

\[
{c_s\over s}\longrightarrow1
\tag{L-15438.17}
\]

and `k_s` is dominated by (L-15438.12),

\[
\boxed{
\sup_{0\le\lambda\le L}
\left|
 c_sI_s(\lambda/s)-(1-e^{-\lambda})
\right|
\longrightarrow0.}
\tag{L-15438.18}
\]

Subtracting (L-15438.18) from (L-15438.15) proves the pointwise local limit:

\[
\boxed{
\sup_{\delta\le\lambda\le L}
\left|
 Y_s(\lambda/s)-e^{-\lambda}
\right|
\longrightarrow0
\qquad(s\downarrow0).}
\tag{L-15438.19}
\]

## 5. Exclusion of compact boundary-layer counterexamples

For every compact interval

\[
0<\delta<L<\infty,
\]

there is `s_(delta,L)>0` such that

\[
\boxed{
Y_s(\lambda/s)>0
\quad
(0<s<s_{\delta,L},\ \delta\le\lambda\le L).}
\tag{L-15438.20}
\]

Equivalently, no negative endpoint sequence can satisfy simultaneously

\[
s_j\downarrow0,
\qquad
0<\delta\le s_j\log N_j\le L<\infty.
\tag{L-15438.21}
\]

This closes the microscopic-spike loophole left by the vague convergence in
`L-15437` throughout every fixed positive boundary-layer window.

## 6. The only two escape corners left

Combine `L-15436` and (L-15438.20).  If

\[
Y_{s_j}(\log N_j)<0,
\qquad N_j\to\infty,
\tag{L-15438.22}
\]

then necessarily `s_j downarrow0`, and after passing to a subsequence one must
have one of the two extreme scalings

\[
\boxed{s_j\log N_j\longrightarrow0}
\tag{L-15438.23}
\]

or

\[
\boxed{s_j\log N_j\longrightarrow\infty.}
\tag{L-15438.24}
\]

The complete finite positive windows `0<lambda<infinity` are closed.

This is a decisive sharpening of the global attack.  The remaining arithmetic
work is no longer a two-dimensional continuum problem; it is confined to two
asymptotic corners.

## 7. Proof boundary

- Every measure used in the convergence argument is positive before the final
  subtraction.
- The local uniform convolution limit avoids any appeal from vague convergence
  of a signed density to pointwise convergence.
- No statement is made uniformly as `lambda downarrow0` or `lambda to infinity`.
- The two escape corners in (L-15438.23)--(L-15438.24) remain open.
- This lemma does not prove `Y_s>=0` globally or RH.
