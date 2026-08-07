# L-24521 — Colossally abundant numbers are prefixes of an exact prime-exponent slope ledger

Claim ID: `L-24521`  
Status: `PROPOSED — complete elementary optimization lemma`  
Scope: Lagarias/Robin colossally abundant localization  
Issue: #245

For a prime `p` and exponent `a>=0`, put

\[
R_{p,a}=\frac{\sigma(p^a)}{p^a}
=\frac{1-p^{-a-1}}{1-p^{-1}}.
\tag{L-24521.1}
\]

Increasing the exponent from `a` to `a+1` multiplies the normalized divisor
ratio by

\[
\boxed{
I_{p,a}
=\frac{R_{p,a+1}}{R_{p,a}}
=\frac{1-p^{-a-2}}{1-p^{-a-1}}.
}
\tag{L-24521.2}
\]

Define the increment slope

\[
\boxed{
\kappa_{p,a}
=\frac{\log I_{p,a}}{\log p}.
}
\tag{L-24521.3}
\]

## 1. Independent prime optimization

Fix `epsilon>0`. For

\[
n=\prod_pp^{a_p},
\]

one has

\[
\frac{\sigma(n)}{n^{1+\epsilon}}
=\prod_p\left(R_{p,a_p}p^{-\epsilon a_p}\right).
\tag{L-24521.4}
\]

The choice of `a_p` is independent for each prime. The ratio obtained by
increasing `a` to `a+1` is

\[
I_{p,a}p^{-\epsilon}.
\]

Therefore an exponent increment is favorable exactly when

\[
\boxed{\kappa_{p,a}>\epsilon,}
\tag{L-24521.5}
\]

unfavorable when the inequality is reversed, and tied at equality.

For fixed `p`, the slopes `kappa_(p,a)` decrease strictly with `a`, so favorable
increments automatically form an initial exponent segment.

## 2. Prefix description

Form the countable item set

\[
\mathscr I=\{(p,a):p\text{ prime},\ a\ge0\},
\]

where item `(p,a)` has weight and value

\[
x_{p,a}=\log p,
\qquad
y_{p,a}=\log I_{p,a}.
\tag{L-24521.6}
\]

Order the items by decreasing ratio `y/x=kappa`. For a threshold `epsilon`,
include every item with slope greater than `epsilon`, exclude every item with
smaller slope, and make an arbitrary tie choice at equality. The resulting
integer is exactly a maximizer of `sigma(n)/n^(1+epsilon)`.

Conversely every colossally abundant number arises from such a threshold and a
tie choice. Hence

\[
\boxed{
\text{colossally abundant numbers are slope prefixes of }\mathscr I.
}
\tag{L-24521.7}
\]

No prime asymptotic enters this statement.

## 3. Exact cumulative ledger

For a finite prefix `P`, define

\[
X(P)=\sum_{(p,a)\in P}\log p,
\qquad
Y(P)=\sum_{(p,a)\in P}\log I_{p,a}.
\tag{L-24521.8}
\]

Then the associated colossally abundant integer satisfies

\[
\boxed{
\log n=X(P),
\qquad
\log\frac{\sigma(n)}n=Y(P).
}
\tag{L-24521.9}
\]

Thus Lagarias's inequality on the CA sequence is the explicit prefix inequality

\[
\boxed{
Y(P)
\le
\log\left(
\frac{H_{e^{X(P)}}+e^{H_{e^{X(P)}}}\log H_{e^{X(P)}}}{e^{X(P)}}
\right),
}
\tag{L-24521.10}
\]

with the integer argument interpreted as the exact product encoded by the
prefix, not by numerical exponentiation.

## 4. Prime-power asymptotic coordinate

Writing `q=p^{a+1}`, one has

\[
\log I_{p,a}
=\log\left(1+\frac{(1-p^{-1})q^{-1}}{1-q^{-1}}ight).
\tag{L-24521.11}
\]

Therefore

\[
\boxed{
\kappa_{p,a}
=\frac{1-p^{-1}}{q\log p}
+O\left(\frac1{q^2\log p}\right).
}
\tag{L-24521.12}
\]

The CA threshold is consequently organized by the same prime-power scale
`q log p` that appears in the carry, Selberg, and prime-ramp packets.

## 5. Use of the Lagarias import

Lagarias, through Robin's theorems, localizes any failure of his harmonic
inequality to the colossally abundant sequence. Equation (L-24521.7) turns that
localization into a completely explicit sorted finite ledger. A proof can now
target prefix increments rather than arbitrary integers.

This does not make the prefix inequality automatic. The cumulative discrepancy
between the prime-exponent slope count and the harmonic envelope retains the RH
burden.

## Dependency boundary

The slope-prefix lemma is elementary. The statement that checking the relevant
CA sequence suffices for the global RH equivalence is imported from the
Lagarias/Robin chain recorded in `T-24502`.

## Status boundary

This lemma proves the finite optimization structure. It does not prove the
Lagarias prefix inequality or RH.
