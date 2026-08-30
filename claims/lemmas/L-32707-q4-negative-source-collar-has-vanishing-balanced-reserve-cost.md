# L-32707 — The Q=4 negative source collar has vanishing cost against the same-parent balanced reserve

Claim ID: `L-32707`  
Title: The complete adverse fifteen-contact packet of the unweighted Q=4 inverse source has homogeneous normalized energy `O(n)`, while the already-proved balanced Selberg reserve is `Omega(n^2)`; its relative cost therefore tends to zero  
Status: **PROPOSED COMPLETE HOMOGENEOUS ROW-DIRECT-SUM THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-32706`; PR #325 `L-32405`  
Scope: exact same-parent scalar-source budget; placement of the complete independent-frequency reflected boundary into this row-direct-sum remains a separate algebraic obligation

## 1. Negative source packet

Retain the Q=4 generalized-prime row

\[
 P_4(n,j)=\sum_{q\le n}\Lambda_4(q)\chi_{n,q}(j),
\tag{L-32707.1}
\]

and its Selberg reserve

\[
 R_4(n,j)=P_4(n,j)^2-S_4(n,j).
\tag{L-32707.2}
\]

Let `Y_4(n,j)` be the unweighted inverse-source carry charge of `L-32706`.
Define the normalized adverse homogeneous packet

\[
 \boxed{
 \mathcal E_4^-(n)
 ={1\over n+1}
  \sum_{j=1}^{n-1}
  [-Y_4(n,j)]_+^2 P_4(n,j)^2.
 }
\tag{L-32707.3}
\]

This is the natural quadratic packet obtained when a scalar row amplitude is multiplied by the unweighted source charge and the generalized-prime current. It is homogeneous in that row amplitude.

`L-32706` proves that the sum in (L-32707.3) contains at most thirty positions and, on every contributing position,

\[
|Y_4(n,j)|\le4.
\tag{L-32707.4}
\]

## 2. Linear upper bound for the complete adverse packet

Because every generalized-prime coefficient is nonnegative and every carry indicator is at most one,

\[
0\le P_4(n,j)\le L_4(n),
\tag{L-32707.5}
\]

where

\[
L_4(n)=\sum_{q\le n}\Lambda_4(q).
\]

PR #325 `L-32405.11` proves the elementary uniform estimate

\[
 \boxed{L_4(n)<{10\over3}n.}
\tag{L-32707.6}
\]

Therefore, for every `n`,

\[
\begin{aligned}
\mathcal E_4^-(n)
&< {1\over n+1}
   \cdot30\cdot16\cdot{100\over9}n^2\\
&<\boxed{{16000\over3}n.}
\end{aligned}
\tag{L-32707.7}
\]

No prime-distribution estimate enters this bound.

## 3. Same-parent balanced reserve

Define the normalized complete quarter-balanced reserve

\[
 \boxed{
 \mathcal R_4^{\rm bal}(n)
 ={1\over n+1}
  \sum_{\lceil n/4\rceil\le j\le\lfloor3n/4\rfloor}
  R_4(n,j).
 }
\tag{L-32707.8}
\]

For every `n>=4735`, PR #325 `L-32405` gives on every row in this sum

\[
R_4(n,j)>{1\over20}P_4(n,j)^2
\tag{L-32707.9}
\]

and

\[
P_4(n,j)\ge{n\over4}\log2.
\tag{L-32707.10}
\]

There are at least `n/3` quarter-balanced integer positions for `n>=12`. Hence, for `n>=4735`,

\[
\begin{aligned}
\mathcal R_4^{\rm bal}(n)
&>{1\over n+1}\,{n\over3}
  {n^2\log^22\over320}\\
&\ge\boxed{{n^2\log^22\over1920}.}
\end{aligned}
\tag{L-32707.11}
\]

The last inequality uses `n/(n+1)>=1/2`.

## 4. Vanishing relative charge

Combining (L-32707.7) and (L-32707.11),

\[
 \boxed{
 {\mathcal E_4^-(n)\over\mathcal R_4^{\rm bal}(n)}
 <{10240000\over n\log^22}
 \qquad(n\ge4735).
 }
\tag{L-32707.12}
\]

In particular,

\[
 \boxed{
 {\mathcal E_4^-(n)\over\mathcal R_4^{\rm bal}(n)}
 \longrightarrow0.
 }
\tag{L-32707.13}
\]

Using the rational lower bound `log2>69/100`, one may use the completely rational envelope

\[
 \boxed{
 {\mathcal E_4^-(n)\over\mathcal R_4^{\rm bal}(n)}
 <{22000000\over n}.}
\tag{L-32707.14}
\]

Thus for every declared `delta>0`, all sufficiently large parents satisfy

\[
 \boxed{
 \mathcal E_4^-(n)
 \le\delta\mathcal R_4^{\rm bal}(n).
 }
\tag{L-32707.15}
\]

## 5. Homogeneous no-double-spend form

Let `alpha_n` be any scalar amplitude attached to parent `n`. Multiplication by `|alpha_n|^2` preserves (L-32707.15):

\[
 |\alpha_n|^2\mathcal E_4^-(n)
 \le
 \delta |\alpha_n|^2\mathcal R_4^{\rm bal}(n).
\tag{L-32707.16}
\]

Summing over any finite family of sufficiently large parents gives

\[
 \boxed{
 \sum_n|\alpha_n|^2\mathcal E_4^-(n)
 \le
 \delta\sum_n|\alpha_n|^2\mathcal R_4^{\rm bal}(n).
 }
\tag{L-32707.17}
\]

The same parent amplitude appears on both sides. Therefore no row amplitude is detached from its source and no reserve is spent twice inside this declared direct-sum ledger.

## 6. Relation to the remaining reflected boundary

PR #302 `L-28013` isolates the unweighted inverse source as the only source coordinate absent from the logarithmic Selberg moments. PR #325 now provides:

- a complete Q=4 balanced Selberg reserve;
- physical Q=4 current absorption with vanishing relative charge;
- an exact real-X one-coefficient collar;
- an exact coefficient-one unitary scattering return.

`L-32706` shows the adverse unweighted carry source is only a fixed fifteen-contact collar. The present theorem shows that the corresponding natural homogeneous negative-source packet costs a vanishing fraction of the **same-parent** balanced reserve.

Therefore, once the complete independent-frequency source-convolved boundary is algebraically placed into the row-direct-sum packet (L-32707.3), its adverse unweighted component is cofinally absorbed without a new analytic estimate.

This theorem deliberately does not assume that placement. A cross-row or cross-frequency boundary quadratic may not be diagonalized merely because its scalar row restrictions obey (L-32707.15).

## 7. Proof boundary

Closed exactly, subject to review:

- fixed finite support and bounded magnitude of the adverse source charge;
- `O(n)` normalized adverse homogeneous energy;
- `Omega(n^2)` normalized same-parent balanced reserve;
- explicit `O(1/n)` relative cost;
- homogeneous finite direct-sum absorption.

Open:

- exact congruence/direct-sum placement of the complete independent-frequency unweighted boundary into this packet;
- the resulting global scattering recurrence;
- RH.
