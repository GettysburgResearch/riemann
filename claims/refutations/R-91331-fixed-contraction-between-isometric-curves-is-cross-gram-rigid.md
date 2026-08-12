# R-91331 — A fixed contraction between isometric curves is cross-Gram rigid and cannot create curvature reserve

Claim ID: `R-91331`  
Status: **PROVED ABSTRACT RIGIDITY THEOREM AND EXACT REFUTATION OF THE PROPOSED FIXED-COLLIGATION RESERVE MECHANISM**  
Created: 2026-08-13  
Corrects: the intended strict data-processing application of `L-91305`  
Strengthens: `R-91330` from an asymptotic speed obstruction to an any-two-scales impossibility for the completed Fisher source  
RH status: **unproved**

## 1. General rigidity theorem

Let `H0,S,H` be Hilbert spaces, let `A` be an index set, and suppose

\[
 V_\alpha:H_0\to S,
 \qquad
 M_\alpha:H_0\to H
 \tag{R-91331.1}
\]

are isometries for every `alpha in A`. Let

\[
 C:S\to H
\]

be a contraction satisfying

\[
 \boxed{CV_\alpha=M_\alpha}
 \tag{R-91331.2}
\]

for every `alpha`.

Then:

\[
 \boxed{
 C^*CV_\alpha=V_\alpha
 \qquad(\alpha\in A),
 }
 \tag{R-91331.3}
\]

\[
 \boxed{
 V_\alpha^*V_\beta
 =M_\alpha^*M_\beta
 \qquad(\alpha,\beta\in A),
 }
 \tag{R-91331.4}
\]

and `C` is an isometry on

\[
 S_0=\overline{\operatorname{span}}
 \{\operatorname{Ran}V_\alpha:\alpha\in A\}.
 \tag{R-91331.5}
\]

### Proof

For `f in H0`,

\[
 \|CV_\alpha f\|
 =\|M_\alpha f\|
 =\|f\|
 =\|V_\alpha f\|.
\]

Since `I-C*C` is positive,

\[
 \langle(I-C^*C)V_\alpha f,V_\alpha f\rangle=0
\]

implies `(I-C*C)^(1/2)V_alpha f=0`, hence (R-91331.3). Therefore

\[
 M_\alpha^*M_\beta
 =V_\alpha^*C^*CV_\beta
 =V_\alpha^*V_\beta,
\]

which is (R-91331.4). The same positive-defect argument shows that
`I-C*C` vanishes on the algebraic span of all source ranges and hence on its
closure, proving (R-91331.5).

This is not merely a necessary infinitesimal inequality. It is exact global
cross-Gram equality.

## 2. Smooth curves have identical normal curvature

Assume now that `A` is an interval and `V_a,M_a` are strongly differentiable.
Every difference quotient

\[
 \frac{V_{a+h}f-V_af}{h}
\]

lies in `S0`, so `dot V_a f in S0`. Since `C` is isometric on `S0`,

\[
 \|C\dot V_af\|=\|\dot V_af\|.
 \tag{R-91331.6}
\]

Moreover `C` maps `Ran V_a` unitarily onto `Ran M_a`. Therefore it maps the
component of `dot V_af` orthogonal to `Ran V_a` onto the component of
`dot M_af` orthogonal to `Ran M_a`. With the notation of `L-91305`,

\[
 \boxed{
 N_a^H=CN_a^S,
 \qquad
 (N_a^H)^*N_a^H=(N_a^S)^*N_a^S.
 }
 \tag{R-91331.7}
\]

Thus the `L-91305` data-processing inequality is necessarily equality for an
actual fixed contraction whose source and output maps are both isometries over
one differentiable family.

The proposed auxiliary terms also vanish:

\[
 \boxed{
 (I-C^*C)^{1/2}N_a^S=0,
 \qquad
 Q_aCN_a^S=0.
 }
 \tag{R-91331.8}
\]

The first vanishes because `N_a^S in S0`; the second because `C` is isometric
on `S0` and `N_a^S` is orthogonal to `Ran V_a`.

Consequently a strict source-minus-output curvature reserve cannot be produced
by this architecture. A valid fixed colligation can only realize an exact
isometric copy of the entire output curve and its curvature.

## 3. Completed Fisher cross-Gram

Retain the completed tilt source of `L-91309`:

\[
 q_a(y)=\xi(\tfrac12+a)^{-1/2}e^{-ay/2},
 \qquad
 (V_af)(t,y)=e^{ity}q_a(y)f(t).
 \tag{R-91331.9}
\]

