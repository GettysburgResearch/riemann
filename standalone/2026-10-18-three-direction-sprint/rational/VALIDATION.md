# Validation scope and deposited receipts

All mathematical files remain **PROPOSED**. Finite checks authenticate
their stated finite arithmetic and normalization; they do not establish
uniform infinite cancellation, any new zeta boundary, or RH. Every
logical guard below is an explicit exception check, so Python `-O`
does not disable it.

## Exact identities and finite complete masks

* `verify.py`, `CHECKS.json`: 46,973 exact rational/formal-log guards.
  Rebuilds actual old ordered pairs, complete products and denominator
  coefficients, prime-incidence and short-Newton identities, target
  response and balances. Eight deliberate wrong variants are rejected.
  `OPTIMIZED_CHECKS.json` reproduces the same main-run data under `-O`;
  the mutation attachment is the only receipt difference.
* `check_compensator.py`, `COMPENSATOR_CHECKS.json`: 12,585 guards,
  including 585 global identities and 5,768 rectangular transitions,
  with the strict final native cells above Y^2. Five wrong variants
  are rejected. `COMPENSATOR_OPTIMIZED.json` reproduces the main data.
* `check_moving.py`, `MOVING_CHECKS.json`: 38,701 guards at 724 cells.
  Y=24 and 32 cover every window cell; Y=48,64,96,128 cover declared
  endpoint sets including every active-support transition. The actual
  annular floor is bracketed by exact integer inequalities. All shared
  square coefficients and every target pair are retained. Seven wrong
  variants are rejected. The final `MOVING_OPTIMIZED.json` reproduces
  all main-run gates, including both cutoff brackets.
* `check_operator.py`, `OPERATOR_CHECKS.json`: 904 guards, 13 middle
  choices and 278 top-pair triples. Confirms that the tempting global
  inverse filter cancels the target itself. Optimized receipt is
  byte-identical. This is a rejected construction, not a successful
  target-preserving estimate.

## Directed conditioning: finite statements only

`certify_conditioning.py` uses integer interval arithmetic with 160
fractional bits and exact rational prefix checks. For Y=517,L=16 it
certifies every cell 8353..268323, including 65,044 primitive nonzero
jumps, 51,002 nuisance states, the rank-one initial case, and every
transition. An independent smallest-prime-factor pass authenticates
the event set at EVERY cell; independent directed native prefixes and
equation residuals authenticate each state.

`CONDITIONING_CERTIFICATE.json` has 2,062,299 guards and proves a finite
Euclidean coefficient budget 4. `ZONOTOPE_CERTIFICATE.json` has
2,827,315 guards and also proves finite existence in the sharper box
budget 9/4, using the exact two-row facet criterion. Empty-generator
facets may have zero margin; no strictly positive uniform margin is
claimed. The respective optimized receipts are byte-identical.
`CONDITIONING_MUTATIONS.json` records five rejected defects, including
missing/flipped event, corrupt prefix, erased equation and budget 1.

`ADAPTIVE_SCOUT.json` and `CROSSING_SCOUT.json` are explicitly floating
reconnaissance. The latter uses 685 directed-sign-authenticated native
crossings through 65536, but its 152,095 coefficient tests are sampled
cells and floating linear algebra. It proves no cofinal conditioning
or actual complete-source contraction.

## Full pair transport and the new signed flux

`check_transport.py`, `TRANSPORT_CHECKS.json`: 759,226 guards at the
explicit finite choice Y=1024,H=32. H is floor(sqrt(Y)), not the
asymptotic X^(1/5+eta) parameter. The checker constructs all 2,775
top-prime targets, 286 interior transports, 2,489 corner targets,
1,139 distinct references, shared-prime references, 9,217 canonical
coefficients and all 44 declared native annulus/core mask cases.
Every omitted boundary target is paid explicitly.

With python-flint 0.9.0 at 192-bit precision, it independently certifies
the full finite transport-kernel energy at EVERY physical cell
1025..1050624, with all 3,591 harmonic-jump cells and no omitted time
tail inside that interval. Its enclosure is approximately

    0.000055185572824787484347402175050640740977212043906495.

