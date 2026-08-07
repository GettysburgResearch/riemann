# X-15416 — Terminal Euler geometry regression

This standard-library-only regression accompanies `R-15407`, `L-15449`, and
`L-15450`.

It verifies the exact finite algebra that a reviewer should check before the
analytic bounded-variation estimate:

1. the true solution step for
   ```text
   av-bq=r
   ```
   is `(q/g,v/g)`, where `g=gcd(q,v)`;
2. the mandatory noncoprime mutation
   ```text
   q=v=5, r=5
   ```
   has three reduced residue chains under the false shift `(5,5)` and true step
   `(1,1)`;
3. the coprime control `q=5,v=6,r=1` has the expected single chain;
4. the noncoprime control `q=8,v=12,r=4` has true step `(2,3)`;
5. finite-difference moment identities vanish through order eight;
6. the terminal amplitude and energy exponents are strictly negative for five
   fixed reserves below `1/2`;
7. at `delta=1/5`, `K=6`, one has `1/K<delta`, excluding a truncated
   `X^(1/K)` variable from the terminal large side.

Run:

```bash
python3 verify.py
python3 -m unittest discover -s tests -v
```

Retained verdict:

```text
SYNTHETIC_TERMINAL_EULER_GEOMETRY_VERIFIED
```

The locally executed source/result digests at publication were:

```text
verify.py SHA-256
1b8b88fdb3252575dd3e7898c9bac48a9b3d450cc6e194408a34db8a106bbf5e

verification.json SHA-256
cd0228cc403b34fb5e509fcc78eba51c955cc66bcaccbff4bce3f9a13e43bf60
```

## Scope boundary

This regression does **not** independently prove:

- the periodic-Bernoulli Euler formula for compact BV functions;
- the derivative integral in `L-15449`;
- the exhaustive terminal reduction for the full production dictionary;
- the balanced Type-II theorem `BTP(K)`;
- RH.

Those remain analytic and source-coverage review obligations. The regression's
purpose is to ensure that the rejected Farey chain cannot silently re-enter the
replacement proposal and that the terminal exponent ledger is internally
consistent.
