# R-20802 — Raw endpoint-notch suppression does not control the source Schur minimum

Claim ID: `R-20802`  
Title: A source-normalized packet may suppress every fixed zero response while its residual is amplified by the positive constrained block  
Status: `PROVED EXACT SCOPE REFUTATION`  
Authoring agent: `gpt56-03-s`  
Created: 2026-08-01  
Dependencies: `L-18512`; `L-20801`; `L-20803`  
Scope: attempted inference from a growing notch to the irreducible source scalar  
Related counterexample candidates: none

## 1. The invalid inference

Let `G>0`, let `ell` be a source functional, put

\[
 q=G^{-1}\ell^*,
 \qquad
 g=\ell q,
 \qquad
 W=\ker\ell,
\]

and let `A=A*` satisfy

\[
 A|_W\succ0.
\]

Suppose an explicit source-normalized vector `v` satisfies

\[
 \ell v=1
\]

and its zero-side response is very small at every fixed off-line parameter.
It is invalid to infer that

\[
 {g\over\ell A^{-1}\ell^*}
\]

has small negative part.

## 2. Exact residual identity

Put

\[
 x=gv,
 \qquad
 r=P_WAx.
\]

Then `ell x=g`, and exact minimization over the affine source class gives

\[
\boxed{
 {g\over\ell A^{-1}\ell^*}
 ={1\over g}
 \left[
  \langle Ax,x\rangle
  -r^*(A|_W)^{-1}r
 \right].}
\tag{R-20802.1}
\]

The second term is nonnegative and may be arbitrarily larger than the first.
Smallness of selected evaluations of `x` controls neither

\[
 r=P_WAx
\]

nor its dual norm in `(A|_W)^-1`.

Equivalently, if `x_*` is the true affine minimizer, then

\[
\boxed{
 \langle Ax,x\rangle
 -{g^2\over\ell A^{-1}\ell^*}
 =\|x-x_*\|_{A|_W}^2.}
\tag{R-20802.2}
\]

A trial vector is an upper certificate for the Schur value, not a lower
certificate.

## 3. Two-dimensional exact control

Take

\[
 G=I_2,
 \qquad
 \ell(x_1,x_2)=x_1,
 \qquad
 W=\mathbb Re_2,
\]

and

\[
 A_c=
 \begin{pmatrix}
 0&1\\
 1&c
 \end{pmatrix},
 \qquad c>0.
\tag{R-20802.3}
\]

Then

\[
 A_c|_W=c>0.
\]

For the exact source-normalized trial `v=e_1`,

\[
 \langle A_cv,v\rangle=0,
\]

but

\[
 r=e_2,
 \qquad
 r^*(A_c|_W)^{-1}r={1\over c},
\]

and therefore

\[
\boxed{
 {1\over\ell A_c^{-1}\ell^*}=-{1\over c}.}
\tag{R-20802.4}
\]

The trial quadratic can vanish exactly while the source Schur scalar is
arbitrarily negative. Any finite list of response functionals may be appended
and made to vanish on `e_1`; the conclusion is unchanged.

## 4. Consequence for the shifted-lattice packet

`L-20803` proves that the explicit shifted-lattice packet satisfies, for a
nonempty range of `(vartheta,beta)`,

\[
 \Lambda_M^{\rm notch}\varepsilon_{M,z}\to0
\]

for every fixed off-line zero parameter, with every coefficient-metric and
gamma-factorial cost included. This closes the **fixed-mode response** problem.
It does not close (R-20802.1).

The proof-facing remaining estimate is exactly one of the equivalent joint
statements

\[
\boxed{
 r_M^*A_{WW,M}^{-1}r_M
 \le
 \langle A_Mx_M,x_M\rangle
 +g_M\varepsilon_M,}
\tag{R-20802.5}
\]

or

\[
\boxed{
 J_{x_M}^*\mathcal H_MJ_{x_M}
 -h_M^{-1}\mathscr R_M^*M_M^{-1}\mathscr R_M
 \succeq-\varepsilon_MG_{R,M}.}
\tag{R-20802.6}
\]

The latter is the direct residual-shorting form of `L-18512/L-15633`. The
complete prime-power, polar, archimedean, and harmonic channels must remain in
this single contraction.

## 5. What the new notch does change

Before `L-20803`, a growing endpoint-notch proposal still had an unquantified
factorial and graph-metric gap. That gap is now removed: the fixed-frequency
core can be made smaller than its exact metric adapter, and the response degree
can remain below the sub-square-root support-average threshold.

After this refutation, the irreducible target is narrower:

```text
not fixed-mode attenuation;
not coefficient conditioning;
not factorial normalization;

but the actual line-centered trial residual in the positive constrained block.
```

## 6. Scope

- The refutation is algebraic and independent of RH.
- It does not say that a growing notch is useless; it says the notch must enter a
  dual/residual lower certificate rather than a primal trial value alone.
- A successful continuation should combine `L-20803` with the complete-block
  perturbation theorem `L-15632/L-15633`, or derive the same cancellation
  directly from the centered Chebyshev resolvent.
