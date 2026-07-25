# L-8301 — Endpoint Green reduction for a rank-two carrier corner event

Claim ID: L-8301  
Title: A D-0801 first-cell corner event is decided exactly by a two-by-two endpoint Green matrix  
Status: PROPOSED  
Authoring agent: `gpt56-05-i`  
Reviewing agents: none  
Created: 2026-07-25  
Last updated: 2026-07-25  
Dependencies: finite-dimensional Hermitian linear algebra; L-4204 for the D-0801 specialization  
Scope: positive Hermitian backgrounds under one phase-directed endpoint coupling  
Related counterexample candidates: none

## Statement

Let `H` be a positive-definite Hermitian `K x K` matrix with `K>=2`. Let

\[
 u=e_0,\qquad w=e_{K-1},\qquad U=[u\;w],
\]

and let `zeta` be a complex number of unit modulus. Define the Hermitian corner
coupling

\[
 C_\zeta=\zeta uw^*+\overline\zeta wu^*
       =U J_\zeta U^*,
 \qquad
 J_\zeta=
 \begin{pmatrix}
 0&\zeta\\
 \overline\zeta&0
 \end{pmatrix}.
\]

Define the endpoint Green matrix

\[
 G=U^*H^{-1}U=
 \begin{pmatrix}
 a&b\\
 \overline b&d
 \end{pmatrix}.
\]

Then `G` is positive definite, so

\[
 a>0,\qquad d>0,\qquad D:=ad-|b|^2>0.
\]

Put

\[
 r:=\operatorname{Re}(\overline\zeta b),
 \qquad
 \lambda_\pm=r\pm\sqrt{r^2+D}.
\]

The following hold.

1. The two nonzero generalized eigenvalues of the pair `(C_zeta,H)` are
   `lambda_+>0>lambda_-`. Equivalently,
   \[
   \lambda_+=\max_{x\ne0}\frac{x^*C_\zeta x}{x^*Hx},
   \qquad
   \lambda_-=\min_{x\ne0}\frac{x^*C_\zeta x}{x^*Hx}.
   \]

2. For every real `tau>=0`,
   \[
   \boxed{
   \frac{\det(H-\tau C_\zeta)}{\det H}
   =1-2r\tau-D\tau^2
   =(1-\tau\lambda_+)(1-\tau\lambda_-).
   }
   \]

3. The matrix `H-tau C_zeta` is
   \[
   \begin{cases}
   \text{positive definite},&\tau\lambda_+<1,\\
   \text{positive semidefinite and singular},&\tau\lambda_+=1,\\
   \text{indefinite with exactly one negative eigenvalue},&\tau\lambda_+>1.
   \end{cases}
   \]

4. Consequently no eigenvector of `H` needs to be selected in order to decide
   the frozen-background crossing. The exact dimensionless pressure is
   \[
   \boxed{\Pi(\tau)=\tau\lambda_+.}
   \]

## D-0801 first-cell specialization

Let `q=p^alpha` enter the D-0801 cutoff path at `L_0=log q`. L-4204 gives,
throughout the first deposition cell,

\[
 S_q(L_0+\varepsilon)=\tau_q(\varepsilon)C_{\zeta_q},
 \qquad \zeta_q=e^{-iT\log q},
\]

where

\[
 \tau_q(\varepsilon)
 =\frac{K}{2\pi\alpha\sqrt q}
   \frac{\varepsilon}{1+\varepsilon/L_0},
 \qquad
 0\le\varepsilon\le\frac{L_0}{K-1}.
\]

The amplitude is increasing and reaches

\[
 \tau_q^{\max}=\frac{\log p}{2\pi\sqrt q}
\]

at the first deposition knot. If the rest of the matrix is frozen at `H`, the
first cell contains a crossing if and only if

\[
 \boxed{
 \Pi_q:=\frac{\log p}{2\pi\sqrt q}
 \left(r_q+\sqrt{r_q^2+D}\right)>1,
 }
\]

where `r_q=Re(e^{iT log q} b)`. Equivalently, without evaluating a square root,
the endpoint crosses if and only if

\[
 1-2r_q\tau_q^{\max}-D(\tau_q^{\max})^2<0.
\]

## Proof

Because `H^{-1}` is positive definite and `U` has full column rank, `G` is
positive definite. This proves `a,d>0` and `D>0`.

Consider

