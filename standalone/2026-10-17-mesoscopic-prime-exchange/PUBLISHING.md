# Publication status: NOT PUSHED

This session's GitHub connector exposed 48 read-only actions. Searches for
create/write actions returned none. The plugin catalog listed the installed
GitHub integration, not a separate available write connection. The container
has git, but no gh executable; a normal HTTPS request to the pinned public
GitHub source failed DNS resolution. No write or PR creation succeeded, and
no remote head or PR number is claimed.

The live base checked on 17 October 2026 is PR #953:

    a93d382951f8fac7b0c28783061a7ddb99fcf0a4

The add-only patch places this packet under:

    standalone/2026-10-17-mesoscopic-prime-exchange/

It changes no inherited file. The patch was applied and its checks replayed
in a LOCAL fixture. That fixture is not a full repository clone. Applying
the same new-file patch does not require cherry-picking #954: all mathematical
arguments used are resident here; #954 is cited for context and credit.

Intended branch:

    research/mesoscopic-prime-exchange-20261017

The draft PR text is in draft_pr.md. Before creating a real branch/PR, verify
that the base is still appropriate, apply the patch without overwriting a
pre-existing packet, and rerun the exact checker and manifest verification.
Do not substitute a local fixture commit or packet hash for a GitHub commit.
