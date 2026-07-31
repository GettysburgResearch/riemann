# L-14319 — Certified-zero frame and S-lemma visible-block floor

Claim ID: `L-14319`  
Title: A certified-zero evaluation cone has an exact one-parameter spectral dual, and its block floor is a visibility-weighted interpolation  
Status: `PROPOSED`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: homogeneous S-lemma under Slater; `L-14308`; `L-14318`; the Weil spectral formula for the certified-zero specialization  
Scope: the evaluation-visible finite block left open by `L-15304`, PR #159, and the capacity-saturation stack  
Related counterexample candidates: none

## Purpose

`L-15304` shows that a low-packet direction whose Fourier--Mellin transform is
visible at certified zeta zeros cannot be approximated by a small-tail global
radical.  That result is an obstruction, not a lower bound.  The present lemma
turns the same evaluation geometry into a positive certificate.

The unexpected bridge is the homogeneous S-lemma: after whitening the zero
evaluations, the visible set is described by one quadratic inequality.  Its
minimum Weil energy is therefore the supremum of a **one-parameter family of
ordinary minimum-eigenvalue problems**.  When combined with the block
Temple--Schur theorem, the entire visible cone is reduced to:

```text
one certified-zero representer block,
one already-certified complement floor,
one scalar multiplier.
```

No basis of the visible cone and no principal-angle convergence theorem is
needed.

## 1. Abstract metric S-lemma

Let `H` be a finite-dimensional real vector space.  Let `G` be positive
definite and let `A,J` be real symmetric operators.  Fix a real number
`delta2` and assume the strict-feasibility condition

\[
 \exists x_0\ne0:
 \qquad x_0^{\mathsf T}(J-\delta^2G)x_0>0.
 \tag{L-14319.1}
\]

Define the visible cone and its exact lower floor by

\[
 \mathcal C_{J,\delta}
 =\{x\ne0:x^{\mathsf T}Jx\ge\delta^2x^{\mathsf T}Gx\},
 \tag{L-14319.2}
\]

\[
 \beta_{J,\delta}(A;G)
 =\inf_{x\in\mathcal C_{J,\delta}}
   \frac{x^{\mathsf T}Ax}{x^{\mathsf T}Gx}.
 \tag{L-14319.3}
\]

Then

\[
 \boxed{
 \beta_{J,\delta}(A;G)
 =\sup_{\alpha\ge0}
   \lambda_{\min}^{G}
   \bigl(A-\alpha(J-\delta^2G)\bigr),}
 \tag{L-14319.4}
\]

where

\[
 \lambda_{\min}^{G}(M)
 =\inf_{x\ne0}\frac{x^{\mathsf T}Mx}{x^{\mathsf T}Gx}.
\]

Equivalently, a real number `F` is a certified visible-cone floor whenever one
can exhibit `alpha>=0` such that

\[
 \boxed{
 A-\alpha(J-\delta^2G)-FG\succeq0.}
 \tag{L-14319.5}
\]

Conversely, every `F<beta_(J,delta)(A;G)` admits such a multiplier.  Thus the
finite certificate is complete up to an arbitrarily small rational retreat
from the exact optimum.

### Proof

For `x in C_(J,delta)` and `alpha>=0`,

\[
 x^{\mathsf T}Ax
 =x^{\mathsf T}[A-\alpha(J-\delta^2G)]x
  +\alpha x^{\mathsf T}(J-\delta^2G)x,
\]

so the right side of (L-14319.4) never exceeds the left side.

Fix `F<beta_(J,delta)(A;G)`.  Then

\[
 x^{\mathsf T}(J-\delta^2G)x\ge0
 \quad\Longrightarrow\quad
 x^{\mathsf T}(A-FG)x\ge0.
\]

The homogeneous S-lemma, using the strict point (L-14319.1), supplies
`alpha>=0` with

\[
 A-FG-\alpha(J-\delta^2G)\succeq0.
\]

Hence the supremum in (L-14319.4) is at least every `F<beta`.  Letting
`F` increase to `beta` proves equality.  QED.

## 2. Certified-zero whitening

Let `I` be a finite logarithmic support interval and let

\[
 Z=\{\gamma_1,\ldots,\gamma_m\}\subset\mathbb R
\]

be distinct proof-grade centered ordinates of actual critical-line zeta zeros.
On the full Hilbert space `L2(I)`, define

\[
 (V_Zf)_j=\widehat f(\gamma_j).
 \tag{L-14319.6}
\]

Let

\[
 H_Z=V_ZV_Z^*.
 \tag{L-14319.7}
\]

The distinct restricted exponentials are linearly independent, so `H_Z` is
positive definite and

\[
 \boxed{
 P_Z=V_Z^*H_Z^{-1}V_Z}
 \tag{L-14319.8}
\]

