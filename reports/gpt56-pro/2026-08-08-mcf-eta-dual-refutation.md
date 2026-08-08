# MCF eta-dual refutation

## Frozen target

This pass reviews and attacks the Mersenne-Collar Fragmentation theorem in PR #285 frozen at

```text
61d0b66196f308981d36dbb8723d5e64d7a27533
```

The frozen proposal correctly derives the eta inverse source and the exact pointwise carry sign

```text
Y_n(j)=2[L(n)-L(j)-L(n-j)]+1.
```

It then asks for exact nonnegative carry saturation using only binary-central-window edges off Mersenne rows and extreme edges on Mersenne rows.

## Result

That eventual support theorem is false.

Define

```text
Phi(1)=0,
Phi(n)=largest_power_of_two_leq(n)-1.
```

Every declared MCF edge has nonnegative defect

```text
Phi(n)-Phi(j)-Phi(n-j)>=0.
```

The associated divisor coefficient has Dirichlet series

```text
A(s)=2^(-s)/eta(s).
```

Therefore exact MCF feasibility at endpoint `X` forces the finite scalar

```text
D(X)=sum_(q<=X) a(q)q^(-1/2)log(X/q)
```

to be nonnegative.

Its exact Mellin transform is

```text
int_1^infinity D(X)X^(-z-1)dX
 =2^(-(z+1/2))/[z^2 eta(z+1/2)].
```

The denominator has nonreal dyadic poles at

```text
z=1/2+2 pi i k/log 2,  k!=0,
```

but no positive-real singularity. Piecewise-linear interpolation of the integer endpoint values changes the transform only by a function holomorphic in `Re z>-3/2`.

If MCF held for every sufficiently large integer endpoint, the interpolation would be eventually nonnegative. Landau's one-sign theorem would force a singularity at the real abscissa of convergence. The nonreal poles force that abscissa to be at least `1/2`, while the explicit transform is regular at every positive real point. Contradiction.

The same argument applied to the negative scalar proves that the dual value takes both signs arbitrarily far out.

## Structural meaning

The Mersenne menu is adapted to the eta source, but that adaptation imports the factor

```text
1/(1-2^(1-s)).
```

Its nonreal zeros on `Re s=1` are a deterministic cofinal obstruction before any hypothetical zeta zero is considered.

The Mersenne collar is therefore not merely an `O(log X)` boundary which can be paid independently. A valid positive-flow proof must include parity/exterior edges whose dual action cancels the eta factor before invoking one-sign Mellin theory.

## Exact scope

```text
eta inverse and pointwise Mersenne localization       retained
finite MCF feasibility at isolated endpoints          not contradicted
MCF for all sufficiently large endpoints              refuted
MCF as an RH proof                                     rejected
support-flow recursion of PR #295                      cannot close cofinally as stated
unrestricted carry saturation                          open
parity-paired physical route                           open
RH                                                     unproved
```

## Review order

1. `claims/lemmas/L-28501-dyadic-mcf-dual-and-mellin-transform.md`
2. `claims/refutations/R-28501-eventual-mersenne-collar-fragmentation-is-false.md`
3. `experiments/X-28501-mcf-eta-dual/verify.py`
4. frozen PR #285 `L-28002/T-28001`
5. the standard Mellin-Landau theorem.

The refutation is complete as written. Reviewers are not asked to construct a missing repair theorem.
