# Validation and review boundaries — BSR26

This is a local proposed research delivery, not independent acceptance or an
RH proof. Exact source versions and reading depths are in SOURCES.json. The
full analytic proof is PROPOSAL.md; the bounded checker does not machine-prove it.

## Accepting interface

From this packet directory:

```
python -I -S -B check.py --check verification.json
python -I -S -B -O check.py --check verification.json
python -I -S -B test_check.py
python -I -S -B -O test_check.py
```

Acceptance authenticates the exact eight-file inventory and all seven hashes,
then reconstructs canonical mathematical output and compares it with strict
typed JSON. Duplicate keys, floats/nonfinite numbers, extra or missing files,
symlink inputs, changed source pins and incorrect reconstructed content reject.
`--emit` is producer-only and is not an acceptance command. Hashes identify
bytes; they are not proof of an analytic assertion.

## Bounded mathematical scope

- Thirteen fixed moments (orders 0 through 12) are compared by TWO algebraic
  derivations: the smoothing recurrence and the reciprocal sinh power series.
- Seventeen gamma-starting moment stages retain mean one and variance 2/5
  exactly; the third moment matches its closed formula. Moments through order
  twelve are propagated; the retained table prints only orders zero through six.
- Thirteen deterministic-leaf second moments and moment upper controls are
  reconstructed separately. These are not a proof of arbitrary-depth zero safety.
- All twenty Bernstein coefficients on all four closed quarter intervals are
  rebuilt, and the four polynomial identities are independently expanded.
  Together with positive coefficients this is the entire finite polynomial
  certificate consumed by the gamma strip proof, not a sampled sign scan.
- Three complete rational transitions (L=2,4,8) expand support 1 -> 2 -> 10 -> 350.
  Exact probabilities, means, bin conditional variances and monotone transport
  marginals are checked. Fourteen uniform bins are covered analytically, not by
  sample quadrature. The true continuous-map residual is bracketed by directed
  96-bit square roots with the complete bin coupling error paid.
- Unit tests additionally compare twenty-one fixed moments, twelve alternative
  law/bin panels and sixty-five square-root brackets.

The result intentionally records `rh_proved=false` and
`orbit_strip_preservation_proved=false`. No actual zeta/gamma value or zero
location is evaluated by the accepting code. The Gamma zero theorem is an
analytic paper argument using a rational polynomial bound, not a finite root
search promoted to all heights.

## Actual adversarial interface tests

One pristine copied-package acceptance and fifteen different actual CLI refusals
are exercised in EACH interpreter mode: false RH and strip-preservation flags,
Boolean and floating aliases, duplicate/empty JSON, resealed wrong moments and
costs, resealed code changes to the gamma polynomial and bin map, resealed
source drift, changed proof bytes, missing/extra members, and a symlink receipt.
The resealed code mutations must fail mathematical reconstruction, not just a
hash comparison. No `assert` is used for acceptance; unittest assertions are
explicit method calls unaffected by Python optimization.

## Exploratory calculations not included in accepting evidence

The branch idea was developed with short ordinary Python/Fraction, SymPy,
NumPy/SciPy and mpmath scouts. In particular:

1. A preliminary special-case square-root defect routine rejected a nonsquare
   radicand. It was superseded by the general rational quantization/transport
   method, not counted as a certificate.
2. A deterministic-leaf first-generation fourth Hankel scout used nondirected
   quadrature and produced a negative sampled eigenvalue. It does not locate a
   critical-strip zero, is not independently certified, and is not a theorem.
3. The gamma-first-step formula (18) was evaluated by tensor Gauss quadrature
   at orders 20 and 32. Sampled log-modulus-ratio derivatives were negative near
   heights 13.5 and 23.5, warning against a naive induction of the stronger
   starting-law monotonicity. This is NOT an interval sign proof.
4. A double-precision root scout for that first iterate (quadrature orders 20
   and 40) returned off-central candidates OUTSIDE 0<Re s<1. It was neither an
   exhaustive search nor a zero-free-strip certificate. The candidate locations
   are not used by any proof or accepting calculation.

No statement of later-stage zero safety or unsafety is based on these scouts.
The local source, residual and initial gamma proofs do not import them.

## External mathematical boundaries

The Brownian distributional equation and entire Mellin identity are credited to
Biane--Pitman--Yor, equation (45) and Proposition 1. Those exact normalization
statements were inspected in page images as well as parsed text. The contraction,
residual estimates, gamma seed sign calculation and quantization proofs are
written here. General Laplace uniqueness, Hardy/Mellin holomorphy, Hurwitz,
and the zeta zero-strip facts are classical. No numerical zero census is imported.

#296 was read at metadata level for prior-art/context, not re-reviewed. #842's
principal construction was read for the Lee--Yang interface, but its numerical
six-moment campaign is not replayed or used as a premise. This is not a new
whole-repository review or a change to any canonical scientific status.

## Delivery scope

The bundle and add-only patch are prepared for a new branch based on the frozen
main commit in SOURCES.json. A complete repository checkout was not obtained;
GitHub reads work but the exposed actions provide no writes, and direct Git
access failed DNS resolution. No repository write, permission, settings, main,
source-branch, formal-library or workflow modification was performed.

The outside execution receipt records completed commands, return codes and
result hashes, together with the packet Git tree and byte inventory. A clean
archive extraction and temporary-Git add-only application are separate packet
checks, not a complete repository build or CI. No Lean proof, native Windows
run, independent referee acceptance, or all-depth feasibility campaign is claimed.
