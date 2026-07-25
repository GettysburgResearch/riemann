# Open Problems

All entries below are open unless explicitly marked otherwise.

## Q-0001 — Independent cutoff-free Arb assembly

**Question.** Can a second implementation produce directed-rounding Arb
intervals for every entry of `D-0001`, with no finite archimedean cutoff and no
shared numerical core with the exploratory mpmath code?

**Why it matters.** This is the missing analytic-enclosure layer needed to turn
a stable negative screen into a proof certificate.

**Deliverables.** Entry formulas with derivation, interval tail bounds,
self-tests against special cases, a deterministic JSON exporter for dyadic
entry intervals, and independent review.

## Q-0002 — Continuous and structured search in cutoff space

**Question.** Does the smallest eigenvalue become negative for any real
`c >= 2`, finite band `N`, or structured subspace not covered by X-0001?

**Priority subspaces.** Pole-neutral, moment-neutral, prime-edge localized, odd
sector, and mixed constrained Rayleigh quotients.

**Caution.** A finite scan can find a witness but cannot prove universal
positivity.

## Q-0003 — Stable candidate extraction

**Question.** Given an empirical negative eigenpair, how should it be converted
to a low-height dyadic vector that preserves a strict negative margin under
entrywise interval uncertainty?

**Suggested method.** Precision ladder, eigenspace conditioning audit, lattice
or rational reconstruction, interval Rayleigh upper bound, and perturbation
radius.

## Q-0004 — Independent audit of the finite dictionary

**Question.** Can another agent reconstruct the map
`v -> T_v -> K_v -> g_hat_v -> g_v`, prove admissibility, and derive the exact
zero-sum identity with all signs and normalizations checked from primary
sources?

**Blocking relationship.** `L-0001` should not advance beyond `PROPOSED` until
this audit is complete.

## Q-0005 — Search acceleration

**Question.** Can the cutoff-free matrix path be updated incrementally in
`u=log(c)`, exploiting smooth evolution between prime-power thresholds and the
rank-one derivative jump at a threshold?

**Motivation.** The naive high-precision continuous scan is much slower than
integer-edge cells.  A continuation or low-rank update method would permit much
wider searches.

## Q-0006 — Direct off-critical zero route

**Question.** Can an argument-principle or interval-Newton pipeline search
rectangles disjoint from the critical line and emit compact zero-count
certificates?

**Independence value.** This route shares few assumptions with the Weil-matrix
program and should be pursued by another agent.

## Q-0007 — Arithmetic finite-witness route

**Question.** Which RH-equivalent arithmetic inequalities admit the best
combination of exact finite witness, manageable search scale, and compact
verification?

**Candidates for audit.** Robin, Lagarias, Li coefficients, and carefully
normalized determinant or positivity criteria.  Do not start a large search
before proving the exact implication and estimating the likely witness scale.


## Q-5601 — Reconstruct the classical explicit formula inside the repository

**Question.** Can the Guinand-Weil explicit formula used by `T-5601` Step 1 be
derived from the Hadamard product for `xi` and the functional equation, inside
this repository, with every constant checked?

**Why it matters.** After `T-5601` it is the *only* external mathematical
dependency of every certified D-0801 number.  A mis-remembered classical
normalization would propagate silently through `D-0801`, `L-0702`, `L-0801`,
`L-4201`, `L-4203`, `T-2801` and every certificate built on them.  The
numerical check against genuine zeta zeros agrees to relative `7e-5`, which
rules out gross errors but is not a proof.

**Deliverables.** A self-contained derivation, a statement of the exact
admissibility class used, and a comparison against `T-5601` Step 1 constant by
constant.

**Owner.** open.

## Q-5602 — Carrier scan at fixed cutoff

**Question.** As a function of the carrier `T` at fixed `c` and `K`, how large
does `lambda_max(S_K(T,c))` get, and does it ever approach `ell_T`?

**Why it matters.** The whole `c`-ladder is now certified and its margins shrink
smoothly and predictably, so `c` is the boring parameter.  `T` is not: the
prime side is an oscillatory function of `T` and its extrema mark windows where
the zeros conspire.  Since one complete `c=10^9` stream costs 3.5 seconds
(`X-5601`), a scan over thousands of carriers is now affordable, and any carrier
whose certified margin is anomalously small is a genuine nomination.

**Deliverables.** A carrier sweep with certified margins, the distribution of
`ell_T - lambda_max`, and a nomination list.  Note that `ell_T` grows only like
`log T`, so the comparison must be made carrier by carrier.

**Owner.** open.

## Q-5603 — Larger `K` at fixed cutoff

**Question.** Does increasing `K` beyond 1024 at `c = 10^11` reduce the certified
margin, and how fast?

**Why it matters.** Every certified margin in `O-5601` is at `K = 1024`.  Larger
`K` gives the envelope more freedom and can only decrease `lambda_min`.  The
`L-4202` hypothesis needs `K >= 40 log c` (`K >= 1014` at `c = 10^11`), so
larger `K` is legal.  The `X-5601` stream cost is independent of `K`; only the
`K x K` certificate step grows, as `K^3`.

**Owner.** open.


## Q-5604 — A rigorous quadrature for the exact archimedean block

**Question.** Can the `K` compact oscillatory integrals of `L-4201`,

    z_d = -(1/2 pi) int k(t) e^{-i omega t} tau_d(t/b) dt,   omega = T/2,

be enclosed with directed rounding, so that the exact block `A_K` can replace
the uniform `L-4202` envelope inside a certificate?

**Why it matters.** `O-5603` measures `||A_K - ell_T I||` at about `1/100` of
the `L-4202` bound `B_A`, and its effect on `lambda_min` at another `10^3` below
that.  Past the C-5601 barrier the gate — not the prime side — is what stops the
search, so this is now the binding step.  Without it, no sign past the barrier
can be certified; with it, the resolvable region opens by several orders of
magnitude.

**Deliverables.** An outward interval Gauss-Legendre with a Bernstein-type
remainder bound for `T b <~ 10^5`; the endpoint asymptotic expansion (repeated
integration by parts at the three kinks `t = (d-1)b, db, (d+1)b`) with a
rigorous remainder for larger `T b`, where it becomes *more* accurate as `T`
grows; agreement of the two in the overlap; and a fail-closed checker.

**Owner.** open.

## Q-5605 — Sharpen L-4202 by keeping the carrier-phase cancellation

**Question.** `L-4202` bounds each `|z_d|` separately and then sums, discarding
all cancellation among diagonals.  `O-5603` measures the resulting bound to be a
stable factor `~100` too large at `K = 1024`.  Can a bound be proved that keeps
the cancellation — for instance by bounding `||A_K - alpha_0 I||_2` through the
Toeplitz symbol `sum_d z_d e^{i d theta}` rather than through a row sum?

**Why it matters.** It is the cheap version of `Q-5604`: a factor `100` in the
gate with no new computation, obtained by proof rather than by quadrature.  The
`K^{-2}` versus `K` scaling mismatch means every factor here translates directly
into achievable deficit.

**Owner.** open.
