# All-radius obstruction for the literal quadratic transport criterion

Status: POST-QT successor design, frozen before evaluating its new threshold
on any source point. The earlier QT five-ratio outcomes are already known
and are not re-labelled as a preregistration prediction.

Authoring/source base:
`530732c5fd7f50364381f8af50e97ce809b674c5`.
This packet will not modify that experiment or add any source point, height,
calibration, radius grid, gauge, or broad native evaluation.

## 1. Analytic theorem and precise conclusion

Use QT's literal hypotheses: real critical t of a real analytic g,
a=g(t), c=g''(t), a*c<0, lambda>0,
q=-a/(lambda*c)>0, 2q<lambda,
d=sqrt(lambda^2-2lambda*q)>0, y=lambda-d>0.

The quadratic sufficient criterion at an admissible radius
0<r<min(y,2d) requires

    M3/|c| < r(d-r/2)/[(y+r)^2((y+r)/6+lambda/2)],

where M3 bounds |g'''| on the complete required disc. In particular
M3>=|g'''(t)|.

Put

    B(lambda,d,y)=3d^2/[y(lambda+d)(3lambda+y)].

If |g'''(t)|/|c| >= B, NO admissible radius and NO valid M3 can satisfy
that particular sufficient criterion. This does not prove there is no
companion root or that no other transport theorem could locate it.

Proof. Since lambda=d+y, the function
F(r)=r(d-r/2)/(y+r)^2 has derivative
F'(r)=(dy-lambda*r)/(y+r)^3. Its maximum on the admissible interval is
d^2/[2y(lambda+d)], attained at r*=dy/lambda. Indeed r*<y and r*<d<2d.
The remaining denominator is strictly greater than lambda/2+y/6.
The full threshold is therefore strictly less than B for EVERY admissible
r. This proves the obstruction, including equality at B.

B is an explicit strict UPPER bound for the full threshold, not its exact
supremum. It is sharper than the simpler estimate d/(2lambda*y), since

    d/(2lambda*y)-B
      = d(5d+4y)/[2lambda(lambda+d)(3lambda+y)] > 0.

The derivative, maximum, admissibility, strictness and last identity were
independently checked before new source evaluation. This is elementary
algebra, not an external priority claim.

## 2. Fixed post-result finite panel

Use ALL26 certified real f6 critical-point intervals from the exact QT
fixture at the source SHA above, in its declared order, and NO others.
The parent used g=f5, so c=f7(t) and g'''(t)=f8(t). Keep lambda_(64)
fixed at its exact digamma calibration; the subscript is not its value.

Inherit the real critical-point existence/uniqueness certificate and complete
containing interval from QT as an accepted theorem dependency, subject to
its independent review. Do not claim to rerun QT's 19,968 outer-cover cells,
broad-task history or critical Newton searches.

Freshly evaluate the ACTUAL Xi coefficients through degree8 on EACH full
real critical interval using the pinned HA wrapper at exactly1024bits.
Use the full interval, never its midpoint, for f5,f7,f8; require f6's
enclosure to contain zero, opposite f5/f7 signs, and positive discriminant.
Evaluate lambda, d,y and B with outward balls. Compare a directed lower
bound of |f8(t)|/|f7(t)| with a directed upper bound of B.

All26 outcomes are retained as ALL_RADII_CRITERION_IMPOSSIBLE or UNRESOLVED.
A failed sign/domain/finite guard is UNRESOLVED, not a false theorem.
Report the coarse threshold too, to distinguish what the sharper algebra
adds. No success count is predicted.

An independently arranged exact Fraction/integersqrt interval calculation
will validate every accepted comparison from the fresh rational jet bounds.
This is a second finite comparison route, not a second special-function
implementation or a fresh proof of the inherited critical zero.

## 3. Resource, provenance and acceptance contract

Arithmetic is MIXED: directed FLINT balls, exact rational arithmetic and
complete finite coverage. Native runtime and executed HA/BC/OA helpers are
locked; all source Git/blob/LF identities, four artifacts and payload are
authenticated. Source inheritance and new calculations remain separate.

Caps:26nodes,1024bits,9coefficients,4096-bit rational endpoints,
24MB source bytes,2MB own report,10000work units. No adaptive precision,
alternate Newton seed, new radius search or larger-height survey occurs.

Required acceptance: full both-mode fresh replay, all26 coverage and exact
comparison controls, strict typing/resource failures, independently resealed
hostile reports, unchanged source artifacts, and independent theorem review.
The all-radius quantifier follows from the analytic maximization proof,
not finite sampling.

This theorem is unconditional about the literal local sufficient criterion.
It does not require raw companion innerness, prove actual innerness/RH,
or establish cofinal capture, native decoder identity or transport failure
for other methods.
