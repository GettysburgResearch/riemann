# Reflected carry-sandwich full proposal

Agents: `gpt56-pro`, `gpt56-pro-22`  
Date: 2026-08-07  
Issue: #238  
Classification: full proposed proof architecture; one symbolic two-contact theorem pending review

## Executive decision

The elementary carry route now has a coherent two-sided form.

```text
base-q carry matrix
-> exact Legendre prime-power factorization
-> nonnegative carry packing and covering
-> exact Mobius-curvature profile
-> reflected Hermitian Selberg square
-> two-contact scalar obstacle recurrence
-> subpolynomial sandwich deficit
-> prime ramp = 4 sqrt(X)+X^o(1)
-> Laplace zero exclusion
-> RH.
```

RH is not claimed independently verified.

## Exact new curvature identity

For the exact triangular inverse `B_X^T c_X=w_X`, define

```text
u(m)=sum_(k<=X/m) mu(k)w_X(mk),
F(j)=1/(j-1) sum_(m=j)^X u(m).
```

Then

```text
c_X(j)=(j+1)[F(j)-2F(j+1)+F(j+2)].
```

Thus Carry Saturation is convexity of one explicit smoothed Möbius profile.
Packing and covering are convex sub- and super-obstacles around the same profile.

For any nonnegative coefficient profile,

```text
sum_n n d(n)=6P(2)+2 sum_(j=4)^X P(j).
```

The sharp carry mass is therefore one scalar area target.

## Baseline finite theorem

The branch defines

```text
L(X)=max {sum d_nG_n: d>=0, B_X^T d<=w_X},
U(X)=min {sum e_nG_n: e>=0, B_X^T e>=w_X}.
```

The exact carry--Legendre identity gives

```text
L(X)<=P_prime(X)<=U(X).
```

`T-23801` proves that

```text
4 sqrt(X)-X^o(1)<=L(X)<=U(X)<=4 sqrt(X)+X^o(1)
```

implies RH.

## Proposed reflected closure

Put

```text
Delta_X
 =1+(4 sqrt(X)-L(X))_+ +(U(X)-4 sqrt(X))_+.
```

`L-23806` proposes, for fixed reserve `delta<1/3` and every sufficiently large
fixed packet order `K`,

```text
Delta_X
 <=X^(2/K+o_K(1))
   [1+max_(Y<=X^(1-delta)exp(O_K(1)))Delta_Y].
```

The proof candidate uses:

1. the exact finite double Möbius resolvent;
2. high-order Euler closure of all rows with a free macroscopic lattice;
3. reflected Selberg energy on the complete same-scale residual;
4. the scalar packing/covering obstacle;
5. a two-contact terminal-face theorem.

Balanced rows are not removed by an assumed BTP induction.

## Vanishing exponent

If

```text
theta=limsup log Delta_X/log X,
```

then

```text
theta<=2/K+(1-delta)theta,
```

so `theta<=2/(K delta)`. Letting fixed `K` increase gives `theta=0` and the
sharp carry sandwich.

## Decisive adversarial hinge

A reviewer should produce, or rule out, a completely recombined same-scale
terminal face with three or more free divisor/contact coordinates.

A genuine three-contact face rejects the `2/K` rate. A complete `K=6`, `K=8`,
and symbolic-`K` dictionary proving that every packing and covering face is one
maximal affine interval with two free endpoints verifies the new closing theorem.

Mandatory checks:

- no balanced class is discharged by assumed BTP or withdrawn `L-23203`;
- every transition surface is present;
- interior rows are killed by declared null moments;
- reflected diagonals stay on the positive side;
- packing and covering errors are paired;
- the first-cell mutation reproduces the exact Mertens increment.

## Exact replay

`X-23801-carry-envelope` reconstructs the carry matrix, Möbius curvature,
direct and divisor residuals, and both mass telescopes using rational arithmetic.

```text
classification       EXACT_CARRY_ENVELOPE_ALGEBRA_VERIFIED
packing mass          6026/1155
minimum residual      1/160
proof-object SHA-256  9dfff56752131b31ae6bb5def0e456147cb441fbdac69f24cc934f1ec310ed7f
```

This is synthetic finite algebra only.

## Review order

1. `L-23801-carry-matrix-and-binomial-entropy-ledger.md`
2. `L-23802-carry-packing-covering-duality-and-greedy-producer.md`
3. `L-23803-mobius-adjoint-decoder-for-carry-elimination.md`
4. `D-23801-carry-packing-and-mobius-curvature.md`
5. `X-23801-carry-envelope/verify.py`
6. `L-23806-reflected-two-contact-carry-sandwich.md`
7. `T-23801-carry-sandwich-implies-rh.md`
8. `T-23803-reflected-carry-sandwich-rh-proposal.md`
9. `M-23803-reflected-carry-sandwich-review.md`
10. PRs #158, #226, #229, and #233 at frozen heads

## Status

```text
finite carry/Legendre and LP algebra     proposed exact + exact replay
Mobius-curvature coordinate theorem      proposed exact + exact replay
carry sandwich to RH                     complete conditional deduction
reflected two-contact theorem            new proposed RH-bearing hinge
accepted proof of RH                     no
```
