# L-102747 — Pair-owner multiplicity costs only a squared logarithm

Claim ID: `L-102747`  
Status: **PROVED EXACT OCCUPANCY REDUCTION**  
Created: 2026-08-23  
Depends on: `L-102746`; `L-102702--L-102705`  
RH status: **not assumed**

Retain the unordered owner-pair coordinate supplied by `L-102746` until after
all equal physical products have been combined.

Let one labelled squarefree occurrence have depth

\[
 k=\omega_{\rm lab}(n).
\]

The two labelled copies of \(67\) count separately.  The occurrence has exactly

\[
 \binom{k}{2}
\]

unordered owner-pair coordinates, and each coordinate carries the fraction
\(1/\binom{k}{2}\) of the same source coefficient.

## 1. Same-occurrence collapse

Let \(v_{n,P}\) be the physical vector belonging to owner pair \(P\).  Before
collapse, the canonical allocation gives

\[
 v_{n,P}=\binom{k}{2}^{-1}v_n.
\]

Therefore

\[
 \sum_P\|v_{n,P}\|^2
 =\binom{k}{2}^{-1}\|v_n\|^2,
\]

while

\[
 \left\|\sum_Pv_{n,P}\right\|^2=\|v_n\|^2.
\]

The exact collapse factor is consequently \(\binom{k}{2}\), not the square of
that number.

On a physical horizon \(n\le16Y\),

\[
 k\le\frac{\log(16Y)}{\log2}+1,
\]

where the extra one accommodates the second labelled copy of \(67\).  Hence

\[
 \boxed{
 \binom{k}{2}\ll(\log(2Y))^2.
 }
 \tag{L-102747.1}
\]

Thus same-occurrence pair-owner collapse is polylogarithmic.

## 2. Same-product factor pairs

Different half-divisor or Wick factorizations of the same integer are already
controlled by `L-102702` and `L-102704`: the source diagonal is subpower and,
after square-root completion, the owner/core representation is injective.
Combining those results with (L-102747.1) gives

\[
 \boxed{
 \text{all equal-product pair-owner multiplicity is }Y^{o(1)}.
 }
 \tag{L-102747.2}
\]

## 3. What remains

After this theorem, the physical restriction no longer contains:

```text
root coordinates;
first chaos;
prime-square pair diagonals;
duplicate owner representations;
multiple pair owners of one occurrence;
multiple factor pairs of one integer;
same-owner square-core overlap.
```

Only correlations between **different integer products** assigned to
different unordered prime pairs remain.
