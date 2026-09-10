# EPD26: endpoint source control and prime-discrepancy energy

**Status:** complete proposed component proofs; independent review pending.
**RH and the source-specific subpower upper bound remain unproved.**

This is an add-only research continuation of PR #811 at
`9e05a2b345369cd16c0973c531650eb37727445e`. It does not alter predecessor
mathematics, reviewer records, main, or canonical/formal sources.

Read [PROOF.md](PROOF.md) in order, then [ATTEMPT.md](ATTEMPT.md).

## Results, with their scope

The same ordinary-prime completion A_X and positive logarithmic cost E(X)
are retained. At the EXACT critical line, its smoothed logarithmic derivative
has a causal L2 norm bounded by

    24 max(1,log X)^(3/2) [2E(X)+10+2log(1+log X)]
                          +max(1,log X)^2+13.

This removes the inward shift from the predecessor's transfer. The proof
uses an explicit one-sided Fourier multiplier for the first-prime band and
pays every higher prime power separately. An off-line zero of depth delta
then forces E(X)>=c X^delta/max(1,log X)^(3/2)-8sqrt(max(1,log X)), with
all multiplicities and every cutoff retained.

The actual Cauchy phase correlations have an exact factorization:

    ||Re S_X||_(L2(Cauchy))^2
      =R_X(1)^2+integral_1^X x R_X(x)^2dx,

where R_X is the complete weighted tail of d(pi-li_2), not its absolute value.
Under RH ONLY this gives Q(X)<<log^3 X and E(X)<<log^(3/2) X. Unconditionally
the PNT comparison still gives a positive power of X. The unproved last
estimate is not labeled a theorem, and finite checks do not fill it.

## Replay and review

From this directory run:

    python validate.py
    python checks.py --expect checks.normal.json
    python -O checks.py --expect checks.optimized.json
    python rejections.py

The checker uses exact standard-library rational arithmetic. It checks
finite polynomial integrations, kernel factorizations and multiplicity
normalizations. It does not evaluate an actual entropy integral, all-cutoff
prime-discrepancy energy, zeta zero, or infinite analytic proof.

Sources, claim scopes, dependency edges and executed results are in
SOURCES.json, CLAIMS.tsv, EDGES.tsv and VALIDATION.md. The positive-measure
control in ATTEMPT.md is continuous and synthetic, not the ordinary primes.
No external novelty or priority claim is made for Fourier multiplier,
Cauchy-kernel, Hardy, or mean-square-prime-error mechanisms.
