# Hostile reconstruction specification

Reject at the first failure of:

```text
PR #488 base SHA is not exact;
odd Hall marginal is not exhausted;
even Hall capacity is overdrawn;
matched plus residual even mass is not exact;
profile difference is negative on an active edge;
rough monomial receives two first owners;
child is named but has no positive physical placement;
endpoint cells are not a tagged complete union;
quantizer depends on source or colour;
quantizer is applied more than once;
thinning has no discard marginal;
signed comparison is called positive source;
all-column domination fails;
Y4 uses a signed error without absolute domination;
checksum or frozen Git blob fails;
endpoint consumer imports the forbidden benchmark bridge.
```

Replay:

```bash
cd experiments/X-91850-physical-coupling
python3 physical_coupling.py
python3 verify.py --output results/verification.json
python3 -m unittest discover -s tests -v
cd ../..
sha256sum -c standalone/2026-08-15-physical-coupling-compiler/CONTENT_SHA256SUMS
sha256sum -c FACTOR67_91850_SHA256SUMS
```
