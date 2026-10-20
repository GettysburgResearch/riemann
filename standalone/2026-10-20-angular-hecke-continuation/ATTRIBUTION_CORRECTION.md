# Correction to the attribution in PR #1009

Date: 20 October 2026.

The previous packet correctly computes the principal factor in Liu's
all-field notation, but its comparison with earlier repository work
was incomplete. The earlier Eisenstein-field principal factorization
was already present in PR #1006.

The exact earlier source is:

- PR: https://github.com/GettysburgResearch/riemann/pull/1006
- Commit: 0c838d130f275efb6e8ddb81dab42462b4ce9454
- File: standalone/2026-10-18-three-direction-sprint/eisenstein/MIXED_CONSUMER.md
- Git blob: dd2ca1c6ef1922efe06e27b882966a968def850d
- Locator: Section 4, “Target and tail interfaces.”

That file already displays

\[
 H_{\mathfrak p}(s)=
 \frac{(1-q^{-2})
    [1-(1-q^{-1})q^{-s}-\kappa(\mathfrak p)q^{2-6s}]}
 {(1-\kappa(\mathfrak p)q^{3-6s})(1-q^{-s})},
 \qquad \kappa(\mathfrak p)=\overline\alpha(\mathfrak p)^6,
 \tag{1}
\]

and proves normal convergence and nonvanishing of the residual
product on \(\operatorname{Re}s>1/2\) after extracting
\(L_E^S(6s-3,\kappa)\). It also gives the Euler-product protection
region \(\operatorname{Re}s>2/3\).

The principal-factor note in PR #1009 at the frozen commit
e2bd86d1d062ac1dc4140d52331797b81d7d825d extends the calculation to
Liu's general-field and general-target notation, keeps the target's
sixth power, and derives an exact Mellin convolution. Its underlying
factorization and the \(2/3\) protection mechanism should not have
been presented without crediting the directly relevant #1006
calculation. The comparison with the different resonance in #975
did not replace that attribution.

This correction preserves both frozen source identities. It changes
the attribution, not the local identity or the normal-convergence
argument.

The analytic advance proposed in the present continuation is
different: it proves the required angular inverse and product
moment adapters and uses them to bound the zeros of the extracted
infinite-order function. The resulting stronger principal
protection is a consequence of that new analytic input, while
the factorization itself is explicitly inherited.
