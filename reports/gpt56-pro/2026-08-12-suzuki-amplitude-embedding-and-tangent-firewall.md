# Suzuki amplitude embedding, scalar-core refutation and corrected full-Gram frontier — 2026-08-12

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

splits into three distinct levels.

1. **Amplitude transport.** Complete the positive generalized-Jordan source by
   the gamma and pole factors and realize the completed xi scattering ratio as
   a positive-metric two-sided Hardy operator.
2. **Scalar tangent transport.** Differentiate the scattering family in the
   normalized radial direction and recover the scalar Cauchy soft count.
3. **Full Gram transport.** Preserve every carrier, delay, Hardy-orientation and
   bridge cross term, obtaining the complete screw/Weil matrix kernel.

The first level was already solved, for exactly the repository's Jordan
coefficients, by Suzuki's multiplicative Hankel operator.  This session imports
and identifies it explicitly.

The second level has an exact Wigner--Smith commutator identity, but
`R-91009` shows that amplitude unitarity does not sign it.

The third level is the actual RH-bearing component.  `R-91010` proves that the
scalar commutator is not its polarization.  No full positive source-to-output
factorization is proved.

The session also:

- proves an exact flaw in the previous scalar fixed-scale form-core theorem;
- repairs the density problem by an energy-preserving delay fibre;
- reduces every natural source-linear Poisson construction to compensated
  first chaos;
- factors the normalized generalized-Jordan radial curvature as an explicit
  positive one-particle Gram;
- imports Suzuki's June 2026 localized Weil-operator theorem, which confirms
  that the unshifted lowest-eigenvalue sign is exactly the remaining gate;
- states the corrected CDFHGI full-Gram theorem.

RH remains unproved.

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

Exact partial fractions give

\[
 \psi(t)=-Ae^{-t}+Bte^{-t}+Cte^{-2t}+Ae^{-4t}+Dte^{-4t}
\]

with algebraic `A,B,C,D` in `R-91008`.  Directed intervals prove

\[
 \psi(31/20)>0,
 \qquad
 \psi(8/5)<0,
\]

and hence

\[
 \tau_0=1.5698664803365582563\ldots .
\]

The nonzero weighted step

\[
 h_0(t)=e^{-\eta t}\mathbf1_{(\tau_0/a,\infty)}(t)
\]

is orthogonal to every scalar carrier derivative.  Its derivative is a Dirac
mass at a zero of the mother.  This is the distributional solution missed by
the implication

```text
H' psi=0 and psi nonzero almost everywhere -> H'=0.
```

Therefore `L-91032` is false and `T-91007` is blocked.

## II. Delay-fibre repair

For any positive probability density `w`, define

\[
 (\mathcal J_wF)(u,\tau)
 =\sqrt{w(\tau)}e^{-iu\tau}F(u).
\]

This is an isometry and preserves the scalar residual density exactly.  Its
physical vector-valued energy is

\[
 E_{a,w}(t)=\int_0^tw(\tau)|\psi_a(t-\tau)|^2d\tau>0
 \qquad(t>0).
\]

Hence no common physical zero survives.  The delayed causal family has only
the true positive-half-line integral defect, the reflected family has the
negative-half-line defect, and one bridge fills their difference in the global
mean-zero space.  This is the proposed repaired form core `L-91034`.

## III. Suzuki closes the amplitude embedding

Suzuki's coefficients are

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

is a positive-metric isometry in the unconditional safe range and

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

This is imported as `L-91035`.

## IV. Why amplitude unitarity is not the sign

For the inner control

\[
 \Theta_a(z)=e^{ia^2z},
\]

the boundary phase delay is positive, while the normalized radial soft
curvature is

\[
 -a^3/4<0.
\]

Differentiating a unitary path gives a self-adjoint tangent generator with no
sign.  PR #398 supplies a stronger zeta-shaped control retaining symmetry,
cocycle and safe Jordan positivity while its target Pick matrix is indefinite.
This is `R-91009`.

## V. Higher Fock chaos cannot repair a linear target

Under intensity scaling `r nu`, a positive product-system-compatible output
kernel has

\[
 K_r=\sum_{m\ge1}r^mK_m,
 \qquad K_m\succeq0.
\]

