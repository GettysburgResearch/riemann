# Joint Taylor remainder for the fixed Xi quadratic transport panel

Status: POST-QT theorem/design, frozen before any new criterion comparison.
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
