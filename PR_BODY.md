## Purpose

Turn PR #550's projective full-row route into a standalone hostile reconstruction
and repair every interface that survives exact checking.

**RH remains unproved.** This successor proves an unconditional correction and
no-go theorem, then isolates one clean global producer whose truth would imply
RH through the exact two-row Mellin-Landau consumer.

## Exact base

```text
base PR:      #550
base branch:  research/gpt56-pro/96300-projective-full-row-landau
base SHA:     20646a78c3e8843001cb49ea0c9741f6d0d446f7
parent PR:    #534
parent SHA:   ef18bdda5a65334695008e4c1f5986833160d84f
head branch:  research/gpt56-pro/96500-parity-covariant-gluing
publication:  add-only hardening/correction
```

## Decisive parity correction

For paired sources `S(E,O)=(O,E)` and signed observation
`O(E,O)=R(E)-R(O)`, every rough history `h` contributes

```text
O(S^|h| P)=(-1)^|h| O(P).
```

Rough placement preserves both coefficient magnitude and every activation:

```text
(X/p)/(k/p)=X/k,
p^(-1/2)(k/p)^(-1/2)=k^(-1/2).
```

The predecessor retained history parity as a label but omitted it from the
terminal realization.

At

```text
X=67*71*13=61841,
history=(67),
terminal=(p,y)=(71,13),
```

exact dyadic rational intervals over all 239 active P61 divisors prove

```text
E_T(71,13)-O_T(71,13)>17.
```

The incoming history is odd, so the leaf requires the reverse Target-Lorenz
orientation `O_T>=E_T`, which is impossible. This refutes the gluing argument,
not full-row nonnegativity.

## Fixed-depth repair is also impossible

The exact depth-L rough source expansion is proved. For its signed current block,

```text
B_L,X(q)/sqrt(X)
 = a_q (-1)^(L-1) (log log X)^(L-1)/(L-1)!
   + O((log log X)^(L-2)).
```

Thus an even depth restores canonical recursive parity only by making the
current block eventually negative. A direct 256-bit MPFR certificate gives

```text
B_2,200000(2) < -11,
B_2,200000(3) <  -2.
```

## Clean successor

`L-96503` expands the finite source fully, incorporates every cumulative parity,
and applies one global common-source coefficient vector simultaneously in
source, target, score, and rows. It proves an exact primal-dual alternative:
either a source-faithful positive packing exists or a finite separating
functional excludes the entire common-source cone.

The remaining producer is `GPHT23`, global parity-Hall feasibility for rows two
and three. The downstream chain is exact:

```text
GPHT23
 -> eventual c_X(2),c_X(3)>=0
 -> reciprocal-zeta fixed-row Mellin transforms
 -> exact rows-2/3 noncancellation
 -> Landau
 -> RH.
```

`GPHT23` is open and RH-bearing.

## Manuscript

The PR includes a 15-page standalone LaTeX paper and deterministic compiled PDF:

```text
standalone/2026-08-17-parity-covariant-gluing/main.tex
standalone/2026-08-17-parity-covariant-gluing/parity-covariant-gluing-fixed-depth-96500.pdf
```

## Replay

```bash
cd experiments/X-96500-parity-covariant-gluing
./build_and_replay.sh
cd ../../standalone/2026-08-17-parity-covariant-gluing
./build.sh
cd ../..
sha256sum -c T96500_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_X_96500_PARITY_COVARIANT_GLUE_AUDIT
918b3ccfb7f99d764e01302ffc2f358fda0e3e2ccfc27eeb038799cf0ee05293
E_T(71,13)-O_T(71,13)>17
```

## Exact scientific boundary

```text
activation and coefficient covariance       PROVED EXACT
parity-covariant gluing                      PROVED EXACT
odd-history leaf obstruction                PROVED EXACT/DIRECTED
fixed-depth parity-reset no-go               PROVED ASYMPTOTIC/DIRECTED
global common-source primal-dual theorem     PROVED EXACT
GPHT23 global producer                       OPEN / RH-BEARING
two-row Mellin-Landau implication            PROVED CONDITIONAL
full native-row nonnegativity                OPEN / NOT REFUTED
Riemann Hypothesis                           UNPROVED
```
