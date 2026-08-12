# Suzuki amplitude embedding, scalar-core refutation and corrected tangent frontier — 2026-08-12

## Freeze

```text
repository:       gfreund123/riemann
live main:        b837c12199dd407116f604ce6c938039d1a76da4
working branch:   research/gpt56-pro/91028-levy-fock-hardy-completion
parent PR:        #400
RH status:        unproved
```

## Executive result

The requested component

```text
explicitly embed the prime Poisson-Fock output
into the completed two-sided Hardy reserve
```

contains two mathematically distinct tasks.

1. **Amplitude transport.**  Complete the positive generalized-Jordan source by
the gamma and pole factors and realize the completed xi scattering ratio as a
positive-metric two-sided Hardy operator.
2. **Tangent transport.**  Differentiate that scattering family in the
normalized radial direction and prove positivity of the resulting
Wigner--Smith/screw curvature.

The first task was already solved, in a form that exactly matches the
repository's source, by Suzuki's multiplicative Hankel operator.  This session
imports and identifies that operator explicitly.

The second task is the actual RH-bearing component.  It does not follow from
amplitude unitarity.  This session:

- finds and proves an exact flaw in the previous scalar fixed-scale form-core
  theorem;
- repairs the density problem by an energy-preserving delay fibre;
- proves that a source-linear positive construction must reduce from full
  Poisson Fock space to the compensated first chaos;
- factors the normalized generalized-Jordan radial curvature as an explicit
  positive one-particle Gram;
- rewrites the remaining tangent lift as a positive commutator for Suzuki's
  unitary involution;
- states the corrected CDFHTI theorem.

No positive factorization of that final commutator is proved.  RH remains
unproved.

## I. Exact scalar-core refutation

The causal rational spectral factor has Laplace transfer

\[
 P(s)=\sqrt{378}
 \frac{s(s+\sqrt\alpha)(s+\sqrt\beta)}
 {(s+1)^2(s+2)^2(s+4)^2},
\]

where

\[
 \alpha=\frac{163-5\sqrt{561}}{28},
 \qquad
 \beta=\frac{163+5\sqrt{561}}{28}.
\]

Exact partial fractions give the causal impulse

\[
 \psi(t)=-Ae^{-t}+Bte^{-t}+Cte^{-2t}+Ae^{-4t}+Dte^{-4t}
\]

with algebraic `A,B,C,D` recorded in `R-91008`.

Directed intervals prove

\[
 \psi(31/20)>0,
 \qquad
 \psi(8/5)<0,
\]

and hence a zero

\[
 \tau_0=1.5698664803365582563\ldots .
\]

For the weighted causal space, the nonzero vector

\[
 h_0(t)=e^{-\eta t}\mathbf1_{(\tau_0/a,\infty)}(t)
\]

is orthogonal to every carrier derivative.  Its derivative is a Dirac mass at
a zero of the mother.  This is the distributional solution missed by the
claim that `H' psi=0` and `psi` nonzero almost everywhere force `H'=0`.

Therefore `L-91032` is false and `T-91007` is blocked.

## II. Delay-fibre repair

For any positive probability density `w`, define

\[
 (\mathcal J_wF)(u,\tau)
 =\sqrt{w(\tau)}e^{-iu\tau}F(u).
\]

This is an isometry and preserves the scalar residual density exactly.
Physically it replaces one mother by all of its positive delays.

The vector-valued pointwise energy is

\[
 E_{a,w}(t)=\int_0^tw(\tau)|\psi_a(t-\tau)|^2d\tau>0
 \qquad(t>0).
\]

Hence there is no common physical zero.  The repaired delayed causal family
has only the true half-line integral defect; reflection gives the other
half-line; one bridge fills their difference inside global mean zero.

This yields the corrected proposed fixed-scale form core `L-91034`.

## III. Suzuki closes the amplitude embedding

Suzuki uses

\[
 c_a(n)=n^a\prod_{p\mid n}(1-p^{-2a})=n^aq_a(n),
\]

exactly the repository generalized-Jordan coefficients.  With his explicit
gamma kernel `g_a`, define

\[
 h_a(x)=x^{-1}\sum_{n\le x}c_a(n)g_a(n/x).
\]

The shifted Mellin transform is

\[
 \Theta_a(z)=
 \frac{\xi(1/2-a-iz)}{\xi(1/2+a-iz)}.
\]

The multiplicative Hankel operator

\[
 (\mathsf H_af)(x)=\int_0^\infty h_a(xy)f(y)dy
\]

is a positive-metric isometry in the unconditional safe range, and

\[
 \mathcal M_{1/2}\mathsf H_a
 =M_{\Theta_a}\mathsf R\mathcal M_{1/2}.
\]

Functional symmetry makes it a unitary involution.  Thus the completed
amplitude-level map is explicit:

