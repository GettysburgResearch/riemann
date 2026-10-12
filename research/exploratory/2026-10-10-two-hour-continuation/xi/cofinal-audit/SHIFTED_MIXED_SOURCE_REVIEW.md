# Independent review of the corrected shifted and mixed-moment packets

Status: full analytic, source and code review ACCEPT at the exact version-two
identities below; independent derived exact controls PASS in normal and
optimized Python. The owner reports native normal/optimized primitive replays.
This review does not duplicate the 11512 native Hardy endpoint evaluations.
Scope: finite complete simple census through 7570; a finite analytic rectangle
of complete mixed shifted signs; exact all-occurrence identities. No cofinal
census or all-order positivity is established.
Exact sources: the eight frozen version-two packet files in the next table,
the explicit old count-free census through 5419, the complete paired product,
the classical complete strip, and the previously reviewed column theorem.
What was actually run: exact derived checker normal/optimized, the owner's
mixed-cone checker normal/optimized with outputs in `/tmp`, source hashes and
all six loaded native backend binary hashes. No historical zero-count replay.
Smallest remaining gap: a source-specific uniform progress or complete mixed
positivity theorem. Native peer primitive replay is a separate execution gate.

## Frozen packet and repair identity

| File in the parent xi directory | SHA256 |
| --- | --- |
| SHIFTED_COMPLETE_MOMENTS_V2.md | 84dff8dd45a579649bf8c515ef273559147d0b3f4a12a158ce1d7fcad1e9505b |
| check_shifted_hierarchy_v2.py | 83b310782d3c98d8cdc27dbac35d6021a5a3de72f76fa64b07b732b4cd6dda44 |
| shifted_hierarchy_v2.json | d6cf40e46dbe0292aff5a48dc5ebec357f378ffed4b2e3aefbfe4d848d517ba3 |
| produce_continuation_prefix.py | d7fc0e858a4bc6f50d24f614eb7ab330a091097a4686890aee66631ad342698e |
| continuation_prefix_candidates.json | e60ea4bd85ee150bcd4ff00d535d5277266a9104c4f71217a0cc9a2cf3a59948 |
| MIXED_MOMENT_CONE_V2.md | dd82159893091b776bf216cb42e20c72a0ba75894898249ce337763717344893 |
| check_mixed_cone_v2.py | 436d5b3f6bf98d6ebac4c5e4df126e3752a24de34bf4e95c370a89335b5e53b4 |
| mixed_cone_v2.json | d7b25f57a33807e8d46e45755b7c962df1ccf8ad92540b6561fcfef7ad62d336 |

The original SM8 correctly enclosed the residual but its written full-width
bound omitted the native coefficient width. Version two adds `C_hi-C_lo` to
the root-interval width price and explicitly assumes `A>0, alpha>0` for the
large-shift explanation. Comparing the complete files confirms these repairs
and the new source/receipt identities. The checker arithmetic already retained
the complete native coefficient interval. This acceptance binds version two;
the preserved version-one files and receipt have their distinct identity.

## Complete analytic review

SM1 follows by evaluating every factor of the complete paired product at
`i sqrt(t^2-w)` and `it`: its ratio is `1-w/(rho^2+t^2)`. Absolute local
convergence permits coefficient extraction. Thus `-k[w^k] log` is the complete
sum, with integer multiplicities, and subtracting one actual real occurrence
per strict sign interval retains all other occurrences. No completeness of the
selected intervals is assumed at this stage.

SM2 optimizes `2xy/(x^2+t^2-y^2)` over `x>=0, |y|<=A` and obtains the sharp
angle `arcsin(A/t)`. The rational implementation uses
`arcsin v<=v/sqrt(1-v^2)` and `cos u>=1-u^2/2`: its exact guard bounds the
argument by `q` and the real projection by `c=1-q^2/2>0`. All remaining
occurrences consequently contribute positively. The inequality
`|rho^2+t^2|<=H^2+A^2+t^2` supplies a safe lower cost for any unselected
occurrence with `|Re rho|<=H`. Comparing this cost with the complete residual
upper endpoint excludes every such occurrence, including an extra occurrence
at a selected root. This proves completeness and simplicity simultaneously.
Boundary intervals are separately checked, so the literal finite count is
well defined.

The actual-Xi shifted jet in SM4 uses the exact completed source at
`s=1/2+sqrt(t^2-w)`, with positive real center greater than one. The local log
branches have real coefficients. The critical-center and shifted degrees are
48 and 32 respectively; the complete product identities, rather than numerical
parity checks alone, supply exact coefficient parity and reality.

