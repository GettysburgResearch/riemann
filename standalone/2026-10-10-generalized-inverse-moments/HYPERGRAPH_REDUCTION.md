# An all-order decomposition with only logarithmic overlap cost

**Status:** proved finite identities and a proved conditional reduction. The short-row analytic moment is not proved.

**Scope:** every fixed integer moment order, the exact inverse/sextic coefficients over the Eisenstein field, all rows including local zeros, and fixed compact smooth tests. Constants may depend on the fixed moment order.

**Dependencies:** the character conventions in the imported October 5 `paper2.tex`, equations `eq:intro-family` and `eq:ms`; the fourth-moment reduction in PR #910 at `670a76c1a3a8f325c43c1755b1cfc24d313a3e3c`; unique factorization of ideals, Minkowski's inequality, and elementary ideal counting. The imported quasi-Riemann analytic theorems are not used in this reduction.

## 1. The actual target and the smaller coefficient family

Put \(K=\mathbb Q(\sqrt{-3})\). Ideal norms are denoted by \(N\), \(S\) is a fixed finite set of prime ideals containing those above 2 and 3 and the conductor of a fixed finite-order character \(\nu\), and

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\tag{1.1}
\]

Here \(\chi_n(u)=(u/n)_6\) uses the source's primary generators and is zero if \((n,u)\ne1\). Rows are nonzero Eisenstein integers, as in the source. All ensuing arguments also apply to any subset of rows.

For fixed \(k\ge1\), the desired estimate is

\[
M_{2k}(D,H;W):=\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{k,\nu,S,W,\theta,\epsilon}H D^{k+\epsilon},
\qquad H=D^{1+\theta},\quad 0<\theta\le1/10.
\tag{1.2}
\]

Let \(W_1,\ldots,W_k\) be fixed smooth functions supported in a common interval \([a,b]\subset(0,\infty)\), with \(b\ge1\). The larger upper endpoint can always be chosen without changing the tests. For a squarefree ideal \(Q\) prime to \(S\) define the rectangular, pairwise-coprime sum

\[
\begin{split}
B_{Q,u}(\mathbf X;\mathbf W)
={}&\sum_{\substack{a_1,\ldots,a_k\ \mathrm{squarefree}\\
(a_i,a_j)=1\ (i\ne j)\\(a_1\cdots a_k,QS)=1}}
\prod_{i=1}^k\mu_K(a_i)\nu(a_i)W_i(Na_i/X_i)
\;\chi_{a_1\cdots a_k}(u).
\end{split}
\tag{1.3}
\]

Its product column is squarefree. Equivalently,

\[
B_{Q,u}(\mathbf X;\mathbf W)
=\sum_{\substack{r\ \mathrm{squarefree}\\(r,QS)=1}}
\mu_K(r)\nu(r)\chi_r(u)\,
\mathcal W_{\mathbf X}(r),
\tag{1.4}
\]

where the exact allocation weight is

\[
\mathcal W_{\mathbf X}(r)
=\sum_{a_1\cdots a_k=r}\prod_{i=1}^k W_i(Na_i/X_i).
\tag{1.5}
\]

Since \(r\) is squarefree, every factorization in (1.5) is automatically pairwise coprime. For nonnegative tests all allocations have the same Möbius sign; there is no cancellation within this coefficient. Replacing it by an arbitrary divisor-bounded weight is not an established extension of the imported theorem and can lead to a false stronger statement; see `LONG_ROW_AND_OBSTRUCTION.md`.

## 2. Exact prime-incidence decomposition

Write \([k]=\{1,\ldots,k\}\), and let \(\mathcal I_k\) be the collection of its subsets with at least two elements. For each \(I\in\mathcal I_k\), choose a squarefree ideal \(q_I\), with all \(q_I\) pairwise coprime and prime to \(S\). Unit ideals are allowed. Put

\[
Q=\prod_{I\in\mathcal I_k}q_I,\qquad
c_i=\prod_{\substack{I\in\mathcal I_k\\i\in I}}q_I,\qquad
X_i=D/Nc_i.
\tag{2.1}
\]

