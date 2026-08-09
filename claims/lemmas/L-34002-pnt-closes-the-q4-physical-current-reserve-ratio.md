# L-34002 — PNT closes the Q=4 physical-current / reserve ratio

Claim ID: `L-34002`  
Title: The exact four-adic source renewal plus the ordinary prime number theorem gives uniform `o(1)` physical-current energy relative to the Q=4 balanced Kummer reserve  
Status: **PROPOSED COMPLETE UNCONDITIONAL ASYMPTOTIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Parent: PR #339 / repair of the dependency used by PR #325 `L-32413`  
Dependencies: PR #325 `L-32412`, `L-32405`; the classical prime number theorem  
Scope: balanced integer rows and their real-X one-coefficient collar; no reflected block recurrence or RH conclusion

## 1. The missing dependency

PR #325 `L-32413` uses the limit

\[
 \sup_{n/4\le j\le3n/4}
 \frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
 \longrightarrow0.
\tag{L-34002.1}
\]

Its displayed dependency points to `L-32412`, but the current `L-32412` is the exact four-adic renewal theorem and does not itself state or prove (L-34002.1). The limit is nevertheless unconditional and follows from that renewal plus PNT.

## 2. Exact renewal for the physical prefix

Retain

\[
 G_4(X)=\sum_{m\le X}c_4(m)
\]

and the exact identity of `L-32412`

\[
 \boxed{
 G_4(X)=G_4(X/4)+H_4(X),
 }
\tag{L-34002.2}
\]

where

\[
 \boxed{
 H_4(X)=\psi(X)-4\psi(X/4)
       +3\lfloor\log_4X\rfloor\log4.
 }
\tag{L-34002.3}
\]

The ordinary prime number theorem gives

\[
 \psi(x)=x+o(x).
\]

Hence

\[
 \psi(X)-4\psi(X/4)=o(X),
\]

while the last term in (L-34002.3) is `O(log X)=o(X)`. Therefore

\[
 \boxed{H_4(X)=o(X).}
\tag{L-34002.4}
\]

## 3. The complete Q=4 prefix is `o(X)`

Iterating (L-34002.2) until the argument falls below one gives a finite geometric-scale expansion

\[
 G_4(X)=\sum_{0\le r\le R_X}H_4(X/4^r)+O(1),
\tag{L-34002.5}
\]

where `R_X=O(log X)`.

Fix `epsilon>0`. Choose `Y` such that

\[
 |H_4(y)|\le\epsilon y
 \qquad(y\ge Y).
\]

The terms in (L-34002.5) with `X/4^r>=Y` have total absolute value at most

\[
 \epsilon X\sum_{r\ge0}4^{-r}
 =\frac43\epsilon X.
\tag{L-34002.6}
\]

Every remaining argument lies in the fixed compact interval `[0,Y]`. Since there are only `O(log X)` remaining levels and `H_4` is bounded on that interval, their total is `O_Y(log X)=o(X)`. Because `epsilon` was arbitrary,

\[
 \boxed{G_4(X)=o(X).}
\tag{L-34002.7}
\]

Moreover the proof gives the uniform tail form

\[
 \boxed{
 \sup_{Y\le x\le X}\frac{|G_4(x)|}{x}\longrightarrow0
 \qquad(Y\to\infty),
 }
\tag{L-34002.8}
\]

in the sense needed below.

## 4. Uniform balanced physical current

For an integer split `n=j+k`, the correctly typed current is

\[
 Q_4^{\rm phys}(n,j)
 =G_4(n)-G_4(j)-G_4(k).
\tag{L-34002.9}
\]

On the quarter-balanced cone

\[
 n/4\le j,k\le3n/4,
\]

all three arguments tend to infinity uniformly with `n`. Equation (L-34002.7) therefore gives

\[
 \boxed{
 \sup_{n/4\le j\le3n/4}
 |Q_4^{\rm phys}(n,j)|=o(n).
 }
\tag{L-34002.10}

No zero-free region stronger than the ordinary PNT is used.

## 5. Divide by the deterministic Kummer reserve

PR #325 `L-32405` proves cofinally and uniformly on the same balanced cone

\[
 \mathcal R_4(n,j)
 >\frac1{20}P_4(n,j)^2
\]

and

\[
 P_4(n,j)\ge\frac n4\log2.
\]

Hence

\[
 \boxed{
 \mathcal R_4(n,j)
 \ge\frac{n^2\log^22}{320}
 }
\tag{L-34002.11]
\]

for all sufficiently large balanced rows. Combining (L-34002.10) and (L-34002.11),

\[
 \boxed{
 \sup_{n/4\le j\le3n/4}
 \frac{|Q_4^{\rm phys}(n,j)|^2}{\mathcal R_4(n,j)}
 \longrightarrow0.
 }
\tag{L-34002.12}
\]

(The closing square bracket in tag `L-34002.11]` is typographical only.)

This is exactly the physical-current limit used by `L-32413`.

## 6. Real-X collar

PR #325 `L-32410` proves that for real `X`, with `N=floor X`, the true interval current differs from one integer-row current by at most one raw coefficient `c_4(m)`, and

\[
 |c_4(m)|\ll\log(2X).
\]

Thus on every fixed balanced carry-position interval the collar contributes

\[
 O(\log^2X)=o(X^2)
\]

to the unnormalized square. Equation (L-34002.12) therefore extends to the real-X current after division by the corresponding cofinal reserve scale.

## 7. Consequence for the augmented reserve

Together with the elementary logarithmic bound for the unweighted source `Y_4` in PR #337 `L-32706`, equation (L-34002.12) justifies the cofinal statement used in `L-32413`: for every fixed `M>0` and every `delta>0`, sufficiently large balanced rows satisfy

\[
 |Q_4^{\rm phys}|^2+M|Y_4|^2
 \le\delta\,\mathcal R_4.
\tag{L-34002.13}
\]

Therefore the true pole current and any fixed multiple of the unweighted source can indeed be charged simultaneously to an arbitrarily small fraction of the balanced Kummer reserve at row scope.

## 8. Proof boundary

Closed unconditionally, subject to review:

1. `H_4(X)=o(X)` from the exact renewal and ordinary PNT;
2. `G_4(X)=o(X)` by geometric iteration;
3. uniform balanced physical current `o(n)`;
4. the missing current/reserve ratio (L-34002.12);
5. repair of the dependency used by `L-32413`;
6. harmless real-X one-coefficient collar at this scale.

Still open:

1. the complete independent-frequency reflected block recurrence;
2. conclusion-producing control of the neutral principal mode;
3. RH.
