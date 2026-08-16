## Research hardening

This successor is stacked directly on PR #542 and stress-tests the
prime-sieved producer before using its direct Mellin--Landau consumer.

```text
base PR:      #542
base SHA:     ca5fb69c15cda29b3b589660f9be44ea2f440677
head branch:  research/gpt56-pro/96400-two-row-prefix-shadow-hardening
```

## Exact corrections

1. The local `FRONTIER-CHAIN` proof from PR #537 is invalid. At
   `(j,P,n)=(3,6,24)` the fixed-product cube leaves coefficient `-1` at one
   knot; it cannot manufacture a three-knot convex packet.
2. PRs #548/#549 replace the actual \(P\)-rough store by an all-integer block.
   At `P=30,p=5,u=2`, the rough block `[2,10)` contains only `7`, so its mass
   is `<1/2`, while the claimed surrogate lower bound is `>2`.
3. The positivity statement is not refuted, but none of those transports
   proves it.

## Exact surviving chain

Only rows two and three are required. This packet proves their exact Möbius
Riesz formulas, sparse coefficient dictionaries, integer-knot reduction,
two-state recurrences, reciprocal-zeta Mellin transforms, and exact
noncancellation:
```text
P2(z)=2*2^(-z)-1-3^(-z)
3P3(z)=5*3^(-z)-2^(-z)-1-3*4^(-z)

P2=P3=0 => -3(2^(-z)-1)(2^(-z)-2)=0.
```

Hence
```text
eventual c_N(2)>=0 and c_N(3)>=0
 -> Landau
 -> RH.
```

The two-row positivity theorem `TRP23` remains explicitly **OPEN /
RH-bearing**. This is a hardening successor and exact frontier reduction, not
a false complete proof.

## Replay

```bash
cd experiments/X-96400-two-row-prefix-shadow
python3 verify.py --output results/verification.json
sha256sum -c SHA256SUMS
```

The replay does not prove `TRP23` or RH.
