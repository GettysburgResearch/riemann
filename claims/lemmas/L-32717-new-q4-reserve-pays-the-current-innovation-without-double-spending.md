# L-32717 — New Q=4 reserve pays the current innovation without double spending

Claim ID: `L-32717`  
Title: On cofinal balanced four-adic lifts, the newly created reserve increment alone pays the exact innovation and its cross term in the normalized true-current square, leaving the inherited reserve untouched  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-32716`; corrected true physical current of PR #325/PR #337  
Scope: exactly dilated integer rows; real-X and nondivisible carry collars are treated in the following block theorem

## 1. Exact current renewal on a dilated row

Let

\[
 e=(n,j),
 \qquad
 4e=(4n,4j).
\]

Write

\[
 Q_e=Q_4^{\rm phys}(n,j)
\]

for the unnormalized correctly typed Q=4 pole current, and let

\[
 \Delta_e=P_4(4n,4j)-4P_4(n,j)
\]

be the nonnegative innovation of `L-32716`.

The coefficient renewal

\[
 c_4=(\varepsilon-4\delta_4)*\Lambda_4+\delta_4*c_4
\]

and the exact scaled carry identity

\[
 \chi_{4n,4d}(4j)=\chi_{n,d}(j)
\]

give

\[
 \boxed{
 Q_{4e}=Q_e+\Delta_e.
 }
 \tag{L-32717.1}
\]

No remainder occurs on an exactly dilated row.

## 2. Optimal normalized Young inequality

Put

\[
 \alpha_n={4n+1\over n+1}>1.
\]

For arbitrary real or complex `Q,Delta`, completing the square gives the sharp inequality

\[
 \boxed{
 |Q+\Delta|^2
 \le
 \alpha_n|Q|^2
 +{\alpha_n\over\alpha_n-1}|\Delta|^2.
 }
 \tag{L-32717.2}
\]

Indeed the difference of the right side and left side is

\[
 (\alpha_n-1)
 \left|Q-\frac{\Delta}{\alpha_n-1}\right|^2.
\]

Since

\[
 \alpha_n-1={3n\over n+1},
\]

dividing (L-32717.2) by `4n+1` yields the exact normalized form

\[
 \boxed{
 { |Q+\Delta|^2\over4n+1}
 \le
 { |Q|^2\over n+1}
 +{ |\Delta|^2\over3n}.
 }
 \tag{L-32717.3}
\]

Applying (L-32717.1),

\[
 { |Q_{4e}|^2\over4n+1}
 \le
 { |Q_e|^2\over n+1}
 +{\Delta_e^2\over3n}.
 \tag{L-32717.4}
\]

## 3. The reserve increment is stronger than the innovation square

Let

\[
 D_e=R_4(4e)-16R_4(e).
\]

`L-32716` gives exactly

\[
 D_e
 =8P_4(e)\Delta_e+\Delta_e^2
  +16S_4(e)-S_4(4e).
 \tag{L-32717.5}
\]

Cofinally on the quarter-balanced cone the last term is nonnegative.

The same uniform Stirling estimate used in `L-32716` gives

\[
 \Delta_e=O(\log(2n)),
 \tag{L-32717.6}
\]

while

\[
 P_4(e)\ge{n\over4}\log2.
 \tag{L-32717.7}
\]

Therefore, uniformly on the cone,

\[
 {P_4(e)\over\Delta_e}\longrightarrow+\infty
\]

whenever `Delta_e>0`. Hence, for every sufficiently large parent,

\[
 8P_4(e)\Delta_e\ge\frac13\Delta_e^2.
\]

Together with (L-32717.5),

\[
 \boxed{
 D_e\ge\frac43\Delta_e^2.
 }
 \tag{L-32717.8}
\]

If `Delta_e=0`, the conclusion is immediate.

Since

\[
 {4n+1\over3n}<\frac32
\]

and in fact tends to `4/3`, moving the threshold once more gives the precise proof-facing inequality

\[
 \boxed{
 {\Delta_e^2\over3n}
 \le
 {D_e\over4n+1}.
 }
 \tag{L-32717.9}
\]

Alternatively, (L-32717.9) follows directly from (L-32717.5) and `P_4/Delta_e -> infinity`, without fixing the intermediate constant `4/3`.

## 4. Coefficient-one normalized recurrence with fresh-reserve payment

Combining (L-32717.4) and (L-32717.9),

\[
 \boxed{
 { |Q_{4e}|^2\over4n+1}
 -{R_4(4e)-16R_4(e)\over4n+1}
 \le
 { |Q_e|^2\over n+1}.
 }
 \tag{L-32717.10}
\]

Equivalently,

\[
 \boxed{
 \mathcal E_Q(4e)
 \le
 \mathcal E_Q(e)+\mathcal D_R(4e:e),
 }
 \tag{L-32717.11}
\]

where

\[
 \mathcal E_Q(e)={|Q_e|^2\over n+1},
 \qquad
 \mathcal D_R(4e:e)={R_4(4e)-16R_4(e)\over4n+1}.
\]

The coefficient of the delayed true-current energy is exactly one.

Most importantly, the innovation is paid by the **new reserve** `D_e`. The inherited amount `16R_4(e)` is not charged. Therefore iteration along a four-adic chain cannot spend the same reserve at two successive generations.

## 5. Finite-chain telescope

For a chain

\[
 e_k=4^ke_0,
 \qquad0\le k\le K,
\]

sum (L-32717.10) over `k=1,...,K`. The current terms telescope with coefficient one:

\[
 \boxed{
 \mathcal E_Q(e_K)
 \le
 \mathcal E_Q(e_0)
 +\sum_{k=1}^K
 {R_4(e_k)-16R_4(e_{k-1})\over4^kn_0+1}.
 }
 \tag{L-32717.12}
\]

Every summand uses a disjoint reserve increment. This is the exact no-double-spend ledger required by an all-generation four-adic assembly.

In a reflected proof the increments appear with dissipative sign. When inserted there, (L-32717.12) leaves only the coefficient-one initial/terminal current state.

## 6. Proof boundary

Closed here, subject to review:

1. exact true-current renewal on divisible rows;
2. sharp normalized cross-term inequality;
3. cofinal reserve-increment domination of the required innovation cost;
4. coefficient-one recurrence with fresh-reserve payment;
5. finite-chain no-double-spend telescope.

Still open:

1. the real-X/nondivisible-row collar in a complete logarithmic block;
2. insertion of the dissipative reserve increments into the exact reflected physical identity;
3. the final unit-block recurrence and RH.
