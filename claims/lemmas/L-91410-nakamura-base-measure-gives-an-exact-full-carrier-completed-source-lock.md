# L-91410 — Nakamura's base measure gives an exact full-carrier completed source lock

Claim ID: `L-91410`  
Status: **PROVED EXACT COMPLETED SAFE-SOURCE REPRESENTATION; SIGNED POSITIVITY OPEN**  
Created: 2026-08-12  
Depends on: Nakamura source lock, `L-91405`, `L-91407`  
RH status: **unproved**

## 1. One scale-independent completed jump measure

For `u>0`, put

\[
 B(u)=\frac1{1-e^{-2u}}-(1+e^u).
\tag{L-91410.1}
\]

Let

\[
 d\Pi(u)
 =\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}
  \delta_{\log n}(du)
\tag{L-91410.2}
\]

and define the signed completed base measure

\[
 \boxed{
 d\mathfrak M(u)
 =d\Pi(u)+e^{-u/2}B(u)du.
 }
\tag{L-91410.3}
\]

For `c>1/2`, put

\[
 \sigma_c=\frac12+c.
\]

Nakamura's signed quasi-Lévy measure is

\[
 d\nu_{\sigma_c}(u)
 =\sum_{p,k}\frac{p^{-k\sigma_c}}k
  \delta_{k\log p}(du)
 +\frac{e^{-\sigma_cu}}uB(u)du.
\]

At every prime-power atom,

\[
 u\frac{p^{-k\sigma_c}}k
 =\Lambda(p^k)(p^k)^{-1/2-c}.
\]

Consequently

