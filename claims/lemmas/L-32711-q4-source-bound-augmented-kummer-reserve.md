# L-32711 — Q=4 source-bound augmented Kummer reserve is positive cofinally

Claim ID: `L-32711`  
Title: Adding the exact inverse-source logarithmic curvature to the Q=4 generalized-prime Kummer reserve gives a positive source-complete scalar reserve on every sufficiently large balanced carry row  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32404/L-32405`; PR #337 `L-32706`; elementary divisor convolution  
Scope: correctly typed Q=4 inverse source and its first two logarithmic currents; no independent-frequency matrix or RH conclusion

## 1. Source deformation and its three row coordinates

Retain the Q=4 Euler–Blaschke system

\[
 A_4(s)=B_4(s)^{-1},
 \qquad
 B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)}.
\]

Let

\[
 b_4=A_4^{-1},
 \qquad
 \Lambda_4=b_4*(a_4\log),
 \qquad
 C_4=\Lambda_4\log+\Lambda_4*\Lambda_4.
\]

Define the first and second source-convolved logarithmic currents

\[
 \boxed{
 q_4=b_4*\Lambda_4=-b_4\log,
 \qquad
 t_4=b_4*C_4=q_4\log+2q_4*\Lambda_4.
 }
 \tag{L-32711.1}
\]

For a split `e=(n,j)`, `k=n-j`, use the carry functional

\[
 \mathcal L_e(f)=\sum_{d\le n}f(d)\chi_{n,d}(j).
\]

Put

\[
 \boxed{
 Y_e=\mathcal L_e(b_4),
 \quad Q_e=\mathcal L_e(q_4),
 \quad T_e=\mathcal L_e(t_4).
 }
 \tag{L-32711.2}
\]

The generalized-prime Kummer coordinates are

\[
 P_e=\mathcal L_e(\Lambda_4),
 \qquad
 S_e=\mathcal L_e(C_4),
 \qquad
 \mathcal R_e=P_e^2-S_e.
 \tag{L-32711.3}
\]

PR #325 `L-32405` proves `R_e>0` on every quarter-balanced row and, for every
`n>=4735`,

\[
 \boxed{
 \mathcal R_e>\frac1{20}P_e^2,
 \qquad
 P_e\ge\frac n4\log2.
 }
 \tag{L-32711.4}
\]

## 2. Exact deformation interpretation

Define the finite Jordan deformation

\[
 J_\tau(s)=\frac{A_4(s-\tau)}{A_4(s)}.
\]

Coefficientwise differentiation at `tau=0` gives

\[
 J_0=\varepsilon,
 \qquad
 J'_0=\Lambda_4,
 \qquad
 J''_0=C_4.
 \tag{L-32711.5}
\]

Now source-convolve once more:

\[
 K_\tau=b_4*J_\tau.
\]

Then

\[
 K_0=b_4,
 \qquad
 K'_0=q_4,
 \qquad
 K''_0=t_4.
 \tag{L-32711.6}
\]

Thus on one carry row

\[
 \mathcal L_e(K_0)=Y_e,
 \qquad
 \mathcal L_e(K'_0)=Q_e,
 \qquad
 \mathcal L_e(K''_0)=T_e.
 \tag{L-32711.7}
\]

The quantity

\[
 \boxed{
 \mathcal A_e
 :=\mathcal R_e+Q_e^2-Y_eT_e
 =P_e^2-S_e+Q_e^2-Y_eT_e
 }
 \tag{L-32711.8}
\]

is therefore the sum of the generalized-prime Kummer reserve and the exact
second logarithmic curvature of the inverse-source deformation. Unlike an
arbitrary rescaling of `L-32405`, every factor in (L-32711.8) is fixed by the
same Q=4 source.

## 3. Elementary bound for the unweighted source charge

PR #337 `L-32706` gives exactly

\[
 Y_e=3(a+c-r)-1,
 \qquad
 a=\lfloor\log_4j\rfloor,
 \quad c=\lfloor\log_4k\rfloor,
 \quad r=\lfloor\log_4n\rfloor.
 \tag{L-32711.9}
\]

Hence, on every nontrivial row,

\[
 \boxed{
 |Y_e|\le 3\log_4 n+4
 \ll\log(2n).
 }
 \tag{L-32711.10}
\]

In the cofinal quarter-balanced cone `Y_e` is in fact positive and grows only
logarithmically; the absolute bound is enough below.

## 4. Elementary coefficient bound for the second source current

Because

\[
 b_4=\mu*e_4,
 \qquad
 e_4(1)=1,
 \qquad e_4(4^r)=-3,
\]

one has

\[
 |b_4(m)|\le1+3\lfloor\log_4m\rfloor
 \ll\log(2m).
 \tag{L-32711.11}
\]

Since `q_4(m)=-b_4(m)log m`,

\[
 \boxed{|q_4(m)|\ll\log^2(2m).}
 \tag{L-32711.12}
\]

PR #325 `L-32405.11` supplies the completely elementary generalized-prime mass
bound

\[
 \sum_{d\le x}\Lambda_4(d)<\frac{10}{3}x.
 \tag{L-32711.13}
\]

Using (L-32711.1), finite divisor switching, and (L-32711.12)--(L-32711.13),

\[
\begin{aligned}
 \sum_{m\le n}|t_4(m)|
 &\le
 \sum_{m\le n}|q_4(m)|\log m\\
 &\quad+2\sum_{ab\le n}|q_4(a)|\Lambda_4(b)\\
 &\ll n\log^3(2n)
   +n\sum_{a\le n}{\log^2(2a)\over a}\\
 &\ll\boxed{n\log^3(2n)}.
\end{aligned}
 \tag{L-32711.14}
\]

Every carry indicator is zero or one, so

\[
 \boxed{|T_e|\ll n\log^3(2n).}
 \tag{L-32711.15}
\]

Consequently

\[
 \boxed{|Y_eT_e|\ll n\log^4(2n).}
 \tag{L-32711.16}
\]

No PNT, zero-free region, or RH-scale cancellation is used in this estimate.

## 5. Cofinal positivity of the augmented reserve

From (L-32711.4),

\[
 \mathcal R_e
 >{n^2(\log2)^2\over320}
 \tag{L-32711.17}
\]

throughout the quarter-balanced cone once `n>=4735`.

Equations (L-32711.16)--(L-32711.17) give

\[
 { |Y_eT_e|\over\mathcal R_e}
 \ll{\log^4(2n)\over n}
 \longrightarrow0
 \tag{L-32711.18}
\]

uniformly over all quarter-balanced positions. Since `Q_e^2>=0`, there exists a
finite `N_*` such that for every

\[
 n\ge N_*,
 \qquad n/4\le j\le3n/4,
\]

one has

\[
 \boxed{
 \mathcal A_e
 =\mathcal R_e+Q_e^2-Y_eT_e>0.
 }
 \tag{L-32711.19}
\]

More strongly,

\[
 \boxed{
 \mathcal A_e
 \ge(1-o(1))\mathcal R_e+Q_e^2
 }
 \tag{L-32711.20}
\]

uniformly on the cofinal balanced cone.

This is the first Q=4 Kummer reserve on the branch which contains the inverse
source itself and its second logarithmic current, rather than only the
zero-blind generalized-prime channel.

## 6. Finite reconnaissance and proof boundary

A direct finite scan of the exact coefficient formulas with high-precision
logarithms found

```text
A_e > 0
```

on every quarter-balanced row through parent `n=5000`; the smallest value in
that scan occurs at the small row `(6,2)`. This is **reconnaissance only** and
is not used in the cofinal proof above.

Closed here, subject to independent review:

1. the exact source-deformation identities through second order;
2. the source-complete augmented reserve (L-32711.8);
3. elementary logarithmic growth of the bare source charge;
4. elementary `O(n log^3 n)` second-current bound;
5. uniform cofinal positivity and asymptotic domination by the ordinary Q=4
   Kummer reserve.

Still open:

1. polarization/placement of `A_e` in the complete independent-frequency
   physical block;
2. treatment of the finite low-parent base table if an all-row theorem is desired;
3. the neutral block recurrence;
4. RH.
