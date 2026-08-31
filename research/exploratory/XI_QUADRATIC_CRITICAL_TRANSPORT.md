# Exact quadratic transport from actual Xi critical jets

Status: PREREGISTERED THEOREM AND FINITE TEST DESIGN; no panel tested yet.
Authoring base: `64165b8c805d182dbc43f2e5855e64a86cf1aaf9` (HA).
Scope: one fixed actual-Xi parameter lambda64 and exactly the twenty-six
new HA nodes in its three boxes centered at 256, 512 and 1024. This is a
local transport theorem and a bounded actual-source test, not a cofinal
zero/alignment/capture assertion or RH claim.

## 1. Exact quadratic theorem

Let g be analytic on a neighborhood of the closed disc `|z-t|<=y+r`,
real on the real line near a real t. Let lambda>0 be fixed and suppose

`g'(t)=0`, `a=g(t)`, `c=g''(t)`, `a*c<0`,
`q=-a/(lambda*c)>0`, `2q<lambda`.

Define the positive real quantities

`d=sqrt(lambda^2-2lambda*q)`,
`y=lambda-d=2lambda*q/(lambda+d)`.

Choose any `0<r<min(y,2d)`. Suppose

`M3 >= sup_(|z-t|<=y+r) |g'''(z)|`

and the strict inequality

`M3*(y+r)^2*((y+r)/6+lambda/2) < |c|*r*(d-r/2)`.

Then `R(z)=g(z)-i lambda g'(z)` has exactly one zero counted with
multiplicity in `|z-(t+i y)|<r`. This zero is simple and in the upper
half-plane. This theorem by itself does NOT assert that `g+i lambda g'`
is nonzero there, or that any further numerator is nonzero.

Proof. Put w=z-t. Taylor's integral remainders on the stated disc give

`g(t+w)=a+c*w^2/2+E3`, `|E3|<=M3*|w|^3/6`,
`g'(t+w)=c*w+E2`, `|E2|<=M3*|w|^2/2`.

The exact quadratic model is

`P(w)=a+c*w^2/2-i lambda*c*w`
`    =(c/2)*(w-i y)*(w-i(lambda+d))`.

Its two zeros are separated by 2d. On `|w-i y|=r`,

`|P(w)| >= (|c|/2)*r*(2d-r)=|c|*r*(d-r/2)`.

On that circle, `|w|<=y+r`, and hence

`|R(t+w)-P(w)| <= M3*(y+r)^2*((y+r)/6+lambda/2)`.

The strict hypothesis and Rouche's theorem give the same zero count as P,
namely one. Counting multiplicity proves simplicity; r<y puts the entire
disc in the upper half-plane. No Gaussian substitute or asymptotic remainder
is used. Keeping the quadratic term removes the explicit linear-model
loss `2q/lambda` appearing in HA3; it does not ensure that the remaining
actual third-derivative bound is small enough. QED.

For actual `f(z)=xi_R(1/2+i z)`, use `g=f^(5)`. Thus a=f5(t), c=f7(t),
and the load-bearing third derivative is the ACTUAL f8 on a complex region.
The parent lambda is held fixed:

`lambda64=[Re psi(1/4+32i)/2-log(pi)/2]^-1`.

There is no exponential gauge or parameter change with the node height.

## 2. Frozen finite panel and critical-point certification

Use exactly all 26 new roots in the frozen HA fixture, sorted by box and
real center as in that fixture, excluding its fourteen earlier nodes.
Every node remains in the outcome table, including every failure. No
additional windows, alternate seeds or post-result radius choices are allowed.

For each node, start REAL Newton iteration for f6 at the exact real part
of its known HA dyadic center. Use 256-bit arithmetic, at most 24 steps,
stopping when the correction upper bound is less than `2^-170`. Iterates
use exact dyadic midpoints and remain real. A vanishing derivative enclosure,
domain exit, arithmetic obstruction or iteration limit is recorded; there
is no restart from another seed. Round a converged candidate to denominator
`2^180`. These iterations locate candidates only and certify nothing.

