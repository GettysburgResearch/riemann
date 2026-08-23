# L-105385 — Real-saddle concentration makes every fixed Xi source order eventually positive

Claim ID: `L-105385`  
Status: **PROVED UNCONDITIONAL REAL-LINE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: the explicit positive Xi Fourier kernel; `L-105384`  
RH status: **not assumed**

## 1. Mellin-tilted Xi law

Use the one-sided positive Xi Fourier kernel in the normalization of the
current programme:

\[
\Phi(u)=
\sum_{n\ge1}
\pi n^2 e^{5u/2}
\left(2\pi n^2e^{2u}-3\right)
 e^{-\pi n^2e^{2u}},
\qquad u\ge0.
\tag{L-105385.1}
\]

A fixed positive normalization factor is irrelevant below. For real `s>0`,
put

\[
M_s=\int_0^\infty u^s\Phi(u)\,du
\]

and define the probability law

\[
\boxed{
 d\mathbb P_s(u)={u^s\Phi(u)\over M_s}\,du.
}
\tag{L-105385.2}
\]

Let

\[
S_s(u)=s\log u+\log\Phi(u).
\tag{L-105385.3}
\]

## 2. The real saddle

For large `u`, the first summand dominates with every fixed derivative:

\[
\Phi(u)
=
\pi e^{5u/2}(2\pi e^{2u}-3)e^{-\pi e^{2u}}
\left(1+O(e^{-3\pi e^{2u}})ight).
\tag{L-105385.4}
\]

Consequently,

\[
(\log\Phi)'(u)
={9\over2}-2\pi e^{2u}+O(e^{-2u}),
\tag{L-105385.5}
\]

\[
(\log\Phi)''(u)
=-4\pi e^{2u}+O(e^{-2u}).
\tag{L-105385.6}
\]

For all sufficiently large `s`, `S_s` has a unique global maximizer `w_s` in
the large-`u` region. It satisfies

\[
\boxed{
2\pi e^{2w_s}
={s\over w_s}+O(1),
}
\tag{L-105385.7}
\]

and hence

\[
\boxed{
w_s={1\over2}\log s+O(\log\log s).}
\tag{L-105385.8}
\]

The curvature is

\[
\boxed{
\kappa_s:=-S_s''(w_s)
={2s\over w_s}
\left(1+O(1/w_s)\right).
}
\tag{L-105385.9}
\]

### Justification of the global maximum

The function `S_s` tends to `-infinity` at both endpoints. Its maximizer tends
to infinity because evaluation at any fixed `u` is beaten by evaluation at a
small fixed multiple of `log s`. On a fixed large half-line, (L-105385.6)
gives `S_s''<0`, so there is at most one critical point there. The derivative
is positive before the point determined by (L-105385.7) and negative after it.
The bounded initial interval is exponentially smaller in the `s log u` scale.
Thus this critical point is the unique global maximizer.

## 3. Uniform real concentration

There are absolute constants `c,C>0` such that, for all large `s`,

\[
S_s(w_s+v)-S_s(w_s)
\le-c\kappa_sv^2
\qquad(|v|\le1),
\tag{L-105385.10}
\]

while the complement `|v|>1` contributes `O(e^{-c\kappa_s})` relative to the
central mass. On the left this follows from strict concavity down to a fixed
large point and the loss in `s log u`; on the right the term
`-pi e^(2u)` gives a still stronger loss.

The matching lower curvature bound on `|v|<=kappa_s^(-1/2)` gives

\[
M_s\asymp
{e^{S_s(w_s)}\over\sqrt{\kappa_s}}.
\tag{L-105385.11}
\]

Integration of (L-105385.10) therefore yields, for every fixed `m>=1`,

\[
\boxed{
\mathbb E_s|U-w_s|^m
=O_m(\kappa_s^{-m/2}).
}
\tag{L-105385.12}
\]

For fixed negative moments, the interval near zero is harmless: its numerator
contains `u^(s-A)` and is superexponentially small relative to
`e^(S_s(w_s))/sqrt(kappa_s)` once `s>A`. Thus (L-105385.12) extends to the
Taylor estimates needed for every fixed real power.

## 4. Fixed-power moment ratios

For every fixed real `a`,

\[
\boxed{
{M_{s+a}\over M_s}
=
\mathbb E_s[U^a]
=w_s^a
\left(1+O_a\!\left(\sqrt{w_s/s}\right)\right).
}
\tag{L-105385.13}
\]

Indeed, on the central event expand `U^a` about `w_s`; the first absolute
remainder is paid by (L-105385.12), and the tails are exponentially smaller.
The displayed error is deliberately weaker than the available
`O_a((sw_s)^(-1/2))` relative bound.

In particular, for every fixed integer `j`,

\[
\boxed{
{\mathbb E_s[U^{2j}]
 \over
 \mathbb E_s[U^2]^j}
\longrightarrow1,
}
\tag{L-105385.14}
\]

and

\[
\boxed{
\mathbb E_s[U^2]\mathbb E_s[U^{-2}]
\longrightarrow1.
}
\tag{L-105385.15}
\]

## 5. Consequences for odd Xi derivatives

For `F=Xi^(r)` with odd `r`, the law in `L-105380` is exactly
`P_s` with

\[
s=r+1.
\]

Taking `omega^2=E_s[U^2]`, (L-105385.14) supplies all normalized moment
convergences required by `L-105384`. Therefore, for every fixed `k`, there is
`R_k^odd` such that

\[
\boxed{
\mathsf A_k^{(0)}(\Xi^{(r)})\succ0,
\qquad
\mathsf A_k^{(1)}(\Xi^{(r)})\succ0
}
\tag{L-105385.16}
\]

for every odd `r>=R_k^odd`.

In particular, the explicit threshold

\[
{\mathbb E[X^2]\over\mathbb E[X]^2}
\le{35\over27}
\]

from `L-105383` holds eventually.

## 6. Consequences for even Xi derivatives

For even `r`, the law in `L-105381` is `P_s` with

\[
s=r+2.
\]

Equations (L-105385.14)--(L-105385.15) supply both the positive and reciprocal
moment convergence in `L-105384`. Hence, for every fixed `k`, there is
`R_k^even` such that

\[
\boxed{
\mathsf A_k^{(0)}(\Xi^{(r)})\succ0,
\qquad
\mathsf A_k^{(1)}(\Xi^{(r)})\succ0
}
\tag{L-105385.17}
\]

for every even `r>=R_k^even`.

In particular,

\[
\mathbb E[X]\mathbb E[X^{-1}]
\le{15\over7}
\]

holds eventually.

## 7. What has been removed from the frontier

For each prescribed finite order, high-derivative **source-matrix positivity**
is unconditional and uses only a positive real integral. It does not require:

```text
complex saddle continuation;
zero-free shifted contours;
phase-cell root localization;
critical residue asymptotics;
or RH.
```

The remaining high-tail capacity problem is entirely on the critical-atom
side and in matching that side to the positive source reserve.

## 8. Scope

The derivative threshold depends on `k`; no uniform all-order threshold is
proved. The theorem supplies no realness or sign theorem for the critical
points, no bound on the normalized critical-capacity operator, and no low-order
descent. It proves neither `CRVH105330`, `OSCC105371`, `BRP105220`, nor RH.
