# L-102720 — Positive completion dominates the native SHARP quadratic disk

Claim ID: `L-102720`  
Status: **PROVED EXACT ALL-SCALE THEOREM**  
Created: 2026-08-22  
Depends on: PR #690 `L-100510`; PR #718 `L-102600`  
RH status: **not assumed**

Let \(\mathcal L\) be a finite labelled prime multiset.  The two copies of
\(67\) remain distinct labels.  Put

\[
r_\ell=p_\ell^{-1/2},
\qquad
U_\ell f(n)=f(p_\ell n),
\]

and define the native and positive-completion operators

\[
E_{\mathcal L}
=
\prod_{\ell\in\mathcal L}(I-r_\ell U_\ell),
\qquad
A_{\mathcal L}
=
\prod_{\ell\in\mathcal L}(I+r_\ell U_\ell).
\]

Their product is the squared source

\[
C_{\mathcal L}
=
A_{\mathcal L}E_{\mathcal L}
=
\prod_{\ell\in\mathcal L}(I-r_\ell^2U_\ell^2).
\]

For \(z=c+id\) in the exact active disk of PR #690,

\[
(3-c)^2+d^2
\le
(16-8\sqrt2)(3-c),
\]

put

\[
W_z(y)
=
|4\sqrt y-3+z|^2\mathbf 1_{y\ge1}.
\]

For any finite source \(\sigma\), write

\[
\mathcal Q_z[\sigma](X)
=
\sum_n
\frac{\sigma(n)}{\sqrt n}W_z(X/n).
\]

PR #690 proves

\[
\mathcal Q_z[E_{\mathcal L}\delta_1](Y)\ge0
\qquad(Y>0)
\]

coefficient-exactly for every labelled source state.

Expanding the positive completion gives

\[
A_{\mathcal L}-I
=
\sum_{\varnothing\ne S\subseteq\mathcal L}
r_S U_S,
\qquad
r_S=\prod_{\ell\in S}r_\ell.
\]

Hence

\[
\begin{aligned}
\mathcal Q_z[(C_{\mathcal L}-E_{\mathcal L})\delta_1](X)
&=
\sum_{\varnothing\ne S}
r_S
\mathcal Q_z[U_SE_{\mathcal L}\delta_1](X)\\
&=
\sum_{\varnothing\ne S}
r_S
\mathcal Q_z[E_{\mathcal L}\delta_1](X/p_S)
\ge0.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal Q_z[C_{\mathcal L}\delta_1](X)
\ge
\mathcal Q_z[E_{\mathcal L}\delta_1](X)
\qquad(X>0)
}
\tag{L-102720.1}
\]

throughout the complete shifted-quadratic disk.

Passing through the finite-horizon limit gives, for the duplicate-\(67\)
source \(\beta\) and its square lift \(\beta^\square\),

\[
\boxed{
\sum_n\frac{\beta^\square(n)-\beta(n)}{\sqrt n}
W_z(X/n)
\ge0.
}
\tag{L-102720.2}
\]

In particular the native-to-squared quadratic defect is nonnegative at
\(z=0\).

## Scope

This is a pointwise supercritical comparison.  It does not prove the
two-mode centered critical envelope of `L-102721`; subtracting the exact
\(X\)- and \(\sqrt X\)-modes is conclusion-bearing.
