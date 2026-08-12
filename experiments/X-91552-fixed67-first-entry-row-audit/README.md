# X-91552 — Exact fixed-`67` first-entry row audit

This checker proves the complete fixed-scale component-row theorem in
`L-91552`.

For every real `2 <= j <= y < 67`, with `x=67y`, it evaluates

```text
A_j(x),
A_j(x)-A_j(x/67),
A_j(x)-67^(-1/2)A_j(x/67),
```

where `A_j` is the exact `P_61` finite-Euler component row.

Each quantity is affine in `log x` on every integer activation cell.  The
replay checks both endpoints of all `143,715` cells, giving `862,290` directed
inequalities.

All square roots and logarithms use integer outward intervals at scale `10^35`.
No floating-point sign decision is used.

Run:

```bash
python3 verify.py > /tmp/verification.json
cmp /tmp/verification.json results/verification.json
python3 -m py_compile verify.py
```

Expected verdict:

```text
PASS_FIXED67_FIRST_ENTRY_ROW_AUDIT
```

This is an independent fixed-scale audit.  It does not by itself verify the
full factor-54 composition or prove RH.