For `a,b>1/2`, direct integration gives

\[
 \boxed{
 V_a^*V_b
 =\rho(a,b)I,
 }
 \tag{R-91331.10}
\]

where

\[
 \boxed{
 \rho(a,b)
 =\frac{
  \xi(\frac12+\frac{a+b}{2})
 }{
  \sqrt{
   \xi(\frac12+a)\xi(\frac12+b)
  }
 }.
 }
 \tag{R-91331.11}
\]

The completed density is nondegenerate. Hence

\[
 \partial_a^2\log\xi(\tfrac12+a)
 =\operatorname{Var}_a(Y)>0,
 \tag{R-91331.12}
\]

so `log xi(1/2+a)` is strictly convex. Therefore

\[
 \boxed{
 0<\rho(a,b)<1
 \qquad(a\ne b).
 }
 \tag{R-91331.13}
\]

## 4. Suzuki cross-Gram

The target maps are the unitary multipliers

\[
 M_a=M_{\Theta_a},
 \qquad
 |\Theta_a(t)|=1
 \quad\text{a.e.}
 \tag{R-91331.14}
\]

Thus

\[
 \boxed{
 M_a^*M_b
 =M_{\overline{\Theta_a}\Theta_b},
 }
 \tag{R-91331.15}
\]

which is a unitary multiplication operator. In particular,

\[
 \|M_a^*M_b\|=1.
 \tag{R-91331.16}
\]

For distinct scales, (R-91331.10)--(R-91331.16) cannot satisfy the mandatory
cross-Gram equality (R-91331.4): the source cross-Gram is the strict scalar
contraction `rho(a,b)I`, while the output cross-Gram is unitary.

Therefore:

\[
 \boxed{
 \text{No fixed contraction can map the completed Fisher source}
 \ V_a\ \text{to the Suzuki multiplier}\ M_{\Theta_a}
 \text{ at even two distinct safe scales.}
 }
 \tag{R-91331.17}
\]

This is stronger than the large-scale speed contradiction in `R-91330` and
requires no asymptotic analysis.

## 5. Consequence for source augmentation

Adding an independent positive-curvature channel to `V_a` while retaining an
isometric source map does not evade the theorem. If one fixed contraction maps
the augmented isometry exactly to the output isometry, then the augmented
cross-Gram must equal the output cross-Gram identically, and its normal
curvature must equal the output normal curvature.

Thus a non-tautological strict domination theorem must relax at least one
ingredient:

```text
source maps are isometries;
output maps are isometries;
observation is one fixed contraction;
exact amplitude identity C V_a=M_a over more than one scale.
```

Possible corrected frameworks include:

```text
positive source forms without an isometric amplitude lift;
a Krein/Pontryagin colligation rather than a Hilbert contraction;
a scale connection with its curvature controlled explicitly;
an exact isometric realization used only for equality, followed by a separate
  arithmetic positive-form comparison;
a one-scale tangent factorization that does not claim a common amplitude curve.
```

## 6. Normative status of `L-91305`

The abstract algebra in `L-91305.1`--`L-91305.11` is correct. Its intended
application as a strict source-curvature data-processing mechanism is not:
under its own isometry hypotheses and a genuine all-scale fixed contraction,
all defect terms vanish and the curvature inequality is equality.

Accordingly, the remaining RH route cannot be closed by constructing the
proposed fixed Hilbert-space contraction with a larger positive source reserve.
The source-minus-output block isolated in `L-91327`--`L-91329` must be proved
as a direct positive-form theorem or in a genuinely different indefinite or
connection-corrected geometry.

## 7. Exact boundary

```text
fixed contraction + isometric source/output curves       CROSS-GRAM RIGID
fixed contraction isometric on full curve span            EXACT
source and output normal curvatures                        IDENTICAL
L-91305 auxiliary reserve for a genuine curve              ZERO
completed Fisher cross-scale overlap                       rho(a,b) I, rho<1
Suzuki cross-scale overlap                                 UNITARY MULTIPLIER
fixed Fisher-to-Suzuki contraction at two scales           IMPOSSIBLE
strict positive reserve by isometric source augmentation   IMPOSSIBLE
one-scale/direct-form/indefinite alternatives              NOT RULED OUT
completed source-minus-output finite block positivity      OPEN / RH-BEARING
Riemann Hypothesis                                         UNPROVED
```
