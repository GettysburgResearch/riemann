# Signed affine cancellation for the weighted completions

**Status:** proposed source-qualified unconditional logarithmic results; not
independently reviewed, not an RH proof, and not pushed in this session.

This pass changes the mathematical input rather than calculating another
positive prime sector. It applies established logarithmically averaged binary
Elliott theory to complete signed correlations of the rational versions of
our native, coupled, two-channel and geometric coefficient families.

## Main result

For any two of those families, fixed power degrees and Dirichlet twists,
fixed finite masks, and fixed nonproportional affine forms L_1,L_2,

    sum_(n<=X) F_1(L_1(n)) conjugate(F_2(L_2(n)))/n=o(log X).

The convergence is uniform in arbitrary bounded powerful-prime profiles.
The actual coefficients can be unbounded: F_6(p^6)=-z_p p^2. They are NOT
fed directly into a theorem for one-bounded functions. The new adapter proves

    sum_(n<=X)|F(n)-F_R(n)|^2<=X/R

for the exact truncation of its unique powerful factor. Finite truncations
reduce by CRT to the bounded theorem, with the affine determinant preserved.
Cauchy pays the entire discarded correlation by O(log X/sqrt R).

## Complete signed consequences

Every fixed additive filter has the sharp mean-square asymptotic

    sum_(n<=X)|sum_j w_j F(n+h_j)|^2/n
             ~delta_F log X sum_j|w_j|^2.

Here the shifts are fixed and distinct, and delta_F is an explicit positive
Euler product. ALL cross terms are included; their opposite signs cancel.

For the unchanged critical Gaussian kernel, every fixed nonzero additive
lag contributes o(log D). Its entire fixed-band signed energy is therefore
asymptotic to the literal diagonal kappa_c delta_F log D. No Mellin-twist
average or random-prime replacement occurs.

## Attribution and boundaries

The difficult bounded cancellation is Tao's 2016 theorem, not a new proof
of Chowla. The contribution here is the unbounded-completion adapter and
its source-specific signed consequences. See THEOREMS.md and SOURCES.md.
These claims are relative to the inspected repository work; global priority
has not been established by an exhaustive literature review.

The same lifting proof transfers the recently released ordinary affine
Elliott result to ordinary averages, but that is a SEPARATELY LABELLED
external-source-dependent addendum. We did not rebuild that new formal
proof. The logarithmic theorem is independent of it.

These results concern F=Q, not aggregated Eisenstein norm coefficients.
The missing RH estimate needs quantitative cancellation jointly over lags
that grow with D. Fixed-lag little-o estimates cannot be summed over that
range without a new uniformity theorem.

## Replay

    python chks/check.py > /tmp/affine.json
    cmp /tmp/affine.json RESULTS.json
    python -O chks/check.py > /tmp/affine-O.json
    cmp /tmp/affine-O.json RESULTS.json
    python verify_manifest.py

The checker verifies finite arithmetic, masks, the exact CRT/source adapter
and positive tail budgets. It does not verify an asymptotic or the imported
analytic theorem. See VALIDATION.md and PUBLISHING.md for actual execution
and publication limitations.
