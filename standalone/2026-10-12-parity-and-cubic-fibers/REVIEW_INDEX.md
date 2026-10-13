# Exact-source review index

Status: three scoped nonauthor automated-agent reviews, each reporting PASS with no substantive blocker. This index records their coverage; it is not an additional proof or an integration verdict.

All verdicts refer to **GettysburgResearch/riemann commit `c07b9f653b8d0eb82d9f056d935a4ecef6770f56`**, directory `standalone/2026-10-12-parity-and-cubic-fibers/`. The full intended source was published before the review requests. The review receipts were appended afterward without changing the mathematical source.

## Proof coverage and replays

| Nonauthor reviewer | Proof/document scope | Independently executed checker | Receipt |
|---|---|---|---|
| amplification agent | ARITHMETIC_PARITY_OBSTRUCTION.md and PARITY_DAMPED_MOMENTS.md; exact masks, smaller scales, PW/NM2 distinction, endpoints, and return to the native moment | verify_parity_damping.py, ordinary and optimized Python; 44,091 explicit guards in each run | [Arithmetic and damping review](reviews/arithmetic_and_damping_review.md) |
| theta_closure agent | CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md in full; PARITY_DAMPED_MOMENTS.md Sections 7–9 and their supporting definitions | verify_cubic_fibers.py, ordinary and optimized Python; 38,577 explicit predicates in each run | [Cubic fibers and norm-envelope review](reviews/cubic_fibers_and_norm_envelope_review.md) |
| moment_obstructions agent | BESSEL_CHANNELS_AND_LEAKAGE.md and its checker in full; CUBIC_FIBERS_AND_RIESZ_PRODUCTS.md Sections 6–7 and required definitions/prime-count lemma; README consistency and scope | verify_bessel_channels.py, ordinary and optimized Python; 11,562 explicit predicates in each run | [Bessel and calibration review](reviews/bessel_and_calibration_review.md) |

Each reviewer fetched the relevant files from GitHub at the immutable source commit, recomputed their SHA-256 and Git blob identities, read the named proof scope, and recorded the commands actually run. The coordinator also read all four proof drafts and checker sources, executed all six ordinary/optimized packet commands, and verified the full published source. The nonauthor receipts above distinguish their work from that coordinator check and from the original authors' replays.

Each independent replay pair was byte-identical to its committed normal result:

| Result | SHA-256 |
|---|---|
| results/parity_damping.json | `2d11b779c54f6710a5a3a439fd3f9493d955b44602b482d307ecf2d38e3c7253` |
| results/cubic_fibers.json | `68c4c47d5c1389ec2c63f6546b01ede6a9e25d6b161b996913a3a837c34df64e` |
| results/bessel_channels.json | `db88a9ab641e11c13686f4aac00339906ce23e2965a36ee4e99e7a6abd9cd943` |

The total is 94,230 finite predicates per ordinary/optimized set. These include setup and domain checks. Repeating the same predicates does not enlarge the finite coverage or prove an infinite analytic estimate.

## Limits of the verdicts

The notes' conditional, finite, and cofinal boundaries remain unchanged. In particular:

- The pointwise premise with exponent 7/8 has not been independently established by this packet. The noise floor at positive damping is not asserted at zero damping.
- The prime-face and deformed-coefficient lower bounds are not lower bounds for the original complete Möbius moment.
- The norm-envelope model is an obstruction to the specified norm-only inference, not an arithmetic counterexample.
- Complete residue identities do not supply a short-row average. The optimal linear comparison is not claimed optimal on the native positive moment cone.
- Finite Bessel compression is not physical covariance, and its exact complementary counterterms have not been produced from the native arithmetic coefficients.
- No review proves the undamped cofinal generalized moment, improves a zero-free boundary, establishes RH, or promotes the packet into main.

The exact analytic target still missing is README equation (5.1): a bound with cofinal sublinear losses for the complete native moment below the proved damping threshold, with the fixed detector, row range, and twist coverage retained.
