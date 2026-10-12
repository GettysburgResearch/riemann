# Independent complete Hankel criterion and countermodel review

Status: ACCEPT, H1–H4, at their exact all-order actual-source criterion and
synthetic finite countermodel scopes. No actual all-order positivity or RH
conclusion is established by this review.

I read the complete frozen operator manuscript
`../../operators/NATIVE_HANKEL_MECHANISM_CROSS_REVIEW.md`, SHA-256
`72134f010ad4464d62017eb12d25faa09a64c2ce3bfd50c919c7c2c5612525f5`,
and exact checker `check_native_hankel_countermodel.py`, SHA-256
`b873f04ef3b0064a5e911afae11aeff4f6708986dcc218c4b8138be08e67a879`.
I independently replayed the checker in normal and optimized Python,
preserving the official receipts. Both outputs are byte-identical to the
owner's corresponding exact receipt, SHA-256
`019cf31bc5d832e490fb2b54c16447a753ea54ffca9d254f5cee69724ea778d9`.
The successful output authenticates
the declared rational synthetic source and interpolation, not actual Xi.

The full complete inverse-square sum gives the uniform geometric moment
bound needed in the GNS argument. All-order Hankel positivity gives
Cauchy–Schwarz on every pair of real polynomials. If f is null, applying
it to f and X^2 f shows that Xf is null, so multiplication is well defined
on the quotient. For each f the squared power norms are log-convex and
have the displayed geometric upper bound. A first ratio above B^2 would
force every later ratio at least as large, contradicting that upper bound.
Thus multiplication is bounded by B on the dense polynomial subspace and
extends to a bounded selfadjoint operator. Its constant-vector spectral
measure represents the complete moments on [-B,B].

The measure transform is analytic at every nonreal point. The complete
parity-square logarithmic derivative has a pole at every actual squared
source root, with residue minus its integer multiplicity. Normal convergence
off those locally finite poles is justified by the complete inverse-square
sum. Square is injective on the positive-real-part representatives, and
coincident multiplicities add; no signed cancellation or missing exponential
can erase a nonreal pole. Identity continuation from the common germ into
either half-plane therefore forbids nonreal root squares. Positive actual
theta excludes the remaining purely imaginary possibility. These steps
prove the stated all-order criterion equivalent to RH, without asserting
simplicity. The optional complete localizers are also valid.

For the declared representatives 15 and 100+/-i/2, the geometric bound proves
ALL scalar moments positive. The exact real quadratic interpolation kills
the real inverse-square node and maps the other two nodes to conjugate
values whose weighted squared contributions each equal -1. The complete
quadratic Hankel contraction is consequently exactly -2. The checker
independently computes the contraction from the first five complete moments
and verifies the interpolation and all-order scalar dominance condition.
Its first 64 scalar values are finite controls; they are not an execution
of the infinite scalar proof. Failure branches remain active under -O.

No mathematical gap found. The missing actual-source statement remains
positivity of EVERY complete finite Hankel form. A growing finite list of
positive scalar moments or matrices does not establish that statement.
