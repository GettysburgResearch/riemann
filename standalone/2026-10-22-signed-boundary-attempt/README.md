# Signed boundary attempt: a complete cubic rectangle and a sharper inverse target

22 October 2026. **Research packet; no improved numerical zero-free boundary
has been proved.** The inherited reference remains

\[
 B_\flat=0.874886647039964\ldots.
\]

The packet derives two analytic components from explicitly named source
inputs and a complete conditional route to the rational target
`1749/2000 = 0.8745`. The latter depends on an unproved high-conductor
estimate. It also records why several apparently favorable changes do
not improve the current comparison. RH remains open.

## Source and status

The frozen parent is PR #1012, commit
`64cb43c038d1828a478cb97cbc32e435e111d2d2`, on
`research/boundary-iteration-20261020`. Its proposed analytic results
remain proposed inputs; their presence on a branch does not make them
integrated mathematics. This packet adds a separate directory and does
not strengthen or replace the inherited claims.

The numerical reference is Liu,
[arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), with that paper's
stated analytic dependencies. It is an imported preprint theorem, not a
global proof reconstructed by the finite checks here. The older first
version's larger decimal must not be substituted for this reference.

## 1. A bound for the whole completed cubic rectangle

[COMPLETED_RECTANGLE.md](COMPLETED_RECTANGLE.md) defines the exact smooth
completed sum, including its cube variables, common-prime zeros, nonzero
angular order, and coherent Möbius row coefficient. For `A >= B >= 2`,
the new deduction is

\[
 |\mathcal T_{\rm comp}(A,B)|
 \ll (AB)^\epsilon B^{3/2}(A/B)^{-(1-\beta/2)}.
\]

The proof combines the inherited signed complementary-variable estimate
with the inherited natural-count cubic mean. It keeps all divisors.
Short complements, including the full divisor, are handled by a legal
left contour shift of the completed expression; long complements retain
their Möbius signs. The optimization is continuous over
`1/2 <= beta <= 1`.

At `beta=1`, the reciprocal input needs only Euler convergence and gives

\[
                  |\mathcal T_{\rm comp}(A,B)|
                      \ll (AB)^\epsilon B^2A^{-1/2}.
\]

This improves the particular inherited resources on power-separated
rectangles `B < A <= B^2`. The sharper substitution `beta=B_flat` needs
the actual angular Hecke premise and is not supplied by the finite-order
theorem alone. No literature-wide novelty claim is made.

[JOINT_EULER_FACTOR.md](JOINT_EULER_FACTOR.md) explains both unresolved
interfaces. Dividing out the cube completion obstructs the short-complement
contour. A quadratic conductor `H` changes the effective ratio to
`BH^2/A`; at the actual terminal `A=HB`, this is `H`. Bounded `H` gives
only a constant improvement, and growing `H` leaves no short-complement
range. Thus the new completed estimate does not lower the current
boundary through that terminal.

## 2. Remove a definite growing conductor range from the inverse target

[RADICAL_STRATIFICATION.md](RADICAL_STRATIFICATION.md) works over the
Eisenstein field. Write a row uniquely as `u=v a^6`, with `v` sixth-power
free, allowing overlap between `v` and `a`. Put

\[
 R(u)=N\operatorname{rad}(v),\qquad \kappa=2\beta-1.
\]

Outside the fixed excluded set, `R(u)` is the primitive-conductor norm;
primes appearing only through sixth powers remain exact punctures.
For the smooth normalized inverse polynomial `M_u(D;Q,W)` defined there,
the common finite-order zero-free input gives

\[
 \sum_{\substack{0<Nu\le H\\R(u)\le C}}
       |M_u(D;Q,W)|^2
 \ll_\epsilon \mathcal S(W)^2(HD C NQ)^\epsilon
                      H^{1/6}C^{5/6}D^\kappa.
\]

The proof supplies the full zero mask, conductor uniformity, row count,
and exact sixth-power amplification reduction. In particular, using only
the weaker inherited `beta=7/8`, at `H >= D^(99/100)` the rows
`R(u) <= D^(2/25)` satisfy

\[
 \sum_{\substack{0<Nu\le H\\R(u)\le D^{2/25}}}
       |M_u(D;Q,W)|^2
 \ll_\epsilon \mathcal S(W)^2(HDNQ)^\epsilon H D^{-1/120}.
\]

The remaining hypothesis is therefore the following concrete statement,
with the complete fixed-character, smooth-profile and polynomial
puncture uniformity specified in that note:

\[
 \boxed{\quad
 \sum_{\substack{0<Nu\le H\\R(u)>D^{2/25}}}
       |M_u(D;Q,W)|^2
 \ll_\epsilon \mathcal S(W)^2(HDNQ)^\epsilon H,
 \qquad H\ge D^{99/100}.
 \quad}
\]

**This high-conductor moment is unproved.** If it held, the real
sixth-power amplifier would give the full inverse exponent

