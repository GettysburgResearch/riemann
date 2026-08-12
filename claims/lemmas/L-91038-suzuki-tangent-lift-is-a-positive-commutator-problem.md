# L-91038 — The Suzuki tangent lift is one positive-commutator problem

Claim ID: `L-91038`  
Status: **PROPOSED COMPLETE EXACT OPERATOR REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-12  
Depends on: `L-91035`, `L-91037`, `R-91009`, main `L-91023`  
RH status: **unproved**

## 1. Suzuki orientation

Use Suzuki's upper-half-plane convention

\[
 \Theta_a(z)
 =\frac{\xi(1/2-a-iz)}{\xi(1/2+a-iz)}.
 \tag{L-91038.1}
\]

For `a>=1/2`, this is meromorphic inner unconditionally.  On the real axis
put

\[
 \boxed{
 q_a(x)
 =-i\Theta_a(x)^{-1}\partial_x\Theta_a(x).
 }
 \tag{L-91038.2}
\]

Functional-equation symmetry gives

\[
 q_a(x)=2\Re\frac{\xi'}{\xi}
 \left(\frac12+a-ix\right).
 \tag{L-91038.3}
\]

Thus, after reflecting the carrier, this is the Wigner--Smith delay of main
`L-91023`.

## 2. Normalized radial tangent symbol

Define

\[
 \boxed{
 B_a(x)
 =-i\partial_a
 \left[\frac1a\log\Theta_a(x)\right].
 }
 \tag{L-91038.4}
\]

Since the boundary multiplier is unimodular, `B_a(x)` is real wherever
finite.  Differentiating in the carrier,

\[
 \boxed{
 \partial_xB_a(x)
 =\partial_a\left[\frac{q_a(x)}a\right].
 }
 \tag{L-91038.5}
\]

The Cauchy soft count is therefore

\[
 \boxed{
 \mathcal N_x(a)
 =-\frac{a^3}{4}\partial_xB_a(x).
 }
 \tag{L-91038.6}
\]

Thus radial Cauchy positivity is the monotonicity

\[
 B_a'(x)\le0.
 \tag{L-91038.7}
\]

## 3. Tangent generator of Suzuki's unitary involution

In Mellin spectral coordinates, Suzuki's completed Hankel operator is

\[
 \mathsf S_a=M_{\Theta_a}\mathsf R,
 \qquad
 (\mathsf RF)(x)=F(-x),
 \tag{L-91038.8}
\]

and satisfies `S_a^2=I`.  Differentiation gives

\[
 \mathsf S_a\partial_a\mathsf S_a
 =-M_{\partial_a\log\Theta_a}.
 \tag{L-91038.9}
\]

The normalized self-adjoint tangent operator is therefore

\[
 \boxed{
 \mathsf B_a
 =-i\partial_a\left[\frac1a\log\Theta_a\right](X)
 =M_{B_a(x)}.
 }
 \tag{L-91038.10}

No abstract existence theorem is needed: the tangent operator is explicit
multiplication by `(L-91038.4)`.

## 4. Positive-commutator form

Let

\[
 \mathsf P=-i\partial_x
\]

on the usual smooth spectral core.  Then

\[
 i[\mathsf P,\mathsf B_a]
 =M_{B_a'}.
 \tag{L-91038.11}
\]

Consequently

\[
 \boxed{
 M_{\mathcal N_x(a)}
 =-\frac{a^3}{4}
  i[\mathsf P,\mathsf B_a].
 }
 \tag{L-91038.12}
\]

The scalar Cauchy gate is a Mourre-type positive-commutator assertion for the
normalized tangent of Suzuki's completed scattering involution.

The fully polarized delayed screw kernel in `T-91008` is the form-core lift of
this commutator identity.

## 5. Exact source split

From

\[
 \Theta_a=\Gamma_aQ_a
\]

one has

\[
 \boxed{
 \mathsf B_a
 =\mathsf B_a^{\Gamma,\mathrm{pole}}
  +\mathsf B_a^{\rm J}.
 }
 \tag{L-91038.13}
\]

On a safe line, `L-91037` factors the normalized Jordan radial derivative as
one positive first-chaos Gram.  The gamma/pole term is an explicit
polygamma/rational multiplier.  Analytic continuation to the symmetric
boundary combines them into the real tangent symbol `B_a`.

CDFHTI is exactly a positive-metric factorization of the negative commutator
in `(L-91038.12)` after this completed recombination.

## 6. Why the amplitude isometry stops here

For a differentiable unitary path, the tangent generator is only
self-adjoint.  Its commutator with the translation generator has no automatic
sign.  The control in `R-91009` has

\[
 \Theta_a(z)=e^{ia^2z},
 \qquad
 B_a(x)=x,
 \qquad
 -i[\mathsf P,\mathsf B_a]=-I.
\]

Thus the exact amplitude embedding of `L-91035` cannot be promoted to a
positive tangent embedding without a new arithmetic theorem.

## 7. Correct final target

The remaining component may now be stated without Fock shorthand:

> Construct an explicit source-ordered factorization of
> 
> \[
> -i[\mathsf P,\mathsf B_{a_0}]
> \]
> 
> as `C^*C` on the corrected delayed two-sided Hardy form core, for one fixed
> safe `a_0>1/2`, with the source vectors of `L-91037` and the exact gamma/pole
> tangent retained.

By `T-91008`, such a factorization proves RH.  It has not been constructed.

## 8. Exact boundary

```text
Suzuki amplitude involution                         IMPORTED PROVED
normalized tangent multiplier                       EXACT
Cauchy soft count = negative tangent commutator      EXACT
safe Jordan component = positive first chaos        EXACT
completed negative-commutator factorization          OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
