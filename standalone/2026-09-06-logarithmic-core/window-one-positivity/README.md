# Full-source length-one positivity

**PROPOSED COMPUTER-ASSISTED THEOREM. RH remains unproved. Independent mathematical
and code review is required.**

This continuation of PR #803 supplies an actual sign, not just an approximation
or a new equivalent endpoint. For the exact #792 arithmetic kernel W and every
nonzero complex L2 test supported in any interval of length at most one,

    Q(h) > 0.

There are no mean-zero, endpoint-moment, finite-basis, or sampling restrictions.
All prime powers remain present through the exact safe source P2 and the
activated n=2 cusp. A quantitative periodic H^-1 lower bound is proved.

The construction is a sum of nonnegative cosine atoms plus a 4-periodic remainder
with strictly positive Fourier coefficients. It agrees with the actual source
on [-1,1]. A 192-bit outward dyadic checker proves all 2049 initial coefficient
inequalities; 256 spline phase classes and an analytic tail prove every remaining
coefficient. An optimizer and numerical zero reconnaissance suggested rational
parameters but are absent from acceptance. Frequencies are not claimed to be zeros.

The full effective matrix, including its coupling to the infinite positive
sector, satisfies the explicit inequality

    S_1 >= 3*2^-35 G H^(-1) G >0,

where G is the ordinary Gram of the parent's104 elementary exceptional functions,
and H is the H1 Gram of their explicitly tapered periodic extensions.
This is not an L2 gap for the original compact operator and is not merely the
positivity of its leading104-dimensional compression.

Read PROOF.md for the all-functions/infinite-frequency argument. The finite
witness is certificate.json. Primitives are reconstructed by intervals.py;
verify.py evaluates the exact formulas and infinite tail. result.json is a
reconstructed receipt, never a replacement for running the checker.

    python -B verify.py --check result.json
    python -B -O verify.py --check result.json
    python -B test_checks.py
    python -B -O test_checks.py
    python -B test_rejections.py
    python -B validate.py

The positive extension is not W outside[-1,1]. Constant-window translation does
not increase support diameter. Unbounded-length positivity is still open. No
external novelty, larger-window record, exact-SHA independent acceptance, or
formal build is claimed. See SOURCES.md and VALIDATION.md.
