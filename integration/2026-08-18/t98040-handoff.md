# T98040 publication handoff

Suggested publication base:

```text
PR #603
head 1dac3eeccb5a01183067c00722d92fbcf2df12c5
```

Suggested branch:

```text
research/gpt56-pro/98040-dickman-stieltjes-corridor
```

Collision-safe publication mapping:

```text
original packet T/L/M/O/X-98030 -> repository T/L/M/O/X-98040
original packet L-98031         -> repository L-98041
original packet L-98032         -> repository L-98042
```

The original packet is
`riemann-dickman-stieltjes-corridor-2026-08-18.zip`, SHA-256
`aa24baf58c3c23e4a04d486e346584f88a90c9a947d4378e3cc4755be2371e3d`.
Only identifiers, paths, publication provenance, and checksum ledgers changed.
Two serialized carriage-return bytes in `L-98040` were restored to the
literal TeX sequence `\\rm`; this is an encoding repair only.
Metadata hard breaks were normalized from trailing spaces to explicit
`<br>` tags.

Suggested draft PR title:

```text
advance: complete-base Stieltjes transfer and mesoscopic Dickman corridor
```

The packet is add-only. Before publication:

1. replay `experiments/X-98040-dickman-stieltjes/verify.py`;
2. check `T98040_CONTENT_SHA256SUMS`;
3. preserve the exact base SHA in the PR body;
4. do not claim GPC67, CBRC67 or RH;
5. compare against any newer critical-saddle successor and re-identify claim
   numbers only if a collision has occurred.
