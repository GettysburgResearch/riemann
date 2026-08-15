# T-93920 publication handoff

## Intended genealogy

```text
repository: gfreund123/riemann
base PR:    #495
base branch: research/gpt56-pro/91760-native-volterra-common-parent
base SHA:   50f45b46cbe3c471d6e702c41c7ef178b530e1ab

review answered:
PR #503 at db77e5792966edf080604fd4b69fb00f07739681

new branch:
research/gpt56-pro/93920-review503-hybrid-direct-row
```

## Frozen imports

```text
PR #508 Target-Lorenz directed hardening:
4ae97dffd1f76ed3244b8f3028560ffa80663caf

PR #352 prime endpoint/Mellin consumer:
906b5a477a1ed7c88a40db7569924f15f3d54b72

PR #353 prime-square moat:
ed566f3198e236c54ba18049181016536f56d456
```

PR #509 at `e01daee9cdfea35d2a7d2591f1df6c8080084119` is comparison-only and is not a theorem antecedent.

## Commit

```text
review503: replace derivative causality by anchored/Volterra direct row
```

## Validation

```bash
cd experiments/X-93920-review503-hybrid-direct-row
python3 verify.py certificates/control.json --output results/verification.json
python3 -m unittest discover -s tests -v
python3 -m py_compile verify.py tests/test_verify.py
sha256sum -c SHA256SUMS
cd ../..
sha256sum -c standalone/2026-08-16-review503-hybrid-direct-row/CONTENT_SHA256SUMS
sha256sum -c T93920_CONTENT_SHA256SUMS
```

Expected verdict:

```text
PASS_REVIEW503_SAFE_ANCHORED_VOLTERRA_DIRECT_ROW
```

The publication must remain a draft. RH remains unproved pending independent reconstruction.
