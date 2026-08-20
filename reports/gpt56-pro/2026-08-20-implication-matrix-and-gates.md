# Implication-matrix pass: opposite owners, two witness classes, and the exact frontier

## Executive result

This pass did not find a valid full proof of RH.  It did find a genuinely new
composition that is more informative than another list of RH-equivalent
criteria:

1. sequential first ownership and reverse largest ownership are opposite
   triangularizations of one Euler source;
2. together they produce an exact min--max interval tensor and a convex joint
   hazard law;
3. centered quadratic/cubic geometry confines every possible negative point to
   two disjoint witness classes;
4. those two classes form an exact logical AND gate to the quadratic envelope
   and hence to RH.

The two witness classes are:

```text
AEP100612: every downward positive-parity activation endpoint is nonnegative;
DNT100612: every double-negative interior cell obeys its 2x2 Turan determinant.
```

They are exhaustive and logically independent.  Thus

```text
AEP100612 AND DNT100612 -> E2>=0 -> Mellin-Landau -> RH.
```

The final two arithmetic estimates remain unproved on long mixed actual-prime
collars.

## The unexpected connection

The first-owner and largest-owner programmes were previously treated as
competing decompositions.  Algebraically they are complementary:

```text
least selected prime  = row coordinate;
greatest selected prime = column coordinate;
interior selected primes = interval Euler packet.
```

Every nonempty Euler monomial belongs to one and only one `(least,greatest)`
cell.  The hazard coefficient

\[
\pi_{ij}=r_ir_jL_iR_j
\]

is exactly the probability that independent Bernoulli labels have minimum
success `i` and maximum success `j`.  This supplies one physical joint measure,
not two independently chosen marginals.

The resulting scalar decomposition has positive root and singleton channels.
Every possible sign loss is therefore an interval-collar loss.

## Important correction during the pass

The first draft split the joint coefficient into row and column Schur
marginals.  That split was too strong.  At `X=1`, for every fixed early owner
`i`, the centered interval entry approaches a nonzero limit as the greatest
owner tends to infinity, whereas the proposed row marginal contains

\[
\sum_jp_j^{-1/4}.
\]

It diverges.  `R-100616` proves this exactly.

The corrected object keeps both outside survivals until after a collar
factorization.  If a single collar occurrence has left and right certificates
`A_ij,B_ij`, then

\[
(H_{ij})_-^2\le A_{ij}B_{ij}
\]

and joint Cauchy--Schwarz gives

\[
F_-\le
\sqrt{
\left(\sum\pi_{ij}A_{ij}\right)
\left(\sum\pi_{ij}B_{ij}\right)
}.
\]

This is a real AND gate: both estimates refer to the same occurrence and
neither independent marginal is sufficient.

## Why the activation/Turán pair is the preferred concrete gate

PR #679's cell calculus reduces the quadratic envelope to

\[
E(x)=16\overline S_{3/2}
+24x^{-1/2}S_1
-9x^{-1}S_{1/2}.
\]

Every cell minimum is either:

1. a downward activation endpoint, or
2. the unique double-negative critical point
   \[
   x_*=(3S_{1/2}/4S_1)^2,
   \]
   whose sign is the determinant inequality
   \[
   S_1^2+\overline S_{3/2}S_{1/2}\le0.
   \]

There is no third witness type.  This turns a diffuse global sign problem into
two structurally different arithmetic obligations.

The repository already attacks the two sides with different machinery:

```text
activation endpoints:
  largest-prime ownership, finite critical squaring, terminal corridors;

interior Turan points:
  first-owner moments, complex shifted-square positivity, interval Gram.
```

This explains why neither line closed alone and why their conjunction is the
natural next integrator.

## Proved regions

The matrix now closes:

- root and singleton channels;
- empty-interior cells;
- endpoint ratios at most eight;
- the asymptotic interval sector `p_j<=p_i^A`, `A<exp(3/4)`;
- every fully active interval;
- finite-completion low-prime corridors;
- hereditary terminal sectors on their native Dickman states.

Only long mixed activation collars survive all of these filters.

## Exact scientific boundary

```text
first-owner identity                     proved
largest-owner identity                   proved
double-owner tensor                      proved
joint min-max hazard                      proved
root/singleton positivity                proved
carrier and short-region positivity      proved
cell witness classification              proved
AEP AND DNT -> envelope sign              proved
envelope sign -> RH                       proved
AEP on long mixed collars                 open
DNT on long mixed collars                 open
Riemann Hypothesis                        unproved
```

The implication matrix is therefore useful but not a completed proof.  The
next attack should not introduce another scalar detector.  It should construct
one source-faithful collar occurrence with both a least-owner and a
greatest-owner certificate, or prove the endpoint and Turán witness classes
separately and then invoke `T-100612`.