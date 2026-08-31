# Independent review of the original-kernel activation certificate

Reviewed freeze: `d1229b38ad83e791ff22032288b0a871735c9781`.
Reviewer: `/root/recent_landscape`, separate from the native author.
Conclusion: **no blocker found within the finite source-owned variational scope**.

I read the full proof, complete certificate producer, all 12 tests, and the
frozen kernel helper used by the certificate. A path-restricted Git diff
confirmed that the reviewed proof, producer, tests and artifact match the
freeze. Artifact identity and scope fields were inspected; I did not run the
certificate or independently recompute its interval endpoints. Exact blobs are:

| file | blob |
|---|---|
| `NATIVE_ACTIVATION_KERNEL_MINIMIZER.md` | `ccc9b690c646a2c7e93426ce01f7d8accbb851c7` |
| `native_activation_certificate.py` | `a0a6dfa09faba5386ad66207c0d583ebccf97fd9` |
| `native_activation_certificate.json` | `1d4d107af90b2407e9b62dd34a4cf553a2554624` |
| `tests/test_native_six_hour_activation_kernel.py` | `75df79f7d7093e3887c597e5ca15f2d8120448d4` |

Artifact schema: `riemann.native_six_hour.activation_certificate.v1`.
Proof object: `a8d5a7e794990563ec56ad9f6e84e2b5a450a411fdf63df1013f087f4df4dbb7`.

The source reduction retains all eight physical factor frequencies and the
original kernel. I checked the nine overlap integrals in the imported helper:
the constant/logarithmic, square-root and linear terms have the correct shift
factors under `y -> y/ratio^2`. The independent anchors at zero and `log(4)`,
support cutoff and symmetry agree with the stated normalization. The activation
field decomposes into its fixed even part and three odd fields; the even/odd
cross terms vanish, but the full off-diagonal odd Gram terms remain.

Positive definiteness follows from the original positive measure and linear
independence of the distinct physical exponentials. The interval determinant
and adjugate calculations then certify the constrained minimizer
`G^{-1}1/(1^T G^{-1}1)` and its interiority. The discovery-selected integer
powers are kept distinct from the later simpler `(4,3,3)` path. The latter's
strict improvement is an exact rational interval inequality, with the required
physical factor `1/K`; it is not a floating-point optimum. The separated
`(3,11,101)` control retains the predicted exactly uniform Gram and optimizer.

The source exponentials are genuine primewise schedules with the full chain
rule, preserving endpoints and signed Hankel current. The result does not
choose arbitrary independent arithmetic coefficients. It also explicitly does
not assert that one common schedule optimizes all overlapping tuples; that
requires the separate full-horizon problem.

The executable helper, original kernel source, geodesic source, preregistration
and discovery output are frozen and authenticated. Logarithms use rational
atanh remainders and an integer-square-root bracket encloses `sqrt(2)`.
Floating midpoints are display/discovery data only; all acceptance inequalities
use rational endpoints. Canonical typed JSON rejects Boolean/float mutations.

Root reports Ruff, ordinary write/check, optimized check, and **12 ordinary plus
12 optimized tests passed**. This reviewer ran none. The full retained gamma
decoder and full moment estimate remain unproved. A source normalization error
or loss of the actual off-diagonal Gram terms would invalidate the conclusion;
agreement with a diagonal surrogate would not rescue it.
