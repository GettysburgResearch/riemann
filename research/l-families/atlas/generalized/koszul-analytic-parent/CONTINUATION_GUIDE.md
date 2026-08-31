# Continuation guide: source objects and their analytic limits

This is the current, deliberately unbound frontdoor for the continuation
of programme #764 in PR #769. The original README and the individual
proof/replay packets remain frozen. Their historical status sentences
should be read together with the exact-SHA review and validation records;
this guide does not rewrite those authenticated sources.

The continuation constructs an analytic realization of a classical
Koszul Lie parent, then tests its ramification behaviour against actual
S3/S4 covers. A separate construction completes polynomial-growth
finite-grade arithmetic cohomology. The latest companion also realizes
the exponential Lie source itself in arithmetic cohomology. These
constructions are related by specified source functors, but their
operators and convergence domains must not be identified.

| Object | Actual source and grade growth | Operator and variables | Analytic domain | Duality and boundary |
| --- | --- | --- | --- | --- |
| Local Koszul Lie parent | The quadratic Segre algebra determines L; the operator uses M_n=L_n^*. In non-finite profiles dim M_n is asymptotic to Lambda^n/n. | K_g(t) is the Hilbert sum of t^n g acting on M_n, with even numerator and odd denominator. | Compact for abs(t)<1. In S_p exactly for abs(t)<rho^(1/p), rho=1/Lambda. Ordinary Fredholm recovery requires abs(t)<rho; rank (2,3) has rho=1/2. | Source dual and parity are essential. A regularized determinant or conditionally ordered grade product has to be specified separately. Boundary constants and the actual S3 cutoff anomaly do not improve the operator's Schatten domain. |
| Finite-grade arithmetic source | R_n=Sym^n(V) tensor Sym^n(W) on a specified finite cover, with full ramified inertia and residual Frobenius. Dimensions grow polynomially in n, but each n is finite. | Actual finite H^i(P1,j_*R_n), or its specified quadratic twist. Arithmetic variable T; n is a grade label. | The cohomological ratio is rational in T. A twist with no H^0/H^2 gives a polynomial. | Classical curve duality and purity apply to each finite source. H^1 zeros have radius Q^(-1/2). Bad-point factors require the full invariant source, not an invariant-input shortcut. |
| Infinite graded global cohomology | The direct sum of those actual finite H^i spaces with their source multiplicity spaces. Growth is polynomial, unlike M_n. | K_i(z) acts by z^n times finite Frobenius; the ratio of det(1-TK_i(z)) equals product_n L_n(Tz^n). | Every S_p for abs(z)<1, bounded noncompact at abs(z)=1, unbounded outside. Meromorphic for all finite T; fixed quadratic twists here are entire in T. The initial true Euler product requires abs(T)<1/Q. | Closed points require z^(n deg v). Finite-cutoff duality sends (T,z) to (1/(QT),1/z), outside the same trace-class disk. Zero circles stack with n. For fixed real 0<T<1/Q, the proved source-count obstructions give a natural boundary at abs(z)=1 under the stated hypotheses. |
| Arithmetic cohomology of the actual Lie source | The S3 local systems M_n themselves, with their full ramified stalks. Their actual finite cohomology still has exponential growth asymptotic to constants times 2^n/n. | Parity-signed ratio with determinant exponent (-1)^(n+i) on H^i_n. M_1 is the regular S3 representation and gives the actual closure zeta factor. | Each cohomological parity block is in S_p exactly for abs(z)<2^(-1/p). Ordinary signed Fredholm ratio for abs(z)<1/2 and all T. Actual place Euler product initially requires Q abs(Tz)<1 as well. | At T=1, unramified place factors recover F_Frobenius(z^deg); bad places need explicit invariant-Lie corrections. Near z=-1/2 the continued local exponent is T times #Z(F_Q)/6. For Q=1 modulo 3 the arithmetic T=1 source has cubic monodromy. |
| Full invariant-Segre place Euler source | The original finite R_j algebra at every place, including full bad-place inertia and residual Frobenius. | E_R(z)=product_v sum_j tr(Frobenius on R_j^I) z^(j deg v). Compact-support Lie cohomology provides finite extraction factors. | Initially abs(z)<1/Q. The new source theorem gives single-valued meromorphic continuation to abs(z)<1 by finite extraction, without enlarging any infinite Lie operator's trace-class disk. | The bad-place correction cancels the first fractional branch and leaves zero order equal to the number of rational split good places. Surviving split-place zeros in all large degrees give a natural boundary at abs(z)=1. This is a distinct completion from the infinite polynomial-growth cohomology sum. |

The Hilbert metrics are specified in the proofs. In particular the
arithmetic construction fixes complex realizations and norms on finitely
many actual Frobenius spaces and uses the same norm in every copy. It
does not claim a choice-free topology or identify the direct sum with
the cohomology of a completed infinite-rank middle-extension sheaf.

## Read the analytic parent in this order

