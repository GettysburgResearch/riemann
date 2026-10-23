# Global wrapper for the strengthened logistic detector

Status: proposed source-dependent improvement of the classical logarithmic
zero-free constant to R=4.82. This extends the separately frozen R=4.84
argument. It does not assert RH or improve the separate fixed-width Hecke
boundary. Human mathematical review has not been obtained.

Baseline analytic/global wrapper: LOGISTIC_GLOBAL_WRAPPER.md,
SHA256 acb4b29ef72c031eb78ec27f41c8f4169e648f554a35badc559472077a8b36cb.
The explicit formula, source kernel, trigonometric polynomial, zero-count
tail and imported finite-height/Littlewood inputs are exactly as there.

The two new inequalities are:

1. ../three-hour-type/LOGISTIC_NEGATIVE_ARCHIMEDEAN.md,
   SHA256 88d8dba1316e61aa3cd67e2bb81a2c04d1ac114985593ecde9082aeae766182f,
   proves E_f(sigma)<=-.31 eta for eta<=.0075 and sigma>=.99.
2. ../three-hour-boundary/LOGISTIC_TWO_PRIME_GAIN.md,
   SHA256 fd4773be0ce4d54ac8ec845c1cb3904a01224008660460973d7056066bde1405,
   proves that the nonnegative arithmetic detector sum is at least
   1.1447 eta-2775 eta^3 in the same parameter range.

Both are uniform analytic inequalities supported by exact rational
constant/polynomial certificates. They are not evaluations at a numerical
minimizer. Their respective reviews are separate packet components.

## 1. Sufficient finite inequality

Use the baseline notation and let

    Astar=50/241=1/4.82,
    Lstar=exp(21.233*Astar)<82.

For 0<A<=Astar and log H<=l<=Lstar, the exact sufficient margin is

    a1[F(sigma-1+eta)+F(sigma-eta)]-F(sigma-1)
      -eta*w0/2*[a*l/2-3.0126]-10^(-7)
      +1.4547 eta-2775 eta^3.                           (P-M)

The positive linear increment is 1.1447+.31. The first part comes
from the arithmetic lower bound; the second comes from the negative
zero-frequency archimedean correction. The cubic prime-side error
has the unfavorable sign. These contributions do not overlap and
are not counted twice.

The root's certify_logistic_prime_extension.py certifies a lower bound
for (P-M), using the same three-transform lower reduction as the
baseline, on the larger closed rectangle

    0<=A<=50/241,       28<=l<=82.

Its initial directed-interval certificate has 44 closed boxes and a
strict minimum lower bound greater than .000004069. A separate exact
Fraction implementation certifies 70 closed boxes, with minimum lower
bound greater than .00001007882. Its source is
../three-hour-type/verify_logistic_prime_extension_fraction.py,
SHA256 b2c09c2b4c9af34a2e460bb4bbec6360044d798892ad3471cd0e18c5c40db425,
and its certificate LOGISTIC_PRIME_FRACTION_CERTIFICATE.json has SHA256
fb6f0752051047df05c42ec6ebedc0ee36c11f3e1a92fcc46c0916baa6ff92cf.
The independent scalar and component reviews remain distinct from this
global analytic composition. The A=0
face is again the continuous extension of the sufficient scalar
expression; the physical detector is used only for A>0.

The enlarged rectangle still satisfies eta<.0075, sigma>.99,
alpha>.98, A<.21 and l>=28. Every bound in the baseline's explicit
gamma, pole, high-frequency E and distant-zero budget therefore
continues to hold. The negative E0 estimate replaces its earlier tiny
positive upper bound; retaining the full 10^(-7) remainder budget is
conservative.

## 2. Global inference

Suppose a nontrivial zero violates

    Re s > 1-1/(4.82 log|Im s|),       |Im s|>=3.       (P-G)

The finite RH verification confines it to |Im s|>H. The published
Littlewood region with coefficient 21.233 confines it below
Tstar=exp(Lstar). Choose a zero minimizing
B=(1-beta)log|gamma| in that finite range. The strict critical strip
gives 0<B<Astar, and the large-height input ensures that this is also
a valid global minimum for all zeros above H.

At the minimizing zero use eta=B/log t and
sigma=1-B/log(Kt+T0), exactly as in the baseline. The pairing,
multiplicity treatment and distant-zero estimates are unchanged.
The explicit formula and its quantitative error budget now yield
the necessary upper bound

    a1[F(sigma-1+eta)+F(sigma-eta)]-F(sigma-1)
      <=eta*w0/2*[a*l/2-3.0126]+10^(-7)
          -1.4547 eta+2775 eta^3.

This contradicts the certified strict positivity of (P-M).
The finite verification handles heights 3 through H, and conjugation
handles negative heights. Thus (P-G) follows from the stated imported
theorems and the independently reviewed analytic/finite certificates.

This composition does not require a numerical zero-free baseline or
an infinitesimal iteration. Its new content is the admissible exact
logistic detector together with the signed archimedean and two-prime
improvements. It is a proposed proof for further mathematical review,
not a claim that a finite program alone proves an infinite theorem.
