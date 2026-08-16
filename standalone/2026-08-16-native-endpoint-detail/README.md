# T-94100 standalone review front door

Base: PR #511 at exact head
`6ece82279cb03474ebc79914db572f6ff095d238`.

Status: unconditional finite native compiler plus an exact asymptotic frontier;
RH remains unproved.

## Review order

1. `R-94100` — exact cone equivalence and separator.
2. `L-94100` — positive radix-four detail of every endpoint atom.
3. `L-94101` — backward native-detail greedy and exact slack identity.
4. `L-94102` — blocker support and `Y_4` price.
5. `T-94100` — complete status and endpoint implication.
6. `X-94100` generator, replay, unit tests and retained certificates.
7. `imports/t94100/IMPORT_MANIFEST.json` and integration lock.

## Immediate falsifiers

Reject the finite compiler at the first occurrence of:

```text
one negative endpoint row atom;
one nonpositive Delta_T(q) with 2<=q<T;
a q or 4q response using a different lambda_T;
a negative greedy residual;
an ordinary or detail overdraw;
a mismatch between common-row q/4q detail and summed atom detail;
a mismatch between literal score and the Y4 pairing;
an unowned endpoint coefficient;
a hidden Möbius child, rough lift, port, or benchmark bridge;
finite blocker reconnaissance promoted to NEDB.
```

The packet passes as an RH proposal only if a separate proof establishes the
stated asymptotic blocker bound and the frozen endpoint consumer survives
reconstruction.
