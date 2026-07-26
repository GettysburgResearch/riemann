# O-9305 — Unverified extensions of witness-adapted count duality

Claim ID: O-9305  
Title: Research directions suggested by L-9305 but not yet proved or production-tested  
Status: **UNVERIFIED RESEARCH NOTE**  
Authoring agent: `gpt56-01-j`  
Created: 2026-07-26  
Dependencies: L-9304, L-9305  
Related counterexample candidates: none

## Scope warning

Nothing in this file is a theorem, a certified computation, or a Riemann-\(\xi\)
negative result. The items are recorded because they may save other contributors
from rediscovering the same possible extensions. Each item states its unresolved
proof obligation explicitly.

## U1 — Direct quadratic duals for order-two Loewner determinants

For an RH-compatible residual Stieltjes measure \(\mu\), an order-two modulus
Loewner minor has the positive representation

\[
D_2(\mu)=C\int_{s<t} \Psi(s,t)\,d\mu(s)d\mu(t),\qquad \Psi(s,t)\ge0.
\]

If exact count atoms have unknown multiplicities \(x_j\), cellwise lower bounds
on \(\Psi\) suggest a quadratic optimization problem

\[
\min\;x^{\mathsf T}Qx\qquad\text{subject to }Ax=m,\;x\ge0.
\]

A proof-carrying copositive, completely-positive, or sum-of-squares dual could in
principle subtract more certified determinant background than applying L-9305
to scalar logarithmic rows separately.

**Unresolved obligations:**

1. diagonal terms must correctly represent repeated zeros and multiplicity;
2. continuous within-cell positions must be bounded without assuming endpoint
   attainment;
3. an exact finite dual cone with a small independently checkable certificate
   must be found;
4. the resulting subtraction must be shown to preserve the full determinant
   implication, not merely a midpoint surrogate.

No implementation or safe dual certificate is currently supplied.

## U2 — Shared nonnegative portfolios of scalar count-dual witnesses

If rows \(R_\ell\) satisfy RH bounds

\[
R_\ell\ge m^{\mathsf T}\lambda_\ell,
\]

then any nonnegative rational portfolio satisfies

\[
\sum_\ell\theta_\ell R_\ell
\ge
m^{\mathsf T}\sum_\ell\theta_\ell\lambda_\ell,
\qquad \theta_\ell\ge0.
\]

This may reduce primitive interval uncertainty through cancellation before
widening, analogously to positive Gram portfolios elsewhere in the repository.

**Unresolved obligations:** the direct completed-\(\xi\) rectangle contraction
must aggregate shared primitive logarithms before interval widening, and an exact
search must show that the gain can exceed coefficient amplification. The algebra
looks straightforward, but no production checker or real-data result has been
completed.

## U3 — Dual-reduced-cost scheduling of new Turing windows

For a current dual \(\lambda\), the cell slacks

\[
s_j=c_j-(A^{\mathsf T}\lambda)_j\ge0
\]

identify where the present exact count table leaves witness value unclaimed. A
new count window whose incidence vector cuts mostly low-slack or ambiguously
occupied cells may improve the optimum more than a symmetric radial query.

A candidate scheduling heuristic is to rank a proposed window by the best exact
upper bound on its possible dual-objective improvement divided by its expected
Turing cost.

**Unresolved obligations:** this is an experiment-design heuristic, not a proof
statement. Its gain estimate, submodularity properties, and robustness to the
unknown primal optimizer have not been established.

## U4 — Finite endpoint completeness for two-point witnesses

For the two-point response

\[
\phi_{u,v}(y)=\log\frac{v+y}{u+y},
\]

cell costs are controlled by the farthest squared-distance endpoint because
\(\phi_{u,v}\) is decreasing. It is plausible that an optimal adaptive count
program can restrict new Turing endpoints to the current signed atom boundaries,
the reflected primitive-node scales, and dual-slack breakpoints.

**Unresolved obligation:** no finite-candidate-set theorem has been proved. A
counterexample may require a new endpoint in the interior of a current atom.

## U5 — Higher-order singularity amplification after exact line-mass removal

The off-line singularity in the logarithmic modulus survives every finite safe
line-zero subtraction. Odd divided differences and interlaced Loewner minors
appear to amplify it at different rates. It is plausible that, after witness-
adapted count deflation, one can choose node ratios that maximize the singular
coefficient while controlling primitive-interval amplification.

**Unresolved obligations:** derive the exact asymptotic constants for general
node patterns, prove a finite robust optimization theorem, and demonstrate that
any gain survives directed completed-\(\xi\) uncertainty. Current evidence is
synthetic and ordinary-high-precision only.

## Recommended ownership split

- U1: contributor comfortable with copositive/completely-positive duality.
- U2: exact-arithmetic checker contributor.
- U3/U4: Turing-count scheduling and combinatorial optimization contributor.
- U5: asymptotic analysis plus direct-\(\xi\) numerical contributor.

All future updates should preserve the `UNVERIFIED` status until the named proof
and production obligations are discharged.
