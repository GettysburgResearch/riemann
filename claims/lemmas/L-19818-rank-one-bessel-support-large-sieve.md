# L-19818 — Rank-one Bessel support large sieve

Claim ID: `L-19818`  
Title: A rank-one zero-profile family pays one source envelope, not its square, under support averaging  
Status: `PROPOSED — COMPLETE ABSTRACT THEOREM; SOURCE-SPECIFIC PROFILE GATES SEPARATE`  
Authoring agent: `gpt56-pro-09-n`  
Created: 2026-08-07  
Dependencies: the support-phase separation geometry of `L-16226`; the Riemann--von Mangoldt unit-interval count; elementary Hilbert-space Bessel estimates  
Scope: complete-frame horizontal/off-line support averaging

## 1. Why a sharper theorem is needed

The generic Hilbert-valued large sieve in `L-16226` treats each coefficient
`A_gamma(R)` as an arbitrary Hilbert-space vector.  In the Weil matrix, however,
the zero contribution is rank one:

\[
 A_\gamma(R)=u_\gamma(R)\otimes v_\gamma(R)^*.
\]

Bounding its Hilbert--Schmidt norm pointwise by

\[
 \|A_\gamma\|_{\rm HS}\leq
 \|u_\gamma\|\,\|v_\gamma\|
\]

and then using the same worst-case envelope for both factors squares the
source-conditioning loss.  That is unnecessary.  One factor may be controlled
pointwise, while the other is summed through the positive line-centered profile
Gram.  The resulting estimate pays only one squared vector envelope.

This distinction is load-bearing for the smooth complete source frame.  Its
regularized vector envelope is of order `R^(3/8+o(1))`; the generic outer-product
bound would see `R^(3/4+o(1))`, whereas the theorem below retains the former
scale.

## 2. Phase and zero-count hypotheses

Fix constants

\[
 0<a<b<\infty
\]

and let `T>=2`.  Let `Gamma_T` be a finite multiset in `[aT,bT]`, counted with
multiplicity.  Assume the unit-bin bound

\[
 \boxed{
 \#\bigl(\Gamma_T\cap[j,j+1)\bigr)\leq L_T
 }
 \tag{L-19818.1}
\]

for every integer `j`, where

\[
 L_T\leq C\log(2T).
 \tag{L-19818.2}
\]

Let `I` be a fixed compact interval and let `S in C^3(I;R)`.  Put

\[
 F(x)=S(x)-xS'(x).
 \tag{L-19818.3}
\]

Assume `I` is the union of a fixed number of intervals on each of which

\[
 |F'(x)|\geq c_0>0.
 \tag{L-19818.4}
\]

The phase attached to `gamma` is

\[
 \phi_\gamma(R)=R S(\gamma/R).
 \tag{L-19818.5}
\]

Thus

\[
 \phi_\gamma'(R)=F(\gamma/R).
 \tag{L-19818.6}
\]

As in `L-16226`, finitely many phase branches and finitely many fixed smooth
partitions are harmless and only change the constants.

## 3. Rank-one profiles

Let `H_T` be a complex Hilbert space of finite dimension `d_T`.  For every
`gamma in Gamma_T` let

\[
 u_\gamma(R),v_\gamma(R)\in H_T,
 \qquad T\leq R\leq2T,
 \tag{L-19818.7}
\]

be `C^1`, supported where `gamma/R in I`.

Assume the one-sided pointwise graph envelope

\[
 \boxed{
 \|u_\gamma(R)\|+
 T\|\partial_Ru_\gamma(R)\|
 \leq M_T.
 }
 \tag{L-19818.8}
\]

Assume the other profile family satisfies the operator Bessel bounds

\[
 \boxed{
 \sum_{\gamma\in\Gamma_T}
 v_\gamma(R)v_\gamma(R)^*
 \preceq E_T I,
 }
 \tag{L-19818.9}
\]

and

