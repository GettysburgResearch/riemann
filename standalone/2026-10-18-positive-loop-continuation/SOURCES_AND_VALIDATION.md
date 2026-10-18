# Sources, validation and honest research scope

## Exact inputs

- GettysburgResearch/riemann #981, commit
  cf41f3f94a0f1df2bb503d22ab384bfc69288f33, directory
  standalone/2026-10-18-theta-degree-eighteen/. The complete proof and compactness
  consumer were read. The user-delivered packet supplies the same primitive
  source and rational parameter file. The new checker authenticates them before
  importing. interval_source.py: blob 769e811651ad9e013377a2159e172ff35ec1f6d7,
  SHA256 aaa8d85c17bee2cbe7fb9bceefbd63f58cd2258fd47c2b989951d97cd8b501ff;
  parameters.json: blob d232b1482e33ae36189c1f3ea144c97344abb846,
  SHA256 c8810df849f30d71aeef2e5b59ffc3b6434df2d5fab4434306de806143777460.
  The current #981 publication/contents endpoints were reread. No historical
  independent review or full prior mutation suite is claimed newly replayed.
- Newman--Wu, Lee--Yang Property and Gaussian Multiplicative Chaos, CMP 369
  (2019), 153--170, DOI 10.1007/s00220-019-03453-0. The published primary HTML
  was read, especially Section 1's nonnegative weighted finite Ising statement,
  Theorem 7's weak closure and Proposition 13's product/variance formula.
  https://link.springer.com/article/10.1007/s00220-019-03453-0
  These classical results are imported, not independently reproved.
- #988, head 86c156baa3f10296a26e066f5f4d276776b79c27, was checked at detailed
  PR-description scope. It also matches degree 18 and has a smaller twentieth-
  moment discrepancy. It is not an input and its checker was not replayed.
- #987 and the current #986/#984 descriptions were checked to identify the
  unresolved fixed-member problem. No sieve, family moment, CT/DF theorem,
  quasi-RH conclusion, or analytic estimate from those packets is used here.

Gibbs edge differentiation, the implicit-function theorem, conditional Ising
factorization, automatic differentiation, interval Newton/Banach certification
and Lee--Yang are classical methods. No global literature-priority claim is
made for them or this local continuation formulation.

## Executed acceptance

`python replay.py` checks the byte manifest, runs verify.py and controls.py in
ordinary and optimized Python, compares their complete outputs, and runs five
separate corrupted controls. All default verify.py runs reconstruct the ORIGINAL
infinite theta source through degree 20 and include all time/index tails.
The accepted old source/root box has radius 10^-36; the new q=1/10000 root box
has radius 10^-34. Neumann-series enclosures are used for the exact compensated
tangent, not an assumed inverse Jacobian. CHECKS.json records rational bounds.

The independent finite assembly enumerates all 128 states of a seven-spin
restriction with two single components and two dimers, for two possible added
edges and three biases 0,1/11,1/3. It checks 126 raw moment identities (orders
0 through 20 in all six cases) plus one elementary compensation identity.
These are NOT 126 independent analytic proofs, a zero census or a complete
2^282-state enumeration. The complete large graph is handled by the exact
conditional factorization proved in PROOF.md.

The five negative controls erase the loop normalizer, reverse its sign, erase
the edge, drop the twentieth moment, or omit lower-moment compensation. Each
actual optimized subprocess must fail at the corresponding named check.
The controls share rational arithmetic; the transcendental source backend is
inherited rather than independently developed. Proof and code have one author.
No separate agent/human referee, proof assistant, CI or repository-wide validator
is claimed. Directed checking establishes the specified finite/local existence
claims subject to the written proofs and inherited implementation, not RH.

## Exploration that did NOT finish

A high-precision exploratory source was computed through degree 24. Direct
least-norm Newton attempts to match degree 20 did not yield an admissible exact
root. Retraction onto the degree-18 manifold reduced the discrepancy slowly.
Two longer exploratory commands hit their 45-second execution limit; neither
is counted as a completed test. Only saved successful outputs informed further
search. Some fixed-coordinate paths approached ill-conditioning; failed steps
are not a proof that no path or graph exists.

Six symmetric edge-subdivision responses were explored. In that particular
chart they moved the next moment away from the target. The exact subdivision
identity is proved, but those exploratory numerical signs are not promoted to
an exhaustive certified obstruction. The positive loop yielded a useful signed
response. A small positive endpoint was then solved at high precision and
CERTIFIED independently of the solver by the default outward check. This endpoint
still has a substantial nonzero degree-20 discrepancy; it is not an all-order
extension, a best residual across architectures, or a large advance toward RH.

## Remaining gap

Opposite local response signs do not prove that the next theta moment lies in
the locally attainable interval, or that the construction can be iterated at
unbounded orders. The required global feasibility statement remains OPEN. No
finite theorem or failed numerical search is substituted for that premise.