Around that real center t0 use the fixed radius `epsilon=2^-120`. Attempt
certification at precisions 256, 512 and 1024 bits, in that order. On the
full square containing this disc, obtain an actual f8 upper bound M2;
at t0 obtain residual A=|f6(t0)| upper and D=|f7(t0)| lower. Require

`A+M2*epsilon^2/2 < D*epsilon`.

This is Rouche against the linear Taylor polynomial, and gives exactly one
simple f6 zero in the disc. Its center is real and f6 obeys Schwarz symmetry;
conjugation preserves the disc and zero, so the zero t is REAL. The full real
interval `T=[t0-epsilon,t0+epsilon]` therefore contains t. Each failed
precision attempt is retained. All later a,c and Taylor coefficients are
evaluated over this entire real interval, never at an uncertified midpoint.

The HA companion root rectangle is retained unchanged, and its local parent
certificate is freshly reconstructed from the exact frozen center. Its
historical complete-box census is an authenticated parent theorem, not an
unnecessarily repeated computation here.

## 3. Every declared radius and literal third-derivative bound

For each certified real critical point attempt EVERY exact ratio

`r/y in {1/16,1/8,1/4,1/2,3/4}`.

The radius r is an exact, generally unknown source-dependent real number;
outward lower and upper ball bounds are used consistently. There is no
substitution of a rounded r into the analytic theorem. Each ratio attempts
256, 512 and 1024 bits in order, stopping at the first full certificate;
all failed attempts and all five terminal outcomes are retained. A failed
sign condition, discriminant, radius condition, analytic-domain bound,
Rouche inequality or parent-root matching is recorded explicitly.

Use both of the following declared methods for M3 whenever their domain
guards hold. Record both bounds; the smaller valid upper bound may be used.
No failed route is silently replaced or omitted.

1. Direct actual f8 ball evaluation on the entire square containing
   `|z-t|<=h`, with `h` the outward upper bound of `y+r`, and with the real
   uncertainty of T INCLUDED in that square.
2. A fixed 32-term Taylor expansion of f8 about each unknown real t in T,
   with actual Xi series coefficients evaluated over T, and an outer
   Cauchy radius `R=7/8` around EACH such t. Its enclosing outer rectangle
   includes the `2^-120` real uncertainty as well as radius R. Use the actual
   Xi scalar upper bound M on that rectangle, not a Gaussian approximation.

For method 2, let N=32, x=h/R<1, and let v_j enclose the Taylor coefficient
`f^(j)(t)/j!` for every t in T. Then the declared bound is

`sum_(n=0..31) |v_(n+8)|*(n+8)!/n!*h^n`
` + M*8!/R^8*binom(N+8,8)*x^N/(1-x)^9`.

Indeed Cauchy gives `|v_j|<=M/R^j`, and
`binom(N+j+8,8)<=binom(N+8,8)*binom(j+8,8)` for j>=0,
by comparing the eight product factors. Summing the generating function
`sum_j binom(j+8,8)x^j=(1-x)^-9` bounds the infinite tail. This proves
the bound on the full disc and needs only coefficient indices through 39.
If h>=7/8, this route fails explicitly rather than changing R or N.

The inherited literal wrapper domain remains
`20<Re z<1100`, `-1<Im z<2`; no override is permitted. All rectangles,
including uncertainty margins, must lie wholly inside it. Precision is
restricted to 256/512/1024 bits and Xi series cap at most 40 in this packet
(the inherited wrapper permits up to 55). Direct f8 uses nine coefficients.

For a transport certificate to be labelled as the MATCHED HA root, the
whole known HA root rectangle must lie inside the transport disc for every
admissible exact t,y,r. In particular the upper modulus of its displacement
from the interval-valued center `T+i*y` must be strictly less than the lower
bound of r. Mere overlap or midpoint proximity is insufficient. Matching
then inherits HA's separate local C5/R0/C0 nonvanishing and noncommon-root
certificate; it is not a new general consequence of quadratic transport.

