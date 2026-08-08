# L-30501 — Exact central-cascade entropy Abel identity

Claim ID: `L-30501`  
Title: The complete signed central cascade evaluates the prime-power ramp through total residual mass and one explicit odd-parity correction, without a capacity norm  
Status: **PROPOSED COMPLETE EXACT FINITE IDENTITY**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #280 exact finite central saturation; Legendre–Kummer  
Scope: exact cancellation-preserving objective formula; no asymptotic estimate or RH conclusion

## 1. Exact central cascade

Fix an endpoint `X` and let

\[
r_0(q)=q^{-1/2}\log(X/q),
\qquad 2\le q\le X.
\tag{L-30501.1}
\]

Use the exact finite residual operator of PR #280:

\[
r_{a+1}(q)=
\sum_{k\ge1}
\left[r_a(2kq-1)-r_a((2k+1)q)\right],
\tag{L-30501.2}
\]

with zero extension beyond the current endpoint.  At depth `a`, put

\[
d_a(n)=r_a(n)-r_a(n+1)
\tag{L-30501.3}
\]

on the central split

\[
[n,\lfloor n/2\rfloor].
\]

Support halves at every step, so the cascade terminates exactly.  The sum of all
stage flows has carry columns `r_0`.

## 2. Central binomial entropy increments

Put

\[
L_n=\log\binom n{\lfloor n/2\rfloor}.
\tag{L-30501.4}
\]

The ratios of consecutive central binomial coefficients are exact:

\[
\boxed{
L_n-L_{n-1}=
\begin{cases}
\log2,&n\text{ even},\\[1mm]
\log2+\log\dfrac n{n+1},&n\text{ odd}.
\end{cases}}
\tag{L-30501.5}
\]

Indeed,

\[
\frac{\binom{2m}{m}}{\binom{2m-1}{m-1}}=2
\]

and

\[
\frac{\binom{2m+1}{m}}{\binom{2m}{m}}
=\frac{2m+1}{m+1}
=2\frac{2m+1}{2m+2}.
\]

## 3. One-stage Abel identity

Finite summation by parts gives

\[
\begin{aligned}
\sum_{n\ge2}d_a(n)L_n
&=r_a(2)L_2
 +\sum_{n\ge3}r_a(n)(L_n-L_{n-1})\\
&=\boxed{
 \log2\sum_{n\ge2}r_a(n)
 +\sum_{\substack{n\ge3\\n\text{ odd}}}
  r_a(n)\log\frac n{n+1}.}
\end{aligned}
\tag{L-30501.6]

The closing bracket in the tag is typographical only.

No positive part, absolute value, or flow-capacity estimate appears.

## 4. Exact complete prime-ramp formula

By Legendre–Kummer and exact saturation,

\[
\sum_a\sum_{n\ge2}d_a(n)L_n
=
\sum_{p^j\le X}
\frac{\Lambda(p^j)}{\sqrt{p^j}}
\log\frac X{p^j}.
\tag{L-30501.7}
\]

Combining with (L-30501.6) gives the exact identity

\[
\boxed{
\begin{aligned}
\mathcal P(X)
={}&\log2
 \sum_a\sum_{n\ge2}r_a(n)\\
&+\sum_a\sum_{\substack{n\ge3\\n\text{ odd}}}
 r_a(n)\log\frac n{n+1},
\end{aligned}}
\tag{L-30501.8}
\]

where

\[
\mathcal P(X)=
\sum_{p^j\le X}
\frac{\Lambda(p^j)}{\sqrt{p^j}}
\log\frac X{p^j}.
\]

Thus the exact central producer has a cancellation-preserving scalar objective
without first converting formal sources into positive edges.

## 5. Why this identity changes the repair target

The Cycle-Debt estimate controls every negative edge in a source-blind
square-root capacity norm.  Equation (L-30501.8) shows that this is sufficient
but not logically necessary for the central producer.  Its objective depends on
only:

```text
the signed total mass of every residual stage;
one 1/n-sized odd-parity correction.
```

A corrected continuation may therefore attack the complete signed resolvent
before positive/negative separation.  In particular, the macroscopic atomic
boundary norm in `R-30501` does not imply a macroscopic entropy loss: adjacent
source atoms have logarithmic objective differences and must first be
recombined.

## 6. Firewall

The identity does not itself estimate either term in (L-30501.8).  The first is
a complete eta-resolvent mass and retains the reciprocal-zeta obstruction.  A
claim that it equals its continuum geometric sum up to polylogarithmic error
would already be load bearing.

Similarly, finite computations showing a small odd correction cannot be
promoted to a cofinal theorem.

## 7. Proof boundary

Closed exactly:

1. the central-binomial increment formula;
2. the one-stage Abel identity;
3. the complete signed-cascade prime-ramp identity;
4. the precise cancellation-preserving scalar replacing the false atomic norm.

Open:

1. a subpower estimate for the complete signed residual mass and odd correction;
2. the sharp prime-ramp lower bound;
3. RH.
