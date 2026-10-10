# Causal removal of the auxiliary Hecke factor: an exact cost

**Status:** proposed component lemma, 10 October 2026. Complete proofs are given for an abstract causal dilation operator. No new zero-free region follows from this note alone.

**Scope:** ideal sums over the fixed Eisenstein field, their Mellin multipliers, and the principal correction identified in [TAIL_AND_EULER.md](TAIL_AND_EULER.md). The operator is not asserted to satisfy the full physical-probe interfaces in the imported manuscript.

**Exact dependencies:** finite ideal convolution; the elementary bound that the number of integral ideals of norm at most (X) is (O(X)) in this fixed field; the explicitly proved Euler factorization in this packet. The conditional version states its additional summatory hypothesis. The connection to the repository's causal program respects the endpoint restriction in [the frozen integrated account](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/research/integrated/CURRENT_RESULTS.md#causal).

**What was run:** exact rational exponent calculations and finite Dirichlet-convolution controls in `checks/check_research_algebra.py`. They check identities, not infinite cancellation.

**Smallest missing gain:** cancellation for the actual infinite-order angular Hecke character, together with a physical-probe and initial-data adapter if this operator is used in the imported argument.

## 1. Why this operator is relevant

At the principal residue, the September 30 correction has the exact factorization

\[
H_\eta(s)=\frac{L_K^S(6s-3,\chi_\eta)}{\zeta_K^S(2)}K_\eta(s),
\qquad \chi_\eta=\bar\alpha^6\eta^6.
\]

Here \(K_\eta\) is holomorphic and nonvanishing in \(\Re s>1/2\). The character \(\chi_\eta\) has nontrivial angular type; it is an infinite-order character. The imported finite-order quasi-RH theorem therefore cannot be applied to it just by renaming the character.

One natural idea is to remove this extra (L)-factor from the signal by a causal inverse. The calculation below shows precisely what that costs in a weighted space. It connects the Euler factorization to the repository's existing work on causal filters, without importing that program's line-one bound into an unproved half-plane.

## 2. Exact causal operator and Mellin multiplier

Let \(\chi\) be a unitary Hecke character away from a fixed finite set \(S\), and write

\[
a(\mathfrak n)=\mu_K(\mathfrak n)\chi(\mathfrak n),
\qquad (\mathfrak n,S)=1.
\]

Fix a real number \(c\). For a function \(F\) defined on \([1,\infty)\), extended by zero on \((0,1)\), define

\[
(\mathcal D_{c,\chi}F)(Z)
=\sum_{N\mathfrak n\le Z^{1/6}}
a(\mathfrak n)(N\mathfrak n)^{3-6c}
F\!\left(\frac{Z}{(N\mathfrak n)^6}\right),
\qquad Z\ge1.
\tag{2.1}
\]

Every argument on the right is at most \(Z\), so the operator is causal on the logarithmic scale. The sum is finite for each \(Z\). If \(|F(Z)|\le C Z^a\), its one-sided Mellin transform obeys

\[
\int_1^\infty (\mathcal D_{c,\chi}F)(Z)Z^{-w}\,\frac{dZ}{Z}
=\frac{1}{L_K^S(6w+6c-3,\chi)}
\int_1^\infty F(Z)Z^{-w}\,\frac{dZ}{Z}
\tag{2.2}
\]

for \(\Re w>\max\{a,2/3-c\}\). Indeed the substitution
\(Z=(N\mathfrak n)^6U\) contributes the factor
\((N\mathfrak n)^{3-6c-6w}\), whose absolute sum converges there. Fubini then gives (2.2).

The inverse operator is obtained by replacing \(\mu_K\chi\) with \(\chi\). Their composition is the identity on every finite causal horizon, since

\[
(\mu_K\chi)*\chi=\delta.
\]

Thus the algebraic inverse is exact. Its existence alone says nothing about boundedness on a chosen weighted space.

## 3. The exact threshold for the absolute estimate

Let \(|F(Z)|\le C Z^a\) for \(Z\ge1\), and put \(s_0=c+a\). From (2.1),

