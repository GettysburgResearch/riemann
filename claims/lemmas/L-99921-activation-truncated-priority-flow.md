# L-99921 — Activation truncation leaves only upward priority-boundary flux

Claim ID: `L-99921`  
Status: **PROVED EXACT FINITE FLOW THEOREM**  
Created: 2026-08-20  
Depends on: `L-99920`; PR #667 normalized box  
RH status: **not assumed**

Let `Phi(A)>=0` be product-monotone:

\[
A\subseteq B\Longrightarrow \Phi(A)\ge\Phi(B).
\]

For the normalized factor-67 box at endpoint `X`,

\[
\Phi_X(A)=\Phi_{67}(X/P_A),
\qquad
P_A=\prod_{i\in A}p_i,
\]

with zero extension below one, has this property.

Give each odd vertex demand `w(A)Phi(A)` and each even vertex capacity `w(A)Phi(A)`.  Truncate the priority edge of `L-99920` to

\[
\boxed{
J_{i,A}^{\Phi}
=J_{i,A}\min\{\Phi(A),\Phi(A\cup\{i\})\}.
}
\tag{L-99921.1}
\]

This is a feasible physical odd-to-even flow.  Every odd demand left unmatched is caused by an edge for which the odd endpoint is the smaller-product endpoint `A`, equivalently `|A|` is odd.  Define

\[
\boxed{
\mathcal U_{\Phi}
=\sum_i
\sum_{\substack{A\subseteq\{i+1,\ldots,k\}\\ |A|\ {m odd}}}
J_{i,A}
[\Phi(A)-\Phi(A\cup\{i\})].
}
\tag{L-99921.2}
\]

Then the total unmatched odd mass of this explicit flow is exactly `U_Phi`.  If `rho_Phi^*` is the optimal unmatched mass among all admissible Hasse flows, and

\[
\mathscr A_{\Phi}
=\sum_A(-1)^{|A|}w(A)\Phi(A),
\]

then

\[
\boxed{
[-\mathscr A_{\Phi}]_+
\le \rho_{\Phi}^*
\le \mathcal U_{\Phi}.
}
\tag{L-99921.3}
\]

## Proof

The truncated flow never exceeds an odd demand or an even capacity, because every incident full-flow coefficient at a vertex sums to `w(A)` by `L-99920`, and each edge multiplier is at most `Phi(A)`.

At an odd vertex `S`, the edge owned by `min S` points from `S` to a divisor and has minimum potential `Phi(S)`, so it loses nothing.  Each earlier-owner edge points from `S` to `S union {j}` and loses exactly

\[
\lambda_jw(S)[\Phi(S)-\Phi(S\cup\{j\})].
\]

Summing over odd vertices gives (L-99921.2).  Finally, for every feasible flow,

\[
\text{odd demand}-\text{even capacity}
=\text{unmatched odd}-\text{unused even},
\]

which implies the first inequality in (L-99921.3); the explicit flow gives the second.

This is an exact cut-compression theorem: an arbitrary Hasse min-cut is bounded by one triangular family of first-owner product-boundary crossings.
