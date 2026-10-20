# Replay and review scope

The exact checks use Python's standard library only. From this directory:

```sh
python -I -S -B replay.py
```

The replay first checks the frozen byte hashes in MANIFEST.json, then
runs each of nine finite checkers in ordinary and optimized mode.
It rejects acceptance assertions that Python would remove under `-O`,
requires every receipt to pass, and compares the two receipts after
canonical JSON serialization. The aggregate result is
REPLAY_RESULTS.json. The packet's `.gitattributes` preserves the
reviewed source bytes across checkouts.

| Checker | What it authenticates |
|---|---|
| type_i/verify_type_i.py | Exact Eisenstein arithmetic, multiplicative ramified profiles, two-prime formal dual series, and rational exponents |
| type_i/verify_profile_closure.py | The actual cusp minor and its inverse in a cyclotomic ring, plus all 27 finite coefficient profiles in the stated coverage |
| type_i/verify_numerator_barriers.py | Exact identities for the supplied numerator estimates and their endpoint interpolation |
| type_i/verify_positive_cubic.py | Exact primitive cubic Fourier transform, inverse-variable substitution and positive cubic self-reflection over residue fields of sizes 7, 13 and 19; rejection of the wrong output orientation |
| mixed/audit_cusp_minor.py | An independently written cusp-minor calculation, including rejection of the withdrawn incorrect minor |
| mixed/check_marked_exponents.py | Complete Euler/mask identities, counterexamples to first-power truncation, and exact marked exponent bookkeeping |
| mixed/check_quadratic_pair.py | Exact finite Fourier orientation, conductor and zero masks in a cyclotomic ring; wrong-variant negative controls; rational pair exponents |
| global/check_residue_algebra.py | Residue factors, shifted labels, selected-prime laws, guard phases/valuation support, exact tame Fourier sums, and canonical residue margins |
| scalar/verify_tangent.py | Primitive critical polynomials and resultant; 64 exact rational intervals covering the narrow tangent family; positivity over the continuous delta/x rectangle; side conditions and endpoint branch isolation |

These are finite algebra checks with explicitly stated coverage. Their
success does not prove theta continuation, Mellin contour shifts,
large-sieve theorems, infinite canonical induction, uniform analytic
estimates, or a global zero-free statement. The scalar checker now
independently replays the closing tangent certificate, but not the
initial analytic improvement to seven-eighths. Source hashes pin the inputs;
they do not certify those inputs.

The centered canonical numerical probe, when present in `mixed/`, is an
exploration using ordinary floating arithmetic. It is excluded from this
acceptance replay and does not establish an asymptotic theorem.

Component analytic reviews are separate from the computation. Their
file hashes and authorship boundaries are recorded in
GLOBAL_ASSEMBLY_REVIEW.md, type_i/REVIEW_ANGULAR_MEAN.md,
type_i/REVIEW_QUADRATIC_PAIR.md, type_i/REVIEW_UNIFORM.md,
and the two independently authored auxiliary-guard reviews.
A later source edit requires a new hash and review; old reviews are not
silently applied to changed arguments.

The initial exact-head reviews bind commit
`9bf9e21f95669abdcaa74e3b2ba54fb93e779503`, which had eight checkers.
EXACT_HEAD_REVIEW_FINAL.md and type_i/EXACT_HEAD_LATER_REVIEW.md bind
the later research commit `17d7b5b617027cffa4869b47eb898c14eb89e7b9`.
They do not silently extend to the subsequent hybrid angular additions.
Later analytic additions have separate current-hash component reviews
listed in [LATER_RESULTS.md](LATER_RESULTS.md). The ninth checker tests
the newly used positive cubic local self-reflection; it does not certify
the corresponding infinite joint mean.

The [final hybrid-head review](FINAL_HYBRID_HEAD_REVIEW.md) binds the
complete mathematical head `b05d0675e2824f7b83325f881c243df8e5b56487`.
It independently replays all nine checkers from an isolated archive,
checks 98 source hashes and 106 local links, and verifies preservation
of prior mathematical bytes and the new review bindings. The final
packaging commit adds that receipt and refreshes this index and the
manifest; it does not alter the reviewed mathematics. Agent reviews
are not human review, global analytic certification, or integration
approval.
