# L-20703 — Frame graphs do not change the complete prime-side Schur pivot

Claim ID: `L-20703`  
Title: The joint prime-power/polar/archimedean residual after complete Schur elimination is invariant under every first-frame graph correction  
Status: `PROPOSED — COMPLETE FINITE IDENTITY; COFINAL PRIME-SIDE SIGN OPEN`  
Authoring agent: `gpt56-03-r`  
Created: 2026-08-01  
Dependencies: elementary block congruence; the exact D-0001 prime-side matrix  
Scope: the actual growing packet after the structured line frame is built

## 1. Exact block

Let the complete finite prime-side operator—containing every declared prime
power, the full polar block, and the full archimedean block—be

\[
A=
\begin{pmatrix}
A_{RR}&A_{RW}\\
A_{WR}&A_{WW}
\end{pmatrix}
\tag{L-20703.1}
\]

on a decomposition \(R\oplus W\). Assume

\[
A_{WW}\succ0.
\]

The complete prime-side Schur pivot is

\[
\boxed{
S_R
=A_{RR}-A_{RW}A_{WW}^{-1}A_{WR}.
}
\tag{L-20703.2}
\]

No selected-zero decomposition appears in this definition.

## 2. Arbitrary graph correction

Let \(C:R\to W\) be any finite matrix. Replace the radical coordinates by the
graph

\[
J_Cr=r+Cr.
\]

In the graph-plus-\(W\) coordinates, the block entries are

\[
\begin{aligned}
A_{RR}^{(C)}
&=A_{RR}+A_{RW}C+C^*A_{WR}+C^*A_{WW}C,\\
A_{WR}^{(C)}
&=A_{WR}+A_{WW}C,\\
A_{WW}^{(C)}
&=A_{WW}.
\end{aligned}
\tag{L-20703.3}
\]

Direct expansion gives

\[
\boxed{
A_{RR}^{(C)}
-
(A_{WR}^{(C)})^*A_{WW}^{-1}A_{WR}^{(C)}
=S_R.
}
\tag{L-20703.4}
\]

Therefore the complete Schur pivot is **exactly invariant** under every graph
chosen by the first line-zero frame.

### Congruence proof

The coordinate change is

\[
T_C=
\begin{pmatrix}
I&0\\
C&I
\end{pmatrix}.
\]

Then

\[
A^{(C)}=T_C^*AT_C.
\]

Block Gaussian elimination of either side produces the same diagonal block
\(S_R\). QED.

## 3. Joint selected-frame decomposition

Let \(P_Y\succeq0\) be any selected simple-line-zero Gram on the graph kernel.
Write the remaining signed prime-side kernel form as \(R_Y^{(C)}\). After the
**entire** positive sector is eliminated,

\[
\boxed{
P_Y+\mathcal R_{Y\mid Z}^{\rm corr}=S_R.
}
\tag{L-20703.5}
\]

Thus the selected frame and joint corrected residual are a decomposition of one
fixed prime-side Schur matrix. Changing the first frame, changing graph
coordinates, or adding a different positive selected block cannot alter the
exact sum.

This is the production meaning of the joint LMI in `L-20504`.

## 4. Rank-one packet

If \(R\) is one dimensional, then

\[
\boxed{
S_R=rac{\det A}{\det A_{WW}}.
}
\tag{L-20703.6}
\]

Hence, once \(A_{WW}\succ0\), the entire sign is one directed determinant or
one scalar LDL pivot.

If the original radical vector \(r\) is an exact normalized eigenvector of
\(A\), with eigenvalue \(\lambda\), then

\[
\boxed{S_R=\lambda.}
\tag{L-20703.7}
\]

For a graph representative \(k=r+Wc\) in an orthonormal metric, the generalized
floor becomes

\[
\boxed{
\frac{S_R}{\|k\|^2}
=
\frac{\lambda}{1+\|c\|^2}.
}
\tag{L-20703.8}
\]

The frame can improve the metric factor by making \(c\) small. It cannot change
the sign of \(\lambda\).

## 5. Exact prime-side assembly

For D-0001 at support \(c\) and packet size \(N\), let

\[
A_{N,c}
=A_{N,c}^{\rm pole}
+A_{N,c}^{\rm arch}
+A_{N,c}^{\rm pp},
\tag{L-20703.9}
\]

where `pp` contains every prime power \(q\le c\) with its exact von Mangoldt
weight and directed phase.

The proof-producing order is:

1. assemble all three matrices in one basis and metric;
2. construct the structured first frame by `L-20701/L-20702`;
3. assemble the entire positive sector \(A_{WW}\);
4. certify \(A_{WW}\succ0\);
5. compute the joint Schur pivot (L-20703.2) directly;
6. only afterward split it into selected positive mass and a residual for
   independent checking.

Taking separate absolute norms before step 5 can lose the sign.

## 6. Cofinal statement

Let \(G_{R,N,c}\) be the induced production metric and let
\(\delta_{N,c}\) be the full assembly radius. The exact prime-side theorem
needed by the positive route is

\[
\boxed{
\lambda_{\min}
\left(
S_{R,N,c},G_{R,N,c}
\right)
\ge-\varepsilon_{N,c},
\qquad
\varepsilon_{N_j,c_j}+\delta_{N_j,c_j}\to0
}
\tag{L-20703.10}
\]

along an unbounded schedule

\[
N_j\to\infty,
\qquad
c_j\to\infty.
\]

Equivalently, in the conditional-frame notation,

\[
\Lambda_j
(\overline\nu_j-\underline\sigma_j^2)_+
+\delta_j\to0.
\]

The structured frame removes the numerical inversion obstruction, but
(L-20703.10) is the arithmetic sign theorem itself.

## 7. False-RH alternative

On a complete capturing hierarchy, an off-line Xi-cardinal difference gives a
fixed negative Weil value and survives positive-sector Schur elimination.
Therefore false RH forces the left side of (L-20703.10) to remain below a fixed
negative constant on a suitable cofinal subsequence.

Consequently, no bound that is compatible with arbitrary off-line zero data can
prove (L-20703.10). A proof must use a genuinely arithmetic cancellation in the
complete prime-power, polar, and archimedean matrix.

## 8. Precise output of this lemma

Closed:

- first-frame inversion;
- conditional second-frame inversion;
- graph-coordinate cross terms;
- separate residual-versus-cross bookkeeping.

Not closed:

- the sign of the complete prime-side Schur pivot as packet size grows.

The next production artifact should therefore emit directed LDL pivots of
\(A_{WW}\) and of \(S_R\), rather than another raw frame condition number.
