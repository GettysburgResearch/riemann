# L-20807 — Negative channels short to one conditional Christoffel defect

Claim ID: `L-20807`  
Title: A finite negative channel changes the source Schur value by one exact Woodbury–Christoffel quotient  
Status: `PROVED FINITE ALGEBRA; ZETA CONDITIONAL-DEFECT MOAT OPEN`  
Authoring agent: `gpt56-03-t`  
Created: 2026-08-01  
Dependencies: `L-20806`; Woodbury's identity; finite orthogonal-polynomial algebra  
Scope: line-centered positive comparators and finite off-line channel packets  
Related counterexample candidates: none

## 1. Positive comparator and negative channel

Use source coordinates `C e direct-sum W`. Let

\[
 H^0=
 \begin{pmatrix}
  a&r^*\\
  r&C_0
 \end{pmatrix},
 \qquad
 C_0\succ0,
 \qquad
 H^0\succeq0,
 \tag{L-20807.1}
\]

and put

\[
 s_0=a-r^*C_0^{-1}r\ge0.
 \tag{L-20807.2}
\]

Let a finite negative channel be represented by

\[
 U=
 \begin{pmatrix}
  \alpha\\ B
 \end{pmatrix}
 :\mathbb C^k\longrightarrow\mathbb C e\oplus W,
 \tag{L-20807.3}
\]

where `alpha` is a `1 x k` row and `B:C^k->W`. Define

\[
 H=H^0-UU^*.
 \tag{L-20807.4}
\]

Its constrained block is

\[
 C=C_0-BB^*.
 \tag{L-20807.5}
\]

Set

\[
 \boxed{
 \Delta=I_k-B^*C_0^{-1}B
 }
 \tag{L-20807.6}
\]

and

\[
 \boxed{
 d=\alpha^*-B^*C_0^{-1}r.
 }
 \tag{L-20807.7}
\]

The vector `d` is the negative-channel evaluation on the canonical comparator
harmonic graph:

\[
 d=U^*y_0,
 \qquad
 y_0=e-C_0^{-1}r.
 \tag{L-20807.8}
\]

It is independent of every affine trial by `L-20806`.

## 2. Exact theorem

The constrained block is positive precisely when

\[
 \boxed{
 C\succ0
 \quad\Longleftrightarrow\quad
 \Delta\succ0.
 }
 \tag{L-20807.9}
\]

Whenever these equivalent conditions hold, the actual source Schur value is

\[
 \boxed{
 s(H)=s_0-d^*\Delta^{-1}d.
 }
 \tag{L-20807.10}
\]

### Proof

Apply the comparator harmonic congruence

\[
 T=
 \begin{pmatrix}
  1&0\\
  -C_0^{-1}r&I
 \end{pmatrix}.
 \tag{L-20807.11}
\]

It gives

\[
 T^*H^0T=
 \begin{pmatrix}
  s_0&0\\0&C_0
 \end{pmatrix}
 \tag{L-20807.12}
\]

and transforms the negative channel to

\[
 T^*U=
 \begin{pmatrix}
  d^*\\B
 \end{pmatrix}.
 \tag{L-20807.13}
\]

The lower block is `C_0-BB*`. The standard Schur complement of

\[
 \begin{pmatrix}I&B^*\\B&C_0\end{pmatrix}
\]

proves (L-20807.9). Woodbury gives

\[
 (C_0-BB^*)^{-1}
 =C_0^{-1}
 +C_0^{-1}B\Delta^{-1}B^*C_0^{-1}.
 \tag{L-20807.14}
\]

Shorting the transformed block, or substituting (L-20807.14), leaves exactly
`s_0-d*Delta^-1 d`. QED.

This formula combines the raw negative response and every inverse-metric
residual amplification before any estimate is taken.

## 3. Trial suppression is exactly compensated

For an arbitrary source trial `x_w=e+w`, the raw negative-channel value is

\[
 U^*x_w=\alpha^*+B^*w.
 \tag{L-20807.15}
\]

The comparator residual correction is

\[
 B^*C_0^{-1}(r+C_0w)
 =B^*C_0^{-1}r+B^*w.
 \tag{L-20807.16}
\]

Their difference is always

\[
 \boxed{
 U^*x_w-B^*C_0^{-1}P_WH^0x_w=d.
 }
 \tag{L-20807.17}
\]

Thus a notch inserted into `U*x_w` is canceled exactly by the corresponding
change in the residual projection. Only the canonical conditional amplitude
`d` enters the source Schur value.

## 4. Determinant form

Assume all displayed matrices are invertible. Then

\[
 \boxed{
 {\det H\over\det C}
 ={\det H^0\over\det C_0}
 -d^*\Delta^{-1}d
 =s(H).
 }
 \tag{L-20807.18}
\]

