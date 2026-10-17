# Publication status: NOT PUSHED

Observed repository: GettysburgResearch/riemann.
Observed existing branch: research/transport-moments-20261017.
Observed existing PR: #955, draft and open.
Observed existing head/base for this continuation:
6d3d69c7896e3a5d61d1f67e4627125257398ec7.

Intended NEW branch name (not created remotely):
research/native-norm-divisibility-20261017.

This session's discovered GitHub functions provide reads, not branch,
commit, ref-update, file-write or PR-creation actions. The installed plugin
was searched for a publishing alternative; none was available to invoke.
The runtime has git but no gh command, no configured Git credential helper,
and none of GH_TOKEN/GITHUB_TOKEN/GIT_ASKPASS/SSH_AUTH_SOCK set. No credential
values were read or exposed. A git ls-remote attempt failed DNS resolution.
No remote branch, commit, issue, comment or pull request was written.
No assertion that main is globally unchanged by other contributors is made;
this pass has made no changes to it.

The outer download includes a ready-to-apply add-only patch. In an
appropriately authenticated checkout, the intended application is:

    git fetch origin research/transport-moments-20261017
    git switch -c research/native-norm-divisibility-20261017 \
      6d3d69c7896e3a5d61d1f67e4627125257398ec7
    git apply --check /path/to/riemann-native-norm-divisibility-20261017.patch
    git apply /path/to/riemann-native-norm-divisibility-20261017.patch
    python standalone/2026-10-17-native-norm-divisibility/verify.py
    python standalone/2026-10-17-native-norm-divisibility/verify_manifest.py
    git add standalone/2026-10-17-native-norm-divisibility
    git commit -m "research: complete native norm-divisibility covariance at fixed center"
    git push -u origin research/native-norm-divisibility-20261017

These publication commands were NOT run successfully here. The patch
contains no inherited modifications or deletions and does not change any
integrated scientific-status file. The prior fourteen-file unpushed packet
is preserved separately as a companion, not silently included in this patch.

Suggested draft PR title:
Research: complete fixed-center native norm-divisibility covariance.

Suggested review targets:
THEOREMS Sections 3-5: rational rather than ideal divisibility, shared-prime
branches, moving-exclusion continuation without unsafe local division, and
absolute summation of the asymptotic error. Then Section 6 and the integer
interval/tail certificate. Finally verify the remaining-core formula (22)
and the distinction between the new lower bound and the missing upper bound.