## 4. Prespecified linear comparison and arithmetic contract

At the SAME critical t and SAME lambda, independently bound actual f8 on
the region `|z-t|<=2q`, using the two methods above with h=upper(2q).
Record the original HA3 quantity

`Delta=2q/lambda+(M3/|c|)*(4q^2/(3lambda)+2q)`.

HA3 certifies only if `Delta<1/2`; require the analogous full-rectangle
containment in `|z-(t+i q)|<2Delta*q` before reporting a match. This is a
separate comparison at each node, not the quadratic inequality relabelled
as the old theorem. No optional raw-alignment eta test is included in this
bounded panel. Existing raw/reduced/common-inner/physical distinctions stay
unchanged, and no new physical trace or cofinal lower bound is inferred.

Arithmetic class: MIXED of DIRECTED_BALL_ENCLOSURES, EXACT_RATIONAL and
CERTIFIED_INTEGER_COVERAGE. FLINT uses outward real/complex balls; all final
inequalities are strict outward interval comparisons. Newton midpoints are
scouts only. The source/runtime implementation trust and native binary lock
are inherited from HA/BC/OA, not formal special-function verification.

Fixed resource caps: 26 nodes, 24 Newton steps per node, three precision
tiers, five quadratic ratios and one linear comparison per node; series cap
40, source file bytes at most 24 million, own JSON bytes at most 12 million,
JSON depth24/nodes300000/container20000/string4096, integer/rational bit
length4096. No matrix survey, new height box, source-domain expansion or
arbitrary precision escalation is part of this preregistration.

The completed packet will authenticate all five frozen HA files, this
preregistration, and the inherited executable BC/OA source and runtime
closure. It will retain source/artifact hashes and a payload seal, exact
finite algebra controls, both-mode replay and independently resealed hostile
checks. Analytic theorem review remains separate from finite machine replay.

## 5. Post-scout source-evaluation refinement, frozen before its test

The initial declared node (the first HA node in the box centered at256)
converged to a certified simple real f6 critical point. Its q is about
0.263602, while the unchanged lambda64 is about0.861699; these decimals
are descriptive scouts, not acceptance data. All five initial quadratic
attempts failed. The direct whole-rectangle Xi evaluation at outer radius
7/8 was nonfinite, preventing the Taylor/Cauchy route; direct whole-region
f8 bounds were too wide at256/512 bits and could be nonfinite at1024 bits.
The linear comparison also failed. These initial failures are retained,
not reclassified as successes of the original evaluation implementation.

Before any refined replay, a bounded implementation refinement is now
declared: evaluate the SAME outer rectangle by a complete fixed16 by16
rectangular cover. Its full real extent is `[t0-R-epsilon,t0+R+epsilon]`
and imaginary extent is `[-R,R]`, with R=7/8 and epsilon=2^-120 unchanged.
Divide each extent into16 equal closed rational subintervals. There are
exactly256 cells, with shared exact endpoints and no gaps. Every cell
is evaluated using the SAME actual Xi scalar wrapper, inside the unchanged
source domain, at the already declared precision. Every cell is attempted;
one nonfinite cell makes this cover route unavailable at that precision.

If all256 upper moduli are finite, their maximum is a valid global scalar
bound for the outer rectangle and therefore for the radius-R circle about
every true t in T. Record the complete ordered cell stream's SHA256,
the number of attempted and finite cells, any failed indices, and the
global maximum. A fresh authenticated producer recomputes every cell; the
hash is not substituted for primitive replay. The direct whole-rectangle
attempt remains separately recorded. The smaller of its bound and the
complete-cover bound may be used when valid. One cover is shared across
the five ratios and the linear comparison at that critical point and
precision; it is not retuned for a favorable radius or cell.

This refines interval evaluation only. It changes no node, radius ratio,
critical-point uncertainty, outer radius, Taylor order, precision tier,
domain, or analytical inequality. It adds no new height survey or raw
alignment test. All mathematical failures remain valid outcomes.