\[
 \boxed{
 T^2\sum_{\gamma\in\Gamma_T}
 (\partial_Rv_\gamma(R))
 (\partial_Rv_\gamma(R))^*
 \preceq E_T I
 }
 \tag{L-19818.10}
\]

uniformly in `R`.  The local-Weyl application has

\[
 E_T\ll T\log(2T).
 \tag{L-19818.11}
\]

Define the rank-one support sum

\[
 \boxed{
 Z_T(R)=\frac1R
 \sum_{\gamma\in\Gamma_T}
 e^{i\phi_\gamma(R)}
 u_\gamma(R)\otimes v_\gamma(R)^*.
 }
 \tag{L-19818.12}
\]

## 4. Theorem

Under the preceding hypotheses,

\[
 \boxed{
 \frac1T\int_T^{2T}
 \|Z_T(R)\|_{\rm HS}^2\,dR
 \leq
 C
 \frac{d_T M_T^2 L_T\log(2T) E_T}{T^2}.
 }
 \tag{L-19818.13}
\]

Consequently, when

\[
 L_T\ll\log T,
 \qquad E_T\ll T\log T,
 \tag{L-19818.14}
\]

one has

\[
 \boxed{
 \frac1T\int_T^{2T}
 \|Z_T(R)\|_{\rm op}^2\,dR
 \leq
 C\frac{d_T M_T^2(\log T)^3}{T}.
 }
 \tag{L-19818.15}
\]

In particular, if

\[
 \boxed{
 d_T M_T^2\frac{\log T}{T}\longrightarrow0,
 }
 \tag{L-19818.16}
\]

then there are supports `R_T in [T,2T]` for which

\[
 \boxed{
 \|Z_T(R_T)\|_{\rm op}=o(\log T).
 }
 \tag{L-19818.17}
\]

If the stronger right side in (L-19818.15) tends to zero, the selected operator
itself tends to zero.

The support may simultaneously avoid a prescribed measure-zero set and any
finite or `T^(o(1))` family of additional bad sets whose total relative measure
tends to zero.

## 5. Proof: Hilbert--Schmidt expansion

Write

\[
 U_\gamma=u_\gamma\otimes v_\gamma^*.
\]

Then

