# T-99100 — Factor-67 Harnack renormalization for C4MBI67

This packet continues T-99000 with one deliberately stronger closure idea:
**do not prove the primitive prefix `C(t)` positive directly; prove that one
factor-67 causal step cannot decrease it too far.**

Define

\[
 H_{67}(t)=C(t)-67^{-1/2}C(t/67).
\]

Then

```text
H_67(t) >= 0 at every remaining scale
    + finite positivity of C
    => C(t) >= 0 at every scale
    => C4MBI67
    => RH.
```

The descent is exact because repeated division by `67` reaches the certified
finite base, and `1/sqrt(67)<1/8`.

## Why this operator is special

At the Dirichlet-series level, `I-67^(-1/2)T_67` multiplies the source by
`1-67^(-z)`.  The reciprocal-zeta source already contains that local factor,
so the new target **squares the 67 Euler factor**.

At the threshold-complex level, the same operation adds a duplicate 67 label
and asks the expected Euler characteristic to cover one distinguished 67
anchor.  This gives a concrete oriented target rather than an unsigned PSD
magnitude bound.

## Exact finite theorem

The low-memory segmented scanner proves

\[
 H_{67}(t)\ge0\qquad(1\le t<2{,}000{,}000{,}001).
\]

For `2<=t<2,000,000,001`, the exact minimum enclosure is

```text
57,262,723,035 / 2^40
    <= min H_67(t)
    <= 57,692,032,737 / 2^40,
```

at `t=61,848,971`.  The lower bound is approximately
`0.052080143209423113`.

Together with T-99000, this also proves

\[
 C(t)\ge0\qquad(1\le t<2{,}000{,}000{,}001).
\]

## Replay

```bash
cd experiments/X-99100-c4mbi67-harnack67
./replay.sh
```

The fast replay checks the retained proof object, independently verifies the
local-square coefficient formula, and recombines the twenty exact block
transcripts.

A full from-source replay is available as

```bash
FULL=1 ./replay.sh
```

It scans twenty blocks of length `10^8`, using about 492 MB resident memory per
block in the publication run.

## Exact boundary

```text
factor-67 dilation descent                 PROVED EXACT
67-local Euler-factor square               PROVED EXACT
anchored duplicate-67 complex identity     PROVED EXACT
H_67 sign below 2*10^9+1                   PROVED COMPUTER-ASSISTED
C sign below 2*10^9+1                      PROVED COMPUTER-ASSISTED
global H_67 tail                           OPEN / RH-BEARING
global C4MBI67                             OPEN / RH-BEARING
Riemann Hypothesis                         UNPROVED
```

The sole proposed tail target is now

\[
 \boxed{H_{67}(t)\ge0\quad(t\ge2{,}000{,}000{,}001).}
\]
