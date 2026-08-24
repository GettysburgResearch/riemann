# L-102903 — Sparse endpoint gauges give unique critical-prime placement

Claim ID: `L-102903`  
Status: **PROVED EXACT LOCAL PLACEMENT AND SOURCE-PARTITION THEOREM**  
Created: 2026-08-25  
Depends on: `L-102901--L-102902`; owner and discrepancy partitions on PR #719  
RH status: **not assumed**

At one labelled prime put

\[
E(x)=1-x,
\qquad
C(x)=1-x^2,
\qquad
T(x)=E(x)C(x)=1-x-x^2+x^3.
\]

The endpoint temperatures in `L-102901` are

```text
t=0:  left factor E, right factor C;
t=1:  left factor C, right factor E.
```

## 1. Unique local split

At `t=0`, every exponent of the target has one and only one allocation:

\[
\begin{array}{c|c}
\text{target exponent}&(\text{left exponent},\text{right exponent})\\
\hline
0&(0,0)\\
1&(1,0)\\
2&(0,2)\\
3&(1,2).
\end{array}
\]

At `t=1` the two coordinates are reversed. Thus the unsquared occurrence of
this prime belongs to exactly one factor, and its squared occurrence belongs
to the complementary factor. No coefficient is split between two owner
histories.

## 2. Source-owned endpoint placement

On one dyadic physical horizon, let `S` be any source-defined set of labels,
for example:

```text
the selected Wick owner pair;
the largest discrepancy prime of a reduced core;
the finite set of activation or boundary labels;
the unique horizon-exceptional label.
```

Choose `t_p=0` or `1` on `S` according to the desired physical side, and keep
`t_p=1/2` for every unselected core prime. By `L-102901`, the product source is
still exactly `Gamma_(1/2)`. By `L-102902`, the change in labelled tensor
energy is at most polylogarithmic.

The choice is made from one source occurrence before additive phases, Cauchy,
physical collapse, or a negative part. Therefore the same critical prime may
not be placed independently in two regions.

## 3. Consequence for the stopped-current coordinate

All distinguished owner and discrepancy primes may be put at endpoint
temperatures. Their unsquared half-order activity is then carried on one
specified factor and their square activity on the other. The only labels that
remain genuinely midpoint-polarized are the undistinguished core primes.

This removes the factor-assignment ambiguity from `SGIC102890`: external owner
phases, internal discrepancy phases, and owner/core renewals can be performed
on factors whose critical labels have unique placement.

## Scope firewall

Unique placement does not orient the remaining core product. The midpoint core
still contains the detector-bearing cancellation, and the two complementary
factors must be recombined before applying a negative part. This theorem is a
normal form for the live arithmetic frontier, not a proof of it.
