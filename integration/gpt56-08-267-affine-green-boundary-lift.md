# Integration handoff — affine Green boundary lift

Branch family: `267-affine-green-boundary-lift`

## New objects

```text
L-26701  exact affine oversupport positivity lift
L-26702  least-charge minimax, monotone-additive dual, Green/dipole bridge
T-26701  ABLC-to-RH proposal
R-26701  scope boundaries
M-26701  production protocol
O-26701  floating canonical-charge reconnaissance
X-26701  exact rational regression
```

## Cross-branch map

- PR #248 supplies the parabolic seed, carry response, objective, and canonical
  endpoint-projected Green solve.
- PR #252 supplies the continuum resolvent interpretation.
- PR #254 supplies the signed constraint-dipole flow.
- PR #257 identifies DCRS/Greedy Slack/common carry state and recommends a
  positivity-preserving deformation.
- PR #265 supplies a positive endpoint scale frame and continuum defect-tail
  majorization.

The new construction composes them as

```text
canonical signed Green equality
or dipole-assisted feasible deformation
-> maximum benchmark deficit C_X
-> prime oversupport affine lift
-> nonnegative finite certificate
-> prime ramp loses only C_X log X.
```

## Recommended review order

1. `L-26701`
2. `X-26701`
3. `L-26702`
4. `R-26701`
5. `T-26701`
6. `M-26701`
7. `O-26701`
8. report
9. inherited PR #248 prime-ramp consumer

## Exact frontier

Prove
\[
\mathcal C_X=X^{o(1)}
\]
or the stronger canonical estimate
\[
C_X^G=X^{o(1)}.
\]

A dipole-assisted proof may certify a different feasible vector and need only
bound its maximum downward displacement. It does not have to prove zero slack,
full Green-energy control, or a separate low-cost flow theorem.
