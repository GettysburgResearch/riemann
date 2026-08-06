# X-18508 — First growing common profile-soft ledger (`c=10,N=2`)

This directory contains the first growing level of the X-18506 source-canonical
schedule assembled with the profile/support-phase and PR #191 direct-short
interfaces.

## Actual finite support

```text
c = 10
N = 2
sector = unnormalised even [e0,e-1+e1,e-2+e2]
metric = diag(1,2,2)
prime powers = 2,3,4,5,7,8,9
arithmetic precision = 384 bits
profile fixed-point precision = 320 bits
```

The arithmetic primitive contains the complete cutoff-free D-0001 pole,
archimedean and prime-power matrices. The profile producer evaluates twenty
proof-grade critical-line rows and their derivatives with respect to `log(c)`.

## Directed profile gates

The positive zero-profile and graph Grams are

```text
D = 2 sum v_gamma v_gamma^T
K = 2 sum [v_gamma v_gamma^T + dot(v_gamma) dot(v_gamma)^T].
```

The exact consumer proves

```text
K <= 44 G.
```

At `tau=10^-6`, both `D-tau G` and `D-2 tau G` have inertia `(-,+,+)`.
Thus the exact generalized profile spectrum has one soft eigenvalue, no
eigenvalue in `[tau,2 tau]`, and two hard eigenvalues. The exported rational
soft graph satisfies

```text
soft Rayleigh upper       3.68893058564543e-9
hard profile floor        4.00000000000000e-5
projector sin^2 bound     8.14984488401341e-21.
```

## Complete arithmetic sign

A direct interval LDL replay proves the complete matrix inequality

```text
A >= 10^-9 G.
```

Consequently the exact Schur complement on the actual spectral soft line is at
least `10^-9 G_soft`, independently of the rational graph enclosure.

An explicit PR #191 trial solve on the frozen rational soft/hard graph also
proves

```text
normalised direct lower       > 5.33647759369972e-9
normalised shifted LDL        > 4.33647759369972e-9
normalised exact Schur        > 5.33647759369972e-9
negative part upper             0.
```

## Replay

```bash
python build_ledger.py \
  --arithmetic artifacts/c10-N2-p384.json \
  --zeros artifacts/zero-config.json \
  --output artifacts/c10-N2-common-ledger.json \
  --summary artifacts/c10-N2-common-summary.json

python verify.py artifacts/c10-N2-common-ledger.json \
  --arithmetic artifacts/c10-N2-p384.json \
  --zeros artifacts/zero-config.json \
  --output artifacts/c10-N2-common-verification.json

PYTHONPATH=. python -m unittest discover -s tests -v
```

The complete generated ledger is preserved as deterministic gzip/base64
transport. Decode with

```bash
base64 -d artifacts/c10-N2-common-ledger.json.gz.b64 \
  | gzip -dc > artifacts/c10-N2-common-ledger.json
```

## Scope

This is a real directed finite level and the first growing X-18506 packet. It is
not an unbounded passing theorem and is not yet the complete augmented
Suzuki/CCM hierarchy. GitHub Actions are disabled/not scheduling in the current
repository state, so the committed artifact was generated and independently
consumed in the active execution environment rather than by a hosted Actions
run.
