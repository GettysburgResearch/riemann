## Purpose

Continue PR #578 at exact head `981bfef5fcfa3a39ccf4f50875cf8a6057650268`
and attack only the histories containing a rough prime larger than
`(log X)^(1/4)`.

**RH remains unproved.** The attack produces a decisive no-go and a sharper
replacement frontier.

## Decisive correction

The published adaptive depth is `L=O(log log log X)`, while the total reciprocal
mass of active rough primes is `~log log X`. A product-safe elementary-symmetric argument, using only Mertens estimates
and a repeated-coordinate collision bound, shows that the final odd layer dominates. Therefore

```text
full depth-L current < 0,
large-prime residual < - positive small-prime cube < 0.
```

Thus `LAPBR67` residual nonnegativity is false and cannot be repaired by a
better constant.

## New exact source theorem

The packet proves the **complete** small-prime cube through
`Z=(log X)^(1/4)` is positive and then adjoins every larger prime with exact
largest-prime Bellman ownership:

```text
U_full(X)
 = U_Z(X)
 - sum_(Z<p<=X/2) p^(-1) U_<p(X/p).
```

Expanding the child gives one signed prime-versus-Mobius correlation with the
exact owner constraint `P^+(v)<p`.

## Type I / Type II

The terminal range `p>X/Z` is proved negligible:

```text
I_Z = O((log Z)^2/log X) = o(U_Z).
```

The sole remaining estimate is

```text
BLPTE67:
T_Z <= U_Z-I_Z,
```

where

```text
T_Z = sum_(Z<p<=X/Z) 1/p
      sum_(Z<P^-(v), P^+(v)<p) mu(v)/v * U_Z(X/(pv)).
```

This is a one-sided, source-faithful balanced Type-II estimate. No rowwise
absolute value, unrestricted rough reservoir, or source-blind large sieve is
used.

## Replay

```bash
cd experiments/X-97700-lapbr-large-prime
./build_and_replay.sh
cd ../..
sha256sum -c T97700_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T97700_LAPBR_NO_GO_AND_TYPEII_REDUCTION_ALGEBRA
PASS_T97700_FULL_REPLAY
```

## Exact boundary

```text
PR #578 small-prime cube                    RETAINED
LAPBR67                                     REFUTED
complete small-prime cube                   PROVED POSITIVE
largest-prime Bellman identity              PROVED EXACT
terminal Type I                             CLOSED
BLPTE67 signed Type II                      OPEN / RH-BEARING
BLPTE67 -> RH                               PROVED CONDITIONAL
Riemann Hypothesis                          UNPROVED
```

## Deterministic Google Drive mirror

```text
ZIP:
https://drive.google.com/file/d/1hbyvBsACrrOJa8LuYGVZHI_owPpbab2n/view?usp=drivesdk

PDF:
https://drive.google.com/file/d/14mej01r7fbLo2bQViGA3bkb7EU9cGUgn/view?usp=drivesdk

LaTeX:
https://drive.google.com/file/d/1Y5mS8TX8XJVR3Y8frI0HY2gQQgsKDm_l/view?usp=drivesdk

Checksum ledger:
https://drive.google.com/file/d/1z2QwA4AtfVkk8ibDs_kK8hb9nWC-9Qwc/view?usp=drivesdk
```
