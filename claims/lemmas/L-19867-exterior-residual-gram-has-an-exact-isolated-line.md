# L-19867 — The exterior-cardinal residual Gram has an exact isolated line and a vanishing residual ratio

Claim ID: `L-19867`  
Status: **PROVED EXACT FINITE THEOREM; COFINAL APPLICATION USES L-19862**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-11  
Depends on: the positive residual Gram and complement floor of `L-19862`  
Scope: proves the corrected prime/source-side isolated-line obligation for the positive residual model  
Nonclaim: this is not a lower bound for the indefinite localized Weil matrix

## 1. Abstract finite theorem

Let

\[
 H=\mathbb Cp\oplus E,
 \qquad \|p\|=1,
\tag{L-19867.1}
\]

be an orthogonal decomposition, and let

\[
 D=
 \begin{pmatrix}
 m&b^*\\
 b&C
 \end{pmatrix}\succeq0,
 \qquad
 m=\langle p,Dp\rangle,
 \qquad C\succeq I_E.
\tag{L-19867.2}
\]

Define

\[
 \mathcal G=
 \begin{pmatrix}1&0\\0&C\end{pmatrix}.
\tag{L-19867.3}
\]

Then the following statements hold exactly.

### (a) Two-sided complement moat

For every `w in E`,

\[
 \boxed{
 \|Dw\|_{\mathcal G^{-1}}
 \ge \|w\|_{\mathcal G}.}
\tag{L-19867.4}
\]

Thus the isolated-line gate at shift `sigma=0` has the exact singular moat

\[
 \boxed{g=1.}
\tag{L-19867.5}
\]

### (b) Target residual

The target row satisfies

\[
 \boxed{
 \|Dp\|_{\mathcal G^{-1}}^2
 \le m+m^2,}
\tag{L-19867.6}
\]

and hence

\[
 \boxed{
 {b_{\rm tar}\over g}\le\sqrt{m+m^2}.}
\tag{L-19867.7}
\]

### (c) Exact generalized spectrum

Put

\[
 c=C^{-1/2}b,
 \qquad \theta=\|c\|^2.
\tag{L-19867.8}
\]

Then

\[
 0\le\theta\le m,
\tag{L-19867.9}
\]

and the generalized spectrum of `(D,mathcal G)` consists of the eigenvalue `1`
on `c^perp subset E`, together with

\[
 \boxed{
 \lambda_\pm
 ={1+m\pm\sqrt{(1-m)^2+4\theta}\over2}.}
\tag{L-19867.10}
\]

If `0<=m<1`, then

\[
 \lambda_-\le m<1\le\lambda_+.
\tag{L-19867.11}
\]

Thus `lambda_-` is a unique simple generalized ground eigenvalue and

\[
 \boxed{
 \lambda_2(D,\mathcal G)\ge1.}
\tag{L-19867.12}
\]

When `dim E>=2`, as in every nontrivial application of `L-19862`, the subspace
`c^perp` is nonzero and therefore

\[
 \boxed{\lambda_2(D,\mathcal G)=1.}
\tag{L-19867.13}
\]

(The equality also holds in dimension one when `c=0`; otherwise the second
eigenvalue is `lambda_+>1`.)

### (d) Ground-line convergence

In whitened coordinates, the generalized ground line has a representative

\[
 \begin{pmatrix}1\\-c/(1-\lambda_-)\end{pmatrix}.
\tag{L-19867.14}
\]

Consequently

\[
 \boxed{
 \sin\angle_{\mathcal G}(\xi,p)
 \le {\sqrt m\over1-m}.}
\tag{L-19867.15}
\]

If `D`, `mathcal G`, and `p` commute with parity, uniqueness also makes `xi`
even.

## 2. Proof

For `w=(0,y) in E`,

\[
 Dw=(b^*y,Cy),
\]

so

\[
\begin{aligned}
 \|Dw\|_{\mathcal G^{-1}}^2
 &=|b^*y|^2+(Cy)^*C^{-1}(Cy)\\
 &=|b^*y|^2+y^*Cy\\
 &\ge y^*Cy
 =\|w\|_{\mathcal G}^2.
\end{aligned}
\]

This proves (L-19867.4).

The Schur complement of `C` in the positive matrix `D` gives

\[
 m-b^*C^{-1}b\ge0.
\tag{L-19867.16}
\]

Therefore

\[
\begin{aligned}
 \|Dp\|_{\mathcal G^{-1}}^2
 &=m^2+b^*C^{-1}b\\
 &\le m^2+m,
\end{aligned}
\]

which proves (L-19867.6).

Whitening gives

\[
 \mathcal G^{-1/2}D\mathcal G^{-1/2}
 =\begin{pmatrix}m&c^*\\c&I_E\end{pmatrix}.
\tag{L-19867.17}
\]

It is the identity on `c^perp`; on `span{p,c}` its characteristic polynomial is

\[
 (m-\lambda)(1-\lambda)-\theta.
\]

This proves (L-19867.10).  Equation (L-19867.9) is (L-19867.16), and
(L-19867.11) follows from

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

```text
p_(L,N)                         exactly normalized Xi target;
E                               p_(L,N)-perp;
D_(L,N)|_E >= I                 exterior-cardinal complement floor;
m_(L,N)=D_(L,N)(p,p)            target residual energy.
```

For every prescribed `B>0`, a suitable quadratic-log cutoff gives

\[
 m_{L,N}\le C_Be^{-BL}.
\tag{L-19867.18}
\]

Choose the complement basis and exterior source lifts parity-equivariantly.
Then `D`, `mathcal G`, and `p` commute with parity and the unique low line is
even.

On the resulting cofinal sequence,

\[
 \boxed{
 g_j=1,
 \qquad
 {b_j\over g_j}
 \le\sqrt{C_Be^{-BL_j}+C_B^2e^{-2BL_j}}
 \longrightarrow0,}
\tag{L-19867.19}
\]

and

\[
 \boxed{
 \sin\angle_{\mathcal G_j}(\xi_j,p_j)
 \le {\sqrt{C_B}e^{-BL_j/2}
       \over1-C_Be^{-BL_j}}.}
\tag{L-19867.20}
\]

This proves a source-bound, unbounded, even isolated-line hierarchy without
asserting a sign for the indefinite localized Weil matrix.

## 4. Directed robustness

Let

\[
 H_j=\mathcal G_j^{-1/2}D_j\mathcal G_j^{-1/2}
\]

and suppose an outward-rounded producer returns `Htilde_j` with

\[
 \|Htilde_j-H_j\|\le\delta_j.
\tag{L-19867.21}
\]

For all large `j`, the exact low spectral gap is at least

\[
 1-\lambda_{-,j}\ge1-m_j\ge3/4.
\]

If `delta_j<=1/8`, Weyl and Davis--Kahan give a unique enclosed low line and

\[
 \sin\angle(\widetilde\xi_j,\xi_j)
 \le {2\delta_j\over1-m_j}.
\tag{L-19867.22}
\]

Every finite source integral and nonresonant zeta value is computable, so ball
precision may be increased until any prescribed positive rational `delta_j` is
reached.  In particular one may impose `delta_j<=e^{-BL_j/2}` separately at
every level.

## 5. Proof boundary

This theorem proves obligation 1 for the **positive arithmetic residual Gram**.
It does not prove that the localized Weil matrix has an isolated Xi line, nor
that the residual Gram belongs to the rank-two CCM commutator class needed for
a real-zero Fourier--Mellin conclusion.  `R-19848` proves that isolation alone
cannot supply that missing bridge.
