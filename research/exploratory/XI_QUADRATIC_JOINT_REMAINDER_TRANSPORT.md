# Joint Taylor remainder for the fixed Xi quadratic transport panel

Status: completed joint-remainder theorem and fixed-panel inherited-data replay.
The POST-QT design in Sections1-3 was frozen before any new comparison at
99a7eb0310ca86392ef28b91b7c6d1fe81f35e61. Sections4-6 report the outcome.
Base: QT science 530732c5fd7f50364381f8af50e97ce809b674c5.
Scope: the same actual Xi primitive, fixed lambda_(64), twenty-six certified
critical points, five prescribed radius ratios and three precision tiers.
No source window, gauge, parameter, derivative bound or parent certificate
is changed. No novelty, RH, innerness or physical-capture claim is made.

## 1. Joint remainder theorem

Keep every hypothesis and definition in QT Section1. In particular
g'(t)=0, a=g(t), c=g''(t), a*c<0, lambda>0,
q=-a/(lambda*c)>0, 2q<lambda,
d=sqrt(lambda^2-2lambda*q), y=lambda-d, and
0<r<min(y,2d). Then 0<y<lambda.
Let M3 bound |g'''| throughout the same closed disc |z-t|<=y+r.
The exact quadratic is
P(w)=a+c*w^2/2-i*lambda*c*w, w=z-t.

The integral Taylor remainders combine BEFORE taking moduli:

    R(t+w)-P(w)
      =w^2 integral_0^1 tau*(w*tau/2-i*lambda)
                          g'''(t+(1-tau)*w) d tau,
    R=g-i*lambda*g'.

On |w-i*y|<=r and 0<=tau<=1, the triangle inequality centered at i*y gives

    |w*tau/2-i*lambda|
       <= |i*tau*y/2-i*lambda|+tau*r/2
       =lambda-tau*(y-r)/2.

The equality uses y<lambda, not an unrestricted assumption on an arbitrary
disc center. All segment points lie in the original |z-t|<=y+r disc.
Consequently

    |R(t+w)-P(w)|
      <= M3*(y+r)^2*(lambda/2-(y-r)/6).

The factor is positive. The new sufficient Rouche criterion is

    M3*(y+r)^2*(lambda/2-(y-r)/6)
          < |c|*r*(d-r/2).                              (JR1)

QT's unchanged lower bound for |P| proves exactly one simple upper-half-plane
R zero in |z-(t+i*y)|<r. No statement about C=g+i*lambda*g' or other
numerators follows without their separate nonvanishing certificates.

The old remainder factor is lambda/2+(y+r)/6. Its difference from the
new factor is exactly y/3>0. This is a genuine theorem improvement but
does not predict that any actual panel cell will certify.

For an exact NONNATIVE control take
g(w)=3/8-w^2/2+w^3/18, lambda=1, c=-1,
d=y=1/2, r=1/4, M3=1/3.
The old and new allowable M3 thresholds are respectively4/15 and4/11.
The exact model-bound lower side is12/128, the old error bound15/128,
and the joint error bound11/128. Thus only the joint criterion certifies.

## 2. Frozen post-QT comparison design

Before any new comparison, fix all of the following:

- Use the exact QT frozen five-file packet and its authenticated source
  declarations. Inherit its actual critical intervals, jet balls, M3 upper
  bounds, parent root rectangles, performance history and certificate proofs.
  Do not rerun or claim to reproduce the full QT special-function producer.
- Attempt ALL26*5*3=390 old quadratic records, at their original source
  ratio and precision. There is no stopping after a success. Retain every
  old outcome and every new failed or unresolved record.
- Reconstruct outward Fraction intervals for lambda,q,d,y,r,c and the
  new error factor. Square roots use integer square root with a fixed
  512-bit dyadic enclosure; no floating computation or new FLINT call.
  Retain every exact lower/upper endpoint and comparison.
- A pass requires all QT prerequisites and the strict upper-error versus
  lower-model-margin inequality. A nonpass means the inherited interval
  data did not certify; it is not a mathematical impossibility conclusion.
- For any new pass, separately prove that the ENTIRE inherited HA companion
  root rectangle lies inside the new transport disc for EVERY admissible
  exact t,y,r. Use an outward squared-displacement upper bound against
  the squared lower radius; midpoint proximity or overlap is insufficient.
  Only then label it a matched parent root and inherit its separate
  C5/R0/C0 nonvanishing guards.
