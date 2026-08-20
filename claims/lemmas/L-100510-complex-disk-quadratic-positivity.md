# L-100510 — The active shifted quadratic source is positive on an exact complex disk

Claim ID: `L-100510`  
Status: **PROVED EXACT ALL-SCALE THEOREM; ACTIVATION TYPING REPAIRED**  
Created: 2026-08-20  
Frozen parent: PR #676 at `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9`  
RH status: **not assumed**

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67).
\]

For `z=c+id`, define the **active** shifted carrier

\[
S_z(y)=(4\sqrt y-3+z)\mathbf1_{y\ge1}
\tag{L-100510.1}
\]

and

\[
Q_z(X)=
\sum_{n\le X}{\beta(n)\over\sqrt n}|4\sqrt{X/n}-3+z|^2.
\tag{L-100510.2}
\]

Equivalently, `Q_z=sum_n beta(n)n^-1/2 |S_z(X/n)|^2`.  The indicator applies to the entire shifted carrier.  The earlier notation `|T(X/n)+z|^2` placed `z` outside the activation indicator and would leave an infinite constant tail; that notation is withdrawn.

Put

\[
C=16-8\sqrt2=8(2-\sqrt2).
\]

Assume

\[
\boxed{(3-c)^2+d^2\le C(3-c).}
\tag{L-100510.3}
\]

This is the closed disk with center `4sqrt(2)-5`, radius `8-4sqrt(2)`, and real diameter `[8sqrt(2)-13,3]`.

## Prime-removal estimate

For one labelled prime `q`, removal is needed only when the selected child is active; then `Y>=q`.  Put `x=sqrt(Y)` and `a=3-c`.  Direct algebra gives

\[
\begin{aligned}
&|4x-3+z|^2-q|4x/\sqrt q-3+z|^2\\
&\qquad=(\sqrt q-1)
\left[8ax-(\sqrt q+1)(a^2+d^2)\right].
\end{aligned}
\tag{L-100510.4}
\]

Since `x>=sqrt(q)` and

\[
{8\sqrt q\over\sqrt q+1}
\ge16-8\sqrt2=C,
\]

condition (L-100510.3) makes (L-100510.4) nonnegative.  If the child is inactive its weight is zero and the removal inequality is immediate.  Hence removing a label costs at most `q^-3/2`.

The elementary labelled-prime estimate

\[
\sum_p p^{-3/2}+67^{-3/2}<0.967<1
\]

then gives, by adjacent-level pairing,

\[
\boxed{Q_z(X)\ge0\qquad(X\ge1)}
\tag{L-100510.5}
\]

throughout the disk (L-100510.3).

The theorem is Hermitian and coefficient-exact.  It supplies an active complex test-vector disk; it does not control the final critical variation by itself.
