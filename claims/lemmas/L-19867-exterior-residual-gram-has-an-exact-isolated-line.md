# L-19867 — The exterior-cardinal residual Gram has an exact isolated line and a vanishing residual ratio

Claim ID: `L-19867`  
Status: **PROVED EXACT FINITE THEOREM; COFINAL APPLICATION USES L-19862**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11  
Depends on: the positive residual Gram and complement floor of `L-19862`  
Scope: proves the corrected prime/source-side isolated-line obligation for the positive residual model  
Nonclaim: this is not a lower bound for the indefinite localized Weil matrix

## 1. Abstract finite theorem

Let `H` be a finite-dimensional Hilbert space with an orthogonal decomposition

\[
 H=\mathbb Cp\oplus E,
 \qquad \|p\|=1.
\tag{L-19867.1}
\]

Let `D` be a positive semidefinite Hermitian matrix.  Write its block form as

\[
 D=
 \begin{pmatrix}
 m&b^*\\
 b&C
 \end{pmatrix},
 \qquad
 m=\langle p,Dp\rangle,
\tag{L-19867.2}
\]

and assume

\[
 C\succeq I_E.
\tag{L-19867.3}
\]

Define the positive metric

\[
 \mathcal G=
 \begin{pmatrix}
 1&0\\0&C
 \end{pmatrix}.
\tag{L-19867.4}
\]

Then the following statements hold exactly.

### (a) Two-sided complement moat

For every `w in E`,

\[
 \boxed{
 \|Dw\|_{\mathcal G^{-1}}
 \ge \|w\|_{\mathcal G}.}
\tag{L-19867.5}
\]

Thus the isolated-line gate holds at shift `sigma=0` with the exact singular
moat

\[
 \boxed{g=1.}
\tag{L-19867.6}
\]

### (b) Target residual

The target row satisfies

\[
 \boxed{
 \|Dp\|_{\mathcal G^{-1}}^2
 \le m+m^2.}
\tag{L-19867.7}
\]

Consequently

\[
 \boxed{
 {b_{\rm tar}\over g}
 \le\sqrt{m+m^2}.}
\tag{L-19867.8}
\]

### (c) Exact generalized spectrum

Put

\[
 c=C^{-1/2}b,
 \qquad \theta=\|c\|^2.
\tag{L-19867.9}
\]

Positivity of `D` gives

\[
 0\le\theta\le m.
\tag{L-19867.10}
\]

The generalized eigenvalues of `(D,mathcal G)` consist of the eigenvalue `1`
on `c^perp subset E`, together with

\[
 \boxed{
 \lambda_\pm
 ={1+m\pm\sqrt{(1-m)^2+4\theta}\over2}.}
\tag{L-19867.11}
\]

If `0<=m<1`, then

\[
 \lambda_-\le m<1\le\lambda_+,
\tag{L-19867.12}
\]

so `lambda_-` is a unique simple generalized ground eigenvalue and

\[
 \boxed{\lambda_2(D,\mathcal G)=1.}
\tag{L-19867.13}
\]

### (d) Ground-line convergence

Let `xi` be the generalized ground line.  In the whitened coordinates
`mathcal G^(1/2)H`, it has a representative

\[
 \begin{pmatrix}
 1\\-c/(1-\lambda_-)
 \end{pmatrix}.
\tag{L-19867.14}
\]

Therefore its metric angle from the target obeys

\[
 \boxed{
 \sin\angle_{\mathcal G}(\xi,p)
 \le {\sqrt m\over1-m}.}
\tag{L-19867.15}
\]

In particular the isolated line converges to `p` whenever `m->0`.

## 2. Proof

For `w=(0,y) in E`,

\[
 Dw=(b^*y,Cy).
\]

Hence

\[
\begin{aligned}
 \|Dw\|_{\mathcal G^{-1}}^2
 &=|b^*y|^2+(Cy)^*C^{-1}(Cy)\\
 &=|b^*y|^2+y^*Cy\\
 &\ge y^*Cy
 =\|w\|_{\mathcal G}^2,
\end{aligned}
\]

which proves (L-19867.5).

The Schur complement of the positive block `C` in `D` is nonnegative:

\[
 m-b^*C^{-1}b\ge0.
\tag{L-19867.16}
\]

Thus

\[
\begin{aligned}
 \|Dp\|_{\mathcal G^{-1}}^2
 &=(m,b)^*\begin{pmatrix}1&0\\0&C^{-1}\end{pmatrix}(m,b)\\
 &=m^2+b^*C^{-1}b\\
 &\le m^2+m,
\end{aligned}
\]

proving (L-19867.7).

Whitening gives

\[
 \mathcal G^{-1/2}D\mathcal G^{-1/2}
 =\begin{pmatrix}m&c^*\\c&I_E\end{pmatrix}.
\tag{L-19867.17}
\]

It is the identity on `c^perp`.  Its restriction to
`span{p,c}` has characteristic polynomial

\[
 (m-\lambda)(1-\lambda)-\theta,
\]

which gives (L-19867.11).  Equation (L-19867.10) is exactly
(L-19867.16).  The ordering (L-19867.12) follows because

\[
 \sqrt{(1-m)^2+4\theta}\ge1-m.
\]

Finally the lower-eigenvalue equation in the `E` coordinate is

\[
 c+(1-\lambda_-)y=0.
\]

Since `lambda_-<=m`,

\[
 \|y\|
 ={\|c\|\over1-\lambda_-}
 \le {\sqrt m\over1-m},
\]

which proves (L-19867.14)--(L-19867.15).

## 3. Cofinal arithmetic application

Apply the theorem to the exact residual Gram `D_(L,N)` of `L-19862`:

- `p_(L,N)` is the exactly normalized Xi-radical target;
- `E=p_(L,N)^perp`;
- the exterior-cardinal lifts give
  \[
  D_{L,N}|_E\succeq I_E;
  \]
- the target residual energy obeys, for every prescribed `B>0` on a suitable
  quadratic-log cutoff,
  \[
  m_{L,N}=D_{L,N}(p,p)\le C_Be^{-BL}.
  \]

Therefore there is a cofinal sequence `(L_j,N_j)` for which

\[
 \boxed{
 g_j=1,
 \qquad
 {b_j\over g_j}
 \le\sqrt{C_Be^{-BL_j}+C_B^2e^{-2BL_j}}
 \longrightarrow0.}
\tag{L-19867.18}
\]

The generalized ground line `xi_j` is simple and satisfies

\[
 \boxed{
 \sin\angle_{\mathcal G_j}(\xi_j,p_j)
 \le {\sqrt{C_B}e^{-BL_j/2}
       \over1-C_Be^{-BL_j}}.}
\tag{L-19867.19}
\]

This is a complete two-sided moat and residual-ratio theorem on an unbounded
source-bound arithmetic hierarchy.  It uses no zeta-zero locations to determine
the sign of a Weil matrix and is compatible with lower eigenvalues of unrelated
indefinite operators.

## 4. Directed robustness

Let

\[
 H_j=\mathcal G_j^{-1/2}D_j\mathcal G_j^{-1/2}
\]

and suppose an outward-rounded producer encloses it by `Htilde_j` with

\[
 \|Htilde_j-H_j\|\le\delta_j.
\tag{L-19867.20}
\]

For all sufficiently large `j`, the exact generalized spectral gap is at least

\[
 1-\lambda_{-,j}\ge1-m_j\ge3/4.
\]

If `delta_j<=1/8`, Weyl and Davis--Kahan give a unique enclosed low line and

\[
 \sin\angle(\widetilde\xi_j,\xi_j)
 \le {2\delta_j\over1-m_j}.
\tag{L-19867.21}
\]

Because every finite source integral and zeta value used after nonresonant
support selection is a computable real/complex number, interval precision may
be increased until any prescribed rational `delta_j>0` is reached.  Thus one
may impose `delta_j<=e^{-BL_j/2}` without changing the analytic hierarchy.

## 5. Proof boundary

This theorem proves obligation 1 for the **positive arithmetic residual Gram**.
It does not prove that the localized Weil matrix has an isolated Xi line, nor
that the residual Gram belongs to the rank-two CCM commutator class required to
turn its ground vector into a real-zero Fourier--Mellin transform.  `R-19848`
shows that this missing real-zero bridge cannot be inferred from isolation
alone.
