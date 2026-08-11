# R-91006 — Diagonal Cauchy gates cannot replace the fixed-scale Lévy Gram

Claim ID: `R-91006`  
Status: **EXACT POLARIZATION FIREWALL**  
Created: 2026-08-11  
Depends on: `L-91029`, `L-91030`, `T-91006`  
RH status: **unproved**

## 1. The diagonal observed by the recurrence

At a fixed safe scale `a_0>1/2`, the normalized sixteenfold Cauchy route tests

\[
 \mathbb K_{a_0}((+,x),(+,x))
 =a_0^4\mathcal R_x(a_0).
\]

Thus it sees only one diagonal family of the complete two-orientation kernel
of `T-91006`.

Even adding the anti-causal diagonal gives only

\[
 \mathbb K(i,i)\ge0
 \qquad(i\in\mathfrak I).
\]

## 2. Exact finite countermodel

Positive diagonal entries do not imply positivity of a Hermitian kernel.  The
matrix

\[
 \boxed{
 H=\begin{pmatrix}1&7/4\\7/4&1\end{pmatrix}
 }
\]

has both diagonal entries positive, while its eigenvalues are

\[
 \frac{11}{4},\qquad-\frac34.
\]

The failure is not repaired by testing the diagonal at every carrier: a
continuous Hermitian kernel may have nonnegative pointwise diagonal and a
negative two-point Pick matrix.

## 3. Why this is load-bearing here

The two Hardy orientations in `L-91030` are needed to span the positive and
negative physical half-lines.  Their cross terms are what reconstruct a
general compact mean-zero Weil test.  Deleting them leaves two codimension-one
half-line conditions and cannot recover Suzuki's complete screw form.

Likewise, the bridge vector is not cosmetic.  Without it, the span has zero
integral separately on each half-line and misses the direction in which the
positive and negative half-line masses cancel globally.

Therefore the following inference is invalid:

```text
all scalar dyadic residuals are nonnegative
    -> full screw kernel is positive
    -> RH.
```

A valid conclusion must provide one of:

1. the full cross-carrier/two-orientation Gram positivity of `T-91006`;
2. an exact polarization identity deriving every cross entry from positive
   source states;
3. a conservative Fock/Hardy colligation whose Gram automatically contains
   the cross terms.

## 4. Relation to the source channel

`L-91020` proves that the inherited Jordan multiplier is a completely positive
correlation channel and contracts negative trace mass.  A forward CP
contraction still does not allow a diagonal positive output to be pulled
backward to a positive input.

The explicit Poisson Fock environment of `L-91028` is valuable precisely
because it retains the full Stinespring vectors.  Any proof that traces them
out before matching the causal and anti-causal Hardy outputs reintroduces this
firewall.

## 5. Boundary

```text
diagonal residual positivity                   INSUFFICIENT EXACTLY
causal-only fixed-scale family                  INCOMPLETE
causal+anti-causal without the bridge           CODIMENSION ONE TOO SMALL
full two-Hardy-channel plus bridge Gram          COMPLETE FORM CORE
conservative source/output polarization          OPEN / RH-EQUIVALENT
Riemann Hypothesis                               UNPROVED
```
