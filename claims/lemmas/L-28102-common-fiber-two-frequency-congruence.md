# L-28102 — Common-fiber congruence for the two-frequency physical block

Claim ID: `L-28102`  
Title: Every exact independent-frequency source identity and positive matrix reserve lifts through a common arithmetic fiber by congruence, with the same coercivity constant  
Status: **PROPOSED COMPLETE ABSTRACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #281  
Dependencies: PR #241 `L-9518`; finite Hermitian linear algebra  
Scope: source maps which are linear over the common fiber; commutator rows must be exported explicitly

## 1. Two-frequency physical block

Let a finite source field have Fourier vector

\[
F(t)\in\mathbb C^d.
\]

For one physical block, write its exact normal energy as

\[
\mathcal Q_A(F)
=
\iint_{\mathbb R^2}
F(t)^*A_J(t,s)F(s)
\Phi_J(t-s)\,dt\,ds,
\tag{L-28102.1}
\]

where `Phi_J` is the reviewed block kernel and `A_J(t,s)` is the complete
source matrix, including every independent-frequency cross term.

Let `h(t)` be the frequency multiplier of one common arithmetic fiber and put

\[
F_h(t)=h(t)F(t).
\tag{L-28102.2}
\]

Then

\[
\boxed{
\mathcal Q_A(F_h)
=
\iint
F(t)^*
\overline{h(t)}A_J(t,s)h(s)
F(s)\Phi_J(t-s)\,dt\,ds.
}
\tag{L-28102.3}
\]

Thus fiber multiplication acts by congruence on the complete two-frequency
kernel.

## 2. Positivity and reserve lift

Suppose two exact physical forms satisfy

\[
\mathcal Q_A(F)\ge\kappa\,\mathcal Q_G(F)
\tag{L-28102.4}
\]

for every represented source vector `F`, with `kappa>=0`.

Apply (L-28102.4) to the represented vector `F_h`. One obtains

\[
\boxed{
\mathcal Q_A(F_h)\ge\kappa\,\mathcal Q_G(F_h).
}
\tag{L-28102.5}
\]

No norm of `h` enters. Zeros of `h` may reduce the represented subspace but
cannot decrease the reserve constant on the image.

In a finite source basis, if

\[
A-\kappa G\succeq0
\]

and `M_h` is the exact matrix of common-fiber convolution/translation, then

\[
\boxed{
M_h^*(A-\kappa G)M_h\succeq0.
}
\tag{L-28102.6}
\]

This is the proof-producing form of the lift.

## 3. Block Schur certificates

A production boundary theorem may be exported as one full block inequality

\[
\begin{pmatrix}
G_B&C^*\\
C&D
\end{pmatrix}
-
\kappa
\begin{pmatrix}
G_{\rm source}&0\\
0&0
\end{pmatrix}
\succeq0.
\tag{L-28102.7}
\]

Congruence with the common-fiber map on every source coordinate gives

\[
\boxed{
M_h^*
\left[
\begin{pmatrix}
G_B&C^*\\
C&D
\end{pmatrix}
-
\kappa
\begin{pmatrix}
G_{\rm source}&0\\
0&0
\end{pmatrix}
\right]
M_h
\succeq0.
}
\tag{L-28102.8}
\]

Therefore a strict source-bound Schur reserve, once authenticated as a full LMI,
survives every common fiber with the same `kappa`.

The certificate should lift the full matrix, not separately invert the
fibered `D` block. This remains valid even when the common fiber is not
injective.

## 4. Exact source maps

Let

\[
I=P+B
\tag{L-28102.9}
\]

be an exact source decomposition on a fixed arithmetic source. Suppose `P` and
`B` are module-linear over convolution by `h`, meaning

\[
P(f*h)=(Pf)*h,
\qquad
B(f*h)=(Bf)*h.
\tag{L-28102.10}
\]

Then

\[
\boxed{
I=P_h+B_h
}
\tag{L-28102.11}
\]

on the fibered source, with every coefficient and cross term retained.

The same applies to finite dyadic delays, parity projections, convolution
multipliers, and source-incidence matrices which act only on the fixed source
coordinate.

## 5. Boundary commutator warning

Physical block restriction and arithmetic convolution need not commute:

\[
\chi_J(f*h)
\ne
(\chi_Jf)*h
\]

as an identity of unrestricted functions. The discrepancy consists of explicit
block-entry and block-exit rows.

Consequently the common-fiber theorem permits exactly two treatments:

1. construct the physical source map directly after fiber convolution; or
2. export every cutoff commutator as a declared boundary/lower-block row.

A certificate which merely says “convolution commutes” after inserting a block
cutoff is rejected.

Likewise, a carry operator depending on the total product index is not
automatically module-linear in an arbitrarily chosen tuple coordinate. The
production manifest must prove the marked-coordinate source binding.

## 6. Application to the top source

By `L-28101`,

\[
S_{K,V}=\omega_2*H_{K,V}.
\]

Every exact independent-frequency matrix theorem for the fixed source
`omega_2` which is:

- source complete;
- module-linear in a common fiber;
- exported as a full PSD/LMI certificate;
- explicit about block commutators;

lifts to `S_(K,V)` with exactly the same reserve and condition numbers.

Thus the packet order creates no new matrix-conditioning loss. The only
remaining issue is whether the fixed-source boundary/commutator theorem exists
and whether all of its rows are genuinely module-linear or explicitly lifted.

## 7. Proof boundary

Closed exactly:

- two-frequency fiber congruence;
- preservation of PSD inequalities and strict reserves;
- preservation of exact module-linear source decompositions;
- the correct treatment of noninjective fibers.

Not closed:

- the actual fixed-source boundary/transverse decomposition;
- block-cutoff and total-product carry source binding;
- the factor-five boundary recurrence;
- RH.