For every row \(u\), the following identity is exact:

\[
\boxed{
\prod_{i=1}^k A_u(D;W_i)
=\sum_{\mathbf q}
\left\{\prod_{I\in\mathcal I_k}
\mu_K(q_I)^{|I|}\nu(q_I)^{|I|}\chi_{q_I}(u)^{|I|}\right\}
B_{Q,u}(X_1,\ldots,X_k;\mathbf W).
}
\tag{2.2}
\]

Only choices with every \(Nc_i\le bD\) can contribute, so the sum is finite. In particular \(Nq_I\le bD\) for every nonunit \(q_I\). Also

\[
NQ\le\prod_{I}(Nq_I)^{|I|/2}
=\left(\prod_i Nc_i\right)^{1/2}\le(bD)^{k/2}.
\tag{2.3}
\]

**Proof.** Expand the product on the left into squarefree tuples \((n_1,\ldots,n_k)\). For each prime ideal occurring in the tuple let \(I\subseteq[k]\) be the exact set of factors containing it. If \(|I|\ge2\), place it in \(q_I\). If \(I=\{i\}\), place it in \(a_i\). This is a bijection between the original tuples and the choices of \(\mathbf q\) and singleton ideals \(a_i\) in (1.3). The ideal \(n_i\) equals \(c_i a_i\), and all prime sets in this representation are disjoint except for the intended incidence between different \(c_i\).

Consequently each prime in \(q_I\) contributes precisely \(|I|\) copies of its Möbius sign, character value, and sextic symbol. The smooth factor becomes \(W_i(Na_i/(D/Nc_i))\). These are exactly the factors on the right of (2.2). The equalities remain true at a row divisible by an occurring prime because the corresponding character factors are zero on both sides. This proves the identity and its support restrictions. Inequality (2.3) uses \(|I|\ge2\). \(\square\)

### A necessary convention when \(k\ge6\)

If \(|I|=6\), then \(\chi_{q_I}(u)^6\) equals \(\mathbf1_{(q_I,u)=1}\), rather than the constant function one. More generally a zero-extended character raised to a positive multiple of six retains its coprimality mask. Identity (2.2) does not replace this factor by one. It is bounded by one only after a row norm is taken.

For \(k=2\), there is one repeated factor \(q_{\{1,2\}}=\gcd(n_1,n_2)\). Formula (2.2) recovers exactly the previous fourth-moment identity. For \(k=3\), it has the four repeated factors \(q_{12},q_{13},q_{23},q_{123}\). They represent exact incidence, not the pairwise gcds, which would incorrectly count the triple overlap multiple times.

## 3. A sufficient estimate with a quantified overlap cost

Fix \(k\), the tests, and \(0<\theta\le1/10\). Suppose that for every \(\epsilon>0\), for all \(D\ge2\), at the single common row range \(H=D^{1+\theta}\),

\[
\|B_{Q,\cdot}(\mathbf X;\mathbf W)\|_{\ell^2(0<Nu\le H)}
\ll D^\epsilon H^{1/2}\prod_{i=1}^k X_i^{1/2}
\tag{3.1}
\]

uniformly for \(1/b\le X_i\le D\) and squarefree \(Q\) prime to \(S\) with \(NQ\le(bD)^{k/2}\). The implied constant is independent of the moving \(Q\) and the \(X_i\). Sums with any \(X_i<1/b\) vanish identically and need no estimate.

**The analytic assertion (3.1) is open.** It keeps the original common \(H\) when any \(X_i\) becomes smaller. Bounds at separate row lengths \(X_i^{1+\theta}\) are not a substitute.

Then

\[
\left\|\prod_{i=1}^k A_{\cdot}(D;W_i)\right\|_{\ell^2(0<Nu\le H)}
\ll D^\epsilon H^{1/2}D^{k/2}
(1+\log D)^{\binom{k}{2}}.
\tag{3.2}
\]

For identical \(W_i=W\), squaring and choosing a smaller input loss gives (1.2).

