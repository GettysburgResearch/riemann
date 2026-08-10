# L-32410 — The true Q=4 real-X collar is one raw coefficient

Claim ID: `L-32410`  
Status: **PROPOSED COMPLETE EXACT COLLAR THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: corrected `L-32407`; `R-32403`; elementary floor arithmetic

## 1. True interval-kernel field

Let

\[
 G_4(y)=\sum_{m\le y}c_4(m),
 \qquad c_4=e_4*\Lambda_4.
\]

The unnormalized physical field is

\[
 \boxed{
 \mathcal Q_4(X,\theta)
 =G_4(X)-G_4(\theta X)-G_4((1-\theta)X).
 }
 \tag{L-32410.1}
\]

This is the inverse transform of `E_4L_4N_theta` and contains no extra floor transform.

Fix real `X` and put

\[
 N=\lfloor X\rfloor,
 \qquad
 j=\lfloor\theta X\rfloor,
 \qquad
 k=\lfloor(1-\theta)X\rfloor.
\]

Because `theta X+(1-theta)X=X`,

\[
 \boxed{j+k\in\{N-1,N\}.}
 \tag{L-32410.2}
\]

## 2. Exact collar formula

If `j+k=N`, then

\[
 \boxed{
 \mathcal Q_4(X,\theta)=Q_4^{\rm phys}(N,j).
 }
 \tag{L-32410.3}
\]

If `j+k=N-1`, then `N-j=k+1`, so

\[
\begin{aligned}
 \mathcal Q_4(X,\theta)
 &=G_4(N)-G_4(j)-G_4(k)\\
 &=Q_4^{\rm phys}(N,j)+G_4(k+1)-G_4(k).
\end{aligned}
\]

Hence

\[
 \boxed{
 \mathcal Q_4(X,\theta)
 =Q_4^{\rm phys}(N,j)+\epsilon c_4(k+1),
 \qquad\epsilon\in\{0,1\}.
 }
 \tag{L-32410.4}
\]

Thus the complete between-integer collar is one raw physical coefficient.

## 3. Uniform logarithmic collar size

The exact coefficient law in `L-32407` gives, for every `m>=2`,

\[
 \boxed{|c_4(m)|\le5\log(2m).}
 \tag{L-32410.5}
\]

Indeed:

- `c_4(p^a)=log p<=log m`;
- `c_4(4^r p^a)=-3log p`, so the absolute value is at most `3log m`;
- mixed `2*4^r*p^a` coefficients vanish;
- on `m=2^(2r)`, `(3r+4)log2 <= (3/2)log m+4log2 <5log(2m)`;
- on `m=2^(2r+1)`, `|1-3r|log2< (3/2)log m+log2 <5log(2m)`.

Hence the collar correction is `O(log X)` pointwise and `O(log^2 X/X)` after critical square normalization.

## 4. Continuous balanced transference

Restrict to

\[
 \frac13\le\theta\le\frac23,
 \qquad X\ge12.
\]

Then the integer row `j=floor(theta X)` lies in the quarter-balanced cone for `N=floor X`, so corrected `L-32407` applies. By (L-32410.4), (L-32410.5), and `(a+b)^2<=2a^2+2b^2`,

\[
 \boxed{
 |\mathcal Q_4(X,\theta)|^2
 \le88000\,\mathcal R_4(N,j)
 +50\log^2(2X).
 }
 \tag{L-32410.6}
\]

After physical normalization,

\[
 \boxed{
 |\mathfrak P_{4,\theta}(\log X)|^2
 \le\frac{88000}{X}\mathcal R_4(N,j)
 +\frac{50}{X}\log^2(2X).
 }
 \tag{L-32410.7}
\]

As `theta` varies, each value of `j` occupies an interval of length at most `1/X`. Therefore

\[
 \boxed{
 \int_{1/3}^{2/3}|\mathfrak P_{4,\theta}(\log X)|^2d\theta
 \le\frac{88000}{X^2}
 \sum_{j\in\mathcal B_X}\mathcal R_4(N,j)
 +O\!\left(\frac{\log^2(2X)}X\right).
 }
 \tag{L-32410.8}
\]

The continuous collar is therefore completely explicit and smaller than the previous extra-floor estimate.

## 5. Proof boundary

Closed exactly:

1. the real-parent floor reduction for the correctly typed interval field;
2. the one-bit dichotomy `j+k=N` or `N-1`;
3. the one-raw-coefficient collar formula;
4. a uniform logarithmic coefficient bound;
5. continuous balanced physical-to-reserve transference.

Open:

1. reflected reserve accounting/no-double-spend in the complete independent-frequency identity;
2. propagation of the explicit unitary scattering state;
3. RH.
