# M-15407 — Cumulative Weyl / Green-lift positive programme

Claim ID: `M-15407`  
Title: Prove the physical Green quotient identity, not a new global Toeplitz estimate  
Status: `PROPOSED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-01  
Dependencies: `L-15421`--`L-15424`, `T-15409`  
Scope: final positive route for Issue #180  
Related counterexample candidates: none

## Strategic reduction

The desired positive conclusion no longer needs to be attacked as a direct
uniform lower-singular-value estimate for an infinite Toeplitz family.
The exact chain is

```text
physical Green quotient / branch domination
    -> cumulative original Weyl positivity
    -> positive de Branges kernel
    -> inner scattering symbol
    -> T_omega^* T_omega = I.
```

The terminal coercivity constant would therefore be the exact value `eta=1`.

## Gate 1 — independent normalization audit

Reconstruct `L-15421` from the chosen Fourier convention and verify:

1. `E_omega(z)=Xi(z+i omega)`;
2. the denominator orientation `2 pi i (bar(w)-z)`;
3. the coordinate variables `s=(a+b)/2`, `d=(a-b)/2`;
4. the exact factor
   ```text
   partial_omega D_tilde_omega = (4/pi) K_omega^W.
   ```

This is a symbolic audit. No zeta zeros or numerical quadrature are needed.

## Gate 2 — quotient-to-original Weyl binding

Starting from the normalized Volterra branch features, prove one exact closed
form identity

```text
< f, K_omega^W f >_physical
 = Q_omega(f)
```

on a common form core, with closure in the physical Weyl metric. A mere
finite-dimensional congruence or bounded condition number is insufficient.

Every kernel division by `Psi(s)Psi(t)` must be accompanied by the exact
multiplication map and its domain/range metric.

## Gate 3 — endpoint branch energy

Use `L-15422` rather than pointwise horizontal monotonicity:

```text
integral_0^omega Q_u(f) du
 = 1/2 ( ||M_+(omega)f||^2 - ||M_-(omega)f||^2 ).
```

Prove only the endpoint inequality

```text
||M_-(omega)f|| <= ||M_+(omega)f||.
```

Temporary negative derivative layers are allowed.

## Gate 4A — Green-minimal quotient route

Represent the branch map as

```text
T_branch = C K E,
C E = I,
|K| <= 1.
```

Prove that the physical branch norm is exactly

```text
||y||_physical = inf_(C h=y) ||h||_lift.
```

Then `L-15423` makes endpoint contraction automatic by data processing.

Equivalent proof object:

```text
E^*(C^*C-K^*C^*C K)E >= 0
```

with all adjoints taken in the declared physical and lifted metrics.

## Gate 4B — Jordan-divisor route

Independently derive the same branch map from Suzuki's positive generalized
Jordan transition

```text
P_omega(n,d)=J_(2 omega)(d)/n^(2 omega),  d|n.
```

The discrete carré du champ is exact. The remaining task is an isometric
Mellin/continuum intertwiner carrying the Jordan conditional expectation to the
Volterra Green-minimal lift, including the archimedean kernel.

Agreement of routes 4A and 4B would give a strong normalization mutation check.

## Gate 5 — exact closure

After cumulative Weyl positivity, invoke only standard de Branges/Hardy facts:

```text
D_omega >= 0
 -> E_omega^#/E_omega is Schur;
unit boundary modulus
 -> inner;
inner
 -> H_omega=0 and T_omega^*T_omega=I.
```

No finite offset grid, compactness passage, or limiting norm inference enters.

## Proof-producing finite programme

1. Choose rational spline/test-function cores in the original coordinate Weyl
   form.
2. Evaluate both the coordinate kernel and the normalized Volterra form with
   directed boxes.
3. Produce an exact finite congruence candidate and a residual operator radius.
4. Compute the physical and quotient Grams independently.
5. Search for an exact symbolic kernel identity suggested by the finite data.
6. Test the Jordan transition against the same finite branch Gram.
7. Promote only after the residual radius is identically zero or has a symbolic
   closed-form proof.

## Fail-closed rules

- A numerical near-isometry is not a metric identity.
- `|kappa|<=1` before Volterra integration is not a physical output
  contraction without the quotient theorem.
- Norm equivalence with condition number greater than one does not preserve a
  sharp contraction constant one.
- The latest Volterra quotient certificate may be used only after its original
  Weyl-form binding is reconstructed.
- No RH-conditional zero expansion may enter Gates 1--4.

## Smallest blocker

The smallest surviving statement is

\[
 \boxed{
 \|y\|_{\rm physical}^2
 =\inf_{Ch=y}\|h\|_{\rm lift}^2
 }
\]

for the complete branch range, or equivalently the compressed Green
commutator LMI in `L-15423`. Everything after it is now an exact transfer.
