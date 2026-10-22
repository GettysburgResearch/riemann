# Exact lift to the original \(K_0\) and theta Gram–commutator factorization

Agent: `gpt56-pro-09-j`  
Date: 2026-08-01  
PR: #202  
Classification: exact transport theorem plus exact theta factorization; no independent RH claim

## Executive result

This pass addressed the requested original-kernel question rather than creating
another scalar RH criterion.

Two exact results were obtained.

1. The normalized mixed/Volterra form pulls back to the original coordinate
   Weyl kernel by parity, a primitive map, one scaling, and multiplication by
   the positive function \(\Phi(s/2)\). There is no endpoint boundary term and
   no quotient repair in this pullback.
2. The original same-sign branch has an exact theta Hankel decomposition into
   one explicit positive Gram and one isolated double commutator, with an
   equivalent multiplicative theta-Volterra form.

Thus the external quotient-to-original lift is closed. Actual positivity of
\(K_0\) follows immediately from a genuinely positive normalized continuum
form. What is not independently established here is the load-bearing continuum
contraction inside the imported normalized certificate.

## 1. Exact pullback

For the parity kernels

\[
P_\varepsilon(x,y)=K_0(x,y)+\varepsilon K_0(x,-y),
\]

put \(H_\varepsilon=\partial_x\partial_yP_\varepsilon\). If

\[
F(u)=\int_0^u f(x)dx,
\]

then two integrations by parts give exactly

\[
Q_{P_\varepsilon}(f,g)=Q_{H_\varepsilon}(F,G).
\]

The lower endpoint vanishes because \(F(0)=0\); infinity vanishes because the
Riemann kernel decays superexponentially. The even-kernel crossing creates no
delta because \(\Phi'(0)=0\).

With

\[
\Psi(s)=\Phi(s/2),
\qquad
\widetilde H_\varepsilon(s,t)=
{H_\varepsilon(s/2,t/2)\over\Psi(s)\Psi(t)},
\]

and

\[
(\mathcal UF)(s)=\frac12\Psi(s)F(s/2),
\]

one has the literal congruence

\[
Q_{H_\varepsilon}(F,G)
=Q_{\widetilde H_\varepsilon}(\mathcal UF,\mathcal UG).
\]

Consequently, positivity of the completed normalized form on these images gives
positivity of both parity kernels and hence of \(K_0\). No density theorem is
needed for this implication, because every original compact test already has an
exact transported image.

## 2. Coordinate factorization

On the same-sign half-line,

\[
K_0(x,y)
=\frac12\int_0^\infty
\left(u+{x+y\over2}\right)
\Phi(x+u)\Phi(y+u)du.
\]

Let \(\mathsf H_\Phi\) be the Hankel operator with kernel
\(\Phi(x+y)\), and let \(X\) be coordinate multiplication. Then

\[
K_0^{++}
=\mathsf H_\Phi X\mathsf H_\Phi
+\frac14[\mathsf H_\Phi,[\mathsf H_\Phi,X]].
\]

The first term is the Gram

\[
\|\sqrt X\,\mathsf H_\Phi f\|^2.
\]

The exact remaining same-sign inequality is therefore

\[
[\mathsf H_\Phi,[\mathsf H_\Phi,X]]
\succeq-4\mathsf H_\Phi X\mathsf H_\Phi.
\]

This is not a generic Hankel statement. Using the explicit theta series, define

\[
G(z)=\pi z^{3/2}\sum_{n\ge1}n^2e^{-\pi n^2z},
\quad
h(z)=-G'(z)>0\quad(z\ge1).
\]

Then \(\Phi(t)=4e^{3t/2}h(e^{2t})\). In multiplicative coordinates the
same kernel is

\[
K_0^{++}(X,Y)
=2(XY)^{3/4}\int_1^\infty
R^{1/2}\log(R\sqrt{XY})h(XR)h(YR)dR.
\]

Writing \(a_X(R)=X^{3/4}R^{1/4}h(XR)\) and using the associated
Volterra map \(\mathcal T\), one gets

\[
K_0^{++}
=2\mathcal T^*L_R\mathcal T
+\{L_X,\mathcal T^*\mathcal T\}.
\]

The first term is positive. The exact theta-specific residual is

\[
\{L_X,\mathcal T^*\mathcal T\}
\succeq-2\mathcal T^*L_R\mathcal T.
\]

This gives a direct coordinate interpretation of what the normalized Volterra
contraction must prove.

## 3. What is now closed

The following chain is exact:

```text
positive normalized mixed/Volterra form
    -> primitive congruence with no boundary term
    -> positive original parity kernels
    -> K0 >= 0
    -> L_Xi >= 0 by L-19812.
```

The quotient-to-original Weyl transport is therefore no longer an external
normalization gap.

## 4. Smallest remaining obstruction

The pass did not independently establish the normalized continuum positivity
premise. In the signed Volterra feature notation, it is the actual-metric
contraction

\[
\boxed{\|CKE\|\le1}
\]

on the completed Green-minimizer trace image, including endpoint continuity and
both parity branches. Pointwise \(|\kappa|\le1\) before Volterra integration is
not, by itself, this operator inequality.

Equivalently in original theta coordinates, the same-sign part is the
commutator inequality above, while the mixed primitive form must also control
the reflected parity block.

If the imported normalized certificate is independently verified to include
this completed-domain contraction, `T-19806` now promotes it immediately to
actual positivity of \(K_0\), and `L-19812` promotes that to the Pick/Loewner
conclusion.

## 5. Files

- `claims/theorems/T-19806-exact-volterra-quotient-to-K0-lift.md`
- `claims/lemmas/L-19814-theta-hankel-gram-commutator.md`

No proof of the internal contraction, and therefore no unconditional proof of
RH, is claimed in this report.