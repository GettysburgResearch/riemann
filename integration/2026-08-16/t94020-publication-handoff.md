# T-94020 publication handoff

## Freeze

```text
repository:       gfreund123/riemann
base PR:          #508
base branch:      research/gpt56-pro/93780-target-lorenz-directed-hardening
base head:        4ae97dffd1f76ed3244b8f3028560ffa80663caf
base tree:        7f63bb7c2aeb08d79ef0bbab04181027d5fb3547
intended branch:  research/gpt56-pro/94020-target-lorenz-live-marginal
main at cutoff:   9c7538559d7f56c2914b39aed5a1fb3fbf7ce131
```

PR #508 is frozen.  This packet is add-only and does not rerun or replace its
full directed tail campaign.

## Review order

```text
R-94020
L-94020
X-94020 full certificate files
L-94021
L-94022
L-94023
M-94020
L-94024
T-94020
O-94020
report and claim-status audit
lock and checksum ledgers
```

## Decisive result

Review #504's missing endpoint/source/path data are now explicit.  The same
reconstruction proves that the actual oriented rough-child aggregate has a
strictly negative ordinary/detail `q=2` coordinate.  Therefore it cannot be
placed as separately nonnegative physical children.

The remaining producer is one joint finite-forcing/oriented-child coupling
before positive physical observation.  It is specified as an exact
primal/Farkas problem (`JNTLC`) and remains open.

## Replay

```bash
cd experiments/X-94020-live-endpoint-source
python3 verify.py --output /tmp/x94020.json
cmp /tmp/x94020.json results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile generate.py verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c TARGET_LORENZ_94020_PACKET_SHA256SUMS
```

Expected:

```text
PASS_LIVE_ENDPOINT_SOURCE_TREE_AND_JOINT_CANCELLATION_GATE
```

## First falsifiers

```text
one occurrence has an inconsistent P61/rough factorization;
one source atom has two first owners;
the finite boundary witness is silently identified with a paired SHARP atom;
the terminal (67,13) leaf has a cloned rather than beta-weighted parent;
an actual oriented child is declared a nonnegative row;
ordinary q and 4q use different coefficient systems;
a signed finite comparison enters positive source;
JNTLC is described as solved without a symbolic/directed proof object;
RH is promoted before JNTLC and the frozen endpoint inputs are reconstructed.
```
