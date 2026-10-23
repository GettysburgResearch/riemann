# Source-bound review of the shifted Revers envelope

Status: reviewed analytic adapter and exact finite endpoint checks; not a
standalone global zero-free theorem.
Date: 2026-10-23.

Reviewed analytic source: `three-hour-root/REVERS_SHIFTED_ENVELOPE.md`,
SHA-256 `1f17190a8fff5d0b4c18ee2dfd926045a2812b1615e97fb00d19c1024eaa4e32`.
Endpoint checker: `three-hour-global/verify_revers_minimum_adapter.py`,
SHA-256 `f1653e05e21def5c0f9a2bf125ffd6fa54a2a3c654a071230274c3c5bd9a2a04`.
Both source files remain unchanged.

No unresolved defect was found in the stated adapter. The review checked
the source equation and its range, the entire shifted integral, the
minimum-zero normalization and the infinite-tail monotonicity. This
reviewer wrote the endpoint checker and contributed the observation that
the low range can use the published .618 bound; those aspects are
coauthor checks. The parent wrote the shifted-envelope proof. This is
neither human review nor a fresh proof of its external theorems.

## Source and analytic interfaces

Revers, arXiv:2602.05614v1, Section 3.5, equation (3.32), explicitly gives
the coefficients .469028, 3.99399 and -21.4623 for all t>=8.97*10^17.
The high-height bound remains a preprint import:
<https://arxiv.org/html/2602.05614v1#S3.E32>.
Dropping the negative constant is legitimate. No intermediate-range
computation from that preprint is imported here.

The global comparison with E(|y|) checks in all three ranges. In the
middle range, the published Hiary--Patel--Yang .618 bound and the exact
inequalities `log t0<42<log D`, `D/t0>2`, `(28/25)^6<2` give the claimed
comparison. At |y|<=3, Euler summation gives the bound below 6, including
y=0; the pole term's denominator has modulus at least 1/2. Above t0,
monotonicity of the shifted envelope suffices.

For j=log E the global derivative bound is valid. The reverse triangle
inequality controls `||t+u/pi|-t|` by `|u|/pi`, so the Lipschitz estimate
applies even where the shifted ordinate crosses zero. Integrating against
sech(u)^2 uses its exact mass 2 and absolute first moment 2log2.
This establishes the smoothing bound over the complete integration line,
not only a neighborhood of its high-height center.

At h>=70, `D exp(-h)<10^-12` and the derivative of
`h/6+log(.469028h+3.99399)` is less than 1. The retained `10^-10` buffer
strictly exceeds both the shift error and 1/D. All four Ford smoothing
centers lie in the valid range. Only corrected Ford Lemma 9.2's
intermediate J-bound is replaced; no final .675 or .685 bootstrap
constant is imported.

The resulting R2 follows from lambda=B/log(4t+1) with the same global
minimizing zero used in the logistic detector. Its right side increases
with B. The only new monotonic term has derivative with numerator
`ah/(ah+b)-log(ah+b)-10^-10`, which is negative for h>=70. Therefore a
strict endpoint gap excludes the whole infinite tail of possible
minimizing-zero heights.

## Replayed finite checks

On 2026-10-23 I ran the checker using the bundled Python with
`-I -S -B`, then `-I -S -B -O`. Both returned zero and produced identical
stdout. All decisions use Fraction; Decimal only formats output.
The log series has an explicit positive remainder. Nested arguments are
rounded outward before further rational evaluation. Every acceptance
check remains active under -O.

| Target R | Log-height cap | Certified positive gap lower bound |
|---|---|---|
| 4.7905 | 75.94 | 0.000004203156978714622065921582 |
| 4.791 | 75.9 | 0.0000001450699132452504644609072 |
| 4.79 | 75.97 | 0.000002739337334155789212005659 |
| 4.785 | 76.3 | 0.000003848060283011022770333253 |
| 4.78 | 76.7 | 0.00004153167995031015248177908 |

Three too-small endpoints were rejected as negative controls. The
checker also verifies the global-envelope comparison constants, the
smoothing error allowance and Ford's 1/160 zero-distance condition.

These checks establish only the finite arithmetic predicates and the
reviewed adapter implication. Each proposed R still requires a positive
logistic margin on its full complementary rectangle and a separately
reviewed complete assembly. Neither RH nor a fixed Hecke boundary is
proved here.
