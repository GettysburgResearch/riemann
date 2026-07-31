# T-20501 — Conditional line-frame criterion for the final kernel and RH

Claim ID: `T-20501`  
Title: An explicit conditional simple-line frame plus one joint corrected-residual LMI gives the complete cofinal lower envelope  
Status: `PROPOSED CONDITIONAL COFINAL THEOREM — ARITHMETIC CERTIFICATE OPEN`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-20501`--`L-20505`; `T-18901`; `T-14302`; exact directed assembly  
Scope: proof-producing sufficient theorem after the infinite complement has been augmented away  
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

## 2. One explicit second frame

Choose a second finite simple-line block \(Y_j\). Define

\[
S_j
=
V_{Y_j}|_{R_j}
-
(V_{Y_j}|_{W_j})B_j^{-1}A_j.
\tag{T-20501.4}
\]

Let

\[
G_{K,j}=J_j^*G_jJ_j,
\]

and let \(M_{Y,j}\succ0\) be the selected positive zero weights. Suppose the
proof object certifies a rational or directed endpoint

\[
\boxed{
P_{Y,j}:=S_j^*M_{Y,j}S_j
\succeq
\underline\sigma_j^2G_{K,j},
\qquad
\underline\sigma_j^2\ge0.
}
\tag{T-20501.5}
\]

Finite simple-line uniqueness guarantees the existence of some injective frame
at every fixed level. It does not supply the endpoint used below.

## 3. One explicit joint corrected-residual certificate

Subtract only the finite positive \(Y_j\)-zero form from the complete Weil form.
Let

\[
R_{Y,j}=J_j^*Q_{\mathrm{rem},Y_j}J_j
\tag{T-20501.6}
\]

be the remaining exact signed kernel form. Define

\[
\boxed{
\mathcal R_j^{\rm corr}
=
R_{Y,j}
-
J_j^*L_j^*C_{+,j}^{-1}L_jJ_j.
}
\tag{T-20501.7}
\]

Suppose the proof object certifies

\[
\boxed{
\mathcal R_j^{\rm corr}
\succeq
-\overline\nu_jG_{K,j},
\qquad
\overline\nu_j\ge0.
}
\tag{T-20501.8}
\]

Put

\[
\boxed{
\underline m_j
=
\underline\sigma_j^2-\overline\nu_j.
}
\tag{T-20501.9}
\]

Then `L-20504` gives

\[
\boxed{
S_{{\rm ker},j}
=P_{Y,j}+\mathcal R_j^{\rm corr}
\succeq
\underline m_jG_{K,j}.
}
\tag{T-20501.10}
\]

This is a finite, independently checkable lower bound. It does not require
computing the exact smallest eigenvalue of the whole corrected kernel.

### Modular separated adapter

If production instead supplies

\[
R_{Y,j}\succeq-\overline\omega_jG_{K,j}
\]

and

\[
J_j^*L_j^*C_{+,j}^{-1}L_jJ_j
\preceq\overline\chi_jG_{K,j},
\]

then one may take

\[
\overline\nu_j
=
\overline\omega_j+\overline\chi_j.
\tag{T-20501.11}
\]

This is valid but can lose strict positivity.

## 4. Exact triangular composition

Let \(G_{+,j}\succ0\) be a metric on \(P_j\) and suppose

\[
C_{+,j}\succeq c_jG_{+,j},
\qquad
c_j>0.
\tag{T-20501.12}
\]

Define

\[
\mathcal L_j(k,p)
=
\left(k,p+C_{+,j}^{-1}L_jk\right).
\tag{T-20501.13}
\]

Completing the square gives

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
\tag{T-20501.14}
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
\tag{T-20501.15}
\]

If \(\underline m_j\ge-\varepsilon_j\), then

\[
\boxed{
\mathcal H_j
\succeq
-\varepsilon_jG_{\triangle,j}.
}
\tag{T-20501.16}
\]

## 5. Adapter to the production metric

Let \(G_j^{\rm full}\) be the production metric used by the cofinal lower-envelope
theorem. Certify

\[
\boxed{
G_{\triangle,j}
\preceq
\Lambda_jG_j^{\rm full},
\qquad
1\le\Lambda_j<\infty.
}
\tag{T-20501.17}
\]

Let \(\delta_j\ge0\) be the complete relative assembly radius. Then

\[
\boxed{
\lambda_{\min}(A_j,G_j^{\rm full})
\ge
-\Lambda_j(-\underline m_j)_+
-\delta_j.
}
\tag{T-20501.18}
\]

Therefore the finite certificates imply RH whenever

\[
\boxed{
\Lambda_j(-\underline m_j)_+
+
\delta_j
\longrightarrow0
}
\tag{T-20501.19}
\]

on an unbounded support sequence. This follows from `T-14302`.

If \(\underline m_j>0\), the exact level is positive and no metric-inflation
loss is paid.

## 6. Exact optimized scalar is not a reduction

For comparison only, let \(S_{{\rm ker},j}\) denote the exact fully corrected
kernel and define the exact split value for a finite selected positive form
\(P\) by

\[
b_j(P)
=
\lambda_{\min}(P,G_{K,j})
-
\left(
-\lambda_{\min}(S_{{\rm ker},j}-P,G_{K,j})
\right)_+.
\tag{T-20501.20}
\]

Allow the empty selected block \(P=0\), and put

\[
\mathfrak J_j^{\rm exact}
=
\sup_Pb_j(P).
\tag{T-20501.21}
\]

`L-20505` proves

\[
\boxed{
\left(-\mathfrak J_j^{\rm exact}\right)_+
=
\left(
-\lambda_{\min}(S_{{\rm ker},j},G_{K,j})
\right)_+.
}
\tag{T-20501.22}
\]

Thus optimizing the **exact** split is sign-equivalent to the final kernel. It
is not a hidden weakening of RH.

The genuine content of this theorem is the construction of explicit finite
proof objects with

\[
\underline m_j
\le
b_j(P_{Y,j})
\]

that satisfy (T-20501.19) without diagonalizing the complete exact operator.

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
\tag{T-20501.23}
\]

Therefore the Möbius producer gives:

1. an independent physical divisor-sum representation of the residual;
2. an independent Mellin representation;
3. optimization freedom for the Hardy realization and full Schur cross;
4. **no freedom at all** in the residual Weil matrix.

The joint corrected residual may improve when source optimization reduces the
full positive-sector cross, but the Weil component itself is invariant.

## 8. False-RH separation and scope

Under the complete form/metric capture hypotheses, false RH supplies a
supported off-line Xi-cardinal difference whose fully corrected Rayleigh
quotient is bounded above by a fixed negative constant. Consequently no
certificate sequence satisfying (T-20501.19) can coexist with false RH.

This proves that the explicit finite-certificate schedule is RH-resolving. It
does **not** manufacture the schedule from finite-dimensionality, line-zero
density, or exact local Möbius inversion.

## 9. Production certificate

A proof-facing level must bind:

- the complete packet metric and \(R/W\) decomposition;
- first-frame matrices \(A_j,B_j\);
- second-frame matrices \(C_j,D_j\);
- the exact conditional matrix \(S_j=C_j-D_jB_j^{-1}A_j\);
- selected positive weights and \(\underline\sigma_j^2\);
- the complete joint corrected residual and \(\overline\nu_j\);
- the full positive-sector block \(C_{+,j}\) and cross \(L_j\);
- the triangular metric inflation \(\Lambda_j\);
- the assembly radius \(\delta_j\);
- immutable zero, source, and matrix provenance.

A separated residual/cross certificate may be retained as an independent lower
bound, but the joint LMI should be attempted first.

## 10. Proof boundary

- Every finite algebraic implication is exact.
- The theorem is strictly weaker as a **certificate requirement** than absolute
  Möbius-tail smallness and the separated \(\omega+\chi\) adapter.
- The exact optimized split itself has the same negative part as the final
  corrected kernel.
- No current result constructs a cofinal finite certificate sequence satisfying
  (T-20501.19).
- Under false RH such a sequence cannot exist on a complete capturing
  hierarchy.
- Consequently this PR advances the proof interface but does not claim RH.
