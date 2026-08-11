# Handoff — safe Jordan / one-Green to Pick continuation firewall

## Freeze

```text
base PR:     #397
base branch: research/gpt56-pro/395-chebyshev-hankel-amplifier
base SHA:    7061072f5a5fd4d6fc741cba9e5035e29b0a0e31
new branch:  research/gpt56-pro/91014-safe-jordan-pick-firewall
RH:          unproved
```

## Consume first

1. `R-91005-safe-jordan-one-green-does-not-imply-pick-continuation.md`
2. `L-91014-local-pick-positivity-forces-global-schur-continuation.md`
3. `L-91015-one-green-versus-target-pick-contractivity-gap.md`
4. `T-91006-safe-real-pick-matrix-rh-criterion.md`
5. `X-91014-safe-jordan-pick-firewall`

## Normative correction

The following implication must not be used:

```text
positive Jordan/compound-Poisson kernel
+ positive one-Green kernel
+ boundary unitarity/cocycle
=> global target Pick positivity.
```

`R-91005` gives an exact countermodel, including a strengthened version retaining
the actual zeta Jordan factor and positive full one-Green measure.

## Correct continuation interface

For

```text
theta_u(q)=xi(1+q)/xi(1+u+q),
C_ij=1/(1+u+q_i+q_j),
D=diag(theta_u(q_i)),
```

prove

```text
C-D C D >= 0
```

for every finite positive rational packet and every positive rational `u<1`.
This is equivalent to a Cauchy-space multiplier contraction.  Finite
Nevanlinna--Pick plus Montel then gives the global moving-half-plane Schur flow;
there is no further analytic-continuation gap.

## Review joints

1. partial-fraction signs in the strengthened `xi_y=F_y xi` control;
2. exact negative two-point Pick determinant;
3. use of finite Nevanlinna--Pick and Montel on a nested uniqueness set;
4. avoidance of numerator cancellation by choosing rational `u`;
5. bounded-type/inner implication under RH;
6. strict separation between the one-Green Hankel matrix and target Cauchy Pick matrix.
