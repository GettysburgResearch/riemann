# T-30402 — The terminal parity boundary is one zero-safe dyadic Möbius–Riesz shell

Claim ID: `T-30402`  
Title: The correctly inverted finite parity source is a dilation of one stably invertible dyadic Möbius–Riesz shell whose subpower bound is equivalent to RH  
Status: **PROPOSED COMPLETE EQUIVALENCE THEOREM — THE SHELL BOUND REMAINS UNPROVEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30407`, `L-30410`; classical Littlewood criterion for weighted Möbius sums  
Scope: full Riemann Hypothesis

## 1. Critical Möbius–Riesz state

Extend

\[
\boxed{
M_{1/2}(x)
=\sum_{n\le x}{\mu(n)\over\sqrt n}}
\tag{T-30402.1}
\]

by zero for `0<x<1`.

Retain

\[
\boxed{
\rho_2=1-\eta(1/2),
\qquad0<\rho_2<1.}
\tag{T-30402.2}
\]

Define the zero-safe dyadic shell

\[
\boxed{
\mathfrak D_2(x)
=M_{1/2}(x)
-\rho_2M_{1/2}(x/2)
+\sqrt2-1.}
\tag{T-30402.3}

The additive constant matches the exact half-pole mode in the finite boundary
source.

## 2. Exact identification of every even-endpoint source coefficient

Let

\[
N=2Q
\]

be even. `L-30407.14` gives, for every `2<=m<=Q`,

\[
\begin{aligned}
\sigma_{N,1/2}(m)
={1\over\sqrt m}\Big[&
-M_{1/2}(N/m)\\
&+\rho_2M_{1/2}(Q/m)
+1-\sqrt2\Big].
\end{aligned}
\]

Since

\[
Q/m={1\over2}(N/m),
\]

this is exactly

\[
\boxed{
\sigma_{N,1/2}(m)
=-{1\over\sqrt m}
\mathfrak D_2(N/m).}
\tag{T-30402.4}

Thus the complete finite terminal parity source is not a growing family of
unrelated coefficient words. It is the multiplicative dilation orbit of one
scalar function `mathfrak D_2`.

Odd endpoints add only the one collar coordinate of `L-30405`; they do not
change the cofinal scalar.

## 3. Stable finite inversion

Put

\[
\widetilde{\mathfrak D}_2(x)
=\mathfrak D_2(x)-(\sqrt2-1)
=M_{1/2}(x)-\rho_2M_{1/2}(x/2).
\tag{T-30402.5}
\]

Iterating the identity gives, for every `x>=1`,

\[
\boxed{
M_{1/2}(x)
=\sum_{j=0}^{\lfloor\log_2x\rfloor}
 \rho_2^j
 \widetilde{\mathfrak D}_2(x/2^j).}
\tag{T-30402.6}

The sum is finite because the state vanishes below one.

Conversely, (T-30402.5) immediately bounds the shell by two values of the state.
Therefore, for every `epsilon>0`,

\[
\boxed{
M_{1/2}(x)=O_\epsilon(x^\epsilon)
\quad\Longleftrightarrow\quad
\mathfrak D_2(x)=O_\epsilon(x^\epsilon).}
\tag{T-30402.7}

Indeed, the forward implication is immediate. For the reverse implication,
(T-30402.6) gives

\[
\begin{aligned}
|M_{1/2}(x)|
&\le C_\epsilon
 \sum_{j\le\log_2x}
 \rho_2^j(x/2^j)^\epsilon\\
&\le {C_\epsilon x^\epsilon
 \over1-\rho_22^{-\epsilon}}.
\end{aligned}
\tag{T-30402.8}

## 4. Mellin transform and zero-safe numerator

Initially for `Re z>1/2`, partial summation gives

\[
\boxed{
\int_1^\infty
M_{1/2}(x)x^{-z-1}dx
={1\over z\zeta(z+1/2)}.}
\tag{T-30402.9}

Using the zero extension below one,

\[
\int_1^\infty
M_{1/2}(x/2)x^{-z-1}dx
={2^{-z}\over z\zeta(z+1/2)}.
\tag{T-30402.10}

Consequently

\[
\boxed{
\int_1^\infty
\mathfrak D_2(x)x^{-z-1}dx
={1-\rho_22^{-z}
 \over z\zeta(z+1/2)}
+{\sqrt2-1\over z}.}
\tag{T-30402.11}

The filter numerator is zero-safe throughout the closed right half-plane:

\[
|\rho_22^{-z}|
\le\rho_2<1
\qquad(\Re z\ge0).
\]

Hence

\[
\boxed{
1-\rho_22^{-z}\ne0
\qquad(\Re z\ge0).}
\tag{T-30402.12}

Every hypothetical zeta zero with real part greater than `1/2` therefore creates
a genuine uncancelled pole in (T-30402.11).

## 5. Equivalence with RH

The classical Littlewood criterion in this normalization is

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
M_{1/2}(x)=O_\epsilon(x^\epsilon)
\text{ for every }\epsilon>0.}
\tag{T-30402.13}

Combining with (T-30402.7),

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
\mathfrak D_2(x)=O_\epsilon(x^\epsilon)
\text{ for every }\epsilon>0.}
\tag{T-30402.14}

The forward implication may alternatively be obtained from the classical RH
bound on the weighted Möbius sum. The reverse implication follows either from
stable inversion (T-30402.6) and Littlewood, or directly from the genuine Mellin
poles in (T-30402.11).

## 6. Meaning for the terminal programme

`R-30404` proves that the atomic norm of the finite source is linear. Equation
(T-30402.4) explains why: the terminal source samples an RH-equivalent scalar at
all multiplicative ratios `N/m`.

At the same time, the source is much more structured than its total variation:

```text
one zero-safe scalar shell
-> multiplicative dilation
-> exact finite source.
```

Therefore the final theorem cannot be an atomic counting estimate. It must be a
source-specific cancellation theorem for `mathfrak D_2`, or an equivalent
physical reflected estimate which preserves the filter numerator in
(T-30402.11).

The existing dyadic-shell, WSTS, central-cascade, and parity-factor routes all
measure stable transforms of the same scalar.

## 7. No proof is delegated to a reviewer

This theorem proves the exact source identification, stable inversion, Mellin
transform, zero-safety, and RH equivalence.

It does **not** assert the unproved estimate

\[
\mathfrak D_2(x)=O_\epsilon(x^\epsilon).
\]

A future claimed RH proof must supply that estimate or a fully proved equivalent
physical theorem. A reviewer is asked only to check the completed equivalence,
not to invent its missing arithmetic input.

## 8. Exact status

```text
finite terminal source -> one scalar shell     proved
stable shell/state inversion                   proved
zero-safe Mellin transform                     proved
shell subpower <=> RH                          proved
unconditional shell subpower estimate          open
Riemann Hypothesis                             unproved
```
