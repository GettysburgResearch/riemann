# Independent review of unitary boundary recovery and nonscalar radius gain

Reviewed scientific commit: `6365e26a5a77d2944e720470fec0b28855777f1c`.
Review date: 2026-08-31. Reviewer: independent `recent_landscape` agent.

Result: no blocker found in the stated proof or bounded replay. I read the
theorem, producer, tests, replay contract and frozen identities independently.
I did not execute test or computation jobs; those remained serialized by
the root agent on the shared machine.

## Frozen scope

The five added files in the Koszul analytic-parent directory are
`NONSCALAR_GRADE_RADIUS.md`, `NONSCALAR_REPLAY.md`,
`nonscalar_replay.py`, `tests/test_nonscalar.py` and
`nonscalar.verification.json`. The bound proof's LF SHA-256 is
`3e5a340b3e7d30d354ad77f3151a5e049b98524dbc3323a5fddf569711fa2ca5`.
The precursor is the critical-boundary scientific checkpoint
`f8b385d69c8b5eea13ef7f474a23835bf0dbbd2f`, with the earlier source and
regularization chain unchanged. The source operator and finite grade
cutoff are fixed before zeros are located or factored.

## General unitary theorem

The sign and normalization in
`P_g=log F_g-log D_(2,g)` are correct. The exact finite identity separates
the degree-N Taylor polynomial of the source characters from the finite
second-regularized block logarithm. Its latter part converges absolutely
strictly inside the Schatten-two disk, using actual source dimensions.

Given a first-zero circle `rho<=s<sqrt(rho)`, isolated zeros allow a
slightly larger disk with no further zeros. Dividing by the finitely many
boundary factors gives a nonvanishing analytic remainder. This is a
legitimate proof device; it does not redefine the modules or operator
by fitting those zeros. Cauchy convergence of the remainder and Dirichlet
convergence of the explicit logarithmic factors prove the claimed open
disk and closed-arc convergence.

At a boundary zero tau of multiplicity m, the only divergent logarithmic
piece is `-m H_N`. The resulting exact rate is
`N^m D_(N,g)(tau) -> exp(-m gamma) (-tau)^m F_g^(m)(tau)/m!`.
The sign, power of tau and factorial are all necessary and correct.
Other zero factors contribute their nonzero boundary values. The statement
therefore applies to every unitary input on the original critical circle,
including an empty zero set, without asserting trace-class membership there.

## Native involution and its stronger disk

For `diag(1,-1)` on the two-dimensional factor and identity on dimension k,
the source symmetric-power characters give the even part
`F_g(t)=((1-t)^(-k)+(1+t)^(-k))/2` directly. The numerator has no
cancellation at `t=+1,-1`; its finite zeros are simple under the displayed
Möbius transformation. The nearest pair is
`+/- i tan(pi/(2k))`.

The elementary inequalities proving
`1/(k-1)<tan(pi/(2k))<1/sqrt(k-1)` hold for every k>=3. Inside that
larger zero-free disk, analyticity of the first-order character series
plus absolute convergence of the remaining block-log terms gives
absolute, locally uniform whole-grade logarithmic convergence. A larger
centered disk would give a holomorphic exponential nonzero at an actual
zero of F, so the stated centered radius is exact. This argument does
not establish divergence of the exponentiated product at every individual
point beyond the disk, and the note correctly does not claim that.

The derivative computation gives the same positive rate constant at
both boundary points,
`exp(-gamma) k sin(alpha) cos(alpha)^(k+1)`, with alpha=pi/(2k).
For k=3 it is `27 exp(-gamma)/32`. The conjugacy of A and -A forces
every odd-degree source character to vanish. The sign of the leading
even-degree character is correctly `(-1)^m sigma^(-2m)/m`.
Trace cancellation inside actual source modules explains the gain;
dimensions, singular values and ordinary Schatten thresholds do not change.

## Exact controls and proof bounds

The producer computes both the identity and involution coefficients from
native symmetric powers, then applies the source Adams/PBW inversion.
Even powers of the involution correctly use the identity series. The
derived plus/minus multiplicities have enforced integrality, positivity
and parity. Degrees 1--3 are independently compared with the actual
frozen Lie quotient, not only a rational-factor reconstruction.

At `tau=i/sqrt(3)`, paired odd grades combine to
`(1+3^(-n))^(epsilon_n/2)`; even grades use the exact rational
`tau^n=(-1/3)^(n/2)`. The two-grade product is `1/8`, consistent with
the independent check in the suite. All large multiplicities remain
integer weights of logarithm intervals; no repeated-state array or
large multiplicity power is allocated.

The proof's explicit Cauchy constant at radius 2/3 correctly bounds
`V=-3 log(1-t^2)-log D_2`. Its dimension tail is
`27(8/9)^65`, the boundary Taylor tail is
`8 C (7/8)^(N+1)`, and the omitted regularized-grade tail is
`(45/4)(2/3)^(N+1)`. These bounds explain why
`log D_N(tau)+H_floor(N/2)` tends to `log(27/64)`.
The factor two converting this regular part to the rate `27/32` comes
from `N exp(-H_floor(N/2))`; it is not an arbitrary normalization.
The real-point error decomposition also has the stated three positive
tails on its declared domain.

The log1p intervals have a rigorous geometric tail and are multiplied by
source multiplicity before outward rounding. The finite compatibility
checks compare these intervals with proved analytic remainder bounds;
they do not infer an infinite theorem from approximate convergence.
The named real point `11/20` is strictly outside trace class and strictly
inside the improved disk; `9/16` supplies a separate held-out input.

I read all 16 tests, including source characters, malformed caps/domains,
odd/even cutoff handling, counterfeit fixture refusal and predecessor
authentication. Compiled Git blob/hash checks precede imported runtime
code. Complete canonical JSON comparison preserves numeric types.
No proof-critical runtime acceptance uses an optimizable Python assert.

## Execution and scope limits

The root/writer reported successful Ruff, producer write/check, optimized
check, and 16 ordinary plus 16 optimized tests, followed by final document
hash binding and replay. These are root-reported execution results,
separate from this independent proof/code reading.

The finite controls cover named involutions and ranks; they do not
machine-prove the general unitary theorem or every k. The analytic
source, Koszul/PBW and earlier Hilbert-root results remain dependencies.
The new continuation concerns canonical whole-grade products, not an
ordinary Fredholm determinant outside trace class. It does not reach a
classification of every tuple beyond the second-regularization region,
an arithmetic prime source, conductor or archimedean completion, or an
RH/GRH conclusion. External priority is not established by this review.
