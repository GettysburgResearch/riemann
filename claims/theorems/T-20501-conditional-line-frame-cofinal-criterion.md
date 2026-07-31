# T-20501 — Conditional line-frame criterion for the final kernel and RH

Claim ID: `T-20501`  
Title: A conditional simple-line frame minus its one-sided residual and full Schur cross gives the complete cofinal lower envelope  
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

Let \(P_j\) be the **entire remaining positive sector complementary to**
\(K_j\). It includes the selected-zero visible quotient and the ambient
complement. In coordinates \(K_j\oplus P_j\), write the exact block

\[
\mathcal H_j=
\begin{pmatrix}
B_{K,j}&L_j^*\\
L_j&C_{+,j}
\end{pmatrix},
\qquad
C_{+,j}\succ0.
\tag{T-20501.3}
\]

All staged visible/ambient eliminations must be assembled into this one positive
block before the kernel theorem is applied.

## 2. Second conditional line frame

Choose a second finite simple-line block \(Y_j\). Define

\[
S_j
=
V_{Y_j}|_{R_j}
-
(V_{Y_j}|_{W_j})
B_j^{-1}A_j.
\tag{T-20501.4}
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
\tag{T-20501.5}
\]

The finite simple-line uniqueness theorem guarantees that some
\(\sigma_j^2>0\) exists at every fixed level. No rate is inherited.

## 3. One-sided residual and full positive-sector cross

Subtract only the finite positive \(Y_j\)-zero form from the complete Weil form.
Let \(R_{Y,j}\) be the remaining exact signed kernel form.

Assume the two directed LMIs

\[
\boxed{
J_j^*R_{Y,j}J_j
\succeq
-\omega_jG_{K,j},
}
\tag{T-20501.6}
\]

and

\[
\boxed{
J_j^*L_j^*C_{+,j}^{-1}L_jJ_j
\preceq
\chi_jG_{K,j}.
}
\tag{T-20501.7}
\]

Then `L-20502` gives the **fully** Schur-corrected kernel

\[
\boxed{
S_{{\rm ker},j}
\succeq
m_jG_{K,j},
\qquad
m_j=\sigma_j^2-\omega_j-\chi_j.
}
\tag{T-20501.8}
\]

Only the negative residual endpoint enters.

## 4. Exact triangular composition

Let \(G_{+,j}\succ0\) be a metric on \(P_j\) and suppose

\[
C_{+,j}\succeq c_jG_{+,j},
\qquad
c_j>0.
\tag{T-20501.9}
\]

Define the triangular coordinate map

\[
\mathcal L_j(k,p)
=
\left(
 k,
 p+C_{+,j}^{-1}L_jk
\right).
\tag{T-20501.10}
\]

Completing the square gives the exact identity

\[
\boxed{
\langle\mathcal H_j(k,p),(k,p)\rangle
=
\langle S_{{\rm ker},j}k,k\rangle
+
\left\langle
C_{+,j}
\left(p+C_{+,j}^{-1}L_jk\right),
\left(p+C_{+,j}^{-1}L_jk\right)
\right\rangle.
}
\tag{T-20501.11}
\]

Put

\[
\boxed{
G_{\triangle,j}
=
\mathcal L_j^*
\operatorname{diag}(G_{K,j},G_{+,j})
\mathcal L_j.
}
\tag{T-20501.12}
\]

If \(m_j\ge-\varepsilon_j\) with \(\varepsilon_j\ge0\), then

\[
\boxed{
\mathcal H_j
\succeq
-\varepsilon_jG_{\triangle,j}.
}
\tag{T-20501.13}
\]

This is the exact full-block conclusion. It does not require a false
"minimum of separate restrictions" step.

## 5. Adapter to the production metric

Let \(G_j^{\rm full}\) be the production metric used by the cofinal lower-envelope
theorem. Certify a finite triangular inflation endpoint

