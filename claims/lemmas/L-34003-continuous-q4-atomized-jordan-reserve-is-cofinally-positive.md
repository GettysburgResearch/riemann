# L-34003 — The continuous Q=4 atomized Jordan reserve is cofinally positive

Claim ID: `L-34003`  
Title: After the exact physical/carry identification, the source-complete augmented Q=4 Kummer--Jordan reserve is uniformly positive on the full continuous balanced carry-position bank  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Parent: PR #341  
Dependencies: `L-34001`; PR #325 `L-32405`; PR #337 `L-32706/L-32711`; elementary factorial bounds  
Scope: complete continuous carry-position reserve; no global neutral-mode recurrence or RH conclusion

## 1. Continuous atomized row

Fix real `X>=1` and `theta in [0,1]`. Put

\[
 \mathcal C_d(X,\theta)
 =\left\lfloor\frac Xd\right\rfloor
  -\left\lfloor\frac{\theta X}{d}\right\rfloor
  -\left\lfloor\frac{(1-\theta)X}{d}\right\rfloor
 \in\{0,1\}.
\tag{L-34003.1}
\]

Retain the Q=4 source/Jordan coefficients

\[
 b_4,\qquad q_4=b_4*\Lambda_4,\qquad
 t_4=b_4*C_4,
\]

and define the continuous carry-position quantities

\[
 Y=\sum_{d\le X}b_4(d)\mathcal C_d,
 \qquad
 Q=\sum_{d\le X}q_4(d)\mathcal C_d,
 \qquad
 T=\sum_{d\le X}t_4(d)\mathcal C_d,
\tag{L-34003.2}
\]

\[
 P=\sum_{d\le X}\Lambda_4(d)\mathcal C_d,
 \qquad
 S=\sum_{d\le X}C_4(d)\mathcal C_d.
\tag{L-34003.3}
\]

By `L-34001`, `Y,Q,T` are exactly the zeroth, first, and second physical Jordan jets at the real point `(X,theta)`.

Define

\[
 \boxed{
 \mathcal A(X,\theta)
 =P^2-S+Q^2-YT.
 }
\tag{L-34003.4}
\]

This is the continuous analogue of the augmented reserve in PR #337 `L-32711`.

## 2. Exact floor reduction

Put

\[
 N=\lfloor X\rfloor,
 \qquad J=\lfloor\theta X\rfloor,
 \qquad K=\lfloor(1-\theta)X\rfloor.
\tag{L-34003.5}
\]

Since the three fractional parts sum to the fractional part of `X` modulo one,

\[
 \boxed{J+K\in\{N-1,N\}.}
\tag{L-34003.6]
\]

Moreover, for every integer `d>=1`, adding a fractional part smaller than one cannot cross the next multiple of `d`, so

\[
 \left\lfloor\frac Xd\right\rfloor=\left\lfloor\frac Nd\right\rfloor,
\]

and similarly for `theta X` and `(1-theta)X`. Hence

\[
 \boxed{
 \mathcal C_d(X,\theta)
 =\left\lfloor\frac Nd\right\rfloor
  -\left\lfloor\frac Jd\right\rfloor
  -\left\lfloor\frac Kd\right\rfloor.
 }
\tag{L-34003.7]
\]

(The closing square brackets in tags `L-34003.6]` and `L-34003.7]` are typographical only.)

Thus the real carry-position bank is an exact integer floor-defect bank with either zero or one missing unit in the child sum.

## 3. Linear lower bound for the generalized Kummer coordinate

Because `Lambda_4>=Lambda` coefficientwise and every `mathcal C_d` is nonnegative,

\[
 P\ge\sum_{d\le X}\Lambda(d)\mathcal C_d.
\tag{L-34003.8]
\]

The factorial identity

\[
 \sum_{d\le M}\Lambda(d)\left\lfloor\frac Md\right\rfloor
 =\log(M!)
\]

therefore gives

\[
 \boxed{
 P\ge\log(N!)-\log(J!)-\log(K!).
 }
\tag{L-34003.9]
\]

If `J+K=N`, the right side is `log binom(N,J)`. If `J+K=N-1`, it is

\[
 \log\left[N\binom{N-1}{J}\right].
\]

Fix any `eta in (0,1/2)`. On

\[
 eta\le\theta\le1-eta,
\]

both `J` and `K` are at least `eta N/2` for all sufficiently large `N`. The elementary product bound

\[
 \binom mr\ge2^{\min(r,m-r)}
\]

then yields a constant `c_eta>0` and a finite threshold such that

\[
 \boxed{P(X,\theta)\ge c_\eta X}
\tag{L-34003.10]
\]

