# Lagarias import, outer carry proof, and Green-energy audit — 2026-08-07

Status: `PROPOSED / PROOF-BEARING CONTINUATION / RH UNPROVED`  
Issue: #245  
PR: #248  
Frozen base: `d1f72553c73037a3990f8c505d0c260d41a223f4`

## Executive result

This continuation did four things.

1. It imported Lagarias's harmonic-divisor equivalence to RH with its exact Robin dependency boundary and elementary harmonic wrapper.
2. It completed the formerly open fixed-ratio sign step for the parabolic seed: every integer constraint `q>=X/28` is feasible once `X>=104301`.
3. It refuted the proposed monotone Divisibility Cover by an exact positive seed-excess band and a prime-counting disjointness argument.
4. It replaced the first PNC formulation by an endpoint-projected Dirichlet Gram and one explicit Green-energy theorem, while proving that the Green norm retains the exact prime-ramp scalar and therefore is not a source-blind shortcut.

RH remains unproved.

## I. Lagarias claims imported

### Main criterion

For

```text
H_n=sum_(j<=n)1/j,
sigma(n)=sum_(d|n)d,
```

Lagarias proves

```text
RH
iff
sigma(n)<=H_n+exp(H_n)log(H_n)
for every n>=1,
```

with equality only at `n=1`.

The local packet is:

```text
T-24502  imported full equivalence
L-24506  elementary harmonic envelope
O-24502  exact prime-power connection to the carry route
```

### Dependency boundary

The elementary wrapper uses the exact estimates

```text
exp(H_n)log(H_n)>=exp(gamma)n loglog n,
```

and

```text
H_n+exp(H_n)log(H_n)
<=exp(gamma)n loglog n+7n/log n.
```

The global RH content imports Robin's theorems. The source-reported check through `5040` has not been independently replayed on this branch.

### Exact carry connection

For `n=product p^(a_p)`,

```text
log(sigma(n)/n)
=sum_(q=p^r)
 [Lambda(q)/log q] (1-q^(-a_p))/q.
```

Thus Robin/Lagarias and the carry LP are different positive functionals of the same prime-power coordinate system. The colossally-abundant exponent profile is retained as a sparse stress test, not as a proof of the carry theorem.

## II. Outer parabolic seed theorem closed

The parabolic seed is

```text
b0(m)=2 sqrt(m)[log(X/m)-2(1-sqrt(m/X))].
```

For `q/X->theta`, its scaled constraint excess is the reciprocal-cell function

```text
E_N(theta)
=theta^(-1/2)
 [A_N+(H_N+1)log theta+4H_N]-4N.
```

`X-24501` gives an exact rational certificate

```text
max E_N < -1/50
for N=2,...,27.
```

The verifier uses dyadic integer-square-root intervals, atanh-series logarithm bounds, positive Taylor exponential bounds, and exact `Fraction` arithmetic. Its proof-object SHA-256 is

```text
c849273361e1c868fe24d814a078c74181bb11d5ffa1160154a29dd6e1e95521.
```

`L-24507` supplies the uniform finite-difference remainder. The result is

```text
X>=104301,
X/28<=q<=X
=> v_q(b0)<=q^(-1/2)log(X/q).
```

This holds for every integer `q`, not only prime powers.

## III. Monotone cover refuted

A second exact certificate proves

```text
E(theta)>1/10
for 1/40<=theta<=1/32.
```

The proof-object SHA-256 is

```text
428307dd3e0be7647aa660094433e2071c5e67454d534d5b0c9219defabd4cda.
```

The uniform remainder gives

```text
e_X(p)>=1/(20 sqrt X)
```

for every sufficiently large prime `p` in that band. Two distinct such primes cannot divide one integer `m<=X`. Therefore any nonnegative divisibility cover must pay separately for every band prime. The PNT yields

```text
sum_m alpha_m log m >> sqrt X.
```

Hence the former `O(log^2 X)` Divisibility Cover is false.

The exact subtraction identities survive, but the proposed positive cover does not. `O-24501` is retained only as a warning about finite pre-asymptotic LP trends.

## IV. Two proof-boundary simplifications

### Signed convexified coefficients are enough

`L-24508` proves that `b_m>=0` is unnecessary after convexification. For every real vector,