\[
\boxed{
G_{\triangle,j}
\preceq
\Lambda_jG_j^{\rm full},
\qquad
1\le\Lambda_j<\infty.
}
\tag{T-20501.14}
\]

Let \(\delta_j\ge0\) be the complete relative assembly radius. Equations
(T-20501.13)--(T-20501.14) give

\[
\boxed{
\lambda_{\min}(A_j,G_j^{\rm full})
\ge
-\Lambda_j\varepsilon_j-\delta_j.
}
\tag{T-20501.15}
\]

Therefore the valid cofinal schedule is

\[
\boxed{
\Lambda_j\varepsilon_j\longrightarrow0,
\qquad
\delta_j\longrightarrow0.
}
\tag{T-20501.16}
\]

The existing monotone cofinal lower-envelope theorem `T-14302` then implies RH.

If \(m_j>0\), the exact block is positive and no metric-inflation loss is paid.

## 6. Exact optimized scalar

For a fixed first frame \(Z_j\), define

\[
\mathfrak C_j(Z_j)
=
\sup_{Y_j}
\left[
\sigma_{Y_j\mid Z_j}^2-\omega_{Y_j\mid Z_j}
\right]
-\chi_j,
\tag{T-20501.17}
\]

where every term is certified in the same full positive-sector block and
metric. Define

\[
\boxed{
\mathfrak C_j
=
\sup_{Z_j}\mathfrak C_j(Z_j).
}
\tag{T-20501.18}
\]

A sufficient exact scalar schedule is

\[
\boxed{
\Lambda_j(-\mathfrak C_j)_+\longrightarrow0.
}
\tag{T-20501.19}
\]

A strictly positive cofinal moat is stronger than necessary. Approaching zero
from below at the metric-adjusted rate is enough.

This is the conditional-kernel counterpart of the visible frame--tail scalar
\(\mathfrak M_j\) on PR #191.

## 7. Möbius producer and invariance

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
\tag{T-20501.20}
\]

Therefore the Möbius producer gives:

1. an independent physical divisor-sum representation of the residual;
2. an independent Mellin representation;
3. optimization freedom for the Hardy realization and full Schur cross;
4. **no freedom at all** in the residual Weil matrix \(\omega_j\).

This prevents optimization of the source from being mistaken for proof of the
sign.

## 8. False-RH separation and scope

Under the complete form/metric capture hypotheses, false RH supplies a
supported off-line Xi-cardinal difference whose fully corrected Rayleigh
quotient is bounded above by a fixed negative constant. Consequently no
certificate sequence satisfying (T-20501.16) can coexist with false RH.

This proves that a cofinal conditional-frame moat is RH-resolving. It does **not**
prove the converse statement that RH automatically supplies this particular
separately bounded decomposition; conservative frame, residual, cross, or
metric endpoints may lose a positive exact cancellation.

Thus `T-20501` is a noncircular sufficient theorem, not an asserted new
iff-formulation.

## 9. Production certificate

A proof-facing level must bind:

- the complete packet metric and \(R/W\) decomposition;
- first-frame matrices \(A_j,B_j\);
- second-frame matrices \(C_j,D_j\);
- the exact conditional matrix \(S_j=C_j-D_jB_j^{-1}A_j\);
- selected positive weights;
- a directed lower LMI for the complete signed residual after selected
  deflation;
- the full positive-sector block \(C_{+,j}\) and cross \(L_j\);
- the triangular metric inflation \(\Lambda_j\);
- the assembly radius;
- immutable zero, source, and matrix provenance.

No root of a floating matrix and no dimension-only comparison is accepted.

## 10. Proof boundary

- Every finite algebraic implication is exact.
- The theorem is strictly weaker than absolute Möbius-tail smallness.
- It corrects the composition to use the entire positive sector and a declared
  triangular metric adapter.
- No current result proves the cofinal one-sided residual moat
  (T-20501.19).
- Under false RH that moat must fail on a complete capturing hierarchy.
- Consequently this PR advances the proof interface but does not claim RH.
