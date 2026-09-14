# Primal Cauchy transport frontier

The T-106620 shallow gate is an exact canonical-correlation defect between the
shallow denominator companion model space and the numerator companion model
space. T-106630 converts that spectral statement into a constructive primal
certificate.

For synthesis maps `E_-`, `E_+`, Grams `G_-`, `G_+`, and cross Gram `C`, every
matrix `X` gives the rigorous cost

\[
R(X)=tr[G_-^{-1}(G_- -CX-X^*C^*+X^*G_+X)].
\]

Its minimum is the exact adverse defect, attained at
`X=G_+^{-1}C^*`. The error of any approximate transport is a second positive
quadratic form in its normal-equation residual. A selected numerator
subfactor is sufficient; additional numerator directions only help.

For one pole pair, the optimal cost is the squared upper-half-plane
pseudohyperbolic distance. For clustered divisors those costs cannot be added
raw: a two-column counterexample has pairwise error tending to zero while the
model-space defect stays one. The generalized whitening is load-bearing.

The live gate `MESOTRANS106630` asks for explicit transport matrices for the
mesoscopic zeta-derivative cross-ratios with total generalized residual below
`11/500 N`. This is exactly sufficient for more than ninety percent, but is
not proved.
