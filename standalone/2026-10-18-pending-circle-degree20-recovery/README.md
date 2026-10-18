# Recover the pending circle and degree-20 packets

**Publication recovery only. No new mathematical result or independent approval.**

This directory preserves all **26 original files (183,164 bytes)** from the two
pending conversation packets. They are inside eight binary archive parts, not
26 separately browsable text files. The archive is deterministic tar.xz:
60,400 bytes, SHA-256
`9e105eed5a7b87861dcc34c24c682a6ad611877a51619e0f5607c851eb172a0d`.

| Original directory | Files | Original Git tree |
| --- | ---: | --- |
| `standalone/2026-10-18-circle-prime-bracketing/` | 13 | `45a5b3b3743c2083a68d6b08f3c57f694f166b1f` |
| `standalone/2026-10-18-degree20-continuation-attempt/` | 13 | `fe8b5af4d603d6a5dca6fb43008a3e77c739c5fb` |

## Restore without executing research code

From a checkout containing this recovery, run:

```sh
python standalone/2026-10-18-pending-circle-degree20-recovery/restore.py --output /path/to/new/directory
```

Omit `--output` to verify only. Python's standard library suffices for restoration.
The script authenticates the compressed bytes, exact regular-file inventory,
both original Git trees and both complete original manifests. It refuses an
existing output path and runs no restored code. The two original directories
are recreated below the new output directory, retaining their `standalone/` paths.
`ORIGINALS.json` also records the supplied ZIP identities.

The original circle packet's `replay.py --numeric` runs its finite checks,
negative controls and optional nondirected diagnostics. The degree-20 packet's
`diagnose.py` reproduces the saved candidate diagnostic. Read the original
READMEs first; these research commands require mpmath. They are not run by
`restore.py`.

## Scientific status is unchanged

The circle packet proposes coefficientwise prime-detector brackets and
complete-source approximation estimates. It does **not** establish the
critical prime-versus-continuum bound or RH.

The degree-20 packet records an **unsuccessful numerical continuation**.
The last saved candidate has a nonzero twentieth-moment discrepancy and a
zero internal coupling. Its small lower-moment residual is not an exact-root
certificate. It is not a new strictly positive connected realization, an
impossibility theorem, or an improvement over the separate #988 discrepancy.

Every original source, report, qualifier and historical NOT PUSHED label is
unchanged. This recovery notice supersedes publication status only. The
optimizer, tangent scan and archived exploration histories have not been
regenerated during recovery.

## Scope and fresh checks

The recovery is based on #992 at
`b586b518a8de634444c1e987a0bba03c593198f0`. Recent PRs through #993 and targeted
recovery searches were inspected; no matching recovery was found. This is not
an exhaustive audit of every historical branch or unavailable conversation.
Older packets already published by other PRs are not duplicated. The nested
copy of the pending circle ZIP in the degree-20 delivery is represented only once.

Both original manifests and Git trees were authenticated. The circle finite
report, all 13 optimized negative controls, optional nondirected numeric report,
and the degree-20 diagnostic reproduce their archived outputs. Both accepting
Python modes pass. `VALIDATION.json` records the exact runtime adjustments and
earlier unsuccessful startup attempts. No original research source was edited.
The source24 diagnostic reconstructs its theta input; this does not certify
the candidate or independently review the inherited arithmetic backend.

No inherited proof, another contributor's branch, main or integrated scientific
status is modified. No independent referee, formal proof build or remote
repository-wide CI is claimed. New work must receive its own review.
