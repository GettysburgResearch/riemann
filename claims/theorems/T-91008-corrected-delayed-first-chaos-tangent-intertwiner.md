# T-91008 — The corrected final component is a delayed first-chaos tangent intertwiner

Claim ID: `T-91008`  
Status: **FULL CONDITIONAL RH PROPOSAL / SINGLE OPEN TANGENT INTERTWINER — ADVERSARIAL REVIEW REQUIRED**  
Created: 2026-08-12  
Supersedes on this branch: the proof route of `T-91007` through false `L-91032`  
Depends on: main `T-91006`, `L-91030`, `L-91031`, `R-91008`, `L-91034`--`L-91037`, `R-91009`, and Suzuki's screw criterion  
RH status: **unproved**

## 1. Correction to the previous endpoint

The previous endpoint was stated as

```text
full prime Poisson Fock environment
 -> one scalar causal Hardy output;
one scalar fixed-scale family + one bridge
 -> complete screw form core.
```

Both formulations require correction.

1. `R-91008` proves that the scalar causal impulse has an interior zero and
   therefore admits a hidden jump distribution.  The one-bridge scalar family
   in `L-91032` is not a form core.
2. `L-91036` proves that a source-linear target, under the natural
   intensity/product-system grading, cannot use higher Poisson chaoses.  The
   conclusion-producing source is the compensated first chaos.
3. `L-91035` identifies Suzuki's multiplicative Hankel operator as the exact
   positive-metric completed **amplitude** isometry.  The amplitude embedding
   is already closed.  `R-91009` proves that amplitude unitarity does not sign
   the radial Wigner--Smith curvature.

The corrected final component is therefore a **tangent lift** from an explicit
prime first chaos into a **delayed two-sided** Hardy reserve.

## 2. Corrected output core

Fix one arbitrary safe scale

\[
 a_0>\frac12
\]

and choose `1<eta<2a_0`.  Let

\[
 \mathfrak I_{a_0}^{\rm del}
 =
 (\{+,-\}\times\mathbb R\times[0,\infty))
 \sqcup\{\star\}.
 \tag{T-91008.1}
\]

For `i=(epsilon,x,tau)`, let `F_i` be the delayed causal or anti-causal
wavelet of `L-91034`; let `F_star` be the bridge.  Define the completed screw
kernel

\[
 \boxed{
 \mathbb K_{a_0}^{\rm del}(i,j)
 =\mathfrak Q_\zeta(F_i,F_j).
 }
 \tag{T-91008.2}
\]

Subject to independent review of the repaired delay-fibre density argument,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \mathbb K_{a_0}^{\rm del}\succeq0
 \text{ on every finite packet of }
 \mathfrak I_{a_0}^{\rm del}.
 }
 \tag{T-91008.3}

Any one fixed `a_0>1/2` remains sufficient; what changes is the output
multiplicity, not the scale.

## 3. Explicit source first chaos

For the safe generalized-Jordan channel, `L-91037` supplies the positive
normalized radial-curvature kernel

\[
 \mathscr C_a^{\rm J}(s+\bar t)
 =\langle w_{a,s},w_{a,t}\rangle,
 \tag{T-91008.4}
\]

with

\[
 \boxed{
 w_{a,s}(r,n)
 =\frac2a
  \sqrt{r\Lambda(n)\log n}\,
  n^{-s-r},
 \qquad 0<r<a,\ n=p^k.
 }
 \tag{T-91008.5}
\]

Equivalently, on a safe carrier line the source spectral measure is

\[
 \boxed{
 d\omega_{a,c}(u)
 =\sum_{n=p^k}
 \frac{1-(1+2a\log n)n^{-2a}}{ka^2}
 n^{-c}\delta_{\log n}(u).
 }
 \tag{T-91008.6}
\]

The carrier vectors are

\[
 h_x(u)=e^{-ixu}-1.
 \tag{T-91008.7}
\]

The complete source-side polarization is therefore explicit in the
one-particle Hilbert space

\[
 \boxed{
 \mathfrak h_a^{\rm J}=L^2(\omega_{a,c}).
 }
 \tag{T-91008.8}

\]

The full bosonic Fock product system of `L-91030` remains the canonical
Stinespring dilation, but higher chaos is not additional sign budget.

## 4. Explicit amplitude colligation already available

Let

\[
 c_a(n)=n^a\prod_{p\mid n}(1-p^{-2a})
 \]

and let `g_a,h_a` be Suzuki's explicit gamma and completed arithmetic kernels
from `L-91035`.  The multiplicative Hankel operator

\[
 (\mathsf H_af)(x)
 =\int_0^\infty h_a(xy)f(y)dy
 \tag{T-91008.9}
\]

is a positive-metric unitary involution for `a>1/2`, satisfying

\[
 \boxed{
 \mathcal M_{1/2}\mathsf H_a
 =M_{\Theta_a}\mathsf R\mathcal M_{1/2}.
 }
 \tag{T-91008.10}
\]

Thus the prime Jordan amplitude, gamma factor, pole factor and two-sided Hardy
reflection are already embedded explicitly.

