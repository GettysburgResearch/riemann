# L-20501 — Conditional simple-line frames and the complete-kernel Schur matrix

Claim ID: `L-20501`  
Title: A first simple-line frame graphs the selected-zero kernel, and a second frame acts on it through one exact Schur complement  
Status: `PROPOSED — COMPLETE FINITE ALGEBRA; SIMPLE-LINE EXISTENCE INHERITED`  
Authoring agent: `gpt56-03-q`  
Created: 2026-08-01  
Dependencies: `L-18507/L-18511`; `L-20302`; exact finite-dimensional metric algebra  
Scope: the complete enlarged finite kernel after ambient-deficit augmentation  
Related counterexample candidates: none

## 1. Two orthogonal packet coordinates

Let \(U\) be a finite-dimensional real or complex Hilbert space with positive
metric \(G_U\). Fix a metric-orthogonal decomposition

\[
U=R\oplus_{G_U}W,
\qquad
G_U=
\begin{pmatrix}
G_R&0\\
0&G_W
\end{pmatrix},
\tag{L-20501.1}
\]

where \(R\) is the inherited repaired-radical packet and \(W\) is its actual
complete finite complement.

Let \(Z\) be a finite block of simple critical-line zero evaluations with
exact matrix

\[
V_Z=
\begin{pmatrix}
A&B
\end{pmatrix},
\qquad
A:R\to\mathbb C^{\dim W},
\quad
B:W\to\mathbb C^{\dim W}.
\tag{L-20501.2}
\]

Assume

\[
\boxed{B\text{ is invertible}.}
\tag{L-20501.3}
\]

The finite simple-line uniqueness theorem of `L-18507/L-18511` supplies such a
block for every fixed finite \(W\).

## 2. The first frame produces the complete kernel as a graph

The selected-\(Z\) kernel inside \(U\) is

\[
K_Z=U\cap\ker V_Z.
\tag{L-20501.4}
\]

Define

\[
\boxed{
J_Z=
\begin{pmatrix}
I_R\\
-B^{-1}A
\end{pmatrix}:R\longrightarrow U.
}
\tag{L-20501.5}
\]

Then

\[
V_ZJ_Z=A-BB^{-1}A=0.
\tag{L-20501.6}
\]

Conversely, if \(r+w\in K_Z\), then

\[
Ar+Bw=0
\]

and therefore \(w=-B^{-1}Ar\). Hence

\[
\boxed{
K_Z=\operatorname{Ran}J_Z,
\qquad
\dim K_Z=\dim R.
}
\tag{L-20501.7}
\]

Its exact induced metric is

\[
\boxed{
G_K
=J_Z^*G_UJ_Z
=G_R+A^*B^{-*}G_WB^{-1}A
\succ0.
}
\tag{L-20501.8}
\]

This is the graph statement of `L-20302`, written in the coordinates needed for
a second frame.

## 3. A second simple-line block

Choose a second finite set \(Y\) of simple critical-line zeros and write its
evaluation matrix as

\[
V_Y=
\begin{pmatrix}
C&D
\end{pmatrix},
\qquad
C:R\to\mathbb C^{m_Y},
\quad
D:W\to\mathbb C^{m_Y}.
\tag{L-20501.9}
\]

On the graph kernel,

\[
V_YJ_Z
=
C-DB^{-1}A.
\]

Define the **conditional evaluation Schur matrix**

\[
\boxed{
S_{Y\mid Z}
=
C-DB^{-1}A.
}
\tag{L-20501.10}
\]

Thus

\[
\boxed{
V_Y|_{K_Z}
=
S_{Y\mid Z}
}
\tag{L-20501.11}
\]

after identifying \(K_Z\) with \(R\) through \(J_Z\).

The formula has a useful interpretation: \(DB^{-1}A\) is the part of the
\(Y\)-evaluation forced by the \(W\)-correction that cancels the first
\(Z\)-frame.

## 4. Exact determinant and rank factorization

Assume now that

\[
m_Y=\dim R.
\]

The complete square evaluation matrix on \(U=R\oplus W\) is

\[
\mathbb V_{Z,Y}
=
\begin{pmatrix}
A&B\\
C&D
\end{pmatrix}.
\tag{L-20501.12}
\]

Swap the two column blocks. The resulting matrix is

\[
\begin{pmatrix}
B&A\\
D&C
\end{pmatrix}.
\]

Ordinary block Gaussian elimination gives

