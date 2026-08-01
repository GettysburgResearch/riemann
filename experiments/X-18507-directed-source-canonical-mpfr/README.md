# X-18507 — directed growing source-canonical D-0001 ladder

This experiment generalizes the real `X-18505` direct-block producer from the
`N=1` calibration to growing cutoff-free D-0001 even packets.

## Exact packet

Use the unnormalised even coordinates

```text
b0 = e0,
bk = e(-k) + e(k),  1 <= k <= N,
G  = diag(1,2,...,2).
```

The source functional and its metric representer are

```text
ell(x) = x0 + 2 sum_(k>=1) xk,
Q_W    = (1,...,1)^T,
G_W    = 1 + 2N.
```

An exact basis of the source-valid complement is

```text
Q_E^(k) = -2 e0 + ek,  1 <= k <= N,
G_E     = 2 I + 4 J.
```

At every level the producer emits, in this one declared metric,

```text
Q_W, P_W, E_W, Z_W, C, X_N, R_N, G_W,
```

where `P_W` is the complete cutoff-free pole/archimedean contraction,
`E_W` contains every prime power `q <= c`, `X_N` is a frozen dyadic trial
harmonic solve, and

```text
R_N = Z_W - C X_N.
```

The standard-library consumer reconstructs the a posteriori lower matrix

```text
D_N = J_X^* H J_X - h^-1 R_N^* G_E^-1 R_N
```

and proves both

```text
C - h G_E > 0,
D_N - m G_W > 0
```

by exact interval LDL arithmetic.

## Directed ladder

The retained 384/512-bit levels are

```text
(c,N) = (10,2), (20,3), (50,4), (100,5), (200,6),
        (500,7), (1000,8), (2000,9), (5000,10).
```

Every 512-bit primitive interval is nested in the corresponding 384-bit
interval. The exact consumer classifies all nine levels as

```text
CERTIFIED_DELTA_ZERO_SOURCE_CANONICAL_DIRECT_BLOCK
```

with

```text
Delta_(c,N) = [G_W^(-1/2) D_N G_W^(-1/2)]_- = 0.
```

The retained summary has SHA-256

```text
5cb0bda48a65ec6ee896ca37d8e9920ea2ed7349bac66b2cdd935c087364c26c
```

and the deterministic complete local archive used to publish this source had
SHA-256

```text
abbb822f934075bebb0c9da5a6b766506d13981589baf27413352149d53a7c48.
```

## Scope

This is a rigorous finite growing ladder for the D-0001 source-canonical
quotient. It is not yet the spectral deficit-canonical augmentation of
`L-18901`, and nine finite levels do not prove an unbounded cofinal theorem.
No RH claim follows from this experiment alone.
