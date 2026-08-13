# O-92000 — Current boundary after the third-order Clark-curvature reduction

Claim ID: `O-92000`  
Status: **RESEARCH BOUNDARY / HANDOFF**  
Created: 2026-08-13  
RH status: **unproved**

## The exact simplification

The parent PR #438 identified order three as the first possible negative level
of the linear safe-real Xi hierarchy.  The present branch removes the matrix
search at that level.

For

\[
 p(t)=\frac1{\sqrt t}
 \frac{\xi'}{\xi}\left(\frac12+\sqrt t\right),
\]

the three-node determinant factors as

\[
 \text{positive prefactor}
 \times [1/p]_{t_1,t_2,t_3}
 \times [tp]_{t_1,t_2,t_3}.
\]

The second factor `tp` is proposed unconditionally strictly concave by an
orbitwise argument.  Therefore the entire actual-Xi order-three sign is

\[
 \boxed{(1/p)''\le0.}
\]

Equivalently,

\[
 \boxed{
 x^2FF''-2x^2(F')^2+xFF'+F^2\ge0.
 }
\]

## What is exact

```text
three-node determinant factorization          EXACT
order-two minors from parent monotonicities    PROPOSED COMPLETE
off-line orbit reciprocal curvature            EXACT WRONG SIGN
large-x scalar asymptotic                      STANDARD EFFECTIVE REDUCTION
```

## What requires review

```text
orbitwise global concavity of tp               PROPOSED UNCONDITIONAL
differentiated Hadamard convergence             REVIEW JOINT
effective threshold in the large-x proof        NOT OPTIMIZED
```

## What remains open

```text
directed compact sign for the scalar curvature;
then the order-four continued-fraction/string coefficient;
then all-order Stieltjes/Caratheodory positivity.
```

## Recommended next attack

1. Use pole-cancelled coordinates near `s=1`:
   `eta_D(s)` together with `(s-1)/(1-2^(1-s))`.
2. Bound `F,F',F''` by directed intervals on a finite partition.
3. Use Stirling with explicit Bernoulli remainder beyond a moderate cutoff.
4. After closing order three, derive the order-four determinant in a
   Stieltjes continued-fraction basis rather than expanding a `4 x 4`
   determinant blindly.

## Firewalls

- A positive floating-point mesh does not prove the compact sign.
- Orbitwise positivity is impossible: one off-line orbit has strictly convex
  reciprocal curvature.
- Order-two monotonicity does not imply order three.
- Order-three positivity would not imply RH; the control orbit shows that the
  hierarchy remains genuinely all-order.
