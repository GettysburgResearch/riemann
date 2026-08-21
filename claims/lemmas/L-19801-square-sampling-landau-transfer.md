# L-19801 — Square-sampling Landau transfer

Claim ID: `L-19801`  
Title: Lower bounds for the zeta screw function at square cutoffs propagate to zero-free half-planes  
Status: `PROPOSED — COMPLETE ANALYTIC PROOF FROM THE IMPORTED SCREW/LAPLACE IDENTITY`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Primary sources: Nakamura--Suzuki, arXiv:2306.08317, equations (1.5), (1.7), (2.2); Suzuki, JLMS 108 (2023), Theorems 1.6 and 11.1  
Scope: scalar replacement for the final low-index/capture gate

## 1. Exact screw function

Let `g_zeta` be Nakamura--Suzuki's even screw function. For `t>=0`,

\[
\begin{aligned}
g_\zeta(t)={}&-4\left(e^{t/2}+e^{-t/2}-2\right)
 +\sum_{m\le e^t}\frac{\Lambda(m)}{\sqrt m}(t-\log m)\\
&-\frac t2\bigl(\psi(1/4)-\log\pi\bigr)
 +\frac14\left[
 e^{-t/2}\Phi(e^{-2t},2,1/4)-\Phi(1,2,1/4)
 \right].
\end{aligned}
\tag{L-19801.1}
\]

Put

\[
\boxed{\Psi(t)=-g_\zeta(t).}
\tag{L-19801.2}
\]

The source proves the locally uniform zero expansion

\[
g_\zeta(t)
 =\sum_\gamma m_\gamma
 \frac{e^{-i\gamma t}-1}{\gamma^2}
\tag{L-19801.3}
\]

and the Fourier--Laplace identity

