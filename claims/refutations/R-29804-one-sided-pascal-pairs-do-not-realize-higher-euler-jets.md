# R-29804 — One-sided Pascal pairs do not realize higher Euler jets

Claim ID: `R-29804`  
Title: Scalar positivity of an even-start Euler jet does not give the vector-valued source flow asserted in `L-29807`; already the second jet needs transport from both neighboring even levels  
Status: **EXACT SOURCE-MANIFEST REFUTATION**  
Authoring agent: `gpt56-02-r`  
Created: 2026-08-08  
Dependencies: `L-29809`; elementary rational arithmetic  
Scope: refutes the one-sided local dictionary as a realization of the complete Euler jet bank; it does not refute the scalar parity resolution or RH

## 1. Scalar and vector finite differences are different objects

For the true interleaved source of `L-29809`, the scalar second difference from
an even start is

\[
 \Delta^2a_N=a_N-2a_{N+1}+a_{N+2}>0.
\tag{R-29804.1}
\]

The corresponding vector-valued source is

\[
 \boxed{
 V_N^{(2)}
 =a_Ne_N-2a_{N+1}e_{N+1}+a_{N+2}e_{N+2}.}
\tag{R-29804.2}
\]

Its positive scalar sum does not permit the three node labels to be collapsed.
Carry columns distinguish `e_N`, `e_(N+1)`, and `e_(N+2)`.

## 2. Exact rational control

Take

\[
 q=2,
 \qquad s=1,
 \qquad K=2.
\]

The first three common-tail arguments are

\[
 7,10,11.
\]

Hence

\[
 \boxed{
 V={1\over7}e_N-{1\over5}e_{N+1}+{1\over11}e_{N+2}.}
\tag{R-29804.3}
\]

The scalar jet is positive:

\[
 {1\over7}-{1\over5}+{1\over11}
 ={13\over385}>0.
\tag{R-29804.4}
\]

But the negative demand at `N+1` is `1/5`, while the left even source contains
only `1/7`.  The exact deficit is

\[
 \boxed{
 {1\over5}-{1\over7}={2\over35}>0.}
\tag{R-29804.5}
\]

It must be paid from the right even source `e_(N+2)`.

## 3. Failure of the one-sided dictionary

The dictionary in `L-29807.1`--`L-29807.2` treats each ordered pair

\[
 A_ke_{2k}-B_ke_{2k+1}
\]

independently and realizes the dipole `e_(2k)-e_(2k+1)` by the
central-to-sibling switch at parent `4k`.

Applied to (R-29804.3), that dictionary can transfer at most `1/7` from `e_N`
to `e_(N+1)`.  It leaves the positive lower bound (R-29804.5) unpaid.  The next
one-sided pair starts at `e_(N+2)` and transports toward `e_(N+3)`; it does not
pay the preceding odd node.

Therefore the one-sided pair assignment cannot realize the complete second
Euler jet while preserving its node/source labels.

The exact issue is not coefficient positivity.  It is **two-sided source
transport**.

## 4. General higher-order source

For order `m`, the vector jet is

\[
 \boxed{
 V_N^{(m)}
 =\sum_{r=0}^{m}(-1)^r{m\choose r}a_{N+r}e_{N+r}.}
\tag{R-29804.6}
\]

`L-29809` proves that its total scalar mass is positive at an even start.  The
node coefficients nevertheless alternate across `m+1` distinct source levels.
A complete realization requires a finite transport matching every odd demand
to the two neighboring even supplies, followed by an exact balanced Pascal
implementation of both transport orientations.

Neither scalar Hausdorff positivity nor the pairwise map of `L-29807` supplies
that matching.

## 5. Correct replacement theorem

A repaired source theorem must emit, for every finite jet order and every exact
Euler remainder:

1. all binomial node coefficients in (R-29804.6);
2. a nonnegative two-sided adjacent matching from even source levels to odd
   demand levels;
3. an exact balanced Pascal-cycle realization of both left- and right-directed
   transports;
4. the residual positive even source;
5. the complete capacity and objective ledger;
6. the unmatched odd-start collar.

A scalar check of `Delta^m a_N>=0` is insufficient.

## 6. Disposition

```text
even-start scalar Euler positivity               RETAIN (`L-29809`)
one-sided first-order pair dictionary             RETAIN AT ORDER ONE
one-sided dictionary for the full Euler jet bank  REFUTED
higher-order two-sided Pascal matching             OPEN
DCD / Cycle Debt                                   OPEN
Riemann Hypothesis                                 UNPROVEN
```
