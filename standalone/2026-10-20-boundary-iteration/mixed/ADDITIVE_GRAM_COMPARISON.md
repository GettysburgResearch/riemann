# The sharp additive Gram bound is already in the current boundary

20 October 2026. Status: exact source comparison; no new boundary gain.

The uniform Gauss-sum moment of Xu--Sang,
[2610.17675v1, Lemma 4.1](https://arxiv.org/html/2610.17675v1), is
useful but does not improve the additive factor used in the current
Liu comparison. This matters because replacing an older elementary
bound by the sharp moment appears to save a positive power, but that
replacement has already been made in the inherited result.

Write the row norm scale as \(q=XY\), and the column norm scale as
\(L=Y\). With fixed exclusions, the Xu--Sang bound reads

\[
 \mathcal G(XY,Y)\ll(XY)^\epsilon
 \left\{X^{5/6}Y^{1/6}+X+X^{11/12}Y^{1/12}+Y/X\right\}.
 \tag{1}
\]

For \(Y\ge X\), the term \(X^{11/12}Y^{1/12}\) is at most
\(X^{5/6}Y^{1/6}\). Thus the three effective terms are
\(X\), \(X^{5/6}Y^{1/6}\), and \(Y/X\).

Liu [2610.26835v1, Lemma 13.2, (13.7)](https://arxiv.org/html/2610.26835v1)
already states, for the *actual additive factor* of the compensated
comparison,

\[
 \sum_{[k]\ne0}|\widetilde A_{[k]}|^2
 \ll (Q'/Y')\{1+P_a^{1/6}+P_a^2/Y'\}Z^\epsilon,
 \qquad Q'=X'Y',\quad P_a=Y'/X'.                     \tag{2}
\]

Equation (2) is exactly
\[
 X'+(X')^{5/6}(Y')^{1/6}+Y'/X'.                        \tag{3}
\]

The compensation is also already included. In Liu (13.4), for a
selected subset of total prime length \(d\),
\(X'=Z^{l_x-d}\) and \(Y'=Z^{l_y-d}\). The unselected prime
divisibility restrictions belong to the full theta index in
\(B_k^{(J)}\); they are not arbitrary moving coefficients in the
additive column sum. Its asymmetry \(b=l_y-l_x\) is unchanged.
Taking the square root of (3) contributes

\[
 Z^{(l_x-d)/2}
 Z^{\max(0,b/12,b-l_y/2+d/2)+\epsilon}.                \tag{4}
\]

At the empty subset \(d=0\), the last maximum is precisely
\(G=\max(0,b/12,b-l_y/2)\) in Liu Section 15.1 and in the inherited
completed low-side majorant. The source's full subset estimate retains
the further subset costs; substituting (1) gives the same three branches.

Comparing the main term to the older bound \(\mathcal G\ll Y\)
would save \(Z^{-5b/12}\) after taking square roots. Subtracting that
quantity from the *current* low-side exponent counts this saving twice.
Neither the asymptotic constant nor the smaller \(P_a^{1/12}\) error
removes the present \(P_a^{1/6}\) main term, which is generally positive.

Fixed finite-order column phases can be handled by refining the fixed
ray classes and using a finite Hilbert-space triangle inequality. The
Liu average (13.2) in fact specifies auxiliary ideal coefficient one,
so its target angular character is not inserted in this additive Gram.
The Xu--Sang statement itself is over the Eisenstein field; a new
all-field result could not be inferred from that citation alone. Here
the required all-field upper bound is already the native Liu estimate
(2), and the scope issue does not create a new improvement.