is the ordinary orthogonal projection onto the zero-representer space

\[
 \mathcal K_Z
 =\operatorname{span}\{e^{-i\gamma_jt}:1\le j\le m\}.
 \tag{L-14319.9}
\]

Moreover,

\[
 \boxed{
 \langle P_Zf,f\rangle
 =(V_Zf)^*H_Z^{-1}(V_Zf).}
 \tag{L-14319.10}
\]

Restricting these operators to any finite packet gives its exact evaluation
geometry. Thus the invariant notion of zero visibility is not an unscaled
singular value of `V_Z`, but the whitened quantity in (L-14319.10).  A packet
`U_vis` satisfies

\[
 \langle P_Zf,f\rangle\ge\delta^2\|f\|_2^2
 \qquad(f\in U_{\rm vis})
 \tag{L-14319.11}
\]

exactly when its smallest principal-angle cosine with `K_Z` is at least
`delta`.  Applying part 1 with `J=P_Z` gives a complete scalar-dual floor for
the evaluation-visible cone.

This replaces the basis-dependent evaluation SVD in `L-15304` by a canonical
frame metric.  A directed implementation may use rational Loewner enclosures
for `H_Z` and for the compressed matrix in (L-14319.10).

## 3. Closed block formula

Assume now that `G=I` and `J=P_Z` is an orthogonal projection.  Decompose

\[
 H=\mathcal K_Z\oplus\mathcal K_Z^\perp
\]

and write

\[
 A=\begin{pmatrix}B&R^*\\R&C\end{pmatrix}.
 \tag{L-14319.12}
\]

Let `M` be positive on `K_Z^perp` and suppose

\[
 C-\gamma I\succeq hM,
 \qquad h>0.
 \tag{L-14319.13}
\]

Put

\[
 b=
 \lambda_{\min}
 \left(B-h^{-1}R^*M^{-1}R\right).
 \tag{L-14319.14}
\]

For `0<delta2<1`, every vector satisfying

\[
 \|P_Zx\|^2\ge\delta^2\|x\|^2
 \tag{L-14319.15}
\]

obeys

\[
 \boxed{
 \frac{\langle Ax,x\rangle}{\|x\|^2}
 \ge F_{\rm vis}(\gamma,b,\delta^2),}
 \tag{L-14319.16}
\]

where

\[
 \boxed{
 F_{\rm vis}(\gamma,b,\delta^2)
 =\begin{cases}
 b,&b\le\gamma,\\[1mm]
 (1-\delta^2)\gamma+\delta^2b,&b>\gamma.
 \end{cases}}
 \tag{L-14319.17}
\]

### Proof

For `alpha>=0`,

\[
 A_\alpha=A-\alpha(P_Z-\delta^2I)
 =\begin{pmatrix}
 B-\alpha(1-\delta^2)I&R^*\\
 R&C+\alpha\delta^2I
 \end{pmatrix}.
\]

The complement satisfies

\[
 C+\alpha\delta^2I-(\gamma+\alpha\delta^2)I
 =C-\gamma I\succeq hM.
\]

`L-14308` therefore gives

\[
 \inf\sigma(A_\alpha)
 \ge
 \min\{\gamma+\alpha\delta^2,
        b-\alpha(1-\delta^2)\}.
 \tag{L-14319.18}
\]

Part 1 permits optimization over `alpha>=0`.  If `b<=gamma`, the optimum is
`alpha=0` and equals `b`.  If `b>gamma`, the two affine terms meet at
`alpha=b-gamma`, giving (L-14319.17).  QED.

### Interpretation

The visible floor is an exact interpolation between:

- the complete complement floor `gamma`; and
- the Schur-corrected certified-zero representer floor `b`.

When visibility is strong, only the small zero-representer block matters.  The
support-dependent visible packet never has to be diagonalized or followed as a
separate object.

## 4. Positive partial-zero frame in the Weil form

For smooth compactly supported logarithmic test functions, the Weil spectral
formula is

\[
 Q_W(f,g)
 =\sum_{\rho}m_\rho
   \widehat f(z_\rho)
   \overline{\widehat g(\overline{z_\rho})}
 \tag{L-14319.19}
\]

in the declared centered convention.  Every certified critical-line zero
`gamma in Z` contributes the positive rank-one form

\[
 m_\gamma\widehat f(\gamma)
 \overline{\widehat g(\gamma)}.
\]

Hence, with

\[
 J_Z=V_Z^*\operatorname{diag}(m_\gamma)V_Z,
 \qquad
 A_Z^{\rm rem}=A_W-J_Z,
 \tag{L-14319.20}
\]

one has the exact form decomposition

\[
 \boxed{A_W=J_Z+A_Z^{\rm rem}.}
 \tag{L-14319.21}
\]

