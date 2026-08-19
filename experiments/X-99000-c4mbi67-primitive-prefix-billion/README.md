# X-99000 exact primitive-prefix replay

This experiment certifies the coefficient prefix

\[
C(N)=\sum_{n\le N}\frac{a(n)}{\sqrt n},\qquad
 a(n)=6\mathbf 1_{n=1}-6\mu(n)+9\mathbf 1_{2\mid n}\mu(n/2)-3\mathbf 1_{4\mid n}\mu(n/4).
\]

The C++ scanner uses `S=2^40` and, for every `n`, computes the unique integer
`q_n` with

```text
q_n^2 n <= S^2 < (q_n+1)^2 n.
```

Signs are then rounded outward. The retained complete run proves
`C(N)>0` for every integer `2<=N<=10^9`; the exact lower bound is minimized at
`N=48433`.

Fast replay:

```bash
./replay.sh
```

Full from-source replay (about 3.3 GB peak RAM on the original run):

```bash
FULL=1 ./replay.sh
```

The finite theorem is genuine computer-assisted evidence. It is not an
all-scale proof of `C(t)>=0`, does not prove global C4MBI67, and does not
establish RH.

## Replay

```bash
./replay.sh
FULL=1 ./replay.sh   # exact regeneration through 10^9; about 3.3 GB RAM
./build_full.sh 1000000000 40  # scanner only
```

The replay sets `PYTHONDONTWRITEBYTECODE=1` and performs syntax compilation in memory, so checksum ledgers are not polluted by Python cache files.
