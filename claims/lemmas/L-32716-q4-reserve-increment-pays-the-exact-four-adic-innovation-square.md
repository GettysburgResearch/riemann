# L-32716 — The Q=4 reserve increment pays the exact four-adic innovation square

Claim ID: `L-32716`  
Title: On every sufficiently large quarter-balanced row, the difference between the reserve at `(4n,4j)` and sixteen copies of the reserve at `(n,j)` is at least the square of the exact generalized-prime four-adic innovation  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: PR #325 `L-32411`; elementary uniform Euler estimates for `sum log^2 m`  
Scope: exact integer dilation rows and the deterministic Q=4 Kummer reserve; physical block/collar integration is handled separately

## 1. Notation

Put

\[
 L=\log4,
 \qquad
 d_r=(4^r-1)L.
\]

For a split `e=(n,j)`, `k=n-j`, define

\[
 c_r=\chi_{n,4^r}(j),
 \qquad
 N_r=\left\lfloor{n\over4^r}\right\rfloor,
 \qquad
 J_r=\left\lfloor{j\over4^r}\right\rfloor,
\]

and

\[
 F(n,j)=\log\binom nj.
\]

Let

\[
 H_2(N)=\sum_{m=1}^N\log^2m
\]

and

\[
 S_0(n,j)=H_2(n)-H_2(j)-H_2(k).
\]

Finally put

\[
 B_r(n,j)=F(N_r,J_r)+c_r\log(N_r-J_r),
 \tag{L-32716.1}
\]

with the second term interpreted as zero when `c_r=0`.

PR #325 `L-32411` gives exactly

\[
 \boxed{
 P_4(n,j)=F(n,j)+\sum_{r\ge1}d_rc_r
 }
 \tag{L-32716.2}
\]

and

\[
 \boxed{
 \begin{aligned}
 S_4(n,j)={}&S_0(n,j)
 +\sum_{r\ge1}d_r rL c_r\\
 &+2\sum_{r\ge1}d_rB_r(n,j)
 +\sum_{r,s\ge1}d_rd_sc_{r+s}.
 \end{aligned}}
 \tag{L-32716.3}
\]

## 2. Exact first-moment innovation

For the dilated row `4e=(4n,4j)`,

\[
 c'_1=0,
 \qquad
 c'_{r+1}=c_r,
 \qquad
 N'_{r+1}=N_r,
 \qquad
 J'_{r+1}=J_r.
 \tag{L-32716.4}
\]

Since

\[
 d_{r+1}=4d_r+3L,
\]

(L-32716.2) gives

\[
 \boxed{
 P_4(4n,4j)=4P_4(n,j)+\Delta_4(n,j),
 }
 \tag{L-32716.5}
\]

where

\[
 \boxed{
 \Delta_4(n,j)
 =\log\frac{\binom{4n}{4j}}{\binom nj^4}
 +3L\sum_{r\ge1}c_r
 \ge0.
 }
 \tag{L-32716.6}
\]

The binomial ratio is at least one by the four-block injection, so the innovation is nonnegative.

## 3. Exact scaling of the three local correction families

### 3.1 Logarithmic local term

Let

\[
 A(n,j)=\sum_{r\ge1}d_rrLc_r.
\]

Using (L-32716.4),

\[
 \boxed{
 A(4n,4j)-4A(n,j)
 =4L\sum_{r\ge1}d_rc_r
 +3L^2\sum_{r\ge1}(r+1)c_r.
 }
 \tag{L-32716.7}
\]

### 3.2 Mixed ordinary/local term

Let

\[
 M(n,j)=2\sum_{r\ge1}d_rB_r(n,j).
\]

The new first four-adic level has `N'_1=n`, `J'_1=j`, and zero carry, so its contribution is `2d_1F(n,j)`. All later levels are shifted copies. Therefore

\[
 \boxed{
 M(4n,4j)-4M(n,j)
 =2d_1F(n,j)+6L\sum_{r\ge1}B_r(n,j).
 }
 \tag{L-32716.8}
\]

### 3.3 Local/local convolution term

Put

\[
 E_t=\sum_{r=1}^{t-1}d_rd_{t-r}
 \qquad(t\ge2).
\]

Then

\[
 \sum_{r,s\ge1}d_rd_sc_{r+s}
 =\sum_{t\ge2}E_tc_t.
\]

A direct geometric summation gives

\[
 {E_t\over L^2}
 =4^t\left(t-\frac53\right)+t+\frac53.
 \tag{L-32716.9}
\]

Consequently

\[
 E_{t+1}-4E_t=L^2(4^{t+1}-3t-4).
\]

Including the new `t=1` contact, for which the same expression equals `d_1^2=9L^2`, one obtains

