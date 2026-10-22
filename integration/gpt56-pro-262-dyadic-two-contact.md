# Integration handoff — dyadic two-contact signed carry proposal

Branch:

```text
agent/gpt56-pro-262-dyadic-two-contact
```

## Purpose

This branch starts from the corrected two-frequency physical block of PR #241
and traces the exact fixed-`q_0=2` Möbius source through:

```text
complete dyadic 2x2 normal Gram
-> pointwise carry incidence
-> signed carry residual
-> full-divisor Green potential.
```

It then tests the two suggested contraction mechanisms.

- Generic parity-comb inversion is not used because its coercive inverse is
  itself zero-sensitive.
- High-index adjacent signed transport is exactly invisible to the dyadic
  source; only a bottom-charge telescope can close it.

The surviving full proposal is `T-26201`.

## New files

```text
claims/lemmas/
  L-26201-dyadic-mobius-two-contact-carry.md
  L-26202-dyadic-signed-slack-riesz-bridge.md
  L-26203-dyadic-two-charge-divisor-green.md
  L-26204-dyadic-source-coupled-normal-gram.md
  L-26205-odd-row-even-column-dyadic-carry-lift.md

claims/refutations/
  R-26201-high-index-signed-transport-is-dyadic-invisible.md

claims/theorems/
  T-26201-dyadic-two-contact-signed-slack-rh-proposal.md

claims/methodology/
  M-26201-dyadic-two-contact-review-protocol.md

experiments/X-26201-dyadic-two-contact-carry/
  verify.py
  verify_bottom_charge.py
  verify_digital_lift.py
  recon.py
  README.md
  tests/test_verify.py
  results/

reports/gpt56-pro/
  2026-08-08-dyadic-two-contact-carry-full-proposal.md
```

## Exact advances

### Coupled physical source

The normalized dyadic atomic source is

```text
beta_2=(I-2^(-1/2)tau_(log2)) alpha_mu.
```

One physical block is the complete positive rank-one matrix

```text
[[1,-1/sqrt(2)],[-1/sqrt(2),1/2]],
```

with all four translate cross terms retained. The dyadic multiplier is zero-safe
and causally invertible.

### Pointwise two contacts

For every finite carry row,

```text
sum_q b_2(q) chi_(n,q)(j)
 = -1_(j=1)-1_(j=n-1).
```

The averaged image is `-2/(n+1)`, and the generalized Kummer cross term is
`-2L(n)/(n+1)`.

### Signed slack

For any feasible carry vector,

```text
Pi_2(X;d)
 = R_2(X)+2 sum_n d(n)/(n+1).
```

For the canonical greedy vector, `Pi_2` is the parity-weighted blocker loss and
also the Möbius-weighted dyadic second difference of final slack.

### Two Green charges

For the full-divisor gradient Gram,

```text
Gbar_X b_2=-3e_2+e_3,
b_2^T Gbar_X b_2=5.
```

Thus

```text
Pi_2=-3T_X(2)+T_X(3),
T_X=Gbar_X^-1 s_X.
```

### Digital half-scale subsystem

Exactly

```text
chi_(2n+1,2q)(2j+epsilon)=chi_(n,q)(j),
beta_(2n+1,2q)=beta_(n,q).
```

The even parent columns and their full Hermitian carry rows descend isometrically
to half scale. Odd-column leakage is the only remaining digital channel.

### Signed-transport no-go

For the adjacent divisor-gradient flow,

```text
sum_q b_2(q)v_q(b)=-2b(2)+b(3),
Delta_F=3F_2-F_3.
```

All moves supported at `j>=4` are invisible. Any transport completion must
retain its accumulated charge down to the bottom boundary.

## Full proposal hinge

Define the exact greedy residual `s_X^gr` and

```text
Pi_2^gr(X)=sum_q b_2(q)s_X^gr(q).
```

The sole theorem is:

```text
DSS:
Pi_2^gr(X)=O_epsilon(X^epsilon)
for every epsilon>0.
```

Equivalent Green form:

```text
|-3T_X(2)+T_X(3)|=X^o(1).
```

A fail-closed sufficient production recurrence is:

```text
|Pi_2^gr(X)|
 <= polylog(X)
    + max_(Y<=(X+1)/2)|Pi_2^gr(Y)|.
```

The exact even-column lift supplies the half-scale channel. A production proof
must control the signed odd-column leakage, all feasibility corrections, every
dyadic-chain boundary, same-scale clusters, and the bottom charges.

## Deduction

DSS gives the same subpower bound for

```text
R_2(X)=sum_(q<=X)b_2(q)q^(-1/2)log(X/q).
```

Its Mellin transform contains

```text
(1-2^(-s))/zeta(s),
```

with no possible cancellation of a zero to the right of the critical line.
Normal convergence in the shifted right half-plane excludes every such zero;
functional-equation symmetry gives RH.

## Exact replay

```text
core exact algebra
  dd6f66f1e026178c1277f2fa634671d8868219e0303db505d9f0547df5eb0715

bottom-charge / high-index invisibility
  395a7a89ea2267cfa5a3b805ead2646fa46a1761408f6ff048fed7b2e218757f

digital half-scale isometry
  17e23d1e2ebc01cc7283d125c15c721d4743e69f906b17b715294f60b0e09b23

finite reconnaissance
  7a249c5a00cb1e5c6daa0434bcbdc40efef890f381f2ae1eb52091e8557f001e
```

The exact tests are finite algebra only. The reconnaissance is discovery only.

## Status

```text
source trace and coupled normal matrix     PROPOSED EXACT
two-contact carry theorem                 PROPOSED COMPLETE
two-charge Green theorem                  PROPOSED COMPLETE
digital half-scale subsystem              PROPOSED COMPLETE
high-index transport no-go                PROPOSED COMPLETE
Odd-Leakage / PBD                         OPEN
DSS                                       OPEN, RH-BEARING
DSS => RH                                 PROPOSED COMPLETE
RH                                        UNPROVED
```

Recommended next attack: use the exact odd-row/even-column isometry to emit the
odd-column leakage of the lifted greedy vector, then solve the three-layer
Möbius combination before any absolute value. This is a much smaller target than
total greedy slack, full Green energy, or all balanced Type-II packets.
