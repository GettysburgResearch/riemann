# Independent exact-SHA audit: QT530732c5

Scientific source: `530732c5fd7f50364381f8af50e97ce809b674c5`.
Immediate parent: `edb7d1ccffdc83c8e2b95e533da078508d009990`.
Five-file authoring base: HA `64165b8c805d182dbc43f2e5855e64a86cf1aaf9`.
Reviewer worktree: `isolated/qt-audit-pass3`.
No scientific source file was changed. The review concerns this frozen
five-ratio source only, not any all-radius successor.

Verdict: PASS at the exact scientific source above. Mathematical,
independent finite, release-protocol and hostile checks are complete.

## 1. Scope and precise result

The exact quadratic Rouche lemma in the source note, lines11-70, is sound.
Its application requires an actual complex-region bound for f8. It does
not itself assert C5 nonvanishing or survival against another numerator.

All26 declared real critical-point intervals contain distinct simple REAL
zeros of f6. All390 quadratic and78 linear attempts fail their sufficient
strict guards, despite possessing valid third-derivative upper bounds.
That means noncertification, not absence of companion roots.

The separately labelled pointwise test is stronger: for exactly118 of
the130 fixed critical-point/radius pairs, every valid M3 fails the
sufficient quadratic inequality. The counts are26,26,26,21,19 for ratios
1/16,1/8,1/4,1/2,3/4. The other12 are UNRESOLVED, not impossible. Neither
statement covers any other radius, calibration or height.

There is no RH, actual-innerness, cofinal alignment, physical capture,
or global zero-count result here. In particular, real derivative critical
points and nonreal companion zeros are not off-line classical Xi zeros.

## 2. Native proof checks

At the real critical t, a/c=-lambda*q. Thus the exact quadratic is

    P(w)=(c/2)(w-i(lambda-d))(w-i(lambda+d)),
    d^2=lambda^2-2lambda*q, y=lambda-d.

The roots have separation2d. A circle centered at iy with radius
0<r<min(y,2d) contains exactly the first root and remains in C+.
Its modulus is at least |c|r(d-r/2). Complex integral Taylor remainders
bounded by M3 give exactly

    |R-P|<=M3*(y+r)^2*((y+r)/6+lambda/2).

The strict comparison therefore gives one zero counting multiplicity,
hence simplicity. No unstated real-root hypothesis on the entire function
or additional C5 conclusion is needed.

For the tiny critical disc, the comparator is
f7(t0)(z-t0), not a Newton approximation promoted to a proof.
The source's A+M2*epsilon^2/2<D*epsilon establishes one simple f6 zero.
Schwarz symmetry and the real center force that unique zero to be real.
The source evaluation includes the full square containing this disc.
This is implemented at producer line490.

Unknown-t geometry is handled correctly. Every exact t lies in
[t0-epsilon,t0+epsilon]; the full outer rectangle extends in real part
by R+epsilon and in imaginary part by R. The16x16 cells share exact
endpoints and cover that WHOLE rectangle. The same inclusion applies
to the direct derivative rectangle with h=upper(y+r), rather than a
midpoint radius. See producer lines260,546,557,594 and687.

The f8 Taylor coefficient is v_(n+8)*(n+8)!/n!, with n=0,...,31.
No factorial or shift is missing. Cauchy supplies the tail

    M*8!/R^8*binom(40,8)*(h/R)^32/(1-h/R)^9.

For j>=0 the binomial comparison follows factorwise from
l*(N+j+l)<=(N+l)*(j+l), l=1,...,8. This gives the uniform infinite
tail, not an extrapolation from the finite tests. R=7/8 and h<R are
kept fixed/checked. See producer lines532 and644.

Full-parent-rectangle matching uses an upper displacement and lower
radius. It cannot follow from overlap or midpoint proximity. Both
transport and matching must hold for a matched success; no such success
occurs in this packet.

## 3. Why118 are genuinely impossible

The diagnostic at source-note line297 and producer line907 reuses the
SAME certified real interval. It freshly bounds m<=|f8(t)|, so every
admissible disc supremum M3 obeys M3>=m. All factors multiplying M3
are positive, after the sign/discriminant/radius guards.

Consequently, lower[m*H(y,r,lambda)]>=upper[|c|r(d-r/2)] implies that
the strict sufficient criterion cannot hold for any valid M3. Interval
dependence causes only conservative widening; it does not invalidate
this implication. The diagnostic is not a search at a new favorable
source point, and no unresolved outcome is promoted to impossibility.

The polynomial g(w)=3/8-w^2/2+w^3/600 has M3=1/100 and passes all five
quadratic controls, while its linear Delta=243/320>1/2. This proves
that a strict gain over the old sufficient test can occur. It does not
assert a universal dominance relation between two fixed-radius panels.

## 4. Timeout/history audit