SM5's conditional cofinal assertion requires real and simple zeros, growing
actual sign selections and convergent directed coefficient evaluation. Fixed
shift and order one then have a summable real tail tending to zero. Conversely,
cofinal successful simple-census guards force every zero real and simple.
Growing order with a fixed selection and `t=alpha k A` has a widening scale
`t/sqrt(k)`, so it does not supply that missing cofinal step. The general
shifted kernel decreases in the real coordinate under the stated stronger
angle control, but need not decrease in the imaginary coordinate; the checker
correctly uses the safe norm cost rather than an unjustified shifted corner.

The unshifted branch imports the exact old simple census
`964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6`
through 5419. Every newly nested low interval selects the same unique old
root, so all unselected occurrences have real coordinate greater than 5419.
The derivative-angle condition `(2k+1)A/5419<1<pi/2` validates the unshifted
joint corner. The shifted projection theorem itself needs no prior real-head
census, although this implementation also authenticates that import.

MC1 retains the complete mixed sum
`sum m lambda*(lambda/L)^n*(1-lambda/L)^j`. MC2 writes
`D=rho^2+t^2`, `Q=rho^2+A^2`, with positive real parts at unknown `x>R`.
Its phase is `-(n+1)theta_D+j(theta_Q-theta_D)`. Both quantities being
subtracted are nonnegative, so their maximum bounds the absolute phase.
The denominator in the exact angle-difference tangent is at least `x^4`.
Therefore the two stated monotone bounds apply to every unknown block and
every multiplicity. Known real-head terms are strictly positive. This proves
the entire finite rectangle, rather than testing a few coefficients or
replacing the complement by a finite set.

## Independent execution boundaries and outcomes

[check_shifted_mixed_exact_audit.py](check_shifted_mixed_exact_audit.py), SHA256
`8f6aa195c700e1adca466cf006d2427f2ae107768e224dde2335c4fb5efc32d2`,
produced byte-identical normal and optimized receipts:

- [shifted_mixed_exact_audit.json](shifted_mixed_exact_audit.json)
- [shifted_mixed_exact_audit_optimized.json](shifted_mixed_exact_audit_optimized.json)

Both have SHA256
`527d1f400083bff8bc1db6f6f3ebb3b8ee897b14c18c82b7d033f4dba2f1c4f3`.
They authenticate 27 direct source identities, all 8049 selected geometries,
all 5756 strict refinements, all 21 declared residual guards and boundary
counts, and all 528 finite mixed indices with `n+j<=31`. The unshifted cost
uses independent repeated Gaussian-rational multiplication; the owner uses
a binomial expression. The mixed audit reconstructs exact interval bounds
from all 32 complete native coefficient intervals and verifies strict
positivity and overlap with the owner's directed derived intervals.

The mixed-cone checker independently passed in normal and optimized modes;
both `/tmp` receipts exactly matched the frozen owner's
`d7b25f57a33807e8d46e45755b7c962df1ccf8ad92540b6561fcfef7ad62d336`.
Its extremes are exactly `8001/5419` and
`235929375000/159131975059`, both less than `3/2<pi/2`. The complete analytic
coverage is `0<=n<=8000, 0<=j<=900000`; those billions of entries were not
individually computed. This finite rectangle does not meet the all-order
Hausdorff criterion.

The strongest finite native record is shifted order 32 at `t=512`: height
7570, 7343 positive simple zeros, guard ratio approximately
`0.9950105344557233`, maximum column derivative order 15137. The old complete
column theorem then supplies its stated positive companion domains. The next
integer fails this particular guard; that does not refute another method.

The backend binary map was independently matched against all six currently
loaded python-flint 0.9.0 / FLINT 3.6.0 binaries. Source inspection confirms
that the checker has no candidate or zero-count calls and that its strict
gates survive Python optimization. The producer's `zeta_zeros` invocation
constructs candidates only. The native checker authenticates fresh strict
signs and complete coefficient/residual intervals, while importing 2293 old
strict sign intervals. It does not authenticate the infinite strip, theta,
product or column theorems. This derived exact replay imports the native
coefficient intervals and reports zero new primitive endpoint evaluations.
Independent native primitive replay remains attributed to its own reviewer.

Verdict: ACCEPT for the exact version-two analytic/source/code packet and
the finite derived controls stated here. RH and the uniform cofinal progress
requirement remain open.