Six wrong variants are rejected. The strip-boundary negative control
uses a separate actual nonzero squarefree old-pair fixture (1021,1022),
where the area term alone is below one. Omitting that boundary happened
to survive the original diffuse finite population; the report does
not mislabel the separate fixture as a population failure.
`TRANSPORT_OPTIMIZED.json` reproduces the main data; only the negative
control attachment is omitted. Root supplied an independent complete
kernel implementation and separate receipt in `../reviews/`.

`check_flux.py`, `FLUX_CHECKS.json`: 80,840 guards for the actual signed
old source at Y=256 and product block [4096,8192), H=16. It rebuilds
1,244 nonzero target coefficients independently from all divisor
factorizations, including 613 negative coefficients, every good
reference and shared input prime. It checks zero transported mass,
the compact flux's absolute BV and localization resources, exact
Mellin integration by parts at powers 1,2,3,-1 and the formal log
moment, then independently replays the complete harmonic/flux identity
on ALL 65,792 native cells. Three wrong variants are rejected.
`FLUX_OPTIMIZED.json` reproduces every main-run field.

The flux check was added specifically to test the new Mellin derivative
normalization and every-jump identity used in `FLUX_COMPRESSION.md`.
It does not certify the imported infinite Weyl theorem or the analytic
fractional Sobolev argument by numerical extrapolation.

`check_column_adapter.py`, `COLUMN_ADAPTER_CHECKS.json`: 4,948 active
guards in normal Python and under `-O`, with IDENTICAL reports. The
checker independently enumerates the complete original coefficient
polynomials and their squarefree-column adapters in four finite fixture
monoids, including 208 nonzero cases where h shares a prime with the
new column. It separately enumerates the coprimality projector and the
Q-smooth inverse-mask identity. Four wrong variants are rejected:
an extra Mobius sign in the projector, an illegal h-coprimality
condition, deletion of the outside square character, and deletion of
the original common input mask. These are finite algebra controls;
the imported asymptotic inverse moment and full coherent mean are
explicitly not certified by the fixtures.

## Mathematical review receipts

`CRITICAL_REVIEW.md` is this agent's independent hash-bound first read
of the other track's critical prime-ray theorems. Its directed replay
receipts rerun that track's own checker and are clearly distinguished
from an independently implemented numerical method.
`EISENSTEIN_REVIEW.md` is the independent hash-bound first read of
the hybrid moment calculation, including complete frozen tails.
`PHASE_REVIEW.md` independently checks the exact reciprocal and
reciprocal-square stationary phases, the rough-vector Fourier price,
and the primary square-root-phase theorem's actual interface.
The Eisenstein agent's independent review of our global pair transport
is `../eisenstein/GLOBAL_TRANSPORT_REVIEW.md`. These are component
reviews, not repository acceptance or exact-final-commit review.
Its additional `../eisenstein/FLUX_REVIEW.md` reviews the exact hashes
of the compact-flux and complete reference-projection arguments.
Root's `../reviews/MASKED_COMPRESSION_REVIEW.md` reviews the fixed
already-masked draft, and `../reviews/NATIVE_CONSUMER_REVIEW.md`
independently reconstructs the complete pinned all-prefix consumer.

