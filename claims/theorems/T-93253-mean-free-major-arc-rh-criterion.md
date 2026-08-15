# T-93253 — RH is equivalent to the nonzero distinct-prime square-root major arc

Claim ID: `T-93253`  
Status: **PROPOSED COMPLETE MEAN-FREE MAJOR-ARC CRITERION — INDEPENDENT REVIEW REQUIRED; RH UNPROVED**  
Created: 2026-08-15  
Depends on: `T-93251`; PR #483 `L-93242` at `87bd7ad2127f98b6141b4c03355556f2b95f6404`; PR #474 `L-93015` at `0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b`  
Scope: the complete centered endpoint row; removes the mean and every same-prime/minor-arc term; no estimate for the remaining distinct-prime major arc

## 1. Center every prime-base row

Let \(R_{N,p}\in\mathbb R^N\) be the complete prime-base row of PR #483 and put

\[
 m_{p,N}={1\over N}\sum_{j=0}^{N-1}R_{N,p}(j),
 \qquad
 \widetilde R_{N,p}=R_{N,p}-m_{p,N}\mathbf1.
\tag{T-93253.1}
\]

Then

\[
 R_N-M_N\mathbf1
 =\sum_{p\le N}\widetilde R_{N,p}.
\tag{T-93253.2}
\]

Define the centered prime diagonal

\[
 \widetilde D_N
 =\sum_p\|\widetilde R_{N,p}\|_2^2.
\tag{T-93253.3}
\]

Orthogonal projection decreases norm, so the sharpened tower bound of
`L-93015` gives

\[
 \boxed{
 \widetilde D_N
 \le D_N
 \le720N^2\log(2N).
 }
\tag{T-93253.4}
\]

The centered endpoint energy is therefore

\[
 \boxed{
 \mathscr V_\circ(N)
 ={\widetilde D_N\over N^2}
 +{2\over N^2}
  \sum_{p<r}
  \langle\widetilde R_{N,p},
          \widetilde R_{N,r}\rangle.
 }
\tag{T-93253.5}
\]

No zero-frequency cross term remains.

## 2. Nonzero Fourier coordinates

Let \(S_{p,N}(a)\) be the exact prime-block sine coordinate of
`L-93015`, for \(1\le a<N\), and let

\[
 d_N(a)=\min(a,N-a),
 \qquad
 K_N=\lceil\sqrt N\rceil.
\tag{T-93253.6}
\]

Centering changes only the zero Fourier coordinate. Hence the complete nonzero distinct-prime cross term is

\[
 {2\over N^3}
 \sum_{a=1}^{N-1}
 { \sum_{p<r}S_{p,N}(a)S_{r,N}(a)
  \over
   \sin^2(\pi a/N)}.
\tag{T-93253.7}
\]

Define the **mean-free distinct-prime major arc**

\[
 \boxed{
 \mathfrak C_{\ne p}^{\,{\rm maj},0}(N)
 ={2\over N^3}
 \sum_{\substack{1\le a<N\\d_N(a)<K_N}}
 { \sum_{p<r}S_{p,N}(a)S_{r,N}(a)
  \over
   \sin^2(\pi a/N)}.
 }
\tag{T-93253.8}
\]

This contains fewer than \(2\sqrt N+O(1)\) nonzero additive modes and no mean coordinate.

## 3. Everything outside the mean-free major arc is logarithmic

The exact estimates of `L-93015` give

```text
centered same-prime diagonal / N^2    <= 720 log(2N);
absolute distinct-prime minor arc     <= 744 log(2N).
```

Therefore

\[
 \boxed{
 \left|
 \mathscr V_\circ(N)
 -\mathfrak C_{\ne p}^{\,{\rm maj},0}(N)
 \right|
 \le1464\log(2N).
 }
\tag{T-93253.9}
\]

Every term omitted from (T-93253.8) is now unconditionally paid:

1. the complete mean mode;
2. the complete same-prime tower diagonal;
3. every distinct-prime mode outside the square-root major arc;
4. the four-adic correction inside the \(p=2\) block.

## 4. Mean-free RH criterion

Combining (T-93253.9) with the native centered-energy equivalence
`T-93251` gives

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \left|
 \mathfrak C_{\ne p}^{\,{\rm maj},0}(N)
 \right|
 \ll(\log(2N))^A
 \quad(N\ge2)
 }
\tag{T-93253.10}
\]

for some fixed \(A\).

Thus the prior endpoint frontier

```text
one RH-bearing mean
+ sqrt(N) nonzero major modes
```

is replaced by

```text
sqrt(N) nonzero major modes only
+ correlations between different prime bases only.
```

The zero mode is not a hidden consumer: it has been removed from both the arithmetic object and the RH implication.

## 5. Large additive moduli

For every surviving \(a\),

\[
 q={N\over(a,N)}
 \ge{N\over a}
 >\sqrt N.
\tag{T-93253.11}
\]

Hence the exact character expansion of PR #383 applies at an additive modulus exceeding the square-root scale. As already emphasized there, an imprimitive character may have smaller primitive conductor; (T-93253.11) is a statement about the reduced additive modulus only.

The final arithmetic theorem may be attacked equivalently as:

1. the nonzero Fourier correlation (T-93253.8);
2. a weighted covariance of large-additive-modulus character prime sums;
3. the centered cubic scalar of `L-93250`, which is one fixed inverse-Laplacian dual direction in the same nonconstant space.

## 6. Quantitative false-RH consequence

If a zero of real part \(\beta>1/2\) exists, then for every
\(0<\varepsilon<\beta-1/2\),

\[
 \mathfrak C_{\ne p}^{\,{\rm maj},0}(N)
 \ne
 O\left(N^{2\beta-1-2\varepsilon}\right).
\tag{T-93253.12}
\]

Indeed (T-93253.9) would transfer such a bound to
\(\mathscr V_\circ\), contradicting `T-93251.9`.

Thus a hypothetical off-line zero must be carried by a purely nonzero, distinct-prime, square-root-major-arc correlation.

## 7. Proof boundary

Closed, subject to review:

1. exact centered prime-row decomposition;
2. elimination of the mean coordinate;
3. import of the safe prime diagonal and minor-arc bounds;
4. the \(1464\log(2N)\) comparison;
5. direct mean-free equivalence with RH;
6. localization of every false-RH obstruction to nonzero distinct-prime major modes.

Open:

1. the polylogarithmic bound in (T-93253.10);
2. the corresponding character-covariance theorem;
3. RH.