Therefore, on any finite packet with metric `G`, the two rational Loewner gates

\[
 J_Z\succeq\sigma_Z^2G,
 \qquad
 A_Z^{\rm rem}\succeq-\varepsilon_ZG
 \tag{L-14319.22}
\]

imply

\[
 \boxed{A_W\succeq(\sigma_Z^2-\varepsilon_Z)G.}
 \tag{L-14319.23}
\]

This is the direct positive-frame form of the theorem.  The certified zeros are
not merely an obstruction to radical approximation: they are an explicitly
positive finite part of the Weil quadratic form.  `L-14318` and `L-14308` can be
applied to the residual operator in (L-14319.20).

No assumption is made about unverified zeros.  They remain inside the exact
residual form and must be covered by its directed lower bound.

## 5. Robust rational certificate

Suppose rational symmetric midpoint matrices `A0,J0,G` and nonnegative rational
numbers `eps_A,eps_J` satisfy the external relative Loewner enclosures

\[
 A_0-\varepsilon_AG\preceq A\preceq A_0+\varepsilon_AG,
 \tag{L-14319.24}
\]

\[
 J_0-\varepsilon_JG\preceq J\preceq J_0+\varepsilon_JG.
 \tag{L-14319.25}
\]

For rational `alpha>=0` and a claimed floor `F`, it is sufficient to certify

\[
 \boxed{
 A_0-\alpha(J_0-\delta^2G)
 -(\varepsilon_A+\alpha\varepsilon_J)G
 -FG\succeq0.}
 \tag{L-14319.26}
\]

A robust Slater vector is certified by

\[
 x_0^{\mathsf T}
 [J_0-(\delta^2+\varepsilon_J)G]x_0>0.
 \tag{L-14319.27}
\]

Every predicate is rational after the upstream zero-evaluation and form
matrices have been outward enclosed.  `X-14312` checks this exact trust boundary.

## Relationship to the current main blocker

The previous architecture was

```text
complete low packet
 -> zero-evaluation near-kernel R
    + evaluation-visible block V
 -> radical repair on R
 -> direct matrix lower bound on V.
```

The last line is replaced by

```text
V lies in one whitened evaluation cone
 -> one scalar alpha
 -> one penalized zero-kernel Schur matrix
 -> exact visible floor.
```

Together with `L-15606`, which reduces the unmatched dimension to the plunge
region, the only remaining finite block is the certified-zero representer block
plus any directions that fail a directed visibility threshold.  Its dimension
is controlled by the number of selected zeros, not by the full multiband rank.

## Exact synthetic separation

Take

\[
 A=\begin{pmatrix}2&0\\0&-1\end{pmatrix},
 \qquad
 J=\begin{pmatrix}1&0\\0&0\end{pmatrix},
 \qquad
 G=I,
 \qquad
 \delta^2=\frac34.
\]

The unrestricted form has minimum `-1`.  On the visible cone
`x_1^2>=3(x_1^2+x_2^2)/4`, however,

\[
 \frac{x^TAx}{\|x\|^2}
 =-1+3\frac{x_1^2}{\|x\|^2}
 \ge\frac54.
\]

The exact multiplier is `alpha=3`, since

\[
 A-3(J-\tfrac34I)=\frac54I.
\]

Thus a globally indefinite block has a strictly positive certified visible
floor.  This is the retained `X-14312` control.

## Gap audit

- The S-lemma identity requires a strict visible point.  Without Slater,
  (L-14319.5) remains sufficient but completeness is not asserted.
- Certified-zero ordinates, multiplicities, Fourier convention, and support must
  be provenance-bound.
- A floating evaluation SVD is not a frame certificate; use (L-14319.10) and
  directed Gram bounds.
- The de Branges/Clark interpretation of the complete zero set is motivational;
  the finite theorem uses only independently certified real zeros.
- Subtracting certified positive zero terms makes the residual lower-bound task
  harder, not automatic.  Every omitted or nonreal zero remains in the residual.
- The theorem removes the arbitrary visible-block basis.  It does not by itself
  prove the cofinal residual floor or RH.

## Immediate proof-producing handoff

At a retained support:

1. choose a proof-grade finite critical-line zero set `Z`;
2. build directed Gram bounds for its restricted exponentials;
3. whiten the evaluation map and freeze a rational `delta2`;
4. assemble the zero-representer block and its Schur correction;
5. certify `gamma`, `b`, and the interpolation floor (L-14319.17);
6. compare it with the direct partial-zero-frame floor (L-14319.23);
7. enlarge `Z` only when its directed frame gain exceeds the added conditioning
   and residual costs.

The decisive cofinal target is no longer an arbitrary visible matrix.  It is a
scalar balance among zero-frame strength, residual lower floor, and the
certified-zero representer Schur block.
