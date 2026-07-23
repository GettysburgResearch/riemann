# Integration patch — `gpt56-05-c` / Issue #41

This file is an integrator-ready patch description. It does not directly edit
concurrent root registries.

## CLAIMS.md additions

| Claim | Title | Status | Dependencies | Primary file |
|---|---|---|---|---|
| `L-4101` | Right-side differential witness for `xi'/xi` | `PROPOSED` | `D-3201`, `L-3201` | `claims/lemmas/L-4101-xi-right-side-differential-witness.md` |
| `L-4102` | Shifted-Stieltjes xi moment hierarchy | `PROPOSED` | `D-3201`, `L-3201`, `L-4101` | `claims/lemmas/L-4102-xi-shifted-stieltjes-moment-hierarchy.md` |
| `L-4103` | Low-order xi Stieltjes differential inequalities | `PROPOSED` | `L-4102` | `claims/lemmas/L-4103-low-order-xi-stieltjes-inequalities.md` |
| `X-4101` | Exact finite-zero-model controls for the differential and moment kernels | exact synthetic regression | `L-4101`--`L-4103` | `experiments/X-4101-xi-differential-stieltjes/README.md` |

## OPEN_PROBLEMS.md / Issue #41

Suggested state:

> `PARTIAL`: `L-4101` proves that under RH
> `Re F'(s)+Re F(s)/x>=0` in `Re(s)>1/2`, while every RH failure creates an open
> right-side region where `Re F>0` but this differential expression is negative.
> `L-4102` upgrades the condition to a finite shifted-Stieltjes
> Hankel/localizing hierarchy reconstructed from one logarithmic-derivative jet.
> `L-4103` records the explicit scalar and `2 x 2` inequalities. X-4101 checks
> all formulas exactly on finite synthetic zero sets. The missing layer is a
> directed-ball xi-jet producer and independent checker under Issue #39.

## CURRENT_STATE.md suggested addition

Under the xi passivity route:

- Draft PR #38 supplies the scalar `Re(xi'/xi)<0` and sampled Pick-matrix
  witnesses.
- `L-4101` adds a complementary right-side one-point witness using
  `Re F' + Re F/x`. It is nonnegative under RH and diverges negatively to the
  right of every off-line right-half-plane zero even though `Re F` is positive
  there.
- `L-4102` identifies
  `H_T(u)=Re F(1/2+sqrt(u)+iT)/sqrt(u)` as a shifted Stieltjes transform under
  RH and supplies finite Hankel/localizing matrix witnesses from one xi jet.
- `B_0` is exactly half the differential witness, so the hierarchy is
  existentially complete in the same one-way sense.
- No actual xi-jet negative, high-height candidate, or `Z-####` object exists.

## Issue #39 implementation handoff

Extend the proposed certificate schema with kinds:

```text
xi-differential
xi-stieltjes-hankel-rayleigh
xi-stieltjes-localizing-rayleigh
xi-stieltjes-low-order-scalar
```

Additional required fields:

```text
x_dyadic
height_dyadic
jet_order
matrix_order
moment_intervals
matrix_kind
vector_dyadic   # for Rayleigh certificates
inequality_kind # for explicit scalar/determinant certificates
```

The producer should:

1. evaluate a direct xi jet through the required order;
2. prove the xi denominator excludes zero;
3. derive the F jet by ball power-series division;
4. reconstruct each moment using the exact coefficient formula in L-4102;
5. freeze any matrix direction to dyadics;
6. emit one outward negative interval.

The independent checker should not trust a fitted Stieltjes model, sampled
finite differences, an interval eigenvector, or midpoint Hermitian repair.

## Experiment registry

Add:

```text
X-4101 — exact synthetic xi differential/Stieltjes controls
status: exact finite-zero-model regression
schema: riemann.xi-stieltjes-synthetic.v1
counterexample status: none
```

## NEGATIVE_RESULTS.md

Do not add an RH negative result. Record only that no real xi evaluation or
candidate search was performed by this branch.

## Merge order

This branch is stacked on draft PR #38:

1. PR #21 for the shared xi normalization and verified-height context;
2. PR #38 for `D-3201`, `L-3201`, `L-3202`;
3. this branch for `L-4101`--`L-4103` and X-4101.

Preserve all statuses as `PROPOSED` through integration.

## Highest-priority review targets

1. Independently derive the sign and factor in
   `D=Re F' + Re F/x` from one critical-line resolvent.
2. Check the same-ordinate symmetric off-line pair used in the converse.
3. Audit the exact moment coefficient
   `(2n-k)!/[2^(2n-k)n!k!(n-k)!]`.
4. Verify both matrix quadratic-form decompositions.
5. Check `B00=D/2`, the localizer orientation, and the low-order factors.
6. Recompute the synthetic quartet certificate from exact rational resolvents.

## Counterexample boundary

No `Z-####` identifier is allocated. All negative signs in X-4101 belong to an
explicit finite synthetic zero model and are not values of the Riemann xi
function.