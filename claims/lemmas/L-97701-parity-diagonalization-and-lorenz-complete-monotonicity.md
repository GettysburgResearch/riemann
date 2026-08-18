# L-97701 — Parity diagonalization and the Lorenz complete-monotonicity cone

Claim ID: `L-97701`  
Status: **PROVED EXACT OPERATOR THEOREM; ARITHMETIC CONE MEMBERSHIP OPEN**  
Created: 2026-08-18  
Depends on: `L-97700`  
RH status: **unproved**

Let `D_0^+(X,lambda),D_0^-(X,lambda)` be the two Lorenz slacks of the complete small-prime `P_61` source. For a rough prime `p`, put

\[
\rho_p=p^{-1/2},\qquad (U_ph)(X)=h(X/p).
\]

For a finite rough-prime set `Q`, define

\[
\mathcal P_Q^+=\prod_{p\in Q}(I+\rho_pU_p),
\qquad
\mathcal P_Q^-=\prod_{p\in Q}(I-\rho_pU_p).
\tag{L-97701.1}
\]

Put \(S_0=D_0^++D_0^-\) and \(A_0=D_0^+-D_0^-\). The prime recurrence of `L-97700` diagonalizes as

\[
S_Q=\mathcal P_Q^+S_0,
\qquad A_Q=\mathcal P_Q^-A_0.
\tag{L-97701.2}
\]

Since \(A_0=2D_0^+-S_0\),

\[
\boxed{D_Q^+=\mathcal P_Q^-D_0^++\frac{\mathcal P_Q^+-\mathcal P_Q^-}{2}S_0.}
\tag{L-97701.3}
\]

Moreover

\[
\frac{\mathcal P_Q^+-\mathcal P_Q^-}{2}
=
\sum_{\substack{A\subseteq Q\\|A|\text{ odd}}}
\left(\prod_{p\in A}\rho_p\right)U_A,
\tag{L-97701.4}
\]

so the second term in (L-97701.3) is universally nonnegative because `S_0>=0`.

Define

\[
\boxed{\mathrm{LBP}_{67}:\quad \mathcal P_Q^-D_0^+(X,\lambda)\ge0}
\tag{L-97701.5}
\]

for every finite rough set `Q`, every real endpoint `X>0`, and every real `lambda`. Then

\[
\boxed{\mathrm{LBP}_{67}\Longrightarrow\mathrm{CPSL}_{67}.}
\tag{L-97701.6}
\]

This is a sufficient theorem, not an equivalence claim. At `lambda=0`, `S_0=0`, hence

\[
D_Q^+(X,0)=\mathcal P_Q^-D_0^+(X,0),
\tag{L-97701.7}
\]

so no positive cushion is hidden at the RH-bearing scalar coordinate.

If `Q` contains the already-installed larger primes and `p` is next, put \(G_Q=\mathcal P_Q^-D_0^+\). Then

\[
\boxed{G_{Q\cup\{p\}}(X,\lambda)=G_Q(X,\lambda)-\rho_pG_Q(X/p,\lambda).}
\tag{L-97701.8}
\]

Thus `LBP67` is exactly the descending family of Bellman inequalities

\[
G_Q(X,\lambda)\ge\rho_pG_Q(X/p,\lambda).
\tag{L-97701.9}
\]

The operator decomposition and invariant-cone mechanism are proved here. Arithmetic membership of the base profile for every finite rough set remains open.