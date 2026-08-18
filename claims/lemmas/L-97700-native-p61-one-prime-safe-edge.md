# L-97700 — A native `P_61` one-prime edge is strictly positive above the certified child range

Claim ID: `L-97700`  
Status: **PROVED UNCONDITIONAL GLOBAL INEQUALITY ON THE STATED RANGE**  
Created: 2026-08-18  
Depends on: repaired `P_61` scalar theorem in PR #576/#587  
RH status: **not assumed**

Let `F(Y)=F_61(Y)` and `M(Y)=M_61(Y)` be the repaired annular scalar and its
positive unsigned mass.  The retained theorem gives, for every real `Y>=67`,

\[
{1\over42}M(Y)\le F(Y)\le {1\over8}M(Y).
\tag{L-97700.1}
\]

The mass `M` is nondecreasing because it is a positive linear combination of
nondecreasing logarithmic hinges.

Fix a prime `p>=67`.  If

\[
Y/p\ge67,
\]

then

\[
\begin{aligned}
F(Y)-p^{-1/2}F(Y/p)
&\ge {1\over42}M(Y)-{1\over8\sqrt p}M(Y/p)\\
&\ge \left({1\over42}-{1\over8\sqrt p}\right)M(Y).
\end{aligned}
\]

The coefficient is strictly positive uniformly for `p>=67`, since

\[
8\sqrt{67}>42
\quad\Longleftrightarrow\quad
64\cdot67>42^2
\quad\Longleftrightarrow\quad
4288>1764.
\]

Hence

\[
\boxed{
F(Y)-p^{-1/2}F(Y/p)>0
\qquad(p\ge67,\ Y\ge67p),
}
\tag{L-97700.2}
\]

except for the vacuous case `M(Y)=0`, which does not occur in the active range.

More generally, for any finite set of distinct rough primes `P` satisfying
`Y/p>=67` for every `p in P`,

\[
F(Y)-\sum_{p\in P}p^{-1/2}F(Y/p)
\ge
M(Y)\left({1\over42}-{1\over8}\sum_{p\in P}p^{-1/2}\right).
\tag{L-97700.3}
\]

Thus every star with

\[
\sum_{p\in P}p^{-1/2}\le {4\over21}
\]

is nonnegative.

## Scope

This is a source-faithful statement for the actual `P_61` scalar, not the
unsieved dictionary.  It is useful for safe peeling and for Bellman barrier
construction.

It does **not** close arbitrary multiprime parity: after one edge is taken, the
remaining signed current is not known to stay inside the same `1/42`--`1/8`
cone.  In particular, the fixed-cutoff `l1` no-go of PR #587 remains binding.