```text
positive generalized-Jordan coefficients
+ explicit gamma/pole kernel
-> multiplicative Hankel unitary
-> two-sided Hardy reflection with multiplier Theta_a.
```

This is `L-91035`.

## IV. Why the amplitude is not the proof

For the inner control

\[
 \Theta_a(z)=e^{ia^2z},
\]

the boundary phase delay is positive, but the normalized radial soft curvature
is

\[
 -a^3/4<0.
\]

More generally, differentiating a unitary path gives a self-adjoint tangent
generator with no sign.  PR #398 supplies a stronger zeta-shaped control that
retains symmetry, cocycle and safe Jordan positivity while its target Pick
matrix is indefinite.

Therefore Suzuki's amplitude isometry cannot be differentiated and declared
positive without a new theorem.  This is `R-91009`.

## V. Higher Fock chaos cannot repair a linear target

Under intensity scaling `r nu`, a positive product-system-compatible output
kernel has the orthogonal chaos expansion

\[
 K_r=\sum_{m\ge1}r^mK_m,
 \qquad K_m\succeq0.
\]

The explicit formula target is linear in the source intensity.  If

\[
 K_r=rK_1
\]

for every `r`, positivity forces

\[
 K_m=0\qquad(m\ge2).
\]

Thus the full Poisson Fock space is the correct dilation, but the actual
conclusion-producing map must act on the compensated first chaos.  This is
`L-91036`.

## VI. The exact positive source tangent

The normalized Jordan radial curvature is

\[
 \mathscr C_a^{\rm J}(z)
 =-\partial_a[a^{-1}\log Q_a(z)].
\]

Its Euler coefficients are

\[
 \frac{1-(1+2a\log n)n^{-2a}}{ka^2}>0
 \qquad(n=p^k).
\]

It has the one-particle Gram factor

\[
 w_{a,s}(r,n)
 =\frac2a\sqrt{r\Lambda(n)\log n}\,n^{-s-r},
 \qquad 0<r<a,
\]

with

\[
 \mathscr C_a^{\rm J}(s+\bar t)
 =\langle w_{a,s},w_{a,t}\rangle.
\]

Thus the safe normalized-curvature source is already a complete positive
first-chaos kernel, not an unknown arithmetic sign.  This is `L-91037`.

## VII. Positive-commutator endpoint

For Suzuki's boundary multiplier define

\[
 B_a(x)=-i\partial_a[a^{-1}\log\Theta_a(x)].
\]

The Cauchy soft count is

\[
 \mathcal N_x(a)=-\frac{a^3}{4}B_a'(x).
\]

In Mellin coordinates Suzuki's unitary involution is

\[
 \mathsf S_a=M_{\Theta_a}\mathsf R.
\]

Its normalized tangent is multiplication by `B_a`.  With

\[
 \mathsf P=-i\partial_x,
\]

one gets

\[
 \boxed{
 M_{\mathcal N_x(a)}
 =-\frac{a^3}{4}i[\mathsf P,M_{B_a}].
 }
\]

The final theorem is therefore a positive-commutator factorization of the
normalized tangent of an explicit unitary scattering operator.  This is
`L-91038`.

## VIII. Corrected final theorem

`T-91008` states CDFHTI:

\[
 \mathcal C_{a_0}:
 \mathfrak g_{a_0}^{\Gamma,\mathrm{pole}}
 \oplus L^2(\omega_{a_0,c})
 \longrightarrow
 \mathcal H_{a_0}^{\rm delayed\ Hardy}
 \oplus\mathfrak e_{a_0}
\]

must be a source-ordered isometry whose defect kernel is the complete delayed
screw Gram.

If constructed, it proves RH by the repaired form-core theorem and Suzuki's
screw criterion.  Under RH an existential Kolmogorov factorization exists; the
open problem is the explicit source construction.

## IX. Verification

The retained finite replay returns

```text
PASS_CORRECTED_FOCK_HARDY_COMPLETION
```

with controls including

```text
causal root                         1.5698664803365583
partial-fraction maximum error      6.33e-81
hidden-jump quadrature maximum      1.48e-60
delay-isometry maximum error        1.06e-81
minimum sampled delay energy        8.03e-06
```

The interval signs and endpoint calculation prove the scalar-core refutation.
The remaining computations are finite diagnostics.

## Exact status

```text
Claude finite Gabor proportion theorem                 UPSTREAM PROVED
scalar one-fixed-scale form core                       REFUTED EXACTLY
energy-preserving delay-fibre repair                   PROPOSED COMPLETE
Suzuki amplitude-level completed embedding             IMPORTED PROVED
full Fock dilation                                     EXACT
source-linear target -> first-chaos reduction          PROPOSED COMPLETE
normalized Jordan curvature first-chaos                EXACT
amplitude unitarity -> tangent sign                     REFUTED
Suzuki tangent = positive-commutator target             EXACT REDUCTION
CDFHTI explicit positive tangent factorization          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```
