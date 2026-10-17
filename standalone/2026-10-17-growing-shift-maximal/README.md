# Quantitative growing-shift maximal cancellation

Status: proposed unconditional component proof; independent mathematical review pending.
No RH proof, improved zero-free boundary, or full physical sextic moment is claimed.

For the rational native/coupled/two-channel/geometric sources of #956, put

    r(H,X)=log log(3H)/log(2H)+(log(2X))^(-1/700).

For every 10<=H<=X, the new proof gives

    sum_(h<=H) max_(Y<=X) |sum_(n<=Y)F(n)conj(G(n+h))|
                  <= C sqrt(A) HX r(H,X)^(1/4),

where G is ANY sequence with sum_(n<=2X)|G(n)|^2<=AX. The bound is uniform in
all m>=2 and arbitrary powerful-prime profiles, including degrees varying with
X. S and the first source's ordinary Dirichlet character remain fixed.
Every summand is retained. This is an ORDINARY average, not weighted by 1/n,
and does not average the Mellin twist. It is not a fixed-h theorem.

Theorem A first proves a uniform short-Fourier square bound, with the frequency
supremum OUTSIDE the short-interval integral. The power components with
microscopic shortened intervals are estimated separately. A square-mass
partition then proves the endpoint maximum while retaining large coefficient
atoms. The full Gaussian kernel has a corresponding growing-band SHELL bound.

The deep input is the published Matomaki--Radziwill--Tao theorem, in its corrected
arXiv v3 form. Classical cancellation and Fourier methods are credited. The new
claim is the stated source extension and uniform/maximal consequence relative
to the inspected packets, not global priority for short-interval methods.

Read THEOREMS.md for complete proofs and SOURCES.md for the exact external input.
VALIDATION.md distinguishes finite diagnostics from mathematical review.

## Recovery and publication

The prior 25-file combined recovery already landed in #956 at
943d7714f81b97a75652ebc6e19990a88c917d4d. The two original subtrees match the
local archives exactly. RECOVERY.json records this pass's checks; no source is
duplicated or silently strengthened.

Latest #959's proposed 11/12 all-field bound is discussed, not used as a premise.
Its critical signed pairing remains unproved. The bound here also stops far
short of a critical power saving: at H=X^theta, the guaranteed relative gain
is only logarithmic. It cannot be summed into an RH proof.

Run:

    python check.py
    python -O check.py
    python verify_manifest.py

Proof and checker have the same author; no independent referee, Lean build,
upstream proof rebuild or repository-wide CI is claimed.
