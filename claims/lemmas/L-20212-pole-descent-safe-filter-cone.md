# L-20212 — Classification of the simple pole-descent-safe filter cone

Claim ID: `L-20212`  
Title: Positive multiplicity descent is exactly the positive mixture cone of the `r`-adic defects, and Haar is its sharp half-knot extremizer  
Status: **PROPOSED — COMPLETE FINITE ALGEBRAIC PROOF**  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: `T-20203`; elementary residue calculus  
Scope: finite dilation filters whose pole cancellation is certified by a positive multiplicity maximum principle

## 1. General dilation filter

Let

\[
 P_\lambda(x)=\sum_{k=1}^{N}\lambda_k(1-\cos kx)
\]

and consider the filtered screw statistic

\[
 \mathcal S_\lambda(t)=\sum_{k=1}^{N}\lambda_k\Psi(kt).
\]

Its Laplace transform is, up to the common factor `-1/z^2`,

\[
 \sum_{k=1}^{N}k\lambda_k
 {\xi'\over\xi}\left({1\over2}-{iz\over k}\right).
\]

Suppose an off-line zero `rho=1/2+w` of multiplicity `m` creates the pole at
`z=iw` through the `k=1` term. If

\[
 \rho_k={1\over2}+{w\over k}
\]

is a zero of multiplicity `m_k`, residue cancellation is exactly

\[
\boxed{
 \lambda_1m+
 \sum_{k=2}^{N}k^2\lambda_km_k=0.}
\]

The factor `k^2` contains one `k` from the transform and one from the derivative
of the scaled logarithmic derivative.

## 2. Positive maximum-principle hypotheses

Assume

\[
 \lambda_1>0,
 \qquad
 \lambda_k\le0\quad(k\ge2),
\]

and the quadratic cancellation

\[
\boxed{
 \sum_{k=1}^{N}k^2\lambda_k=0.}
\]

Put

\[
 p_k={-k^2\lambda_k\over\lambda_1}
 \qquad(k\ge2).
\]

Then

\[
 p_k\ge0,
 \qquad
 \sum_{k=2}^{N}p_k=1,
\]

and the residue equation becomes

\[
\boxed{
 m=\sum_{k=2}^{N}p_km_k.}
\]

Therefore at least one descendant satisfies

\[
 m_k\ge m.
\]

Iterating chooses a sequence of zeros whose displacements shrink by a factor at
least two while their multiplicities never decrease. The zeros accumulate at
`1/2`, impossible for nonzero entire `xi`. Thus holomorphy of the filtered
transform implies RH by the same pole-descent argument as `T-20203`.

## 3. Exact cone classification

Set

\[
 c_k=-\lambda_k\ge0
 \qquad(k\ge2).
\]

The moment identity gives

\[
 \lambda_1=\sum_{k=2}^{N}k^2c_k.
\]

Hence

\[
\begin{aligned}
 P_\lambda(x)
 &=\sum_{k=2}^{N}c_k
 \left[k^2(1-\cos x)-(1-\cos kx)\right]\\
 &=\sum_{k=2}^{N}c_kd_k(x),
\end{aligned}
\]

where `d_k` is the `k`-adic Fejer defect of `T-20203`. Conversely every positive
mixture of the `d_k` has exactly these coefficient signs and the quadratic
cancellation.

Thus

\[
\boxed{
 \text{simple positive multiplicity descent}
 \quad\Longleftrightarrow\quad
 P_\lambda\in\operatorname{cone}\{d_2,\ldots,d_N\}.}
\]

Every such filter is automatically nonnegative because every `d_k>=0`.

## 4. Sharp half-knot debt in the safe cone

The prime ramp of one `d_k` is

\[
 L_k(s)=k^2(1-s)_+-(k-s)_+.
\]

Therefore

\[
 L_k(0)=k(k-1),
 \qquad
 L_k(1/2)={1\over2}(k-1)^2.
\]

For a positive mixture,

\[
 {L_\lambda(1/2)\over L_\lambda(0)}
 ={
   \sum_{k\ge2}c_k(k-1)^2
  \over
   2\sum_{k\ge2}c_kk(k-1)
  }.
\]

This is a weighted average of `(k-1)/(2k)`. Hence

\[
\boxed{
 {L_\lambda(1/2)\over L_\lambda(0)}
 \ge{1\over4},}
\]

with equality only for the pure Haar defect `d_2`.

The first ramp zero is

\[
 s_0
 ={
   \sum c_kk(k-1)
  \over
   \sum c_k(k^2-1)
  },
\]

which is a weighted average of `k/(k+1)`. Thus

\[
\boxed{
 s_0\ge{2\over3}.}
\]

The general Fejer cone can approach a half-knot ratio `O(N^-2)`, but the simple
pole-descent-safe cone cannot beat `1/4`.

## 5. Consequence for the endpoint family

The alternating-sine endpoint filter of `L-20211` has alternating nonzero
`lambda_k` and does not lie in the safe cone for `N>=3`. Its sharp `O(N^-2)`
debt cannot be combined automatically with the positive multiplicity descent
used by `T-20203`.

Therefore a growing endpoint-Fejer proof needs an additional false-RH exposure
theorem, for example:

1. a signed residue-tree argument stronger than the maximum principle;
2. a complete dense FIR hierarchy rather than one filter per scale;
3. a zero-free transform/terminal-prime exponent theorem;
4. an independent prime-pair energy criterion.

Without such a theorem, positivity of the endpoint family would not by itself
imply RH.

## 6. Status boundary

This lemma classifies one robust pole-descent mechanism. It does not prove that
no other signed filter can be RH-equivalent. It does prove that the strongest
simple multiplicity argument and the strongest half-knot Fejer extremizer live
in different cones, and any full proof combining them must explicitly bridge
that gap.
