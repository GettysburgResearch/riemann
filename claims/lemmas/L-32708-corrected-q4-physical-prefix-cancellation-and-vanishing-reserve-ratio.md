# L-32708 — Corrected Q=4 physical prefix cancellation and vanishing reserve ratio

Claim ID: `L-32708`  
Title: In the correctly typed interval-kernel coordinate, the Q=4 pole-preserving physical coefficient has zero linear density by PNT, so its balanced physical defect consumes a vanishing fraction of the already-proved Selberg reserve  
Status: **PROPOSED COMPLETE UNCONDITIONAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `R-32704`; PR #325 `R-32403`, corrected `L-32407`, `L-32405`; classical PNT/Chebyshev bound  
Scope: corrected physical current-to-reserve absorption; no global reflected recurrence or RH conclusion

## 1. Correct physical coefficient

Retain

\[
 c_4=e_4*\Lambda_4,
\]

where

\[
 e_4(1)=1,
 \qquad e_4(4^r)=-3\quad(r\ge1),
\]

and let

\[
 \boxed{
 G_4(x)=\sum_{n\le x}c_4(n).
 }
\tag{L-32708.1}
\]

PR #325 `R-32403` identifies the correctly typed integer physical field as

\[
 \boxed{
 Q_4^{\rm phys}(n,j)
 =G_4(n)-G_4(j)-G_4(n-j).
 }
\tag{L-32708.2}
\]

This is the interval-kernel/additive-split coordinate. No second carry transform is applied.

## 2. Exact prefix formula

Let

\[
 \Psi_4(x)=\sum_{m\le x}\Lambda_4(m).
\]

Because `c_4=e_4*Lambda_4`, ordinary summation of the convolution gives

\[
\begin{aligned}
G_4(x)
&=\sum_{ab\le x}e_4(a)\Lambda_4(b)\\
&=\boxed{
\Psi_4(x)-3\sum_{r\ge1}\Psi_4(x/4^r).}
\end{aligned}
\tag{L-32708.3}
\]

The sum is finite for every fixed `x`.

This is the same formal expression that appeared in the earlier Q=4 current attack, but `R-32704` proves that its legitimate coefficient is `c_4`, not `q_4`.

## 3. Separate the ordinary-prime and local Q-adic pieces

By PR #325 `L-32404`,

\[
\Lambda_4(n)
=\Lambda(n)
 +(\log4)\sum_{m\ge1}(4^m-1)\mathbf1_{n=4^m}.
\tag{L-32708.4}
\]

Hence

\[
\Psi_4(x)=\psi(x)+D_4(x),
\tag{L-32708.5}
\]

where

\[
D_4(x)
=(\log4)\sum_{4^m\le x}(4^m-1).
\tag{L-32708.6}
\]

Substitution into (L-32708.3) gives

\[
G_4(x)=H_4(x)+L_4^{\rm loc}(x),
\tag{L-32708.7}
\]

with

\[
\boxed{
H_4(x)=\psi(x)-3\sum_{r\ge1}\psi(x/4^r),}
\tag{L-32708.8}
\]

and

\[
L_4^{\rm loc}(x)
=D_4(x)-3\sum_{r\ge1}D_4(x/4^r).
\tag{L-32708.9}
\]

## 4. The local Q-adic piece is only quadratic-logarithmic

Equivalently one may read the explicit pure-dyadic coefficient law of corrected PR #325 `L-32407`:

\[
 c_4(2^{2m})=(3m+4)\log2,
\qquad m\ge1,
\]

\[
 c_4(2^{2m+1})=(1-3m)\log2,
\qquad m\ge0.
\]

Only `O(log x)` such coefficients occur below `x`, each of size `O(log x)`. Therefore

\[
 \boxed{
 L_4^{\rm loc}(x)=O((\log(2x))^2).
 }
\tag{L-32708.10}
\]

This may also be obtained directly by telescoping (L-32708.9).

## 5. PNT kills the complete linear density

The prime number theorem gives

\[
\psi(y)=y+o(y).
\tag{L-32708.11}
\]

The linear terms in (L-32708.8) cancel exactly because

\[
 \boxed{
 3\sum_{r\ge1}4^{-r}=1.
 }
\tag{L-32708.12}
\]

