# X-91128 — `P_79` first-moment splice certificate

This exact `Fraction` replay enumerates every squarefree `P_79` divisor below
`83` and proves

```text
A_P79(y) <= 1,  1 <= y < 83.
```

Combined with the retained parent-prefix theorem

```text
A_P79(x) > 1/25,  x >= 83,
```

it yields

```text
A_P79(py)-A_P79(y)/p > 1/25-1/83 = 58/2075
```

for every `p>=83`, `1<=y<83`.

Replay:

```bash
python3 verify.py
```

Expected verdict:

```text
PASS_P79_CHILD_FIRST_MOMENT_UPPER
```