More precisely,

\[
 {\det C\over\det C_0}=\det\Delta
 \tag{L-20807.19}
\]

and

\[
 {\det H\over\det H^0}
 =\det\Delta\,
 {s(H)\over s_0}
 \tag{L-20807.20}
\]

when `s_0` is nonzero. These identities provide an independent directed
consumer for the conditional defect.

## 5. Orthogonal-polynomial / Christoffel corollary

Let `P_n` be the polynomials of degree at most `n`, equipped with a positive
inner product. Split

\[
 P_n=\mathbb C m_n\oplus P_{n-1},
 \tag{L-20807.21}
\]

where `m_n` is any monic degree-`n` trial. The source functional is the leading
coefficient. The comparator harmonic graph is the unique monic orthogonal
polynomial `p_n`, and

\[
 h_n=\|p_n\|^2=s_0.
 \tag{L-20807.22}
\]

Let `Z=(z_1,...,z_k)` be complex evaluation points, let `T=T*>0`, and subtract
the negative evaluation form

\[
 \langle f,g\rangle_{\rm new}
 =\langle f,g\rangle
 -(V_Zf)^*T(V_Zg).
 \tag{L-20807.23}
\]

Let `K_(n-1)(Z,Z)` be the reproducing-kernel matrix of `P_(n-1)`. Then the
lower-degree block remains positive exactly when

\[
 \boxed{
 T^{-1}-K_{n-1}(Z,Z)\succ0.
 }
 \tag{L-20807.24}
\]

Under this condition, the new monic norm is

\[
 \boxed{
 h_n^{\rm new}
 =h_n-p_n(Z)^*
  [T^{-1}-K_{n-1}(Z,Z)]^{-1}
  p_n(Z).
 }
 \tag{L-20807.25}
\]

For one point of weight `tau>0`,

\[
 \boxed{
 h_n^{\rm new}
 =h_n-{\tau|p_n(z)|^2
  \over1-\tau K_{n-1}(z,z)}.
 }
 \tag{L-20807.26}
\]

This is the negative-mass Uvarov formula. The denominator is the conditional
evaluation defect left after all lower-degree directions have been shorted.

## 6. One-step Christoffel interpretation

Since

\[
 K_n(z,z)=K_{n-1}(z,z)+{|p_n(z)|^2\over h_n},
 \tag{L-20807.27}
\]

single-channel positivity satisfies

\[
 h_n^{\rm new}\ge0
 \quad\Longleftrightarrow\quad
 \tau K_n(z,z)\le1,
 \tag{L-20807.28}
\]

whereas positivity of the constrained block alone is only

\[
 \tau K_{n-1}(z,z)<1.
 \tag{L-20807.29}
\]

The irreducible source scalar is therefore exactly the **next Christoffel
increment** beyond the already-positive constrained packet. No trial polynomial
can alter this increment.

## 7. Application to the D-0001 source gate

For a proof-grade line-centered comparator, diagonalize the finite horizontal
off-line correction and absorb every positive channel into `H^0`. The remaining
negative channels have a matrix `U_M`. Equations (L-20807.6)--(L-20807.10) give

\[
 \boxed{
 {g_M\over\ell_MA_M^{-1}\ell_M^*}
 =s_{0,M}-d_M^*\Delta_M^{-1}d_M,
 }
 \tag{L-20807.30}
\]

in the source normalization.

Hence the requested estimate is precisely

\[
 \boxed{
 d_M^*\Delta_M^{-1}d_M
 \le s_{0,M}+\varepsilon_M,
 \qquad
 \Lambda_M\varepsilon_M+\delta_M\to0.
 }
 \tag{L-20807.31}
\]

The factorial response of an arbitrary trial does not bound either `d_M` or
`Delta_M`. A valid growing-notch argument must be proved for the canonical
orthogonal/source graph itself, or must control the conditional defect ratio
(L-20807.31) directly.

## 8. False-RH compensation mechanism

A complete hierarchy that captures a fixed off-line cardinal channel has the
following exact alternatives:

1. `Delta_M` loses positivity, so the constrained block `A_WW,M` ceases to be
   positive; or
2. `Delta_M` remains positive but the quotient
   `d_M*Delta_M^-1 d_M` leaves a fixed negative source gap.

This is the finite-rank version of `T-19701`. The inverse metric is not an
auxiliary numerical instability: it is the mechanism that restores a hidden
negative cardinal after any raw trial notch.

## 9. Proof boundary

- The finite-rank and orthogonal-polynomial formulas are exact.
- The theorem identifies the joint residual requested in the prompt with one
  conditional Christoffel quotient.
- No zeta-specific upper bound for that quotient is proved here.
- Proving (L-20807.31) on a complete cofinal hierarchy remains an RH-bearing
  theorem.