NativeRunner at producer line363 has the necessary separation:

- The canonical546-task history is pinned independently in code and the
  manifest. Every task is keyed by exact route, center, radius and tier.
- All373 prior successful bounds are genuinely recomputed and must agree
  exactly. A timeout or changed bound raises ReplayFailure, a RuntimeError
  that the ordinary mathematical-failure handlers do not catch.
- The161 old native-nonfinite entries and12 old timeouts provide NO upper
  bound. They remain frozen environmental history, not freshly evaluated
  mathematical failures.
- Every stored task must be requested by the fresh panel; the exact task
  set agrees independently. A omitted/new task blocks acceptance.

The timeouts are exactly the direct outer calls at nodes22-25 at all
three tiers. Every one of the78 complete covers supplies a fresh bound,
so the173 unresolved broad entries do not deprive any final attempt of
a valid M3.

The118 pointwise obstructions do not depend on any broad-task bound or
timeout classification at all: the critical certificates and fresh point
jets already establish them. The twelve unresolved cases must not be
promoted using the noncertifying upper-bound attempts.

I authenticate the recorded history and its treatment, not the reported
historical elapsed durations, faulthandler incident or process-stop
events themselves. Those facts were not independently observed by this
reviewer. They are not premises of the mathematical conclusions.

The original design9162b5ea, cover refinement24c52d25 and runtime/history
checkpointedb7d1cc are separately authenticated. The final pointwise
diagnostic is expressly post-result. This review does not call that
diagnostic a blinded prediction or erase the earlier interval failures.

## 5. Independent arithmetic and primitive reconstruction

The companion independent-audit script imports NO QT or HA producer code.
It verifies the frozen five scientific files, all four current artifact
seals, payload and history digests, and32 transitive Git/LF source bindings.

Using Fraction intervals and integer-square-root bounds, it recomputes
all130 pointwise decisions from source intervals using y=lambda-d, rather
than the producer's rationalized formula. It checks468 full Taylor
polynomial and infinite-tail majorants,390 failed quadratic guards,
all546 task identities,78 complete-cover geometries, and505 extra
binomial controls. All agree.

Separately, its directly written REFLECTED completed-Xi formula at1024
bits recertifies all26 tiny Rouche discs and independently reconstructs
the same130 pointwise decisions. Three additional full512-bit native
covers, at fixed indices0,12,25, evaluate768 cells and reproduce the
published cover maxima exactly.

This is independent formula/algebra code but the SAME pinned FLINT
special-function library. It is not a second numerical implementation
of zeta/gamma or formal analytic verification. Normal and optimized
independent outputs agree.

Frozen source fixture LF SHA256:

    45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce

Frozen source payload SHA256:

    8f41ac9fe470c9f88d198b20a1935b2e8dfd5f4a32471e1251f05a4bee50a44b

Environmental ledger SHA256:

    20e3b2d04d62b9b26119c77613a68fc9f4d76eba4be09bdee28d4f4bd7d8cd2e

Independent audit payload SHA256:

    cd08ea66f1efd75140242cba00ca6c87039f68abfddd82fe9f71eea1a621af65

## 6. Release checks

The source48-test suite passes at exact530732c5 in normal Python
(218.241s) and optimized Python (228.407s). The complete source note,
1052-line producer,657-line tests and manifest were read; fixture
semantics and all claimed finite counts were reconstructed.

Both source/fixture emit protocols, both producer checks, independent
normal/optimized replay, and genuinely fresh resealed attacks are
recorded in the final completion paragraph. Arithmetic is correctly
MIXED: directed outward balls, exact rational comparisons and complete
finite coverage. No acceptance relies on Python assertions.

No actionable mathematical repair was found. Remaining limitations are
the twelve unresolved pointwise cases, untried radii/parameters/heights,
the lack of any actual transport success in this panel, and the shared
pinned-library trust. None is concealed by timeout labels or a numerical
margin.

Additional acceptance attacks:19 strict guard/history-corruption inputs
were rejected in EACH mode. A fully resealed false-impossibility report
was rejected after complete fresh reconstruction in normal mode
(193.391s); an independently resealed false-cover-count report was
rejected after complete fresh reconstruction in optimized mode
(202.312s). No reconstruction function, successful bound or source cache
was mocked in these two full attacks. The separate hostile helper imports
the frozen producer only to exercise its acceptance API; the mathematical
independent helper remains free of author-code imports.

Final completion: both fresh producer checks PASS, and all four normal/
optimized fixture and source-manifest emits are byte-identical after LF
normalization. Independent normal/optimized checks both match the frozen
independent fixture. Ruff and formatting pass for the source and review
scripts. Full authoring-base-to-source and source-to-review whitespace
checks pass; all five scientific source files remain unchanged. No push,
main-branch modification or author scientific repair was performed.
