# T-20501 — Conditional line-frame criterion for the final kernel and RH

Claim ID: `T-20501`  
Title: A conditional simple-line frame minus its one-sided residual and Schur cross gives the complete cofinal lower envelope  
Status: `PROPOSED CONDITIONAL COFINAL THEOREM — ARITHMETIC MOAT OPEN`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20501`, `L-20502`; `T-18901`; `T-14302`; exact directed assembly  
Scope: shortest complete composition after the infinite complement has been augmented away  
Related counterexample candidates: none

## 1. Cofinal finite packets

At level \(j\), let \(U_j\) be the complete finite packet produced after the
canonical ambient-deficit augmentation of `T-18901`. Let

\[
U_j=R_j\oplus_{G_j}W_j.
\tag{T-20501.1}
\]

Choose a first proof-grade simple-line block \(Z_j\) such that

\[
B_j=V_{Z_j}|_{W_j}
\]

is invertible. Put

\[
K_j
=
U_j\cap\ker V_{Z_j}
=
\operatorname{Ran}J_j,
\qquad
J_j=
\begin{pmatrix}
I\\
-B_j^{-1}A_j
\end{pmatrix},
\tag{T-20501.2}
\]

where \(A_j=V_{Z_j}|_{R_j}\).

The quotient represented by \(W_j\) is handled by the direct frame--tail theorem
of PR #191. The remaining finite sign is the Schur-corrected kernel \(K_j\).

## 2. Second conditional line frame

Choose a second finite simple-line block \(Y_j\). Define

\[
S_j
=
V_{Y_j}|_{R_j}
-
(V_{Y_j}|_{W_j})
B_j^{-1}A_j.
\tag{T-20501.3}
\]

Let

\[
G_{K,j}=J_j^*G_jJ_j,
\]

and let \(M_{Y,j}\succ0\) be the selected positive zero weights. Suppose the
directed finite frame certificate proves

\[
\boxed{
S_j^*M_{Y,j}S_j
\succeq
\sigma_j^2G_{K,j}.
}
\tag{T-20501.4}
\]

The finite simple-line uniqueness theorem guarantees that some
\(\sigma_j^2>0\) exists at every fixed level. No rate is inherited.

## 3. One-sided residual and Schur cross

Subtract only the finite positive \(Y_j\)-zero form from the complete Weil form.
Let \(R_{Y,j}\) be the remaining exact signed kernel form.

Assume the two directed LMIs

\[
\boxed{
J_j^*R_{Y,j}J_j
\succeq
-\omega_jG_{K,j},
}
\tag{T-20501.5}
\]

and

\[
\boxed{
J_j^*Z_{{\rm ker},j}^*C_j^{-1}Z_{{\rm ker},j}J_j
\preceq
\chi_jG_{K,j}.
}
\tag{T-20501.6}
\]

Then `L-20502` gives

\[
\boxed{
S_{{\rm ker},j}
\succeq
m_jG_{K,j},
\qquad
m_j=\sigma_j^2-\omega_j-\chi_j.
}
\tag{T-20501.7}
\]

Only the negative residual endpoint enters.

## 4. Complete finite level

Let the selected-\(Z_j\) visible quotient have directed floor \(v_j>0\), and let
the remaining infinite-dimensional complement have floor \(\Gamma_j>0\).
Those are supplied by the existing frame--tail and canonical augmentation
layers.

Let \(\delta_j\ge0\) be the complete relative assembly radius between the exact
operator and the proof-facing block matrix.

Block min--max and the exact Schur reductions give

\[
\boxed{
\lambda_{\min}(A_j,G_j^{\rm full})
\ge
\min\{\Gamma_j,v_j,m_j\}
-\delta_j.
}
\tag{T-20501.8}
\]

In particular, if

\[
m_j\ge-\varepsilon_j,
\qquad
\varepsilon_j\to0,
\qquad
\delta_j\to0,
\tag{T-20501.9}
\]

while \(\Gamma_j,v_j>0\), then

\[
\boxed{
\lambda_{\min}(A_j,G_j^{\rm full})
\ge
-(\varepsilon_j+\delta_j)
\longrightarrow0^-.
}
\tag{T-20501.10}
\]

The existing monotone cofinal lower-envelope theorem `T-14302` then implies RH.

## 5. Exact optimized scalar

For a fixed first frame \(Z_j\), define

\[
\mathfrak C_j(Z_j)
=
\sup_{Y_j}
\left[
\sigma_{Y_j\mid Z_j}^2-\omega_{Y_j\mid Z_j}
\right]
-\chi_j.
\tag{T-20501.11}
\]

The supremum ranges over compatible finite proof-grade simple-line blocks and
complete one-sided residual certificates in the same normalization.

Define

\[
\boxed{
\mathfrak C_j
=
\sup_{Z_j}\mathfrak C_j(Z_j).
}
\tag{T-20501.12}
\]

The exact cofinal scalar target is

\[
\boxed{
\liminf_{j\to\infty}\mathfrak C_j\ge0.
}
\tag{T-20501.13}
\]

A strictly positive cofinal moat is stronger than necessary. Approaching zero
from below is enough.

This is the conditional-kernel counterpart of the visible frame--tail scalar
\(\mathfrak M_j\) on PR #191.

## 6. Möbius producer and invariance

The local Möbius theorem of PR #204 supplies an explicit exact radical
extension

\[
\mathcal R_j=J_j+T_j
\]

for every complete kernel vector.

For every finite \(Y_j\),

\[
Q_{\mathrm{rem},Y_j}(T_jc,T_jd)
=
Q_{\mathrm{rem},Y_j}(J_jc,J_jd).
\tag{T-20501.14}
\]

Therefore the Möbius producer gives:

1. an independent physical divisor-sum representation of the residual;
2. an independent Mellin representation;
3. optimization freedom for the Hardy realization and Schur cross;
4. **no freedom at all** in the residual Weil matrix \(\omega_j\).

This prevents optimization of the source from being mistaken for proof of the
sign.

## 7. False-RH separation

Under the complete form/metric capture hypotheses, false RH supplies a
supported off-line Xi-cardinal difference whose corrected Rayleigh quotient is
bounded above by a fixed negative constant.

Every finite selected simple-line form vanishes on the limiting global
difference. Thus

\[
\limsup_j\mathfrak C_j<0
\]

along any hierarchy that captures that direction and has vanishing assembly
error.

Conversely, under RH the complete Weil form is positive. The complete residual
after removing a finite positive line block is then the positive contribution
of all remaining real zeros, so one may take

\[
\omega_j=0.
\]

The finite Schur cross remains explicitly represented by \(\chi_j\).

Hence (T-20501.13), with complete capture, is another exact RH-bearing
formulation rather than a soft consequence of finite-dimensionality.

## 8. Production certificate

A proof-facing level must bind:

- the complete packet metric and \(R/W\) decomposition;
- first-frame matrices \(A_j,B_j\);
- second-frame matrices \(C_j,D_j\);
- the exact conditional matrix \(S_j=C_j-D_jB_j^{-1}A_j\);
- selected positive weights;
- a directed lower LMI for the complete signed residual after selected
  deflation;
- the exact complement cross LMI;
- the visible and ambient floors;
- the assembly radius;
- immutable zero, source, and matrix provenance.

No root of a floating matrix and no dimension-only comparison is accepted.

## 9. Proof boundary

- Every finite implication is exact.
- The theorem is strictly weaker than absolute Möbius-tail smallness.
- No current result proves the cofinal one-sided residual moat
  (T-20501.13).
- Under false RH that moat must fail by a fixed amount on a capturing
  hierarchy.
- Consequently this PR advances the proof interface but does not claim RH.
