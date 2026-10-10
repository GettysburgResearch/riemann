# Build scripts used for the 7/8 Lean check (copied from session scratch)

```text
Status: TOOLING (reproduction aid). No mathematical claim.
Scope: the shell and Python helpers used in ../../reviews/LEAN_BUILD_ATTEMPT.md (Sections 4 and 7,
  Addenda A-C). The absolute scratch path was replaced by ${LEANBUILD}.
Exact sources or dependencies: the pr908 import tree (ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6)
  extracted to ${LEANBUILD}/src; elan installed to ${LEANBUILD}/elan
What was actually run: these scripts, at the timestamps in LEAN_BUILD_ATTEMPT Section 4
Smallest remaining gap: the scripts assume the layout above; the comparator commands are in
  LEAN_BUILD_ATTEMPT Addenda B-C
```

* `env.sh`: sets `ELAN_HOME`, `PATH`, `P` (the Lean project dir), `GLIBC_TUNABLES` and
  `LEAN_NUM_THREADS`.
* `step2_cache.sh`: runs `lake exe cache get`. This also runs the lakefile's `run_cmd`, which
  clones and patches 11 packages.
* `apply_post_update_patches.sh`: applies the other 12 shipped patches, which upstream applies only
  in `lake update`'s `post_update` hook. It first checks that each package HEAD equals its manifest
  revision.
* `step3_build.sh`: the incremental `lake build OAI.NumberTheory.DirichletL.Nonvanishing`.
* `progress.sh`, `closure.py`, `verify_revs.py`: build progress, import closure, and manifest
  revision checks.

Usage: `export LEANBUILD=/some/dir`, extract the import there, then `. env.sh` and run the steps
in order.
