# L-15626 — A compression floor controls the extra-low spectral trace

Claim ID: `L-15626`  
Title: A strict floor on the packet complement bounds the nonreducing low-spectral trace by one quadratic cross term  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: spectral theorem below an isolated threshold; finite-rank block algebra  
Scope: the sole remaining term in `L-15625`  
Related counterexample candidates: none

## 1. Setting

Let `A` be self-adjoint on a Hilbert space `H`. Let `P` be a finite-rank
orthogonal projection of rank `d` and put

\[
 Q=I-P.
 \tag{L-15626.1}
\]

Fix real numbers

\[
 \Gamma<\gamma.
 \tag{L-15626.2}
\]

Assume the spectrum of `A` below `Gamma` is discrete with finite multiplicity
(the localized compact-resolvent setting is more than sufficient), and assume
the **compression** floor

\[
 \boxed{
 QAQ\succeq\gamma Q
 \quad\hbox{on }\operatorname{Ran}Q.}
 \tag{L-15626.3}
\]

Put

\[
 X=QAP:\operatorname{Ran}P\to\operatorname{Ran}Q.
 \tag{L-15626.4}
\]

The projection `Q` is not assumed to reduce `A`.

## 2. Main spectral-leakage bound

Then

\[
 \boxed{
 \operatorname{Tr}\!\left[Q(\Gamma I-A)_+Q\right]
 \le
 {\|X\|_{\mathrm{HS}}^2\over4(\gamma-\Gamma)}.}
 \tag{L-15626.5}
\]

In particular, if

\[
 X^*X=PAQAP\preceq\beta^2P,
 \tag{L-15626.6}
\]

then

\[
 \boxed{
 \operatorname{Tr}\!\left[Q(\Gamma I-A)_+Q\right]
 \le
 {d\beta^2\over4(\gamma-\Gamma)}.}
 \tag{L-15626.7}
\]

Thus a positive compression floor is enough to control the exact spectral
normal-form term of `L-15625`, even though the packet/complement decomposition
is not invariant under `A`.

## 3. Proof

Let

\[
 A\phi_n=\lambda_n\phi_n,
 \qquad \lambda_n<\Gamma,
 \tag{L-15626.8}
\]

be an orthonormal basis of the spectral subspace below `Gamma`, with
multiplicity retained. Write

\[
 p_n=P\phi_n,
 \qquad
 q_n=Q\phi_n.
 \tag{L-15626.9}
\]

Projecting the eigenvalue equation onto `Ran Q` gives

\[
 (QAQ-\lambda_n)q_n=-Xp_n.
 \tag{L-15626.10}
\]

By (L-15626.3),

\[
 \|q_n\|
 \le
 {\|Xp_n\|\over\gamma-\lambda_n}.
 \tag{L-15626.11}
\]

Set

\[
 \delta=\gamma-\Gamma>0,
 \qquad
 x=\gamma-\lambda_n>\delta.
\]

The elementary sharp inequality

\[
 {\Gamma-\lambda_n\over(\gamma-\lambda_n)^2}
 ={x-\delta\over x^2}
 \le {1\over4\delta}
 \tag{L-15626.12}
\]

follows by maximizing the right side at `x=2 delta`. Therefore

\[
 (\Gamma-\lambda_n)\|q_n\|^2
 \le
 {\|Xp_n\|^2\over4(\gamma-\Gamma)}.
 \tag{L-15626.13}
\]

Summing gives

\[
 \begin{aligned}
 \operatorname{Tr}\!\left[Q(\Gamma I-A)_+Q\right]
 &=\sum_{\lambda_n<\Gamma}
   (\Gamma-\lambda_n)\|q_n\|^2\\
 &\le {1\over4(\gamma-\Gamma)}
   \sum_{\lambda_n<\Gamma}\|Xp_n\|^2.
 \end{aligned}
 \tag{L-15626.14}
\]

Since

\[
 \sum_{\lambda_n<\Gamma}|p_n\rangle\langle p_n|
 =P\mathbf1_{(-\infty,\Gamma)}(A)P
 \preceq P,
 \tag{L-15626.15}
\]

we have

\[
 \sum_{\lambda_n<\Gamma}\|Xp_n\|^2
 \le\operatorname{Tr}(X^*X)
 =\|X\|_{\mathrm{HS}}^2.
 \tag{L-15626.16}
\]

This proves (L-15626.5). Equation (L-15626.6) implies

\[
 \operatorname{Tr}(X^*X)\le d\beta^2,
\]

which proves (L-15626.7). QED.

## 4. Cofinal corollary

For a sequence `A_j,P_j,Q_j`, suppose

\[
 Q_jA_jQ_j\succeq\gamma_jQ_j,
 \qquad
 \gamma_j>\Gamma_j,
 \tag{L-15626.17}
\]

and

\[
 P_jA_jQ_jA_jP_j\preceq\beta_j^2P_j.
 \tag{L-15626.18}
\]

If

\[
 \boxed{
 {d_j\beta_j^2\over
  (\gamma_j-\Gamma_j)(\Gamma_j-t_j)}
 \longrightarrow0,}
 \tag{L-15626.19}
\]

then

\[
 \boxed{
 \operatorname{Tr}
 \left[Q_j(\Gamma_jI-A_j)_+Q_j\right]
 =o(\Gamma_j-t_j).}
 \tag{L-15626.20}
\]

Consequently the requested spectral-tail term is closed once a genuine
compression floor with a moat above `Gamma_j` has been proved. No spectral
invariance or packet-angle theorem is required.

For the Gevrey/disjoint-bump packets of `L-15617/L-15619`, `d_j` has at most
near-quadratic growth while `beta_j` beats every inverse power. Hence
(L-15626.19) is automatic for every polynomial or logarithmic moat. The only
remaining substantive task is the compression floor (L-15626.17).

## 5. Sharpness

The factor `1/[4(gamma-Gamma)]` is sharp already for a two-dimensional block.
Equality in the scalar estimate occurs when

\[
 \lambda=2\Gamma-\gamma.
\]

The theorem cannot be improved to a bound independent of the complement moat:
as `gamma` decreases to `Gamma`, an arbitrarily small cross map can rotate a
low eigenvector deeply into `Ran Q`.

## 6. Proof boundary

- The spectral-leakage inequality is exact.
- It closes the distinction between a compression floor and the spectral
  functional-calculus trace in `L-15625`.
- It does not produce the compression floor `QAQ>=gamma Q` for the complete
  zeta packet.
- No RH conclusion is claimed without that cofinal floor.