If the target is exactly source-linear, `K_r=rK_1`, positivity forces

\[
 K_m=0\qquad(m\ge2).
\]

Thus full Poisson Fock space is the canonical dilation, but the
conclusion-producing map acts on compensated first chaos.  This is `L-91036`.

## VI. Exact positive source tangent

The normalized Jordan radial curvature is

\[
 \mathscr C_a^{\rm J}(z)
 =-\partial_a[a^{-1}\log Q_a(z)].
\]

Its prime-power coefficients are

\[
 \frac{1-(1+2a\log n)n^{-2a}}{ka^2}>0.
\]

It has the one-particle Gram factor

\[
 w_{a,s}(r,n)
 =\frac2a\sqrt{r\Lambda(n)\log n}\,n^{-s-r},
 \qquad0<r<a,
\]

and

\[
 \mathscr C_a^{\rm J}(s+\bar t)
 =\langle w_{a,s},w_{a,t}\rangle.
\]

The entire safe generalized-prime normalized curvature is therefore a positive
first-chaos kernel with complete carrier polarization.  This is `L-91037`.

## VII. The scalar Wigner--Smith shadow

For Suzuki's boundary multiplier put

\[
 B_a(x)=-i\partial_a[a^{-1}\log\Theta_a(x)].
\]

Then

\[
 \mathcal N_x(a)=-\frac{a^3}{4}B_a'(x),
\]

and, with `P=-i partial_x`,

\[
 M_{\mathcal N(a)}
 =-\frac{a^3}{4}i[P,M_{B_a}].
\]

This is an exact scalar-diagonal identity, retained in corrected `L-91038`.

It is **not** the complete screw Gram.  For one real zero ordinate, the true
carrier kernel is

\[
 \Psi_a(\gamma-x)\overline{\Psi_a(\gamma-y)},
\]

which is generically nonzero when `x!=y`; the multiplication surrogate has
zero off-diagonal distribution kernel.  `R-91010` records this exact
polarization refutation.

## VIII. Correct full-Gram endpoint

Let

\[
 \mathcal A_a^{\rm del}:
 \ell^2_{\rm fin}(\mathfrak I_a^{\rm del})
 \longrightarrow\mathcal H_{\eta,0}
\]

synthesize delayed causal, anti-causal and bridge tests.  The actual target is

\[
 \boxed{
 \mathbb K_a^{\rm del}
 =
 (\mathcal A_a^{\rm del})^*
 \mathfrak Q_\zeta
 \mathcal A_a^{\rm del}.
 }
\]

`T-91008` states CDFHGI: construct an explicit source-ordered isometry

\[
 \mathcal C_{a_0}:
 \mathfrak g_{a_0}^{\Gamma,\mathrm{pole}}
 \oplus L^2(\omega_{a_0,c})
 \longrightarrow
 \mathcal H_{a_0}^{\rm delayed\ Hardy}
 \oplus\mathfrak e_{a_0}
\]

whose **complete** defect kernel is `K_(a_0)^del`, including every carrier,
delay, orientation and bridge cross term.

If constructed, this proves RH by the repaired form-core theorem and Suzuki's
screw criterion.  Under RH an existential Kolmogorov factorization exists;
the open problem is the explicit source construction.

## IX. Suzuki 2026 localized-operator confirmation

Suzuki's June 2026 paper constructs the localized Weil operator explicitly:

\[
 B_a=D^*G_aD,
 \qquad
 A_a=\text{Friedrichs extension of }B_a.
\]

Its lowest eigenvalue

\[
 \lambda_a=\inf Q_W^a(v)/\|v\|_2^2
\]

is continuous, is positive for sufficiently small support, and becomes
negative at some support if RH is false.  A shifted positive Hilbert norm exists
for every `lambda<lambda_a`, but inserting such a shift does not prove the
unshifted sign.  The source lock is
`2026-08-12-suzuki-2026-weil-quadratic-source-lock.md`.

This independently confirms the corrected boundary:

```text
positive shifted/self-adjoint realizations are available;
unshifted full-Gram positivity is the RH gate.
```

## X. Verification

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
scalar commutator -> full delayed Gram                 REFUTED
Suzuki localized Weil operator                         IMPORTED PROVED
CDFHGI explicit completed full-Gram factorization      OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```