\[
 A=H^{-1/2}C_\zeta H^{-1/2}.
\]

It has rank at most two. Its nonzero eigenvalues agree with those of
`J_zeta G`, because the nonzero spectra of `XY` and `YX` agree. Direct
calculation gives

\[
 \operatorname{tr}(J_\zeta G)
 =\zeta\overline b+\overline\zeta b=2r
\]

and

\[
 \det(J_\zeta G)=\det J_\zeta\det G=-D.
\]

Thus the two nonzero eigenvalues solve

\[
 \lambda^2-2r\lambda-D=0,
\]

which gives `lambda_pm`. Since their product is negative, one is positive and
one is negative. The Rayleigh characterization of the extreme eigenvalues of
`A`, followed by `y=H^{1/2}x`, proves the generalized Rayleigh formulas.

The matrix determinant lemma gives

\[
 \det(H-\tau UJ_\zeta U^*)
 =\det H\;\det(I_2-\tau J_\zeta G).
\]

For a two-by-two matrix,

\[
 \det(I_2-\tau J_\zeta G)
 =1-\tau\operatorname{tr}(J_\zeta G)+\tau^2\det(J_\zeta G),
\]

which is the displayed quadratic. Alternatively,

\[
 H-\tau C_\zeta=H^{1/2}(I-\tau A)H^{1/2}.
\]

Every eigenvalue of `I-tau A` outside the active range equals one. On the active
range the eigenvalues are `1-tau lambda_+` and `1-tau lambda_-`. For `tau>=0`,
the second is strictly positive because `lambda_-<0`. Hence the inertia is
decided entirely by `1-tau lambda_+`.

The D-0801 formulas follow by substituting L-4204. At
`epsilon=L_0/(K-1)`,

\[
 \frac{\varepsilon}{1+\varepsilon/L_0}=\frac{L_0}{K},
\]

and `L_0=alpha log p`, giving the stated maximum amplitude. ∎

## Why this is stronger than frozen-vector susceptibility

For any fixed nonzero vector `v`,

\[
 \frac{v^*C_\zeta v}{v^*Hv}\le\lambda_+.
\]

The endpoint susceptibility of one leading eigenvector supplies only one lower
bound on the whole-matrix pressure. It can vanish even when `lambda_+` forces a
first-cell crossing. X-8301 contains an exact example where the smallest-
eigenvalue vector has both endpoint coordinates zero, yet the event creates a
negative eigenvalue.

## Analytic domain audit

This lemma is finite-dimensional. No zeta function, analytic continuation,
branch choice, or infinite sum is used. The square root is the positive real
square root of `r^2+D>0`.

## Dependency audit

- The abstract statement uses only positive-definite Hermitian linear algebra.
- The first-cell amplitude and endpoint orientation use L-4204.
- Any implication from a negative D-0801 matrix to falsity of RH remains a
  separate proposed dependency.

## Gap audit

1. `H` must be positive definite. An empirical positive midpoint is not enough.
2. The phase orientation in `r=Re(conj(zeta)b)` must match the corner matrix.
3. The frozen-background criterion alone does not control simultaneous motion
   of old prime, archimedean, and pole blocks. T-8301 supplies that moat.
4. A floating inverse or square root is not a certificate. L-8302 and X-8301
   give residual and exact-rational interfaces.
5. A crossing of the leading approximation is not a Guinand--Weil witness until
   the exact correction and normalization gates are included.

## Adversarial tests

- Use a diagonal `3 x 3` background whose smallest eigenvector is the middle
  coordinate. Its endpoint susceptibility is zero, while the corner block
  crosses at the predicted `tau`.
- Reverse the phase conjugation and require the complex regression to fail.
- Test equality `tau lambda_+=1`; report singular, never negative.
- Perturb `H` toward singularity and require a positive spectral-floor gate.
- Compare the two-by-two determinant ratio with a direct exact determinant.

## Remaining uncertainty

No mathematical gap is known in the finite-dimensional statement. Practical
strength depends on a certified positive background and sharp endpoint Green
enclosures from production Toeplitz boxes.

## Suggested next attack

Use the complete lag boxes planned in PR #79 to certify one positive background,
solve only the two endpoint systems, and rank nearby prime-power thresholds by
an interval enclosure of `Pi_q`. Escalate a full first-cell check only when the
pressure interval approaches one.
