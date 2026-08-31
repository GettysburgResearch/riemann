# Independent review of the single-witness contract59618937

Reviewed freeze:596189377cb5d167c95334bfc5ddb74af2d1cc5f.

| Frozen file | Git blob |
| --- | --- |
| single_top_witness.py | 148a8d9523b30a71b5b49ba92bf957e64a25dbe4 |
| SINGLE_TOP_WITNESS_PREREGISTRATION.md | 2ad3d6dc7140f185d9c1eb0ee0b0f4ecbc2d63ad |
| SINGLE_TOP_WITNESS_REPLAY.md | 7e3dc118419af96630b57d5177828ff551c691e1 |
| tests/test_segre_hadamard_single_top_witness.py | 92f6434a53b55dd6b7189d95141f1a29b6f12194 |

I independently read the complete producer, both contract notes and
all26 tests, then inspected the final binding and cleanup changes.
All four working files have no diff from this freeze. I ran no
scientific job. The coordinator reported format/lint success and
18 ordinary precheck passes; the optimized prechecks, actual witness
acquisition and fixture-dependent checks were pending at review time.
This report does not claim that a top witness has been acquired.

The frozen547d91b6 code is used only for authenticated source loading,
the complete original central matrix and the complete old-column list.
Its unexecuted full-kernel/build entrypoints are not called. The exact
promotion proof and all transitive accepted-prefix/Tor inputs remain
authenticated. I authored that promotion proof, so this is an independent
implementation and contract review, not a self-review of the theorem.

The new nonmembership certificate is sufficient: an actual49-by49
old-coordinate minor with nonzero determinant modulo a fixed prime
is invertible over the rationals. Hence a nonzero relation vanishing
on all49 chosen coordinates cannot lie in the complete old span.
All49 old columns are retained and checked in every original row.
The final candidate is a nonzero primitive integer vector with exact
zero gauge coordinates and zero residual in every original D2 row.
No complete50-vector kernel or unmeasured rational nullity is required
or inferred from the modular search.

I checked the incremental modular row selection, packed row-pivoted
LU and its permutation solve, exact Dixon divisibility, the bounded
rational reconstruction, and the final full-row acceptance. The search
may stop after542 independent rows, but unselected original rows are
still tested on every proposed witness. A reconstruction is merely a
candidate until that exact test passes. Fixed-prime rank drops, failed
reconstructions, nonzero residuals and lift exhaustion remain explicit
failures or UNKNOWN outcomes, with unchanged caps.

The tests include a signed multi-lift reconstruction, a candidate that
solves every selected row but fails an unselected original row, modular
old-rank-drop and fixed-prime fallback controls, gauge/nonprimitive/type
refusals, independent old-minor rank checking and final original-coordinate
acceptance. The final hardening validates distinct candidate coordinates.
Both source and final-fixture test classes release their retained large
objects; this resolves the review observation that default unittest
class order need not put the source class before the fixture class.

After an accepted witness, the actual top polynomial map and complete
polynomial compositions are checked afresh, while every lower map is
preserved. The global775/776 dimensions remain theorem deductions,
not measured matrices. The older20/52/42/26 and full-composed contracts
remain explicitly uncompleted. No blocker was found in this contract.
