# L-18512 — Direct residual shorting on the actual complete complement

Claim ID: `L-18512`  
Title: The exact complete-complement Schur block is one trial-lift arithmetic matrix minus one squared harmonic-solve residual  
Status: `PROVED FINITE/FORM ALGEBRA; PRODUCTION SIGN NOT YET EVALUATED`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: exact harmonic lift in `L-16901`; coercive ambient metric; endpoint decomposition `L-15610`; triangular assembly `L-15306`  
Scope: the actual complete harmonic complement `W_lambda`, without a selected-zero threshold or absolute zero-tail budget  
Related candidates: none

## 1. The actual complete complement

Fix one support and suppress the support index. Let the exact localized Suzuki
form, after the finite low packet has been chosen but before ambient
elimination, be

\[
\mathcal H=
\begin{pmatrix}
B&L^*\\
L&C
\end{pmatrix}
\quad\text{on}\quad U\oplus E,
\qquad C\succ0.
\tag{L-18512.1}
\]

Let `R subset U` be the exact localized radical packet and let

\[
W=R^{\perp_{G_C}}\cap U
\tag{L-18512.2}
\]

be the **actual complete metric complement**, not a separately constructed
cardinal packet. Write

\[
Q_W:W\hookrightarrow U,
\qquad
B_W=Q_W^*BQ_W,
\qquad
Z_W=LQ_W.
\tag{L-18512.3}
\]

The exact harmonic Schur block on `W` is

\[
\boxed{
S_W=B_W-Z_W^*C^{-1}Z_W.
}
\tag{L-18512.4}
\]

The purpose of this lemma is to certify (L-18512.4) directly from the complete
prime/archimedean form, without introducing

\[
\Sigma,\qquad B_T,\qquad\epsilon,
\]

or separately bounding the terminal matrix and the harmonic cross.

## 2. Exact trial-lift identity

Let

\[
X:W\longrightarrow E
\tag{L-18512.5}
\]

be any trial harmonic solve and define its residual

\[
\boxed{
\mathscr R_X=Z_W-CX.
}
\tag{L-18512.6}
\]

The corresponding trial lift is

\[
J_Xw=(Q_Ww,-Xw).
\tag{L-18512.7}
\]

### Theorem

One has the exact identity

\[
\boxed{
S_W
=J_X^*\mathcal HJ_X
-\mathscr R_X^*C^{-1}\mathscr R_X.
}
\tag{L-18512.8}
\]

### Proof

Direct block multiplication gives

\[
J_X^*\mathcal HJ_X
=B_W-Z_W^*X-X^*Z_W+X^*CX.
\tag{L-18512.9}
\]

Since `Z_W=CX+mathscr R_X`,

\[
\begin{aligned}
Z_W^*C^{-1}Z_W
={}&X^*CX+X^*\mathscr R_X
+\mathscr R_X^*X
+\mathscr R_X^*C^{-1}\mathscr R_X.
\end{aligned}
\tag{L-18512.10}
\]

Subtracting (L-18512.10) from `B_W` and comparing with (L-18512.9) proves
(L-18512.8). QED.

The identity is a matrix-valued a posteriori energy formula. It keeps every
arithmetic cancellation inside the trial-lift energy and charges only the
actual harmonic-solve residual.

## 3. Coercive proof-producing lower matrix

Suppose

\[
C\succeq hM,
\qquad h>0,
\qquad M\succ0.
\tag{L-18512.11}
\]

Then

\[
C^{-1}\preceq h^{-1}M^{-1},
\]

and (L-18512.8) gives

\[
\boxed{
S_W\succeq
\mathscr D_X,
}
\tag{L-18512.12}
\]

where

\[
\boxed{
\mathscr D_X
=J_X^*\mathcal HJ_X
-h^{-1}\mathscr R_X^*M^{-1}\mathscr R_X.
}
\tag{L-18512.13}
\]

Thus one directed finite LMI

\[
\boxed{
\mathscr D_X\succeq mG_W
}
\tag{L-18512.14}
\]

proves the sharp direct block statement

\[
\boxed{
B_W-Z_W^*C^{-1}Z_W\succeq mG_W.
}
\tag{L-18512.15}
\]

No selected-zero eigenvalue count, principal angle, line-zero frame constant, or
absolute omitted-zero radius enters this implication.

## 4. Sharpness and completeness

For the exact harmonic minimizer

\[
X_*=C^{-1}Z_W,
\tag{L-18512.16}
\]

one has `mathscr R_(X_*)=0`, and therefore

\[
\mathscr D_{X_*}=S_W.
\tag{L-18512.17}
\]

Since (L-18512.12) holds for every trial solve,

