# L-91321 — Every monotone interval seed has a positive butterfly lift with one explicit upper boundary atom

Claim ID: `L-91321`  
Status: **PROPOSED COMPLETE EXACT FINITE BUTTERFLY-FACTORISATION THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91105`, `L-91320`  
RH status: **unproved**

## 1. Finite endpoint coefficients

Retain the positive two-node butterfly seed of `L-91105`,

\[
 \mathcal P_T=A_T\delta_{T-1}+B_T\delta_T,
 \qquad A_T,B_T>0.
\tag{L-91321.1}
\]

The same algebra extends to `T=3` by direct substitution.  The directed
standard-library checker `X-91108` proves on every endpoint level needed by one
factor-54 generation,

\[
 \boxed{
 A_T>B_T>0,
 \qquad 3\le T\le55,
 }
\tag{L-91321.2}
\]

and quantitatively

\[
 \boxed{
 \frac{B_T}{A_T}<\frac{199}{200}.
 }
\tag{L-91321.3}
\]

The least directed gap occurs at `T=55` and is still strictly positive.

## 2. One monotone parity edge

Fix

\[
 1\le e<o\le54,
 \qquad m\ge0,
\]

and define the interval seed

\[
 \boxed{
 I_{e,o}^{m}(n)=m\,\mathbf1_{e<n\le o}.
 }
\tag{L-91321.4}

This is the elementary seed attached in `L-91320` to one monotone parity edge
`e<-o`.

Use the harmless convention `B_2=0`.  Define nonnegative candidate butterfly
intensities recursively by

\[
 \eta_{e+1}=0,
\tag{L-91321.5}
\]

and, for `e+1<=n<=o`,

\[
 \boxed{
 \eta_{n+1}
 =\frac{m-B_n\eta_n}{A_{n+1}}.
 }
\tag{L-91321.6}

For `m=0` all coefficients vanish.  Assume below that `m>0` and put

\[
 x_n=\frac{B_n\eta_n}{m}.
\]

Then `x_(e+1)=0` and

\[
 \boxed{
 x_{n+1}
 =\frac{B_{n+1}}{A_{n+1}}(1-x_n).
 }
\tag{L-91321.7}

Equations (L-91321.2)--(L-91321.3) give inductively

\[
 \boxed{
 0\le x_n<\frac{199}{200}<1.
 }
\tag{L-91321.8}

Consequently every numerator in (L-91321.6) is positive and

\[
 \boxed{
 \eta_T\ge0
 \qquad(e+2\le T\le o+1).
 }
\tag{L-91321.9}

## 3. Exact seed identity

At an interior node `e+1<=n<=o`, only the butterflies centered at `n` and
`n+1` contribute.  The coefficient there is

\[
 B_n\eta_n+A_{n+1}\eta_{n+1}=m
\]

by the recurrence.  At `n=e`, the possible term is
`A_(e+1) eta_(e+1)=0`.  Above `o+1` every butterfly vanishes.

At the single upper boundary node,

\[
 \rho_{e,o}m:=B_{o+1}\eta_{o+1}
\]

satisfies

\[
 0\le\rho_{e,o}<\frac{199}{200}.
\]

Therefore

\[
 \boxed{
 \sum_{T=e+2}^{o+1}\eta_T\mathcal P_T
 =I_{e,o}^{m}
  +m\rho_{e,o}\delta_{o+1},
 \qquad
 0\le\rho_{e,o}<\frac{199}{200}.
 }
\tag{L-91321.10}

Thus every no-upward parity edge lies in the nonnegative adjacent-butterfly cone
up to one explicit positive atom immediately above its upper endpoint.

## 4. Aggregate transport

Let `pi(e,o)>=0` be any finite transport supported on `e<=o`.  Ignore diagonal
edges, which require no correction.  Apply (L-91321.10) with
`m=pi(e,o)` and sum.

Writing `I_pi` for the interval seed of `L-91320`, one obtains

\[
 \boxed{
 \sum_T\eta_T^{\pi}\mathcal P_T
 =I_\pi+\mathcal B_\pi,
 }
\tag{L-91321.11}

where

\[
 \boxed{
 \mathcal B_\pi
 =\sum_{e<o}\pi(e,o)\rho_{e,o}\delta_{o+1}
 \ge0
 }
\tag{L-91321.12}

and

\[
 \boxed{
 \|\mathcal B_\pi\|_1
 <\frac{199}{200}
  \sum_{e<o}\pi(e,o).
 }
\tag{L-91321.13}

The complete nonlocal parity correction has therefore become:

```text
nonnegative adjacent butterfly intensities;
plus one explicit positive upper-boundary measure.
```

No signed bidiagonal inversion remains in the interior.

## 5. Score and inherited bulk

Every butterfly preserves the two inherited endpoint moments and is supported
on four moving rows.  Therefore the left side of (L-91321.11) leaves the entire
deep inherited bulk unchanged.

Its exact score gain is

\[
 \sum_T\eta_T^\pi E_T,
\]

where `L-91105` gives

\[
 E_T=A_T\log\frac{T-1}{T-2}
     +B_T\log\frac T{T-1}>0.
\]

Hence

\[
 \boxed{
 \sum_T\eta_T^\pi E_T\ge0.
 }
\tag{L-91321.14}

The interval-seed lift is automatically score-favorable.

## 6. Exact divisor and detail interpretation

`L-91320` already proves that `I_pi` has the exact divisor and radix-four
responses of the matched odd-minus-even parity transport.  Equation
(L-91321.11) now realizes that seed through the actual compact endpoint
butterfly packets, with only the response of the explicit positive boundary
measure `B_pi` left over.

Because `B_pi` is supported at the single-step nodes `o+1<=55`, it is a finite
boundary channel rather than a new rough renewal.  It must be combined with the
unspent balanced even capacity, the positive complementary reserve
`(2-kappa_*)R`, and the decaying boundary port of `L-91315`.

## 7. What remains load bearing

A butterfly is a signed perturbation of the resident endpoint weights even
though its seed is positive.  The present theorem does not prove that the total
negative center intensity is bounded by the baseline outer endpoint packing.
Nor does it prove that `B_pi` fits in the remaining column capacities.

The exact remaining finite gate is now:

> Couple the nonnegative butterfly intensity vector in (L-91321.11) with the
> resident outer endpoint weights so that every final endpoint coefficient is
> nonnegative, and absorb the explicit positive boundary measure through the
> complementary reserve and boundary-port ledger.

This is strictly smaller than constructing an arbitrary endpoint inverse of the
interval seed.

## 8. Verification

The companion checker uses directed `Fraction`, square-root and logarithm
intervals. It certifies

```text
A_T>B_T>0 for T=3,...,55;
B_T/A_T<199/200;
all 1,431 monotone local edges;
the positivity induction for 26,235 recurrence steps.
```

Retained verdict:

```text
PASS_INTERVAL_SEED_POSITIVE_BUTTERFLY_LIFT
```

## 9. Proof boundary

```text
finite A_T>B_T>0 hierarchy                         DIRECTED EXACT
positive recurrence for every monotone edge         EXACT
interval seed + one positive boundary atom          EXACT
aggregate positive butterfly factorization          EXACT
moment cancellation and favorable score             EXACT
baseline endpoint-weight compatibility              OPEN
positive boundary-atom capacity allocation          OPEN
coefficient-one rough-prime reset                    OPEN / RH-BEARING
Riemann Hypothesis                                   UNPROVED
```
