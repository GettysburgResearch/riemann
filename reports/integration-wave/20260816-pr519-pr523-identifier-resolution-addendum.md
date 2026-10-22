# Normative identifier-resolution addendum for the PR #519 / PR #523 review

This addendum supersedes only the identifier-allocation paragraph in
`20260816-pr519-pr523-comparative-review.md`. It does not change any
mathematical verdict, normalization identity, Type-I result, Type-II boundary,
or PR #520 finding.

## Exact commit chronology

The apparent `93300` namespace collision was introduced in stages, so the
entire block cannot be assigned wholesale to either branch.

PR #523 committed the two root identifiers first:

```text
R-93300  4bcca58c0596a5554e6bfed24261d3794fb0ba8b
         2026-08-16T00:28:24Z

L-93300  9681cd6d9416511768219e966971cfd910469b8d
         2026-08-16T00:28:46Z
```

PR #519 then committed its continuation before PR #523's final continuation
commit:

```text
R-93300  bd953d293f58b40e6fb1a1e8749fc28f3d945fb7  01:17:58Z
L-93300  16d131fcec20d1550a188895ebfaae8de253924a  01:18:27Z
L-93301  866942904991deecb34e88cf0989e31dda85866f  01:18:50Z
L-93302  636ff7b212604162162b219fcb17e85c825fd73a  01:19:17Z
L-93303  ea4cc9da5b51720546636a3d1c831052eaedd2b3  01:19:47Z
L-93304  7975bc0f7bd125bd0833edc9c5e9a6add04f8f7f  01:20:13Z
T-93305  ae6151fff61da031f913492e5f0ceae2f6c639a5  01:20:44Z
O-93300  913eec3b062f4dc34ae068771e322ce198e0cf2c  01:21:00Z
M-93300  dc54e44e46e798926c26578e96e6ea6ba0659279  01:21:17Z
X-93300  6f9d66b5145120446f48eec85172a11d62f17e41  01:23:25Z
```

PR #523 added its remaining `L-93301--L-93304`, `R-93301`, `O-93300`,
`X-93300`, and `T-93300` files in the final commit
`f2e2e96c48285f59a8df807ba49122778cb10ff4` at `01:36:14Z`.

## Normative first-owner allocation

```text
PR #523 retains:
R-93300
L-93300
T-93300                    unique relative to PR #519

PR #519 retains:
L-93301
L-93302
L-93303
L-93304
T-93305
O-93300
M-93300
X-93300
```

The later colliding files move as follows in a reconciled successor:

```text
PR #519:
R-93300 -> R-93320
L-93300 -> L-93320

PR #523 continuation:
L-93301 -> L-93310
L-93302 -> L-93311
L-93303 -> L-93312
L-93304 -> L-93313
R-93301 -> R-93310
O-93300 -> O-93310
X-93300 -> X-93310
```

The historical source branches should remain frozen. The renaming belongs in a
single explicit reconciliation successor.

## Canonical lineage after correction

```text
PR #498
  -> one reconciled successor based on PR #519's complete F-normalized cubic
  -> import PR #523's earlier L-93300 endpoint-order family
  -> retain PR #519 L-93301--L-93304 and T-93305
  -> place PR #523's later higher-order continuation at L-93310--L-93313
  -> place PR #519's two colliding root files at R/L-93320
  -> mark PR #523 r=1 as SUPERSEDED / SCALAR-NORMALIZATION DUPLICATE
```

The exact mathematical dictionary remains

```text
G_1 = 3K
W_1 = 3F
A_1 = 3 A_circ
B_1^sharp = 3 BCD
```

Balanced dispersion remains open, and RH remains unproved.