\[
|\mathcal D_{c,\chi}F(Z)|
\le C Z^a
\sum_{N\mathfrak n\le Z^{1/6}}
(N\mathfrak n)^{-(6s_0-3)}.
\tag{3.1}
\]

Counting ideals and applying partial summation proves

\[
|\mathcal D_{c,\chi}F(Z)|\ll_{c,a,S} C
\begin{cases}
Z^a,&s_0>2/3,\\
Z^a(1+\log Z),&s_0=2/3,\\
Z^{2/3-c},&s_0<2/3.
\end{cases}
\tag{3.2}
\]

For example, when \(6s_0-3<1\), the sum in (3.1) is
\(O(Z^{(4-6s_0)/6})\), giving the last line. The other cases are the convergent and logarithmic endpoints of the same integral. No cancellation has been used.

The published signal normalization is \(C(s)=s-11/16\). With \(c=11/16\),

\[
2/3-c=-1/48.
\]

Therefore this absolute causal inversion preserves a signal power \(a\) only above \(-1/48\), corresponding exactly to \(s_0>2/3\). Below that line, (3.2) introduces a \(Z^{-1/48}\) bound. This matches the absolute Euler-product threshold of the auxiliary \(L(6s-3,\chi)\).

This is a limitation of the displayed absolute argument. It does not rule out a sharper estimate using the actual arithmetic signs. In particular, finite invertibility must not be mistaken for a half-plane norm bound.

## 4. What an actual angular cancellation input would buy

Suppose, additionally, that for some \(\theta\ge0\) and every \(\epsilon>0\),

\[
A_\chi(X):=\sum_{N\mathfrak n\le X}a(\mathfrak n)
\ll_{\chi,S,\epsilon}X^{\theta+\epsilon}.
\tag{4.1}
\]

Assume \(F\in C^1([1,\infty))\) and

\[
|F(U)|+|UF'(U)|\le C U^a.
\tag{4.2}
\]

Abel summation applied to
\(f_Z(x)=x^{3-6c}F(Z/x^6)\), on \(1\le x\le Z^{1/6}\), gives

\[
|f_Z(x)|\le C Z^a x^{3-6(c+a)},
\quad |f'_Z(x)|\le C'_{c,a}Z^a x^{2-6(c+a)}.
\]

Using (4.1) in the endpoint term and the resulting integral proves that the operator preserves \(O(Z^a)\) whenever

\[
6(c+a)>3+\theta+\epsilon.
\]

Since \(\epsilon\) can be chosen after a fixed strict gap, the corresponding open domain is

\[
s_0=c+a>\frac{3+\theta}{6}.
\tag{4.3}
\]

The same proof gives a logarithm at equality with an exact bound \(A_\chi(X)=O(X^\theta)\), and a floor \(Z^{(3+\theta+\epsilon)/6-c}\) below it. All constants can depend on the fixed gap and on the fixed character; no uniform height estimate is implicit.

| Assumed angular summatory exponent | Domain in which this argument preserves the source power |
|---|---|
| \(\theta=1\), the trivial counting scale | \(\Re s>2/3\) |
| \(\theta=7/8\), if separately proved for this character | \(\Re s>31/48\) |
| \(\theta=1/2\), square-root cancellation up to arbitrary small powers | \(\Re s>7/12\) |

The middle and last rows are conditional. Even the square-root input for the angular inverse does not by this route push the multiplier inversion all the way to \(1/2\). Its nontrivial zeros at auxiliary argument \(6s-3\) remain a genuine issue for inverse continuation.

## 5. Conditions still needed for use in the imported proof

Equation (2.2) is an exact one-sided transform identity. The imported Gaussian signal uses its own Mellin convention, normalization and full physical expression. To use this operator there, one must carry the lower cutoff contribution and the correction through both the low and high representations of the *same* probe. A transform identity for the principal residue does not by itself accomplish that.

The useful conclusion is a specific interface: the extra Euler factor has an explicit causal inverse, and its weighted cost agrees with the analytic obstruction found independently by factorization. Further progress requires either an estimate for this actual angular source, a compensation that removes the factor before the problematic continuation, or a detector that can tolerate and separate its zeros. None of those inputs is assumed here.
