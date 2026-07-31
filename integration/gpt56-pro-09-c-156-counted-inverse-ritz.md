# Integration handoff — counted inverse–Ritz lower floor

Stack this branch after PR #157.

## Consume from PR #152 / PR #155

- exact localized operator normalization;
- a certified count cap `d` below `Gamma`;
- ideally the exact symbol cells and count proof digest.

## Consume from PR #157

- exactly `d` independent repaired radical sources;
- localized trial vectors and source hashes;
- complete directed `A` and `A^2` packet forms.

## Run

```bash
cd experiments/X-15601-counted-inverse-ritz
python verify.py certificate.json --output verification.json
```

## Promotion gate

A per-level result is a valid ambient floor only when:

```text
count cap == packet dimension
H_upper < 0
K_lower > 0
q K_upper - H_upper >= 0
q < 0
```

The final value is

```text
F = t + 1/q.
```

RH promotion requires a symbolic cofinal theorem proving `liminf F>=0`; a finite
list or fitted decay curve is not sufficient.
