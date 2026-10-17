# Lossless recovery of the eighth-moment packet

Publication only; proposed mathematics and historical review qualifications are unchanged.

This directory preserves all THIRTEEN original files delivered as
`riemann-eighth-moment-composition-20261018.zip`, whose source was not present
on the inspected #971 recovery head. The four binary parts concatenate to
one deterministic 25,992-byte tar.xz, SHA-256
`3f6588cd688efc7bd18796896d851c563fd5ad68c507c0117e1b596b386a0d9f`.
The original plain-file Git subtree is
`2385ec9053f269f736ee52f54bfd7c1af60d26c5`.

The preserved packet proposes a 163/180 all-field composition using selected
eighth numerator moments. It is NOT a critical native moment theorem, an RH
proof, or newly independently approved mathematics. Historical NOT PUSHED
labels remain in its files; this receipt supersedes publication status only.
The ramified thirteen-file predecessor is already present on #971 and is not
duplicated. Other conversations' unseen files are not claimed recovered.

Restore to a NEW directory:

```sh
python standalone/2026-10-18-eighth-recovery/restore.py --output /tmp/eighth-original --replay
```

The script authenticates the archive, regular member list and complete original
Git tree before writing. It refuses existing destinations. Without --replay it
executes no restored code. With --replay it runs the original byte manifest and
both normal and optimized checkers, requiring byte-identical CHECKS.json.
The publisher freshly ran these three checks; historical mutation generation
is not relabeled as newly executed. These finite tests do not certify the
infinite analytic proofs. This is archived-source recovery, not thirteen
separately browsable repository files; the downloadable delivery also includes
the expanded originals.

Base: #971, `3f1d2a07631eb6cca1f2716be01f64e874667639`.
New all-order mathematics is separate from this immutable recovery.