```text
J_X(b)=sum_(q=p^a) Lambda(q)v_q(b).
```

Thus the prime-power inequalities alone imply `J_X(b)<=S_X`. A completed correction need not return to a nonnegative combination of binomial rows.

### Local same-scale clusters are finite and invertible

`L-24511`, imported and sharpened from PR #254, proves:

```text
one direct q-repair
-> only q-1 or q+1 can remain above half scale;
consecutive prime-power clusters
-> length <=3, except {2,3,4,5};
all cluster repair matrices
-> explicit entrywise-nonnegative inverses;
after the joint solve
-> every positive child <=(q+1)/2.
```

This is a genuine local scale descent. It does not by itself control the global signed cost.

## V. Endpoint-projected Dirichlet Gram

For prime powers `q`, define

```text
f_q(j)=1_(q|j)-(j/X)1_(q|X).
```

The matrix

```text
G_X(q,d)=sum_(j=0)^(X-1) Delta f_q(j) Delta f_d(j)
```

is positive definite. If

```text
F_T(j)=sum_d T_d f_d(j),
```

then the corrected constraint vector is exactly

```text
r_X-G_X T.
```

For `lambda_q=Lambda(q)`, the physical profile is

```text
h_X(j)=log j-(j/X)log X,
```

and

```text
lambda^T G_X lambda<=6.
```

Define

```text
Gcal_X=r_X^T G_X^(-1) r_X.
```

Then

```text
S_X>=J_X(b0)-sqrt(6 Gcal_X).
```

This gives the new full proposal `T-24503`:

```text
Gcal_X<=C log^4(2X)
-> S_X>=4 sqrt(X)-O(log^2 X)
-> square-screw/Landau
-> RH.
```

## VI. Green and flow firewalls

The Green theorem is explicit but does not evade the scalar obstruction.

Put

```text
delta_X=J_X(b0)-S_X,
E_X=lambda^T G_X lambda.
```

`L-24510` proves the exact decomposition

```text
Gcal_X
=delta_X^2/E_X
 + orthogonal Green energy.
```

Therefore a subpower Green theorem already contains a subpower prime-ramp theorem.

Likewise, `L-24512` computes the dual of every nonnegative adjacent-flow LP. The choice

```text
y_q=Lambda(q)
```

saturates every flow-coordinate inequality because

```text
2log j-log(j-1)-log(j+1)
=log(j^2/(j^2-1)).
```

Its dual value is exactly `J_X(b0)-S_X`. Hence generic rank, underdetermination, top-half support, or local scale descent cannot prove a cheap flow without using source-specific arithmetic cancellation.

## VII. Current full proposal

The strongest honest elementary architecture on this branch is now

```text
exact carry/binomial second differences
-> signed prime-power divisor-gradient identity
-> explicit 4 sqrt(X)-O(log X) parabolic seed
-> exact outer feasibility q>=X/28
-> endpoint-projected Dirichlet Gram
-> source-specific Green-Energy Theorem
-> 4 sqrt(X)-polylog prime ramp
-> square-screw/Landau
-> RH.
```

A signed primitive-neighbor transport remains an equivalent alternative proof language. Its local half-scale algebra is closed; its global cost is not.

## VIII. Review order

1. `T-24502` and `L-24506` — Lagarias import and dependency boundary;
2. `L-24507` and `X-24501` — outer theorem;
3. `R-24501` and `X-24502` — cover refutation;
4. `L-24508` — signed certificates suffice;
5. `L-24509` and `L-24510` — Green factorization and scalar mode;
6. `L-24511` — local cluster descent;
7. `L-24512` — exact flow dual firewall;
8. `T-24503` — current full conditional proposal;
9. existing square-screw/Landau consumer.

## Final status

```text
Lagarias equivalence import                 COMPLETE AT SOURCE-QUALIFIED SCOPE
outer parabolic seed q>=X/28               PROPOSED COMPLETE + exact replay
monotone Divisibility Cover                REFUTED
signed b positivity requirement            REMOVED
local prime-power cluster descent           PROPOSED COMPLETE EXACT ALGEBRA
endpoint-projected Dirichlet Gram           PROPOSED COMPLETE EXACT ALGEBRA
Green scalar-mode decomposition             PROPOSED COMPLETE EXACT ALGEBRA
Green-Energy Theorem                        OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVED
```
