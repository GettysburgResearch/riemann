# Report — conditional line frames reduce the final kernel to one one-sided moat

Agent: `gpt56-03-q`  
Issue: #205  
Stack: PR #204

## Main result

A first finite simple-critical-line block \(Z\) frames the complete complement
\(W\) and makes the selected-zero kernel a graph over the old radical packet:

\[
J_Z=
\begin{pmatrix}
I\\-B^{-1}A
\end{pmatrix}.
\]

A second simple-line block \(Y\) acts on this kernel through the exact
conditional Schur matrix

\[
S_{Y\mid Z}=C-DB^{-1}A.
\]

If the complete combined evaluation table is square, then

\[
\det V_{Z\cup Y}
=
(-1)^{\dim R\dim W}\det(B)\det(S_{Y\mid Z}).
\]

Thus finite line-zero capture of the whole packet is exactly equivalent to
invertibility of the two successive frames.

## One-sided kernel floor

The selected \(Y\)-zeros give the positive kernel Gram

\[
S_{Y\mid Z}^*M_YS_{Y\mid Z}
\succeq\sigma^2G_K.
\]

After subtracting this positive form from the exact Weil matrix, only the lower
endpoint of the residual matters:

\[
Q_{\rm rem}|_K\succeq-\omega G_K.
\]

If the positive-complement correction is bounded by

\[
Z_K^*C^{-1}Z_K\preceq\chi G_K,
\]

then

\[
S_K\succeq(\sigma^2-\omega-\chi)G_K.
\]

This replaces the absolute Möbius-tail target by one one-sided residual LMI.

## RKHS obstruction

Every exact global-radical extension tail has evaluation vector equal to the
negative conditional frame vector. If \(H_Y\) is the Hardy representer Gram,

\[
T^*G_\tau T
\succeq
S_{Y\mid Z}^*H_Y^{-1}S_{Y\mid Z}.
\]

Therefore no fixed finite kernel admits a uniformly vanishing exact radical
tail. A cofinal small-tail claim requires collapse of this conditional
interpolation floor.

## Exact controls

Main retained control:

```text
conditional evaluation        3/4
graph metric                  17/16
frame floor                   18/17
negative residual endpoint     9/85
Schur cross endpoint          49/3400
corrected floor             3191/3400
Hardy tail floor                6/17
```

Positive-residual control:

```text
residual restriction           100
negative endpoint                0
corrected floor             3551/3400
```

The second control proves that absolute tail size is not the correct lower-floor
quantity.

Eleven local tests pass. No remote CI result is claimed.

## Honest frontier

The remaining arithmetic statement is now

\[
\sup_{Z,Y}
\left[
\sigma_{Y\mid Z}^2-\omega_{Y\mid Z}-\chi_Z
\right]
\ge-o(1)
\]

cofinally, with every matrix and residual formed in one declared metric.

This is RH-bearing: a captured off-line Xi-cardinal difference forces a fixed
negative alternative. No RH proof is claimed.
