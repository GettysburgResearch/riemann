# Elementary Lagarias–carry checkpoint — 2026-08-08

Status: `FULL ELEMENTARY SYNTHESIS / RH UNPROVED`  
Issue: #245  
PR: #248

## Executive result

The branch now contains a complete, reviewer-auditable elementary equivalence
triangle and several new native proofs:

```text
Lagarias harmonic divisor inequality
<=> one-dimensional CA threshold-count inequality
<=> critical ordinary-prime ramp
<=> finite signed carry-block certificate
<=> RH.
```

The finite geometry has been closed. The remaining statement is one explicit
arithmetic scalar, not an omitted matrix estimate or an invitation to the
reviewer to supply a proof.

## Paper import

Imported from Jeffrey C. Lagarias, arXiv:math/0008177:

```text
sigma(n) <= H_n + exp(H_n) log H_n  for every n>=1
<=> RH,
```

with equality only at `n=1`, and with the Robin/colossally-abundant dependency
boundary stated explicitly.

Native wrappers and extensions:

- `T-24502`, `L-24506`, `O-24502`;
- literature and integration notes;
- `L-24521`, exact CA exponent-increment slope ordering;
- `L-24522`, exact threshold counting function and layer cake;
- `T-24505`, one-dimensional CA counting equivalence.

## Native carry proofs

### Exact convexification

`L-24501` proves

```text
Delta^2[(n+1)G_n]=(n-1)log(n/(n-1)),
Delta^2[(n+1)beta_(nq)]
 =(n-1)(1_(q|n)-1_(q|n-1)).
```

The resulting divisor-gradient LP has the exact von Mangoldt dual.

### Critical seed

`L-24502` constructs

```text
b0(m)=2 sqrt(m)[log(X/m)-2(1-sqrt(m/X))]
```

with objective `4 sqrt(X)-O(log X)`.

### Outer and continuum analysis

- `L-24507`: seed feasibility for `q>=X/28` beyond an explicit threshold;
- `L-24514`: a continuum objective-4 pointwise minorant is uniquely the
  smoothed Möbius profile;
- `L-24515`: fixed-ratio harmful affine prime edges have upper-sieve density
  `O(X/log^2 X)`;
- `L-24516`: exact prime-power cube budget and short-run theorem.

### Prime-only reduction and exact transport

`L-24517` proves

```text
S_X-P_X=O(log^2 X)
```

and removes higher prime powers from the final problem.

`L-24520` proves that the direct block

```text
delta b_m=-t 1_(A<m<=B)
```

between two ordinary primes changes exactly those two prime constraints and
pays `t log(B/A)`. Hence every finite ordinary-prime residual is explicitly
transportable.

`X-24503` replays this algebra with exact rational arithmetic.

## Corrections and refutations

- `R-24501`: nonnegative divisibility covering costs order `sqrt X`;
- `L-24508`: positivity of `b_m` is not required;
- `R-24502`: generic Green energy retains the exact logarithmic RH mode;
- `R-24503`: the old `q+1` repair sign is reversed;
- `L-24518`: a flow plateau transports endpoint jumps, not pure incidences;
- `T-24501`: original Jacobi PNC architecture is superseded.

## Colossally abundant slope ledger

For exponent increment `a->a+1` at prime `p`,

```text
I_(p,a)=(1-p^(-a-2))/(1-p^(-a-1)),
kappa_(p,a)=log I_(p,a)/log p.
```

CA integers are exact prefixes sorted by decreasing `kappa`.
For threshold `epsilon`,

```text
A_p(epsilon)
=#{m>=1: p^m < (p^epsilon-p^-1)/(p^epsilon-1)},
X(epsilon)=sum_p A_p(epsilon)log p,
M(epsilon)=integral_epsilon^infinity X(t)dt.
```

The complete normalized divisor ratio is

```text
epsilon X(epsilon)+M(epsilon).
```

Thus the Lagarias criterion becomes one explicit one-dimensional inequality at
every slope threshold and tie.

## Exact remaining scalar

Any one of the following completes the branch:

```text
P_X >= 4 sqrt(X)-X^o(1),
```

```text
sigma(n) <= H_n+exp(H_n)log H_n for every n,
```

or

```text
Phi(X(epsilon))
 >= epsilon X(epsilon)+integral_epsilon^infinity X(t)dt
```

for every CA threshold.

The branch proves these are equivalent and proves all finite adapters between
them. It does not prove the scalar itself.

## Why no stronger claim is made

A monotone cover, a generic positive Gram, a smooth objective-4 seed, local
prime transport, and naive descending repair were each tested. Where false,
they were refuted exactly. Where correct, their optimum was shown to be the same
RH-bearing scalar. Relabeling that scalar as a norm or contraction would be
circular.

## Recommended adversarial review order

1. Lagarias/Robin import boundary;
2. `L-24501/L-24502`;
3. `L-24507/L-24508/L-24514/L-24517`;
4. `R-24501/R-24502/R-24503`;
5. `L-24518/L-24519/L-24520` and `X-24503`;
6. `L-24521/L-24522/T-24505`;
7. `T-24504`;
8. final scalar.
