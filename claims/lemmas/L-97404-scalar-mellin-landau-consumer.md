# L-97404 — Complete Mellin–Landau consumer for the 5:3 scalar

Claim ID: `L-97404`  
Status: **PROVED EXACT CONDITIONAL ANALYTIC THEOREM**  
Created: 2026-08-18  
RH status: conditional on eventual nonnegativity of the scalar

Define

`R_X=5c_X(2)+3c_X(3)`.

The unsieved coefficient dictionary is

```text
q_*(1)=0,
q_*(2)=15,
q_*(3)=6,
q_*(4)=3,
q_*(m)=6 for m>=5.
```

After Möbius convolution,

`R_X=sum_(n<=X) a_*(n)n^(-1/2)log(X/n)`,

where

`a_*(n)=6 1_(n=1)-6mu(n)+9 1_(2|n)mu(n/2)-3 1_(4|n)mu(n/4)`.

Every hinge is locally integrable and continuous at activation: the entering logarithmic term is zero at `X=n`. The elementary bound `|a_*(n)|<=24` gives

`|R_X| <= 24 log X sum_(n<=X)n^(-1/2) <= 60 sqrt(X)(1+log X)`

for `X>=2`. Hence the Mellin integral converges absolutely for `Re s>1/2`.

## Exact transform and the substitution factor

For `Re s>1/2`, Fubini is justified by the displayed growth bound. The substitution `X=kY` in a Möbius term contributes

`k^(-s-1/2)`,

not `k^(-s)` and not `k^(-s-1)`. Writing `z=s+1/2`, one obtains

`int_1^infty R_X X^(-s-1)dX`

`=6/s^2 - 3(1-2^(-z))(2-2^(-z))/(s^2 zeta(z))`.

The constant `6/s^2` is the unit-source term. The formula gives meromorphic continuation to `Re s>0`.

## Positive real axis

For real `s>0`, `z=s+1/2` is real and greater than `1/2`. Zeta has no real zero there. At `z=1`, the reciprocal `1/zeta(z)` vanishes, so the quotient is removable. The factor `s^(-2)` has no singularity on the positive real axis. Thus the continued transform is analytic at every real `s>0`.

## Pole survival

The finite numerator

`N(z)=-3(1-2^(-z))(2-2^(-z))`

is zero-free in `Re z>0`: there `|2^(-z)|<1`, so it is neither `1` nor `2`. If `rho` is a zeta zero of arbitrary multiplicity `m` with `Re rho>1/2`, then the transform has a nonremovable pole of order `m` at `s=rho-1/2`.

## Landau after logarithmic change of variable

Put `X=e^t` and `f(t)=R_(e^t)`. If `R_X>=0` for all sufficiently large `X`, discard the finite initial interval. The Laplace transform of the remaining nonnegative locally integrable function differs from the Mellin transform by an entire function.

Landau’s theorem says that the finite real abscissa of convergence of a nonnegative Laplace transform is a singularity unless the transform continues farther left. Since the continuation is analytic at every positive real `s`, the abscissa is at most zero. The defining transform is therefore holomorphic throughout `Re s>0`.

A zero `rho` with `Re rho>1/2` would give a nonremovable pole inside that half-plane, contradiction. The functional equation reflects the conclusion and places every nontrivial zero on `Re rho=1/2`.

```text
coefficient dictionary              PROVED EXACT
growth and Fubini region             PROVED EXACT
k^(-s-1/2) factor                    PROVED EXACT
6/s^2 term                           PROVED EXACT
positive-axis removability           PROVED EXACT
arbitrary-multiplicity pole survival PROVED EXACT
Landau composition                   PROVED CONDITIONAL
```
