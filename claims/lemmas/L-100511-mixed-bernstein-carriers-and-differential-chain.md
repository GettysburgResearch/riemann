# L-100511 — Every mixed Bernstein carrier is positive, yielding a differential Harnack chain

Claim ID: `L-100511`
Status: **PROVED EXACT ALL-ORDER SOURCE THEOREM**
Created: 2026-08-20
Depends on: the labelled prime-mass theorem used by PR #673
RH status: **not assumed**

Put

\[
S_-(y)=4(\sqrt y-1)\mathbf1_{y\ge1},
\qquad
S_+(y)=4\sqrt y\,\mathbf1_{y\ge1}.
\]

For nonnegative integers \(a,b\) with \(a+b=m\ge2\), define

\[
Q_{a,b}(X)
=
\sum_{n\ge1}
\frac{\beta(n)}{\sqrt n}
S_-(X/n)^aS_+(X/n)^b.
\tag{L-100511.1}
\]

If a labelled prime \(q\) is removed from an active subset, then

\[
\frac{S_-(Y/q)}{S_-(Y)}
\le q^{-1/2},
\qquad
\frac{S_+(Y/q)}{S_+(Y)}
=q^{-1/2}.
\]

Hence the weight ratio is at most

\[
q^{-(m+1)/2}.
\]

Since \(m\ge2\),

\[
\sum_p p^{-(m+1)/2}+67^{-(m+1)/2}<1.
\]

Adjacent-level pairing gives

\[
\boxed{
Q_{a,b}(X)>0
\qquad(X>1,\ a+b\ge2).
}
\tag{L-100511.2}
\]

For \(t=(c+1)/4\in[0,1]\),

\[
T(y)+c
=
(1-t)S_-(y)+tS_+(y).
\]

Thus every shifted power of total degree \(m\ge2\) is a positive Bernstein
mixture of the \(Q_{a,b}\).

## Differential chain at degree two

Define

\[
G_0(u)=e^{-u}Q_{2,0}(e^u),
\qquad
G_1(u)=e^{-u}Q_{1,1}(e^u),
\qquad
G_2(u)=e^{-u}Q_{0,2}(e^u).
\]

All three are nonnegative. Away from activation points,

\[
\frac{d}{du}S_-(e^u)=\frac12S_+(e^u),
\qquad
\frac{d}{du}S_+(e^u)=\frac12S_+(e^u).
\]

The activation-zero factor \(S_-\) removes distributional atoms from
\(G_0\). Direct differentiation gives

\[
\boxed{
G_1=G_0+G_0',
}
\tag{L-100511.3}
\]

and

\[
\boxed{
G_2=G_0+3G_0'+2G_0''.
}
\tag{L-100511.4}
\]

Consequently

\[
G_0\ge0,
\qquad
G_0+G_0'\ge0,
\qquad
G_0+3G_0'+2G_0''\ge0.
\tag{L-100511.5}
\]

The critical linear scalar is

\[
L_-(X)
=
\sum_{n\le X}
\frac{\beta(n)}{\sqrt n}S_-(X/n),
\]

and

\[
G_0'(u)=4e^{-u}L_-(e^u).
\tag{L-100511.6}
\]

Thus the entire shifted quadratic family becomes one positive differential
Harnack chain around the activation-free critical observable.
