# L-100200 — The quadratic-envelope source is exactly conjugate to the native critical Euler geometry

Claim ID: `L-100200`  
Status: **PROVED EXACT SOURCE/OPERATOR IDENTITY**  
Created: 2026-08-20  
Inputs: PR #672, `L-99980--L-99981`  
RH status: **not assumed**

Let

\[
f(y)=
\begin{cases}
16,&0<y<1,\\
24y^{-1/2}-9y^{-1},&y\ge1,
\end{cases}
\]

so that PR #672 writes

\[
\frac{\mathcal E_2(X)}{X}
=
\sum_{n\ge1}\frac{\beta(n)}{n^{3/2}}f(X/n).
\tag{L-100200.1}
\]

Here `beta` is represented by one labelled copy of every prime and a second
labelled copy of \(67\).

## 1. Exact half-order conjugation

Put

\[
\widetilde f(y)=\sqrt y\,f(y)
=
\begin{cases}
16\sqrt y,&0<y<1,\\
24-9y^{-1/2},&y\ge1.
\end{cases}
\tag{L-100200.2}
\]

For \(U_qF(y)=F(y/q)\),

\[
\boxed{
(I-q^{-3/2}U_q)f(y)
=
y^{-1/2}(I-q^{-1}U_q)\widetilde f(y).
}
\tag{L-100200.3}
\]

The factors commute, hence for every finite labelled block \(B\),

\[
\boxed{
\prod_{q\in B}(I-q^{-3/2}U_q)f(y)
=
y^{-1/2}
\prod_{q\in B}(I-q^{-1}U_q)\widetilde f(y).
}
\tag{L-100200.4}
\]

Thus the apparently summable \(q^{-3/2}\) source becomes the critical
prime-harmonic \(q^{-1}\) source after the exact normalization used by the
conclusion-facing scalar.

The one-prime block remains positive. Indeed
\(\widetilde f(y/q)\le\widetilde f(y)\) for every \(q\ge2\). The only
nontrivial regime is \(1\le y<q\). Writing \(t=\sqrt y\) and
\(s=\sqrt q\), the required inequality is

\[
16t^2\le24st-9s.
\]

The right-minus-left side is concave in \(t\), so it is enough to check
\(t=1\) and \(t=s\); these reduce to \(16\le15s\) and \(9\le8s\).

## 2. Monotone part plus one critical step

Define

\[
G(y)=
\begin{cases}
16\sqrt y,&0<y<1,\\
25-9y^{-1/2},&y\ge1,
\end{cases}
\qquad
H(y)=\mathbf1_{y\ge1}.
\tag{L-100200.5}
\]

Then

\[
\boxed{\widetilde f=G-H.}
\tag{L-100200.6}
\]

The function \(G\) is continuous, nonnegative and strictly increasing on
\((0,\infty)\). For a finite labelled Euler block with activities \(1/q\), the
exact priority-Hasse flow therefore gives

\[
\prod_{q\in B}(I-q^{-1}U_q)G(y)\ge0.
\tag{L-100200.7}
\]

The step part is the literal reciprocal prefix:

\[
\prod_{q\in B}(I-q^{-1}U_q)H(y)
=
\sum_{\substack{A\subseteq B\\q_A\le y}}
\frac{(-1)^{|A|}}{q_A}.
\tag{L-100200.8}
\]

Passing through the absolutely convergent finite-\(B\) limit appropriate to
(L-100200.1) gives

\[
\boxed{
\frac{\mathcal E_2(X)}{\sqrt X}
=
\mathcal G(X)-A_\beta(X),
\qquad
\mathcal G(X)\ge0,
\qquad
A_\beta(X)=\sum_{n\le X}\frac{\beta(n)}n.
}
\tag{L-100200.9}
\]

Equation (L-100200.9) identifies the exact critical content of the quadratic
envelope. All smooth monotone mass is positively transportable. The sole
nonmonotone datum is the activation step, whose Euler projection is the native
reciprocal prefix.

This theorem neither refutes nor proves the finite activation gate
`FEAG99980`. It proves that a proof based only on summability of the
\(q^{-3/2}\) labels cannot close that gate: after the required half-order
conjugation the live source is \(q^{-1}\).
