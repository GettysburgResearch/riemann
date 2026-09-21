# BCP26 publisher handoff

Published as an additive continuation of [PR #903](https://github.com/GettysburgResearch/riemann/pull/903),
on the current parent `36ffd15df96866a3f1c4f306000dd4a4dbf4153b`.
All 18 archive files were preserved byte for byte; publisher notes and
execution receipts are separate additions. The author's no-push notes remain
historical records of that authoring session.

The branch had advanced since the packet's observed head
`67132424e3cbe35a94752581a5b5271ab8bfc56f`. It already contained RCB26 and a
substantial SBC26 correction/execution pass under
`standalone/2026-09-19-sylvester-cutoff-boundary/`. Those existing files were
not overwritten. This BCP26 directory is a parallel continuation with
overlapping themes, not an assertion that the current SBC26 packet is still
the original untested sketch. Its introduction and audit address the earlier
snapshot. Reviewers should compare the distinct partitions, source adapters,
and L-family fixtures before consolidating the two accounts.

[PUBLISHER_REPLAY.json](PUBLISHER_REPLAY.json) records all eight successful
Windows/Python 3.12.10 commands: boundary reconstruction, separate verifier,
L-family reconstruction, and the 12-method regression suite, each in normal
and optimized mode. Supplied SHA256SUMS entries match. These are finite
software replays, not independent mathematical acceptance. No full repository
validator, earlier packet replay, external theorem verification, Lean build,
or remote CI success is claimed. RH and GRH remain open.
