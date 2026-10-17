# Complete Eisenstein norm tensors: local polynomial uniformity

**Status: proposed unconditional component theorem, with a complete written deduction from MRSTT Theorem 1.1(i). Independent mathematical review is required. No RH proof, new zero-free exponent, or full physical sextic moment is claimed.**

The source is now the actual complete rational-norm coefficient of an Eisenstein ideal sum, including distinct conjugate ideals, and not the one-bounded rational surrogate. At a split rational prime the native coefficient is -2. Its exact decomposition is `mu * (mu chi_-3)`.

For the actual k-fold tensor with all original column caps or full Gaussian tests retained, every fixed polynomial degree ell and every fixed B>0 satisfy

    integral_X^(2X) sup_(deg P<=ell; AP Q in (x,x+H])
        |sum_(n in Q) a_D(n)e(P(n))|^2 dx
      << X H^2 / (log X)^B,

provided

    X^(1-1/(3k)+epsilon) <= H <= X^(1-epsilon).

Test variation factors are explicit in PROOF.md. Phase and progression may vary for each interval. There is no Mellin-twist average. The result covers the native, coupled 0/1/m, two-channel, and geometric sources, uniformly in m>=2 and bounded powerful-prime profiles. Fixed norm Dirichlet twists and fixed ideal exclusions are included. Arbitrary physical sextic row twists and growing conductors are not included.

For one column, H starts above X^(2/3). For two columns, H starts above X^(5/6) in PRODUCT-norm coordinates: at product length X=D^2 this means D^(5/3+2epsilon), not D. All logarithmic powers are available, but constants depend on the chosen power. This does not improve #960's much shorter-H range everywhere.

The proof assigns each convolution tuple to its largest factor, keeps its original group caps, and applies the published short-interval theorem before summing the integrated errors. The completion kernels have a uniform absolute mass at weight 3/4; large and microscopic dilations receive separate positive bounds. This permits m to grow without applying a short-interval theorem to intervals of length less than one.

A further consequence, reusing #960's heavy/light endpoint argument, is ordinary growing-shift cancellation against any L2 second sequence. For the actual Gaussian kernel on the complete selected shell,

    sum_(h<=H) |sum_(D<n<=2D) f(n)conj(g(n+h))K_D(n,n+h)|
       << H/(log D)^B,

for D^(2/3+epsilon)<=H<=D^(1-epsilon). These are the full principal Eisenstein norm fibers, not independent-prime variables. The other shells are not bounded by this statement.

**Remaining gap:** any fixed logarithmic saving is still weaker than a subpower bound at polynomial H. No identification with #961's low-powerful theta pairing is supplied. Its OPEN-L, the critical signed energy, and RH remain open in this packet.

## Reading and replay

Read PROOF.md, then SOURCES_AND_VALIDATION.md. Run:

    python check.py > /tmp/local-uniformity.json
    cmp /tmp/local-uniformity.json RESULTS.json
    python -O check.py > /tmp/local-uniformity-opt.json
    cmp /tmp/local-uniformity-opt.json RESULTS.json
    python verify_manifest.py

MUTATIONS.json records six separately executed corrupted optimized processes. Their failure authenticates selected finite algebra, not the analytic theorem. The main diagnostics include 26 complete supported-ideal censuses, the full native norm identity through 20,000, local completion identities, progression preimages, unique largest-factor ownership, and dilation Jacobians.

Base: #960 at `c127f4f22d08585b699ccd59faa4eedd9bb001ae`.
Branch: `research/native-field-local-uniformity-20261017`.
Only this new standalone packet is added. Existing recovery archives, proofs, main, and integrated scientific status are unchanged.
