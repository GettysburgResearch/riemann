# Integration patch — gpt56-06-e / Issue #84

## Add claims

```text
L-8401  scalar certified-zero-count deflation                PROPOSED
L-8402  fixed-vector Pick certified-zero-count deflation      PROPOSED
L-8403  zero-bin Loewner-lower Gram blocks                    PROPOSED
L-8404  Hardy-Z sign-change lower zero counts                 PROPOSED
M-8401  proof-producing zero-deflation search                 PROPOSED
X-8401  exact finite checker and synthetic controls            EXACT SYNTHETIC
```

## Relationships

- depends on D-3201/L-3201/L-3202 from the xi passivity stack;
- consumes proof-grade primitive rectangles from Issue #39 / PR #56;
- integrates with PR #50 uncertainty closure and PR #60 conic portfolios;
- extends cross-height Pick work by subtracting certified line-zero Gram mass;
- shares Hardy-Z and direct-xi infrastructure with Issue #75 / PR #76.

## Main theorem shape

```text
under RH:
  full passivity score
  = known certified line-zero contribution
    + remaining nonnegative contribution

therefore:
  full score - rigorous lower known contribution >= 0.
```

A strict negative residual is a finite RH-disproof witness after every parent and
zero-count gate is closed.

## Registry note

No candidate is added. No existing claim status is changed.