- Summarize all390 cells and all130 node/ratio cases, with no additional
  radius or parameter choices. No new lower-bound diagnostic or all-radius
  search is part of this design.

The unchanged QT/QR obstruction to the OLD sufficient criterion remains
valid. It is not a theorem about JR1, which has a smaller error majorant.
The actual source remains g=Xi^(5), so g''' is the inherited actual Xi^(8).

## 3. Arithmetic and review boundary

The new arithmetic is MIXED: EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE.
Operations are exact Fraction/integer operations; square-root interval
rounding is explicitly outward to the fixed dyadic grid. Inherited directed
balls retain their original proof/runtime provenance and are not advertised
as newly computed values.

The completed proof/producer/fixture/manifest/tests will bind this frozen
post-QT design and the exact QT packet, enforce strict JSON/types/caps and
authenticate the inherited source/artifact/payload seals before use.
Normal/-O checks, both emissions, independent rational controls and
resealed mutations must pass. No finite check proves the analytic theorem
or an infinite native claim.

## 4. Completed inherited-data comparison

All390 source cells were processed, without new source evaluations:

| Radius ratio r/y | Cells | Old certified | Joint certified | Joint matched |
|---|---:|---:|---:|---:|
| 1/16 | 78 | 0 | 0 | 0 |
| 1/8 | 78 | 0 | 0 | 0 |
| 1/4 | 78 | 0 | 0 | 0 |
| 1/2 | 78 | 0 | 0 | 0 |
| 3/4 | 78 | 0 | 0 | 0 |
| Total | 390 | 0 | 0 | 0 |

These are26 nodes times5 ratios times3 tiers, not390 distinct physical
nodes. Each tier retains its original256,512 or1024-bit source provenance.
The least *sufficient-check* quotient E_upper/M_lower is at node19,
r/y=1/2, tier256. Exact integer comparisons give

    1637350 <= 1000000*E_upper/M_lower < 1637351.          (JR2)

This is a quotient of the chosen upper-error and lower-margin bounds,
NOT a measurement or lower bound for the actual remainder. No cell passes
JR1 with these inherited enclosures. A sharper M3, a different analytic
majorant, or another prescribed panel might change the outcome; none was
substituted here. No new companion root or quotient pole is claimed.

Every old status/reason and both old certificate booleans are retained,
together with an exact hash of the entire source attempt and jet tier.
All390 new statuses are NOT_CERTIFIED_INHERITED_BOUND. The full parent
rectangle containment comparison is nevertheless recorded for every cell;
it never by itself authorizes transport or nonvanishing inheritance.

The necessary tests belonging to the OLD QT criterion, and QR's separate
old-criterion obstruction, are untouched. Neither is silently promoted
to an obstruction to JR1. The theorem improvement and the exact polynomial
control remain valid independently of the zero-success native panel.

## 5. Exact arithmetic and source transport

All twenty-six real critical-point certificates are inherited from QT;
their residual-plus-quadratic-error versus derivative-margin inequalities
are also recomputed exactly. The three jet enclosures at each point cover
the whole inherited critical interval. Fractions reconstruct q and the
discriminant in the two equal forms

    lambda^2-2lambda*q = lambda^2+2a/c.

Their valid interval intersection is square-rooted outward on the fixed
512-bit dyadic grid using integer square root. The resulting d enclosure
is intersected with QT's authenticated d enclosure. For y, the dyadic
intersection of lambda-d and the original y enclosure is retained; the
stable identity y=2lambda*q/(lambda+d) supplies another consistency
intersection, but is not used to create unnecessary large non-dyadic
endpoints. The original radius enclosure is intersected with (r/y)*y.
Every retained enclosure remains conservative for the exact source value.
In particular, the stored upper endpoint of y+r must not exceed the
ORIGINAL M3 region radius. This guard succeeds in all390 cases; the
inherited M3 theorem is never applied on a larger disc.

Interval multiplication takes all four endpoint products. The joint
factor, error and model margin retain exact rational endpoints. JR1 uses
only E_upper<M_lower, with every prerequisite checked first. For a parent
rectangle centered at (x_H,eta_H) with coordinate radius epsilon_H, use

    sup|[x_H-epsilon_H,x_H+epsilon_H]-T|^2
      +sup|[eta_H-epsilon_H,eta_H+epsilon_H]-Y|^2
          < (lower endpoint of r)^2.                    (JR3)

This bounds every rectangle point against every admissible t,y,r. It is
strictly more than overlap or checking the parent center. Only a JR1 pass
AND JR3 would be labeled a matched parent root. Since there is no JR1
pass, this packet does not claim a new instance of that inheritance.

Arithmetic is MIXED: EXACT_RATIONAL/CERTIFIED_INTEGER_COVERAGE. The only
numerical interval rounding is the explicit outward dyadic square root.
JR2 is an exact pair of integer inequalities, not a rounded approximation
used in certification. The inherited directed-ball primitive values and
their runtime record are transported as source certificates; neither
FLINT nor QT's special-function producer is reexecuted by this module.

The producer authenticates38 distinct commit/path source versions by
Git blob identity and LF-normalized SHA256, recursively following the
frozen source manifests. It additionally checks QT's payload seal, all
four QT artifact seals, and its exact contract, runtime-provenance,
source-list and historical-ledger bindings. Source commits must actually
be Git commit objects; paths are canonical relative POSIX paths. The
new manifest must equal the literal source/contract declaration. The
new fixture seals its proof, producer, manifest and tests plus its own
canonical payload. No arbitrary prose dependency or executable historic
runtime closure is claimed by this traversal.

The hard bounds are24,000,000 JSON/source bytes,12,288 integer bits,
600,000 JSON nodes, depth28, container size30,000,100 source versions,
and exactly390 cells. Duplicate keys, floats/nonfinite numbers, boolean
integers in numeric fields, noncanonical rational pairs, source/payload
tampering, omitted/reordered outcomes and type drift fail closed, also
under Python -O. Guards use explicit exceptions, not assertions.

## 6. Literal frozen source bindings and verification scope

All five QT artifacts below have commit
530732c5fd7f50364381f8af50e97ce809b674c5. Paths are repository relative.

| Path | Git blob | LF SHA256 |
|---|---|---|
| research/exploratory/XI_QUADRATIC_CRITICAL_TRANSPORT.md | cb634e9ac1e5ddbdffad01286a0b37ca958ac92b | b9e7cf4911688d81c44ec9d871104e063c7bf46f574d86b479c6d912559d7269 |
| research/exploratory/xi_quadratic_critical_transport.py | a5e48dea3a25e1ff7419b2f6e2cfeef3de230185 | 28033a330ade30e0079f6e24cd0f4b07e9de9ba70438f92c88fe5c0f7fe8c373 |
| research/exploratory/xi_quadratic_critical_transport.json | 322281110f34af24575be29aed32acfd25657959 | 45e9d81f5cfe22662ad9e07b9a994796b3c3b18743ae74c8cbd3ce095f3a4cce |
| research/exploratory/xi_quadratic_critical_transport.sources.json | 58bd03b1d15ce4d2eb91addb4c209a0f43fab80c | 66aa6f3d483bc638eed43315592c3cc5f3f8ef2baa9d9518e2fa0de3e685d757 |
| tests/test_xi_quadratic_critical_transport.py | cde20699d7b3894bf40db419b2d90a3d93459751 | d5493e8c31d53d66fdb00f35dfa1198b173513e23b2bfd3bdcb2d39d80423749 |

The pre-comparison design is the present proof path at commit
99a7eb0310ca86392ef28b91b7c6d1fe81f35e61, blob
0b13e70ffef6610f9ae2a2dc484ac17ebb3294f3, LF SHA256
7f2c0270404fce9b627154c68464d5f96f58823f7644228e17fd1a1b8a92e1c9.
QT's transported payload SHA256 is
8f41ac9fe470c9f88d198b20a1935b2e8dfd5f4a32471e1251f05a4bee50a44b.

The test module independently expands the Taylor integral on monomials,
checks exact rational disc-factor examples, reconstructs the polynomial
control, tests interval/square-root/whole-rectangle arithmetic, and checks
complete panel coverage and exact comparisons. Twelve fully resealed
candidate mutations are rejected against a separately fresh reconstruction;
source/hash/path/type/cap and inherited-domain failures are also exercised.
These finite controls support the implementation and provenance. The
analytic proof above, not finite sampling, supplies the theorem.