\[
\boxed{
\lambda_{\min}(S_W,G_W)
=
\sup_X\lambda_{\min}(\mathscr D_X,G_W).
}
\tag{L-18512.18}
\]

Accordingly, the trial-lift certificate loses no mathematical sign information.
It replaces an exact inverse by a finite solve plus a residual moat.

If `X_N` is a form-core Galerkin approximation to `X_*`, then

\[
\|X_N-X_*\|_C\to0,
\qquad
\|\mathscr R_{X_N}\|_{C^{-1}}\to0.
\tag{L-18512.19}
\]

Hence directed lower matrices obtained from (L-18512.13) converge to the exact
Schur block. Every strict positive or strict negative finite level is therefore
algorithmically decidable after sufficient Galerkin refinement and precision.

## 5. Exact Suzuki endpoint specialization

For the endpoint-visible production packet of `L-15610`, restrict every matrix
to the actual `W`. The exact low block has the decomposition

\[
B_W=P_{a,W}+E_{a,W},
\tag{L-18512.20}
\]

where

\[
\begin{aligned}
P_{a,W}={}&A_{a,W}^{\rm loc}
+2\bigl(v^-(v^+)^*+v^+(v^-)^*\bigr)_W
-2e^{-a}\bigl(v^+(v^+)^*\bigr)_W,
\end{aligned}
\tag{L-18512.21}
\]

and `E_(a,W)` is the **complete centered terminal-prime Hankel matrix** with its
order-`e^a` pole term already cancelled exactly.

Equations (L-18512.9) and (L-18512.13) give the production lower matrix

\[
\boxed{
\begin{aligned}
\mathscr D_{a,X}
={}&P_{a,W}\\
&+E_{a,W}
-Z_W^*X-X^*Z_W+X^*C X\\
&-h^{-1}\mathscr R_X^*M^{-1}\mathscr R_X.
\end{aligned}
}
\tag{L-18512.22}
\]

This is the correct object to assemble from the actual Suzuki packet.

All phase-sensitive cancellation between

- the centered terminal-prime matrix;
- the visible/ambient harmonic response;
- the finite local and pole-cancelled endpoint terms

is retained inside one finite Hermitian matrix. Bounding those channels
separately is unnecessary and may destroy a true positive moat.

## 6. Strict separation from separate norm charging

Take the scalar exact control

\[
P=1,
\qquad
E=\frac9{10},
\qquad
C=1,
\qquad
Z=1.
\tag{L-18512.23}
\]

Then

\[
B=P+E=\frac{19}{10}
\]

and the exact complete-complement Schur value is

\[
S_W=\frac{19}{10}-1=\frac9{10}>0.
\tag{L-18512.24}
\]

A separated estimate that retains only `E>=0` and charges the cross by `1`
proves merely

\[
1-1=0.
\tag{L-18512.25}
\]

Now take the deliberately inexact trial solve

\[
X=\frac34.
\]

Then

\[
\mathscr R_X=\frac14,
\qquad
J_X^*\mathcal HJ_X=\frac{77}{80},
\qquad
\mathscr R_X^*C^{-1}\mathscr R_X=\frac1{16},
\]

so (L-18512.8) gives exactly

\[
\boxed{
\frac{77}{80}-\frac1{16}=\frac9{10}.
}
\tag{L-18512.26}
\]

The joint residual certificate proves the exact strict moat that separate
terminal and cross norms lose.

## 7. Smallest exact production obstruction

Define the whitened negative part of the direct lower matrix by

\[
\boxed{
\Delta_{W,a,X}
=
\left[
G_W^{-1/2}\mathscr D_{a,X}G_W^{-1/2}
\right]_-.
}
\tag{L-18512.27}
\]

The production level is closed whenever

\[
\Delta_{W,a,X}=0.
\tag{L-18512.28}
\]

A cofinal lower envelope needs only

\[
\|\Delta_{W,a,X}\|\to0
\tag{L-18512.29}
\]

on the retained support sequence, together with the already-separated radical
row and assembly rates.

As the harmonic solve and directed arithmetic are refined, (L-18512.27)
converges to the negative part of the **actual** complete-complement Schur block.
Thus no smaller scalar tail, count, or conditioning obstruction remains on
`W`: the only unresolved datum is the sign of one explicit finite production
matrix.

## 8. Proof boundary

- The block identity, coercive lower matrix, sharpness, and endpoint
  specialization are exact.
- The theorem removes `Sigma`, `B_T`, and `epsilon` from the direct `W` sign
  test; they remain optional zero-side cross-checks.
- A complete prime-power manifest, directed archimedean/local entries, an exact
  `W` basis, and a proof-grade harmonic residual are still required.
- No such production matrix has yet been assembled on this branch.
- Therefore the real packet has been reduced to its smallest exact finite LMI,
  but its sign and RH remain unresolved.
