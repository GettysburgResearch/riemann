# Reflected carry-envelope full proposal

Agent: `gpt56-pro-22`  
Date: 2026-08-07  
Issue: #238  
Classification: full proposed proof architecture; one symbolic terminal-face theorem pending review

## Executive decision

The repository's arithmetic routes now agree that the obstruction is coherent
balanced Möbius cancellation. Generic operator norms and rowwise absolute values
cannot solve it. The new route avoids proving a complete balanced packet norm.
It asks only for the scalar functional needed by the prime ramp and converts
that scalar problem into a finite convex packing.

The spine is

```text
base-q carries in binomial rows
-> exact Legendre prime-power identity
-> finite nonnegative packing beneath the prime ramp
-> Mobius-curvature profile
-> reflected Hermitian Selberg square
-> two-contact carry-obstacle recurrence
-> subpolynomial packing deficit
-> sharp 4 sqrt(X) prime-ramp lower bound
-> square-screw/Landau transfer
-> RH.
```

RH is not claimed independently verified.

## New exact breakthrough 1: inverse carry coefficients are Möbius curvature

For the exact triangular carry inverse `B_X^T c_X=w_X`, define

```text
u(m)=sum_(k<=X/m) mu(k) w_X(mk),
F(j)=1/(j-1) sum_(m=j)^X u(m).
```

Then exactly

```text
c_X(j)=(j+1)[F(j)-2F(j+1)+F(j+2)].
```

Thus Carry Saturation is simply convexity of one explicit smoothed Möbius
profile.

More generally, every nonnegative carry packing is a convex profile `P`, and
its unused ramp is reconstructed from `F-P` by one exact finite divisor sum.
This gives a one-dimensional convex obstacle containing every Möbius sign.

## New exact breakthrough 2: the sharp mass is profile area

For

```text
d(j)=(j+1) Delta^2 P(j),
```

one has

```text
sum_j j d(j)=6P(2)+2 sum_(j=4)^X P(j).
```

The required `8 sqrt(X)` coefficient mass is therefore a geometric area target,
not a mysterious triangular-inverse statistic.

## Exact finite LP

The entropy packing is

```text
maximize  sum_n d(n) G_n
subject to d>=0, B_X^T d<=w_X.
```

Its dual is

```text
minimize  sum_q w_X(q)y(q)
subject to y>=0, B_X y>=G.
```

Every feasible primal vector gives a rigorous prime-ramp lower bound by the
carry--Legendre identity. Exact Carry Saturation is sufficient but unnecessary.

## Proposed closing theorem

Let

```text
D_X=(4 sqrt(X)-optimal carry entropy packing)_+.
```

For fixed reserve `delta<1/3` and every sufficiently large packet order `K`, the
proposed reflected carry theorem is

```text
D_X
 <= X^(2/K+o_K(1))
    [1+max_(Y<=X^(1-delta) exp(O_K(1))) D_Y].
```

The proof candidate uses:

1. the exact finite double Möbius resolvent;
2. high-order Euler cancellation for every row with one free macroscopic
   lattice variable;
3. the reflected Selberg identity for the complete same-scale Hermitian
   residual;
4. the scalar convex-envelope projection;
5. the fact that one maximal affine contact interval has only two endpoints.

This explicitly repairs the dependency flaw in the earlier reflected proposal:
balanced rows are not removed by the withdrawn `L-23203` induction. They are
sent to the carry obstacle.

## Why the exponent vanishes

Let

```text
theta=limsup log(1+D_X)/log X.
```

The recurrence gives

```text
theta <= 2/K+(1-delta)theta,
```

so

```text
theta <= 2/(K delta).
```

Let fixed `K` increase. Then `theta=0`, hence the packing objective is

```text
4 sqrt(X)-X^o(1).
```

Legendre and entropy transfer this to the complete prime-power ramp. At square
cutoffs, the square-screw negative part is subpolynomial. The exact rightmost-
zero exponent is zero, and RH follows.

## Why this may evade generic BTP

BTP asks for a contraction of the complete packet energy. The carry route needs
only one scalar lower functional. The convex envelope also absorbs positive
Hermitian diagonal energy rather than estimating it.

The proposal therefore seeks a two-contact theorem for a scalar obstacle,
not a complete arbitrary-vector Type-II bound.

## Exact adversarial hinge

A reviewer should attempt to produce a fully recombined same-scale terminal
carry face with three or more free divisor/contact coordinates.

Such a face rejects the `2/K` exponent.

Conversely, a complete `K=6`, `K=8`, and symbolic-`K` dictionary proving that
every face is one affine interval with two free endpoints verifies the new
closing theorem.

Mandatory additional checks:

- no balanced class is discharged by assuming BTP;
- all transition surfaces are present;
- every interior row is killed by the declared null moments;
- reflected diagonals remain on the positive side;
- the first-cell mutation reproduces the exact fixed-ratio Mertens increment.

## Exact regression

`X-23801` independently reconstructs the carry matrix, Möbius curvature,
componentwise residual, and both telescoping mass identities using rational
arithmetic only.

Retained synthetic result:

```text
classification       EXACT_CARRY_ENVELOPE_ALGEBRA_VERIFIED
packing mass          6026/1155
minimum residual      1/160
proof-object SHA-256  9dfff56752131b31ae6bb5def0e456147cb441fbdac69f24cc934f1ec310ed7f
```

The regression is synthetic and proves no asymptotic statement.

## Review order

1. `D-23801-carry-packing-and-mobius-curvature.md`
2. `L-23801-carry-legendre-entropy-consumer.md`
3. `L-23802-canonical-carry-envelope-lp.md`
4. `X-23801-carry-envelope/verify.py`
5. `L-23803-reflected-two-contact-carry-contraction.md`
6. `T-23801-reflected-carry-envelope-rh-proposal.md`
7. `M-23801-carry-envelope-review-and-production.md`
8. PR #226 reflected Selberg identity
9. PR #158 high-order Euler theorem
10. PR #229 first-cell Mertens decoder

## Exact status

```text
finite carry/Mobius algebra             proposed exact + exact replay
packing/entropy consumer                proposed complete
reflected two-contact contraction       proposed new RH-bearing hinge
conditional deduction to RH             complete
accepted proof of RH                    no
```
