# L-91023 — The positive generalized-Jordan source is exactly the zeta factor of the radial xi scattering matrix

Claim ID: `L-91023`  
Status: **PROPOSED COMPLETE EXACT SOURCE/SCATTERING BOUNDARY IDENTITY — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91014`; the functional equation and conjugation symmetry of `xi`; the Cauchy soft count  
RH status: **unproved**

## 1. Completed radial scattering ratio

For `a>0` and real `x`, put

\[
 s_\pm=\frac12\pm a+ix
\]

and define

\[
 \boxed{
 \Theta_a(x)=\frac{\xi(s_-)}{\xi(s_+)}.
 }
 \tag{L-91023.1}
\]

The functional equation and real conjugation give

\[
 \xi(s_-)=\xi(1-s_-)=\xi(\overline{s_+})
 =\overline{\xi(s_+)}.
 \tag{L-91023.2}
\]

Hence, wherever the denominator is nonzero,

\[
 \boxed{|\Theta_a(x)|=1.}
 \tag{L-91023.3}
\]

Thus `Theta_a` is the exact scalar all-pass scattering ratio between the two
lines symmetric about the critical line.  An off-line zero of depth `a` and
ordinate `x` is exactly a real-axis pole of this scattering ratio.

## 2. Exact factorisation through the positive Jordan source

Let

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}.
\]

Then

\[
 \boxed{
 \Theta_a(x)=\Gamma_a(x)Q_a(s_-),
 }
 \tag{L-91023.4}
\]

where the explicit archimedean/pole factor is

\[
 \boxed{
 \Gamma_a(x)
 =\pi^a
 \frac{s_-(s_--1)}{s_+(s_+-1)}
 \frac{\Gamma(s_-/2)}{\Gamma(s_+/2)}.
 }
 \tag{L-91023.5}
\]

Thus the coefficientwise-positive generalized-Jordan Dirichlet series of
`L-91014` is not an auxiliary source chosen by analogy: its analytic
continuation to `s_-` is exactly the zeta component of the completed radial
scattering matrix.

The equality

\[
 |\Gamma_a(x)Q_a(s_-)|=1
 \tag{L-91023.6}
\]

is the completed source/scattering boundary condition.

## 3. Wigner--Smith delay

Put

\[
 L(s)=\frac{\xi'}{\xi}(s),
 \qquad p_x(a)=\Re L(s_+).
\]

Differentiating (L-91023.1) along the carrier gives

\[
 \frac{\partial_x\Theta_a(x)}{\Theta_a(x)}
 =-2i\,p_x(a).
 \tag{L-91023.7}
\]

Therefore the scalar Wigner--Smith delay is

\[
 \boxed{
 \mathcal T_a(x)
 =i\Theta_a(x)^{-1}\partial_x\Theta_a(x)
 =2p_x(a).
 }
 \tag{L-91023.8}
\]

The completed Cauchy soft count becomes

\[
 \boxed{
 \mathcal N_x(a)
 =\frac14\left[
  a\mathcal T_a(x)-a^2\partial_a\mathcal T_a(x)
 \right].
 }
 \tag{L-91023.9}
\]

Hence the dyadic Cauchy gate is exactly a scale finite difference of the
Wigner--Smith delay of the completed Jordan scattering ratio.

## 4. Prime/gamma splitting is exact

Taking logarithmic carrier derivatives in (L-91023.4) gives

\[
 \mathcal T_a(x)
 =i\partial_x\log\Gamma_a(x)
  +i\partial_x\log Q_a(s_-).
 \tag{L-91023.10}
\]

The first term is the completed gamma/pole reserve.  The second is the
analytically continued positive-source phase.  Thus the familiar

```text
archimedean reserve - prime interaction
```

splitting is exactly the phase-delay splitting of one completed unitary
scattering matrix, not a post hoc rearrangement of the explicit formula.

## 5. Cocycle as radial propagation

The generalized-Jordan cocycle gives

\[
 Q_{a+b}(s_x-a-b)
 =Q_a(s_x-a-b)Q_b(s_x+a-b).
 \tag{L-91023.11}
\]

After multiplication by the corresponding explicit `Gamma` factors, this is
the exact radial propagation from the line `1/2-a-b` to `1/2+a+b` through the
intermediate line `1/2+a-b`.  The coefficient-one divisor isometry of
`L-91014` is therefore a Hilbert-space realization of the zeta part of radial
scattering composition.

## 6. Relation to the sixteenfold recurrence

The normalized gate of `T-91005` can be written entirely in terms of the
scattering delay:

\[
\begin{aligned}
 \mathcal E_x(a)
 =\frac1{4a^4}\Bigg\{&
 2a\mathcal T_{2a}(x)-4a^2\partial_a\mathcal T_{2a}(x)\\
 &-a\mathcal T_a(x)+a^2\partial_a\mathcal T_a(x)
 \Bigg\},
\end{aligned}
 \tag{L-91023.12}
\]

with the derivative in the first term interpreted with respect to its scale
argument.  Thus the coefficient-one recurrence is a monotonicity law for a
renormalized scattering-delay curvature.

## 7. What this closes

The earlier source/scattering programme had one conceptual interface left:
why the coefficientwise-positive generalized-Jordan cocycle should be the
correct source for the Cauchy/xi gate.  Equations (L-91023.4) and
(L-91023.8) close that interface exactly:

```text
positive Jordan source
 -> analytic radial continuation
 -> completed unitary xi scattering ratio
 -> Wigner--Smith delay
 -> Cauchy soft count and dyadic gate.
```

## 8. Boundary

Closed:

```text
completed radial xi all-pass ratio;
exact factorisation into explicit gamma factor times positive Jordan source;
exact Wigner--Smith identity;
exact source/gamma phase-delay split;
radial cocycle interpretation;
identification of the Cauchy gate as scattering-delay curvature.
```

Open:

```text
positivity/monotonicity of the renormalized delay curvature;
prime-side three-port residual positivity;
RH.
```
