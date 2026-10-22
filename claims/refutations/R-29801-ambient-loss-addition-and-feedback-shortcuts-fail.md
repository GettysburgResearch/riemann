# R-29801 — Ambient-loss addition and feedback shortcuts fail

Claim ID: `R-29801`  
Title: The bulk and boundary constants must be assembled in the exact triangular source graph; both naive addition and an undeclared boundary-to-bulk edge can invalidate contraction  
Status: **EXACT SCOPE CORRECTION**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Dependencies: `L-29802/L-29803`

## 1. Adding the strict constants is the wrong test

The available strict factors are

\[
 \alpha={6\over7},
 \qquad
 \theta_*<{2\over3}.
\]

Their sum exceeds one.  A scalar ambient estimate of the form

\[
 E_{a+1}\le(\alpha+\theta_*)E_a+\cdots
\]

therefore cannot close the cascade.

The exact source graph is instead

\[
 \begin{pmatrix}A_{a+1}\\D_{a+1}\end{pmatrix}
 \le
 \begin{pmatrix}\alpha&0\\C&\theta_*\end{pmatrix}
 \begin{pmatrix}A_a\\D_a\end{pmatrix}+\cdots,
\]

whose spectral radius is `max(alpha,theta_*)<1`.

Thus failure of the scalar sum test is not an obstruction to the triangular proposal.

## 2. The zero upper-right block is load bearing

If a boundary state were allowed to regenerate one unit of current-scale analytic bulk, the homogeneous comparison matrix could become

\[
 M=\begin{pmatrix}6/7&1\\1&2/3\end{pmatrix}.
\]

Then

\[
 \det(I-M)
 =\left(1-{6\over7}\right)
  \left(1-{2\over3}\right)-1
 =-{20\over21}<0.
\]

Hence `M` has an eigenvalue greater than one.

A proof which merely bounds the boundary-to-bulk block instead of proving that it is absent does not establish contraction.  The exact no-feedback source typing in `L-29802` must be reconstructed.

## 3. Euler damping is not a third independent contraction

The finite Euler coefficients satisfy

\[
 \sum_{m=0}^{M-1}2^{-m-1}+2^{-M}=1.
\]

They partition one positive boundary source among finite jets and one exact remainder.  Adding `2^{-M}` to `theta_*`, or multiplying by a source-independent norm after taking total variation, double counts the same boundary event.

The eta–Pascal factor is applied after the Euler partition.

## 4. Positive coefficient forcing is not inversion

`L-29804` proves

\[
 (\varepsilon-\omega_2)*(a_\omega\log^2)\ge0
\]

coefficientwise.  This does not imply positivity of the Riesz mean of `epsilon-omega_2`: the positive kernel has no unit coefficient and no established positive inverse.

The coefficientwise defect is a forcing reserve, not a proof of Bottom-Charge Positivity.

## 5. Step-window sampling is not the full prime normal block

`L-29805` gives an exact physical/carry intertwiner for the compact dyadic numerator window.  It does not permit applying the inverse-zeta source once in the coefficients and a second time in the carry wavelet.

A full physical source map must retain the complete convolution and every boundary term.

## 6. Status boundary

This file refutes only the listed shortcuts.  It does not verify the triangular source typing or RH.
