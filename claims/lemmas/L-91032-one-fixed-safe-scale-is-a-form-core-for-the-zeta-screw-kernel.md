# L-91032 — Scalar fixed-scale form core: refuted and superseded

Claim ID: `L-91032`  
Status: **REFUTED EXACTLY BY `R-91008`; SUPERSEDED BY DELAY-FIBRE REPAIR `L-91034`**  
Created: 2026-08-11  
Corrected: 2026-08-12  
RH status: **unproved**

## 1. Original claim

The original packet claimed that, for one fixed `a_0>1/2`, the carrier
modulations of one causal Cauchy mother span the positive-half-line weighted
zero-integral space, the reflected mother spans the negative-half-line
counterpart, and one bridge fills the remaining global defect.

The proposed proof used the distributional identity

\[
 H'\overline{\psi_{a_0}}=0
\]

and inferred that `H` is constant because `psi_(a_0)` is nonzero almost
everywhere.

## 2. Exact failure

`R-91008` computes the causal impulse explicitly and proves that it has a
positive-time zero

\[
 \tau_0/a_0,
 \qquad
 \tau_0=1.5698664803365582563\ldots .
\]

The weighted vector

\[
 h_0(t)=e^{-\eta t}
 \mathbf1_{(\tau_0/a_0,\infty)}(t)
\]

is orthogonal to every carrier modulation of the causal derivative family.
Its derivative contains a Dirac mass at the zero of the mother, so

\[
 \psi_{a_0}\delta_{\tau_0/a_0}=0.
\]

Thus “nonzero almost everywhere” is insufficient against point-supported
distributions.  The scalar causal orthogonal complement has dimension at
least two, not one.  Reflection gives an independent anti-causal hidden jump,
and one bridge cannot repair the resulting global codimension.

Therefore the original density statement is false.

## 3. Surviving pieces

The following parts of the original packet remain useful:

```text
weighted screw-form continuity, subject to its declared review;
causal/anti-causal support and exponential decay;
mean-zero carrier derivatives;
the need for a bridge between half-line integral defects;
one fixed safe scale as a desirable target.
```

The scalar completeness assertion and every theorem using it are not retained.

## 4. Correct repair

`L-91034` replaces the single mother by an energy-preserving direct integral of
all positive delays:

\[
 (\mathcal J_wF)(u,\tau)
 =\sqrt{w(\tau)}e^{-iu\tau}F(u).
\]

The delayed copies have no common physical zero.  The repaired causal family
has only the true half-line integral defect; the reflected family has the
opposite defect; one bridge then gives a proposed complete global form core.

## 5. Consequential corrections

- `T-91007` is blocked because its reverse implication used this false density
  theorem.
- The corrected fixed-scale criterion and final tangent-intertwiner target are
  `T-91008`.
- No claim of RH follows from the scalar family.

## 6. Exact boundary

```text
scalar causal form core                          FALSE
one scalar two-sided family plus bridge          FALSE
interior causal impulse zero                     EXACT
delay-fibre common-zero repair                   PROPOSED COMPLETE in L-91034
corrected delayed fixed-scale criterion          PROPOSED in T-91008
Riemann Hypothesis                               UNPROVED
```
