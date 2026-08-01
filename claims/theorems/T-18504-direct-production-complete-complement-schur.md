# T-18504 — Direct production Schur certificate on the complete harmonic complement

Claim ID: `T-18504`  
Title: A directed trial-lift LMI on the actual Suzuki complement replaces the frame–tail threshold and feeds the full three-block floor  
Status: `PROVED CONDITIONAL TRANSFER; PRODUCTION LMI OPEN`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `L-18512`; triangular Schur theorem `L-15306`; cofinal lower-envelope theorem `T-14302`  
Scope: shortest production continuation on the actual complete packet  
Related candidates: none

## 1. Direct complete-complement certificate

At support `lambda`, let

\[
U_\lambda
=R_\lambda\oplus_{G_{C,\lambda}}W_\lambda,
\qquad
W_\lambda
=R_\lambda^{\perp_{G_C}}\cap U_\lambda.
\tag{T-18504.1}
\]

Let the complete low/ambient form be

\[
\mathcal H_\lambda
=
\begin{pmatrix}
B_\lambda&L_\lambda^*\\
L_\lambda&C_\lambda
\end{pmatrix},
\qquad
C_\lambda\succeq h_\lambda M_\lambda>0.
\tag{T-18504.2}
\]

Choose any proof-grade trial harmonic solve

\[
X_\lambda:W_\lambda\to E_\lambda
\]

and form the exact residual

\[
\mathscr R_\lambda
=L_\lambda Q_{W,\lambda}-C_\lambda X_\lambda.
\tag{T-18504.3}
\]

Define

\[
\boxed{
\mathscr D_\lambda
=J_{X_\lambda}^*\mathcal H_\lambda J_{X_\lambda}
-h_\lambda^{-1}
 \mathscr R_\lambda^*M_\lambda^{-1}\mathscr R_\lambda.
}
\tag{T-18504.4}
\]

If directed arithmetic proves

\[
\boxed{
\mathscr D_\lambda\succeq m_\lambda G_{W,\lambda},
\qquad m_\lambda>0,
}
\tag{T-18504.5}
\]

then `L-18512` gives the sharp direct block statement

\[
\boxed{
B_{W,\lambda}
-(L_\lambda Q_{W,\lambda})^*
 C_\lambda^{-1}
 (L_\lambda Q_{W,\lambda})
\succeq
m_\lambda G_{W,\lambda}.
}
\tag{T-18504.6}
\]

No selected-zero Gram, omitted-zero budget, generalized-eigenvalue count, or
principal-angle estimate is a hypothesis.

## 2. Full three-block composition

Return to the radical/complete-complement/ambient decomposition. Suppose

\[
B_{R,\lambda}
\succeq-e_\lambda G_{R,\lambda}
\tag{T-18504.7}
\].

Write the raw radical/complement cross in the low block as

\[
X_{RW,\lambda}=Q_{W,\lambda}^*B_\lambda Q_{R,\lambda},
\]

put

\[
Z_{R,\lambda}=L_\lambda Q_{R,\lambda},
\qquad
Z_{W,\lambda}=L_\lambda Q_{W,\lambda},
\]

and define the exact cross after ambient elimination by

\[
\widetilde X_\lambda
=X_{RW,\lambda}-Z_{W,\lambda}^*C_\lambda^{-1}Z_{R,\lambda}.
\tag{T-18504.8}
\]

Assume

\[
\begin{aligned}
&Z_{R,\lambda}^*C_\lambda^{-1}Z_{R,\lambda}\\
&\qquad
+m_\lambda^{-1}
 \widetilde X_\lambda^*
 G_{W,\lambda}^{-1}
 \widetilde X_\lambda
\preceq
\kappa_\lambda G_{R,\lambda}.
\end{aligned}
\tag{T-18504.9}
\]

Then the triangular Schur theorem yields

\[
\boxed{
\lambda_{\min}
(\mathcal H_\lambda,\mathcal G_\lambda)
\ge
-(e_\lambda+\kappa_\lambda+\delta_\lambda),
}
\tag{T-18504.10}
\]

where `delta_lambda` is the complete directed assembly radius.

## 3. Cofinal theorem

If an unbounded support sequence admits direct certificates (T-18504.5) and

\[
\boxed{
 e_\lambda\to0,
 \qquad
 \kappa_\lambda\to0,
 \qquad
 \delta_\lambda\to0,
}
\tag{T-18504.11}
\]

then

\[
\lambda_{\min}
(\mathcal H_\lambda,\mathcal G_\lambda)
\longrightarrow0^-.
\tag{T-18504.12}
\]

The existing monotone cofinal lower-envelope theorem then implies RH.

## 4. Production specialization

For the endpoint-profile Suzuki packet, `L-18512` gives the directed matrix

\[
\begin{aligned}
\mathscr D_\lambda
={}&P_{\lambda,W}+E_{\lambda,W}\\
&-Z_{W,\lambda}^*X_\lambda
-X_\lambda^*Z_{W,\lambda}
+X_\lambda^*C_\lambda X_\lambda\\
&-h_\lambda^{-1}
 \mathscr R_\lambda^*M_\lambda^{-1}\mathscr R_\lambda.
\end{aligned}
\tag{T-18504.13}
\]

Here:

- `P_(lambda,W)` is the complete finite/local and pole-cancelled endpoint block;
- `E_(lambda,W)` is the complete centered terminal-prime Hankel matrix;
- all prime powers in the exact Suzuki support are enumerated;
- `X_lambda` is one finite form-core harmonic solve;
- the last line is the a posteriori solve moat.

The finite LMI (T-18504.5) is therefore a direct arithmetic calculation on the
actual packet. Zero-side frames are independent reproduction tools, not part
of the lower-bound logic.

## 5. Exact obstruction when the production sign is not closed

Define

\[
\rho_\lambda
=
\left\|
\left[
G_{W,\lambda}^{-1/2}
\mathscr D_\lambda
G_{W,\lambda}^{-1/2}
\right]_-
\right\|.
\tag{T-18504.14}
\]

Then

\[
S_{W,\lambda}
\succeq-\rho_\lambda G_{W,\lambda}.
\tag{T-18504.15}
\]

As the harmonic solve, Galerkin core, and directed precision are refined,
`rho_lambda` converges to the negative endpoint of the actual complete-
complement Schur matrix. Consequently:

- `rho_lambda=0` closes the finite `W_lambda` block;
- `rho_lambda->0` is the exact cofinal direct-block target;
- a strict negative interval persisting under independent refinement is a
  genuine finite low-block candidate, not an omitted-zero or conditioning
  artefact.

This is the smallest exact obstruction left on `W_lambda`.

## 6. Proof boundary

- The transfer from (T-18504.5) to the full floor is exact.
- The theorem eliminates the stronger scalar condition
  `epsilon < B_T+beta < Sigma` from the production route.
- It does not assert the sign of any uncomputed Suzuki matrix.
- The first required artifact is now one actual `W_lambda` basis, complete
  arithmetic block, trial harmonic solve, and residual LMI.
- RH is not claimed before a cofinal sequence of such proof objects is produced.
