## Purpose

Continue PR #624 with one factor-67 renormalization step that turns the global
primitive-prefix sign into a single contracted Harnack tail.

**RH remains unproved.**

## Core idea

Define

```text
H_67(t) = C(t) - C(t/67)/sqrt(67).
```

If `H_67(t)>=0` at every remaining scale, repeated division by `67` reaches the
finite positive base and proves `C(t)>=0` globally.  Since
`1/sqrt(67)<1/8`, this is a strict scalar contraction.

The operator also multiplies the Dirichlet series by `1-67^(-z)`, thereby
squaring the 67 Euler factor already present in the reciprocal-zeta source.
In the threshold-complex model it is an anchored duplicate-67 inequality.

## Exact finite result

A low-memory segmented `2^40` scanner proves

```text
H_67(t) >= 0 for every real 1 <= t < 2,000,000,001.
```

The positive minimum enclosure is attained at `t=61,848,971`:

```text
57,262,723,035 / 2^40
 <= min H_67
 <= 57,692,032,737 / 2^40.
```

Together with T-99000 this doubles the certified `C(t)>=0` range to
`2*10^9`.

## Exact remaining line

```text
H_67(t) >= 0 for every t >= 2,000,000,001    OPEN / RH-BEARING
C4MBI67 global                               UNPROVED
Riemann Hypothesis                           UNPROVED
```

## Validation

- independent fast coefficient and proof-object replay;
- twenty retained exact segment transcripts;
- deterministic block recombination;
- optional full from-source replay;
- fail-closed status flags for the global tail and RH.
