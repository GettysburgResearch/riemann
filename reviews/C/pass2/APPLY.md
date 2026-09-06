# Applying the prepared review-only patch

This packet was **not pushed** by Reviewer C. The active connector exposed no GitHub write actions. The existing target is PR #798, branch `review/C/2026-09-05-post-release-audit`, exact head:

```text
7466ad8081101508be7c7acf0065cb2e0944a639
```

Use a clean disposable checkout of that branch, not main or a research branch. First inspect the downloaded patch and its external SHA256 receipt. Replace the path below with the patch location:

```sh
git switch review/C/2026-09-05-post-release-audit
test "$(git rev-parse HEAD)" = 7466ad8081101508be7c7acf0065cb2e0944a639
test -z "$(git status --porcelain)"
git apply --check /path/to/reviewer_C_pass2.patch
git apply /path/to/reviewer_C_pass2.patch
python reviews/C/check_census.py
python -O reviews/C/check_census.py
python reviews/C/pass2/scripts/validate_pass2.py
python -O reviews/C/pass2/scripts/validate_pass2.py
git diff --stat
```

The expected change is confined to `reviews/C/`. No production `.github`, `formal`, `canonical`, `claims`, main-branch or research-branch edit is part of this patch. Seven existing review files are updated and their original bytes are archived under `pass2/evidence/`. Any subsequent commit/push is a separate explicit publication action; this packet supplies neither a fictitious new head SHA nor a claim that PR #798 already contains the second pass.

The local application test authenticates the seven materialized original Git blobs, applies the patch to those original files in a temporary Git index, and compares every resulting review file byte-for-byte. It is **not** a full repository checkout/build or test of live branch protections. The application receipt is supplied beside the ZIP/patch, avoiding a self-referential patch digest inside the patch.

The ZIP is the proposed review file set, not a full clone of the repository or a replacement for unchanged first-pass evidence already in PR #798. Bounded Python/grep checks can run from the ZIP's root; the optional, uncompiled Lean regression requires the real pinned repository and dependencies.
