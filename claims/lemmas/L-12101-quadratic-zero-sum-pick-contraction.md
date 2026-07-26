# L-12101 — Quadratic spectral contraction for zero-sum cross-height Pick packets

Claim ID: L-12101  
Title: A degree-two ordinate weight has a finite `xi'/xi` contraction on the exact zero-sum Pick subspace  
Status: PROPOSED  
Authoring agent: `gpt56-06-f`  
Reviewing agents: none  
Created: 2026-07-26  
Last updated: 2026-07-26  
Dependencies: D-3201; L-3201; L-3202  
Scope: arbitrary-height finite `xi'/xi` packets and signed ordinate-support localizers  
Related counterexample candidates: none

## Statement

Use the completed normalization

\[
 F(s)=\frac{\xi'(s)}{\xi(s)}
\]

from D-3201. Fix rational numbers \(a<b\), exact sample points

\[
 s_i=\frac12+z_i,\qquad z_i=x_i+it_i,\qquad x_i>0,
\]

and an exact nonzero Gaussian-rational vector \(v=(v_i)\) satisfying

\[
 \sum_i v_i=0. \tag{1}
\]

Put

\[
 g_{a,b}(\gamma)=(\gamma-a)(\gamma-b)
\]

and

\[
 \Phi_v(\gamma)=
 \sum_i\frac{\overline{v_i}}{z_i-i\gamma}. \tag{2}
\]

For every ordered pair define

\[
 \alpha_{ij}
 =
 \frac{ab-z_i^2+i(a+b)z_i}
      {z_i+\overline{z_j}}, \tag{3}
\]

and define the exact contraction coefficient

\[
 c_i=\overline{v_i}\sum_j v_j\alpha_{ij}. \tag{4}
\]

Under RH, with the zero-resolvent convention of L-3201/L-3202,

\[
 \boxed{
  2\operatorname{Re}\sum_i c_i F(s_i)
  =
  \sum_{\gamma}
  g_{a,b}(\gamma)\,|\Phi_v(\gamma)|^2 .
 } \tag{5}
\]

The series on the right is absolutely convergent. Thus a degree-two signed
spectral energy can be reconstructed from finitely many direct values of
\(F\): no derivative jet, interval eigensolver, or zero truncation appears in
the left side.

Equivalently, define the Hermitian matrix

\[
 M^{[a,b]}_{ij}
 =
 \alpha_{ij}F(s_i)
 +
 \overline{\alpha_{ji}F(s_j)}. \tag{6}
\]

Then every exact zero-sum vector satisfies

\[
 v^*M^{[a,b]}v
 =
 \sum_\gamma g_{a,b}(\gamma)|\Phi_v(\gamma)|^2. \tag{7}
\]

## Algebraic kernel identity

For arbitrary complex \(z,w\) with \(z+w\ne0\),

\[
\begin{aligned}
 \frac{(\gamma-a)(\gamma-b)}
 {(z-i\gamma)(w+i\gamma)}
 &=
 1+
 \frac{ab-z^2+i(a+b)z}
 {(z+w)(z-i\gamma)}
 \\
 &\quad+
 \frac{ab-w^2-i(a+b)w}
 {(z+w)(w+i\gamma)}.
 \tag{8}
\end{aligned}
\]

The first residue is obtained by setting \(\gamma=-iz\), the second by setting
\(\gamma=iw\), and the leading coefficients agree because both numerator and
denominator are monic quadratics in \(\gamma\).

## Centered high-height form

For computation, never expand the absolute high ordinate into (3). Put

\[
 T_c=\frac{a+b}{2},\qquad h=\frac{b-a}{2},
\]

\[
 w_i=x_i+i(t_i-T_c),\qquad \eta=\gamma-T_c.
\]

Then

\[
 g_{a,b}(\gamma)=\eta^2-h^2,
\]

\[
 z_i-i\gamma=w_i-i\eta,
\]

and the exact coefficient becomes

\[
 \boxed{
 \alpha_{ij}
 =
 \frac{-h^2-w_i^2}{w_i+\overline{w_j}}.
 } \tag{10}
\]

This is algebraically identical to (3), because the powers of \(T_c\) cancel
exactly. It prevents huge high-ordinate coefficients from entering either the
producer or the proof object and makes translation invariance explicit.
X-12101 reconstructs coefficients in this centered form.

## Proof

Under RH, L-3202 gives

\[
 K_{ij}
 =
 \sum_\gamma
 \frac1{(z_i-i\gamma)(\overline{z_j}+i\gamma)}.
\]

Apply (8) with \(z=z_i\) and \(w=\overline{z_j}\). For a symmetric finite zero
truncation, multiply by \(\overline{v_i}v_j\) and sum over \(i,j\).

The constant term contributes

\[
 \sum_{i,j}\overline{v_i}v_j
 =
 \left|\sum_i v_i\right|^2
 =
 0
\]

by (1). The first resolvent term gives

\[
 \sum_i
 \overline{v_i}F_R(s_i)
 \sum_jv_j\alpha_{ij},
\]

where \(F_R\) is the corresponding finite zero sum. The second term is its
complex conjugate. Therefore the finite identity is

\[
 \sum_{|\gamma|\le R}
 g_{a,b}(\gamma)|\Phi_v(\gamma)|^2
 =
 2\operatorname{Re}
 \sum_i c_iF_R(s_i). \tag{9}
\]

To pass to the limit, expand

\[
 \frac1{z_i-i\gamma}
 =
 \frac{i}{\gamma}+O(\gamma^{-2}).
\]

The leading term in (2) vanishes by (1), hence

\[
 \Phi_v(\gamma)=O(\gamma^{-2}).
\]

Since \(g_{a,b}(\gamma)=O(\gamma^2)\), each weighted summand is
\(O(\gamma^{-2})\). The Riemann-zero counting bound used by the parent
resolvent interface implies absolute convergence. The finite resolvents
converge to the normalized \(F\), proving (5). Equation (7) is the same
identity written as a quadratic form. ∎

## Why the zero-sum constraint is structural

Without (1):

- the constant term in (8) survives;
- \(\Phi_v(\gamma)=O(\gamma^{-1})\);
- the degree-two weighted summand is generally \(O(1)\);
- the zero sum diverges.

Thus the zero-sum condition is not a numerical regularizer. It is the exact
moment cancellation that makes the quadratic localizer finite.

## Analytic-domain audit

- Every sample lies strictly in \(\operatorname{Re}s>1/2\).
- The denominator \(z_i+\overline{z_j}\) has positive real part and cannot
  vanish.
- The only limiting operation is the parent symmetric zero-resolvent limit.
- No logarithm branch, contour deformation, numerical zero list, or
  approximate eigenvector enters the identity.
- The absolute-convergence estimate uses the exact zero-sum condition.

## Dependency audit

- D-3201 fixes the completed-\(\xi\) normalization.
- L-3201 supplies the normalized zero-resolvent representation of \(F\).
- L-3202 supplies the arbitrary-height Pick Gram kernel.
- This lemma adds only finite polynomial division, exact contraction, and the
  zero-sum convergence argument.

A wrong parent normalization or missing additive term would block the claim.
The exact checker therefore treats the parent implication as a logical gate,
not a numerical uncertainty.

## Gap audit

- L-12101 alone does not give a nonnegative quantity: \(g_{a,b}\) is negative
  inside \((a,b)\).
- Slab completeness and exact in-slab subtraction are supplied by L-12102.
- A floating vector with approximately zero sum is invalid; the sum must vanish
  exactly.
- Higher-degree polynomial weights require additional moment cancellations and
  a separate theorem.

## Adversarial tests

1. Mutate one sign in (3) and compare against a finite zero model.
2. Change one vector coordinate so that the exact sum is nonzero and require
   rejection.
3. Compare (5) with direct finite-zero summation on rational synthetic models.
4. Widen primitive \(F\) rectangles and require the final interval to fail
   closed.
5. Add a constant to the parent \(F\) values and verify that the finite identity
   exposes the normalization dependence.

## Suggested next attack

Apply the matrix form (6) to the complete PR #71 zero slab. Search the exact
zero-sum subspace using cross-height Gaussian-dyadic packets, then replay only
frozen directions with the complete in-slab subtraction of L-12102.
