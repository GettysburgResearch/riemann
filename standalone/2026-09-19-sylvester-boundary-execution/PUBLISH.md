# Publication handoff — NOT a claim of a successful push

## Exact intended destination

```text
repository: GettysburgResearch/riemann
existing PR: #903 (draft)
branch: research/sylvester-cutoff-boundary-20260919
observed old head: 67132424e3cbe35a94752581a5b5271ab8bfc56f
stacked programme: #848
new add-only directory: standalone/2026-09-19-sylvester-boundary-execution/
```

The current #848 head read during this pass was
`7de75c02417d5d8db7eafb1ceba364380e72d16a`; it includes the independent
rough-squareclass packet absent from #903's older parent. Do not reset
that work or overwrite any concurrent branch updates.

This authoring session successfully read the repository. Its GitHub
connector exposed no write operation; the plugin directory confirmed
GitHub installed rather than disconnected. A direct clone failed with
`Could not resolve host: github.com`. No remote commit, comment, PR edit,
or branch update was made by this pass.

## Safe publication sequence

Use an authenticated checkout with a clean worktree. Fetch and use the
CURRENT target branch, not the frozen old SHA. Apply the add-only patch
(or copy the included new directory), then run the four replay commands
in both ordinary and optimized Python modes. Preserve all earlier files.

A typical publisher sequence, with the supplied patch path substituted:

```bash
git fetch origin research/sylvester-cutoff-boundary-20260919
git switch research/sylvester-cutoff-boundary-20260919
git merge --ff-only origin/research/sylvester-cutoff-boundary-20260919
git apply --check /path/to/riemann-bcp26-continuation.patch
git apply /path/to/riemann-bcp26-continuation.patch
cd standalone/2026-09-19-sylvester-boundary-execution
sha256sum -c SHA256SUMS
python -S -B boundary.py --check result.json
python -S -B verify.py result.json
python -S -B lfamily.py --check lfamily_result.json
python -S -B -m unittest -v test_boundary
python -S -O -B boundary.py --check result.json
python -S -O -B verify.py result.json
python -S -O -B lfamily.py --check lfamily_result.json
python -S -O -B -m unittest -v test_boundary
cd ../..
git add standalone/2026-09-19-sylvester-boundary-execution
git commit -m "research: execute cutoff-pivot collapse and native covariance audit"
git push origin HEAD:research/sylvester-cutoff-boundary-20260919
```

Create the local tracking branch first if it does not already exist.
Never force push. A concurrent remote advance should cause an ordinary
push rejection; reconcile it without deleting work, replay, and retry.
Read back the remote head and compare the new directory's hashes.

Then comment on #903 and cross-reference #848/#902 and #738. Use the
summary in REPO_COMMENT.md, adding the ACTUAL published SHA and a fresh
publisher validation receipt. Keep this historical no-push receipt
unchanged; add a new PUBLISHER.md rather than rewriting what happened.

No workflow changes, accepted-claim promotions, or broad CI campaign are
part of this handoff. The old malformed prose remains historical; direct
readers to the correctly escaped formulas in this executed continuation.
