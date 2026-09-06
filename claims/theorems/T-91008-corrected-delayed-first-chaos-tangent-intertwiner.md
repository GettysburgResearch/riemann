# T-91008 — The corrected final component is a delayed first-chaos full-Gram intertwiner

Claim ID: `T-91008`  
Status: **FULL CONDITIONAL RH PROPOSAL / SINGLE OPEN FULL-GRAM INTERTWINER — ADVERSARIAL REVIEW REQUIRED**  
Created: 2026-08-12  
Corrected: 2026-08-12  
Supersedes: scalar-core `T-91007`; scalar-commutator endpoint refuted by `R-91010`  
Depends on: main `T-91006`, `L-91030`, `L-91031`, `R-91008`, `L-91034`--`L-91037`, `R-91009`, `R-91010`, and Suzuki's screw criterion  
RH status: **unproved**

## 1. Corrections to the previous endpoints

Three successive simplifications required hostile correction.

1. `R-91008` proves that one scalar causal mother has an interior physical
   zero and a hidden jump distribution.  The one-bridge scalar family in
   `L-91032` is not a form core.
2. `L-91036` proves that a source-linear target, under the natural
   intensity/product-system grading, cannot use higher positive Poisson
   chaoses.  The conclusion-producing source is the compensated first chaos.
3. `R-91010` proves that the Wigner--Smith commutator is only a scalar diagonal.
   It does not contain cross-carrier, cross-delay, cross-orientation or bridge
   interference.

`L-91035` nevertheless closes an important genuine component: Suzuki's
multiplicative Hankel operator is the exact positive-metric completed
**amplitude** isometry for the same generalized-Jordan coefficients.

The corrected final component is therefore a **fully polarized first-chaos
Douglas/Stinespring factorization** into a **delayed two-sided** Hardy reserve.

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
wavelet of `L-91034`; let `F_star` be the bridge.  Define

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

Any one fixed `a_0>1/2` remains sufficient; the additional coordinate is a
passive output delay, not a scale limit.

## 3. Synthesis-operator formulation

Let

\[
 \mathcal A_{a_0}^{\rm del}:
 \ell^2_{\rm fin}(\mathfrak I_{a_0}^{\rm del})
 \longrightarrow\mathcal H_{\eta,0}
 \tag{T-91008.4}
\]

send a finitely supported coefficient vector to the corresponding linear
combination of delayed tests.  Then

\[
 \boxed{
 \mathbb K_{a_0}^{\rm del}
 =
 (\mathcal A_{a_0}^{\rm del})^*
 \mathfrak Q_\zeta
 \mathcal A_{a_0}^{\rm del}.
 }
 \tag{T-91008.5}
\]

This is an integral/full matrix operator.  It is not the multiplication
operator supplied by the scalar Wigner--Smith commutator.

## 4. Explicit source first chaos

For the safe generalized-Jordan channel, `L-91037` supplies

\[
 \mathscr C_a^{\rm J}(s+\bar t)
 =\langle w_{a,s},w_{a,t}\rangle
 \tag{T-91008.6}
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
 \tag{T-91008.7}
\]

Equivalently, on a safe carrier line,

\[
 \boxed{
 d\omega_{a,c}(u)
 =\sum_{n=p^k}
 \frac{1-(1+2a\log n)n^{-2a}}{ka^2}
 n^{-c}\delta_{\log n}(u).
 }
 \tag{T-91008.8}
\]

The carrier defects

\[
 h_x(u)=e^{-ixu}-1
\]

live in

\[
 \boxed{
 \mathfrak h_a^{\rm J}=L^2(\omega_{a,c}).
 }
 \tag{T-91008.9}
\]

The full bosonic Fock product system of `L-91030` remains the canonical
Stinespring dilation, but higher chaos is not additional source-linear sign
budget.

## 5. Explicit amplitude colligation already available

Let

\[
 c_a(n)=n^a\prod_{p\mid n}(1-p^{-2a})
\]

and let `g_a,h_a` be Suzuki's explicit gamma and completed arithmetic kernels
from `L-91035`.  The multiplicative Hankel operator

\[
 (\mathsf H_af)(x)
 =\int_0^\infty h_a(xy)f(y)dy
\]

