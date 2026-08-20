# L-99810 — Potential-weighted Cheeger reduction for the decorated squarefree network

Claim ID: `L-99810`  
Status: **PROVED EXACT REDUCTION; WEIGHTED ISOPERIMETRIC CONSTANT OPEN**  
Created: 2026-08-20  
Depends on: PR #658 `L-99702--L-99705`; PR #659 compact scalar spine  
RH status: **unproved**

Let `V_X` be the decorated squarefree source vertices after neutral-trace cancellation of `L-99705`, with signed channel `sigma(n)=sgn beta(n)` and positive mass

\[
 m_X(n)=\frac{|\beta(n)|}{n}\Phi_X^{\Box}(n).
\]

Let `E_X` be the reversible prime-power Hasse edges of `L-99702`, with conductance

\[
 c_X(n,q)=\frac{\Lambda_g(q)g(n)}{nq}.
\]

The ordinary unweighted Cheeger constant is not uniform: vertices close to the activation boundary may have very few admissible birth edges. This is not a conclusion-facing obstruction because the box potential vanishes at the same boundary.

Define the potential-drop edge capacity

\[
 \boxed{
 \widehat c_X(n,q)
 :=c_X(n,q)\,[\Phi_X^{\Box}(n)-\Phi_X^{\Box}(nq)]
 \ge0.
 }
\tag{L-99810.1}
\]

For a set `S` of negative vertices, put

\[
 M_-(S)=\sum_{n\in S,\sigma(n)=-1}m_X(n)
\]

and let

\[
 \partial_\Phi S
 =\sum_{(n,nq)\in\partial S}\widehat c_X(n,q).
\]

Then the exact Green identity and coarea formula on the finite reversible graph reduce any source-owned orientation estimate to the weighted Cheeger inequality

\[
 \boxed{
 M_-(S)-M_+(N(S))
 \le C_X\,\partial_\Phi S
 }
\tag{L-99810.2}
\]

for all left sets `S`, where `M_+` is the positive-channel capacity and `N(S)` is the allowed one-prime neighborhood.

More precisely, if `chi_S` is the indicator of a min-cut witness, summation by parts gives

\[
 \sum_n \pi(n)f(n)\Phi_X^{\Box}(n)\chi_S(n)
 =\frac{1}{2\log X}\mathcal E_X(f,\Phi_X^{\Box}\chi_S)
   -\frac{1}{2\log X}\langle\mathfrak R_X,\Phi_X^{\Box}\chi_S\rangle_\pi.
\]

Every boundary contribution from `mathcal E_X` is supported on `partial S` and is bounded by a universal multiple of `partial_Phi S`; interior terms cancel by the exact owner identity. Therefore a uniform or subpower bound for the best constant in (L-99810.2) implies the max-flow residual bound `PXGC99700`, hence subpower negative mass for the zero-free box scalar and RH.

This lemma repairs the false uniform unweighted-Cheeger idea. It does not claim that the weighted Cheeger constant is already bounded. The remaining theorem is `PWCI99810`: prove that the optimal constant in (L-99810.2) is `X^o(1)` uniformly on logarithmic blocks.
