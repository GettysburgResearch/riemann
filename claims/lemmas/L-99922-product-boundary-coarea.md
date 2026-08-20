# L-99922 — Exact Stieltjes coarea for the upward priority flux

Claim ID: `L-99922`  
Status: **PROVED EXACT COAREA IDENTITY**  
Created: 2026-08-20  
Depends on: `L-99921`  
RH status: **not assumed**

Assume the potential is a nonincreasing function of the subset product:

\[
\Phi(A)=F(P_A),
\qquad
P_A=\prod_{i\in A}p_i,
\]

and write `dnu=-dF` for its positive Stieltjes measure.  Then

\[
F(P_A)-F(p_iP_A)
=\int_{[P_A,p_iP_A)}d\nu(t).
\]

Define the first-owner crossing profile

\[
\boxed{
\mathcal C(t)
=\sum_i
\sum_{\substack{A\subseteq\{i+1,\ldots,k\}\\|A|\ {m odd}\\P_A\le t<p_iP_A}}
J_{i,A}.
}
\tag{L-99922.1}
\]

Finite Fubini gives

\[
\boxed{
\mathcal U_{\Phi}
=\int_{[1,\infty)}\mathcal C(t)\,d\nu(t).
}
\tag{L-99922.2}
\]

Every possible negative contribution is therefore attached to the first prime whose native Hasse edge crosses a literal multiplicative threshold.  No arbitrary set-valued min-cut remains in the upper bound.

For the normalized box,

\[
F_X(t)=\Phi_{67}(X/t),
\]

so `dnu_X` is supported only on its explicit activation shell.  The remaining arithmetic problem is a source-faithful bound for the crossing profile on this shell.
