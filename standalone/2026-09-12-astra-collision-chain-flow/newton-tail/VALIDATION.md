# Validation boundary

The analytic arguments are proposed paper proofs, not proof-assistant output.
The checker has no native zeta evaluator, supplied zero coordinates, floating
quadrature, or implicit infinite-prefix oracle in its accepting path.

## Exact reconstructed scope

`check.py` reconstructs finite positive-factor polynomial controls by rational
multiplication, with a separate subset-enumeration comparison for smaller
products. It checks Newton, terminal-ratio and Maclaurin inequalities, complete
finite Taylor tails, exact complex-factor identities, and rational scalar
minimum-modulus controls. Its Gaussian tests are finite polynomial
approximations, not numerical verification of a limit theorem.

The arithmetic examples use actual Möbius values obtained by trial
factorization, and an independent divisor-fiber computation of the Newton
output. They retain the whole physical constant future, reciprocal energy,
complete quadratic annulus and oracle-completion cost. The oracle examples
intentionally use the Möbius prefix through B; they are sharpness controls,
not a short-prefix estimate for RH.

The checker also verifies a compact, fully specified Gaussian comparison
witness with n=2^100 repeated rational factors and17 coefficient coordinates.
It does not expand the entire polynomial or count this as a native fit.

The schedule tests check 39 displayed integer budgets j=2 through40. The
proof for every j is algebraic in PROOF.md, not an extrapolation from that
list. The F5 consequence tests only the new rational allowances and the
support-bound inequalities; the defining-integral zero certificate is an
explicit unreplayed import.

## Commands and receipt

The production command is separate from acceptance:

```text
python -I -S -B check.py --emit result.json
```

Final acceptance and tests are run in both modes:

```text
python -I -S -B check.py --check result.json
python -I -S -B -O check.py --check result.json
python -I -S -B test_checks.py
python -I -S -B -O test_checks.py
```

Execution results and final packaging replays are recorded in the accompanying
`evidence/` logs and delivery record. The final receipt's semantic SHA256 is

`f7baa9f246bec036451abd7a35795e2df81e13f3a140a3e58303de36551fe12a`.

Each completed five-method test suite includes a pristine accepting CLI run,
additional direct exact comparisons, and NINE actual CLI refusals. Seven
altered copies are resealed, so hash authentication is not their rejection
mechanism. In particular, altered full-energy and schedule formulas reach
mathematical reconstruction and are rejected there. The other two refusals
are unexpected inventory and unresealed source drift. Duplicate-key and
Boolean/integer type aliases have their own acceptance checks.

Normal and optimized execution use the SAME integer/Fraction backend and
same author. They are not independent mathematical review. The extra subset
and divisor calculations are implementation cross-checks of bounded identities,
not independent authors or machine proofs of the imported theorems.

## Publication and checkout scope

The prior six-moment packet and CJB26 are already on PR875. This NJT26
continuation was authored locally. The connector offered no push action;
the installed GitHub plugin was rediscovered, but no separate write-capable
action was available. The direct Git remote read failed with DNS resolution
exit128. No remote NJT26 commit, PR update, CI success, or remote validation
is claimed by this record.

An add-only patch and same-PR publisher are supplied outside the research
folder. A local minimal-Git application can verify patch integrity and
preservation of unrelated files; it is not a full pinned Riemann checkout.
No full repository validator, predecessor quadrature campaign, native
high-order fit, new root computation, formal build, or independent referee
acceptance is claimed.
