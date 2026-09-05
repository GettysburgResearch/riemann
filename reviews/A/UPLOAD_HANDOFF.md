# Publication handoff

Target repository: GettysburgResearch/riemann.
Target review PR: #795.
Target review branch: review/2026-09-05/A-scientific-post707.
Scientific baseline: 8d16f8d9c475db290bc85e53d775b93b9bcdb336.
Last previously verified review head: f184ca0895713aa5323321ac482a11aeb2e6284b.
**That old head does not contain this continuation and is not a publication receipt.**

The user authorized an uploader to publish the preliminary ZIP. Fetch the
actual review branch first and preserve that upload and any unrelated files.
Copy this packet's `reviews/A/` files onto the review branch only. Do not
check out or commit to main or any original research branch. Do not force
push. The old handoff is preserved byte-for-byte in `prior-pass/`.

Run:

    python reviews/A/replay/run_replay.py
    python reviews/A/replay/validate_packet.py
    git diff --check

Stage only the intended `reviews/A/` additions/updates, commit and push
normally. Update #795 to identify this as an independent first-pass scientific
review with scoped holds. Do not label it an exhaustive completed review,
an RH proof, a rejection of every research route, or an independent
acceptance of A-authored work. Link OMISSIONS.md in the PR body.

After pushing, verify the remote PR head and the changed paths. Record the
exact full new SHA in the uploader's receipt and final response. Keep that
receipt outside the self-hashed commit contents to avoid a circular SHA.
If the review branch has moved concurrently, rebase/merge the review-only
changes normally; do not overwrite a moved ref or a research source.

The packet's SHA256SUMS checks its own files, not external source bytes.
SOURCES.tsv records previously inspected external/repository blob identities.
A fresh acquisition receipt is a separate object and must state actual
successes, failures and unread sources.