**Proof.** Multiplication by each external character factor in (2.2) is a contraction on the row Hilbert space. Apply Minkowski and (3.1). Since

\[
\prod_i X_i^{1/2}
=D^{k/2}\prod_{I\in\mathcal I_k}(Nq_I)^{-|I|/2},
\tag{3.3}
\]

the remaining norm is at most \(D^\epsilon H^{1/2}D^{k/2}\) times

\[
\sum_{\mathbf q}\prod_I(Nq_I)^{-|I|/2}.
\tag{3.4}
\]

Discarding pairwise coprimality, squarefreeness, and the joint support restrictions only enlarges this nonnegative sum. For each of the \(\binom{k}{2}\) subsets of size two, keep \(Nq_I\le bD\) and use

\[
\sum_{Nq\le bD}(Nq)^{-1}\ll_{K,b}1+\log D.
\tag{3.5}
\]

For every subset of size at least three, extend its sum to all nonzero integral ideals and use the convergent Dedekind zeta value

\[
\sum_q(Nq)^{-|I|/2}=\zeta_K(|I|/2)<\infty.
\tag{3.6}
\]

There are finitely many such subsets for fixed \(k\). Thus (3.4) is \(O_{K,k,b}((1+\log D)^{\binom{k}{2}})\). This proves (3.2). Its square costs \((1+\log D)^{k(k-1)}\), which is absorbed into an arbitrarily small fixed power of \(D\). No uniformity as \(k\to\infty\) is asserted or needed for this fixed-order implication. \(\square\)

## 4. Removing the moving exclusion from the remaining problem

The companion `MASKS_AND_EULER_FACTORS.md` proves a further adapter. Enlarge the fixed set \(S\), for this fixed \(k\), to contain the finitely many prime ideals with \(Np\le4k^2\). If (3.1) is known for \(Q=1\), with all the displayed rectangular smaller scales and the same common \(H\), then it holds for the required moving \(Q\) at a \((NQ)^\delta\) cost for every \(\delta>0\). By (2.3), that cost is absorbed into \(D^\epsilon\).

The exact local inverse is

\[
\frac1{1-z_1-\cdots-z_k}
=\sum_{e_1,\ldots,e_k\ge0}
\binom{e_1+\cdots+e_k}{e_1,\ldots,e_k}\prod_i z_i^{e_i}.
\tag{4.1}
\]

At the square-root norm weights, the resulting local norm cost is

\[
(1-k/\sqrt{Np})^{-1}.
\tag{4.2}
\]

For \(Np>4k^2\) this is well defined. For any fixed \(\delta>0\), it is at most \((Np)^\delta\) for all sufficiently large \(Np\). The finitely many remaining permitted primes contribute only a fixed constant, so the product over \(p\mid Q\) is \(\ll_{k,\delta}(NQ)^\delta\).

Enlarging \(S\) does not lose the original fixed small primes: restore each one by its finite set of incidence allocations among the original \(k\) squarefree factors. This produces finitely many norm dilations and bounded row phases. All required dilations are covered by the rectangular scale range; constants may depend on the finite set and on \(k\). The source's omitted Euler factors are also nonzero in \(\Re s>0\), so fixing these extra exclusions does not weaken the intended zero-free implication.

The resulting focused analytic target is therefore **unmasked rectangular squarefree allocation sums**. The overlap and moving-exclusion arguments are complete. The uniform mean-square bound for these unmasked sums is not.

## 5. What the decomposition establishes

Every repeated-prime pattern at every fixed order has been accounted for. Pair overlaps have a harmonic cost; larger overlaps have absolutely convergent cost. Higher-order overlaps therefore create no additional power loss once the correctly normalized singleton estimate is available. The same argument preserves all local zero extensions, including principal masks at multiples of six.

This is a theorem about the algebraic and summation structure of the generalized moment. It is not a proof of the off-diagonal cancellation needed for the short-row estimate. In particular, the all-order theorem cannot be concluded by replacing the remaining exact allocation weights by arbitrary coefficients or by enlarging smaller row ranges without an estimate.
