# R-98610 — An unconstrained cross-state contraction is equivalent to the target signs

Claim ID: `R-98610`  
Status: **PROVED EXACT FINITE-DIMENSIONAL FIREWALL**  
Created: 2026-08-18  
Depends on: PR #612 `T-98600` notation  
RH status: **unproved**

Let `V` be a finite state set and let

\[
E_v^+=\Gamma_v+U_v,\qquad E_v^-=\Gamma_v-U_v,
\qquad E_v^\pm\ge0.
\]

Consider the unconstrained assertion that there exist Hilbert spaces, vectors
`phi_v^+`, `phi_v^-`, and one contraction `W` such that

\[
\|\phi_v^\pm\|^2=E_v^\pm,
\qquad W\phi_v^+=\phi_v^-
\quad(v\in V).
\]

Then this assertion is equivalent to

\[
\boxed{U_v\ge0\quad(v\in V).}
\]

Indeed, contractivity gives `E_v^-<=E_v^+`, hence `U_v>=0`. Conversely, if all
`U_v>=0`, take orthonormal vectors `e_v`, put

\[
\phi_v^+=\sqrt{E_v^+}e_v,\qquad
\phi_v^-=\sqrt{E_v^-}e_v,
\]

and define

\[
We_v=
\begin{cases}
\sqrt{E_v^-/E_v^+}\,e_v,&E_v^+>0,\\
0,&E_v^+=0.
\end{cases}
\]

This is a contraction and has the required action.

Therefore a theorem stated only as existence of features and a common
contraction does not produce the signs: it repackages them. A noncircular
producer must prescribe the cross-state Gram entries and transition covariance
independently of the unknown `U_v>=0` conclusions.
