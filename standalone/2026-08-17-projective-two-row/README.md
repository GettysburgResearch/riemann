# T-96400 standalone review front door

The packet abandons the endpoint-blocker statement as a load-bearing RH gate
and proposes a direct two-row Mellin–Landau closure.

Replay:

```bash
cd experiments/X-96400-projective-two-row
python3 verify.py --mutations --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c PROJECTIVE_TWO_ROW_96400_SHA256SUMS
```

Expected verdict:

```text
PASS_T96400_PROJECTIVE_STOPPING_LINE_TWO_ROW
```

The replay checks exact finite algebra and type firewalls.  It does not replay
the full directed Hall campaign or prove RH.
