# X-104570 — Modular dual-route hardening replay

This is a lightweight exact-algebra replay for the continuation of PR #720.

It verifies:

```text
the negative 2x2 origin minor of the mixed theta matrix;
the strict likelihood-ratio derivative identity;
the polynomial derivatives in the complete modular integration formula;
the symbolic local-moment positivity radius;
the negative leading coefficient of every fixed-cutoff Laguerre tail;
the normalization of the modular jet-correction basis.
```

Run:

```bash
python3 verify.py --output /tmp/t104570.json
cmp /tmp/t104570.json results/verification.json
```

The replay does not evaluate Xi, prove global positive definiteness, produce
cofinal directed margins, derive `alpha_2` from `alpha_3`, or prove RH.