\[
 \langle U_\gamma,U_{\gamma'}\rangle_{\rm HS}
 =\langle u_\gamma,u_{\gamma'}\rangle
  \langle v_{\gamma'},v_\gamma\rangle.
 \tag{L-19818.18}
\]

Hence

\[
 \begin{aligned}
 \|Z_T(R)\|_{\rm HS}^2
 =\frac1{R^2}
 \sum_{\gamma,\gamma'}
 e^{i(\phi_\gamma-\phi_{\gamma'})}
 \langle u_\gamma,u_{\gamma'}\rangle
 \langle v_{\gamma'},v_\gamma\rangle.
 \end{aligned}
 \tag{L-19818.19}
\]

The trace consequence of (L-19818.9)--(L-19818.10) is

\[
 \sum_\gamma\|v_\gamma(R)\|^2
 +T^2\sum_\gamma\|\partial_Rv_\gamma(R)\|^2
 \leq d_T E_T.
 \tag{L-19818.20}
\]

This is the only dimension cost.  No entrywise `d_T^2` summation occurs.

## 6. Near-bin pairs

Group ordinates into unit bins.  For equal or adjacent bins, use the trivial
phase bound.  Cauchy--Schwarz inside each bin and (L-19818.1) give

\[
 \sum_{\substack{\gamma,\gamma'\\
 |j(\gamma)-j(\gamma')|\leq1}}
 |\langle v_{\gamma'},v_\gamma\rangle|
 \leq C L_T\sum_\gamma\|v_\gamma\|^2.
 \tag{L-19818.21}
\]

Together with (L-19818.8), (L-19818.20), and `R asymp T`, the contribution of
near pairs to the averaged integral is at most

\[
 C\frac{d_T M_T^2L_TE_T}{T^2}.
 \tag{L-19818.22}
\]

## 7. Separated-bin pairs

Let the two ordinates lie in bins whose distance is `r>=2`.  On every common
phase branch, (L-19818.4) and the mean-value theorem give

\[
 |\phi_\gamma'(R)-\phi_{\gamma'}'(R)|
 \geq c\frac rT,
 \tag{L-19818.23}
\]

while the derivative of the left side is `O(r/T^2)`.  Integrating by parts in
`R`, and differentiating the factor `R^-2` and the two profile inner products,
gives a pair bound of the form

\[
 \frac{CM_T^2}{Tr}
 \Bigl(
 |\langle v_{\gamma'},v_\gamma\rangle|
 +T|\langle\partial_Rv_{\gamma'},v_\gamma\rangle|
 +T|\langle v_{\gamma'},\partial_Rv_\gamma\rangle|
 \Bigr),
 \tag{L-19818.24}
\]

with the endpoint values included.

For bin `j`, put

\[
 B_j=\sum_{\gamma\in[j,j+1)}\|v_\gamma\|^2,
 \qquad
 \dot B_j=T^2\sum_{\gamma\in[j,j+1)}
 \|\partial_Rv_\gamma\|^2.
 \tag{L-19818.25}
\]

Cauchy--Schwarz and the bin population bound show that the total numerator for
bin pair `(j,k)` is at most

\[
 CM_T^2L_T
 \sqrt{B_j+\dot B_j}
 \sqrt{B_k+\dot B_k}.
 \tag{L-19818.26}
\]

The finite Hilbert matrix with kernel `1/|j-k|` has `ell^2` norm
`O(log(2T))`.  Therefore summing (L-19818.24) gives

\[
 C\frac{M_T^2L_T\log(2T)}T
 \sum_j(B_j+\dot B_j)
 \leq
 C\frac{d_TM_T^2L_T\log(2T)E_T}T.
 \tag{L-19818.27}
\]

This is the integral before division by the outer averaging length `T`.  It
proves (L-19818.13).  Equations (L-19818.15)--(L-19818.17) follow from
`||Z||_op<=||Z||_HS` and Markov's inequality. QED.

## 8. Comparison with the generic operator-amplitude estimate

Suppose a whitened profile vector has envelope `M_T`.  Its rank-one outer
product has pointwise Hilbert--Schmidt envelope `M_T^2`.  Feeding that generic
operator envelope into `L-16226` would produce a fourth power `M_T^4`.

The present theorem instead uses the positive Bessel sum for the second factor
and produces only

\[
 d_TM_T^2(\log T)^3/T.
 \tag{L-19818.28}
\]

For a `T^(o(1))`-dimensional smooth complete source frame with

\[
 M_T=T^{3/8+o(1)},
 \tag{L-19818.29}
\]

this is

\[
 T^{-1/4+o(1)},
 \tag{L-19818.30}
\]

whereas the generic outer-product estimate does not decay.  This is the precise
one-factor saving needed by the whole-matrix positive route.

## 9. Fold and endpoint channels

A fixed finite number of Airy/fold windows may be removed and charged by their
shrinking measure exactly as in `L-16226`.  Endpoint-polylogarithm and Poisson
channels may either be retained as additional phase families or placed into the
regular error, provided their Bessel and derivative ledgers are included.

The theorem does not authorize dropping a nonoscillatory diagonal channel.  In
the Weil application, such channels belong to the positive line-centered main
profile or to the separately bounded regular correction.

## 10. Proof boundary

- The rank-one large-sieve theorem is abstract and unconditional.
- The application must produce the Bessel bounds (L-19818.9)--(L-19818.10) in
  the same regularized metric used for the pointwise envelope.
- The theorem controls the oscillatory cross/off-line block; it does not itself
  prove the line-centered local-Weyl lower estimate.
- No RH conclusion is asserted by this lemma alone.