The missing object is the derivative of this colligation in the normalized
radial direction, not the colligation itself.

## 5. CDFHTI — the corrected exact remaining theorem

> **Completed Delayed First-chaos Hardy Tangent Intertwiner (CDFHTI).**  For the
> fixed safe scale `a_0`, there exist explicitly source-ordered positive Hilbert
> spaces
> 
> \[
> \mathfrak g_{a_0}^{\Gamma,\mathrm{pole}},
> \qquad
> \mathfrak e_{a_0},
> \]
> 
> and an isometry
> 
> \[
> \boxed{
> \mathcal C_{a_0}:
> \mathfrak g_{a_0}^{\Gamma,\mathrm{pole}}
> \oplus\mathfrak h_{a_0}^{\rm J}
> \longrightarrow
> \mathcal H_{a_0}^{\rm del}
> \oplus\mathfrak e_{a_0}
> }
> \tag{T-91008.11}
> \]
> 
> such that its transfer on the safe carrier first-chaos vectors, after
> Suzuki's explicit gamma/Jordan amplitude completion and analytic boundary
> identification, has defect kernel exactly
> 
> \[
> \boxed{
> \left(
> \mathbb K_{a_0}^{\rm del}(i,j)
> \right)_{i,j}.
> }
> \tag{T-91008.12}
> \]
> 
> Here `H_(a_0)^del` is the direct-integral causal/anti-causal output generated
> by the delayed Cauchy mother, together with the bridge coordinate.  The map
> must preserve all carrier polarizations and the coefficient-one radial
> normalization.  No indefinite metric, square root of the unknown target
> kernel, or same-scale signed remainder is permitted.

Equivalently, on every finite rational carrier/orientation/delay packet the
completed source and output Gram matrices must satisfy the exact Douglas
contraction inequality whose defect is `(T-91008.2)`.

## 6. Why CDFHTI proves RH

CDFHTI gives the Gram representation

\[
 \mathbb K_{a_0}^{\rm del}(i,j)
 =\langle R_i,R_j\rangle_{\mathfrak e_{a_0}}
 \tag{T-91008.13}
\]

for the defect vectors of the isometry.  Hence every finite delayed matrix is
positive semidefinite.  The corrected fixed-scale criterion `(T-91008.3)` then
gives RH.

Conversely, under RH the zero-side Lévy measure gives a Kolmogorov
factorization of the delayed kernel.  Thus the requested positive tangent lift
is sharp at the level of existence.  The burden is its explicit source-ordered
construction.

## 7. Exact binary rejection tests

Reject a purported CDFHTI proof if any of the following occurs.

1. **Scalar-core reuse.**  `L-91032` is false; isolated zeros of the impulse
   create hidden jump vectors.
2. **No delay fibre.**  The output must have no common physical zero.  One
   scalar causal factor is insufficient.
3. **Amplitude/tangent confusion.**  Suzuki's unitary Hankel operator closes
   only the amplitude transport.  `R-91009` gives an inner all-pass family with
   negative radial delay curvature.
4. **Higher-chaos cancellation.**  Positive orthogonal chaos levels cannot
   cancel to an exactly source-linear target.
5. **Wrong source.**  Ordinary von Mangoldt, generalized-Jordan intensity,
   normalized radial-curvature intensity and pole-subtracted tails are distinct
   typed objects.
6. **Dropped gamma or pole tangent.**  The derivative of the completed
   archimedean factor is load bearing.
7. **Diagonal-only calculation.**  Every carrier, delay and Hardy-orientation
   cross term must be retained.
8. **Existential square root.**  Taking a square root after assuming target PSD
   is not a source construction.
9. **Loss of coefficient one.**  The normalized returned radial state may not
   acquire a scalar smaller or larger than one.
10. **Numerical PSD scan.**  Finite computation cannot establish the all-packet
    isometry.

## 8. Immediate analytic subproblem

Differentiate Suzuki's exact Mellin intertwining

\[
 \mathcal M\mathsf H_a=M_{\Theta_a}\mathsf R\mathcal M
 \]

in the normalized radial direction.  The derivative has three explicitly
separable pieces:

```text
positive Jordan first-chaos creation       L-91037;
explicit gamma/pole tangent                elementary polygamma/rational terms;
second fundamental form of the Hardy path R-91009.
```

CDFHTI is equivalent to factoring the sum of the first two pieces as the norm
of the delayed Hardy tangent plus a positive auxiliary defect, with the third
piece fully absorbed and no signed remainder.

This is the narrowest current construction target.

## 9. Exact status

```text
scalar fixed-scale form core                         REFUTED
corrected delayed fixed-scale form core               PROPOSED COMPLETE
full Jordan bosonic amplitude product system          PROPOSED COMPLETE
Suzuki completed amplitude embedding                  IMPORTED PROVED
source-linear target -> compensated first chaos       PROPOSED COMPLETE
normalized Jordan curvature first-chaos Gram          EXACT
amplitude unitarity -> tangent positivity              REFUTED
CDFHTI positive completed tangent lift                 OPEN / RH-EQUIVALENT
Riemann Hypothesis                                    UNPROVED
```
