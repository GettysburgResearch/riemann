# X-18508 immutable bundle

The complete first-growing common-ledger producer, exact consumer, inputs,
retained generated proof object, verification result, and mutation suite are
stored as base64 transport chunks in

```text
bundle/bundle.part00
...
bundle/bundle.part07
```

Reconstruct with

```bash
cat bundle/bundle.part* \
  | base64 -d \
  > X-18508-c10-n2-common-profile-soft.bundle.tar.gz

sha256sum X-18508-c10-n2-common-profile-soft.bundle.tar.gz
# 784a9e8e5b286d500f4cb60e6e3292f65195174316f031c866ee8077045b9a00

tar -xzf X-18508-c10-n2-common-profile-soft.bundle.tar.gz
```

The extracted bundle contains:

```text
build_ledger.py
verify.py
tests/test_verify.py
README.md
L-18513.md
X-18508.md
SHA256SUMS
artifacts/c10-N2-common-ledger.json.gz
artifacts/c10-N2-common-summary.json
artifacts/c10-N2-common-verification.json
artifacts/c10-N2-p384.json
artifacts/c10-N2-trial.json
artifacts/zero-config.json
artifacts/tests.txt
```

Replay:

```bash
gzip -dc artifacts/c10-N2-common-ledger.json.gz \
  > artifacts/c10-N2-common-ledger.json

python verify.py artifacts/c10-N2-common-ledger.json \
  --arithmetic artifacts/c10-N2-p384.json \
  --zeros artifacts/zero-config.json \
  --output /tmp/x18508-verification.json

PYTHONPATH=. python -m unittest discover -s tests -v
sha256sum -c SHA256SUMS
```

The exact mathematical proof-object SHA-256 is

```text
55a98486f0b07f3fd7fa729808863304b10b9cda101e0687eeaf874a4484a3f6
```

and the retained verdict is

```text
CERTIFIED_FIRST_GROWING_C10_N2_COMMON_PROFILE_SOFT_LEDGER
```

This bundle was generated and independently consumed with directed arithmetic
in the active execution environment. GitHub Actions are currently not
scheduling in this repository, so it is not represented as a hosted Actions
artifact.
