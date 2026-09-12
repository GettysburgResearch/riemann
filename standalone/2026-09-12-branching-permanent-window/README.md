# BPW26 — one window certified for every later branching depth

**Proposed component proof plus directed finite source certificate. Independent
mathematical/code review is required. RH and cofinal expanding-window confinement
remain unproved.**

For the prescribed Gamma(5/2, rate 5/2), shared-uniform branching orbit, every
integer depth **n >= 32** has exactly three positive-height critical-strip zeros
below height **30**. They are simple and exactly central. There is exactly one
in each square centred at heights 14.134725, 21.022040, 25.010858 with half-width
1/100; the whole remaining rectangle contains none. The same calculation counts
the literal Xi zeros in that window. It is not a new zero or height record.

The change in strategy is to pay the entire future perturbation geometrically
ONCE, rather than prove that a generic one-step operation preserves zeros.
An explicit complete theta polynomial and zero-free contour enclosures protect
the outer count and every inner count simultaneously for Xi, every later
iterate, and their real convex interpolations. Actual derivative bounds give
geometric motion estimates for all three roots.

Read PROOF.md, then REVIEW.md and VALIDATION.md. SOURCES.json records the frozen
context and the classical inputs. No parent numerical program is imported.
The two historical BHH26 variants #859/#860 share a path but are distinct;
this unique new packet neither overwrites nor reconciles them.

## Replay

From this directory, using Python 3.10+ standard library:

```sh
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_check.py --part fast
python -I -S -B -O test_check.py --part fast --optimized
python -I -S -B test_check.py --part full
python -I -S -B -O test_check.py --part full --optimized
```

The accepting check authenticates eleven regular files and ten checksums,
then reconstructs the 57,347 term/node evaluations, complete analytic tails,
121 interval polynomial coefficients, all 3,220 contour segments, four exact
windings and three derivative intervals. It does not merely accept a retained
result's consistency or hash. The producer is `certificate.py --write PATH`;
production alone is not acceptance. Run it with `-B` to avoid cache files.

The `full` tests execute one pristine complete acceptance and one resealed
numerical corruption that is refused only after full reconstruction. The `fast`
tests exercise exact primitives and eleven other CLI refusals plus a symlink
refusal when permitted. An unsupported symlink test skips explicitly; report
that platform omission rather than counting it as executed.

## The open interval is still there

The predecessor controls heights ABOVE a depth-dependent T_n. This packet
controls heights BELOW 30 for all n>=32. Their union does not control the
intervening region. A new argument must produce protected windows with unbounded
height (allowing shrinking-width clusters instead of assuming simple zeros).
No such all-height theorem is claimed here, and no numerical pattern substitutes
for it. Review concerns these components, not an RH proof with a missing lemma.
