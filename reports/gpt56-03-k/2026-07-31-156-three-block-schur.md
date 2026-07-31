# Session report — exact triangular solution of the finite three-block floor

Agent: `gpt56-03-k`  
Date: 2026-07-31  
Base: PR #159  
Classification: exact finite theorem and checker; cofinal zeta rates remain open

## Result

For

\[
\mathcal H=
\begin{pmatrix}
B_R&X^*&Y^*\\
X&B_V&Z^*\\
Y&Z&C
\end{pmatrix},
\]

the correct proof order is:

1. eliminate `C`;
2. certify the resulting visible Schur block;
3. eliminate the visible block;
4. charge the radical row once.

The exact corrected cross is

\[
\widetilde X=X-h^{-1}Z^*M^{-1}Y,
\]

and the complete radical loss is

\[
K_R=h^{-1}Y^*M^{-1}Y
+\beta^{-1}\widetilde X^*G_V^{-1}\widetilde X.
\]

If

```text
B_R >= -e G_R
C >= h M
B_V-h^-1 Z* M^-1 Z >= beta G_V
K_R <= kappa G_R
```

then

```text
lambda_min(H,diag(G_R,G_V,M)) >= -(e+kappa).
```

A complete assembly radius adds linearly.

## Main improvement

The visible-complement cross `Z` is not an independent error and need not tend
to zero. It is absorbed in the visible Schur floor. Moreover the direct
radical-visible channel `X` can cancel the indirect path through `E` exactly.
The old decomposition loses that cancellation.

For an exact global-radical truncation, `(X,Y)` is one tail functional. `K_R` is
its squared dual norm in the triangular positive metric on `V+E`. This is the
right analytic object for a uniform Gaussian tail estimate.

## Cofinal implication

At support `lambda`, put

```text
epsilon_lambda=e_lambda+kappa_lambda+delta_lambda.
```

If all three terms tend to zero, the cofinal localized-Weil lower-envelope
theorem proves RH. A Gaussian packet bound beats every sub-Gaussian metric and
inverse-floor loss.

## Exact finite replay

`X-15304` has one strict cancellation control and nine passing adversarial tests.

```text
proof-object SHA  83553370cdf517e38ac7d186286cebd7ef61f011d26dcfb4f072f20e2d3554b8
verification SHA  ef8e96b8a88eda00549c5514fa89bee4cf432f8f2e8deb94f5c8747d27db858d
final floor        -17/1250
```

## Honest frontier

The finite three-block algebra is closed. The remaining zeta-specific tasks are:

1. source-bound positive visible Schur floors;
2. a uniform growing-packet tail-functional estimate in the triangular metric;
3. a vanishing complete assembly radius.

No production cofinal sequence and no proof of RH are claimed.
