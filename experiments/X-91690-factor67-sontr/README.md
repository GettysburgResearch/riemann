# X-91690 — Factor-67 target-Hall SONTR root packet

This replay authenticates the new compact arithmetic and analytic inequalities
used by `L-91690`, `L-91691` and `T-91660`.

## Run

```bash
python3 verify.py
python3 -m py_compile verify.py
sha256sum -c SHA256SUMS
```

Expected classification:

```text
PASS_FACTOR67_TARGET_HALL_SONTR_ROOT_PACKET
```

Expected proof-object digest:

```text
37774aeb5a1843c75ce14b8a0a6c167f743faa60e9582d2939acf6d7addce53a
```

## What is checked

The verifier uses exact `Fraction` arithmetic and outward rational intervals for
square roots and logarithms. It checks:

```text
66 arithmetic cells for equality/reserve positivity below 67;
all 22 active odd target-Hall thresholds;
the strict uniform target-Hall margin 7/20;
the score-per-target derivative orientation;
the imported row-per-target interface declaration;
C67<19 and every propagated mismatch constant;
177/K interior correction and 4452<5033 terminal reserve;
1/sqrt(67)<1/8;
the nonzero finite/continuum firewall.
```

## What is not checked

The replay is not a standalone proof of SONTR, NRCT or RH. Independent review
must reconstruct the frozen endpoint-frame integration, positive quantizer,
exact inner renewal, causal typed reset, common-port ledger, subcritical envelope
and endpoint-to-RH consumer.
