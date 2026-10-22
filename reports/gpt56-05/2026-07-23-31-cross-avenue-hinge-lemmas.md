# Agent report — cross-avenue hinge lemmas

Agent ID: `gpt56-05`  
Issue: #31  
Branch: `agent/gpt56-05/31-cross-avenue-hinge-lemmas`  
Session date: 2026-07-23  
Classification: proposed mathematical lemmas; no counterexample candidate

## Startup and repository state read

I read the repository protocol, the bootstrap state on draft PR #4, all open
issues, and the active draft PR summaries and claim file lists. I then inspected
the exact definitions or proof kernels needed from the following branches:

- cutoff-free finite Weil normalization and project state (PR #4);
- Robin witness and canonical branch-and-bound kernels (PRs #19 and #24);
- literature/equivalence and contour kernels (PR #21);
- Li coefficient formulas and scale barrier (PR #22);
- prime-power edge search (PR #23);
- carrier-shifted Weil formulas and negative tail findings (PR #27).

At session start, no counterexample had been found or certified. The active
project had seven draft PRs and open routes through cutoff-free Weil matrices,
carrier-shifted Weil matrices, Robin, Li coefficients, Nicolas primorials,
Deléglise--Nicolas bounded prime products, direct zeta rectangles, Speiser
zeta-prime rectangles, and positive-time de Bruijn--Newman rectangles.

The dominant cross-route pattern was that exploratory discovery had advanced
faster than proof-producing candidate promotion. I therefore chose the role of
**cross-avenue hinge-lemma producer**: small quantitative results that convert
screens into safe bounds, prune exact search spaces, or provide compact
certificates.

## Contributions

### L-3101 — quantitative dyadic negative witness

For a Hermitian matrix with `||A||<=B`, a negative margin `mu`, and a rounding
error `delta`, the rounded vector remains negative whenever

`B(2||x|| delta + delta^2) < mu`.

Nearest `k`-bit dyadic rounding gives an explicit `delta`, so discovery agents
can compute a sufficient denominator before invoking an exact checker. A matrix
uncertainty corollary absorbs `||A-A_tilde||<=epsilon`.

Immediate use: Issues #1 and #26, and any future finite matrix criterion.

### L-3102 — complete carrier prime-tail envelope

For the exact carrier convolution matrix,

`|v^T C(xi) v| <= v^T G v`

by translation invariance and Cauchy--Schwarz. Therefore any omitted prime-power
set `E` satisfies

`-W_E G <= P_E <= W_E G`,

where `W_E=(1/pi) sum_{q in E} Lambda(q)/sqrt(q)`.

This gives a deterministic, phase-independent bound for partial prime sums and
a generalized-eigenvalue movement bound of at most `W_E`.

Immediate use: Issue #29. This directly addresses the false-negative failure
mode documented in PR #27.

### L-3103 — finite-exponent Robin ceiling

In the canonical nonincreasing exponent tree, every suffix exponent is bounded
above by the last chosen prefix exponent `a_j`. Replacing each L-2004 infinite
factor `p/(p-1)` by the exact finite factor `sigma(p^{a_j})/p^{a_j}` gives a
strictly sharper rational subtree ceiling. The exact improvement factor is

`prod_{i>j}(1-p_i^{-(a_j+1)})`.

Immediate use: Issue #25.

### L-3104 — second-derivative contour tube

A twice differentiable complex curve differs from its endpoint chord by at most

`M (b-a)^2 / 8`,

where `M` bounds the second derivative. Along a straight complex domain segment,
this becomes `|z_1-z_0|^2 sup|f''|/8`. Endpoint ball radii add directly.

Immediate use: one shared compact polygon certificate for Issues #7, #17, and
#18, combined with L-0304.

### L-3105 — Li quartet negative window

For a left-of-line zero with transformed value `z=r exp(i theta)`, the complete
four-zero symmetry orbit contributes

`Q_n = 4 - 2(r^n+r^{-n}) cos(n theta)`.

With `N_0=floor(log 4/log r)+1`, a six-bin pigeonhole argument proves that some
`n` in `{N_0,2N_0,...,6N_0}` has `Q_n<0`.

Immediate use: target selection for Issue #14 after any future off-line zero
enclosure. It is not a sign claim for the complete Li coefficient.

### L-3106 — exact Pareto frontier

A bounded-prime-product state `(s_1,P_1)` safely dominates `(s_2,P_2)` when
`s_1<=s_2` and `P_1>=P_2`. Every future completion feasible from the second is
feasible and no better than the corresponding completion from the first.

Immediate use: sparse exact scaling of Issue #16 with auditable deletion
witnesses.

### L-3107 — additive Nicolas margin

The transformed margin

`M_k = log A_k - gamma - log(log Theta_k)`

has an exact additive one-prime recurrence. Directed increment intervals give
prefix-safe block exclusion or a certified violation, while ambiguous blocks
remain explicitly unresolved.

Immediate use: restartable, hash-chained Issue #15 searches.

## Verification performed

No external numerical RH claim was produced. I performed local algebraic and
finite checks of the new kernels:

- random Hermitian tests of the L-3101 perturbation inequality;
- numerical quadrature checks of `|v^T C(xi)v|<=v^TGv` for several carrier
  frequencies and shifts;
- exhaustive small canonical exponent completions for the L-3103 ceiling;
- the sharp quadratic example `g(t)=t^2` for L-3104;
- 10,000 random `(r,theta)` tests of the factor-six L-3105 window;
- exhaustive comparison of the L-3106 sparse frontier with brute-force prime
  subsets for budgets below 50;
- high-precision recurrence checks of L-3107 at the first several primes;
- structural checks that all claim files contain the required audit sections.

These computations are tests of elementary formulas, not evidence about RH.

## Important limitations and negative findings

1. No `Z-####` candidate was created.
2. L-3102 is safe but can be loose; it removes false promotion, not necessarily
   expensive complete reevaluation for near-zero cases.
3. L-3105 guarantees a negative contribution from one off-line quartet but does
   not control the rest of the Li sum.
4. L-3103 improves fixed-support pruning but does not bound the global support
   size.
5. L-3104 requires a rigorous supremum for the correct second derivative; point
   samples are not enough.
6. L-3107 can accumulate interval width and therefore needs precision escalation
   or shorter checkpoints near zero.

## Suggested immediate handoffs

1. **Highest priority:** Issue #29 should implement L-3102 blockwise and rerun
   the strongest carrier near misses with deterministic tail envelopes.
2. Issue #25 should benchmark L-3103 against the existing L-2004 ceiling before
   designing more elaborate Robin bounds.
3. Issues #7/#17/#18 should agree on one L-3104/L-0304 polygon certificate schema
   so three independent routes can share a verifier without sharing analytic
   evaluation code.
4. Issue #16 should implement L-3106 and validate every deletion against L-0370
   on overlapping small budgets.
5. Issues #1/#26 should expose the L-3101 bit-depth estimate in candidate export.

## Process proposal

Maintain a standing cross-avenue lemma queue. Every experimental PR should list
its three smallest missing one-way lemmas separately from its large search goal.
This creates useful work for agents who cannot immediately reproduce the full
numerical backend and reduces the chance that identical certification gaps are
solved repeatedly in incompatible forms.
