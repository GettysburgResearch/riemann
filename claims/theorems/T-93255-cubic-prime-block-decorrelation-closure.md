# T-93255 — Cubic Prime-Block Decorrelation is a candidate-complete closure theorem

Claim ID: `T-93255`  
Status: **FULL CLOSURE INTERFACE / OPEN UNCONDITIONAL PRODUCER — RH UNPROVED**  
Created: 2026-08-15  
Depends on: `T-93251`, `L-93252`, `T-93253`, `R-93254`  
Scope: one explicit arithmetic estimate with all source, normalization, interpolation, and pole interfaces closed; the estimate itself is not proved here

## 1. The producer statement

For the exact cubic prime blocks

\[
 Z_{p,N}
 =\sum_{m\le N}c_{\circ,p}(m)
  {m\over N}\left(1-{m\over N}\right)
  {2m/N-1\over3},
\tag{T-93255.1}
\]

define

\[
 \operatorname{CPBD}(N)
 =\left|\sum_{p\le N}Z_{p,N}\right|^2.
\tag{T-93255.2}
\]

The proposed **Cubic Prime-Block Decorrelation theorem** is:

> There exist fixed constants \(B,C>0\) such that for every integer
> \(N\ge2\),
> \[
> \boxed{
> \operatorname{CPBD}(N)
> \le C N(\log(2N))^B.
> }
> \tag{T-93255.3}
> \]

The same-prime baseline is already

\[
 \sum_p|Z_{p,N}|^2
 \le {20\over243}N\log(2N).
\tag{T-93255.4}
\]

Thus (T-93255.3) asks only for a polylogarithmic loss over the complete prime-tower diagonal.

## 2. CPBD implies RH

By `L-93252.3`,

\[
 \sum_pZ_{p,N}=\mathcal A_\circ(N).
\]

Therefore (T-93255.3) gives

\[
 \mathcal A_\circ(N)
 \ll\sqrt N(\log(2N))^{B/2}.
\tag{T-93255.5}
\]

The endpoint interpolation and exact zero-safe Mellin transform of
`L-93250` then exclude every zero with real part greater than \(1/2\).
Functional-equation symmetry yields RH.

No endpoint mean, macroscopic Selberg estimate, QIDR recurrence, factor-67 root allocation, or unreviewed PIG-to-pole adapter is used.

## 3. RH implies CPBD

Under RH, the von Koch estimate gives

\[
 C_\circ(x)\ll\sqrt x\log^2(2x).
\]

Summation by parts in `L-93250.16`, using \(K(0)=K(1)=0\) and
\(\|K'\|_\infty\le1/3\), therefore gives

\[
 \mathcal A_\circ(N)
 \ll\sqrt N\log^2(2N).
\tag{T-93255.6}
\]

Thus CPBD holds with \(B=4\).

Consequently,

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \operatorname{CPBD}(N)
 \ll N(\log(2N))^B
 \text{ for some fixed }B.
 }
\tag{T-93255.7}
\]

This equivalence is the intended full closure interface. It is not presented as an unconditional proof of (T-93255.3).

## 4. Equivalent producer coordinates

Relative to the proposed-complete equivalences `T-93251` and `T-93253`, a producer may prove any one of the following RH-equivalent statements:

### A. Cubic scalar form

\[
 |\mathcal A_\circ(N)|^2
 \ll N(\log N)^B.
\tag{T-93255.8}
\]

### B. Distinct-prime cubic cross form

\[
 \left|
 2\sum_{p<r}Z_{p,N}Z_{r,N}
 \right|
 \ll N(\log N)^B,
\tag{T-93255.9}
\]

because the diagonal (T-93255.4) is already safe.

### C. Mean-free Q4 major-arc form

\[
 \left|
 \mathfrak C_{\ne p}^{\,{\rm maj},0}(N)
 \right|
 \ll(\log N)^B,
\tag{T-93255.10}
\]

by `T-93253`.

### D. Independent First-Hermite producer

On the frozen First-Hermite criterion, prove the scalar nonnegative at every carrier. This is not an algebraic restatement of CPBD; it is an independent RH-equivalent producer whose remaining obstruction has the same projective normal form by `L-93252`.

## 5. Stress-tested interfaces

The composition has the following explicit firewalls:

1. **Discrete endpoint:** the second prefix is \(N-j-1\).
2. **Centering:** the Bernoulli weight has exactly zero mean.
3. **Normalization:** \(|\mathcal A|^2\le N\mathscr V/180\).
4. **Mellin multiplier:** \((s-1)/[3(s+1)(s+2)(s+3)]\) is zero-free in the open strip.
5. **Source multiplier:** \(1-4^{1-s}\) does not cancel a nontrivial zero.
6. **Real endpoints:** integer bounds extend with \(O(1)\) loss.
7. **Same-prime towers:** complete diagonal is \(O(N\log N)\).
8. **Mean:** not used.
9. **Minor arc:** not used in the cubic scalar composition and already safe in the equivalent Fourier composition.
10. **Abstract coherence:** `R-93254` forbids treating cardinality alone as the producer.

## 6. Exact remaining theorem

The sole conclusion-producing arithmetic theorem is (T-93255.3), or one of its equivalent producer forms.

The packet does not conceal that this theorem is RH-bearing. Its contribution is to reduce the two neglected architectures to an independently reconstructible, one-dimensional, complete-prime-tower decorrelation problem with no unresolved adapter after it.

## 7. Boundary

```text
centered Bernoulli/cubic source identity        PROPOSED COMPLETE
centered Q4 energy <=> RH                       PROPOSED COMPLETE
same-prime cubic diagonal O(N log N)            PROPOSED COMPLETE
mean-free sqrt-major-arc criterion              PROPOSED COMPLETE
abstract alignment-count shortcut               REFUTED
CPBD producer estimate                          OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
