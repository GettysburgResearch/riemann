# R-19849 — The isolated-line counterexample has an empty positive CCM completion cone

Claim ID: `R-19849`  
Status: **PROVED EXACT FINITE CONE CLASSIFICATION**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11  
Depends on: `R-19848`  
Scope: strengthens the non-ground firewall without using a converse theorem

## 1. Statement

Let

\[
 \xi=(1,-1,1)^T
\]

on the frequency set `{-1,0,1}`.  There is no nonzero real parity-invariant
CCM/divided-difference matrix `Q` such that

\[
 Q\succeq0,
 \qquad
 \ker Q=\mathbb R\xi.
\tag{R-19849.1}
\]

More precisely, every parity-invariant CCM matrix satisfying `Q xi=0` is a
scalar multiple of the indefinite matrix in `R-19848`.

## 2. Complete parity-invariant CCM family

For `N=1`, the parity conditions are

\[
 a_{-1}=a_1=a,
 \qquad a_0=d,
 \qquad
 b_{-1}=-u,
 \quad b_0=0,
 \quad b_1=u.
\]

The divided-difference formula gives the same off-diagonal value `u` in every
position.  Hence every matrix in the class is

\[
 Q(a,d,u)=
 \begin{pmatrix}
 a&u&u\\
 u&d&u\\
 u&u&a
 \end{pmatrix}.
\tag{R-19849.2}
\]

## 3. Kernel equations

Multiplication by `xi` gives

\[
 Q(a,d,u)\xi
 =\begin{pmatrix}
 a\\2u-d\\a
 \end{pmatrix}.
\tag{R-19849.3}
\]

Thus `Q xi=0` if and only if

\[
 a=0,
 \qquad d=2u.
\tag{R-19849.4}
\]

Therefore

\[
 \boxed{
 Q=u
 \begin{pmatrix}
 0&1&1\\
 1&2&1\\
 1&1&0
 \end{pmatrix}.}
\tag{R-19849.5}
\]

## 4. Positivity is impossible

The matrix in (R-19849.5) has eigenvalues

\[
 -u,\qquad0,\qquad3u.
\tag{R-19849.6}
\]

If `u>0`, the eigenvalue `-u` is negative.  If `u<0`, the eigenvalue `3u` is
negative.  If `u=0`, the matrix is zero and its kernel has dimension three.
Consequently no matrix satisfies (R-19849.1).

## 5. Consequence

The obstruction in `R-19848` is not merely that one chosen interior matrix is
indefinite.  The target line itself admits **no** positive matrix in the exact
three-dimensional CCM completion class.  Any valid non-ground theorem must add
new dimensions, change the target line, or perform a rank-changing operation.
If it changes the finite transform, it must separately prove that hypothetical
nonreal Xi zeros are not cancelled in the limiting operation.