\[
\begin{pmatrix}
I&0\\
-DB^{-1}&I
\end{pmatrix}
\begin{pmatrix}
B&A\\
D&C
\end{pmatrix}
=
\begin{pmatrix}
B&A\\
0&C-DB^{-1}A
\end{pmatrix}.
\tag{L-20501.13}
\]

Therefore

\[
\boxed{
\det\mathbb V_{Z,Y}
=
(-1)^{(\dim R)(\dim W)}
\det(B)\det(S_{Y\mid Z}).
}
\tag{L-20501.14}
\]

Consequently,

\[
\boxed{
\mathbb V_{Z,Y}\text{ is invertible}
\iff
B\text{ and }S_{Y\mid Z}\text{ are invertible}.
}
\tag{L-20501.15}
\]

More generally, without assuming square \(Y\), \(S_{Y\mid Z}\) is injective if
and only if the combined evaluations \(V_Z\oplus V_Y\) are injective on \(U\),
provided \(B\) is invertible.

### Proof of the rectangular assertion

If \(S_{Y\mid Z}r=0\), then \(J_Zr\in\ker V_Z\cap\ker V_Y\). Thus injectivity of
the combined map implies \(r=0\).

Conversely, if \(u=r+w\) lies in both kernels, the \(Z\)-equation forces
\(w=-B^{-1}Ar\), and the \(Y\)-equation becomes
\(S_{Y\mid Z}r=0\). Injectivity of \(S_{Y\mid Z}\) gives \(r=w=0\). QED.

## 5. Existence of a finite conditional frame

Every nonzero vector of \(K_Z\) is represented by a nonzero compactly supported
harmonic lift. The simple critical-line ordinates are a uniqueness set for this
finite Paley--Wiener space by `L-18507/L-18511`.

Therefore there exists a finite simple-line block \(Y\) for which

\[
S_{Y\mid Z}:R\to\mathbb C^{m_Y}
\]

is injective. By finite row elimination, one may retain exactly \(\dim R\)
rows and obtain an invertible square conditional matrix.

Hence the two-frame construction is unconditional at every fixed finite
support:

\[
\boxed{
Z\text{ frames }W,
\qquad
Y\text{ conditionally frames }K_Z.
}
\tag{L-20501.16}
\]

No quantitative lower bound follows from this existence theorem.

## 6. Positive conditional frame Gram

Let \(M_Y\succ0\) be the declared diagonal or Hermitian positive matrix of
simple-line multiplicity/residue weights. The selected-\(Y\) positive form on
the graph kernel is

\[
Q_Y|_{K_Z}
=
J_Z^*V_Y^*M_YV_YJ_Z
=
S_{Y\mid Z}^*M_YS_{Y\mid Z}.
\tag{L-20501.17}
\]

Define

\[
\boxed{
\sigma_{Y\mid Z}^2
=
\lambda_{\min}
\left(
G_K^{-1/2}
S_{Y\mid Z}^*M_YS_{Y\mid Z}
G_K^{-1/2}
\right).
}
\tag{L-20501.18}
\]

If \(S_{Y\mid Z}\) is injective, then

\[
\boxed{
\sigma_{Y\mid Z}^2>0,
\qquad
Q_Y|_{K_Z}\succeq
\sigma_{Y\mid Z}^2G_K.
}
\tag{L-20501.19}
\]

The exact right-inverse interpretation is

\[
\sigma_{Y\mid Z}^{-2}
=
\left\|
S_{Y\mid Z}^{-1}
\right\|_{\ell^2(M_Y)\to G_K}^2
\tag{L-20501.20}
\]

in square coordinates.

## 7. Why this is not the same frame twice

The first block \(Z\) is chosen to frame \(W\). It defines the kernel graph.
The second block \(Y\) is evaluated **after conditioning on the first block**.

Using \(C\) alone would be wrong: it ignores the cancellation vector
\(-B^{-1}Ar\) in \(W\). The correct finite object is always

\[
C-DB^{-1}A.
\]

Thus the relevant production conditioning is a block Gaussian elimination
problem on one complete evaluation table, not two unrelated singular-value
computations.

## 8. Proof boundary

- The graph, Schur matrix, determinant, metric, and positive Gram identities are
  exact finite algebra.
- Existence of finite \(Z\) and \(Y\) inherits the corrected simple-line
  uniqueness theorem of PR #191.
- No cofinal lower rate for \(\sigma_{Y\mid Z}\) is proved.
- Under false RH, supported off-line-cardinal approximants may force the
  conditional frame floor to collapse.
- Therefore the theorem closes conditional-frame capture, not the RH-bearing
  one-sided residual moat.
