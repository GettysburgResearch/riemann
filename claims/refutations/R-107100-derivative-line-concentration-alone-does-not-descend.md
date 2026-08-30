# R-107100 — Derivative line concentration alone does not descend

Claim ID: `R-107100`  
Status: **EXACT COUNTEREXAMPLE / BINDING FIREWALL**  
Created: 2026-08-30  
Depends on: `L-107100`  
RH status: **not involved**

Take

\[
f(x)=x^2+1.
\]

The parent has no real zero, while

\[
f'(x)=2x
\]

has one real zero and therefore has `100%` of its zeros on the real line.

At the critical point `c=0`,

\[
f(c)f''(c)=2>0,
\]

so this is a wrong-sign positive minimum. Equivalently,

\[
\mathcal L_f(0)
=f'(0)^2-f(0)f''(0)
=-2<0.
\]

On `[-2,2]`, the boundary logarithmic derivatives have opposite signs, so

\[
\varepsilon=1.
\]

The exact reverse–Rolle identity reads

\[
0=1-2+1.
\]

Thus the coefficient `2` on an extra extremum is necessary, and no theorem using only the proportion of derivative zeros on the line can imply a comparable parent proportion.

A stronger multiplicity fixture is

\[
f(x)=x^4+1,
\qquad
f'(x)=4x^3.
\]

The derivative has one real zero of multiplicity three. Its upward critical index is `+1`, so the exact defect is

\[
r+\iota=3+1=4.
\]

On `[-2,2]`,

\[
0=3-4+1.
\]

Therefore multiplicity cannot be omitted or replaced by a simple count.

This firewall does not address Xi-specific structure. It proves that the next step must use the Xi Hadamard/Pick/Fourier architecture rather than a source-free converse to Rolle.