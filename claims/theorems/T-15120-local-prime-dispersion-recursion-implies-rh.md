# T-15120 — A local prime-dispersion recursion implies RH

Claim ID: `T-15120`  
Title: One orientation-correct recurrence for the finite prime-only safe blocks gives a polynomial energy bound and the Riemann Hypothesis  
Status: **PROPOSED CONDITIONAL THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15151`, `L-15153`, `T-21502`, `L-21504`  
Scope: exact composition theorem for the repaired full-problem proposal

## 1. Finite prime-only blocks

Let `H` be the compact prime-only safe window of `T-21502` and define

\[
 Q_H^{\mathbb P}(x)
 =\sum_p{\log p\over\sqrt p}H(x-\log p).
 \tag{T-15120.1}
\]

For integer `J` beyond the fixed initial boundary, put

\[
 \boxed{
 \mathcal B_J
 =\int_J^{J+1}|Q_H^{\mathbb P}(x)|^2dx.}
 \tag{T-15120.2}
\]

Every `B_J` is a finite, nonnegative prime Gram. Split it exactly as

\[
 \mathcal B_J=\mathcal D_J+\mathcal O_J,
 \tag{T-15120.3}
\]

where `D_J` is the ordinary-prime diagonal and `O_J` is the signed balanced semiprime form of `L-21504/L-15153`.

The compact support and the elementary bound `log p<=O(J)` give

\[
 \boxed{
 0\le\mathcal D_J\le C_0(1+J)^d}
 \tag{T-15120.4}
\]

for fixed constants `C0,d` depending only on the window.

## 2. The localized dispersion recurrence

Assume there are constants `C1,A`, an index `J0`, and numbers `eta_J>=0` such that

\[
 \boxed{
 [\mathcal O_J]_+
 \le C_1(1+J)^A
 +\eta_J
  \max_{J_0\le k<J}\mathcal B_k}
 \tag{T-15120.5}
\]

for every `J>J0`, and

\[
 \boxed{
 \limsup_{J\to\infty}\eta_J<1.}
 \tag{T-15120.6}
\]

This is a statement only about the actual finite arithmetic block sequence. It is not a homogeneous inverse theorem for arbitrary vectors.

## 3. Polynomial block bound

Choose `eta<1` and `J1` so that `eta_J<=eta` for `J>=J1`. Let

\[
 M_J=\max_{J_0\le k\le J}\mathcal B_k.
\]

From (T-15120.3)--(T-15120.5),

\[
 \mathcal B_J
 \le C_2(1+J)^B+\eta M_{J-1},
 \tag{T-15120.7}
\]

where `B=max(A,d)`.

If `B_J<=M_(J-1)`, then `M_J=M_(J-1)`. Otherwise `M_J=B_J`, and since `M_(J-1)<=M_J`,

\[
 (1-\eta)M_J\le C_2(1+J)^B.
\]

After absorbing the finite initial range,

\[
 \boxed{
 \mathcal B_J\le M_J\le C_3(1+J)^B.}
 \tag{T-15120.8}
\]

Thus the cumulative prime-only energy through `X` is polynomial:

\[
 \int^{X}|Q_H^{\mathbb P}(x)|^2dx
 \le C_4(1+X)^{B+1}.
 \tag{T-15120.9}
\]

## 4. RH conclusion

`L-15151` supplies the complete Hardy-abscissa transfer for the prime-only safe signal. Polynomial growth in the logarithmic translation variable is `exp(o(X))`, so the rightmost shifted zeta-zero displacement is zero. Therefore

\[
 \boxed{
 \text{(T-15120.5)--(T-15120.6)}
 \quad\Longrightarrow\quad
 \mathrm{RH}.}
 \tag{T-15120.10}
\]

No zero expansion is used in the arithmetic recurrence. The zero-side theorem is used only after the finite prime bound has been established.

## 5. Exact finite form of the open estimate

The off-diagonal term in (T-15120.5) is explicitly

\[
 \boxed{
 \mathcal O_J
 =\sum_{p<q}
 {2\log p\log q\over\sqrt{pq}}
 K_J(\log p,\log q),}
 \tag{T-15120.11}
\]

where the sum is finite and `p/q` lies in one fixed multiplicative interval. Thus the recurrence is a signed balanced Type-II estimate with an exact piecewise-polynomial kernel.

## 6. Why this theorem survives the second-pass objections

- It does not use the false universal `SM(J)`.
- It does not identify a product-dilation channel with a ratio Gram.
- It has no continuous Hardy-averaging remainder or infinite-dimensional boundary-rank assertion.
- It measures the actual finite source sequence, not all vectors in an operator graph domain.
- The block and its lower-scale feedback use the same unweighted logarithmic energy, so there is no hidden `4^(-J)` volume mismatch.

## 7. Proof boundary

The deduction from the recurrence to RH is complete. The recurrence itself remains the load-bearing arithmetic theorem and is not proved here.