For completeness, fix an integer `R`. For `1<=r<=R`, PNT gives

\[
\psi(x/4^r)=x/4^r+o(x)
\]

for each fixed `r`. For the tail `r>R`, the elementary Chebyshev estimate `psi(y)<=C y` gives

\[
\sum_{r>R}\psi(x/4^r)
=O(x4^{-R}).
\]

Let first `x->infinity` and then `R->infinity`. Thus

\[
 \boxed{H_4(x)=o(x).}
\tag{L-32708.13}
\]

Combining with (L-32708.10),

\[
 \boxed{G_4(x)=o(x).}
\tag{L-32708.14}
\]

This is unconditional and uses no critical-strip zero estimate.

## 6. Uniform balanced physical current decay

Fix `0<eta<=1/2`. If

\[
\eta n\le j\le(1-\eta)n,
\]

then all three arguments in (L-32708.2) tend uniformly to infinity with `n`. Equation (L-32708.14) therefore gives

\[
 \boxed{
 \sup_{\eta n\le j\le(1-\eta)n}
 { |Q_4^{\rm phys}(n,j)|\over n}
 \longrightarrow0.
 }
\tag{L-32708.15}
\]

In particular the statement applies to the quarter-balanced cone.

## 7. Vanishing fraction of the source-matched reserve

PR #325 `L-32405` proves for every `n>=4735` and every quarter-balanced row

\[
R_4(n,j)>\frac1{20}P_4(n,j)^2,
\tag{L-32708.16}
\]

with

\[
P_4(n,j)\ge\frac n4\log2.
\tag{L-32708.17}
\]

Hence

\[
R_4(n,j)
>{n^2\log^22\over320}.
\tag{L-32708.18}
\]

Given `epsilon>0`, equation (L-32708.15) gives, for all sufficiently large `n`,

\[
|Q_4^{\rm phys}(n,j)|\le\epsilon n
\]

uniformly on the quarter-balanced cone. Therefore

\[
\boxed{
\sup_{n/4\le j\le3n/4}
{ |Q_4^{\rm phys}(n,j)|^2\over R_4(n,j)}
\longrightarrow0.
}
\tag{L-32708.19}
\]

Equivalently, for every declared `delta>0`, there is `N_delta` such that

\[
 \boxed{
 |Q_4^{\rm phys}(n,j)|^2
 \le\delta R_4(n,j)
 }
\tag{L-32708.20}
\]

for all `n>=N_delta` and all quarter-balanced `j`.

## 8. Finite direct-sum consequence

If `nu(n,j)>=0` is any finite row measure supported on quarter-balanced parents above `N_delta`, then multiplication and summation of (L-32708.20) gives

\[
 \boxed{
 \sum_{n,j}\nu(n,j)|Q_4^{\rm phys}(n,j)|^2
 \le\delta\sum_{n,j}\nu(n,j)R_4(n,j).
 }
\tag{L-32708.21}
\]

All source amplitudes and row weights are retained identically on the two sides.

## 9. Consequence for the live Q=4 route

This repairs the strongest conclusion of the earlier source-mistyped current argument at the exact coordinate licensed by `R-32403`:

```text
correct coefficient c4=e4*Lambda4
-> exact interval-kernel physical field
-> complete linear-density cancellation by PNT
-> balanced physical field=o(n)
-> physical-current / Selberg-reserve ratio -> 0.
```

Thus PR #325's fixed-constant corrected transference can be sharpened cofinally to an arbitrarily small absorption fraction without changing the physical source.

The theorem still does not place the complete source-convolved reflected product/boundary term into this row-direct-sum reserve. That remains the exact algebraic step needed before the reserve can be spent in a global recurrence.

## 10. Proof boundary

Closed here, subject to review:

- the exact correctly typed Q=4 prefix formula;
- separation of ordinary-prime and local Q-adic pieces;
- PNT cancellation of the complete linear density;
- uniform balanced physical current decay;
- vanishing physical-current / source-matched-reserve ratio;
- homogeneous finite direct-sum absorption.

Open:

- exact independent-frequency/source-convolved placement of the remaining unweighted boundary;
- the resulting coefficient-one scattering recurrence;
- RH.
