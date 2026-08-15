# T-93920 review front door

This packet freezes PR #495 at

```text
50f45b46cbe3c471d6e702c41c7ef178b530e1ab
```

and accepts review #503 at

```text
db77e5792966edf080604fd4b69fb00f07739681.
```

The exact negative witness `(67,15,1005,14)` is mandatory. `L-91763` and `T-92910` are forbidden.

## New route

```text
bottom anchored finite cells
 -> directed finite Target-Lorenz typed leaves

top anchored finite cells
 -> literal positive finite atoms

complete outer cells
 -> L-91760 direct positive Volterra row

anchored + bulk
 -> one signed retained-cell quadrature defect
 -> one scalar thinning
 -> every ordinary/detail column
 -> native Y4 deficit <3457
 -> frozen one-sided endpoint consumer.
```

No derivative-fibre causal subtraction, rough-lift parent, bulk quantizer, collar, terminal comparison, exported child, or auxiliary port is used.

## Quick validation

```bash
cd experiments/X-93920-review503-hybrid-direct-row
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
```

The checker validates the witness, exact interface firewalls, constants, genealogy, and native-cost arithmetic. It does not replay the directed Target-Lorenz sweep or the Mellin-Landau consumer and does not prove RH.
