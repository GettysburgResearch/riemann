# L-95041 — The positive two-leaf tree cone has an exact interval criterion

Claim ID: `L-95041`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Depends on: `L-95040`  
Scope: nonnegative source mass on parents `n>=4`, routed through quarter-balanced trees terminating at leaves of size two and three; no claim that every critical source has this sign pattern

## 1. Admissible terminal counts

For `n>=4`, let

\[
\mathcal B_n
=\{b\in\mathbb Z_{\ge0}: 3b\le n,
\ b\equiv n\pmod2\}.
\tag{L-95041.1}
\]

For `b in B_n`, put

\[
a={n-3b\over2}\in\mathbb Z_{\ge0}.
\]

Thus `a` leaves of size two and `b` leaves of size three have total size `n`.
Define

\[
b_n^-=\min\mathcal B_n,
\qquad
b_n^+=\max\mathcal B_n.
\tag{L-95041.2}
\]

Explicitly,

\[
b_n^-=\begin{cases}0,&n\text{ even},\\1,&n\text{ odd},\end{cases}
\]

and `b_n^+` is the largest integer not exceeding `n/3` with the parity of `n`.

## 2. Every admissible count has a legal tree

For every `n>=4` and every `b in B_n`, there exists a binary tree whose root has size `n`, whose leaves consist of exactly

\[
a={n-3b\over2}
\]

copies of node two and `b` copies of node three, and every internal split belongs to `E_n^circ`.

To prove this, view the leaves as coins of values two and three. For total `n>=12`, add coins greedily until the partial sum first reaches `n/3`. The overshoot is at most two, so the selected sum `j` obeys

\[
{n\over3}\le j\le{n\over3}+2\le{n\over2}.
\]

Both parts have size at least two, and the split is quarter-balanced. Apply induction to the two submultisets. The totals `4<=n<=11` are checked directly. This constructs the desired tree.

Let `T_(n,b)` be one such tree. Then

\[
\boxed{
\partial T_{n,b}
=e_n-{n-3b\over2}e_2-be_3.
}
\tag{L-95041.3}
\]

## 3. Convex terminal interval

Because flows have real nonnegative coefficients, convex mixtures of two trees are allowed. Hence one unit of source at node `n` can produce any real terminal three-leaf mass in the complete interval

\[
[b_n^-,b_n^+].
\tag{L-95041.4}
\]

The corresponding two-leaf mass is `(n-3b)/2`.

## 4. Exact positive criterion

Let `r` satisfy

\[
r(1)=0,
\qquad
\sum_mmr(m)=0,
\qquad
r(n)\ge0\quad(n\ge4).
\tag{L-95041.5}
\]

Put

\[
B_- =\sum_{n=4}^Xr(n)b_n^- ,
\qquad
B_+ =\sum_{n=4}^Xr(n)b_n^+ .
\tag{L-95041.6}
\]

Then the following are equivalent:

1. `r` is realized by a nonnegative superposition of quarter-balanced trees rooted in the source masses `r(n)`, `n>=4`, and terminating only at nodes two and three;
2. the terminal coordinates satisfy

\[
\boxed{
r(2)\le0,
\quad r(3)\le0,
\quad -r(3)\in[B_-,B_+].}
\tag{L-95041.7}
\]

Indeed choose, for each `n`, a terminal-three count `b_n in [b_n^-,b_n^+]` such that

\[
\sum_{n=4}^Xr(n)b_n=-r(3).
\]

The Minkowski sum of intervals is the interval `[B_-,B_+]`, so such choices exist exactly under (L-95041.7). Size conservation then forces

\[
\sum_{n=4}^Xr(n){n-3b_n\over2}=-r(2).
\]

The corresponding nonnegative tree mixture has divergence `r`.

Conversely, expand any such tree superposition into its terminal leaves. Each root `n` contributes a terminal-three mass in `[b_n^-,b_n^+]`, proving necessity.

## 5. Implication for CRCTP

This theorem closes a substantial positive subcone with no LP solver. A root-completed critical source would be solved whenever a positive preliminary transform makes its high-node divergence nonnegative and places the terminal demand inside (L-95041.7).

The actual Möbius divergence is not proved to have that sign pattern. The theorem is a constructive target for a source-specific Green transform, not an RH proof.

## 6. Proof boundary

Established exactly:

1. all feasible two/three terminal counts admit quarter-balanced trees;
2. the complete convex terminal interval;
3. a necessary and sufficient positive-cone criterion for nonnegative high-node source mass;
4. an explicit positive flow construction.

Open:

1. a cofinal positive transform of the actual root-completed critical source into this cone;
2. the root scalar estimate;
3. RH.
