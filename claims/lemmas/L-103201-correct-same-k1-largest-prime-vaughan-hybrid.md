# L-103201 — Correct same-K1 largest-prime/Vaughan hybrid

Claim ID: `L-103201`  
Status: **PROVED EXACT TRANSLATION; TERMINAL ESTIMATE OPEN**  
Created: 2026-08-20  
Depends on: PR #688 largest-prime identity; PR #685 Vaughan identity  
RH status: **unproved**

Use one scalar throughout:

\[
G_1(X)=\sum_n\frac{\mu(n)}{\sqrt n}K_1(X/n).
\]

Applying largest-prime ownership directly to \(K_1\) gives

\[
\boxed{G_1=S_1+R_1,}
\]

where the \(Y_X=(\log X)^{3/2}\)-smooth sector satisfies

\[
S_1(X)=X^{-1/6+o(1)}
\]

and belongs to \(L^1(dX/X)\).

Applying the exact zero-moment Vaughan identity to the same scalar gives

\[
\boxed{G_1=T_1+B_1,}
\]

with

\[
T_1(X)=O(X^{-1/6})
\]

and \(B_1\) the balanced compact trilinear.

Therefore

\[
\boxed{R_1-B_1=T_1-S_1\in L^1([2,\infty),dX/X).}
\]

Since

\[
|a_--b_-|\le|a-b|,
\]

\[
\boxed{
\int_2^Y(R_1)_-\frac{dX}{X}=Y^{o(1)}
\iff
\int_2^Y(B_1)_-\frac{dX}{X}=Y^{o(1)}.
}
\]

This is the correctly typed hybrid coordinate change.

It is not a proof of XD.  `L-103200` shows that a regional norm can remain
power-sized even after the extra notch.  The open estimate must be imposed on
the complete common terminal scalar, after every deterministic carrier has
cancelled.
