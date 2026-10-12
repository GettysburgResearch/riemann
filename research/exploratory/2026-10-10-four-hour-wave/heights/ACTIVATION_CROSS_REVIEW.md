# Independent review of the prime activation envelope packet

Status: analytic, implementation, and complete independent source-replay
review **ACCEPT**. Normal and optimized replays are byte-identical to each
other and to both retained owner receipts. This review is frozen.

The reviewed statement is the component theorem in
[ACTIVATION_ENVELOPES.md](../arithmetic/ACTIVATION_ENVELOPES.md):
`H_m(x)>0` for every real `m>=9/7` and `x>=1`, with literal beta, the native
activation kernel, and the two distinct label indices at 67. The prior
reviewed exclusion/weighted/four-label packets are explicit inputs. Critical
power one and RH remain open.

## Analytic and code audit

| Contract | Independent finding |
|---|---|
| P-A1--P-A2 | For an active omitted prime `q>C_i`, its positive numerator is bounded above by the numerator at `C_i`. Inactivity contributes zero. Every representative numerator is positive over the required `x>=N`, including representatives greater than the current endpoint. The continued function is a positive majorant. |
| P-A3 | The finite ordinary-prime bins exactly partition `(N/2,3N/2]`; the final mass is the complete augmented prime-zeta sum minus the selected single-label mass and those bins. Both copies of67 are already selected, so the residual is precisely the ordinary-prime tail. Positivity and directed upper endpoints are guarded. |
| P-A4--P-A5 | For `1<m<2`, the generalized binomial coefficients after degree one are positive and decrease; the recurrence in `kernel_upper` has the correct index and sign. The omitted degrees32 and higher are bounded by the degree32 coefficient times `v^32/(1-vmax)`. The kernel domain guard encloses every representative's actual activation range. |
| P-A6 | Each bin mass upper multiplies a positive polynomial upper kernel. The selected numerator is also an upper bound. Consequently the collected `Q_A` bounds the entire one-label source, including its infinite tail. Interval coefficient arithmetic encloses the chosen polynomial; strict Bernstein positivity concerns every whole coefficient ball. |
| P-A7 | The negative one-label term uses the lower-power upper numerator and lower normalization denominator. Positive even/marked levels use upper-power lower numerators and an upper normalization denominator. All removal coefficients are positive because the complete `V` upper is less than3. After multiplication by the two positive denominators, lowering the positive leading denominator product gives exactly the implemented polynomial. |
| Complete real coverage | Nine consecutive exact rational slabs cover `[9/7,1.3]`; each includes all21 closed endpoint rectangles covering `[1,N]` and an entire tail `[N,infinity)`. The prior accepted exclusion theorem covers `m>=1.3`. No finite endpoint scan is promoted to a tail theorem. |
| Bernstein acceptance | The outward forty-bit dyadic cap contains `N^-1/2`; any subdivision retains both children, and exact dyadic midpoints preserve coverage. Acceptance requires every entire Bernstein coefficient ball to be strictly positive. Depth or leaf exhaustion raises an explicit error. |

The implementation review included `activation_tail.py`,
`verify_activation_stitch.py`, and `test_activation_tail.py`, plus the
dependency interfaces in `verify_exclusion_stitch.py`, `exclusion_tail.py`,
`exclusion_moments.py`, `polynomial_tail.py`, `weighted_moments.py`,
`verify_four_label.py`, `verify_weighted_stitch.py`, and
`verify_horizon_stitch.py`. The finite prefix recursion preserves increasing
label indices, exact integer quotient cutoffs, and marked used-label sums.
The Möbius log-zeta tail remains a directed enclosure of the complete
convergent prime source; its remainder uses `log(zeta(s))<=zeta(s)-1` and a
geometric bound beyond index80.

## Independent execution scope

`test_activation_tail.py` passes all four controls in normal and optimized
Python. Those controls compare the representative polynomial against the
literal kernel, independently sum finite bins at256bits, account for the
full Euler residual, cover inactive representatives, and reject invalid
domains. `test_exclusion_moments.py` also passes its four control groups in
both modes, preserving the inherited marked-removal contracts.

The independent full replay commands use the pinned cloud virtual environment
and the unchanged arithmetic sources:

```
python -B arithmetic/verify_activation_stitch.py --progress --output heights/activation_audit_normal.json
python -B -O arithmetic/verify_activation_stitch.py --progress --output heights/activation_audit_optimized.json
```

Paths in this display are relative to the four-hour-wave directory. All four
complete receipts share SHA-256
`77d274d15270bb281d0d7c41d2a088ed4d34e538779c896c298aa3db5659036d`.
The independent runs certify all189 bounded rectangles and all9 whole
unbounded tails. [activation_cross_review.json](activation_cross_review.json)
binds source and dependency hashes, exact scope, and the independent control
counts. The analytic lemmas remain human/agent-reviewed mathematics; Arb
receipts are directed finite certificates for those contracts.
