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

## Dependency-hygiene finding

The moment chain runs `L-9314 -> L-9310 -> L-9309 (basis portfolios) -> L-9308
(frozen residual functional)`.  On the PR #134 stack, **`L-9308` and `L-9309`
have no claim files** — they are cited (L-9310 quotes L-9309's inverse formula
inline) but never committed, the same pattern `opus5-01` recorded for
`L-4701`/`L-4702` on the Pick branch.  Combined with the uncommitted basis
artifact, the complete directed pipeline for the candidates is not
reconstructible from any committed data.  The precise requests, in order of
value: (1) the directed basis table behind `source_directed_basis_sha256`,
(2) the `L-9308` residual-functional definition, (3) the `L-9309` file.

## The directed verdict (directed_walls.py)

The missing basis turned out to be reconstructible after all:
`X-9306/basis_check.py`, committed on the PR #134 stack, pins every
convention of the moment pipeline in executable code.  `directed_walls.py`
re-implements it with Arb ball logs in place of the exact-atanh layer (the
`2^P` scale cancels identically because every basis vector sums to zero),
regenerates the sixteen old primitives at 768 bits with the audited X-5605
assembly, computes the old moments and the full seventeen-node `b0`
contraction as balls, and evaluates both Schur walls in ball linear algebra.

Validation oracle: their 70-digit scan rows, reproduced at every node to
10-11 digits by the ball midpoints before any verdict was read.

```text
x       lower_gap  b0 - ell(w)                upper_gap  u(w) - b0            verdict
1/20    [11.5671160272    +/- 1.2e-11]        [6159.30465951  +/- 3.2e-9]     CERTIFIED_INSIDE
1       [4.05033367723e-6 +/- 2.8e-18]        [1.4586e-5      +/- 1.9e-17]    CERTIFIED_INSIDE
2       [2.85749894842e-12 +/- 3.2e-24]       [6.6525e-12     +/- 7.7e-25]    CERTIFIED_INSIDE
3       [1.31596927237e-16 +/- 1.8e-29]       [2.6826e-16     +/- 4.2e-28]    CERTIFIED_INSIDE
4       [6.64128787395e-20 +/- 4.3e-32]       [1.2622e-19     +/- 1.0e-32]    CERTIFIED_INSIDE
5       [1.49293147674e-22 +/- 2.2e-35]       [2.67588739818e-22 +/- 3.1e-34] CERTIFIED_INSIDE
```

**Candidate A (`x = 1/20`) and Candidate B (`x = 5`) are both closed**: the
new scalar sits strictly inside its admissible interval at every tested node,
rigorously.  PR #124's `t = 4` directed control (`x = 2` here) is likewise
produced and inside.  No RH-disproof nomination; the degree-15 positive-node
extension cone at this ordinate is certified positive at all six nodes.

At the first pass, using their p512 table, `x = 5` was UNDECIDED: the old
rectangles' widths propagate through the ill-conditioned basis to moment
radii `~1e-21`, larger than the `1.5e-22` gap.  Regenerating the table at
768 bits (40 s for all sixteen points) shrank the radii below `1e-34` and
decided it.  The conditioning of the 16-node basis costs roughly `10^120` —
the same class of collapse `R-5603` measured on the Pick side — and is why
"raw moat" ranking misleads, exactly as PR #134's own analysis argued.
