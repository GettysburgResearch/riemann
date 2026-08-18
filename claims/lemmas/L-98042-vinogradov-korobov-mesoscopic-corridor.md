# L-98042 — Vinogradov–Korobov discrepancy gives a mesoscopic positive corridor

Claim ID: `L-98042`<br>
Status: **PROVED UNCONDITIONAL UNIFORM ASYMPTOTIC THEOREM**<br>
Created: 2026-08-18<br>
Depends on: `L-98040/L-98041`; PR #603 `L-98020`; the classical
Vinogradov--Korobov zero-free region<br>
RH status: **not assumed**

Let

\[
U(Y,z)={\mathcal F(Y,z)\over\sqrt Y},
\qquad
L=\log z,
\qquad
u={\log Y\over L}.
\]

PR #603 compares the exact reciprocal rough-Möbius prefix to the Dickman
function by

\[
\sup_{0\le v\le u}
|A_z(z^v)-\rho(v)|
\le
u e^{\Delta(Y,z)}
\left(2\Delta(Y,z)+{1\over2(z-1)}\right).
\tag{L-98042.1}
\]

The classical Vinogradov--Korobov prime-number theorem, followed by partial
summation over primes, gives constants `c,C>0` such that

\[
\boxed{
\Delta(Y,z)
\le C\exp\!\left[-cL^{3/5}(\log L)^{-1/5}\right]
}
\tag{L-98042.2}
\]

uniformly in `1<=v<=u` once `z` is sufficiently large.

Applying the exact Stieltjes transfer (L-98040.4) and total variation
`V_0<infinity` gives

\[
\boxed{
|U(Y,z)-\mathcal C_L(u)|
\ll_{P_{61}}
 u\exp\!\left[-cL^{3/5}(\log L)^{-1/5}\right].
}
\tag{L-98042.3}
\]

The de Bruijn lower bound

\[
\rho(u)\ge\exp[-C_1u\log(u+2)]
\tag{L-98042.4}
\]

shows that the error in (L-98042.3) is `o(rho(u))` whenever

\[
\boxed{
 u\log(u+2)
\le c_1L^{3/5}(\log L)^{-1/5}
}
\tag{L-98042.5}
\]

for a sufficiently small absolute `c_1>0`. Condition (L-98042.5) also implies
`L>>log(u+2)`, so `L-98041` applies. Hence

\[
\boxed{
\mathcal F(Y,z)>0
}
\tag{L-98042.6}
\]

throughout (L-98042.5), for all sufficiently large `Y`.

## A simple endpoint-only corridor

Put `N=log Y`. There is an absolute `c_0>0` such that

\[
\boxed{
2\le u\le
c_0 N^{3/8}(\log N)^{-3/4}
}
\tag{L-98042.7}
\]

implies (L-98042.5). Indeed, with `L=N/u`, the left-to-right comparison reduces
to

\[
u^{8/5}\log u\,[\log(N/u)]^{1/5}\ll N^{3/5},
\]

and the powers of `log N` cancel exactly at exponent `3/4`.
Consequently

\[
\boxed{
 u\le c_0(\log Y)^{3/8}(\log\log Y)^{-3/4}
\Longrightarrow
\mathcal F(Y,z)>0.
}
\tag{L-98042.8}
\]

This strictly extends PR #603's corridor of order
`loglog(Y)/logloglog(Y)`.

## Scope

The improvement comes from two source-faithful facts:

1. the whole nonhomogeneous `P_61` base is transported by one finite-variation
   Stieltjes measure, so there is no separate unsigned bounded-remainder loss;
2. the prime-reciprocal discrepancy is used at Vinogradov--Korobov strength
   rather than at the coarse `1/log z` scale.

The theorem does not reach fixed `z` or the full root. A counterexample sequence
must now lie beyond the mesoscopic corridor in (L-98042.8).
