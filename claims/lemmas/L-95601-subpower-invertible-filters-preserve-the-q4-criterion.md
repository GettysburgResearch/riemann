# L-95601 — Every subpower-invertible scale filter preserves the Q4/RH criterion

Claim ID: `L-95601`  
Status: **PROPOSED COMPLETE EXACT FILTER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95600`

Let

\[
(SF)(X)=F(X/2)
\]

and let

\[
P(S)=\sum_{r=0}^{R}c_rS^r,
\qquad c_0=1.
\]

Suppose the formal inverse is

\[
P(S)^{-1}=\sum_{j\ge0}b_jS^j
\]

and, with \(L=\lfloor\log_2X\rfloor+O(1)\),

\[
\sum_{j\le L}|b_j|=\exp(o(L)).
\tag{L-95601.1}
\]

Then

\[
\boxed{
F(X)=X^{o(1)}
\Longleftrightarrow
P(S)F(X)=X^{o(1)}.
}
\tag{L-95601.2}
\]

The forward implication is finite linearity. For the reverse implication,
truncate the exact inverse after the last scale above the fixed base range.
The inverse coefficient mass is \(X^{o(1)}\), and the finitely many terminal
values also contribute \(X^{o(1)}\).

## Fixed critical-Haar differences

For every fixed integer \(k\ge1\),

\[
(I-S)^{-k}
=
\sum_{j\ge0}
\binom{j+k-1}{k-1}S^j,
\]

and

\[
\sum_{j=0}^{L}\binom{j+k-1}{k-1}
=
\binom{L+k}{k}
=
O_k(L^k).
\tag{L-95601.3}
\]

Thus any fixed number of additional vanishing Mellin moments preserves the
subpower criterion and cannot make the Q4 gate weaker than RH.

The same remains true for an endpoint-dependent order \(k=k(X)\) whenever

\[
k\log(1+L/k)=o(L).
\tag{L-95601.4}
\]

Therefore fixed finite filters, fixed moment annihilators, and a broad class of
slowly growing filters merely repackage the same RH criterion.


---
