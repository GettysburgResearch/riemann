# X-18501 — Exact sacrificial-subspace harmonic count

This experiment verifies the finite arithmetic in `L-18501`.

For positive metric `G`, positive evaluation Gram `K`, threshold `tau`, and a
witness basis `W`, the checker proves

```text
codim(W) <= radical_rank,
W^* (K-tau G) W > 0
```

by exact rational rank and `LDL^T`. Courant--Fischer then gives

```text
N_(G^-1/2 K G^-1/2)(tau) <= radical_rank.
```

A supplied radical basis is checked separately through

```text
R^* (epsilon G-K) R > 0,
epsilon < tau.
```

This gives the reverse min--max inequality and therefore exact count saturation,
plus

```text
principal_angle^2 <= epsilon/tau.
```

The witness subspace is deliberately allowed to differ from the radical
orthogonal complement. This is the point of the theorem.

## Retained exact control

The synthetic `4 x 4` evaluation Gram contains nonzero radical/witness cross
entries. With

```text
radical rank     2
threshold        1/2
radical endpoint 3/100
```

the one-sided witness `span(e3,e4)` has exact floor pivots

```text
3/2, 187/75,
```

while the radical upper-moat pivots are

```text
1/50, 1/100.
```

The checker certifies

```text
count lower = count upper = 2
angle^2 upper = 3/50.
```

Proof-object SHA-256:

```text
997492a615abfd5bd5a4ada88a9513b649d3126cfe2b38833f12b488de10b8e2
```

Nine central/adversarial checks were independently replayed with Python
`Fraction` arithmetic in the authoring session.

## Production contract

A harmonic production certificate must bind:

1. exact `G_C` and selected-zero `K_T^C` enclosures;
2. a rational witness subspace inside the complete low packet;
3. exact witness codimension no larger than the radical rank;
4. a strict witness frame floor above `B_T+beta`;
5. the exact radical packet and its evaluation upper endpoint;
6. all assembly radii in the safe Loewner direction.

The preferred first target is the fixed-dimensional external Hermite corrector
from `L-18502`. A second target is a same-end profile packet, which avoids the
opposite-end terminal-prime matrix in the min--max witness.

A floating generalized eigencount is not a proof object.
