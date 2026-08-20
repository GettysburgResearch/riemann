# L-100510 — The shifted quadratic source is positive on an exact complex disk

Claim ID: `L-100510`
Status: **PROVED EXACT ALL-SCALE THEOREM**
Created: 2026-08-20
Frozen parent: PR #676 at `9849df6a52bb4791ebf10cf0dd9f0c929d36bdd9`
RH status: **not assumed**

Let

\[
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For \(z=c+id\), define

\[
Q_z(X)
=
\sum_{n\ge1}
\frac{\beta(n)}{\sqrt n}
|T(X/n)+z|^2.
\tag{L-100510.1}
\]

Represent \(\beta\) by one labelled copy of each prime and one additional
labelled copy of \(67\).  Put

\[
C=16-8\sqrt2=8(2-\sqrt2).
\]

Assume

\[
\boxed{
(3-c)^2+d^2
\le
C(3-c).
}
\tag{L-100510.2}
\]

Equivalently, \(z\) belongs to the closed disk with center

\[
c_0=4\sqrt2-5
\]

and radius

\[
R_0=8-4\sqrt2.
\]

Its real diameter is

\[
[\,8\sqrt2-13,\ 3\,],
\]

which strictly contains the real interval \([-1,3]\) from PR #673.

## Prime-removal estimate

For one labelled prime \(q\), let \(Y\ge q\), \(x=\sqrt Y\), and
\(a=3-c\). Then

\[
\begin{aligned}
&|4x-3+z|^2
-q|4x/\sqrt q-3+z|^2\\
&\qquad=
(\sqrt q-1)
\left[
8ax-(\sqrt q+1)(a^2+d^2)
\right].
\end{aligned}
\tag{L-100510.3}
\]

Since \(x\ge\sqrt q\) and

\[
\frac{8\sqrt q}{\sqrt q+1}
\ge
\frac{8\sqrt2}{\sqrt2+1}
=
16-8\sqrt2=C,
\]

condition (L-100510.2) makes (L-100510.3) nonnegative. Therefore removing a
label gives

\[
\frac{w_z(A)}{w_z(A\setminus\{q\})}
\le
q^{-3/2}.
\tag{L-100510.4}
\]

The labelled mass bound is elementary.  Every prime \(p\ge5\) is congruent
to \(1\) or \(-1\) modulo \(6\), so monotone integral comparison gives

\[
\begin{aligned}
\sum_p p^{-3/2}+67^{-3/2}
\le{}&
2^{-3/2}+3^{-3/2}+5^{-3/2}+7^{-3/2}\\
&+\frac13\left(5^{-1/2}+7^{-1/2}\right)
+67^{-3/2}\\
<{}&0.967<1.
\end{aligned}
\tag{L-100510.5}
\]

For each Euler level \(M_k\), summing (L-100510.4) over the \(k\) possible
parent edges gives

\[
kM_k
\le
\left(\sum_p p^{-3/2}+67^{-3/2}\right)M_{k-1}
<
M_{k-1}.
\]

Pairing levels \(M_0-M_1+M_2-M_3+\cdots\) therefore gives

\[
\boxed{
Q_z(X)\ge0
\qquad
(X\ge1,\ z\text{ satisfying (L-100510.2)}).
}
\tag{L-100510.6}
\]

The theorem is Hermitian and genuinely stronger than real shifted positivity.
It supplies a disk of complex test vectors, not merely a list of scalar
inequalities.
