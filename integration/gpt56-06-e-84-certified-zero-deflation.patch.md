# Integration patch — gpt56-06-e / Issue #84

## Add claims

```text
L-8401  scalar certified-zero-count deflation                 PROPOSED
L-8402  fixed-vector Pick certified-zero-count deflation       PROPOSED
L-8403  zero-bin Loewner-lower Gram blocks                     PROPOSED
L-8404  Hardy-Z sign-change lower zero counts                  PROPOSED
L-8405  RH-forced total critical-strip slab-count deflation    PROPOSED
M-8401  proof-producing zero-deflation search                  PROPOSED
X-8401  exact finite checker and rigorous numerical controls   PROPOSED EXPERIMENT
```

## Relationships

- depends on D-3201/L-3201/L-3202 from the xi passivity stack;
- consumes proof-grade primitive rectangles from Issue #39 / PR #56;
- integrates with PR #50 uncertainty closure and PR #60 conic portfolios;
- extends cross-height Pick work by subtracting certified zero Gram mass;
- shares Hardy-Z, total zero-count, and direct-xi infrastructure with Issue #7
  and Issue #75 / PR #76;
- genuinely enlarges the value-only cone closed by PR #67.

## Main theorem shape

```text
under RH:
  full passivity score
  = guaranteed contribution from independently counted zeros
    + remaining nonnegative contribution

therefore:
  full score - rigorous lower guaranteed contribution >= 0.
```

The counted zeros may be certified directly on the line or merely counted as
nontrivial zeros in a horizontal full-strip slab. Under the RH assumption, the
latter are forced onto the line in the same ordinate bin.

A strict negative residual is a finite RH-disproof witness after every parent and
zero-count gate is closed.

## Exact controls

- synthetic hidden-off-line scalar: raw `20/3`, deflated `-10/3`;
- synthetic hidden-off-line Pick: raw `400/3`, deflated `-800/3`;
- actual first-zero Arb control: positive residual near `0.00338406673605`;
- actual exact slab-count control `N(14.14)-N(14.13)=1`: positive residual near
  `0.2007996313314755`.

The actual controls validate the finite numerical pipeline but do not promote the
parent analytic claims.

## Registry note

No candidate is added. No existing claim status is changed.
