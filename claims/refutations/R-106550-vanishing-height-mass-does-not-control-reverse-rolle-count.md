# R-106550 — Vanishing height mass does not control reverse–Rolle count

Claim ID: `R-106550`  
Status: **PROVED EXACT FIREWALL**  
Created: 2026-08-25  
Depends on: elementary trigonometric factorization  
RH status: **not assumed**

A horizontal first-moment theorem, even together with a positive even Fourier
source and a completely real-rooted fifth derivative, does not control the
number of parent real zeros.

Fix `c>1` and for every integer `n>=1` put

\[
\boxed{F_n(z)=c+\cos(nz).}
\tag{R-106550.1}
\]

## 1. Positive source and real fifth derivative

The Fourier source is the positive even measure

\[
c\,\delta_0+\frac12\delta_n+\frac12\delta_{-n}.
\]

On the real axis, `F_n(x)>=c-1>0`, so

\[
\boxed{N_{\mathbb R}(F_n;I)=0}
\tag{R-106550.2}
\]

on every interval `I`.

But

\[
F_n^{(5)}(x)=-n^5\sin(nx),
\]

and therefore every zero of the fifth derivative is real and simple.

## 2. The complete nonreal divisor is arbitrarily shallow

Let

\[
a=\operatorname{arcosh}c>0.
\]

The zeros are exactly

\[
\boxed{
z_{k,\pm}={(2k+1)\pi\over n}\pm i{a\over n}.}
\tag{R-106550.3}
\]

On a fixed real interval of length `L`, their number is

\[
{nL\over\pi}+O(1),
\]

whereas their total vertical height is

\[
\boxed{
\sum_{\Re z\in I}|\Im z|
 ={2a\over n}
  \left({nL\over2\pi}+O(1)\right)
 ={aL\over\pi}+O_c(n^{-1}).
}
\tag{R-106550.4}
\]

Hence

\[
{\text{vertical-height mass}\over\text{zero count}}
 \longrightarrow0,
\]

while the parent real-zero proportion remains zero and the fifth derivative
real-zero proportion is one.

## 3. Consequences

The following implications are false in the ambient positive-Fourier class:

```text
total off-axis height = o(total zero count)
 -> almost all parent zeros are real;

positive even Fourier source
 + real-rooted fifth derivative
 + arbitrarily thin zero strip
 -> positive parent real-zero proportion;

small companion pole-height reserve
 -> small all-pass index.
```

The obstruction is microscopic but topological. Each conjugate pair carries
one reverse–Rolle unit even when its height tends to zero.

Therefore `L-106550` can close macroscopic height and reserve terms, but a
valid ninety-percent proof must still control the **number or canonical
correlation of the shallow companion fibres**. That surviving quantity is
isolated in `T-106550`.