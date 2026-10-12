# Independent review of actual global heat and scalar-moment positivity

Status: full analytic/source/code ACCEPT; independent normal and optimized
native finite-guard replays PASS, byte-identical to the owner's receipt.
Scope: the complete ACTUAL-Xi heat trace positive at every u>0, and every
complete scalar shifted logarithmic moment positive for all k>=1 and t>=0.
The theorem includes all unknown complex occurrences and multiplicities.
It does not establish complete monotonicity of K, mixed/Hankel positivity,
global real zero location, simplicity or a cofinal simple census.
Exact sources: [GLOBAL_SCALAR_MOMENT_POSITIVITY.md](../GLOBAL_SCALAR_MOMENT_POSITIVITY.md),
SHA256 `bc0e85724fdd33ff1a0c5fe1a6e97d7f925823066847d2eff74435ab71db1826`;
[check_global_scalar_positivity.py](../check_global_scalar_positivity.py),
SHA256 `acf8c360928d4a2c7987ecc0eca5d499f13581c35749b5af27e1b1575d65a3ca`;
the complete heat source `d48987c9143620d6b433163c080a89f3bc4966764d0880a83666a671fda3fb29`;
the complete tail derivation `d0679c63b57ffe755ad22853bc5d2d98c007d00d4a1c4941e2383a91e184fcc7`;
the old count-free real-head receipt
`964f49cc79a61b354cd77fe1f077637e54bb46f39a5643e1455e87f60fabc4d6`;
and the actual theta/Jensen count source
`67725ad90c5caaad231c4e232b76f5c38c81a84efe5005fc8909342456afa726`.
What was actually run: native constants-only checker normal and optimized,
full code/proof read, all nine direct source and four loaded binary checks.
No new Hardy endpoints, root inventory, count routine, high jet or infinite
time/order enumeration was executed by this checker or this review.
Smallest remaining gap for RH: the complete mixed/Hankel sign family or
complete monotonicity of K itself; scalar positivity is strictly weaker.

## Small-time complete source bound

GS1's heat formula is the exact previously reviewed completed Gamma-minus-
prime source. Its factor `-2S` inside the bracket agrees with the complete
heat formula's `-1/(2 sqrt(pi u))` prime prefactor.

The Gamma integrand is nonnegative exactly outside its possible negative
region `0<q<12u`. On that region, dropping the Gaussian gives the lower
bound `(exp(-q)-exp(-q/4))/(1-exp(-q))`. The numerator inequality
`1-exp(-3q/4)<=3q/4` and denominator bound
`1-exp(-q)>=q exp(-q)` imply the stated `-(3/4)exp(3q/4)` lower bound.
For all `u<=U=1/100000`, the native `exp(9U)<2` guard pays the ENTIRE
negative integral by `-18U`.

The retained positive interval `[delta,1]`, `delta=1/20`, lies strictly
above `12U`. Its elementary positive part integrates to the exact J in GS2.
For its Gaussian loss, `1-exp(-delta)>=delta/(1+delta)=1/21`, giving
prefactor at most `399/20<20`; its exponential is at most `exp(-125/8)`
for every u<=U. All other discarded intervals have nonnegative integrand.
Thus the C lower bound pays the whole Gamma integral and all discarded
regions, rather than omitting an unknown-sign complement.

For n=2 through 8, `Lambda(n)<=log n<3` and `n^(-1/2)<=1` give the entire
coarse `21 exp(-log^2(2)/(4U))` upper price. For n>8 the logarithmic
derivative of the dominating real function is
`1/log x-1/2-log x/(2U)<0` under `log8>2`. Decreasing-sum integral comparison
therefore pays all remaining integers, and `log8>4U` changes its exponent
to the stronger Gaussian `-q^2/(8U)`. The integral is exactly
`4U exp(-log^2(8)/(8U))`. This D is a bound for the RAW prime sum S, not
its K prefactor; consequently C-2D is the correct complete bracket margin.
Every inequality holds uniformly on the entire small-time interval.

## All remaining times and all scalar orders

The count-free old census authenticates a closed complete real head through
5419 and an actual real root in `(14,15)`. Its head contributes at least
`exp(-225u)`. The separately reviewed Stieltjes bound uses the complete
actual theta/Jensen `N(T)<=T^2` count and every unknown tail occurrence to
give `(R^2+1/u) exp(-u(R^2-1/4))`. Its negative closed-head endpoint is
discarded safely. These source roles remain separate; no assumed real tail
or historical complete zero count enters the comparison.

The ratio B(u) in GS9 has both positive factors strictly decreasing for
u>0, since its exponential rate is positive. The finite strict B(U)<1
guard therefore covers all u>=U, including the common endpoint. The
small-time argument covers all 0<u<=U. Their union is exactly every positive
time. Every inequality compares complete sources and gives strict K(u)>0.

The closed head is real and every unknown root has positive real coordinate
above 5419, so every squared root has positive real part. For each k>=1
and t>=0, absolute Gamma/Laplace Fubini is paid by
`sum m/(t^2+Re(rho^2))^k<infinity`; outside a finite set those denominators
are comparable to `|rho|^(2k)`, and the complete inverse-square sum converges.
Hence GS11 holds with every occurrence and multiplicity. Its integral is
strictly positive by the already proved all-time K sign. This supplies
EVERY scalar order and nonnegative shift as an analytic theorem, rather
than extrapolating the finite native degree-32 experiment.

The logarithmic derivative f is therefore completely monotone as a function
of X>0. Its normalized integral logarithm starts at zero, has positive
derivative and is a Bernstein function. This is a statement about derivatives
of f; it supplies no complete-monotonicity signs of K itself. The previously
reviewed positive-Fourier Bessel/cosine countermodel has K>0 at every time
and all scalar shifted signs while retaining off-real zeros. Thus neither
the original positive Fourier source nor the new actual scalar theorem
can be promoted to the stronger mixed/Hankel or real-location conclusion.

## Independent executed guards and source boundary

[global_scalar_normal.json](global_scalar_normal.json) and
[global_scalar_optimized.json](global_scalar_optimized.json) both have SHA256
`316a88278fc8854c3a649d39c478b43d6e35588160eae0bc325e9b983cb45ace`,
exactly matching the owner's frozen `global_scalar_positivity.json`.
All nine direct proof/data/checker identities are current, every inherited
prior direct source hash was authenticated by the checker, and all four
currently loaded Arb/FLINT/GMP/MPFR binary hashes match the receipt.
Both modes use python-flint 0.9.0 / FLINT 3.6.0 at 320 bits.

The directed small-time margin C-2D is approximately `0.839824138165101`,
with a strict exact rational positive lower endpoint. The complete large-
time tail/head ratio at U is approximately `8.65529669210376e-121`, with a
strict exact rational upper endpoint below one. The exact finite interval
endpoints are retained in the receipts. The checker also enforces all
domain inequalities used by the uniform bounds, validates the explicit
prior count-free census scope and first-root bracket, and survives optimized
execution without removed assertions.

The native checker authenticates these constants and imported frozen
source identities; it does not independently prove the complete heat
formula, theta/Jensen theorem, count-free census or infinite transport.
Those load-bearing arguments were independently reviewed at their exact
identities, including the complete tail and head-coverage semantics.

Verdict: ACCEPT for GS1–GS11 as the stated complete actual-source heat and
scalar-positivity theorem, with exact finite directed guards. The universal
mixed/Hankel family, universal heat derivatives and RH remain open.
