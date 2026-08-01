# L-15634 — The explicit main-density profile block closes the soft Schur estimate

Claim ID: `L-15634`  
Title: The Riemann--von Mangoldt main profile Gram is a positive comparator, so no full line-centered zero matrix is needed  
Status: `PROVED ABSTRACT COMPOSITION; PRODUCTION JOINT-PROFILE LEDGER OPEN`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Dependencies: `L-15632`, `L-15633`, `L-16220`, `L-16226`  
Scope: explicit comparator for the exported profile-soft packet  
Related counterexample candidates: none

## 1. Purpose

`T-15606` compares the actual complete Weil block with the full artificial
line-centered zero block. That is mathematically clean, but a production
certificate should not have to construct an infinite line-zero matrix or its
harmonic minimizer.

The Riemann--von Mangoldt main density already supplies an explicit positive
comparator. It is the joint source/harmonic profile Gram multiplied by
`log R`. The bounded line-centered correction and the horizontally displaced
zero block are then treated together as one perturbation.

## 2. Joint profile Gram

Let `U_R` be the finite low/source packet and `E_R` the finite harmonic packet.
Let

\[
 \mathcal P_R:U_R\oplus E_R\longrightarrow\mathcal Y_R
 \tag{L-15634.1}
\]

be the complete line-centered profile synthesis entering the zero-side local
Weyl theorem. Write its positive Gram as

\[
 \mathcal D_R
 =\mathcal P_R^*\mathcal P_R
 =
 \begin{pmatrix}
 D_R&Y_R^*\\
 Y_R&M_R
 \end{pmatrix}
 \succeq0,
 \qquad M_R\succ0.
 \tag{L-15634.2}
\]

The low profile Gram `D_R` is the same object used in the soft/hard split. Let

\[
 \widehat D_R=D_R+\tau_RG_R
 \tag{L-15634.3}
\]

be its regularization.

Define the explicit main-density comparator

\[
 \boxed{
 \mathcal H_R^{\rm main}
 =
 (\log R)\mathcal D_R.
 }
 \tag{L-15634.4}
\]

It is positive semidefinite. Its blocks are

\[
 B_R^{\rm main}=(\log R)D_R,
 \quad
 Z_R^{\rm main}=(\log R)Y_R,
 \quad
 C_R^{\rm main}=(\log R)M_R.
 \tag{L-15634.5}
\]

Therefore `L-15632` applies with

\[
 h_R=\ell_R=\log R,
 \qquad
 D=\widehat D_R.
 \tag{L-15634.6}
\]

## 3. Explicit harmonic minimizer

The comparator's exact harmonic minimizer is

\[
 \boxed{
 X_R^{\rm prof}=M_R^{-1}Y_R.
 }
 \tag{L-15634.7}
\]

Positivity of the joint profile Gram gives its Schur complement inequality

\[
 D_R-Y_R^*M_R^{-1}Y_R\succeq0.
 \tag{L-15634.8}
\]

Hence

\[
 \boxed{
 (X_R^{\rm prof})^*M_RX_R^{\rm prof}
 \preceq D_R\preceq\widehat D_R.
 }
 \tag{L-15634.9}
\]

Thus the trial graph has no condition-number loss at all in the declared
profile metrics.

## 4. Complete perturbation

Let `H_R` be the actual complete prime/polar/archimedean/harmonic block. Split

\[
 \mathcal H_R-\mathcal H_R^{\rm main}
 =
 \underbrace{
  (\mathcal H_R^{\rm line}-\mathcal H_R^{\rm main})
 }_{\mathcal C_R^{\rm line}}
 +
 \underbrace{
  (\mathcal H_R-\mathcal H_R^{\rm line})
 }_{\mathcal E_R^{\rm hor}}.
 \tag{L-15634.10}
\]

The first term is the line-centered counting correction. The dimension-free
operator local Weyl theorem gives, in the block metric

\[
 \widehat{\mathcal G}_R
 =\widehat D_R\oplus M_R,
 \tag{L-15634.11}
\]

\[
 \boxed{
 \left\|
 \widehat{\mathcal G}_R^{-1/2}
 \mathcal C_R^{\rm line}
 \widehat{\mathcal G}_R^{-1/2}
 \right\|
 \le c_R,
 \qquad
 c_R=O(1)+o(\log R).
 }
 \tag{L-15634.12}
\]

The second term is the complete horizontal-displacement block. The
support-average theorem selects a support from every retained dyadic block for
which

