# L-99281 — The alpha-only factor-67 resolvent preserves Mellin-holomorphic subpower defects

Claim ID: `L-99281`  
Status: **PROVED EXACT ABSTRACT TREE/ANALYTIC THEOREM**  
Created: 2026-08-20  
RH status: **not assumed**

## 1. The natural defect class

Let

\[
\mathscr H_0
=
\left\{
f:[1,\infty)\to\mathbb C:
\forall\varepsilon>0,\
|f(X)|\le C_\varepsilon X^\varepsilon
\right\}.
\tag{L-99281.1}
\]

Every bounded or polylogarithmic function belongs to `H_0`.

If \(f\in\mathscr H_0\), then

\[
\widehat f(s)
=
\int_1^\infty f(X)X^{-s-1}\,dX
\]

converges absolutely and locally uniformly for every \(\Re s>0\): on a compact
half-plane \(\Re s\ge\sigma>0\), choose \(\varepsilon=\sigma/2\). Hence

\[
\boxed{
f\in\mathscr H_0
\Longrightarrow
\widehat f\text{ is holomorphic on }\Re s>0.
}
\tag{L-99281.2}
\]

## 2. Source-owned tree resolvent

Let a typed root of endpoint \(X\) have mass at most \(M_0\). Only genuine
alpha-children recurse. Assume

\[
\sum_{w\succ v}m_w\le\kappa m_v,
\qquad
\kappa<\frac18,
\tag{L-99281.3}
\]

and, outside a fixed terminal region,

\[
Y_w\le Y_v/67+1\le qY_v
\qquad(q<1).
\tag{L-99281.4}
\]

For example \(q=35/67\) works for \(Y_v\ge2\); the remaining endpoints form a
fixed terminal set.

Suppose the source-owned local calibration in one fixed component row satisfies,
for every \(\varepsilon>0\),

\[
|C_v(j)|
\le
A_{\varepsilon,j}m_v(1+Y_v^\varepsilon).
\tag{L-99281.5}
\]

Define the fully resolved calibration by summing the actual one-owner tree:

\[
\mathfrak E_X(j)=\sum_v C_v(j).
\tag{L-99281.6}
\]

At depth \(\ell\), total source mass is at most \(M_0\kappa^\ell\), while every
nonterminal endpoint is at most \(q^\ell X\). Therefore

\[
\begin{aligned}
|\mathfrak E_X(j)|
&\le
A_{\varepsilon,j}M_0
\sum_{\ell\ge0}
\kappa^\ell
\left(1+q^{\varepsilon\ell}X^\varepsilon\right)\\
&\le
A_{\varepsilon,j}M_0
\left(
\frac1{1-\kappa}
+
\frac{X^\varepsilon}{1-\kappa q^\varepsilon}
\right).
\end{aligned}
\tag{L-99281.7}
\]

Thus

\[
\boxed{
\mathfrak E_\bullet(j)\in\mathscr H_0.
}
\tag{L-99281.8}
\]

This theorem remains valid for a positive endpoint measure inserted as a
virtual root, provided its total typed source mass is uniformly finite.

## 3. Why this repairs the fixed-row route

A proof no longer needs a sharp uniform constant for every knot, anchor or
finite/continuum term. It is enough to show, in the actual source ledger, that
each primitive calibration has subpower size per unit typed source. Compact
factor-67 terms, finite knot ledgers, bounded endpoint fibres, and
polylogarithmic corrections all qualify.

The same child kernel must carry the calibration and the positive current.
Separate coordinatewise trees are not covered.
