# Logarithmic one-node annular Green continuation

## Freeze

```text
main:        b837c12199dd407116f604ce6c938039d1a76da4
parent PR:   #413
parent head: 3ba7021d4ed2aa0f42e42917114be06510919bac
branch:      research/gpt56-pro/91520-log-annular-green
```

## Result

The model-side crossed-zero telescope has been converted from a weighted
nonlinear recurrence into an additive Green-potential ledger.

For the fixed node `eta`, define

```text
Lambda_a(eta)=-2 log |B_a(eta)|.
```

Then every dyadic annulus contributes one nonnegative scalar and

```text
Lambda_(a_J)(eta)
 =sum_(j<=J) Lambda_(a_j,a_(j-1))^ann(eta).
```

No inherited factor from earlier annuli remains.

Each crossed zero coordinate `zeta=x+i y` contributes exactly

```text
log [((eta+x)^2+y^2)/((eta-x)^2+y^2)]
```

and at `eta>x` this is the Green-Laplace integral

```text
4 int_0^infinity exp(-eta t) sinh(x t) cos(y t) dt/t.
```

The contribution has the explicit lower moat

```text
4 eta x / [ (eta+x)^2+y^2 ].
```

## New target

The parent ONAIE route asked for one-node Hilbert norm exhaustion. The new
`LONAIE_j` target asks only for a source-ordered log-determinant identity per
annulus. Because the model log mass is additive, it matches the multiplicative
Euler/Jordan/Xi source architecture more naturally.

The exact remaining theorem is still not scalar positivity. A one-node source
value does not determine the denominator Blaschke factor; an explicit control
constructs two distinct factors with the same modulus at the chosen node.
The arithmetic source-to-model factorization remains load bearing.

## Exact state

```text
additive annular log telescope                EXACT
zero-by-zero Green potential                  EXACT
quantitative fixed-node moat                  EXACT
one scalar value determines hyperbolic factor FALSE
source-ordered logarithmic exhaustion         OPEN / RH-BEARING
Riemann Hypothesis                            UNPROVED
```
