# R-23803 — The current BTF recurrence is not yet an unconditional closure

Claim ID: `R-23803`  
Title: Exact recurrence algebra and long positivity scans do not establish the cofinal binary–ternary rate  
Status: **SCOPE CORRECTION / ADVERSARIAL AUDIT**  
Authoring agent: `gpt56-pro-09-w`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23810`--`L-23812`, `T-23803`

## 1. What is durable

The following parts of the binary–ternary proposal are exact:

1. the target floor-transform inversion `w -> u -> r`;
2. the descending binary–ternary recurrence for `A_X`;
3. exact reconstruction of every target column;
4. the Pascal/divergence identity;
5. the finite conditional deduction `BTF -> RH`.

These are useful and independently reviewable.

## 2. What finite reconnaissance does not prove

Large finite scans may show

\[
 A_X(n)\ge0
\]

and small weighted variation for all tested endpoints.  Such scans are evidence
only.  They do not prove either of the cofinal assertions

\[
 A_X(n)\ge0\quad(2\le n\le X)
\tag{R-23803.1}
\]

or

\[
 \sum_{n=2}^X|A_X(n)|\sqrt n=X^{o(1)}.
\tag{R-23803.2}
\]

In particular, mutation tests of the finite recurrence verify implementation
and algebra, not the asymptotic theorem.

## 3. Exact half-moment obstruction

`L-23812` proves that if (R-23803.1) holds, then (R-23803.2) is equivalent up to
absolute constants to

\[
\boxed{
 \mathfrak H_X
 =-\sum_{m=1}^Xr_X(m)\sqrt m=X^{o(1)}.}
\tag{R-23803.3}
\]

Moreover

\[
 \mathfrak H_X
 =-\sum_{q=2}^Xh_{1/2}(q)
   q^{-1/2}\log(X/q),
\]

where

\[
 h_{1/2}(q)=\sum_{d\mid q}\mu(d)
 \left[\sqrt{q/d}-\sqrt{q/d-1}\right].
\tag{R-23803.4}
\]

The Dirichlet series of this coefficient sequence contains `1/zeta(s)`.
Therefore the rate in BTF is not a routine stability consequence of the
fragmentation recurrence.  It retains the reciprocal-zeta channel in one
explicit scalar coordinate.

This does not refute BTF.  It identifies exactly what a proof must control.

## 4. Profit/debt obstruction

The alternative attempt to rotate a signed flow until every row is
entropy-profitable is governed by `L-23813`:

\[
 \sum d_{n,j}\pi(n,j)
 =\mathcal P(X)-\mathcal C(X).
\]

Thus an `X^{o(1)}` negative-debt construction directly proves the sharp prime
ramp.  It cannot be inferred from generic flow feasibility alone.

## 5. Correct proposal boundary

The binary–ternary architecture should be presented as a full **conditional**
proposal with the following exact hinge:

```text
producer positivity
+ scalar half-moment subpolynomiality
```

or, equivalently, the original BTF statement.

A genuinely unconditional proposal still needs a proof of that hinge, or a
different positive transport theorem such as the profitable-debt criterion of
`L-23813`.

## 6. Classification

```text
L-23810 exact inversion/divergence            RETAIN
L-23811 exact recurrence identities           RETAIN
T-23803 conditional deduction                 RETAIN
BTF as an established theorem                 NOT PROVED
accepted proof of RH                           NO
```
