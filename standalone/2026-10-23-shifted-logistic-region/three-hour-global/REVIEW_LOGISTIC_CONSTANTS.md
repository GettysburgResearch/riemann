# Independent review of the logistic real-axis constants

Reviewed note: ../three-hour-type/LOGISTIC_REAL_AXIS_CONSTANTS.md
SHA256: 9da9ad7051fcf3deb94db3d951051425c549313074d0ee5bd0dcfae3312c8139.
Reviewed checker: ../three-hour-type/verify_logistic_constants.py
SHA256: 50a2373d94a19406cb51c081958dab7772ec939e2d34f5033f58745735f689fb.
Reviewer: global-route agent, independently of the author.

No outstanding issue was found. The note and checker were read in full.
The interval operations preserve outward enclosures using exact rational
arithmetic. The trigonometric and arctangent remainders are alternating
tails in the stated ranges; the logarithm remainder has the required
geometric upper bound after reduction to [1,2]. Machin's formula and
the lower bound for Euler's constant have the correct signs. All
acceptance tests remain active under optimized Python.

The algebra leading to R1 is correct, and monotonicity of
u^2/(1-exp(-a*u)) reduces the full real interval to the stated worst
endpoint. The exponential bounds therefore prove the initial segment
inequality uniformly, not only at sample points. The remaining positive
tail is bounded with the exact rational value 3/1495000000000 times eta.

I recomputed the four derivative majorants directly from the elementary
formula for w. The linear-times-cosine term contributes exactly the
additional j/2 factor shown in the checker. The source coefficient
normalization is reconstructed rather than copied. The gamma constant
uses the value at sigma=1 as an upper bound and the lower enclosure for
Euler's constant in the direction needed for an upper bound on Carch.

Independent replay: ordinary Python and Python -O both passed all 22
checks and four negative controls; their complete stdout bytes were
identical. Informational floating-point decimal rendering occurs only
after acceptance and is not used in the decisions.

This is a finite constants review. It does not certify the remaining
uniform logistic-transform inequality or a global zero-free theorem,
and it is not a human mathematical review.
