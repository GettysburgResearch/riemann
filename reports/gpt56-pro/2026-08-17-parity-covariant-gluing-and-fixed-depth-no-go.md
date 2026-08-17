# Parity-covariant gluing and fixed-depth no-go

UTC cutoff: 2026-08-16T23:52:55Z

## Frozen genealogy

```text
repository:      gfreund123/riemann
main at audit:   994bd4bedcc8b61cebabaf005cc69225fc3fe459
base PR:         #550
base branch:     research/gpt56-pro/96300-projective-full-row-landau
base head:       20646a78c3e8843001cb49ea0c9741f6d0d446f7
parent PR:       #534
parent head:     ef18bdda5a65334695008e4c1f5986833160d84f
successor ID:    T-96500
```

## Hostile reconstruction result

The full-row route preserves the endpoint/index ratio and coefficient magnitude
through every rough placement:

\[
(X/p)/(k/p)=X/k,
\qquad
p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.
\]

It does not preserve the signed orientation. Each rough prime swaps the positive
parity channels, so a history h contributes (-1)^|h|.

The explicit path

```text
X=61841, history=(67), terminal=(71,13)
```

has canonical Target-Lorenz target gap greater than 17. The odd incoming parity
requires the reverse Hall orientation, which is impossible. This refutes the
parity-blind gluing argument, not the native-row inequality.

## Fixed-depth repair disposition

The exact depth-L source expansion is proved. Its current block satisfies

\[
B_{L,X}(q)/\sqrt X
=
 a_q(-1)^{L-1}(\log\log X)^{L-1}/(L-1)!
 +O((\log\log X)^{L-2}).
\]

Thus fixed even depth restores recursive parity only by making the current block
eventually negative. At depth two and X=200000, direct MPFR intervals give:

```text
row 2 upper < -11.2745354467343289715
row 3 upper <  -2.1151635282980809581
```

## Clean successor architecture

The source tree must be expanded at fixed X, cumulative parity incorporated,
and one global common-source problem solved. L-96503 proves the exact finite
primal-dual theorem. Its two-row all-endpoint producer is GPHT23.

The downstream implication is exact:

```text
GPHT23
 -> c_X(2),c_X(3)>=0 eventually
 -> reciprocal-zeta fixed-row Mellin transforms
 -> exact rows-2/3 noncancellation
 -> Landau
 -> RH.
```

GPHT23 is open and RH-bearing. RH remains unproved.

## Replay

```bash
cd experiments/X-96500-parity-covariant-gluing
./build_and_replay.sh
cd ../../standalone/2026-08-17-parity-covariant-gluing
./build.sh
```

Retained proof object:

```text
918b3ccfb7f99d764e01302ffc2f358fda0e3e2ccfc27eeb038799cf0ee05293
```