\[
 \boxed{
 u\,d\nu_{\sigma_c}(u)
 =e^{-cu}d\mathfrak M(u).
 }
\tag{L-91410.4}

Thus all safe radial scales are exponential tilts of one completed signed
source.  Its atomic part is the exact critical prime measure of `L-91405`.

## 2. Explicit Jordan split of the base source

Let `varpi>1` solve

\[
 \varpi^3-\varpi-1=0,
 \qquad
 \kappa=\log\varpi.
\]

Since

\[
 B(u)=\frac{1+e^u-e^{3u}}{e^{2u}-1},
\]

one has

\[
 B(u)>0\quad(0<u<\kappa),
 \qquad
 B(u)<0\quad(u>\kappa).
\]

Define positive measures

\[
 \boxed{
 d\mathfrak M^+(u)
 =d\Pi(u)+e^{-u/2}B(u)
  \mathbf1_{0<u<\kappa}du,
 }
\tag{L-91410.5}
\]

\[
 \boxed{
 d\mathfrak M^-(u)
 =-e^{-u/2}B(u)
  \mathbf1_{u>\kappa}du.
 }
\tag{L-91410.6}
\]

Then

\[
 \mathfrak M=\mathfrak M^+-\mathfrak M^-.
\tag{L-91410.7}
\]

The prime source is an orthogonal atomic direct summand of `M_plus`.

## 3. Safe logarithmic-derivative representation

Let

\[
 Q(s)=\frac{\xi'}{\xi}(s).
\]

Nakamura's Lévy--Khintchine formula implies, for real `t` and `c>1/2`,

\[
 \boxed{
 Q(\sigma_c+it)
 =-\lambda_{\sigma_c}
  -\int_0^\infty
  e^{-cu}
  \left(e^{-itu}-\mathbf1_{u\le1/2}\right)
  d\mathfrak M(u).
 }
\tag{L-91410.8}
\]

Differentiating in the safe real direction gives

\[
 \boxed{
 Q'(\sigma_c+it)
 =-\lambda_{\sigma_c}'
  +\int_0^\infty
  u e^{-cu}
  \left(e^{-itu}-\mathbf1_{u\le1/2}\right)
  d\mathfrak M(u).
 }
\tag{L-91410.9}
\]

The compensation makes the continuous integral convergent at zero.  These are
complex identities, not merely real-part formulas.

## 4. The six-pole completed resolvent functional

`L-91407` gives the full carrier Gram

\[
 \mathfrak W_a(x,y)
\]

as a linear expression in

```text
Q(1/2+ra+ix),
Q'(1/2+ra+ix),
Q(1/2+ra-iy),
Q'(1/2+ra-iy),
r=1,2,4,
```

with explicit rational residue coefficients.  Denote this linear functional by

\[
 \mathscr R_{a;x,y}[Q,Q'].
\tag{L-91410.10}
\]

Thus

\[
 \mathfrak W_a(x,y)
 =\mathscr R_{a;x,y}[Q,Q'].
\tag{L-91410.11}
\]

Substitute (L-91410.8)--(L-91410.9) into every safe evaluation in
(L-91410.10).  Since the sum has only six poles and all integrals are
absolutely convergent after compensation, finite summation and integration may
be interchanged.

## 5. Exact completed source formula

Let

\[
 \mathfrak C_a^\lambda(x,y)
\]

be the explicit result of applying the resolvent functional
`R_(a;x,y)` to the deterministic values

\[
 Q(\sigma_r\pm it)=-\lambda_{\sigma_r},
 \qquad
 Q'(\sigma_r\pm it)=-\lambda_{\sigma_r}'.
\tag{L-91410.12}
\]

For each `u>0`, let

\[
 \mathfrak K_{a;x,y}(u)
\]

be the same resolvent functional applied to the elementary safe kernels

\[
 -e^{-rau}
  \left(e^{\mp itu}-\mathbf1_{u\le1/2}\right)
\tag{L-91410.13}
\]

in the `Q` slots and

\[
 u e^{-rau}
  \left(e^{\mp itu}-\mathbf1_{u\le1/2}\right)
\tag{L-91410.14}
\]

in the `Q'` slots, with the signs and carrier arguments dictated by
(L-91407.12).

Then

\[
 \boxed{
 \mathfrak W_a(x,y)
 =\mathfrak C_a^\lambda(x,y)
  +\int_0^\infty
   \mathfrak K_{a;x,y}(u)d\mathfrak M(u).
 }
\tag{L-91410.15}
\]

Every term is explicit.  The first is a finite deterministic connection
kernel; the second is one signed source integral over a scale-independent
measure.

## 6. Prime atoms recover the full Green kernel

Every prime atom satisfies

\[
 u=\log n\ge\log2>\frac12.
\]

Hence the compensation in (L-91410.13)--(L-91410.14) vanishes on the atomic
part.  Substituting the residue expansion of `Psi_a` and collecting the six
safe-scale terms gives exactly

\[
 \boxed{
 \mathfrak K_{a;x,y}(u)
 =-\left[
  k_{a;x,y}(u)+k_{a;x,y}(-u)
 \right]
 \quad\text{on the prime atomic support}.
 }
\tag{L-91410.16}

Therefore the atomic part of (L-91410.15) is the full independent-carrier prime
block of `L-91405`, and its delayed two-sided-plus-bridge extension is the
source of `L-91409`.

This proves that the quasi-Lévy completed source and the prime Wick--Green
source are not separate ansatzes: they are the continuous and atomic pieces of
one base measure.

## 7. Positive-metric reading

Using (L-91410.7),

\[
\boxed{
\begin{aligned}
 \mathfrak W_a(x,y)
 ={}&\mathfrak C_a^\lambda(x,y)\\
 &+\int\mathfrak K_{a;x,y}(u)d\mathfrak M^+(u)\\
 &-\int\mathfrak K_{a;x,y}(u)d\mathfrak M^-(u).
\end{aligned}}
\tag{L-91410.17}
\]

Both integration spaces have positive metric.  All indefiniteness is now
localized to:

```text
the explicit minus sign of the long-jump channel;
the deterministic connection kernel C_lambda.
```

On finite packets, any Gram factorization of the elementary kernel
`K_(a;x,y)(u)` gives a positive two-channel Hilbert realization with the sign
stored in the observation, exactly as in `L-91402`.

## 8. Delays, orientations, and bridge

The prime atomic part already has the complete delayed two-sided-plus-bridge
factorization of `L-91409`.  The continuous kernels use the same exponential
modes and the same support geometry; replacing the atomic measure `Pi` by the
positive continuous measures `M_plus_cont` and `M_minus` in the mode-split
source spaces gives the corresponding continuous source maps whenever the
compensation term is included.

The remaining bookkeeping is finite and explicit:

```text
insert the compensated short-jump source;
insert the long-jump source with negative observation sign;
insert the deterministic connection;
match the bridge normalization.
```

No prime or zero sum remains.

## 9. Correct remaining theorem

The completed source lock is now exact at the full-carrier level.  To prove the
corrected delayed screw Gram positive, it remains to:

1. factor the compensated elementary kernel `K_(a;x,y)(u)` on the full delayed
   two-sided-plus-bridge packet;
2. prove that the positive `M_plus` production and Julia reserves dominate the
   negative `M_minus` channel and the connection Schur complement with
   coefficient one.

This is an explicit long-jump/connection domination problem in positive
Hilbert spaces.

## 10. Exact boundary

```text
scale-independent completed base measure M           EXACT
prime atoms as direct summand of M_plus               EXACT
one-sign-change continuous Jordan split               EXACT
safe complex xi'/xi representation                    EXACT
safe derivative representation                        EXACT
full independent-carrier completed source formula     EXACT
prime Green kernel recovered on atomic support        EXACT
all indefiniteness localized to long jumps + connection EXACT
full compensated delayed source factorization         OPEN
positive-channel domination                           OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```