`THETA_LATTICE_REVIEW.md`, `THETA_ANALYTIC_REVIEW.md`,
`GAUSSIAN_MEDIATOR_REVIEW.md`, `STRIP_MEDIATOR_REVIEW.md`,
`BESSEL_COMPLETION_REVIEW.md`, `ENTIRE_ONSITE_REVIEW.md`, and
`POSITIVE_ONSITE_REVIEW.md` bind the exact other-track drafts whose
proofs were reconstructed. Their architecture and quantifier limits
are stated separately; none is a classification of all approximants.
`INFINITE_DIVISIBILITY_REVIEW.md` checks the deductions from the
explicit classical Levy--Khintchine import, including the separate
infinitesimal-star corollary; it does not reprove that imported theorem.
`GROWING_GAUSS_GRAM_REVIEW.md` reconstructs both the squarefree and
complete sixth-power-free row Gram arguments and their true orthogonal
projection bound. The sixth-power-free extension was partly jointly
derived by this reviewer, as that receipt explicitly records. None of
these receipts validates an unbounded complementary row space.
`GROWING_RESIDUE_REVIEW.md` independently reconstructs the complete
growing weighted response matrix, its analytic tail resource and the
unit-cusp constant calculation for exponent-two progressions. It does
not import a squarefree nonconstant Gauss formula at those moduli.
`SUZUKI_COMPLETION_REVIEW.md` checks the other track's finite unit
centering, beta endpoint constants and exact Mellin multiplier; the
classical eventual-sign criterion is explicitly imported and remains
unsatisfied. `WEIGHTED_CANONICAL_REVIEW.md` and
`WEIGHTED_STRIP_REVIEW.md` separately bind their precise all-order
moment and connected-domain gates, without asserting those gates.
`RELAXED_MIXED_REVIEW.md` independently checks the whole robust
witness-polygon and selected-prime eligibility in the conditional
U^(6/5) consumer, including the exact closed-box inequalities. The
consumer's normal/optimized continuum-cover runs are separate replay
receipts; no arithmetic mixed-mean hypothesis is tested there.
The new cubic-core bounds are analytic source-qualified proofs. Their
all-power extension uses a complete bilinear comparison, rather than
an experimental signed-sector triangle inequality. The primary sieve
versions, fixed-family conventions, bad-frequency resources and full
profile separation are specified in the proofs. Internal reviews
reconstruct these estimates; no finite experiment is presented as a
test of the open complementary frequency estimate.
The Eisenstein track's `../eisenstein/CUBIC_CORE_REVIEW.md` also binds
the final all-power transfer and `JOINT_CUBIC_CORE_COMPOSITION.md`.
That composition rebuilds both-original-input collision restrictions,
the sharp integer-conductor cutoff and the actual radical-filtered
Poisson kernel. Its finite orthogonality formulas and convergent
row-sieve resources are analytic proof steps, not numerical fits.
The resulting simultaneous complementary signed form remains open.
`ANNULAR_PROFILE_DEBIAS.md` has independent complete reconstructions
in `../eisenstein/ANNULAR_PROFILE_REVIEW.md` and
`../theta/ANNULAR_DEBIAS_REVIEW.md`, including the annular/prefix
height distinction and the entire original Fourier integration.
`../theta/SIXFREE_POLAR_REVIEW.md` and
`../theta/UNRESTRICTED_POLAR_REVIEW.md` bind the true-weight coordinate
energy proofs, checking every exponent-five and sixth-replica local
resource and the ACTUAL restored adjoint normalization. These reviews
do not identify a complete operator or estimate either nonconstant
remainder. The corresponding bounds are analytic source-qualified
proofs; no new finite experiment is offered as proof of them.
`LONG_FRAME_REVIEW.md` binds the Eisenstein track's final exact
unweighted long-frame reconstruction and its actual principal synthesis
normalization. The review explicitly distinguishes the principal-energy
input and row-unitary gauge contributed by this reviewer from the
independently reconstructed frame proof. It validates neither unpaid
coordinate vector nor an all-power physical-row extension.

The source-qualified all-prefix/cofinal exponent theorem, Tolev's
uniform squarefree density, and the corrected Hiary--Patel--Yang Weyl
bound remain explicit primary-source dependencies. The full balanced
remainder estimate is unresolved after these checks and reviews.

The exploratory NumPy scripts `scout_adaptive.py`, `scout_crossings.py`
and their floating `ADAPTIVE_SCOUT.json`, `CROSSING_SCOUT.json` outputs
remain on disk and are ignored from publication. They are reconnaissance,
not dependencies of any proof, exact verifier, directed certificate,
mutation control, or review receipt. The exact and directed scripts and
their receipts listed above are retained for publication.
