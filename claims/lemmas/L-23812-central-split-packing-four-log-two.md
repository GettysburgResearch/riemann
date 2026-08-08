# L-23812 — Central-split packing recovers the unconditional `4 log 2` prime-ramp constant

Claim ID: `L-23812`  
Title: One explicit nonnegative balanced carry packing gives `4(log 2)sqrt(X)-O(log^2 X)` for the complete prime-power ramp  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`  
Scope: unconditional positive carry packing; no RH conclusion

## 1. Central split and target differences

For an integer endpoint `X>=3`, put

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad 2\le q\le X,
\]

and extend by `w_X(X+1)=0`.  Since `w_X` decreases on `[1,X]`, define

\[
 \boxed{d_X(n)=w_X(n)-w_X(n+1)\ge0}
 \qquad(2\le n\le X).
 \tag{L-23812.1}
\]

At row `n`, choose only the central split

\[
 j_n=\lfloor n/2\rfloor.
 \tag{L-23812.2}
\]

Let `chi_(n,j)(q)` be the atomized carry indicator of `L-23808`.

## 2. Exact feasibility

Every carry indicator is `0` or `1`, and it vanishes for `q>n`.  Therefore,
for every `2<=q<=X`,

\[
\begin{aligned}
 \sum_{n=q}^{X}d_X(n)\chi_{n,j_n}(q)
 &\le \sum_{n=q}^{X}d_X(n)\\
 &=w_X(q)-w_X(X+1)\\
 &=w_X(q).
\end{aligned}
\]

Hence

\[
 \boxed{
 d_X(n)\ge0,
 \qquad
 \sum_{n=q}^{X}d_X(n)\chi_{n,j_n}(q)
 \le q^{-1/2}\log(X/q).
 }
 \tag{L-23812.3}
\]

This is an explicit nonnegative balanced packing at every finite endpoint.  It
uses no triangular inversion, optimization, prime-number estimate, or Möbius
sign assertion.

By the exact atomized valuation identity,

\[
 \boxed{
 \sum_{p^a\le X}{\Lambda(p^a)\over\sqrt{p^a}}
 \log{X\over p^a}
 \ge
 \sum_{n=2}^{X}d_X(n)
 \log\binom n{\lfloor n/2\rfloor}.
 }
 \tag{L-23812.4}
\]

## 3. Main mass

The elementary central-binomial lower bound

\[
 \binom n{\lfloor n/2\rfloor}
 \ge {2^n\over n+1}
\]

gives

\[
 \log\binom n{\lfloor n/2\rfloor}
 \ge n\log2-\log(n+1).
 \tag{L-23812.5}
\]

Discrete summation by parts yields

\[
\begin{aligned}
 \sum_{n=2}^{X}n d_X(n)
 &=2w_X(2)+\sum_{n=3}^{X}w_X(n)\\
 &=\sum_{n=2}^{X}w_X(n)+w_X(2).
\end{aligned}
\tag{L-23812.6}
\]

The monotone integral comparison

\[
 \sum_{n=2}^{X}n^{-1/2}\log(X/n)
 =4\sqrt X+O(\log X)
 \tag{L-23812.7}
\]

therefore gives

\[
 \boxed{
 \sum_{n=2}^{X}n d_X(n)
 =4\sqrt X+O(\log X).
 }
 \tag{L-23812.8}
\]

For the logarithmic correction, another summation by parts gives

\[
\begin{aligned}
 \sum_{n=2}^{X}d_X(n)\log(n+1)
 &=w_X(2)\log3\\
 &\quad+\sum_{n=3}^{X}w_X(n)
   \log\left(1+{1\over n}\right).
\end{aligned}
\tag{L-23812.9}
\]

Since `log(1+1/n)<=1/n`,

\[
 \sum_{n=2}^{X}d_X(n)\log(n+1)
 \ll \log X+\sum_{n=3}^{X}{\log(X/n)\over n^{3/2}}
 \ll \log X.
 \tag{L-23812.10}
\]

The weaker review-safe bound `O(log^2 X)` is already more than sufficient.

Combining (L-23812.5), (L-23812.8), and (L-23812.10),

\[
 \boxed{
 \sum_{n=2}^{X}d_X(n)
 \log\binom n{\lfloor n/2\rfloor}
 \ge4(\log2)\sqrt X-O(\log X).
 }
 \tag{L-23812.11}
\]

Consequently,

\[
 \boxed{
 \sum_{p^a\le X}{\Lambda(p^a)\over\sqrt{p^a}}
 \log{X\over p^a}
 \ge4(\log2)\sqrt X-O(\log X).
 }
 \tag{L-23812.12}
\]

## 4. Interpretation

The full critical constant is `4`.  Independent central splits recover the
fraction `log 2` of that constant unconditionally.  The remaining leading debt
is therefore

\[
 \boxed{4(1-\log2)\sqrt X.}
 \tag{L-23812.13}
\]

This debt cannot come from improving the entropy of one fixed balanced split:
`log binom(n,j)<=n log2`.  It must be supplied by cross-scale reuse of carry
capacity, equivalently by Pascal circulation, endpoint-scale transport, or a
signed balanced recurrence.

Thus the theorem separates the elementary RH problem into:

```text
within-row entropy:       4 log(2) sqrt(X)  closed unconditionally;
cross-scale transport:    4(1-log(2))sqrt(X) remaining.
```

## 5. Proof boundary

Closed exactly:

- explicit nonnegative balanced coefficients;
- every finite carry-column inequality;
- the unconditional `4 log 2` prime-ramp lower bound;
- identification of the remaining leading debt.

Open:

- a cross-scale packing or signed recurrence recovering the remaining debt;
- the critical `4 sqrt(X)-X^o(1)` bound;
- RH.
