# L-105642 — Adaptive bandwidth splits crossings into source-visible and index-collar parts

Claim ID: `L-105642`  
Status: **PROVED EXACT FOR THE FIRST SIMPLE CROSSING**  
Created: 2026-08-25  
Depends on: `L-105640--L-105641`; sibling `L-106430--L-106431`  
RH status: **not assumed**

## 1. Exact source/index partition

Retain the first-crossing notation

\[
b=\alpha+i\delta,
\qquad
U=\overline{B_b}A,
\]

with `A` inner, and let `P_L` be the source-frequency cutoff to `[0,L]`.
`L-105640` proves

\[
\|H_UP_L\|_{\mathcal S_2}^2
=|A(b)|^2(1-e^{-2\delta L}),
\tag{L-105642.1}
\]

\[
\|H_UP_L^\perp\|_{\mathcal S_2}^2
=|A(b)|^2e^{-2\delta L}.
\tag{L-105642.2}
\]

The first term is visible in the source bank.  The second is the exact positive
signed-complement charge which must remain in the endpoint/index ledger.

## 2. Tunable collar dichotomy

Fix `c>0`.  Split crossings according to

\[
\delta L\ge c
\qquad\hbox{or}\qquad
0<\delta L<c.
\]

### Source-visible region

If `delta L>=c`, then

\[
\boxed{
\|H_UP_L^\perp\|_{\mathcal S_2}^2
\le e^{-2c}|A(b)|^2,
}
\tag{L-105642.3}
\]

and the source frame captures at least

\[
\boxed{
(1-e^{-2c})|A(b)|^2.
}
\tag{L-105642.4}
\]

### Microscopic endpoint collar

If `0<delta L<c`, then the zero lies in the explicit moving collar

\[
\boxed{
0<\operatorname{Im}\rho-H<{c\over L}.
}
\tag{L-105642.5}
\]

No absolute source-coverage claim is required there.  Its uncaptured charge is
retained exactly by the signed model-space complement.

Thus, for every chosen `c`, all but an `e^(-2c)` fraction of every deeper
simple crossing is moved into the source bank, while the endpoint problem is
confined to a vertical collar of width `c/L`.

## 3. Optimal moving scale

The theorem gives a precise design rule:

\[
\boxed{
L\asymp{1\over\delta}
}
\tag{L-105642.6}
\]

is the critical bandwidth for a crossing at depth `delta`.  A fixed bandwidth
cannot see first contact.  An unnecessarily much larger bandwidth is not
needed to capture a prescribed fixed fraction.

For a cofinal height parameter `T`, choosing a source bandwidth `L(T)` reduces
the non-source endpoint analysis to zeros in a collar of thickness

\[
O(1/L(T)).
\]

If the natural physical bank has `L(T)` of logarithmic size, the surviving
collar is precisely of reciprocal-logarithmic thickness.  This observation is
a scaling consequence, not a zero-density estimate.

## 4. Relation to signed Paley–Wiener tails

The absolute-coverage requirement of the former sampling programme charged
both pieces in (L-105642.1)--(L-105642.2) as errors.  The signed identity of
`L-106431` keeps their exact topological roles.  At the first anti-inner
factor, the source and complement pieces sum to the full adverse Hankel charge:

\[
\boxed{
\text{visible charge}+
\text{signed complement}
=|A(b)|^2.
}
\tag{L-105642.7}
\]

Accordingly, the correct cofinal theorem is not absolute coverage of every
near-boundary model vector.  It is a hybrid theorem:

```text
deep factors:       current/Turan source contraction;
shallow factors:    signed endpoint spectral flow;
interface:          exact exponential split exp(-2 delta L).
```

## 5. Multiple and confluent events

For a confluent factor of multiplicity `m`, the corresponding coverage is the
explicit Laguerre sum

\[
\sum_{q=0}^{m-1}
\int_0^{2\delta L}e^{-t}L_q(t)^2dt
\]

from `L-106430`.  For several distinct simultaneous factors, the exact object
is the confluent model-space sampling matrix of `L-106415`; scalar addition of
individual charges is not asserted.

## 6. Scope

This theorem does not estimate the number of Xi-prime zeros in the microscopic
collar and does not identify their signed endpoint contribution with a parent
Xi zero count.  Those are the remaining analytic/topological tasks.  It proves
the exact scale and removes absolute coverage as the wrong interface.  RH
remains unproved.