is a positive-metric unitary involution for safe `a`, satisfying

\[
 \boxed{
 \mathcal M_{1/2}\mathsf H_a
 =M_{\Theta_a}\mathsf R\mathcal M_{1/2}.
 }
 \tag{T-91008.10}
\]

Thus the prime Jordan amplitude, gamma factor, pole factor and two-sided Hardy
reflection are already embedded explicitly.

This does not determine the full delayed screw Gram.  `R-91009` blocks the
amplitude-to-tangent shortcut, while `R-91010` blocks the diagonal-to-matrix
shortcut.

## 6. CDFHGI — the corrected exact remaining theorem

> **Completed Delayed First-chaos Hardy Gram Intertwiner (CDFHGI).**  For the
> fixed safe scale `a_0`, construct explicitly source-ordered positive Hilbert
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
> whose complete transfer on every finite carrier/orientation/delay/bridge
> packet has defect kernel exactly
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
> The map must preserve coefficient-one radial normalization, every cross term
> and the exact gamma/pole completion.  No indefinite metric, square root of the
> already-unknown target kernel, scalar-diagonal substitution or same-scale
> signed remainder is permitted.

Equivalently, on every finite rational packet, the explicit completed source
and delayed-output Gram matrices must satisfy the exact Douglas contraction
inequality whose defect is `(T-91008.2)`.

## 7. Why CDFHGI proves RH

CDFHGI gives

\[
 \mathbb K_{a_0}^{\rm del}(i,j)
 =\langle R_i,R_j\rangle_{\mathfrak e_{a_0}}
 \tag{T-91008.13}
\]

for explicit defect vectors.  Hence every finite delayed matrix is positive
semidefinite.  The corrected fixed-scale criterion `(T-91008.3)` then gives RH.

Conversely, under RH the zero-side Lévy measure gives an existential
Kolmogorov factorization.  The open burden is the explicit source-ordered
construction from the prime first chaos and completed reserve.

## 8. Exact binary rejection tests

Reject a purported proof if any of the following occurs.

1. **Scalar-core reuse.** `L-91032` is false.
2. **No delay fibre.** One scalar causal mother has a hidden jump defect.
3. **Amplitude/tangent confusion.** Suzuki closes amplitude transport only.
4. **Scalar-commutator substitution.** `R-91010` proves it omits every
   off-diagonal carrier interference term.
5. **Higher-chaos cancellation.** Positive orthogonal chaos levels cannot
   cancel to an exactly source-linear target.
6. **Wrong source.** Ordinary von Mangoldt, generalized-Jordan intensity,
   normalized radial-curvature intensity and pole-subtracted tails are distinct
   typed objects.
7. **Dropped gamma or pole channel.** The completed reserve is load bearing.
8. **Existential square root.** Assuming target PSD and taking its square root
   is not a source construction.
9. **Loss of coefficient one.** No scalar loss or gain is permitted in the
   returned normalized state.
10. **Numerical PSD scan.** Finite computation does not prove the all-packet
    isometry.

## 9. Immediate analytic subproblem

Use Suzuki's explicit amplitude isometry to transport the safe source vectors
of `L-91037`, then compute the complete sesquilinear transfer between two
independent delayed output packets.  The target equality must be established
at the kernel level:

\[
 \langle \mathcal C_{a_0}X_i,\mathcal C_{a_0}X_j\rangle
 =\langle X_i,X_j\rangle
 -\mathbb K_{a_0}^{\rm del}(i,j),
 \tag{T-91008.14}
\]

for all indices `i,j`, including opposite Hardy orientations and bridge terms.

The scalar Wigner--Smith identity of corrected `L-91038` supplies only the
`i=j` diagonal shadow and may be used as a normalization check, not as the
factorization.

## 10. Exact status

```text
scalar fixed-scale form core                         REFUTED
corrected delayed fixed-scale form core              PROPOSED COMPLETE
Suzuki completed amplitude embedding                 IMPORTED PROVED
source-linear target -> compensated first chaos      PROPOSED COMPLETE
normalized Jordan curvature first-chaos Gram         EXACT
amplitude unitarity -> tangent/full-Gram positivity  REFUTED
scalar commutator -> full delayed Gram                REFUTED
CDFHGI explicit completed full-Gram factorization    OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