\[
\boxed{
\int_0^\infty \Psi(t)e^{izt}\,dt
 =-\frac1{z^2}\frac{\xi'}{\xi}\left(\frac12-iz\right),
\qquad \Im z>\frac12.}
\tag{L-19801.4}
\]

Under RH, the zeros `gamma` are real, conjugate pairing in (L-19801.3) gives

\[
\boxed{\Psi(t)\ge0\quad(t\in\mathbb R).}
\tag{L-19801.5}
\]

## 2. Unconditional derivative budget

Away from the prime-power knots `t=log m`, differentiation of the finite prime
sum gives

\[
\frac d{dt}
\sum_{m\le e^t}\frac{\Lambda(m)}{\sqrt m}(t-\log m)
 =\sum_{m\le e^t}\frac{\Lambda(m)}{\sqrt m}.
\tag{L-19801.6}
\]

For `t>=log 2`, the elementary estimates

\[
\Lambda(m)\le\log m\le t,
\qquad
\sum_{m\le e^t}m^{-1/2}\le2e^{t/2}
\tag{L-19801.7}
\]

give

\[
\sum_{m\le e^t}\frac{\Lambda(m)}{\sqrt m}
 \le2t e^{t/2}.
\tag{L-19801.8}
\]

For the Lerch term, the absolutely convergent expansion

\[
e^{-t/2}\Phi(e^{-2t},2,1/4)
 =\sum_{k=0}^\infty
 \frac{e^{-(2k+1/2)t}}{(k+1/4)^2}
\tag{L-19801.9}
\]

yields

\[
\left|\frac d{dt}
 e^{-t/2}\Phi(e^{-2t},2,1/4)\right|
 =2\sum_{k=0}^\infty
 \frac{e^{-(2k+1/2)t}}{k+1/4}
 =O(1)
\tag{L-19801.10}
\]

uniformly for `t>=log 2`. The remaining elementary and linear terms are
`O(e^(t/2))+O(1)`. Consequently there is an absolute effective constant `C_*`
such that

\[
\boxed{
|\Psi'(t)|\le C_*(1+t)e^{t/2}}
\tag{L-19801.11}
\]

on every open interval between consecutive knots. Since `Psi` is continuous,
(L-19801.11) controls its variation across every closed interval as well.

No prime number theorem and no zero-location hypothesis enter this bound.

## 3. General logarithmic sampling

Fix `A>0` and put

\[
t_n=A\log n.
\tag{L-19801.12}
\]

For `t_n<=t<=t_(n+1)`,

\[
t_{n+1}-t_n
 =A\log(1+1/n)\le A/n,
\tag{L-19801.13}
\]

and `e^(t/2)<= (n+1)^(A/2)`. Hence (L-19801.11) gives

\[
\boxed{
|\Psi(t)-\Psi(t_n)|
 \le C_A(1+t)
 e^{\sigma_A t},
\qquad
\sigma_A=\max\left(0,\frac12-\frac1A\right),}
\tag{L-19801.14}
\]

for one effective constant `C_A` and all sufficiently large `n`.

The critical sampling exponent is `A=2`: the growth `e^(t/2)` is exactly
cancelled by the square-support mesh `t_(n+1)-t_n=O(e^(-t/2))`, leaving only a
polynomial interpolation loss.

## 4. Landau transfer with a lower envelope

Suppose that, for some `sigma>=0`,

\[
\Psi(t_n)\ge-C(1+t_n)^B e^{\sigma t_n}
\tag{L-19801.15}
\]

eventually, where `sigma>=sigma_A`. Equations (L-19801.14)--(L-19801.15) imply

\[
\Psi(t)\ge-C'(1+t)^{B'}e^{\sigma t}
\tag{L-19801.16}
\]

eventually on the whole half-line.

Choose a positive polynomial `P(t)` dominating the polynomial factor and set

\[
H(t)=\Psi(t)+P(t)e^{\sigma t}.
\tag{L-19801.17}
\]

After adding one compactly supported continuous correction, which changes its
Laplace transform by an entire function, we may assume

\[
H(t)\ge0\quad(t\ge0).
\tag{L-19801.18}
\]

The transform of `P(t)e^(sigma t)` is holomorphic for `Im z>sigma`. Combining it
with (L-19801.4) gives a meromorphic continuation of

\[
\int_0^\infty H(t)e^{izt}\,dt
\tag{L-19801.19}
\]

to that half-plane. On its positive imaginary axis `z=iy`, `y>sigma`, the
corresponding xi argument is the positive real number `1/2+y`; `xi` has no zero
there.

Landau's one-sign theorem for Laplace transforms says that the abscissa of
convergence of a nonnegative, non-eventually-zero function is a singularity on
the real Laplace axis. Therefore (L-19801.19) cannot have an abscissa larger
than `sigma`. If `H` is eventually zero, the same conclusion follows directly
because its tail transform is entire. It follows that (L-19801.19) converges for

\[
\Im z>\sigma.
\]

Equation (L-19801.4) then implies that `xi'/xi(1/2-iz)` has no pole there.
Thus

\[
\boxed{
\xi(s)\ne0
\quad\text{whenever}\quad
\Re s>\frac12+\sigma.}
\tag{L-19801.20}
\]

This is the sampling-to-zero-free-half-plane transfer.

## 5. Square-support consequences

Take `A=2`, so `sigma_A=0` and `t_n=2log n`. If

\[
\Psi(2\log n)\ge-C_\varepsilon n^{2\varepsilon}
\tag{L-19801.21}
\]

for every `epsilon>0` and all sufficiently large `n` (with constants allowed to
depend on `epsilon`), then (L-19801.20) excludes zeros in

\[
\Re s>\frac12+\varepsilon
\]

for every `epsilon>0`. Functional-equation symmetry therefore gives RH.
Equivalently, it is sufficient that

\[
\boxed{
(-\Psi(2\log n))_+=n^{o(1)}.}
\tag{L-19801.22}
\]

The stronger eventual sign condition

\[
\boxed{
\Psi(2\log n)\ge0
\quad\text{eventually}}
\tag{L-19801.23}
\]

is therefore sufficient for RH.

Conversely RH gives (L-19801.23) for every `n` by (L-19801.5). Hence

\[
\boxed{
\mathrm{RH}
\iff
\Psi(2\log n)\ge0
\text{ for every sufficiently large integer }n.}
\tag{L-19801.24}
\]

A second exact equivalent is

\[
\boxed{
\mathrm{RH}
\iff
\sup_{n\ge2}|\Psi(2\log n)|<\infty.}
\tag{L-19801.25}
\]

For the reverse implication, bounded samples and (L-19801.14) give a polynomial
bound on the complete half-line; adding a polynomial one-sign correction and
repeating Section 4 yields RH. Under RH, Suzuki's zero expansion bounds `Psi`
on the whole line.

## 6. Proof boundary

- The derivative and interpolation estimates are elementary consequences of the
  exact prime/Lerch formula.
- The Landau step is the same one-sign Laplace principle used by
  Nakamura--Suzuki and Suzuki.
- The theorem genuinely replaces an infinite-dimensional low-index statement by
  scalar finite prime-power inequalities.
- It does **not** prove the cofinal inequalities (L-19801.21) or
  (L-19801.23). Those inequalities carry the remaining RH content.
- A finite numerical ladder, however long, does not establish the eventual
  statement.