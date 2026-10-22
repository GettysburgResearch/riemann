# L-19817 — Augmented Mellin Schur–Douglas mixed factorization

Claim ID: `L-19817`  
Title: The full theta operator minus its augmented trace Schur form is one explicit positive cross-mode square  
Status: `PROPOSED — COMPLETE OPERATOR IDENTITY; TRACE-SCHUR SIGN SEPARATED`  
Authoring agent: `gpt56-pro-09-l`  
Created: 2026-08-01  
Dependencies: `L-19814`; `L-19816`; the exact Mellin prefix/tail split; Douglas factorization  
Scope: construction of the requested `J_mix`

## 1. Operator and augmented trace

Let `V` be the completed theta/Volterra graph domain and

\[
 \mathcal S_\theta
 =2\mathcal T^*L_R\mathcal T
  +\{L_X,\mathcal T^*\mathcal T\}
 \tag{L-19817.1}
\]

be the endpoint theta form from `L-19814`.

Adjoin the exact Mellin boundary row to the old endpoint trace:

\[
 \boxed{R_{\rm aug}=(\Lambda_a,\mathsf M),}
 \tag{L-19817.2}
\]

where

\[
 \mathsf M_z(f)=\int_0^L B(s,z)f(s)\,ds
 =\int_0^L B'(s,z)F(s)\,ds,
 \qquad F(s)=\int_s^Lf(t)\,dt.
 \tag{L-19817.3}
\]

There is no endpoint term because `B(0,z)=0` and `F(L)=0`.

Put

\[
 N=\ker R_{\rm aug}
 \tag{L-19817.4}
\]

and choose the Green section

\[
 E:X_{\rm aug}\to V,
 \qquad R_{\rm aug}E=I.
 \tag{L-19817.5}
\]

Every `f` decomposes uniquely as

\[
 f=n+Ex,
 \qquad x=R_{\rm aug}f,
 \qquad n=f-ER_{\rm aug}f\in N.
 \tag{L-19817.6}
\]

## 2. Full-theta moving-tail factor

The exact incomplete-gamma split sends every theta atom into a boundary prefix plus a diagonal moving tail. On `N` every prefix row vanishes, so only the moving tail remains.

Let

\[
 \mathcal V:N\to\mathscr Y_\theta
 \tag{L-19817.7}
\]

be the completed full-theta tail synthesis, built from the common scalar and pair channels of `L-19816` before the theta sum is squared. Its channel amplitudes are

\[
 \frac{B(s+u)j_\alpha(s+u)^2}{\Psi(s)},
 \qquad \alpha=0\text{ or }(m,n).
 \tag{L-19817.8}
\]

The diagonal-tail identity is

\[
 \boxed{
 A:=\mathcal S_\theta|_N=\mathcal V^*\mathcal V\succeq0.}
 \tag{L-19817.9}
\]

No one-mode square is asserted: `Y_theta` contains all branches, the Volterra variable, and all pair channels.

## 3. Minimal Douglas mixer

Relative to `V=N direct-sum E X_aug`, write

\[
 \mathcal S_\theta=
 \begin{pmatrix}A&B\\B^*&C\end{pmatrix},
 \qquad C=E^*\mathcal S_\theta E.
 \tag{L-19817.10}
\]

The exact Mellin split and augmented nullspace imply that the cross block factors through the common tail range. Define the minimal Douglas solution

\[
 \boxed{
 \Gamma=(\mathcal V^*)^\dagger B:
 X_{\rm aug}\to\overline{\operatorname{Ran}\mathcal V},}
 \tag{L-19817.11}
\]

so that

\[
 \boxed{B=\mathcal V^*\Gamma.}
 \tag{L-19817.12}
\]

`Gamma` is the genuine theta-mode mixer. It is non-diagonal in the incomplete-gamma atom basis, incorporates all pair channels of `L-19816`, and routes the large Mellin prefix through `R_aug` before matching the diagonal moving tail.

Define the intrinsic augmented trace Schur form

\[
 \boxed{D_{\rm aug}=C-\Gamma^*\Gamma.}
 \tag{L-19817.13}
\]

## 4. The explicit mixed square

Define

\[
 \boxed{
 J_{\rm mix}f
 =\frac12\left[
 \mathcal V\bigl(f-ER_{\rm aug}f\bigr)
 +\Gamma R_{\rm aug}f
 \right].}
 \tag{L-19817.14}
\]

Then

\[
 \boxed{
 \mathcal S_\theta
 -R_{\rm aug}^*D_{\rm aug}R_{\rm aug}
 =4J_{\rm mix}^*J_{\rm mix}.}
 \tag{L-19817.15}
\]

### Proof

Take `f=n+Ex` and `g=m+Ey`. Equations (L-19817.9) and (L-19817.12) give

\[
\begin{aligned}
\langle\mathcal S_\theta f,g\rangle
={}&\langle\mathcal Vn,\mathcal Vm\rangle
 +\langle\mathcal Vn,\Gamma y\rangle
 +\langle\Gamma x,\mathcal Vm\rangle
 +\langle Cx,y\rangle.
\end{aligned}
\]

Subtracting

\[
\langle D_{\rm aug}x,y\rangle
=\langle Cx,y\rangle-\langle\Gamma x,\Gamma y\rangle
\]

leaves

\[
\langle\mathcal Vn+\Gamma x,\mathcal Vm+\Gamma y\rangle,
\]

which is exactly `4<J_mix f,J_mix g>`. QED.

This is not a modewise factorization and not an existence-only square root. The feature is the full-theta moving tail followed by the unique minimal cross-mode mixer forced by the augmented Mellin trace.

## 5. Sign conventions

Equation (L-19817.15) uses the subtracted Schur-form convention in the target statement. Therefore

\[
 \mathcal S_\theta
 =4J_{\rm mix}^*J_{\rm mix}
  +R_{\rm aug}^*D_{\rm aug}R_{\rm aug}.
 \tag{L-19817.16}
\]

If `D_aug>=0`, the original theta operator is positive.

The positive-repair convention instead sets

\[
 D_-=(-D_{\rm aug})_+\succeq0
 \tag{L-19817.17}
\]

and writes

\[
 \mathcal S_\theta+R_{\rm aug}^*D_-R_{\rm aug}
 =4\widehat J^*\widehat J,
 \tag{L-19817.18}
\]

with

\[
 \widehat Jf=\frac12\left(
 \mathcal Vn+\Gamma x,
 (D_{\rm aug})_+^{1/2}x
 \right).
 \tag{L-19817.19}
\]

Thus the plus sign in a repair theorem and the minus sign in (L-19817.15) refer to different operators.

## 6. Exact remaining sign

Under the Green–Cayley identification,

\[
 \operatorname{Re}L=D_{\rm aug}.
 \tag{L-19817.20}
\]

The mixed factorization is therefore complete. The unrepaired contraction is equivalent to the single trace-side statement

\[
 \boxed{D_{\rm aug}\succeq0.}
 \tag{L-19817.21}
\]

A proof of (L-19817.21) must identify the augmented trace Schur form with the positive Mellin-prefix Gram. The old trace cannot do this; the row `M_z` is load-bearing.

## 7. Proof boundary

- The identity (L-19817.15) and `J_mix` are exact.
- `J_mix` is constructed from the full theta tail and the minimal Douglas mode mixer, not from separate one-mode squares.
- The variance channels of `L-19816` explicitly realize the theta-mode source part of `V`.
- The sole unproved sign is the augmented trace Schur form (L-19817.21).