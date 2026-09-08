# FC26 validation

Status: author checks of a proposed mathematical continuation. These are not
independent referee acceptance, an RH certificate, or a formal Lean verification.

## Executed scope

The new checker uses integers and fractions only. It authenticates the exact
parent proof and verification JSON by length, SHA-256 and Git blob before reading
the rational trial coefficients. It executes no parent code. The parent proof
and JSON were freshly read through GitHub at the pinned commit; archive copies
have the identical content identities.

The fixed scope is: 16 rational polynomial-evaluation points; four synthetic
finite jump-ratio lists tested against all primes through 257; 128 coefficients
of the actual two-term inverse seed; explicit disk, Harnack and exceptional-set
constants; 90 rank dimensions (1 through 64 and powers 2^7 through 2^32); and
eight synthetic nonouter Gram matrices. Large rank values test only INTEGER
BUDGET FORMULAS. No actual high-rank source or Gram matrix is built at those ranks.

The verification record contains 1,008 bounded controls. These are mostly
arithmetic identities and inequality instances, not 1,008 separate theorem proofs.
The rank-independent analytic arguments are in PROOF.md and need review.

## Commands

From standalone/2026-09-07-astra-feedback-and-conditioning/:

```sh
python -B check.py
python -B -O check.py
python -B check.py --rejections
python -B -O check.py --rejections
```

Both reconstruction modes completed successfully, with identical output.
Both complete rejection runs completed: one pristine control and twelve refusals
in each mode. An initial combined 30-second invocation completed the normal run
but timed out during the optimized run. That incomplete optimized invocation is
not counted as a PASS; a subsequent standalone optimized run completed.
The final sealed executions are recorded in the delivery execution receipt.
The two reconstruction modes must produce identical bytes. Each rejection run
first accepts a pristine copied packet, then invokes the real CLI on twelve
mutations: false RH status, boolean alias, wrong atomic sign, narrowed source
scope, wrong floor exponent, false multiplier status, float alias, duplicate
JSON key, extra file, empty manifest, modified parent, and a symlink payload.
The semantic JSON mutations are rehashed so they must fail primitive replay,
not merely the manifest. Acceptance does not use Python assert statements.

The exact flat inventory has nine files and eight checksum entries. The code
rejects missing, extra and symlink payload files. It binds only its explicitly
listed parent paths; it does not claim repository-wide source coverage.

## Arithmetic and analytic boundaries

No zeta or gamma function is numerically evaluated. No real frequency integral,
prime asymptotic, unknown zero, high-rank actual Gram, or new full output-error
certificate is computed. In particular the 300-fold predecessor result is NOT
counted as newly reproduced. The new Dirac mass uses the authenticated rational
polynomial; its distributional interpretation is a paper proof.

The minimum-modulus argument is analytic: local zero disks describe a proved
exceptional-set bound, not a numerical zero census. Its rational constants are
conservative. No claim of practically useful small-rank improvement is made.

The fixed-controller theorem has its stated compact piecewise-AC finite-jump
scope. It does not cover arbitrarily rough L2 inputs, infinitely many accumulating
jump times, or a different input chosen at every horizon. No synthetic control
is substituted for the literal zeta source in that theorem.

## Unperformed checks

No predecessor numerical suite, full repository checkout/build, Lean/Comparator,
Windows execution, remote CI, independent mathematical review, or broad research
campaign was run. Publication and clean-bundle/patch validation are recorded
separately in the final receipt, not assumed from these instructions.

## Scientific verdict

The manuscript supplies proposed proofs of the feedback obstruction and the
source-specific all-rank conditioning bound. It supplies a complete conditional
chain from FC26.OPEN to RH. It does NOT supply a proof of FC26.OPEN, of RH, or of
the earlier uniform Mobius/block-gain estimates. Those omissions are not
matters for a checker or referee to fill by implication.
