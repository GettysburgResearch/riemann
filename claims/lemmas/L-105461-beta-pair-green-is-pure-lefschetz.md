# L-105461 — The Beta pair Green operator is the pure-Lefschetz minimum-energy owner

Claim ID: `L-105461`

Status: **PROVED EXACT CODIMENSION-TWO INCIDENCE/HODGE THEOREM**

Let \(\mathscr C^{(k)}_{\mathcal P}\) be the degree-\(k\) part of the
prime-box Chow algebra.  For a monomial \(h_S\), \(|S|=k\ge2\), define the
unordered-pair marking map

\[
\delta_2h_S
 =
 \sum_{\substack{P\subset S\\|P|=2}}
 e_P\otimes h_{S\setminus P}.
\tag{L-105461.1}
\]

Let \(m_2\) forget the mark and recombine the pair with its complementary
support.  Then

\[
\boxed{
m_2\delta_2h_S=\binom{k}{2}h_S.
}
\tag{L-105461.2}
\]

If \(N\) is the degree operator, define on degrees at least two

\[
\boxed{
\mathcal G_2
 =
 \delta_2\binom{N}{2}^{-1}.
}
\tag{L-105461.3}
\]

Equation (L-105461.2) gives

\[
\boxed{m_2\mathcal G_2=I.}
\tag{L-105461.4}
\]

Thus \(\mathcal G_2\) is the exact codimension-two incidence Green operator.

## 1. Beta realization

For one support of depth \(k\),

\[
2\int_0^1(1-\theta)\theta^{k-2}\,d\theta
 =
 \frac{2}{k(k-1)}
 =
 \frac1{\binom{k}{2}}.
\tag{L-105461.5}
\]

Consequently the Beta pair allocation in `L-106133` is exactly
\(\mathcal G_2\), not merely an asymptotically comparable owner rule.

## 2. Exact minimum norm

Give the marked-pair fibres the free orthonormal norm.  An owner allocation
\((w_P)_{P\in\binom S2}\) which recombines to a scalar \(c\) satisfies

\[
\sum_Pw_P=c.
\]

Cauchy gives

\[
\sum_P|w_P|^2
 \ge
 \frac{|c|^2}{\binom{k}{2}},
\tag{L-105461.6}
\]

with equality if and only if

\[
w_P=\frac{c}{\binom{k}{2}}
\quad\hbox{for every }P.
\]

Hence the canonical equal-pair gauge is the unique minimum-energy right
inverse of physical recombination.  A deterministic pair has norm
\(|c|^2\), so the exact free-owner norm ratio is

\[
\boxed{\binom{k}{2}.}
\tag{L-105461.7}
\]

This sharpens the earlier \(O(\log^2Y)\) transfer cost.

## 3. Lefschetz, star, and primitive components

Fix \(k\ge3\) labels and let

\[
V_2=\mathbf R^{\binom{k}{2}}.
\]

Let \(B\) be the unsigned vertex-edge incidence matrix of the complete graph:
the column of \(\{i,j\}\) is \(e_i+e_j\).  Then

\[
BB^T=(k-2)I+J.
\tag{L-105461.8}
\]

The orthogonal Hodge splitting is

\[
V_2
 =
 \underbrace{\mathbf R\mathbf 1}_{\text{constant Lefschetz}}
 \oplus
 \underbrace{B^T(\mathbf 1^\perp)}_{\text{shared-owner stars}}
 \oplus
 \underbrace{\ker B}_{\text{primitive cycles}}.
\tag{L-105461.9}
\]

The equal-pair vector \(\binom{k}{2}^{-1}\mathbf1\) lies entirely in the first
summand.  Its star and primitive projections vanish exactly.

For comparison, let \(\delta_e\) be one deterministic edge owner.  Its
squared projection norms are

\[
\boxed{
\begin{aligned}
\|\operatorname{proj}_{\rm const}\delta_e\|^2
 &=\frac1{\binom{k}{2}},\\
\|\operatorname{proj}_{\rm star}\delta_e\|^2
 &=\frac2k,\\
\|\operatorname{proj}_{\rm prim}\delta_e\|^2
 &=\frac{k-3}{k-1}.
\end{aligned}}
\tag{L-105461.10}
\]

They sum to one.  In particular, an extreme-pair owner is asymptotically almost
entirely primitive, whereas the canonical Beta owner is pure Lefschetz.

## Consequence for checkpoint four

The star/cycle decomposition in `L-105431` is exact for a chosen pair-owner
tensor.  This lemma shows that its source-level star and primitive debts are
not intrinsic to the complete Boolean source: they are created by
concentrating the owner.  The canonical equal-pair gauge removes both before
physical observation.

This does **not** prove physical contraction.  Different source supports still
collapse to nearby multiplicative translations; that remaining obstruction is
identified in `L-105462--L-105463`.
