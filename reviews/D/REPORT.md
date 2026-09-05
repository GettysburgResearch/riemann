# Reviewer D — integrated-main mathematical re-audit

Status: first review pass concluded at the scope below; selective component
acceptance, proposed repairs, and explicit omissions. No canonical status changes.
Scope: mathematics already represented on main, including its exact historical
proof references; this is not Reviewer B's post-707 review.
Frozen main: `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
Frozen root tree: `91742c176e5f7e5df8669e9a55f258c4889a1c12`.
Review branch: `review/D/20260905-integrated-main-reaudit`.
What was run: 45 named independent bounded checks, 9,380 fixtures per Python mode.
Smallest remaining task: reconcile the exact corrections and scoped verdicts
below, then audit the named unread inputs and uncovered families.
RH status: no proof or disproof supplied.

## 1. Executive verdict

The review found real mistakes, but not grounds to discard the integrated
release wholesale. Five component statements fail as written. Two further
resident-main extractions lost a hypothesis or necessary definitions. Three
additional contracts need explicit quantifiers or norm assumptions. Several
previously recorded repairs are confirmed rather than presented as new findings.

The most consequential new error is the extrapolation from a fixed inverse
filter to a filter whose order varies with the observation scale. A bounded
periodic order schedule annihilates an exponentially growing synthetic input.
The most consequential source-normalization error is the claimed identity
between two different wavelet energies. The latter has a constructive outcome:
D supplies a separate suffix-field proof that preserves the literal old RH
criterion without using the false identity.

The strongest positive conclusions of this pass are that the scalar
Mellin–Landau consumer, exact fixed-row noncancellation, source-specific compact
Hall calculation, periodized carry/Jordan algebra, half-divisor algebra, and
the repaired finite-order Xi argument withstand the checks described below.
These remain reductions, local results or statements with specified imported
inputs. Their unproved arithmetic or all-order premises have not disappeared.

All verdicts are recommendations to the integrator. `ACCEPT_LOCAL` means the
specified component survived this review, not that its full source PR is
accepted or that every dependency has been rerun.

## 2. Exact coverage and review method

The release's 24 canonical families contain 139 rows. Its 22 mathematical
family packets contain 135 rows; the other four are three review-infrastructure
rows and the RH terminal. This arithmetic is consistent, not an omission.

This pass records 74 component-level review units. It inspected 46 mathematical
source files, of which two original sources were read only for their statement
and/or fixture; those exceptions are explicit in `SOURCES.tsv`. It also records
21 main metadata/contract files. These 67 records are exact commit/path/blob
inspection pins, not a claim that all source trees were downloaded or replayed.

Focused proof reading covers parts of eleven canonical mathematical families:
Mellin–Landau, SHARP/native, Q4, wavelet/XD, owner/Vaughan, Xi Pick, heat,
safe-line, Suzuki/Hardy, Dickman/Bellman and conjunctive APIs. One elementary
resident Schur-rescue statement is also checked in the Brownian/Weil family.
The legacy Robin, derivative-free Xi and correction packets are additionally
read as resident main mathematics. `COVERAGE.tsv` identifies what was not read.
No numerical percentage of the 139 claims is asserted: review units can split
one claim or examine only one component of a multi-source claim.

Method:

1. Freeze main and follow its listed historical source SHAs, not live branch tips.
2. Separate the current integrated wording from the original theorem wording.
3. Reconstruct finite algebra, signs, endpoint terms and counterexamples.
4. Mark classical imports, source identities and large certificates not rerun.
5. Supply replacement statements where a repair can actually be proved.

The same assistant previously worked on other project material, including
post-707 work. The D designation does not create an external referee or prove
absence of all historical authorship overlap. The code here is an independent
reconstruction in the operational sense: it imports no upstream producer and
recomputes from the displayed definitions. It is not an independent model,
external peer review, Lean proof or second special-function backend.

## 3. Seven concrete findings

### D-F01 — varying-order Q4 filters can hide exponential growth

P12, L-95601, extends a fixed-filter inverse estimate to `k=k(X)` under a
slow-order condition. That implication fails even for orders restricted to 2
and 4. R1 in `REPAIRS.md` gives a complete sequence whose second difference has
values `0,(-2)^m,2(-2)^m` in successive triples, while the selected second/fourth
difference vanishes after the initial rows.

The fixed polynomial filter theorem survives. The actual varying-row inverse
must have its own subpower bound; individually frozen inverses do not supply
it. This is a source-theorem overextension, not a counterexample to the actual
arithmetic Q4 sequence. Main's generic subpower-invertible filter statement
should be explicitly restricted so that this false extension is not imported.

### D-F02 — full spectrum does not imply a Birman–Schwinger eigenvector

P20, L-91900.6, equates a nonzero kernel with `1 in spectrum(K(0))` without
requiring that the spectral point be an eigenvalue. For
`K=diag((1-2^-n)^2)`, one is an approximate spectral point, but `I-K` is
injective. The above-one spectrum is empty, so the stated discreteness there
is not enough.

Replace spectrum by point spectrum, or add compactness/isolation at one.
The eigenvalue correspondence, negative-index and small-gain components
survive at their proper form domains. This is not a rejection of the
Birman–Schwinger principle.

### D-F03 — an incorrect principal-minor sentence is physically resident on main

P34 says a negative principal minor is sufficient but not necessary for
non-PSD. For a finite Hermitian matrix it is both. The valid warning concerns
checking only **leading** principal minors. The exact determinant expansion
proof and `diag(0,-1)` control are in R3.

The surrounding Hermite inertia formula is correct and survives. This is a
local certificate-semantics correction, not a lost global RH argument.

### D-F04 — the wavelet energy identification drops an endpoint weight

P13 defines a Hardy suffix energy with initial term `|G_mu(X)|^2`. P14 calls
its Cauchy–Poisson average the same energy. That average instead has initial
term `(X/8)^2 |G_mu(X)|^2`. The difference is exact and is nonzero on the
actual Mobius wavelet at X=16. The new directed rational reconstruction gives
`G_mu(16)` approximately `0.0107400328395` and energy difference approximately
`0.0003460449162`, with exact endpoints retained in the output.

Both explicitly defined energies are meaningful; their identification is
false. R4 proves a separate source-faithful suffix-field criterion for the
literal old normalization. It controls a fixed countable dense family of
compact Mellin multipliers, at least one of which detects any hypothetical
off-line pole. The classical RH Mertens bound supplies the converse.

Thus this review **repairs the criterion rather than rejecting it**. It does
not prove the energy estimate, pointwise comparability of the two energies,
or every quantitative rightmost-zero assertion in the successor manuscript.

### D-F05 — integration dropped n>=2 from the matched-pole annihilator

P32's resident section 6 omits the original P33 requirement `n>=2`. For one
node its vector is zero, and the claimed normalization -1 fails. R5 restores
the assumption and derives the correct normalization by partial fractions.
The original theorem statement already has the necessary hypothesis.

### D-F06 — integration dropped the Robin cap definitions

P29's powered dynamic program uses `n_r` without defining the certified
exponent caps from which it comes. The original P31 also requires that the
minimal tail fit inside the remaining budget. R6 states those assumptions
explicitly and gives a weaker cap-free option. The finite envelope proof
survives; its source fixture is rebuilt exactly.

This is a statement-completeness issue, not a discovered counterexample to
the Robin envelope. No large search range is inferred from the repaired
small fixture.

### D-F07 — a negative excursion at the initial endpoint is uncharged

P45's Poincare estimate includes a terminal-component remainder but no initial
boundary mass and assumes that all other negative components vanish at both
endpoints. For `f(u)=u-1`, `log Y=2`, the left side is 1/2 and the stated right
side is either zero or at most `1/pi`, depending on the component convention.

R7 charges both boundary components, or adds `f(0)>=0`. For asymptotic use
with one fixed function, an initial component that eventually ends contributes
only a fixed finite constant. Therefore the asymptotic reduction is repairable.
Also, total logarithmic excursion length is always at most log Y. Its subpower
condition is automatic, so the assertion that neither premise alone suffices
is incorrect. Main already recognizes the strategic length-key redundancy;
the missing initial boundary term is an additional finding here.

## 4. Contracts and already recognized repairs

**Growing regional Schur covers.** P46's displayed Schur inequalities are
correct. A growing subpower-sized partition also needs subpower bounds uniform
in the active regions, or a bound for their sum. R9 gives disjoint one-entry
regions: every fixed region has an eventually constant cumulative integral,
but O(log Y) activated regions carry total mass of order Y. This refutes the
pointwise-in-fixed-region reading, not a correctly uniform theorem or the
actual native arithmetic packet.

**First-chaos contraction.** P37 correctly eliminates positive higher-chaos
terms under exact intensity linearity. It does not, from support alone,
identify a contraction from the specified input features. R8 gives the exact
finite-Gram domination condition and its extension proof. If conservativity
already includes that inequality, the contract should say so.

**First-Hermite domain.** The all-center/all-resolution criterion in P27 is
not exhausted by the large-center wedge in P28. A sufficient remaining gate
must cover the entire complement, including bounded centers and arbitrarily
large resolution at each fixed center. A thin “constant-four” boundary needs
a separate propagation theorem before it can replace that complement.

**Xi reserve multiplicity.** P26 omits `(m0-1)R0` when the chosen low critical
orbit has multiplicity m0. Main already requires that correction. D retains
it and does not present it as a newly missed integration issue.

**Half-divisor endpoints.** P17's full-line Hardy estimate must be applied to
the coefficient source truncated at `n<=N`, before using the expanded interval
`[U,4N]`. P18 uses this finite field explicitly. Main's existing truncation
repair is essential; an untruncated field on the larger interval is different.

**Julia margin.** P38's displayed arithmetic equality should be
`21587/38416`, not `19751/38416`. The printed smaller positive lower bound
still follows. Main already records a margin repair; D confirms it conditional
on the two upstream mass bounds, which were not reread.

**SHARP empty levels.** Strict adjacent-level comparisons should be weak
when both levels are inactive. The first alternating pair is strictly positive,
so the m>=2 positivity conclusion survives.

## 5. Positive results and the reasons they survive

### Fixed arithmetic consumers

P01–P04 preserve the correct tail transform on `[1,infinity)`. Subpower
logarithmic negative mass makes the negative-part Mellin transform holomorphic
in the open right half-plane. The fixed box multiplier `(1-A^-s)/s` has no
zeros there. Landau's real-boundary argument applies to the remaining
nonnegative density with finite initial abscissa. This proves a conditional
consumer, not the arithmetic producer premise.

For rows 2 and 3, with `a=2^-z`, `b=3^-z`, substitution of `b=2a-1` gives
`3P3=-3(a-1)(a-2)`. The fixed 5:3 combination has the same factorization.
Neither root lies in `|a|<1`; no large-row asymptotic is needed. The positive
row-source factorization is also checked through its exact Mellin product,
finite row moment and positive activation increment `3N+2`.

The SHARP child is the actual Radon–Nikodym ratio, not a bare support cutoff.
At `(Y,Z,t)=(16,4,4)` it equals 1/5. The compact Hall minimum is independently
reproduced over all 66 prefixes and exceeds 7/20, with unique worst integer
prefix 13 at the boundary 67. This says nothing about the remaining rough
Euler-source identification.

The m>=2 positivity proof retains the duplicate 67 label and a strictly
subunit complete removal mass. Its distributional descent retains activation
atoms. The critical negative-mass identity uses only the absolutely continuous
negative variation, not all variation of the jump measure. A positive
primitive alone does not bound that variation.

### Carry, wavelet and half-divisor structure

The complete carry field is a finite sine transform of `1*f`. The exact
cyclic Green norm is reconstructed rationally, including its zero mode. The
periodized carry covariance is `(gcd(d,e)^2-1)/(4de)`, and Jordan inversion
produces a genuine positive Gram with a squared-logarithmic bound. That
measure is not the native fixed-endpoint ensemble.

The ratio-eight compactifier follows from the three carrier roots of
`(1-sqrt(2)z)(1-z)^2`. The factor-67 second shell and geometric scalar inverse
are exact. The source negative-mass criterion and the repaired literal MWOC
criterion remain reductions to RH, not weakened arithmetic bounds.

The half-divisor local coefficient is `binom(2k,k)/4^k`, whose convolution
square is the constant-one arithmetic function, not delta at one. Given the
upstream balanced-source identity, it produces two identical factors. The
future Hardy multiplier has sharp norm 3. The finite Haar autocorrelation
and ratio-four support are exact; the coefficient diagonal is subpower from
`|h_U(n)|<=tau(n)`. The signed off-diagonal is not bounded by that fact.

### Actual Xi through order three

D checked the order-two orbit monotonicities, the full symbolic three-node
determinant factorization, the `tp` curvature, one-orbit reciprocal-curvature
absorption, the total reserve estimate and the corrected local C2 passage.
For `p(t)=F(sqrt(t))/sqrt(t)`, the determinant factors into a positive scalar
times the two divided differences of `1/p` and `tp`. Both are nonpositive
after the reserve allocation, so the product is nonnegative.

Each off-line orbit costs at most `9m/b^2` of one low critical reserve. The
published verification through `3*10^12` and the stated zero-count bound
make the complete allocated amount less than one. Parallel-sum closure and
local C2 convergence then preserve reciprocal concavity. Restore the omitted
multiplicity remainder before taking that limit. Repeated nodes give duplicate
rows, preserving PSD rather than positive definiteness.

The published finite-height theorem was externally confirmed by primary
bibliographic/abstract sources, not rerun. The conclusion is therefore a
reviewed proof with named imported inputs, not a new numerical verification or
an unconditional Lean theorem. Order four and all-order positivity remain open.

### Heat, safe-line and legacy finite criteria

The terminal-pair heat argument retains bounded imaginary displacement,
subquadratic zero counting and local finiteness. Its first-Hermite pair has a
negative leading coefficient. The Gaussian Fourier normalization, pole terms,
gamma term and complete prime-power tail are retained. The finite replay
checks algebraic pieces, not the infinite explicit formula.

The safe-line beta differences and Bernstein partition are exact. Under the
stated zero expansion RH gives a finite positive Hausdorff measure. A matching
off-line zero creates a noncancellable interior generating-function pole.
For rational-center reduction, use continuity of the pole location in an open
neighborhood, not an unsupported assertion about continuity of a limsup.
The original upstream safe-line producer itself was not reread in full.

The resident derivative-free Xi secants, cross-Loewner Cauchy–Binet proof,
barycentric product localizers and two sign channels survive at their stated
RH-conditional or isolated-pair scope. The Hermite inertia and saturated
sign-chain arguments preserve multiplicity. None converts a local zero census
into a global functional sign.

### Robin and conjunctive components

Two independent exact integer algorithms agree on every sigma(n) through
5582. The maximum abundancy through 5040 is `403/105`, uniquely at 5040;
on 5041–5582 it is `224/65`, uniquely at 5460. Outward rational harmonic,
logarithm and exponential bounds prove the finite barrier and distinguish
5582 from 5583. This reconstructs the finite foundation only, not the larger
historical traversals. Canonicalization and its threshold argument remain an
infinite search-domain reduction.

The positive-completion Perron estimate retains the signed flux before
inversion. Matched transfer uses the identical transfer in both channels;
its pointwise infimum is attained. Root/excess absorption explicitly pays
`(1-theta)^(-1/2)`. These statements are correct deterministic interfaces.
They do not supply their own source estimates. The regional and excursion
qualifications in section 4 remain binding.

### Dickman and Suzuki limits of acceptance

D checked the algebra of the Stieltjes source transfer and the displayed
VK/Dickman exponent balance. The upstream P61 expansion, uniform profile
comparison and full parent/child parameter ranges remain imported and partly
unread. This pass does not newly discharge their mandatory integration fixes.
Likewise first-chaos support and fixed-scale Julia absorption are accepted only
at the source/norm hypotheses stated in their rows.

## 6. Integration actions

Apply the local replacement statements in R1–R10 through a new reviewed
repair commit, preserving the old source versions. In particular:

- narrow `Q4.FILTER.EXHAUSTION` so it excludes the varying-row shortcut;
- split the two wavelet energies and attach the suffix-field proof to the
  literal old criterion rather than retaining their false equality;
- fix the resident principal-minor sentence, restore annihilator `n>=2`,
  and restore the Robin cap/feasibility contract;
- repair the excursion endpoint and the growing-partition quantifiers;
- distinguish point spectrum from full spectrum at the feedback threshold.

The proposed dependency dispositions in `EDGES.tsv` keep valid component
arrows while blocking unsupported promotions. Nothing here changes the
canonical registry automatically. A repaired reduction is not a proof of
its arithmetic gate.

## 7. Explicit omissions and next audit targets

This is not an exhaustive re-review of main. No new verdict is issued for
unread claim bodies in the 139-row registry. In particular, the full native
first-owner and endpoint producers, P79 and critical-Taylor chains, factor-67
root programs, carry hinge, staircase/vector amplitudes and several historical
native-source assets remain outside this pass. The Brownian/Fredholm source
proofs are not reread merely because their main manifest was inspected.

Priority source inputs still needing a complete separate check include the
general reciprocal-zeta vertical-growth/Hardy adapter in P15, the P61/Dickman
uniform comparison and Bellman ranges, the complete balanced two-field source
identity, the fixed-scale Julia mass bounds and the original safe-line
arithmetic producer. Their dependence is explicit, not silently discharged.

No large zero census, repaired screw scan, Brownian campaign, original
infinite Gram campaign, repository-wide test suite, Lean build, Comparator,
Nanoda or axiom audit was executed. Formal-v0.1 is inspected here only through
its honest open-gate metadata. The earlier Reviewer B package is not an
independent premise of any D acceptance.

## 8. External reference boundary

The primary publication/abstract records checked in this pass include:

- D. Platt and T. Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
  Bulletin of the London Mathematical Society 53 (2021), 792–797,
  DOI `10.1112/blms.12460`, arXiv `2004.09765`.
- J. C. Lagarias, *Correction to: On a positivity property of the Riemann
  xi-function*, Acta Arithmetica 116 (2005), 293–294,
  DOI `10.4064/aa116-3-5`.
- R. P. Brent, D. J. Platt and T. S. Trudgian, *Accurate estimation of sums
  over zeros of the Riemann zeta-function*, Mathematics of Computation 90
  (2021), 2923–2935, DOI `10.1090/mcom/3652`, arXiv `2009.13791`.

These are source attribution and scope checks. No full PDF audit or numerical
rerun of these works is claimed. Classical Mertens implications, canonical
products, explicit-formula and spectral facts used above remain declared
inputs where this report does not supply a self-contained proof. No external
novelty or priority claim is made for any repair.
