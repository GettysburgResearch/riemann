# Two terminal routes to the RH producer

This standalone packet contains the proofs of `L-100300--L-100312` and the
integration theorem `T-100300`.

## Route A

On every activation cell the critical quadratic envelope is

\[
E(y)=A+B y^{-1/2}+C y^{-1}.
\]

After \(t=\sqrt y\), its sign is the sign of one quadratic
\(At^2+Bt+C\). The complete negative logarithmic area is elementary:

\[
\int[-E(y)]_+\frac{dy}{y}
=
\sum_{(\alpha,\beta)}
\left[
-2A\log t+\frac{2B}{t}+\frac{C}{t^2}
\right]_\alpha^\beta.
\]

Summing these exact cell deficits gives a one-sided Mellin density. Subpower
growth is equivalent to RH.

## Route B

The additional notch

\[
K_1=(I-\sqrt2S_2)K_0
\]

creates the true moment

\[
\int_1^{16}K_1(y)y^{-3/2}dy=0.
\]

Euler--Maclaurin then gives complete-lattice decay \(Y^{-3/2}\). The exact
Vaughan identity

\[
\mu=2\mu_U-\mu_U*\mu_U*\mathbf1+a_U*a_U*\mu
\]

yields

\[
\mathcal W_1(X)=O(X^{-1/6})+\mathcal B_{X^{1/3}}(X).
\]

The first term is logarithmically integrable. The second is the unique balanced
compact trilinear. Subpower negative mass of this term is equivalent to RH.

No claim in this packet proves either terminal estimate.
