# T-107100 Xi reverse–Rolle execution — five-minute handoff

Status: **exact real descent theorem proved; Xi complex transport and RH open**

Parent programme: PR #714 at `d1a9fea34aa0620a5cb2da41061518638ab8b219`.

## Read in order

1. `claims/lemmas/L-107100-exact-multiplicity-sensitive-reverse-rolle.md`
2. `claims/lemmas/L-107101-laguerre-curvature-nonreal-zero-pair-budget.md`
3. `claims/theorems/T-107100-exact-xi-reverse-rolle-defect-cascade.md`
4. `claims/refutations/R-107100-derivative-line-concentration-alone-does-not-descend.md`
5. `standalone/2026-08-30-xi-reverse-rolle/REVIEW_SPECIFICATION.md`

## Exact result

For every real analytic parent `f`, with multiplicities and interval endpoints retained,

```text
N_I(f) = N_I(f') - R_I(f) + epsilon_I(f).
```

A local derivative zero of multiplicity `r` and logarithmic-derivative orientation `iota` contributes

```text
r+iota.
```

A simple ordinary Rolle extremum costs `0`; a simple wrong-sign extremum costs `2`.

For `F_k=Xi^(k)`,

```text
N_0(I)
 = N_m(I)
   - sum_(k<m) R_k(I)
   + sum_(k<m) epsilon_k(I).
```

## New complex dictionary

```text
Q_f = - (f'/f)' = sum_rho 1/(x-rho)^2.
```

Real zeros contribute positively. One nonreal conjugate pair at height `b` has exact negative-curvature mass `2/b`.

## Live target

```text
XICURV107110:
  turn the continuous nonreal-pair curvature budget into a summable discrete
  extra-extremum defect using Xi-specific depth/separation and Pick/Loewner
  information.
```

## Boundary

```text
real reverse-Rolle target             CLOSED
complex Xi defect transport           OPEN
growing-order derivative theorem      OPEN
Riemann Hypothesis                     UNPROVEN
```