1. [The quadratic source, dual, equivariant PBW and ordinary Fredholm theorem](MATHEMATICS.md).
2. [Mixed ranks and the genuine S_p regularized determinants](MIXED_RANKS_AND_REGULARIZATION.md).
3. [Critical operator ideals and intrinsic grade cutoffs](CRITICAL_GRADE_BOUNDARY.md), followed by [nonscalar first-zero radii](NONSCALAR_GRADE_RADIUS.md).
4. [The local analytic-continuation natural boundary and fractional cutoff constants](LOCAL_NATURAL_BOUNDARY.md).
5. [The actual S3 holonomy cutoff anomaly](S3_GRADE_CUTOFF_ANOMALY.md): at the first special circle, the same intrinsic finite-grade products can tend to d^(-1/d)F_g rather than the Abel value F_g.

The last two entries carefully separate the germ of a scalar analytic
continuation from an operator determinant on its genuine ideal domain.
They do not assert pointwise divergence at every exterior complex point.
The ordinary, regularized and grade-ordered products are not interchangeable.

The latest [actual global Lie cohomological theorem](GLOBAL_KOSZUL_LIE_COHOMOLOGY.md)
connects this parent to arithmetic without changing its source modules.
Its [ramification correction](S3_LIE_RAMIFICATION_CORRECTION.md) gives
three explicit Mahler equations and the failure of invariant-input or
invariant-Segre substitutions. Its first grading branch is tied to
actual closure point counts, rather than inferred merely from failure
of trace class. Finite cohomological poles can occur before that point;
the continuation proof factors out finitely many grades and proceeds
locally around those poles.

The cubic branch is not universal across source corrections. The actual
compact-support localization sequence removes the bad Lie factors; gluing
the genuine invariant-Segre factors then gives a holomorphic germ at
z=-1/2 with integer zero order equal to the number of rational completely
split good places. The [full Segre place-Euler theorem](S3_SEGRE_EULER_MEROMORPHIC_BOUNDARY.md)
continues that corrected source to the unit disk by classical finite
Koszul extraction and proves its different, later natural boundary.
Its proof does not identify analytic continuation with the same Hilbert
operator beyond the trace-class disk.

## Bind arithmetic sources before taking the infinite sum

[S3 ramification and its all-grade family](S3_RAMIFICATION_AND_GRADED_FAMILY.md)
uses the actual elliptic cubic cover and discriminant sector. It gives
two distinct low-degree failures: taking invariant inputs before forming
the Segre algebra, and taking invariant Lie grades before the PBW product.
The full invariant Koszul complex remains the appropriate finite source.

[Global finite-grade cohomological completion](GLOBAL_COHOMOLOGICAL_COMPLETION.md)
then gives a different infinite operator. The
[S3 duality and grading boundary](GLOBAL_DUALITY_AND_GRADING_BOUNDARY.md)
expresses its leading radial coefficient through the actual genus-three
Galois closure counts. The
[finite-group theorem and S4 specialization](FINITE_GROUP_SOURCE_BOUNDARY.md)
allow extra scalar group elements and retain their positive resonances.
For faithful S4 permutation input the identity coefficient is
5/12 times the genus-nineteen closure count series with denominator m^7.

The geometric constructions are maintained in the adjacent
[S3 source packet](../global-s3-prym/GLOBAL_S3_PRYM_SOURCE.md) and
[S4 resolvent packet](../global-s4-resolvent/S4_RESOLVENT_AND_RAMIFIED_FROBENIUS.md).
Their actual quotient curves, inertia projectors, independent point
counts and held-out extension degrees precede the analytic assembly.

## A quadratic twist has two different operation laws

| Construction | Multiplication/source meaning | Principal factor | Grading-boundary coefficient |
| --- | --- | --- | --- |
| Untwisted R_n | The original Segre graded algebra. | All grades with a trivial constituent. | Positive regular-cover count weights, with all scalar resonances included. |
| Fixed M_n=R_n tensor chi | A graded R-module. Two odd-colour factors multiply into the untwisted colour; M alone is not a subalgebra. | For the actual chi_u sources, H^0/H^2 vanish and grade zero contributes 1. A general quadratic cover can have a nontrivial grade-zero H^1 polynomial. | Signed difference of joint-cover and old-cover counts. Nonzero anti-cohomology and the identity-only full-pole hypothesis are essential. |
| Coherent A_n=R_n tensor chi^n | The diagonal subalgebra of the actual two-colour algebra R tensor (1 plus chi), equivalently the Segre source (V tensor chi,W). | Untwisted principal factors only in even grades. | Two nonnegative scalar weights: Ztilde/(2 abs(G)) and (2Z-Ztilde)/(2 abs(G)). The minus-grading source is the constant quadratic twist. |

