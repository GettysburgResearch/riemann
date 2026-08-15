# X-93601 — Target-Lorenz two-ledger native endpoint replay

This exact-rational regression checks the finite algebra and type firewalls of
`L-93603--L-93605`.

It verifies:

- the leftmost common-source removal and the exact identity
  `residual row + bonus = even row - odd row`;
- positive source-Fubini across multiple labelled leaves;
- strict separation of positive source stages from signed observation errors;
- the exact all-column thinning reserve
  `(sqrt(K)+129)/(sqrt(K)+130)<1`;
- the direct native `Y_4` charge `60989<61000`;
- an empty exported recursive family and zero root-global port;
- eight hostile mutations, including full-child-capacity promotion and the
  RH-bearing benchmark bridge.

Replay:

```bash
python3 verify.py --output results/verification.json
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_TARGET_LORENZ_TWO_LEDGER_NATIVE_ENDPOINT_PACKET
```

The replay does not replace reconstruction of the source-tree measure, endpoint
frame, analytic all-column estimates, Tail-AVLT, or endpoint-to-RH consumer.