\[
               e(r)=\max\{1,\;1/6+33r/40\}.
\]

The low-conductor removal does not identify or delete the diagonal
created by a later positive transform. The high-conductor target still
includes proper-order quadratic and cubic rows: the supplied classical
large sieves do not remove their unsaved column-length term.

## 3. A finite conditional target: 0.8745

[CONDITIONAL_08745_CERTIFICATE.md](CONDITIONAL_08745_CERTIFICATE.md)
uses the exact rational choices

\[
 \kappa=\frac34,\qquad \ell=\frac{253}{1500},\qquad
 b=\frac7{100},\qquad \eta=\frac1{100}.
\]

With the stronger inverse exponent above, these give

\[
 B(\ell)=\frac{11}{12}-\frac\ell4=\frac{1749}{2000}=0.8745.
\]

The proof covers the full continuous detector domains, including the
inverse floor at `r=100/99` and the unchanged high-delta branch. It
derives a polynomial completed-square certificate with a uniform
endpoint margin exceeding `1/25000`, and verifies every inherited side
condition. This is a finite positive range improvement, not an
extrapolation from the earlier derivative at zero. A negative control
shows that the old inverse envelope fails at these same parameters.

There are two expressly matched family interfaces:

- [EISENSTEIN_CONDITIONAL_ASSEMBLY.md](EISENSTEIN_CONDITIONAL_ASSEMBLY.md)
  uses Xu--Sang, arXiv:2610.15291v2, over the Eisenstein field itself.
  Its numerator theorem accepts a general valid row count. With their
  imported analytic inputs retained, `HC(E;1/100,2/25)` and the
  reduction above therefore imply the conditional `0.8745` boundary
  for the stated Eisenstein and Dirichlet families, including zeta.
- [MATCHING_FIELD_RADICAL_REDUCTION.md](MATCHING_FIELD_RADICAL_REDUCTION.md)
  independently ports the arithmetic reduction into Liu's actual
  exterior-ideal and finite S-unit conventions. This supplies the
  reduction for a matching `HC_F` premise over, for example,
  `F=Q(zeta_12)`. It does not infer `HC_F` from `HC(E)`.

Both are **conditional implications**. Neither field version of `HC`
has been proved here, and the imported analytic inputs have not been
independently reconstructed in full. The completed-cubic result in
Section 1 is separate; it does not prove either high-conductor premise.

## 4. Exact algebra and method-specific obstructions

| File | Result and scope |
|---|---|
| [JOINT_EULER_FACTOR.md](JOINT_EULER_FACTOR.md) | Reassembles the cube inverse and signed complement into the exact local factor `1-x+z-y`; gives its full correction-product tube and the remaining coherent-series obstruction. |
| [DIRECT_AUXILIARY_AND_LOCAL_KAPPA_AUDIT.md](DIRECT_AUXILIARY_AND_LOCAL_KAPPA_AUDIT.md) | A growing auxiliary prime loses at least `r/12` in the most favorable permitted separated-norm proposal. The better zero buffer on the original rows is not licensed for newly transformed characters. |
| [M2_CAPACITY_AUDIT.md](M2_CAPACITY_AUDIT.md) | For proposed coefficients `lambda>3`, one exact face of the current amplifier and pointwise-stripping architecture requires `lambda>=6 kappa`. This is not a lower bound on the actual moment. |

The diagonal specialization of the local Euler factor must not be
multiplied by an unevaluated divergent series to claim vanishing. In
its original domain, the full Möbius convolution equals the unit
contribution, one. The independent rectangular Mellin variables cannot
be replaced by their diagonal.

## Verification boundaries

Run, using Python's standard library:

```sh
python -I -S -B standalone/2026-10-22-signed-boundary-attempt/verify_algebra.py
python -I -S -B standalone/2026-10-22-signed-boundary-attempt/verify_conditional_08745.py
```

[ALGEBRA_CHECKS.json](ALGEBRA_CHECKS.json) is the exact replay output. It
checks the local polynomial factorization, rejects an omitted inverse-cube
term, checks the two continuous affine optimization pieces, isolates the
inherited reference root, and checks the rational conductor thresholds,
auxiliary-prime exponents and quadratic-terminal normalization. It does
not evaluate L-functions or prove the imported means, contour identities,
high-conductor premise, zero-free boundary, or RH.

[CONDITIONAL_08745_CHECKS.json](CONDITIONAL_08745_CHECKS.json) records
the separate exact scalar certificate. Its checker constructs the
polynomials from the primitive endpoint formula, uses coefficient
positivity to cover the continuous ranges, and checks all rational
side margins. It does not certify the analytic hypotheses or the
family-assembly notes.

The independent mathematical review record is [REVIEW.md](REVIEW.md).
Its source commit identifies the frozen mathematical snapshot; the later
review commit only deposits the reports. Review scope and omitted work
are explicit. Agreement between agents is not a substitute for the
displayed proofs or human scrutiny. No changes to `main` or to the
integrated research account are part of this packet.