See the [S3 fixed-twist construction](RAMIFIED_TWISTED_GLOBAL_COMPLETION.md),
the [general signed theorem and S4 diagonal-inertia adapter](QUADRATIC_SIGNED_SOURCE_BOUNDARY.md),
and the [coherent graded algebra comparison](COHERENT_QUADRATIC_GRADED_ALGEBRA.md).
The S4 infinity example is an explicit warning: over Q congruent to 3
modulo 4, a first Frobenius trace can be zero while a two-dimensional
stalk and its nontrivial local determinant remain. A second power detects it.

The S4 quadratic reconstruction has a complete degree-ten constituent
only in the p=5 panel, with the sixth extension degree held out. The two
p=7 panels retain four independently known traces. No later adapter may
silently promote those prefixes to complete degree-ten polynomials.

## Classical scope and the remaining programme gap

Koszul duality, super PBW, finite-cover cohomology, the trace formula,
curve duality/purity and regularized determinant theory are classical
inputs, with primary references and hypotheses in the proof packets.
During this run predecessor PR #766 independently acquired a
[formal Koszul realization at 834819bf96ce6611db5bc988c2ae88aa401c4656](https://github.com/gfreund123/riemann/blob/834819bf96ce6611db5bc988c2ae88aa401c4656/research/l-families/atlas/generalized/SEGRE_KOSZUL_LIE_PARENT.md).
That overlap is acknowledged; this continuation does not claim to be
the first Koszul realization or to discover the basic exponential growth.
The predecessor branch has not been merged or rebased into the frozen
source chain used here.

The later predecessor head
[`5de42b9f3f309d6770a64df7541b4aa50fed3a4c`](https://github.com/gfreund123/riemann/commit/5de42b9f3f309d6770a64df7541b4aa50fed3a4c)
also contains actual number-field global constructions: classical
level-one cusp-form spaces, a normalized Fourier-coefficient flag, and
a Schur quotient of the Rankin--Selberg period matrix. Their common
gamma factor and completed Eisenstein reflection give a meromorphic
quotient with real-half-line positivity. The stated quotient fails an
ordinary absolutely convergent integer-frequency Euler product, and
extra denominator-zero poles remain uncontrolled. The all-weight and
positive-spectrum notes retain those distinctions. Consequently this
continuation does not describe its predecessor as merely local/formal
or lacking global examples. Our finite-field geometry, ramified source
operations, exponential Lie cohomology and sharp analytic domains test
different maps and obstructions. The late overlap audit is read-only;
it is not a full independent review of those predecessor packets.

The polynomial-growth R_n scalar global products also belong to a
classical function family; this statement does not cover the exponential
arithmetic Lie completion.
[The exact multiple q-factorial reduction](CLASSICAL_Q_FACTORIAL_SCOPE.md)
expresses them as finite products/ratios of Narukawa's multiple
q-shifted factorials with actual arithmetic Frobenius parameters. The
source-count coefficients, ramification, operation law and exact domains
are the useful distinctions here; a new species of higher gamma function
is not claimed. Exterior special-function definitions do not by themselves
continue these germs through the proved natural boundary.

The outstanding programme gates are substantive. These finite-field
sources do not supply number-field archimedean factors, a native Riemann
operator, or a new proof of RH/GRH. Completing finite cohomology does not
prove an infinite-rank sheaf trace formula. The natural-boundary and
duality obstructions exclude the stated ordinary domains or finite
rational prefactors, not every possible new regularization. Any next
proposal must specify its source functor, ramification, topology and
operation law before claiming that it repairs these failures.

## Validation and source acquisition

Each replay authenticates exact Git blobs and LF-normalized SHA-256
digests before importing its frozen dependencies. Each JSON fixture binds
the proof, runtime, substantive tests and replay note and is regenerated
only before that packet's freeze. Root serializes all numerical/test work;
the independent reviewer separately reads proofs, code and controls.
The individual replay notes and exact-SHA reports distinguish those two
forms of evidence.

Packets 1 through 14 have passed their focused Ruff checks, producer
write/check and optimized checks, and all normal/optimized tests. Packet
13's coherent-algebra source is frozen at
`4fb6ffd9b626af2d9ee22fdd075280ccadb7a675`, with 24 tests passing in each
mode. Packet 14's actual global Lie source is frozen at
`83506c9741bded6c8932163ff8e56b78892155b2`, with all 29 localization,
ramification and branch-cancellation tests passing in each mode. Its
exact-freeze independent review is available. Checkpoint 5 includes
these completed sources and this guide.

Packet 15, the full place-Euler theorem linked above, is active work
outside checkpoint 5. Its proof and bounded source replay are being
extended and independently read; its final source binding and validation
are not yet complete. In particular its meromorphic-continuation,
natural-boundary and coefficient-asymptotic statements must be read as
this explicitly marked continuation until its separate freeze. No
pending packet is included in the passed test count.

The current packets' source freezes are direct ancestors of this branch.
The earlier graph companions retain their separately published review
source ancestry, as documented in the parent programme handoff. A shallow
clone must fetch the relevant full history before replaying authenticated
source chains; bypassing a missing-source check is not a supported replay.
