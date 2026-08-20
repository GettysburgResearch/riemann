# T99810 publication handoff

Repository: `gfreund123/riemann`

Base:

```text
PR #659
research/gpt56-pro/99800-canonical-scalar-spine-gpmoc
83c17b32a99ac9e1aa5aec3168535550eb286636
```

Suggested branch:

```text
review/gpt56-pro/99810-canonical-proof-spine
```

Suggested draft PR title:

```text
review: canonical RH proof spine and Euler–Hausdorff completion firewall (T99810)
```

All changes are add-only. Apply the companion patch or copy the packet files,
run the replay and checksum ledger, push the branch, open a draft PR using
`PR_BODY_99810.md`, and read back the final head, file list, verification JSON,
and checksum ledger before claiming publication.

The authored packet originally froze PR #656 and used T99800.  Because PR #659
now canonically owns that namespace, this publication mechanically migrates
the suite to T99810 and records the mapping in
`t99810-namespace-migration.json`.

Scientific status is binding: RH is unproved and the Abelian-to-Carleson
cross-core localization remains open/RH-equivalent.
