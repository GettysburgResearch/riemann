# Report — conditional line frames reduce the final kernel to one joint moat

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

## Sharp one-sided kernel floor

The selected \(Y\)-zeros give the positive kernel Gram

\[
P_Y=S_{Y\mid Z}^*M_YS_{Y\mid Z}
\succeq\sigma^2G_K.
\]

After subtracting this positive form, let \(R_Y\) be the complete signed Weil
residual. Assemble the entire already-positive visible-plus-ambient sector as
\(C_+\succ0\), with complete kernel cross \(L_K\). The fully corrected residual
is

\[
\mathcal R_{Y\mid Z}^{\rm corr}
=
R_Y-L_K^*C_+^{-1}L_K.
\]

If

\[
\mathcal R_{Y\mid Z}^{\rm corr}
\succeq-\nu G_K,
\]

then exactly

\[
S_K\succeq(\sigma^2-\nu)G_K.
\]

This is sharper than separately proving

\[
R_Y\succeq-\omega G_K,
\qquad
L_K^*C_+^{-1}L_K\preceq\chi G_K,
\]

which gives only \(\nu\le\omega+\chi\). Positive omitted-zero mass may pay the
Schur correction.

The exact one-dimensional separation

\[
P_Y=1,
\quad
R_Y=9/10,
\quad
L_K^*C_+^{-1}L_K=1
\]

has exact floor \(9/10\). The separated estimate gives only zero, while the
joint residual gives the strict floor \(9/10\).

## Full-block metric correction

The full positive sector must be eliminated before the kernel result is promoted.
Completing the square gives a triangular metric

\[
G_\triangle
=\mathcal L^*\operatorname{diag}(G_K,G_+)\mathcal L.
\]

If

\[
S_K\succeq-\varepsilon G_K
\]

and

\[
G_\triangle\preceq\Lambda G_{\rm full},
\]

then, after assembly radius \(\delta\),

\[
\lambda_{\min}(A,G_{\rm full})
\ge-\Lambda\varepsilon-\delta.
\]

The valid cofinal schedule is therefore

\[
\Lambda_j\varepsilon_j+\delta_j\to0.
\]

This corrects an earlier draft composition that took a minimum of separate
kernel and visible restrictions.

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
quantity. The joint-residual strict-separation example is proved algebraically
in `L-20504`.

Eleven local tests pass. No remote CI result is claimed.

## Honest frontier

Define

\[
\mathfrak J_j
=
\sup_{Z,Y}
\left[
\sigma_{Y\mid Z,j}^2
-\nu_{Y\mid Z,j}
\right],
\]

where \(\nu\) is a directed negative endpoint for the complete joint corrected
residual. The remaining sufficient arithmetic statement is

\[
\boxed{
\Lambda_j(-\mathfrak J_j)_+
+
\delta_j
\longrightarrow0.
}
\]

This is RH-bearing: a captured off-line Xi-cardinal difference forces a fixed
negative alternative. No RH proof is claimed.