uniformly on the balanced bank. For the concrete interval `[1/3,2/3]`, one may take for example `c_eta=(log2)/5` after enlarging the finite threshold.

## 4. Complete Selberg forcing is only `O(X log X)`

Since `C_4(d)>=0` and `0<=mathcal C_d<=1`,

\[
 0\le S(X,\theta)\le\sum_{d\le X}C_4(d).
\]

The elementary generalized-prime mass estimate already used in the Q=4 reserve proofs gives

\[
 \boxed{
 \sum_{d\le X}C_4(d)
 \ll X\log(2X).
 }
\tag{L-34003.11]
\]

Thus

\[
 \boxed{S(X,\theta)=O(X\log(2X))}
\tag{L-34003.12]
\]

uniformly in `theta`.

## 5. The unweighted source is logarithmic

Because `1*b_4=e_4`, the general prefix/carry identity `L-34001` gives

\[
 Y(X,\theta)
 =E_4(N)-E_4(J)-E_4(K),
\]

where

\[
 E_4(M)=\sum_{m\le M}e_4(m)
 =1-3\lfloor\log_4M\rfloor
\]

for `M>=1` (and `E_4(0)=0`). Hence

\[
 \boxed{|Y(X,\theta)|\ll\log(2X).}
\tag{L-34003.13]
\]

uniformly in the complete carry-position bank.

## 6. The second source current has polynomial-logarithmic mass

PR #337 `L-32711` proves an absolute coefficient bound of the form

\[
 \sum_{d\le X}|t_4(d)|
 \ll X\log^4(2X).
\tag{L-34003.14]
\]

Since `|mathcal C_d|<=1`,

\[
 \boxed{|T(X,\theta)|\ll X\log^4(2X).}
\tag{L-34003.15]
\]

Therefore

\[
 \boxed{|Y(X,\theta)T(X,\theta)|
 \ll X\log^5(2X)=o(X^2).}
\tag{L-34003.16]
\]

uniformly in `theta`.

## 7. Cofinal positivity with a quadratic reserve

The first-current square `Q^2` is nonnegative and may be discarded in a lower bound. Combining (L-34003.10), (L-34003.12), and (L-34003.16) gives

\[
\begin{aligned}
 \mathcal A(X,\theta)
 &\ge P(X,\theta)^2-S(X,\theta)-|Y(X,\theta)T(X,\theta)|\\
 &\ge c_\eta^2X^2-O(X\log^5(2X)).
\end{aligned}
\tag{L-34003.17]

Consequently there are `X_eta<infinity` and `c'_eta>0` such that

\[
 \boxed{
 \mathcal A(X,\theta)\ge c'_\eta X^2
 }
\tag{L-34003.18]
\]

for every `X>=X_eta` and every `theta in [eta,1-eta]`.

Thus the source-complete Q=4 augmented reserve is uniformly and quadratically positive on the **actual continuous physical carry-position bank**. No row-measure approximation or integer-grid transference theorem is needed.

## 8. Integrated physical form

For any fixed balanced interval `I=[eta,1-eta]`, integrate (L-34003.18):

\[
 \boxed{
 \int_I\mathcal A(X,\theta)d\theta
 \ge |I|c'_\eta X^2.
 }
\tag{L-34003.19]
\]

By `L-34001`, the `Y,Q,T` terms in this integral are exactly the physical Jordan source jets, and their complete quadratic block is the exact atomized carry Gram. Therefore the previously open phrase

```text
source-convolved physical block -> carry reserve placement
```

is closed at the level of the complete augmented Jordan reserve.

## 9. Interaction with the PNT current estimate

`L-34002` additionally proves

\[
 Q(X,\theta)=o(X)
\]

uniformly on every fixed balanced interval. Hence, for every fixed `M>0`,

\[
 Q^2+M Y^2=o(X^2)
\]

uniformly there. The cofinal reserve (L-34003.18) therefore has arbitrarily large relative slack after paying any fixed weighting of the true pole current and unweighted source.

This is stronger than the former integer-row source-placement statement, but it still does not by itself control the neutral principal mode globally in logarithmic time.

## 10. Proof boundary

Closed unconditionally, subject to review:

1. exact real-X floor reduction;
2. linear generalized-Kummer lower bound on every fixed balanced interval;
3. complete `O(X log X)` Selberg forcing bound;
4. logarithmic unweighted-source bound;
5. `O(X log^4 X)` second-current bound;
6. uniform quadratic positivity of the complete continuous augmented Jordan reserve;
7. direct integrated physical/carry placement of that reserve.

Still open:

1. the coefficient-one neutral-mode block recurrence in logarithmic time;
2. a proof that the reflected block spends this reserve with the required sign and no current-scale return besides the declared neutral state;
3. RH.