\[
 \boxed{
 \begin{aligned}
 &\sum_{r,s\ge1}d_rd_sc'_{r+s}
 -4\sum_{r,s\ge1}d_rd_sc_{r+s}\\
 &\qquad=L^2\sum_{t\ge1}(4^{t+1}-3t-4)c_t.
 \end{aligned}}
 \tag{L-32716.10}
\]

All identities in this section are finite.

## 4. Uniform linear error in the second-moment scaling

The elementary Euler estimate

\[
 H_2(N)
 =N(\log^2N-2\log N+2)+O(\log^2(2N))
 \tag{L-32716.11}
\]

is uniform for integer `N>=1`. On the fixed cone

\[
 n/4\le j,k\le3n/4,
\]

substitution into the three-term defect gives

\[
 \boxed{
 S_0(4n,4j)-4S_0(n,j)=O(n)
 }
 \tag{L-32716.12}
\]

uniformly in `j`.

Every correction on the right of (L-32716.7)--(L-32716.10) is also `O(n)` uniformly:

\[
 \sum_rd_r c_r=O(n),
 \qquad
 \sum_r(r+1)c_r=O(\log^2(2n)),
\]

\[
 F(n,j)=O(n),
 \qquad
 \sum_rB_r(n,j)=O(n),
 \qquad
 \sum_t4^tc_t=O(n).
\]

Therefore

\[
 \boxed{
 S_4(4n,4j)=4S_4(n,j)+O(n)
 }
 \tag{L-32716.13}
\]

uniformly on the complete quarter-balanced cone.

## 5. Uniform lower growth of the second moment

Because `C_4>=C_0` coefficientwise,

\[
 S_4(n,j)\ge S_0(n,j).
\]

The same Euler expansion gives

\[
 S_0(n,j)
 =2nH(j/n)\log n+O(n)
 \tag{L-32716.14}
\]

uniformly on the quarter-balanced cone, where

\[
 H(x)=-x\log x-(1-x)\log(1-x).
\]

The entropy has a positive minimum on `[1/4,3/4]`. Hence there is an absolute `c>0` such that

\[
 \boxed{
 S_4(n,j)\ge c n\log n
 }
 \tag{L-32716.15}
\]

for every sufficiently large quarter-balanced row.

Combining (L-32716.13) and (L-32716.15),

\[
 \frac{S_4(4n,4j)}{S_4(n,j)}
 =4+O(1/\log n)
 \tag{L-32716.16}
\]

uniformly. In particular, cofinally,

\[
 \boxed{
 S_4(4n,4j)\le16S_4(n,j).
 }
 \tag{L-32716.17}
\]

## 6. The reserve increment pays the innovation square

Let

\[
 R_4=P_4^2-S_4.
\]

Using (L-32716.5),

\[
\begin{aligned}
 R_4(4n,4j)-16R_4(n,j)
 ={}&8P_4(n,j)\Delta_4(n,j)\\
 &+\Delta_4(n,j)^2\\
 &+16S_4(n,j)-S_4(4n,4j).
\end{aligned}
 \tag{L-32716.18}
\]

Every term on the right is nonnegative once (L-32716.17) holds. Therefore

\[
 \boxed{
 R_4(4n,4j)-16R_4(n,j)
 \ge\Delta_4(n,j)^2
 }
 \tag{L-32716.19}
\]

for every sufficiently large quarter-balanced row.

More strongly, the reserve increment also contains the positive cross storage

\[
 8P_4(n,j)\Delta_4(n,j)
\]

and the full second-moment scale surplus.

## 7. Identification with the exact physical innovation

Let

\[
 h_4=(\varepsilon-4\delta_4)*\Lambda_4
\]

be the compact innovation coefficient of PR #325 `L-32412`. On the exactly dilated row,

\[
 \boxed{
 \mathcal L_{(4n,4j)}(h_4)
 =P_4(4n,4j)-4P_4(n,j)
 =\Delta_4(n,j).
 }
 \tag{L-32716.20}
\]

Thus (L-32716.19) is not merely a reserve-scaling inequality: the newly created reserve pays the square of the literal arithmetic innovation in the coefficient-one four-adic current renewal.

## 8. Proof boundary

Closed here, subject to review:

1. exact first-moment innovation;
2. exact scaling identities for every local second-moment family;
3. uniform `S_4(4e)=4S_4(e)+O(n)`;
4. cofinal `S_4(4e)<=16S_4(e)`;
5. exact innovation-square storage in the reserve increment;
6. identification with the compact physical innovation.

Still open:

1. handling floor-offset rows not exactly of the form `(4n,4j)` inside one physical block;
2. allocating cross terms between the delayed current and the innovation without spending the reserve increment twice;
3. the final coefficient-one block recurrence;
4. RH.
