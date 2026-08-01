# L-15632 — Line-centered full-block perturbations control the soft harmonic Schur block

Claim ID: `L-15632`  
Title: A positive line-centered comparator plus a relative full-block error bounds the actual harmonic Schur negative part  
Status: `PROVED FINITE BLOCK/FORM THEOREM`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-18512`; finite-dimensional spectral calculus  
Scope: the exported profile-soft packet after the complete-frame support selection  
Related counterexample candidates: none

## 1. Purpose

The profile-soft sector isolated in `L-15630` cannot be declared near-radical
from its ordinary tail Gram alone. The correct comparison is not with zero. It
is with the full **line-centered** Weil block obtained by replacing every zero
parameter by its real ordinate. That comparator is positive semidefinite on the
entire low-plus-harmonic block.

This lemma proves that a small relative perturbation of that complete block
produces only a proportionally small negative harmonic Schur complement. The
terminal-prime, polar, archimedean, local, and harmonic channels are never
bounded separately.

## 2. Finite block setup

Let `S` be a finite low packet and `E` a finite harmonic/form-core packet. Let

\[
 D\succ0\quad\text{on }S,
 \qquad
 M\succ0\quad\text{on }E.
 \tag{L-15632.1}
\]

The line-centered comparator is

\[
 \mathcal H^0
 =
 \begin{pmatrix}
 B^0&(Z^0)^*\\
 Z^0&C^0
 \end{pmatrix}
 \quad\text{on }S\oplus E.
 \tag{L-15632.2}
\]

Assume

\[
 \boxed{\mathcal H^0\succeq0,}
 \tag{L-15632.3}
\]

\[
 \boxed{C^0\succeq hM,\qquad h>0,}
 \tag{L-15632.4}
\]

and

\[
 \boxed{B^0\preceq \ell D,\qquad \ell\ge0.}
 \tag{L-15632.5}
\]

Let the actual complete prime/polar/archimedean/harmonic block be

\[
 \mathcal H
 =
 \begin{pmatrix}
 B&Z^*\\
 Z&C
 \end{pmatrix}
 =\mathcal H^0+\mathcal E.
 \tag{L-15632.6}
\]

Assume the complete relative perturbation LMI

\[
 \boxed{
 -\varepsilon
 \begin{pmatrix}D&0\\0&M\end{pmatrix}
 \preceq
 \mathcal E
 \preceq
 \varepsilon
 \begin{pmatrix}D&0\\0&M\end{pmatrix},
 \qquad 0\le\varepsilon<h.
 }
 \tag{L-15632.7}
\]

Equivalently, the self-adjoint block obtained by whitening `mathcal E` with
`diag(D,M)` has operator norm at most `epsilon`.

## 3. Exact theorem

Let

\[
 \mathscr S
 =B-Z^*C^{-1}Z
 \tag{L-15632.8}
\]

be the actual harmonic Schur complement. Then

\[
 \boxed{
 \mathscr S\succeq-\eta D,
 }
 \tag{L-15632.9}
\]

where

\[
 \boxed{
 \eta
 =
 \varepsilon\left(1+\frac\ell h\right)
 +
 \frac{\varepsilon^2}{h-\varepsilon}
 \left(1+\sqrt{\frac\ell h}\right)^2.
 }
 \tag{L-15632.10}
\]

In particular, if another packet metric `G` satisfies

\[
 D\preceq qG,
 \tag{L-15632.11}
\]

then

\[
 \boxed{
 \left\|
 \left[
 G^{-1/2}\mathscr S G^{-1/2}
 \right]_{-}
 \right\|
 \le q\eta.
 }
 \tag{L-15632.12}
\]

## 4. Proof

Put

\[
 X_0=(C^0)^{-1}Z^0.
 \tag{L-15632.13}
\]

This is the exact harmonic minimizer for the line-centered block. Since
`mathcal H^0` is positive semidefinite,

\[
 B^0-(Z^0)^*(C^0)^{-1}Z^0\succeq0.
 \tag{L-15632.14}
\]

Moreover,

\[
\begin{aligned}
 X_0^*MX_0
 &\preceq h^{-1}X_0^*C^0X_0\\
 &=h^{-1}(Z^0)^*(C^0)^{-1}Z^0\\
 &\preceq h^{-1}B^0\\
 &\preceq \frac\ell hD.
\end{aligned}
 \tag{L-15632.15}
\]

Let

\[
 J_0s=(s,-X_0s).
 \tag{L-15632.16}
\]

The line-centered trial energy is nonnegative:

\[
 J_0^*\mathcal H^0J_0
 =B^0-(Z^0)^*(C^0)^{-1}Z^0
 \succeq0.
 \tag{L-15632.17}
\]

Using (L-15632.7) and (L-15632.15),

\[
\begin{aligned}
 J_0^*\mathcal HJ_0
 &\succeq
 -\varepsilon(D+X_0^*MX_0)\\
 &\succeq
 -\varepsilon\left(1+\frac\ell h\right)D.
\end{aligned}
 \tag{L-15632.18}
\]

The actual ambient block satisfies

\[
 C\succeq(h-\varepsilon)M.
 \tag{L-15632.19}
\]

The residual of the line-centered trial solve in the actual block is

\[
\begin{aligned}
 \mathscr R_0
 &=Z-CX_0\\
 &=(Z-Z^0)-(C-C^0)X_0.
\end{aligned}
 \tag{L-15632.20}
\]

Whiten (L-15632.7). Every block of the whitened perturbation has norm at most
`epsilon`. Equation (L-15632.15) therefore gives

\[
 \left\|
 M^{-1/2}\mathscr R_0D^{-1/2}
 \right\|
 \le
 \varepsilon
 \left(1+\sqrt{\frac\ell h}\right).
 \tag{L-15632.21}
\]

Consequently,

\[
 \mathscr R_0^*M^{-1}\mathscr R_0
 \preceq
 \varepsilon^2
 \left(1+\sqrt{\frac\ell h}\right)^2D.
 \tag{L-15632.22}
\]

Apply the direct residual-shorting identity of `L-18512` with trial solve
`X_0` and the coercivity (L-15632.19):

\[
\begin{aligned}
 \mathscr S
 &\succeq
 J_0^*\mathcal HJ_0
 -(h-\varepsilon)^{-1}
 \mathscr R_0^*M^{-1}\mathscr R_0\\
 &\succeq-\eta D.
\end{aligned}
 \tag{L-15632.23}
\]

This proves (L-15632.9)--(L-15632.10). Compression by `G^{-1/2}` and
(D<=qG) prove (L-15632.12). QED.

## 5. Cofinal form

Suppose along a support sequence

\[
 h_R\ge c\log R,
 \qquad
 \ell_R\le C\log R,
 \qquad
 \varepsilon_R=o(\log R),
 \tag{L-15632.24}
\]

with fixed positive `c,C`. Then

\[
 \eta_R=o(\log R).
 \tag{L-15632.25}
\]

Therefore every soft packet satisfying

\[
 D_R|_{S_R}\preceq q_RG_R,
 \qquad
 q_R\log R\longrightarrow0,
 \tag{L-15632.26}
\]

obeys

\[
 \boxed{
 \left\|
 \left[
 G_R^{-1/2}\mathscr S_RG_R^{-1/2}
 \right]_{-}
 \right\|
 \longrightarrow0.
 }
 \tag{L-15632.27}
\]

The theorem is dimension-free. The rank of `S_R` may grow arbitrarily.

## 6. Exact relation to the Suzuki production matrix

The actual matrix `mathcal H` is assembled from:

1. every archimedean/local Weil term;
2. every prime power in the exact Suzuki support;
3. the full polar channel, with terminal-prime pole cancellation performed
   before interval contraction;
4. the low--ambient harmonic cross and ambient block.

The comparator `mathcal H^0` is the same zero-side matrix after every zero
parameter is moved horizontally to its real ordinate. It is positive
semidefinite because every centered zero contribution is a positive rank-one
square.

The difference `mathcal E` is exactly the complete horizontal-displacement
matrix. The support-average theorem acts on this full matrix before the soft
projector is formed. Therefore no selected zero, terminal matrix, polar term,
or harmonic cross is charged separately in (L-15632.7).

## 7. Production form with an approximate line-centered solve

A proof-producing implementation may replace `X_0` by a finite form-core solve
`X_N`. If its line-centered residual satisfies

\[
 (Z^0-C^0X_N)^*M^{-1}(Z^0-C^0X_N)
 \preceq\sigma_N^2D,
 \tag{L-15632.28}
\]

then the right side of (L-15632.9) acquires only

\[
 {\sigma_N^2\over h}D
 \tag{L-15632.29}
\]

plus the corresponding mixed perturbation term. At every finite support,
form-core density allows `sigma_N` to be made arbitrarily small. The directed
producer should retain this residual exactly as in `L-18512`.

## 8. Scope and gap audit

- No RH assumption is used: the line-centered block is an artificial positive
  comparator, not an assertion about the actual zero locations.
- The theorem is stronger than a separate bound for the terminal-prime matrix
  and the harmonic cross because it permits their cancellation inside the full
  perturbation and trial-lift energy.
- Small ordinary profile mass alone is insufficient; `R-15604` remains valid.
  The new load-bearing input is the relative **complete-block** perturbation
  (L-15632.7).
- The theorem does not itself construct the support sequence or prove
  (L-15632.7) for the production frame. That composition is `T-15606`.
