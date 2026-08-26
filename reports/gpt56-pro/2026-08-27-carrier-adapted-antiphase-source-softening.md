# Carrier-adapted fifth antiphase source softening

The full T-106670 free energy is lossless but contains the endpoint index as a
forced unit spectrum. T-106700 therefore correctly rejects any closure based
only on positivity, pole height or solving the Cauchy normal equations.

The new calculation attacks the Xi-specific part rather than the abstract
transport algebra. For an odd endpoint, the Fourier density of

\[
A_{K,\lambda}=FF^{(K)}+\lambda^2F'F^{(K+1)}
\]

splits into an exact carrier-mismatch term and a positive spread term. At the
frequency-adapted scale `lambda_xi=2/xi`, the mismatch vanishes and

\[
0\le a_{K,\lambda_\xi}(\xi)\le K L_K(\xi)/\xi.
\]

For the explicit Xi kernel and K=5, the conditional concentration theorem of
L-106502 sharpens this to

\[
a_{5,2/\xi}/[(2/\xi)L_5]
=1/10+O(e^{-\xi}/\xi^2).
\]

This exact `1/10` carrier phase is not present in the structural countermodel
`c+cos(nt)`, whose topological defect is driven by a zero-mode/carrier
interaction and fails Xi conditional concentration.

The missing theorem is now a physical transfer: carry this frequency-adaptive
law through the constant mesoscopic companion scale, the common outer factor,
and the forced endpoint index in the source-Pick metric. The packet does not
claim that transfer or the resulting 90% conclusion.
