# A bottleneck in the quasi-RH endpoint method

Status: **EXPLORATORY**; no new zero-free region is proved here.

Scope: This note identifies a specific possible target for improving a published proof route and an obstruction to retuning a particular set of parameters. The source claims have not been independently verified in this note.

Exact sources and dependencies:

- OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*, 30 September 2026, Lemma 17.6 and Proposition 19.2, available in [openai/math](https://github.com/openai/math); the PDF examined had SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`. That paper asserts a half-plane for finite-order Hecke L-functions over the Eisenstein field and transfers it to Dirichlet L-functions. Its large proof is an input here, not independently checked.
- [LW56e2/quasi-riemann-improved](https://github.com/LW56e2/quasi-riemann-improved), commit `b83dbbd914c5751acf9bc3389cde58970437278f`, especially `lean/Transport/TunedEndpoint.lean` and `lean/Transport/Endpoint.lean`. That source asserts a refined boundary and a Lean proof. We inspected its statements but did not build Lean or independently review its import closure.

## What limits this parameter screen

The refinement sets the proposed boundary to `7/8 - p/4`, with p = 214651/1250000000, giving 0.8749570698. Its `beyond_screenUpper_fails` statement uses two specified bin parameters and positive rational weights to show that, with the source's particular adaptive count and affine geometry, the pair of strict endpoint inequalities cannot both hold if

```
p >= 4562748652437347 / 26570739037370607802.
```

The source further asserts by exact arithmetic that its chosen boundary is less than 10^-12 above the corresponding screen limit. Thus this is a necessary obstruction to improvement **within that specific two-parameter endpoint screen**; it is not a general bound on any zero-free region or on other geometries, counts, and moments. It does not itself certify that the asserted refinement or the input theorem is correct.

## Concrete analytic target

The 5/6 slope in the count has a clear source. In OpenAI's Lemma 17.6, for sixth-power-free physical rows u with norm about U, a normalized inverse sum M_u of length D satisfies the asserted bound

```
sum_u |M_u(D)|^2  <<  max{U, U^(1/6) D^(5(1+c)/6)} (UD)^epsilon.
```

The proof amplifies with sixth powers: the map `(u,a) -> u a^6` is injective on the relevant rows, and the sextic character is unchanged away from the explicitly handled zero extensions. Taking H = max(2U,D^(1+c)) supplies about `(H/U)^(1/6)` amplifiers, leading to H divided by this number. For D = U^r, this yields exponent `max{1,(1+5r)/6}`. Proposition 19.2 converts it into a long-row count with the coefficient alpha = 5/6. Its balanced combination with the short-row count is the adaptive count used by the endpoint certificate.

A proposed route is a strictly stronger *uniform* inverse-witness second-moment or row-count estimate in the range actually used by the endpoint, with all moving rows, original zero extensions, character twists, profile seminorms, and height dependence preserved. A smaller amplifier power is not immediately valid: cubing generally does not preserve a sextic character, and dropping the zero extensions can destroy the identity. An estimate only for individual rows, a fixed conductor, or a subfamily of characters would not supply the required bound for the entire high expansion. Any proposed improvement must also redo the endpoint, slot supply, contour, and order-of-choice checks with the new estimate.

What was actually run: inspected the cited paper text and the two cited Lean files; no proof checker, independent numerical certificate, or new moment computation was run. The repository SHA and PDF hash above identify the examined sources.

Smallest remaining gap: prove a quantitative improvement over the source's *uniform* long-row count or its underlying moment in the load-bearing range, then verify that it is compatible with the same physical probe and all remaining estimates. This note supplies neither that estimate nor a new zero-free theorem.
