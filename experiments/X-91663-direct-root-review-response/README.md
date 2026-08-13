# X-91663 — direct-row response to PR #450

This exact-rational replay supports `R-91655`, `L-91663--L-91665` and
`T-91653`. It checks:

- the corrected two entropy bases at `67`;
- the elementary derivative margin used for the global fixed-67 inequality;
- the Möbius convolution behind `Gamma(c_X)=w_X`;
- the corresponding radix-four identity;
- the literal parent-minus-child-plus-replacement capacity inequality;
- the exact failure of the obsolete `P_61<9/2` port bound and validity of the corrected `<14/3` bound;
- the explicit `P_61` terminal constant `<3600`;
- unique least-prime partition of rough integers in a finite structural replay;
- the coefficient-one factor-67 logarithmic iteration;
- shape and uniqueness of the frozen claim blobs.

It does **not** replay the expensive Hall-prefix, normalized-row, source-tree,
finite mismatch, collar, omission or terminal-annulus certificates. Those are
imported as frozen proof objects and remain the independent-review boundary.
The replay does not establish RH.

Run:

```bash
python3 verify.py --json results/verification.json
sha256sum -c SHA256SUMS
```

Expected:

```text
PASS_DIRECT_ROOT_REVIEW_RESPONSE
```
