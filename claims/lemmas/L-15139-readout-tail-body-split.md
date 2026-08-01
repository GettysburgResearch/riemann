# L-15139 — Readout compression controls only the Schatten tail, not the central-jet body

Claim ID: `L-15139`  
Status: **PROVED OPERATOR-THEORETIC LEMMA; RIEMANN BODY DECAY NOT CLAIMED**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-01  
Dependencies: `T-15116`; spectral theorem; Schatten Hölder  
Scope: decide what an explicit coupled window/readout schedule can and cannot prove

## 1. Setup

For each window parameter `M`, let `E_M` be the complete readout Hilbert space and
let

\[
 P_{M,N}\uparrow I_{E_M}
\]

be nested finite-rank orthogonal readout projections.  Let

\[
 C_M:E_M\to\mathcal K_R
\]

be the **full window-level central finite-jet comparison map** and put

\[
 C_{M,N}=C_MP_{M,N}.
\tag{L-15139.1}
\]

The same statements hold, after isometric identification, when the finite map is
written on `P_(M,N)E_M` rather than extended by zero to `E_M`.

## 2. Exact body/tail decomposition

If `C_M in S_4`, then

\[
 \boxed{\|C_M-C_{M,N}\|_4\longrightarrow0\qquad(N\to\infty).}
\tag{L-15139.2}
\]

Moreover the reverse triangle inequality gives

\[
 \boxed{
 \big|\|C_{M,N}\|_4-\|C_M\|_4\big|
 \le \|C_M-C_{M,N}\|_4.}
\tag{L-15139.3}
\]

Consequently, along any coupled sequence `(M_j,N_j)` for which

\[
 \|C_{M_j}-C_{M_j,N_j}\|_4\to0,
\tag{L-15139.4}
\]

one has the exact equivalence

\[
 \boxed{
 \|C_{M_j,N_j}\|_4\to0
 \iff
 \|C_{M_j}\|_4\to0.}
\tag{L-15139.5}
\]

Increasing the readout dimension can remove only the compression **tail**.  It
cannot make a nonzero window-level central-jet **body** disappear.

### Proof

Finite-rank spectral projections converge strongly to the identity and finite-rank
operators are dense in every Schatten class, proving (L-15139.2).  Equation
(L-15139.3) is the norm reverse triangle inequality.  Combine it with
(L-15139.4). QED.

## 3. Explicit spectral tail

Assume the readout regularizer has a positive self-adjoint reference operator
`H_M` with spectral projection `P_(M,N)` onto its first `N` eigenvectors and

\[
 \lambda_{M,n}\ge c_\Sigma n\qquad(n\ge1),
\tag{L-15139.6}
\]

for a uniform constant `c_Sigma>0`.  Suppose

\[
 C_M=B_M(I+H_M)^{-a},
 \qquad \|B_M\|\le b_M,
 \qquad a>\frac14.
\tag{L-15139.7}
\]

Then

\[
\begin{aligned}
 \|C_M(I-P_{M,N})\|_4^4
 &\le b_M^4\sum_{n>N}(1+\lambda_{M,n})^{-4a}\\
 &\le \frac{b_M^4c_\Sigma^{-4a}}{4a-1}N^{1-4a}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 \|C_M-C_{M,N}\|_4
 \le
 \beta_M N^{1/4-a},
 \qquad
 \beta_M=
 b_Mc_\Sigma^{-a}(4a-1)^{-1/4}.}
\tag{L-15139.8}
\]

This is the quantitative content of the two-dimensional, order-two
Schatten-four regularization used by the seam construction.

## 4. Explicit coupled schedule

For any prescribed summable error sequence `eta_M>0`, choose

\[
 \boxed{
 N(M)=\left\lceil
 \left(\frac{\beta_M}{\eta_M}\right)^{1/(a-1/4)}
 \right\rceil.}
\tag{L-15139.9}
\]

Then

\[
 \|C_M-C_{M,N(M)}\|_4\le\eta_M.
\tag{L-15139.10}
\]

The canonical choice `eta_M=2^{-M}` gives

\[
 N(M)=\left\lceil
 (2^M\beta_M)^{1/(a-1/4)}
 \right\rceil.
\tag{L-15139.11}
\]

This is a genuine explicit window/readout schedule, but its conclusion is only
compression-tail decay.

## 5. Raw determinant readout tail

Let `\widetilde R_M` be the full raw comparison map,
`\widetilde R_(M,N)=\widetilde R_MP_(M,N)`, and

\[
 A_M=\widetilde R_M^*S_R\widetilde R_M,
 \qquad
 A_{M,N}=\widetilde R_{M,N}^*S_R\widetilde R_{M,N}.
\]

Since `||S_R||=1`, Schatten Hölder gives

\[
 \boxed{
 \|A_M-A_{M,N}\|_2
 \le
 (\|\widetilde R_M\|_4+
  \|\widetilde R_{M,N}\|_4)
 \|\widetilde R_M-\widetilde R_{M,N}\|_4.}
\tag{L-15139.12}
\]

Thus the same spectral schedule controls the raw determinant **readout tail**
whenever the raw comparison maps have uniform `S_4` bounds.

## 6. Exact split for the raw pullback error

Define the complete-window raw determinant transform

\[
 g_{A,M}(w)=\frac d{dw}\log\det{}_2(I+iwA_M)
\]

and the body error

\[
 \rho_M^{\rm body}(r)
 =\sup_{|w|\le r}|g_M^{\rm lin}(w)-g_{A,M}(w)|.
\tag{L-15139.13}
\]

Assume

\[
 \|A_M\|_2,\|A_{M,N}\|_2\le C,
 \qquad Cr<1,
\]

and put

\[
 \delta_{M,N}=\|A_M-A_{M,N}\|_2.
\]

The power-trace stability estimate of `T-15116` gives

\[
 \sup_{|w|\le r}|g_{A,M}(w)-g_{A,M,N}(w)|
 \le
 \delta_{M,N}\left[(1-Cr)^{-2}-1\right].
\tag{L-15139.14}
\]

Hence

\[
 \boxed{
 \begin{aligned}
 \rho_M^{\rm body}(r)-L_C(r)\delta_{M,N}
 \le{}&\rho_{M,N}(r)\\
 \le{}&\rho_M^{\rm body}(r)+L_C(r)\delta_{M,N},
 \end{aligned}}
\tag{L-15139.15}
\]

where

\[
 L_C(r)=(1-Cr)^{-2}-1.
\]

Therefore, on every schedule with `delta_(M,N(M))->0`,

\[
 \boxed{
 \rho_{M,N(M)}(r)\to0
 \iff
 \rho_M^{\rm body}(r)\to0.}
\tag{L-15139.16}
\]

Readout completeness cannot prove the missing one-contour/full-window cyclic
identity.  It can only transfer that identity from the complete window to finite
readouts.

## 7. Proof boundary

This lemma supplies the explicit coupled schedule requested in the production
programme and proves all readout-tail estimates.  It also proves that the two
original targets

\[
 \|C_{M,N(M)}\|_4\to0,
 \qquad
 \rho_{M,N(M)}(r)\to0
\]

reduce respectively to the two window-body statements

\[
 \|C_M\|_4\to0,
 \qquad
 \rho_M^{\rm body}(r)\to0.
\]

Neither body statement follows from the finite-readout Schatten estimate.
