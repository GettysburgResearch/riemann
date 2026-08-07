# L-23205 — Terminal lattice rows are exponentially small

Claim ID: `L-23205`  
Title: Exact half-pole moment cancellation and one Euler remainder close every unrestricted terminal lattice row  
Status: **PROPOSED COMPLETE ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-21`  
Created: 2026-08-07  
Issue: #232  
Dependencies: PR #158 `L-15155`; elementary periodic-Bernoulli Euler summation  
Scope: terminal Type-I rows only; no balanced Type-II estimate

## 1. Window hypotheses

Let `W` be compactly supported in `[u_-,u_+]`, continuous, piecewise `C^1`,
zero at both support endpoints, and with `W' in L^1`.  Fix `R>=0` and assume

\[
\boxed{
\int_{\mathbb R}u^r e^{-u/2}W(u)\,du=0,
\qquad 0\le r\le R.
}
\tag{L-23205.1}
\]

The high-order safe window `H^[m]` of PR #158 has these moments through
`R=m-1`.

Let `P` be a polynomial of degree at most `R`.

## 2. One unrestricted terminal row

For `A>=1`, define

\[
\boxed{
\mathcal T_{A,P,W}(x)
=
\sum_{n\ge1}
\frac{P(\log n)}{\sqrt{An}}
W\!\left(x-\log(An)\right).
}
\tag{L-23205.2}
\]

The sum is finite.  Assume its active interval is separated from the initial
integer endpoint, equivalently

\[
\frac{e^{x-u_+}}A>1.
\tag{L-23205.3}
\]

The finitely many rows before this condition holds are harmless finite source
terms.

## 3. Exact continuous cancellation

Put

\[
F_{A,x}(t)
=
\frac{P(\log t)}{\sqrt{At}}
W\!\left(x-\log(At)\right).
\]

The substitution `u=x-log(At)` gives

\[
\int_0^\infty F_{A,x}(t)\,dt
=
\frac{e^{x/2}}A
\int_{\mathbb R}
 e^{-u/2}P(x-\log A-u)W(u)\,du.
\tag{L-23205.4}
\]

The second integrand contains a polynomial in `u` of degree at most `R`.
Equation (L-23205.1) therefore proves

\[
\boxed{
\int_0^\infty F_{A,x}(t)\,dt=0.
}
\tag{L-23205.5}
\]

The pole-model main term vanishes before any estimate, uniformly in `A`.

## 4. Directed Euler remainder

For a compact continuous piecewise-`C^1` function vanishing at its support
endpoints, the first periodic-Bernoulli formula gives

\[
\left|
\sum_{n\in\mathbb Z}F(n)-\int_{\mathbb R}F(t)dt
\right|
\le\frac12\int_{\mathbb R}|F'(t)|dt.
\tag{L-23205.6}
\]

Direct differentiation, followed by `u=x-log(At)`, yields

\[
\begin{aligned}
\int_0^\infty|F'_{A,x}(t)|dt
\le e^{-x/2}
\int_{u_-}^{u_+}e^{u/2}
\Big(&|P'(x-\log A-u)|\,|W(u)|\\
&+|P(x-\log A-u)|
 [\tfrac12|W(u)|+|W'(u)|]
\Big)du.
\end{aligned}
\tag{L-23205.7}
\]

Define

\[
\mathcal P_{A,x}
=
\max_{u_-\le u\le u_+}
\left(
|P(x-\log A-u)|+|P'(x-\log A-u)|
\right)
\]

and

\[
C_W
=
\frac12\int_{u_-}^{u_+}e^{u/2}
\left(\frac32|W(u)|+|W'(u)|\right)du.
\]

Combining (L-23205.5)--(L-23205.7) gives the uniform row bound

\[
\boxed{
|\mathcal T_{A,P,W}(x)|
\le C_W\mathcal P_{A,x}e^{-x/2}.
}
\tag{L-23205.8}
\]

The leading exponential is independent of the small multiplicative prefix `A`.

## 5. A complete terminal family

Let `J<=x<=J+1` and suppose a source-bound terminal family has the form

\[
\mathcal T_J(x)
=
\sum_{A\in\mathcal A_J}c_A\mathcal T_{A,P_A,W}(x),
\]

with

\[
A\le e^{\delta J+O_K(1)}
\tag{L-23205.9}
\]

and fixed-order coefficient mass

\[
\sum_A|c_A|
\max_{J\le x\le J+1}\mathcal P_{A,x}
\le e^{(\delta+o_K(1))J}.
\tag{L-23205.10}
\]

Then

\[
\boxed{
\sup_{J\le x\le J+1}|\mathcal T_J(x)|
\le
\exp\left[-\left(\frac12-\delta-o_K(1)\right)J\right],
}
\tag{L-23205.11}
\]

and

\[
\boxed{
\int_J^{J+1}|\mathcal T_J(x)|^2dx
\le
\exp\left[-\left(1-2\delta-o_K(1)\right)J\right].
}
\tag{L-23205.12}
\]

At the canonical fixed reserve

\[
\delta=\frac15,
\]

this is

\[
\boxed{
E_{K,\mathrm{term}}(J)
\le e^{-(3/5-o_K(1))J}.
}
\tag{L-23205.13}
\]

Thus the terminal coefficient exponent is exactly zero; in fact the terminal
family decays exponentially.

## 6. Scope

The lemma uses no prime number theorem, zero-free region, RH assumption, or
packet/global-Selberg identification.  It closes a terminal row only after an
exact source reduction has shown that the remaining large variable runs over a
complete positive-integer lattice and that every cutoff lies in the small
prefix.

That structural reduction is supplied by `L-23206`.  Balanced Type-II rows are
not covered here.

## 7. Proof boundary

Closed here:

- exact half-pole main-term cancellation;
- the first Euler remainder with explicit window norm;
- exponential terminal-family decay.

Open elsewhere:

- the corrected source reduction to the unrestricted lattice form;
- the signed balanced Type-II estimate;
- RH.