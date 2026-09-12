# Validation boundary

This packet contains proposed analytic proofs and bounded exact-algebra checks.
No native complex-zero or collision certificate is claimed.

## Accepting commands

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py --optimized
```

The final recorded commands pass in the authoring Linux environment. Their
stdout/stderr and return codes are retained in the separate delivery receipt.
The mathematical reconstruction has semantic SHA256
`0ac7a030a7b89fc34f93e2208e8b2f460b8893da02836385c4528726067e063e`.

The exact core includes 266 raw-versus-normalized moment comparisons, 133 direct
orthogonal-coordinate comparisons, 91 beta-diagonal panels, 121 orthogonality
panels, 121 finite Mellin panels and 160 tail-ratio panels. These are finite
algebra instances, not counts of independent infinite theorems. Additional
normalization/constant checks include the exact signed forcing and pole
coefficient. The maximum native moment order is 18 at seven rational theta
values. The code does not verify the source law from finite moments alone.

All four test methods pass in ordinary and optimized Python. EACH mode runs
one pristine CLI acceptance and ten actual altered-receipt CLI refusals. These
include false RH/collision/zero flags, numeric aliases, altered native b3,
altered pole/forcing coefficients, an omitted tail coverage and duplicate JSON.
The comparator authenticates the complete packet and reconstructs its exact
finite result; it does not merely accept a matching stored checksum. No asserts
implement mathematical acceptance.

The two representations of finite source moments have the SAME AUTHOR and
share Fraction primitives. Normal and optimized runs are not independent
mathematical review or independently implemented special functions. The
analytic norm, completeness, tail, continuation and Rouché statements require
review of PROOF.md.

## Explicitly unperformed

- No parameter-derivative tail estimate was proved or numerically certified.
- No new actual Xi zero, H_theta zero, collision or full defect was certified.
- No supplied parent checker, original theta quadrature, full repository
  validator, Lean/axiom build, Windows execution or remote CI was rerun here.
- No comprehensive review of the latest repo or external novelty was performed.
- The symbolic coefficients are not evidence of all-order Fourier positivity.

## Scouting and interrupted work

SCOUTING.md and scout_comparison.json retain the nondirected discrepancy that
prevented promoting the numerical response sign. Orders 1000 and 1500 completed;
an order-2500 job timed out and supplies no result. A failed interactive request
also supplies no result. An earlier ordinary-moment wrapper timed out during
an endpoint special-function comparison; only separately retained completed
outputs are described. Optional scout.py uses mpmath, including a numerical
zeta/zero routine, and is not imported by check.py or test_check.py.

A source-proof self-check caught an insufficient intermediate trigonometric
lower estimate before publication: pi>25/8 alone does not prove sin3>1/8.
The proof uses pi>157/50 there; the exact guard at 7/50 is independently
reconstructed. No final statement relies on the discarded estimate.

## Delivery and threat boundary

The external receipt records clean-ZIP extraction and an add-only minimal-Git
application followed by both mathematical modes. Those fixtures are not full
Riemann checkouts. The source parent is frozen by SHA/path/blob and was not
rewritten. No published claim ID or canonical status is changed.

SHA256SUMS binds every packet file other than itself. A separately retained
archive/patch receipt binds the package. The checker cannot detect a malicious
replacement of its entire executable and manifest together; no such stronger
security claim is made. Development --no-auth is explicitly NOT authenticated
acceptance. All reported accepting commands omit that option.

The authoring session has no repository write action, and its direct Git remote
probe failed DNS. This packet is locally prepared, NOT pushed. A later uploader
must report its actual head and own platform results separately, without
rewriting these historical execution boundaries.
