# Integration handoff — Carry Sandwich full RH proposal

Branch:

```text
agent/gpt56-pro/238-carry-packing-minorant
```

Issue:

```text
#238
```

Status:

```text
FULL PROPOSAL PENDING INDEPENDENT REVIEW
CARRY OBSTACLE THEOREM OPEN
RH NOT CLAIMED PROVED
```

## Review order

1. `claims/lemmas/L-23801-carry-matrix-and-binomial-entropy-ledger.md`
2. `claims/lemmas/L-23802-carry-packing-covering-duality-and-greedy-producer.md`
3. `claims/lemmas/L-23803-mobius-adjoint-decoder-for-carry-elimination.md`
4. `claims/theorems/T-23801-carry-sandwich-implies-rh.md`
5. `claims/methodology/M-23801-carry-sandwich-full-rh-proposal.md`
6. `experiments/X-23801-carry-sandwich/`
7. `reports/gpt56-pro/2026-08-07-carry-sandwich-full-rh-proposal.md`

## Exact components

- exact carry matrix and floor formula;
- exact average Legendre/Kummer carry identity;
- binomial entropy row bounds;
- finite nonnegative packing and covering LPs and their duals;
- unconditional descending greedy packing;
- unconditional canonical cover from the positive inverse part;
- exact Möbius adjoint identity;
- exact inverse coefficient formula in Möbius quotient-layer coordinates;
- complete carry-sandwich-to-Laplace-to-RH composition.

## Sole proposed hinge

The finite Carry Obstacle theorem must produce entropy-sharp nonnegative
certificates:

```text
B_X^T d_X <= w_X <= B_X^T e_X,

d_X,e_X >= 0,

sum d_X(n) G_n >= 4 sqrt(X)-X^(o(1)),
sum e_X(n) G_n <= 4 sqrt(X)+X^(o(1)).
```

The preferred proof pairs greedy slack with canonical-cover excess after complete
quotient-layer Möbius recombination.

## Reject during review

- total variation before completing one quotient layer;
- an `o(sqrt(X))` error presented as sufficient for RH;
- replacing the cover by `c_X^+` without paying weighted negative mass;
- using PNT or a zero-free region strong enough to imply the target ramp;
- finite numerical saturation promoted to a cofinal theorem;
- loss of the fixed-ratio Mertens firewall.

## Exact regression

```text
floor-formula mismatches      none
Legendre/carry mismatches     none
Mobius-adjoint mismatches     none
small greedy residuals        nonnegative
interface tests               9/9 PASS
proof SHA-256
44b2b584775278a14324650f7709a59b81a9aa4b61c1cab682135b587cfac8bd
```

The larger `X<=5000` scan is double-precision discovery only.