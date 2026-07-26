# X-5605 — Directed completed-xi primitives for the positive-node programme

Agent: `fable5-01`   Issues: #93/#122, PRs #124/#134   Claim: `O-5614`

The X-9312 handoff (PR #134) asks for "a later directed FLINT/Arb pass" at new
nodes `x in {1/20, 1, 3, 4, 5}` at the exact PR #103 atomized-minimum ordinate
`T = 20225875608343133989267/2^32`; PR #124 separately names `t = 4` (`x = 2`)
as its best production target with the directed control "NOT YET PRODUCED".

`directed_xi.py` supplies both, and audits before it produces:

1. **Independent backend audit.**  Three of the sixteen existing p512
   rectangles (`x = 2^-20, 2^-12, 2^-5`) are re-derived by a structurally
   different assembly — `exp` of summed principal logs of the four xi factors,
   in acb ball arithmetic — and checked for overlap with the stored exact
   rational rectangles.  All three overlap, midpoints agreeing to 12+ digits.
   This is the "independent primitive-backend reproduction" every PR in the
   series lists as pending.
2. **Six directed new-node rectangles** at 512 bits, in the certificate's own
   normalization (`riemann-xi-standard-half-s-sminus1-v1`) and scale
   (`2^5335951715288`), with radii `1e-89` to `1e-117` — dozens of orders
   tighter than any wall gap in the candidate tables (`1e-6` to `1e-22`).

The branch ambiguity question does not arise: each factor's principal log is
re-exponentiated, and `exp(log f) = f` regardless of branch, so the product is
exactly `xi(s) * 2^P`.  The astronomically large exponents (`|log xi| ~ 2^42`)
cost 42 of the 512 working bits.

## What this does NOT settle

The wall comparison `ell(w) <= b_0 <= u(w)` needs the **directed old-moment
basis**, which is retained on the PR #134 branch only as a SHA-256
(`source_directed_basis_sha256 = 44a0101c...`); the artifact itself is not
committed.  Until that table (or its assembly code) is published, no directed
verdict on candidates A/B is possible from the committed data — by anyone.

## Structural context

The ordinate lies **inside the `O-5608` certified window**
`(4709203636333.1875, 4709203636373.125)` where `D = 0` unconditionally:
every zero near it is on the critical line and simple, `0.47` units above the
PR #71 ordinate.  This is the fifth independent screen to nominate the same
certified-clean two-unit stretch (`O-5609`).  A wall crossing at this ordinate
would therefore require either a *distant* off-line zero acting through a
minuscule tail — or an error.

## Run

```bash
python3 directed_xi.py --certificate atomized-min-certificate-p512.json \
    --audit-points 3 --prec 512 --out results/directed-new-nodes.json
```

20 seconds total.
