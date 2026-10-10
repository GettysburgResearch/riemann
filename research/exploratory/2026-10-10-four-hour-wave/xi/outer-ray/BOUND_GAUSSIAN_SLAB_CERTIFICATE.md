# Native Taylor-bound Gaussian transport across real zeros

Status: proposed certificate; complete directed replay passed, independent
certificate review pending. Result: actual `Xi(z)=xi(1/2+i*z)`, derivative order zero, `lambda=10`,
and the closed rectangle `|T|<=100`, `0<=y<=1/2`, `z=T-i*y`.

The checker [check_bound_gaussian_slab.py](check_bound_gaussian_slab.py)
replays the same entire 8,049-zero primitive census and imported complete
count as NATIVE_SLAB_CERTIFICATE.md. It separately evaluates the native
Taylor jet by directed Gamma/zeta series and uses (TB3) to enclose the
**whole actual coefficient interval**. The Gaussian parameter is enclosed
by that interval, rather than replaced by its midpoint. Nonreal unseen
tail zeros remain allowed in the classical strip.

The finite product is evaluated by the full adapter in
[FINITE_PRODUCT_JET.md](FINITE_PRODUCT_JET.md). All known roots whose
bracket lower bound exceeds 256 are in the finite far part. With `K=16`
and `B=101`, every one of those finite factors is retained in the finite
Taylor sums and the explicit geometric remainder. All other known roots
are evaluated individually. On each complex box, paired factors whose
brackets meet the real interval enlarged by one are handled by the exact
local polynomial and (FJ6)--(FJ7), which avoids division at their real zeros.
Every remaining bulk and companion denominator is guarded.

The positive-T half starts with 400 by 4 boxes of widths `1/4` and `1/8`,
exactly covering `[0,100]` by `[0,1/2]`. A failed enclosure is replaced by
all four exact dyadic children, with depth exhaustion failing the checker.
The identity `leaves=1600+3*splits` guards the full finite cover, and every
accepted leaf encloses the whole source-bound parameter ball. The exact
even-real companion symmetry (GS2) gives the negative-T half. The disk
`B=101` contains the entire rectangle since `100^2+(1/2)^2<101^2`.

The unseen infinite tail remains complete. It is controlled by (G6), with
the source-qualified count bound and the negative endpoint in (GS1).
On every accepted leaf, the checker requires the strict predicate (G14)
and extracts the actual-source lower bound (GS3). The finite Taylor
remainder (FJ3)--(FJ4) is part of its Gaussian-base ball computation; it is
distinct from and additional to the unseen infinite residual budget.

All root, Taylor, parameter, polynomial, finite remainder and transport
arithmetic is directed Arb/acb/acb_series at 160 bits. The accepted receipt
stores exact rational domain margins and hashes the displayed direct
proof/checker sources and backend binaries. The FLINT historical finite
complete-count contract has precisely the imported scope stated in the
native census document; its Rosser rule input is not independently rerun.

The full replay accepted all 8,049 primitive brackets and all 29,509 leaves
from the 1,600 coarse boxes and 9,303 complete four-child subdivisions.
Maximum refinement depth was five. All 111 low factors and 7,938 finite
far factors were retained. The exact receipt bounds imply
`Re W_Xi > 1/200000` on the entire closed rectangle.
The full receipt is stored without losing any exact rational box margin as
[bound_gaussian_slab_certificate.json.gz](bound_gaussian_slab_certificate.json.gz),
deterministic gzip JSON. Standard `gzip.open(..., "rt")` and `json.load`
read its complete records. Compression changes storage only; every box is
replayed before the artifact is written.

This target is finite and has fixed derivative order and lambda. It
produces no new complete census above 8192, no whole-half-plane sector,
and no RH conclusion. Failed sufficient enclosures will not be treated
as negative points or accepted domain claims.