\[
 \boxed{
 \left\|
 \widehat{\mathcal G}_R^{-1/2}
 \mathcal E_R^{\rm hor}
 \widehat{\mathcal G}_R^{-1/2}
 \right\|
 \le\delta_R,
 \qquad
 \delta_R=o(\log R).
 }
 \tag{L-15634.13}
\]

Consequently the total perturbation satisfies `L-15632.7` with

\[
 \varepsilon_R=c_R+\delta_R=o(\log R).
 \tag{L-15634.14}
\]

## 5. Soft Schur conclusion

At the selected support define

\[
 S_R=\operatorname{Ran}
 \mathbf1_{[0,\tau_R]}
 (G_R^{-1/2}D_RG_R^{-1/2}).
 \tag{L-15634.15}
\]

Then

\[
 \widehat D_R|_{S_R}\preceq2\tau_RG_R|_{S_R}.
 \tag{L-15634.16}
\]

Since `ell/h=1`, `L-15632` gives

\[
 \mathscr S_R^{\rm soft}
 \succeq
 -\eta_R\widehat D_R|_{S_R},
 \tag{L-15634.17}
\]

where

\[
 \boxed{
 \eta_R
 =2\varepsilon_R
 +{4\varepsilon_R^2\over\log R-\varepsilon_R}.
 }
 \tag{L-15634.18}
\]

Therefore

\[
 \boxed{
 \left\|
 \left[
 G_{S,R}^{-1/2}
 \mathscr S_R^{\rm soft}
 G_{S,R}^{-1/2}
 \right]_{-}
 \right\|
 \le
 2\tau_R
 \left[
 2\varepsilon_R
 +{4\varepsilon_R^2\over\log R-\varepsilon_R}
 \right].
 }
 \tag{L-15634.19}
\]

In particular, the soft signature tends to zero whenever

\[
 \boxed{
 \tau_R\varepsilon_R\longrightarrow0,
 \qquad
 {\tau_R\varepsilon_R^2\over\log R}\longrightarrow0.
 }
 \tag{L-15634.20}
\]

## 6. Rate under the complete-frame schedule

Use the notation of `T-15606`:

\[
 \mathfrak a_T
 ={\mathfrak M_T^2(\log T)^2\over T},
 \qquad
 \tau_T={\sqrt{\mathfrak a_T}\over\log T}.
 \tag{L-15634.21}
\]

The horizontal support selection gives

\[
 \delta_T=O(\mathfrak a_T^{1/4}\log T).
 \tag{L-15634.22}
\]

If the line-centered remainder is bounded, `c_T=O(1)`, then

\[
\boxed{
\begin{aligned}
 \left\|
 \left[
 G_{S,T}^{-1/2}
 \mathscr S_T^{\rm soft}
 G_{S,T}^{-1/2}
 \right]_{-}
 \right\|
 &\le
 O\!\left({\sqrt{\mathfrak a_T}\over\log T}\right)\\
 &\quad+O(\mathfrak a_T^{3/4})
 +O(\mathfrak a_T)\\
 &\longrightarrow0.
\end{aligned}
}
 \tag{L-15634.23}
\]

Thus the explicit main-density comparator loses a slower but still vanishing
term relative to the full line-centered comparator. It removes the need to
construct any infinite line-zero matrix.

## 7. Graph-only producer

The same conclusion follows from `L-15633` by support-averaging only:

\[
 J_{X^{\rm prof}}^*
 (\mathcal H_R-\mathcal H_R^{\rm main})
 J_{X^{\rm prof}}
 \tag{L-15634.24}
\]

and

\[
 Z_R-C_RX_R^{\rm prof}.
 \tag{L-15634.25}
\]

Equation (L-15634.9) guarantees the graph envelope is no larger than the
combined low and harmonic envelopes. The covariant derivative theorem of
`L-15633` applies to `M_RX_R^{prof}=Y_R`.

Accordingly, the production proof object needs only the explicit joint profile
Gram, not a line-centered zero manifest.

## 8. Proof boundary

- The main-density comparator and its minimizer are explicit finite profile
  algebra.
- The local-Weyl and support-average inputs are the source-specific analytic
  gates already declared in `L-16220/L-16226`.
- A production certificate must emit the joint profile Gram and directed
  operator remainders on the complete source/harmonic frame.
- No such production packet has yet been emitted, and no RH conclusion is
  claimed by this lemma alone.
