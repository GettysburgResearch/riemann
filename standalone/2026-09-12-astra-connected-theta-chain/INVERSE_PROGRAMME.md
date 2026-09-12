# What this changes, and the remaining all-order construction

Status: research proposal following the proved components in PROOF.md.
**No full identification of the chain with theta, and no RH proof.**

## The design change

The previous Ising programme had exact finite moment matches and a necessary
restriction on bounded lattice components. Merely attaching more dimers or
turning on negligible connecting edges is not an all-order construction.
The present model instead has one fixed infinite connected graph, a fixed
positive edge correlation, and a rigorously defined continuous limiting law.
Its complete complex convergence is paid before any identification with theta
is proposed. The infinite support of the observable is genuine: its weights
are not summable, although their squares are.

The unexpected calculational connection is between the observable's far tail
and the gamma factor's real-field growth. The `1/(2n)` tail creates the
`(h/2)log h` term. A finite total mass correction changes the linear term.
The summable `d log n/n^2` correction ALSO changes the logarithmic term because
large field samples indices comparable to h. Its coefficient is
`2d log(3/5)=7/4`. A bounded-error product comparison for the exact Markov
transfer matrices makes this a theorem about the full correlated law, not a
formal single-site approximation.

This is a family with correct leading growth, not evidence that matching that
growth forces the correct arithmetic zeros. The certified sixth-moment error
shows that it does not, even when the second and fourth moments agree exactly.

## An explicit inverse problem on the actual transfer map

For any positive weights and edge correlations 0<=q_n<1, compute the formal
endpoint response and characteristic function by

    S_new=(tan(a_n u)+q_(n-1) S)/(1-q_(n-1)tan(a_n u)S),
    -log F_new=-log F-log cos(a_n u)
                         -log(1-q_(n-1)tan(a_n u)S).

This is a constructive polynomial recurrence at each finite Taylor order.
It preserves the interactions and their signs; it is not a free mixture of
independent cosine laws. The finite interval checker verifies its low-order
instances against direct spin enumeration.

One next attack is to redistribute more of the finite head while preserving
its SUM A, and/or change positive edge correlations there. Such finite changes
preserve all three growth coefficients. They give explicit inverse equations
for additional actual theta cumulants. Nonnegative couplings and positive
weights must remain constraints, not penalties that may be violated by a fit.
The present two-parameter curve has the wrong sixth moment, so it is not an
all-order induction by itself.

A more ambitious attack lets the modified region grow, while maintaining a
uniform variance bound and a source-specific control of the remaining tail.
Lee--Yang and the bounded-variance moment bound would then pay complex
convergence if every fixed moment converged to its theta value. The limiting
spin process need not be this fixed homogeneous chain. There is no theorem
here asserting that the homogeneous-chain class is universal for Lee--Yang
laws, or that theta belongs to it even under RH.

## The exact sufficient conclusion, and what is not proved

If a family of finite zero-field ferromagnets with nonnegative weights satisfies

    |E X_m^(2r)-mu_(2r)| <= 2^-m, 1<=r<=m,

then its variances are bounded. The paired Lee--Yang product gives

    E X_m^(2r)/(2r)! <= (Var(X_m)/2)^r/r!.

This bounds the entire complex Taylor tail uniformly. Moment convergence then
implies locally uniform convergence of the characteristic functions to
Xi(z)/Xi(0); Hurwitz proves that the latter has only real zeros. This is the
complete conditional ending, not the missing construction.

The new packet proves existence of one infinite chain, TWO matched even
moments, a complete growth comparison, and a sixth-moment mismatch. It does
not supply that family, an arbitrary-order reachability theorem, or a global
continuation radius. It also does not turn a bounded positive-real-axis ratio
into a comparison of the oscillating characteristic functions on the real
Fourier axis.

## Exploration actually performed

Non-directed exploratory calculations tested simpler harmonic tails, then
selected the corrected tail and the rational parameter brackets. Several
fixed-correlation, few-head higher-moment fits did not reach their targets.
An early variable-correlation scout used a short correlation sum and was not
reliable near correlation one; it was discarded. None of those failures is
promoted to an impossibility theorem, and no scout value is accepted evidence.
The final model fixes q=1/5, reconstructs the whole infinite variance tail,
and independently verifies all brackets by outward integer intervals.

In the accepting implementation, an initial bisection stopped too early when
a midpoint interval overlapped the target; a quarter-point refinement repairs
that numerical enclosure issue. A coarse lambda rectangle was then too loose
for the whole-curve check; sixteen covering subintervals provide the stated
strict certificate. These are coverage/algorithm repairs, not exclusions of
unfavourable parameter points. The complete interval is still covered.

No actual zero of the constructed chain or of Xi was computed. There is no
numerical zero-density comparison, no physical Gibbs simulation, and no
large-field numerical fit used to prove the asymptotic.
