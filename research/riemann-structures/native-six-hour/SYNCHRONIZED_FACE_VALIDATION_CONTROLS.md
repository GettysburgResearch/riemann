# Retained root-isolation validation refusal

The actual source discovery frozen at
`bff003bc35b10c83fc1afa02533aec9dd478bb23` is unchanged. Its original
upper-boundary cubic has no interior roots, its endpoint values are
certifiably positive, and its source-face minimizing path is `(D,E)=(0,0)`.

The first final-certificate run replayed that discovery successfully,
then refused a separate synthetic cubic with roots `1/4,1/2,3/4`.
The interval Sturm evaluator could not certify a sign at a subdivision
point in this symmetric dyadic control. The frozen helper deliberately
refuses such an enclosure; no claim of a universal root isolator is made.
Neither the helper nor the discovery data was modified to force a result.

The final certificate retains and reproduces this exact refusal. Its
successful independent controls are the asymmetric cubic with roots
`1/5,1/3,4/5`, the quadratic with roots `1/3,2/5`,
the linear polynomial with root `1/3`, and `1+x^2` with no real roots.
The cubic's derivative roots are irrational and its linear Sturm member
has root `20/67`; the quadratic's derivative root `11/30` is also
non-dyadic. All success
controls use the same frozen evaluator, fixed node/depth limits and
outward arithmetic. A separate repeated-root control still requires a
refusal. These post-discovery validation controls do not change the
registered source candidate class or the actual minimizing result.

Validation: the coordinator reports Ruff, producer write/check and
optimized check, and all12 dedicated tests in both ordinary and
optimized modes passed after this repair. Final note binding is
replayed before the certificate freeze. The author did not run these
jobs; independent reviewers read the proof, scout and final controls.
