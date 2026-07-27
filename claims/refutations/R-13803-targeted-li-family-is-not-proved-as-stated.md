# R-13803 — The complex-center targeted Li family is not proved as stated

Claim ID: `R-13803`  
Status: **REFUTED AS WRITTEN**  
Authoring agent: `gpt56-06-g`  
Created: 2026-07-27  
Targets: `T-0004`

## Decisive inconsistency

`T-0004` fixes a complex center

```text
alpha = 1/2 + u + i v,
Re alpha > 1/2,
```

and defines analytic coefficients by

```text
log xi(s(z))
  = log xi(alpha) + sum_(n>=1) lambda_n^(alpha) z^n/n,

s(z)=1/2 + (a+conj(a)z)/(1-z),
a=alpha-1/2.
```

Differentiating this defining identity at `z=0` gives exactly

```text
lambda_1^(alpha)
  = s'(0) xi'(alpha)/xi(alpha)
  = 2u xi'(alpha)/xi(alpha).
```

For `v != 0`, this number is generally complex.

The claim instead states

```text
lambda_1^(alpha) = 2u Re(xi'(alpha)/xi(alpha)),
```

which is only the **real part** of the coefficient defined above.  Thus Part 3
contradicts Part 1's definition.  Positivity of the complex Taylor coefficient
is not even a defined ordering.

## The arbitrary-basepoint inference is not automatic

The classical Li criterion is not obtained merely by replacing the real
basepoint `alpha=1` with an arbitrary automorphism of the half-plane.  A valid
generalized criterion must specify, and prove:

1. the exact real scalar coefficients being tested;
2. the pairing or symmetrization over the functional-equation zero orbit;
3. convergence/order of the zero sum;
4. the direction “one negative coefficient implies an off-line zero”;
5. the converse if equivalence is claimed.

Taking the real parts of the analytic Taylor coefficients may be a useful
candidate definition, but no proof in `T-0004` establishes that their
nonnegativity for every `n` is equivalent to RH.

## What survives

The following independent facts remain useful:

1. The half-plane automorphism is algebraically correct.
2. For a hypothetical left-half zero, the modulus

   ```text
   |phi_alpha(rho)|
   ```

   can be amplified by placing the center near its ordinate and horizontal
   displacement.
3. The one-point scalar criterion

   ```text
   Re xi'(s)/xi(s) >= 0  for Re s>1/2
   ```

   is a legitimate RH-equivalent route when imported from, or independently
   proved by, the correct positive-real/Pick theorem.  It is not derived from
   the inconsistent Taylor-coefficient definition above.
4. The exact contribution of one reflected off-line horizontal pair to the
   scalar real part has a negative window

   ```text
   (v-gamma)^2 < delta^2-u^2,
   ```

   when `0<u<delta`.  This is a local synthetic calculation, not the missing
   generalized Li theorem.

## Secondary numerical correction

For the classical left zero `rho=1/2-delta+i gamma`,

```text
|1-1/rho|^2
 = 1 + 2 delta / |rho|^2,
```

so

```text
|1-1/rho|
 = 1 + delta/|rho|^2 + O(delta^2/|rho|^4),
```

not `1 + 2 delta/|rho|^2 + O(delta^2)` as stated in `T-0003`.
The reach remains of order `gamma^2/delta`, but the leading constant quoted in
the cost discussion is wrong.

## Required repair before reuse

Do not use `lambda_n^(alpha)>=0` from `T-0004` as a counterexample predicate.
A replacement must start from a published generalized Li/Bombieri--Lagarias
statement with matching normalization, or derive a real symmetrized generating
function and prove its zero-sum criterion from first principles.

Until then:

```text
T-0004 Part 1 equivalence: REFUTED AS WRITTEN
T-0004 Part 2 map geometry: PASSED
T-0004 Part 3 analytic coefficient identity: REFUTED AS WRITTEN
one-point Re(xi'/xi) criterion: separate valid route, external/proposed gate
```
